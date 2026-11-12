# Method and cases

Two independent in-memory SQLite connections simulate authority state and effect sink. The sink enforces only its observed epoch watermark. Ordered transitions are controlled sequentially in tests; `receiver.py` captures in-memory trace, but a separate raw trace file was **not** produced in the original local run. The effect oracle checks actual sink rows, not decision labels alone.

| Case | Expected assertion | Safety classification |
| --- | --- | --- |
| S1 | stale write accepted, 1 sink row | **VIOLATION** |
| S2 | stale write rejected after sink observes higher epoch, 0 rows | Bounded rejection |
| S3 | stale write accepted while sink unaware, 1 row | **VIOLATION** |
| S4 | current approval commits before revocation, 1 row | Valid at defined commit |

These four passing assertions measure scenario sensitivity, **not** protection success rate. Other research objects are referenced in `EVIDENCE_MAP.md` and not rerun here.
