MODEL_REGISTRY: dict[str, type] = {}


def register_model(name: str):
    def decorator(cls):
        MODEL_REGISTRY[name] = cls
        return cls
    return decorator
