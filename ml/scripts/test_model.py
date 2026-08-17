import sys
import torch

sys.path.insert(0, "ml")

from src.model import create_model, get_device


def main():
    device = get_device()

    print("Device:", device)

    if device.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(0))

    model = create_model()
    model = model.to(device)
    model.eval()

    # Dummy RGB image: batch=1, channels=3, height=256, width=256
    test_input = torch.randn(1, 3, 256, 256, device=device)

    with torch.no_grad():
        output = model(test_input)

    print("Input shape:", test_input.shape)
    print("Output shape:", output.shape)


if __name__ == "__main__":
    main()