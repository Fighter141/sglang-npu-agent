# SGLang NPU Agent

An agentic engineering workspace for developing, deploying, optimizing, and debugging [SGLang](https://github.com/sgl-project/sglang) on Ascend NPUs.

> **Project status:** bootstrap / architecture proposal. This repository starts with workflow contracts and scaffolding; it does not claim that the planned tools or skills are implemented.

## Goals

- Make SGLang-on-Ascend development workflows reproducible.
- Separate agent decisions from deterministic tools and remote execution.
- Preserve benchmark, correctness, profiling, and environment evidence for every change.
- Reuse upstream SGLang, Ascend, CANN, and community knowledge with source/version traceability.
- Support model bring-up, serving configuration, MoE, graph, speculative decoding, PD disaggregation, profiling, and regression workflows.

## Architecture

The project adopts a **Plugin / Workflow → Agent → Skill** organization, with independent infrastructure services and a governed knowledge layer.

```text
User / Coding Agent (Codex, Claude Code, Cursor, ...)
  |
  +-- Plugins / Workflows       task entry, routing, gates, orchestration
  |     +-- model bring-up
  |     +-- performance optimization
  |     +-- incident diagnosis
  |     +-- release / regression
  |
  +-- Specialist Agents         bounded roles; optional, not mandatory
  |     +-- model / correctness
  |     +-- performance / profiling
  |     +-- runtime / distributed debugging
  |     +-- reviewer
  |
  +-- Skills                    reusable procedures and decision logic
  |     +-- SGLang model adapter
  |     +-- Ascend serving & configuration
  |     +-- MoE / EP / communication
  |     +-- graph / FIA / MTP
  |     +-- benchmark / profiler / debugging
  |
  +-- Infrastructure Services   deterministic execution, independently testable
  |     +-- remote-dev / job manager
  |     +-- NPU coordinator / resource leases
  |     +-- benchmark runner
  |     +-- profiler & trace analyzer
  |     +-- experiment ledger / artifact store
  |     +-- git / CI / regression
  |
  +-- Knowledge                 versioned, sourced, validated engineering knowledge
        +-- hardware & software constraints
        +-- procedures / workflows
        +-- model and PR history
        +-- validated optimization lessons
```

### Architectural rules

1. **Skills decide; tools execute.** Do not implement SSH, device allocation, process supervision, benchmark execution, or profiler parsing as prompt-only instructions.
2. **Evidence before optimization.** Establish a reproducible baseline and correctness check before changing performance-sensitive code.
3. **Separate diagnostic and acceptance measurements.** Profiling explains bottlenecks; non-profiled benchmark runs establish performance claims.
4. **Every result is attributable.** Record source commit, model revision, container/image, CANN/driver/PyTorch/torch_npu/SGLang versions, hardware topology, launch arguments, workload, warmup, repetitions, and raw outputs.
5. **Framework-neutral core, SGLang-first adapter.** Keep common experiment and evidence contracts independent of SGLang internals; put framework-specific logic behind adapters.
6. **Knowledge is evidence-bearing.** Mark claims as hardware specification, upstream documentation, reproduced result, single observation, or hypothesis. Keep negative results.
7. **No silent configuration changes.** Show the effective configuration and explain deviations from defaults.
8. **Human approval for destructive or costly operations.** Resource release, process termination, environment replacement, and long multi-node runs require explicit safety boundaries.

## Repository layout

```text
.
├── AGENTS.md
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   └── workflow/
├── plugins/                  # end-to-end task workflows and routing
├── agents/                   # optional role definitions and handoff contracts
├── skills/                   # procedural skills: SKILL.md + references + scripts
│   ├── README.md
│   ├── model-bringup/
│   ├── serving-config/
│   ├── performance-optimization/
│   ├── benchmark/
│   ├── profiling/
│   ├── incident-triage/
│   └── code-review/
├── services/                 # deterministic tools; not prompt instructions
│   ├── remote-dev/
│   ├── npu-coordinator/
│   ├── benchmark/
│   ├── profiler/
│   └── experiment-store/
├── knowledge/                # sourced knowledge cards and schemas
│   ├── schema/
│   ├── hardware/
│   ├── software/
│   ├── sglang/
│   ├── models/
│   └── lessons/
├── reference/                # stable contracts, workload and artifact specs
│   ├── schemas/
│   └── templates/
├── runs/                     # local experiment outputs; ignored by git
└── tests/                    # lint, schema, routing, and workflow tests
```

## Initial workflow lifecycle

`Discover → Baseline → Diagnose → Plan → Change → Correctness → Benchmark → Review → Record`

A performance optimization must not skip baseline capture, correctness validation, or controlled comparison. Failed attempts and regressions should be retained as searchable evidence.

## Initial scope

### P0 — establish a reliable engineering loop
- Repository and environment inventory
- SGLang + Ascend version compatibility record
- Remote command/job execution contract
- NPU topology and resource reservation contract
- Reproducible baseline benchmark manifest
- Correctness and performance result schema
- Profiler collection / analysis interface
- Experiment record and regression comparison

### P1 — SGLang-specific optimization workflows
- Model bring-up and model support diagnosis
- Serving configuration audit and effective-config capture
- MoE / EP / communication mode comparison
- CUDA Graph / NPU graph and attention backend compatibility
- MTP / speculative decoding evaluation
- Prefill / decode and PD-disaggregation analysis

### P2 — advanced automation
- Automated candidate generation and bounded tuning
- Cross-version regression tracking
- Knowledge ingestion, deduplication, validation, and promotion
- Multi-agent parallel investigation with isolated worktrees

## Upstream references

- [SGLang](https://github.com/sgl-project/sglang)
- [SGLang Ascend NPU documentation](https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus)
- [vLLM-Ascend Workspace](https://github.com/mindie-agent/vllm-ascend-workspace) — workspace and multi-worktree patterns
- [xLLM AI Coding Workflow](https://github.com/xLLM-AI/xllm-workflow) — experiment lifecycle and evidence patterns
- [Ascend Agent Skills](https://github.com/Ascend/agent-skills) — reusable Ascend-specific skills
- [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge) — knowledge organization and governance reference
- [MindIE Agent](https://github.com/mindie-agent/mindie-agent) — remote execution, coordination, profiler, and debugger component boundaries

These are references, not vendored dependencies. Reuse code only after checking its license, compatibility, and maintenance status.

## Status

See [docs/roadmap.md](docs/roadmap.md). The initial commit defines the intended boundaries and contracts; implementation will be added incrementally and validated on real Ascend hardware.
