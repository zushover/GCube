from golden_cube.config import EngineConfig
from golden_cube.scheduler.request import Request
from golden_cube.scheduler.scheduler import Scheduler


def test_scheduler_builds_batch():
    scheduler = Scheduler(EngineConfig(model="dummy", max_num_seqs=2))
    scheduler.add_request(Request("1", "hello"))
    scheduler.add_request(Request("2", "world"))
    batch = scheduler.schedule()
    assert len(batch.requests) == 2
