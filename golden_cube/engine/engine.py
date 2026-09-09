from golden_cube.config import EngineConfig
from golden_cube.scheduler.request import Request
from golden_cube.scheduler.scheduler import Scheduler
from golden_cube.kv_cache.manager import KVCacheManager
from golden_cube.model_executor.model_runner import ModelRunner
from golden_cube.sampling.sampler import Sampler


class Engine:
    """Top-level orchestration layer for Golden Cube."""

    def __init__(self, config: EngineConfig):
        self.config = config
        self.scheduler = Scheduler(config)
        self.kv_cache = KVCacheManager(config)
        self.model_runner = ModelRunner(config)
        self.sampler = Sampler()

    def add_request(self, request: Request) -> None:
        self.scheduler.add_request(request)

    def step(self):
        """Run one engine iteration.

        Future flow:
        schedule -> prepare KV -> model forward -> sample -> update request state
        """
        batch = self.scheduler.schedule()
        if not batch:
            return []

        outputs = self.model_runner.execute(batch, self.kv_cache)
        return self.sampler.sample(outputs)
