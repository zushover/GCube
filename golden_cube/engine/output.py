from dataclasses import dataclass


@dataclass(slots=True)
class RequestOutput:
    request_id: str
    text: str
    finished: bool
