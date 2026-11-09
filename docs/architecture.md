# Architecture (portfolio demo)

```
Synthetic case (JSONL)
        |
        v
validate_dataset.py  --> schema OK?
        |
        v
scoring.py  --> critical overrides + soft score
        |
        v
run_gate.py --> CSV recommendation report
```

Trust boundaries:

1. Inputs and retrieved documents are untrusted until evidenced.
2. Tool actions in the trace are recorded events, not proof of safe production execution.
3. Gate output is advisory; a named human authorises limited use.
