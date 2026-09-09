# Golden Cube

**Golden Cube** is an experimental LLM inference engine focused on efficient scheduling,
KV-cache management, model execution, and future GPU kernel optimization.

## Status

v0.1 scaffold.

## Development

```bash
pip install -e ".[dev]"
pytest
golden-cube --help
```

## Initial roadmap

- [x] Repository scaffold
- [ ] Single-request inference loop
- [ ] KV cache manager
- [ ] Static batching
- [ ] Continuous batching
- [ ] Paged KV cache
- [ ] FlashAttention / Triton backend
- [ ] OpenAI-compatible API
- [ ] Tensor Parallel
