"""
AkashDristi ML Baseline Model Definition
File: ml/src/model.py
"""

import torch
import segmentation_models_pytorch as smp


# ==============================================================================
# Model Architecture & Rationale
# ==============================================================================
#
# # Model Architecture
# U-Net encoder-decoder network paired with a ResNet-34 backbone.
#
# # Why U-Net
# U-Net utilizes skip connections between the contracting encoder path and the
# expanding decoder path. This preserves fine-grained spatial and boundary details
# (essential for delineating building footprints) while retaining high-level
# contextual features.
#
# # Why ResNet34
# ResNet-34 provides a strong feature extraction capacity with residual connections
# that prevent vanishing gradients, maintaining an ideal balance between
# performance, model size, and computational efficiency for the baseline pipeline.
#
# # Why ImageNet pretrained weights
# Pretrained weights provide general visual representations (e.g., edges, textures,
# corners), accelerating convergence and boosting feature transfer on aerial imagery
# compared to random initialization.
#
# # Why 5 output classes
# Corresponds to standard disaster damage classification mapping (e.g., xBD taxonomy):
#   - Class 0: Background / Non-building
#   - Class 1: No Damage
#   - Class 2: Minor Damage
#   - Class 3: Major Damage
#   - Class 4: Destroyed
# ==============================================================================


# Device selection
def get_device() -> torch.device:
    """
    Returns CUDA device if available, otherwise CPU.
    Avoids hardcoding GPU device requirements.
    """
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def create_model() -> smp.Unet:
    """
    Instantiates and returns the baseline U-Net segmentation model.
    """
    model = smp.Unet(
        encoder_name="resnet34",
        encoder_weights="imagenet",
        in_channels=3,
        classes=5,
    )
    return model