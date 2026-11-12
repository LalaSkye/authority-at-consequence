# Separate Authority/Sink Fencing Counterexample v0.1

TRILOGYOS × PRECITA | CANDIDATE | HOLD

Two independently owned in-memory SQLite connections, one for authoritative epoch and one for a sink watermark and effect rows. No network, remote service, concurrency, real document release or military integration. No third-party dependencies.

Run from this directory: `python3 -I -m unittest discover -s . -p test_separation.py -v`

This benchmark tests four frozen schedules. S1 and S3 deliberately commit forbidden effects and must be reported as **safety violations**, despite the test suite passing. S2 rejects after the sink observes the newer epoch. S4 permits a valid effect before later revocation. Fencing is a known technique; no novelty or distributed guarantee claimed.

The sink's epoch is not automatically updated when the authority revokes. The local oracle can inspect both databases; a real remote sink generally cannot. The authority snapshot and sink transition are sequential here, not an atomic cross-store operation. See FROZEN_CASES.md and RECEIPT.md.
