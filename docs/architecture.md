# Architecture

## Decision

Use a **CANNBot-inspired Plugin / Agent / Skill model**, but implement the system as a modular engineering workspace rather than cloning CANNBot's repository layout. Adopt the evidence lifecycle from xLLM Workflow, workspace isolation from VAWS, and infrastructure boundaries from MindIE Agent.

## Component responsibilities

| Layer | Responsibility | Must not own |
|---|---|---|
| Plugin / Workflow | User-facing task entry, routing, orchestration, phase gates | Low-level SSH, profiling parsers, benchmark mechanics |
| Agent roles | Bounded reasoning roles and handoff contracts | Hidden stateful infrastructure |
| Skills | Reusable procedures, decision trees, constraints, tool composition | Long-running process supervision or device locking |
| Services | Deterministic remote execution, NPU leases, benchmark, profiler, experiment storage | LLM task interpretation |
| Knowledge | Versioned facts, SOPs, workflows, validated lessons and provenance | Unverified claims presented as facts |
| Reference contracts | Schemas, manifests, artifact formats and stable interfaces | Model-specific transient observations |

## Workflow interfaces

A workflow should declare:
- intent and required inputs;
- prerequisites and safety boundaries;
- skills/services invoked;
- expected outputs and artifact paths;
- validation gates and failure branches;
- evidence required before claiming success.

A service should expose a deterministic interface with explicit inputs, outputs, exit status, timeout, cancellation, and idempotency semantics where applicable.

A knowledge card should declare applicability (framework, device, software versions, model/workload), provenance, evidence strength, procedure or observation, validation status, and known limitations.

## Initial workflow domains

1. Model bring-up: model config, architecture support, weight loading, tokenizer, numerical correctness, serving smoke test.
2. Serving configuration: hardware topology, parallelism, attention backend, graph, memory, scheduler, quantization and speculative decoding compatibility.
3. Performance optimization: baseline, workload characterization, profiling, bottleneck attribution, candidate plan, controlled A/B and ablation.
4. Incident triage: reproduce, classify, collect logs, isolate layer, validate fix, regression.
5. Release and regression: upstream synchronization, compatibility matrix, correctness/performance gates, changelog and evidence package.

## Evidence model

Every run has an immutable run ID and a manifest. Do not mix:
- diagnostic profiling captures;
- correctness test results;
- non-profiled performance acceptance runs.

Record source commit(s), image digest, CANN/driver/firmware, Python/PyTorch/torch_npu/SGLang versions, hardware topology, model revision, workload, launch arguments, warmup, repetitions, concurrency, and raw outputs.

## Deployment model

Start with local CLI / coding-agent integration and SSH-based remote execution. Keep the service API transport-neutral so a later MCP server or web UI can be added without changing workflow semantics. Do not build a multi-agent runtime or web control plane before single-agent workflows and deterministic services are useful and tested.
