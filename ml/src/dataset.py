"""
AkashDristi ML - PyTorch Dataset for xBD Segmentation
File: ml/src/dataset.py
Purpose: Load xBD images and generate damage masks for segmentation training.
"""

import os
import torch
import cv2
import numpy as np
from pathlib import Path
from typing import Tuple, Optional
from PIL import Image

from .mask_utils import create_damage_mask


class XBDDataset(torch.utils.data.Dataset):
    """
    PyTorch Dataset for xBD building damage segmentation.
    
    This dataset loads RGB satellite images and their corresponding pixel-level
    damage masks from xBD annotations. Masks are generated on-the-fly using the
    create_damage_mask() function, which rasterizes building polygons from JSON
    annotations into 5-class segmentation maps.
    
    Attributes:
        image_size (int): Target size for images and masks (default 256x256).
        filter_post_disaster (bool): If True, load only post-disaster images.
                                      If False, load all images (default).
    
    Returns:
        Tuple[torch.Tensor, torch.Tensor]: (image, mask) where:
            - image: torch.float32, shape (3, H, W), values in [0, 1]
            - mask: torch.long, shape (H, W), class IDs in {0, 1, 2, 3, 4}
    
    Mask Class IDs (standard xBD damage taxonomy):
        0 = background / non-building
        1 = no damage
        2 = minor damage
        3 = major damage
        4 = destroyed
    
    Example:
        >>> dataset = XBDDataset(
        ...     dataset_root="D:/dev_dataset/dev_dataset",
        ...     image_size=256,
        ...     filter_post_disaster=True
        ... )
        >>> image, mask = dataset[0]
        >>> print(image.shape, mask.shape)  # (3, 256, 256), (256, 256)
    """
    
    def __init__(
        self,
        dataset_root: str,
        image_size: int = 256,
        filter_post_disaster: bool = False
    ):
        """
        Initialize the XBD dataset.
        
        Args:
            dataset_root (str): Path to the dataset root directory containing
                               'images/' and 'labels/' subdirectories.
            image_size (int): Target size for resized images and masks.
                            Default: 256 (produces 256x256 tensors).
            filter_post_disaster (bool): If True, load only post-disaster images
                                        (filenames containing "_post_disaster").
                                        If False, load all images.
                                        Default: False (load all).
        """
        self.dataset_root = Path(dataset_root)
        self.image_dir = self.dataset_root / "images"
        self.label_dir = self.dataset_root / "labels"
        self.image_size = image_size
        self.filter_post_disaster = filter_post_disaster
        
        # Validate directory structure
        if not self.image_dir.exists():
            raise FileNotFoundError(f"Images directory not found: {self.image_dir}")
        if not self.label_dir.exists():
            raise FileNotFoundError(f"Labels directory not found: {self.label_dir}")
        
        # Discover image files
        self.image_files = sorted([
            f for f in os.listdir(self.image_dir)
            if f.endswith('.png')
        ])
        
        # Apply filter for post-disaster images if requested
        if self.filter_post_disaster:
            self.image_files = [
                f for f in self.image_files
                if "_post_disaster" in f
            ]
        
        # Validate that all images have matching labels
        self._validate_image_label_pairs()
    
    def _validate_image_label_pairs(self) -> None:
        """
        Ensure each image has a matching JSON label file.
        Raises FileNotFoundError if any image lacks a corresponding label.
        """
        for image_file in self.image_files:
            label_file = image_file.replace('.png', '.json')
            label_path = self.label_dir / label_file
            
            if not label_path.exists():
                raise FileNotFoundError(
                    f"Missing label for image {image_file}: "
                    f"expected {label_path}"
                )
    
    def __len__(self) -> int:
        """
        Returns the number of image-label pairs in the dataset.
        """
        return len(self.image_files)
    
    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Load and preprocess an image-mask pair.
        
        Args:
            idx (int): Index of the sample to load.
        
        Returns:
            Tuple[torch.Tensor, torch.Tensor]:
                - image: torch.float32 tensor of shape (3, image_size, image_size)
                         with values scaled to [0, 1]
                - mask: torch.long tensor of shape (image_size, image_size)
                        containing class IDs {0, 1, 2, 3, 4}
        
        Raises:
            FileNotFoundError: If image or label file cannot be found or loaded.
            ValueError: If image is not RGB or has unexpected format.
        """
        # Get filenames
        image_file = self.image_files[idx]
        label_file = image_file.replace('.png', '.json')
        
        image_path = self.image_dir / image_file
        label_path = self.label_dir / label_file
        
        # Load image as RGB
        image = Image.open(image_path).convert('RGB')
        original_height, original_width = image.size[::-1]  # PIL returns (W, H)
        
        # Generate mask from annotations
        mask = create_damage_mask(str(label_path), original_height, original_width)
        
        # Resize image to target size (bilinear interpolation)
        image_np = cv2.resize(
            np.array(image),
            (self.image_size, self.image_size),
            interpolation=cv2.INTER_LINEAR
        )
        
        # Resize mask to target size (nearest-neighbor interpolation)
        mask_resized = cv2.resize(
            mask,
            (self.image_size, self.image_size),
            interpolation=cv2.INTER_NEAREST
        )
        
        # Convert image to torch.float32 in CHW format, scale to [0, 1]
        image_tensor = torch.from_numpy(image_np).permute(2, 0, 1).float() / 255.0
        
        # Convert mask to torch.long
        mask_tensor = torch.from_numpy(mask_resized).long()
        
        return image_tensor, mask_tensor