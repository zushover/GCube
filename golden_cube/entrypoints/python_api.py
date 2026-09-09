from golden_cube.config import EngineConfig
from golden_cube.engine.engine import Engine


def create_engine(model: str, **kwargs) -> Engine:
    return Engine(EngineConfig(model=model, **kwargs))
