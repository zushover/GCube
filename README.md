<p align="center">
  <img src="docs/assets/golden-cube-logo.png" width="420" alt="Golden Cube Logo"/>
</p>

<h1 align="center">Golden Cube</h1>

<p align="center">
  <strong>GCube — A high-performance LLM inference engine.</strong>
</p>

<p align="center">
  Fast · Efficient · Scalable · Open
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-benchmark">Benchmark</a>
</p>

---

## ✨ Overview

**Golden Cube (GCube)** is an experimental high-performance inference engine for large language models.

The project focuses on the core problems that determine real-world inference performance:

- **request scheduling**
- **KV-cache management**
- **continuous batching**
- **efficient model execution**
- **attention backends**
- **GPU kernel optimization**
- **distributed inference**
- **OpenAI-compatible serving**

GCube is designed as a research-friendly engine: the runtime is split into clear components so that scheduling, memory management, kernels, and execution strategies can be independently optimized and benchmarked.

> **From tokens to new worlds.**

---

## 🚀 Features

### Core runtime

- [x] Modular engine architecture
- [x] Request / sequence abstraction
- [x] Scheduler skeleton
- [x] KV-cache manager skeleton
- [x] Model execution abstraction
- [x] Sampling abstraction
- [ ] Single-request autoregressive decoding
- [ ] Static batching
- [ ] Continuous batching
- [ ] Chunked prefill
- [ ] Paged KV cache
- [ ] Prefix caching

### Model execution

- [ ] Qwen support
- [ ] Llama support
- [ ] Native model runner
- [ ] FP16 / BF16
- [ ] FP8
- [ ] INT8 / INT4
- [ ] MoE support

### GPU optimization

- [ ] FlashAttention
- [ ] FlashInfer
- [ ] Triton kernels
- [ ] CUDA Graph
- [ ] Fused RMSNorm
- [ ] Fused RoPE
- [ ] Optimized sampling kernels

### Serving

- [ ] Python API
- [ ] CLI
- [ ] Streaming generation
- [ ] OpenAI-compatible API
- [ ] Concurrent request serving

### Distributed

- [ ] Tensor Parallel
- [ ] Pipeline Parallel
- [ ] Data Parallel
- [ ] Expert Parallel
- [ ] Multi-node / NCCL

---

## 🧠 Architecture

```text
                         Golden Cube / GCube

┌─────────────────────────────────────────────────────────────┐
│                         API Layer                           │
│             Python API · CLI · OpenAI Server              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                         LLM Engine                          │
│        Request Lifecycle · Streaming · Orchestration       │
└───────────────┬───────────────────────┬─────────────────────┘
                │                       │
                ▼                       ▼
┌──────────────────────────┐   ┌─────────────────────────────┐
│        Scheduler         │   │       KV Cache Manager      │
│  Continuous Batching     │   │   Allocation · Reuse       │
│  Prefill / Decode        │   │   Paging · Prefix Cache    │
└─────────────┬────────────┘   └─────────────┬───────────────┘
              │                              │
              └──────────────┬───────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Model Executor                         │
│       Model Loader · Model Runner · Sampling              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     Attention / Kernels                     │
│     FlashAttention · Triton · CUDA · PagedAttention       │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
                         NVIDIA GPU
```

GCube deliberately separates three of the most important inference subsystems:

```text
Scheduler        KV Cache Manager        GPU Execution
    │                   │                     │
    ▼                   ▼                     ▼
how to run        how to store         how to compute
requests fast     tokens efficiently    tokens efficiently
```

---

## 📦 Repository Structure

```text
golden-cube/
│
├── golden_cube/
│   ├── engine/             # Engine orchestration
│   ├── scheduler/          # Request scheduling
│   ├── kv_cache/           # KV-cache management
│   ├── model_executor/     # Model loading & execution
│   ├── attention/          # Attention backends
│   ├── sampling/           # Token sampling
│   ├── kernels/            # Triton / CUDA kernels
│   ├── worker/             # GPU workers
│   ├── distributed/        # Distributed inference
│   ├── entrypoints/        # CLI / Python / OpenAI API
│   └── utils/
│
├── benchmarks/             # TTFT / TPOT / throughput / memory
├── tests/                  # Unit & integration tests
├── examples/               # Usage examples
├── docs/                   # Architecture & design docs
└── pyproject.toml
```

---

## ⚡ Quick Start

### 1. Clone

```bash
git clone https://github.com/<your-name>/golden-cube.git
cd golden-cube
```

### 2. Create environment

Python **3.11+** is recommended.

```bash
conda create -n gcube python=3.11 -y
conda activate gcube
```

### 3. Install

```bash
pip install -e ".[dev]"
```

### 4. Run tests

```bash
pytest
```

### 5. CLI

```bash
gcube --help
```

Future serving interface:

```bash
gcube serve Qwen/Qwen3-8B
```

---

## 🐍 Python API

Target API:

```python
from golden_cube import Engine, EngineConfig

config = EngineConfig(
    model="Qwen/Qwen3-8B",
    device="cuda",
    dtype="bfloat16",
)

engine = Engine(config)
```

A higher-level API may later be exposed as:

```python
from golden_cube import GCube

engine = GCube(model="Qwen/Qwen3-8B")
output = engine.generate("Explain KV cache in one paragraph.")
```

---

## 🧩 Design Principles

GCube follows a few simple rules:

**1. Performance is measurable.**  
Every optimization should improve a real metric.

**2. Runtime components stay independent.**  
Scheduler, KV cache, attention backends, model execution and kernels should be replaceable without rewriting the entire engine.

**3. Start simple, optimize later.**  
Correctness first. Then profiling. Then kernels.

**4. GPU memory is a first-class resource.**  
KV-cache efficiency is treated as a core engine problem, not an implementation detail.

**5. Benchmark against strong baselines.**  
GCube should be continuously compared with Transformers, vLLM and SGLang.

---

## 📊 Benchmark

The primary metrics are:

| Metric | Meaning |
|---|---|
| **TTFT** | Time To First Token |
| **TPOT** | Time Per Output Token |
| **Throughput** | Generated tokens / second |
| **GPU Memory** | Peak / steady-state GPU memory |
| **Concurrency** | Simultaneous requests served |

Planned comparison:

```text
Golden Cube
vs.
Hugging Face Transformers
vs.
vLLM
vs.
SGLang
```

Hardware used during early development:

```text
GPU: NVIDIA RTX 4090D 24GB
Backend: CUDA
OS: Linux / WSL2
Python: 3.11+
```

---

## 🗺️ Roadmap

### v0.1 — Foundation

- repository architecture
- engine abstraction
- scheduler abstraction
- KV-cache abstraction
- model runner abstraction

### v0.2 — First Tokens

- Qwen model loading
- autoregressive decoding
- greedy sampling
- single-request inference

### v0.3 — KV Cache

- native KV-cache path
- prefill / decode separation
- memory accounting

### v0.4 — Batching

- static batching
- continuous batching
- request lifecycle

### v0.5 — Paged Memory

- block allocator
- block table
- paged KV cache
- chunked prefill

### v0.6 — GPU Fast Path

- FlashAttention / FlashInfer
- Triton kernels
- CUDA Graph

### v0.7 — Cache Intelligence

- prefix cache
- KV reuse
- scheduling improvements

### v0.8 — Serving

- streaming
- OpenAI-compatible API
- concurrent serving

### v0.9 — Scale

- Tensor Parallel
- NCCL communication
- multi-GPU execution

### v1.0 — Golden Cube

A stable high-performance inference runtime with reproducible benchmarks.

---

## 🔬 Research Directions

GCube is intended to become a playground for inference research, including:

- scheduler design
- dynamic batching
- KV-cache eviction policies
- prefix reuse
- speculative decoding
- prefill / decode disaggregation
- heterogeneous GPU scheduling
- quantized inference
- MoE routing
- kernel fusion
- long-context inference
- latency-aware serving

---

## 🤝 Contributing

Golden Cube is currently in early development.

Issues, performance experiments, kernel implementations, model integrations and benchmark contributions are welcome.

```bash
git checkout -b feature/my-feature
```

Please include benchmark results when submitting performance-related changes.

---

## 📄 License

MIT License.

---

<p align="center">
  <strong>Golden Cube · GCube</strong>
</p>

<p align="center">
  Inference for a more open universe.
</p>
