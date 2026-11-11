# AGENTS.md

Repository-wide instructions for coding agents.

## Purpose and scope
This repository develops reusable agentic workflows and engineering tools for SGLang on Ascend NPUs. The repository is in bootstrap stage: do not describe planned components as implemented.

## Working rules
1. Read the relevant skill, architecture contract, and target upstream source before making changes.
2. Prefer the smallest change that can be validated. Do not create speculative abstractions.
3. Keep workflow decisions in `skills/`; deterministic operations in `services/`; sourced domain facts in `knowledge/`; stable machine-readable contracts in `reference/`.
4. Do not put secrets, private hostnames, internal IPs, credentials, private model paths, or non-public logs in committed files.
5. Never invent benchmark results, compatibility claims, hardware capabilities, or upstream behavior. Cite the exact source revision or record the claim as an unverified hypothesis.
6. For performance work, capture a warmed-up baseline before editing. Keep profiling runs separate from acceptance benchmark runs.
7. For correctness work, preserve a minimal reproducer and compare against a trusted reference.
8. Record exact hardware, software versions, model revision, workload, launch arguments, warmup, repetitions, and raw artifact locations.
9. Keep failed attempts and negative results; do not overwrite history with only the best run.
10. Require explicit user approval before destructive operations, process termination, environment replacement, or expensive multi-node jobs.

## Required optimization loop
Research → Baseline → Diagnose → Plan → Implement → Correctness → Benchmark → Review → Record.

A performance claim is incomplete without comparable baseline and candidate measurements under the same workload and environment.

## Contribution hygiene
- Keep `SKILL.md` concise and procedural; move detailed material into `references/`.
- Add tests for scripts, schemas, and routing changes.
- Update README, architecture, and roadmap when changing public project boundaries.
- Do not add generated run artifacts to Git unless explicitly intended as a sanitized fixture.
