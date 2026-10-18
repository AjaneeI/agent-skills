---
name: verified-status-reconciliation
description: Reconcile engineering truth across repositories, project trackers, documentation, and communications without inflating completion claims. Use after milestones or when GitHub, Notion, Asana, or other systems disagree about status or blockers.
license: MIT
metadata:
  version: "0.1.0"
---

# Verified Status Reconciliation

## Trigger
Use when a project has multiple trackers, stale summaries, reopened issues, conflicting acceptance states, or progress reports requiring evidence-backed updates.

## Source-of-truth agreement
Define which system is authoritative for each fact *before* editing: code/CI/experiments, roadmap and scientific rationale, human-action ownership, communications, schedule, or release state. Never infer technical completion from a green project badge.

## Procedure
1. Read current authoritative artifacts and timestamps; retrieve latest issue/PR/CI evidence for the relevant work rather than trusting prior summaries.
2. Reconcile status categories: **verified complete**, **in progress**, **blocked**, **failed**, **proposed**, **historical**, and **not started**. Count tasks separately from research or product milestones.
3. Compare each tracker statement against the highest-authority evidence. Record contradictions and staleness explicitly.
4. Update program narrative and action queue with minimal changes; preserve historical context and supersession dates.
5. Set project health according to objective risks and blockers. Avoid green status when a critical gate is known to be blocked.
6. Link each milestone to exact commits, test runs, artifacts, or explicit decision records. Treat a draft PR as unmerged and a passing unit test as not necessarily a passing live experiment.
7. Verify writes by rereading records. If a write fails or branch protection blocks it, preserve the pending correction and report that it is not integrated.

## Stop conditions
Do not rewrite immutable evidence, remove audit trails, merge without required checks, or adjust scientific claims to match a desired progress narrative.

## Output
A brief reconciliation matrix using [the template](references/reconciliation.md), plus changes verified and changes still pending.

## Success
A reader can immediately distinguish *work done*, *evidence accepted*, *phase passed*, and *next human decision*.
