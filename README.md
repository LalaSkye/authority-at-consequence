# Authority at Consequence v0.1

**MIT-licensed synthetic research demonstration · Public release candidate**

This is a scoped research export, prepared for publication following an owner rights confirmation. It includes one executable harmless synthetic counterexample (S1–S4) and source-bound references to other completed research. It does not reproduce the entire private Authority Race Lab. Internal examiner instructions are excluded from this candidate folder.

## Research question

What happens when an approval is issued, authority changes, and the sink has not observed the newer authority epoch? The historical drone-origin question is motivation only. No drone, weapon, aircraft or operational code is included.

## Test results and safety classification

S1: unfenced stale write produces an effect: **SAFETY VIOLATION**.
S2: sink observes higher epoch and rejects stale write: zero effects in fixture.
S3: sink does not observe higher epoch and accepts stale write even with fencing: **SAFETY VIOLATION**.
S4: authorised effect precedes later revocation: valid at commit.

**4/4 assertion tests passing is not 4/4 safety protections.**

## Reproduce

From `fixtures/separate-authority-sink-v0.1/` run `python3 -I -m unittest discover -s . -p test_separation.py -v`. Python 3.10+, standard library. Test receipts in that directory are local-run evidence only. Ricky supplied Vector's independent examination receipt dated 12 November 2026: Python 3.10.21, 4/4 assertions passing, S1 and S3 classified as safety violations. The complete manifest was not independently rehashed in that receipt; four executable source hashes were explicitly checked.

## Boundaries

Two separate in-memory SQLite connections in one process, deterministic sequential schedule. No network, separate processes, distributed linearizability, remote revocation guarantee, independent legal authority, or real external effect. Sink watermark only enforces epochs observed by the sink.

The other experiments are listed in `EVIDENCE_MAP.md` with pinned private source references. They are not bundled and must not be described as included public code.

Licence: MIT. Copyright (c) 2026 OS-TRILOGY LTD. Ricky confirmed rights for the included material. This export contains no internal review-only files. Its original fixture bytes remain unchanged.
