from dataclasses import dataclass


@dataclass(slots=True)
class EngineConfig:
    model: str
    device: str = "cuda"
    dtype: str = "bfloat16"
    max_model_len: int = 4096
    max_num_seqs: int = 16
    kv_block_size: int = 16
