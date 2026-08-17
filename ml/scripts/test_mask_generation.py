import sys
from pathlib import Path

import numpy as np
from PIL import Image

# Allow imports from ml/src
ML_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ML_DIR))

from src.mask_utils import create_damage_mask


DATASET_ROOT = Path(
    r"D:\dev_dataset-20260817T183422Z-1-001\dev_dataset"
)

IMAGES_DIR = DATASET_ROOT / "images"
LABELS_DIR = DATASET_ROOT / "labels"


def save_mask_visualization(mask, output_path):
    """
    Save a colorized visualization of the segmentation mask.

    Actual mask class IDs remain:

    0 = background
    1 = no damage
    2 = minor damage
    3 = major damage
    4 = destroyed
    """

    visual_mask = np.zeros(
        (mask.shape[0], mask.shape[1], 3),
        dtype=np.uint8
    )

    # Colors are only for visualization.
    visual_mask[mask == 1] = [255, 255, 255]   # No damage
    visual_mask[mask == 2] = [255, 255, 0]     # Minor damage
    visual_mask[mask == 3] = [255, 165, 0]     # Major damage
    visual_mask[mask == 4] = [255, 0, 0]       # Destroyed

    Image.fromarray(visual_mask).save(output_path)


def save_overlay(image_path, mask, output_path):
    """
    Overlay the damage mask on the original image.

    This is only for visual validation.
    It is NOT used as model training data.
    """

    # Load original image
    image = np.array(
        Image.open(image_path).convert("RGB")
    )

    # Create a copy for applying the mask colors
    colored_mask = image.copy()

    # Apply visualization colors
    colored_mask[mask == 1] = [255, 255, 255]   # No damage
    colored_mask[mask == 2] = [255, 255, 0]     # Minor damage
    colored_mask[mask == 3] = [255, 165, 0]     # Major damage
    colored_mask[mask == 4] = [255, 0, 0]       # Destroyed

    # Blend original image with colored mask
    blended = (
        0.6 * image.astype(np.float32)
        + 0.4 * colored_mask.astype(np.float32)
    ).astype(np.uint8)

    Image.fromarray(blended).save(output_path)


def main():

    # ---------------------------------------------------------
    # Select a known post-disaster image containing
    # multiple damage classes.
    # ---------------------------------------------------------

    image_path = (
        IMAGES_DIR /
        "socal-fire_00000525_post_disaster.png"
    )

    if not image_path.exists():
        raise FileNotFoundError(
            f"Image not found:\n{image_path}"
        )

    # ---------------------------------------------------------
    # Find matching JSON annotation
    # ---------------------------------------------------------

    json_path = LABELS_DIR / f"{image_path.stem}.json"

    if not json_path.exists():
        raise FileNotFoundError(
            f"Matching JSON not found:\n{json_path}"
        )

    # ---------------------------------------------------------
    # Read image dimensions
    # ---------------------------------------------------------

    with Image.open(image_path) as image:
        width, height = image.size

    print("Selected image:")
    print(image_path)

    print("\nMatching JSON:")
    print(json_path)

    print("\nImage dimensions:")
    print(f"Width: {width}")
    print(f"Height: {height}")

    # ---------------------------------------------------------
    # Generate segmentation mask
    # ---------------------------------------------------------

    mask = create_damage_mask(
        json_path,
        image_height=height,
        image_width=width,
    )

    # ---------------------------------------------------------
    # Print mask information
    # ---------------------------------------------------------

    print("\nMask information:")
    print("Shape:", mask.shape)
    print("Dtype:", mask.dtype)

    unique_classes = sorted(
        set(mask.flatten().tolist())
    )

    print("\nUnique class IDs:")
    print(unique_classes)

    print("\nPixel counts:")

    for class_id in range(5):
        count = int((mask == class_id).sum())
        print(f"Class {class_id}: {count}")

    # ---------------------------------------------------------
    # Save colorized mask
    # ---------------------------------------------------------

    mask_output_path = (
        Path(__file__).parent /
        "test_damage_mask.png"
    )

    save_mask_visualization(
        mask,
        mask_output_path
    )

    print("\nMask visualization saved to:")
    print(mask_output_path)

    # ---------------------------------------------------------
    # Save original image + mask overlay
    # ---------------------------------------------------------

    overlay_output_path = (
        Path(__file__).parent /
        "test_damage_overlay.png"
    )

    save_overlay(
        image_path,
        mask,
        overlay_output_path
    )

    print("\nOverlay saved to:")
    print(overlay_output_path)


if __name__ == "__main__":
    main()