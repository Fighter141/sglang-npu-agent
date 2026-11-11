# Knowledge Base

This directory will contain source-traceable engineering knowledge. The organization is inspired by CANNBot Knowledge / OKF; the exact schema is intentionally minimal until validated against real SGLang-on-Ascend use cases.

## Proposed categories
- `hardware/`: device topology, memory, communication and hardware constraints.
- `software/`: CANN, driver, firmware, PyTorch, torch_npu, Triton-Ascend and related compatibility.
- `sglang/`: upstream architecture, backend integration, configuration and known limitations.
- `models/`: model-specific bring-up, precision and serving notes.
- `lessons/`: validated optimization and troubleshooting lessons.

## Knowledge quality rules
Every non-trivial card should include source URLs or repository commit references, applicability conditions, evidence strength, validation status, known limitations, and last-reviewed date. Distinguish upstream-documented facts from local reproduction and hypotheses. Never promote a single unverified observation as a general rule.
