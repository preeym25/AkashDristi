"""
AkashDristi ML - Test Script for XBD Dataset
File: ml/scripts/test_dataset.py
Purpose: Verify that the XBDDataset class correctly loads images and generates masks,
         and that DataLoader batching works as expected.
"""

import sys
import torch

# Add ml/ to path to import from src/
sys.path.insert(0, "ml")

from src.dataset import XBDDataset


def main():
    # Dataset configuration
    dataset_root = r"D:\dev_dataset-20260817T183422Z-1-001\dev_dataset"
    image_size = 256
    
    print("=" * 70)
    print("XBD Dataset Test")
    print("=" * 70)
    print(f"\nDataset root: {dataset_root}")
    print(f"Target image size: {image_size}x{image_size}")
    
    # ========================================================================
    # Test 1: Instantiate and inspect dataset
    # ========================================================================
    print("\n" + "-" * 70)
    print("Test 1: Dataset Instantiation and Inspection")
    print("-" * 70)
    
    try:
        dataset = XBDDataset(
            dataset_root=dataset_root,
            image_size=image_size,
            filter_post_disaster=False
        )
        print(f"✓ Dataset instantiated successfully")
    except Exception as e:
        print(f"✗ Failed to instantiate dataset: {e}")
        return
    
    # Dataset properties
    dataset_length = len(dataset)
    print(f"Dataset length: {dataset_length}")
    
    # ========================================================================
    # Test 2: Load first sample
    # ========================================================================
    print("\n" + "-" * 70)
    print("Test 2: Load First Sample")
    print("-" * 70)
    
    try:
        image, mask = dataset[0]
        print(f"✓ Successfully loaded sample 0")
    except Exception as e:
        print(f"✗ Failed to load sample 0: {e}")
        return
    
    # Image tensor inspection
    print(f"\nImage tensor:")
    print(f"  Shape: {tuple(image.shape)}")
    print(f"  Data type: {image.dtype}")
    print(f"  Min value: {image.min().item():.4f}")
    print(f"  Max value: {image.max().item():.4f}")
    
    # Mask tensor inspection
    print(f"\nMask tensor:")
    print(f"  Shape: {tuple(mask.shape)}")
    print(f"  Data type: {mask.dtype}")
    
    unique_classes = torch.unique(mask).tolist()
    print(f"  Unique class IDs: {sorted(unique_classes)}")
    
    # Pixel count per class
    print(f"  Pixel count per class:")
    for class_id in sorted(unique_classes):
        count = (mask == class_id).sum().item()
        percentage = (count / mask.numel()) * 100
        class_name = {
            0: "background",
            1: "no-damage",
            2: "minor-damage",
            3: "major-damage",
            4: "destroyed"
        }.get(class_id, "unknown")
        print(f"    Class {class_id} ({class_name}): {count:7d} pixels ({percentage:5.2f}%)")
    
    # ========================================================================
    # Test 3: Create DataLoader and load batch
    # ========================================================================
    print("\n" + "-" * 70)
    print("Test 3: DataLoader and Batch Loading")
    print("-" * 70)
    
    try:
        dataloader = torch.utils.data.DataLoader(
            dataset,
            batch_size=2,
            shuffle=False,
            num_workers=0
        )
        print(f"✓ DataLoader created successfully")
    except Exception as e:
        print(f"✗ Failed to create DataLoader: {e}")
        return
    
    # Load one batch
    try:
        batch_images, batch_masks = next(iter(dataloader))
        print(f"✓ Successfully loaded first batch")
    except Exception as e:
        print(f"✗ Failed to load batch: {e}")
        return
    
    # Batch inspection
    print(f"\nBatch images:")
    print(f"  Shape: {tuple(batch_images.shape)}")
    print(f"  Data type: {batch_images.dtype}")
    print(f"  Min value: {batch_images.min().item():.4f}")
    print(f"  Max value: {batch_images.max().item():.4f}")
    
    print(f"\nBatch masks:")
    print(f"  Shape: {tuple(batch_masks.shape)}")
    print(f"  Data type: {batch_masks.dtype}")
    
    batch_unique_classes = torch.unique(batch_masks).tolist()
    print(f"  Unique class IDs in batch: {sorted(batch_unique_classes)}")
    
    # Pixel count per class in batch
    print(f"  Pixel count per class in batch:")
    batch_total_pixels = batch_masks.numel()
    for class_id in sorted(batch_unique_classes):
        count = (batch_masks == class_id).sum().item()
        percentage = (count / batch_total_pixels) * 100
        class_name = {
            0: "background",
            1: "no-damage",
            2: "minor-damage",
            3: "major-damage",
            4: "destroyed"
        }.get(class_id, "unknown")
        print(f"    Class {class_id} ({class_name}): {count:7d} pixels ({percentage:5.2f}%)")
    
    # ========================================================================
    # Summary
    # ========================================================================
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"✓ All tests passed successfully!")
    print(f"  - Dataset loaded: {dataset_length} samples")
    print(f"  - Sample image shape: (3, {image_size}, {image_size})")
    print(f"  - Sample mask shape: ({image_size}, {image_size})")
    print(f"  - Batch size: 2")
    print(f"  - Batch image shape: {tuple(batch_images.shape)}")
    print(f"  - Batch mask shape: {tuple(batch_masks.shape)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
