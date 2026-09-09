from dataclasses import dataclass
from golden_cube.scheduler.request import Request


@dataclass(slots=True)
class Batch:
    requests: list[Request]

    def __bool__(self) -> bool:
        return bool(self.requests)
