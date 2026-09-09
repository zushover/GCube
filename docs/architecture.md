# Architecture

Golden Cube is organized around five core runtime responsibilities:

1. Engine orchestration
2. Request scheduling
3. KV-cache management
4. Model execution
5. Sampling

Future optimization layers include attention backends, Triton/CUDA kernels,
distributed execution, and OpenAI-compatible serving.
