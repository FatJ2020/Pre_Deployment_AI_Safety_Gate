# Pre-Deployment AI Safety Gate

### A risk-gated release check for operational AI systems — before limited use is authorised

A transparent, deterministic pre-deployment gate that decides whether an AI system (or agent trajectory) is ready for limited operational use, must be reviewed, or must be blocked.

> **Portfolio status:** self-directed demonstrator.  
> All cases and traces are synthetic.  
> This is a framework prototype, not a production safety system and not a regulatory filing tool.

---

## Why this project exists

Regulation and enterprise practice are moving toward the same question:

**Before this AI system is allowed to influence real work, what must be proven?**

Typical gaps in demos:

- fluent answers without evidence
- missing human approval on high-impact actions
- prohibited actions still present in the trajectory
- incomplete or non-sequential traces
- no clear owner for release

This project implements a **pre-deployment safety gate** that applies critical overrides and produces an auditable recommendation:

| Outcome | Meaning |
|---|---|
| `PASS_FOR_LIMITED_USE` | Configured checks passed; still requires named human authorisation for real use |
| `REVIEW` | Non-critical gaps; human review required before any use |
| `BLOCK` | Critical condition triggered; do not proceed |

---

## Design principles

1. **Gates before capability claims** — a high score does not override a critical failure.
2. **Evidence is mandatory** — claims without required evidence IDs fail the gate.
3. **High-impact actions need humans** — approval events must appear in the trace when required.
4. **Trajectory over final answer** — the full sequence is evaluated, not only the last message.
5. **Human remains accountable** — `PASS_FOR_LIMITED_USE` is advisory, never automatic production authorisation.

---

## What the code does

| Component | Role |
|---|---|
| `data/safety_gate_cases.jsonl` | Synthetic pre-deployment scenarios |
| `src/safety_gate/scoring.py` | Transparent rules + critical overrides |
| `src/safety_gate/run_gate.py` | CLI gate runner → CSV report |
| `src/safety_gate/validate_dataset.py` | Schema checks |
| `tests/test_scoring.py` | Unit tests for pass / review / block logic |
| `docs/` | Method, risk register, interview demo script |
| `reports/` | Sample and latest gate results |

---

## Quick start

```bash
git clone https://github.com/<YOUR_USERNAME>/pre-deployment-ai-safety-gate.git
cd pre-deployment-ai-safety-gate

python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

python -m src.safety_gate.validate_dataset
python -m src.safety_gate.run_gate
python -m unittest tests.test_scoring -v
```

---

## Scoring dimensions (summary)

| Check | Critical if failed? |
|---|---|
| Required evidence present | Yes → BLOCK |
| Prohibited action attempted | Yes → BLOCK |
| Human approval present when required | Yes → BLOCK |
| Trace sequential and complete | Yes → BLOCK |
| Expected outcome met | Contributes to score; may REVIEW |
| Risk tier consistent with controls | Contributes to score |

Full detail: `docs/evaluation_method.md` and `src/safety_gate/scoring.py`.

---

## Relationship to other portfolio projects

| Project | Role in the stack |
|---|---|
| Industrial AI Evaluation Framework | Scores answer quality dimensions |
| Northstar Operational AI CoPilot | Governs day-to-day decision support + routing |
| Agent Development Lifecycle (ADL) | Full lifecycle stages + trajectory evaluation |
| AI Evaluation Process Assurance | Assures the evaluation process itself |
| **This repo** | **Pre-release gate before limited operational use** |
| Operational AI Compliance Evidence Pack | Evidence pack for audits / disclosure |

Together: **evaluate → govern → lifecycle → process assurance → pre-deployment gate → compliance evidence**.

---

## Interview one-liner

> “This gate applies automotive-style release discipline to AI systems: critical failures block, evidence and human approval are mandatory for high-impact paths, and a named human still owns limited-use authorisation.”

---

## Limitations (stated on purpose)

- Synthetic data only
- Rule-based evaluation (not a trained judge model)
- No live model calls or production tool execution
- Not a substitute for legal, security or regulatory review

---

## Licence

See `LICENSE`.
