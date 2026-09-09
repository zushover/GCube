import torch


def default_device() -> str:
    return "cuda" if torch.cuda.is_available() else "cpu"
