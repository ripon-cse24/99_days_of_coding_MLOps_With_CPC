from pathlib import Path
import json

root = Path(".")

# Create root files
root_files = ["README.md", "LICENSE", ".gitignore", "MODEL_INDEX.md"]

for file in root_files:
    path = root / file
    if not path.exists():
        path.touch()

# Valid starter Jupyter Notebook
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Day Learning Notebook\n", "## Topics Covered\n"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# Write your code here\n"]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {"name": "python"}
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# Create phases and daily folders
phases = {
    "phase-1": (1, 31),
    "phase-2": (32, 60),
    "phase-3": (61, 80)
}

for phase, (start, end) in phases.items():
    (root / phase).mkdir(exist_ok=True)
    (root / phase / "README.md").touch(exist_ok=True)

    for day in range(start, end + 1):
        day_name = f"day-{day:03d}"
        day_path = root / phase / day_name
        day_path.mkdir(exist_ok=True)

        notebook_path = day_path / f"{day_name}.ipynb"
        notes_path = day_path / "NOTES.md"

        if not notebook_path.exists():
            notebook_path.write_text(
                json.dumps(notebook, indent=2),
                encoding="utf-8"
            )

        notes_path.touch(exist_ok=True)

# Phase 4
phase4 = root / "phase-4"
phase4.mkdir(exist_ok=True)
(phase4 / "README.md").touch(exist_ok=True)

# MLOps Capstone
mlops = phase4 / "mlops-capstone"

for folder in ["data", "src", "tests"]:
    (mlops / folder).mkdir(parents=True, exist_ok=True)

for file in [
    "src/train.py",
    "src/predict.py",
    "src/config.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "MODEL_CARD.md",
    "README.md"
]:
    (mlops / file).touch(exist_ok=True)

# Research Capstone
research = phase4 / "research-capstone"

for folder in ["data", "experiments", "results", "paper"]:
    (research / folder).mkdir(parents=True, exist_ok=True)

for file in ["environment.txt", "README.md"]:
    (research / file).touch(exist_ok=True)

# GitHub Actions
workflow = root / ".github" / "workflows"
workflow.mkdir(parents=True, exist_ok=True)
(workflow / "ci.yml").touch(exist_ok=True)

print("99 Days of Coding MLOps repository structure created!")