from golden_cube.config import EngineConfig


class ModelRunner:
    def __init__(self, config: EngineConfig):
        self.config = config

    def execute(self, batch, kv_cache):
        """Execute one batch.

        TODO:
        1. tokenize
        2. build attention metadata
        3. run model forward
        4. return logits
        """
        raise NotImplementedError("Model execution is the next Golden Cube milestone.")
