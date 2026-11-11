# Roadmap

Status: proposed; update only when implementation and validation exist.

## P0 — trustworthy baseline and execution
- [ ] Repository inventory and version compatibility manifest
- [ ] Remote host/container inventory and safe command execution
- [ ] NPU topology probe and explicit resource lease contract
- [ ] SGLang service launch / health / stop lifecycle
- [ ] Workload and benchmark manifest
- [ ] Correctness smoke-test workflow
- [ ] Profiler collection and analysis interface
- [ ] Run manifest, raw artifact index, and comparison report
- [ ] Skill routing and schema validation tests

## P1 — SGLang NPU workflows
- [ ] Model bring-up and support-gap analysis
- [ ] Effective serving configuration capture
- [ ] MoE / EP backend and mode comparison
- [ ] Attention backend and graph compatibility audit
- [ ] MTP / speculative decoding evaluation
- [ ] PD disaggregation and prefill/decode bottleneck analysis
- [ ] Performance regression gates

## P2 — optimization automation and knowledge flywheel
- [ ] Bounded candidate generation and tuning
- [ ] Multi-task worktree isolation
- [ ] Knowledge ingestion, deduplication, lint, provenance and review
- [ ] Validated lesson promotion from experiment records
- [ ] Optional multi-agent parallel investigation

## Exit criteria
A workflow is complete only when its inputs, deterministic execution, validation gates, evidence artifacts, failure behavior, and documentation are tested on a declared software/hardware configuration.
