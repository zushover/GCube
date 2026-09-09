from collections import deque

from golden_cube.config import EngineConfig
from golden_cube.scheduler.batch import Batch
from golden_cube.scheduler.request import Request, RequestStatus


class Scheduler:
    def __init__(self, config: EngineConfig):
        self.config = config
        self.waiting: deque[Request] = deque()

    def add_request(self, request: Request) -> None:
        self.waiting.append(request)

    def schedule(self) -> Batch:
        selected: list[Request] = []

        while self.waiting and len(selected) < self.config.max_num_seqs:
            request = self.waiting.popleft()
            request.status = RequestStatus.RUNNING
            selected.append(request)

        return Batch(selected)
