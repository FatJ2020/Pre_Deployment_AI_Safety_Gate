# Interview demo script (about 5 minutes)

## Positioning (15s)

> “This is a pre-deployment safety gate for operational AI. It applies critical overrides — missing evidence, prohibited actions, missing human approval — and outputs PASS_FOR_LIMITED_USE, REVIEW or BLOCK. A human still owns real authorisation.”

## Problem (30s)

Fluent demos fail when high-impact actions are attempted without approval, evidence is missing, or traces are incomplete. Organisations need a gate before limited use.

## Live commands (90s)

```bash
python -m src.safety_gate.validate_dataset
python -m src.safety_gate.run_gate
```

Highlight:

| Case | Teaching point |
|---|---|
| SG-001 | Clean grounded path → PASS |
| SG-003 | Prohibited PO → BLOCK |
| SG-004 | Missing evidence → BLOCK |
| SG-002 / SG-006 | High-risk with approval → can PASS |

## Connect to background (30s)

> “Same instinct as programme gates in automotive product development: critical failures block release; evidence and ownership are mandatory.”

## Limitation (15s)

> “Synthetic traces and deterministic rules — designed to show governance structure, not a production runtime.”
