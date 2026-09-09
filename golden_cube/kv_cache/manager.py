from golden_cube.config import EngineConfig


class KVCacheManager:
    """KV-cache ownership and allocation boundary.

    v0.1 intentionally leaves physical allocation unimplemented.
    """

    def __init__(self, config: EngineConfig):
        self.config = config
