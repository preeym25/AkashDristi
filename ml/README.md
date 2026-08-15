# AkashDristi ML Setup

## Purpose

This folder is the ML workspace for the AkashDristi project. It is intended to hold the Python environment, safety checks, and future reusable ML code for the post-disaster damage mapping workflow.

The current scope is intentionally small and conservative. This setup does not claim that model training or inference is already implemented.

## Colab history and preservation

The xBD/xView2 dataset work for this project was already explored in Google Colab before this repository was structured. That work included:

- confirming the xBD dataset layout
- inspecting JSON annotation structure
- checking the building feature geometry and WKT conversion workflow
- visualizing building polygons over images
- inspecting damage classes
- matching pre/post image pairs
- creating a 200-pair development subset
- verifying image-label alignment

That exploration is valuable project knowledge and should be preserved as a source of reusable logic. The goal of this repository is to provide a clean place to migrate reusable ML code gradually, without copying the xBD dataset into GitHub.

## Dataset location

The xBD dataset is not stored in this repository and must remain outside GitHub.

The expected local pattern is a dataset directory kept on the machine outside the project repo, for example:

- C:/data/xbd
- D:/datasets/xbd
- another local non-Git folder of your choice

The repository should reference that external local dataset location, not include the data itself.

## Python version guidance

The local machine currently has Python 3.13.5 installed. That version is not the best default choice for a stable PyTorch setup in a laptop ML environment.

For this project, it is recommended to create a dedicated Python 3.12 virtual environment under `ml/.venv/` instead of modifying the system Python installation. This keeps the setup isolated and reduces risk to the machine.

## Create the virtual environment

From the repository root:

```powershell
cd C:\Users\loq\OneDrive\Desktop\AkashDristi\AkashDristi
python -m venv ml/.venv
```

If Python 3.12 is installed on the machine, prefer that interpreter explicitly when creating the environment:

```powershell
cd C:\Users\loq\OneDrive\Desktop\AkashDristi\AkashDristi
C:\Path\To\Python312\python.exe -m venv ml/.venv
```

Do not replace the system Python installation.

## Activate the virtual environment on Windows

```powershell
cd C:\Users\loq\OneDrive\Desktop\AkashDristi\AkashDristi
ml\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
ml\.venv\Scripts\Activate.ps1
```

## Install requirements

After activation:

```powershell
python -m pip install --upgrade pip
python -m pip install -r ml/requirements.txt
```

## Verify the environment

Run the safe environment check script:

```powershell
python ml/scripts/verify_environment.py
```

## Expected successful output

The script should print values similar to:

```text
Python version: 3.12.x
PyTorch version: 2.x.x
CUDA available: True
GPU count: 1
GPU: NVIDIA GeForce RTX 3050
```

If CUDA is not available, the output should still be valid and should clearly report `False` instead of failing.

## Important status

This setup step does not include:

- model training
- dataset download
- large GPU benchmarking
- loading the full xBD dataset
- pretrained model selection

The goal here is only to confirm that the Python environment is valid and that PyTorch can see the local GPU safely.

## Ongoing workflow

Google Colab remains part of the ML experimentation workflow. The reusable parts of the exploratory code will gradually be moved into the repository structure, starting with:

- `ml/scripts/`
- `ml/src/`
- future notebook exports or migration notes

This is intentionally a clean, controlled setup step rather than a full model pipeline implementation.
