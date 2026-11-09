"""CLI runner for the Pre-Deployment AI Safety Gate."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from src.safety_gate.scoring import evaluate_case

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "safety_gate_cases.jsonl"
OUT = ROOT / "reports" / "latest_gate_results.csv"


def load_cases(path: Path) -> list[dict]:
    cases = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError(f"Missing dataset: {DATA}")

    cases = load_cases(DATA)
    results = [evaluate_case(c) for c in cases]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "case_id",
        "title",
        "risk_tier",
        "score",
        "recommendation",
        "critical_reasons",
        "notes",
    ]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            row = dict(r)
            row["critical_reasons"] = ";".join(r["critical_reasons"])
            row["notes"] = ";".join(r["notes"])
            writer.writerow(row)

    print(f"Evaluated {len(results)} cases -> {OUT}")
    for r in results:
        reasons = ";".join(r["critical_reasons"]) or "no critical rule triggered"
        print(f"{r['case_id']}: {r['score']}/100 | {r['recommendation']} | {reasons}")


if __name__ == "__main__":
    main()
