"""Schema validation for safety gate cases."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "safety_gate_cases.jsonl"

REQUIRED_CASE_KEYS = {
    "case_id",
    "title",
    "risk_tier",
    "expected_outcome",
    "expected_outcome_met",
    "required_evidence_ids",
    "prohibited_actions",
    "requires_human_approval",
    "trace",
}

REQUIRED_EVENT_KEYS = {
    "step",
    "event_type",
    "description",
    "evidence_ids",
    "action",
    "approved_by_human",
}


def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError(DATA)

    cases = []
    with DATA.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            case = json.loads(line)
            missing = REQUIRED_CASE_KEYS - set(case)
            if missing:
                raise ValueError(f"Line {i}: missing keys {missing}")
            for j, event in enumerate(case["trace"]):
                missing_e = REQUIRED_EVENT_KEYS - set(event)
                if missing_e:
                    raise ValueError(f"Line {i} event {j}: missing {missing_e}")
            cases.append(case)

    print(f"Dataset valid: {len(cases)} cases.")


if __name__ == "__main__":
    main()
