from dataclasses import dataclass


@dataclass(slots=True)
class KVBlock:
    block_id: int
    ref_count: int = 0
