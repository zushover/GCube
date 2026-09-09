from dataclasses import dataclass, field
from enum import Enum, auto


class RequestStatus(Enum):
    WAITING = auto()
    RUNNING = auto()
    FINISHED = auto()


@dataclass(slots=True)
class Request:
    request_id: str
    prompt: str
    max_new_tokens: int = 32
    status: RequestStatus = RequestStatus.WAITING
    output_token_ids: list[int] = field(default_factory=list)
