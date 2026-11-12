# Frozen cases and safety oracle

Before execution, S1: approval epoch 1, revocation epoch 2, unfenced sink accepts stale token, safety_violation=True. S2: same ordering but sink observes epoch 2 before fenced commit, reject and zero rows. S3: fenced sink remains at epoch 1, stale token accepted, safety_violation=True (the key counterexample). S4: current approval commits before later revocation, one row and safety_violation=False.

The safety oracle uses the authority snapshot immediately before the sink transition and actual SQLite sink rows. These are deterministic sequential events, not a concurrent distributed history. Expected forbidden commits are **violations**, not successful protection. An assertion that misses them fails benchmark sensitivity.
