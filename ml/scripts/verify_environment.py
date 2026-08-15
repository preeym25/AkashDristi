import platform


def main() -> None:
    print(f"Python version: {platform.python_version()}")

    try:
        import torch
    except ImportError as exc:
        print("PyTorch version: not installed")
        print(f"Import error: {exc}")
        return

    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        count = torch.cuda.device_count()
        print(f"GPU count: {count}")
        try:
            print(f"GPU: {torch.cuda.get_device_name(0)}")
        except Exception:
            print("GPU: CUDA is available but device name could not be read.")
    else:
        print("GPU: not detected")


if __name__ == "__main__":
    main()
