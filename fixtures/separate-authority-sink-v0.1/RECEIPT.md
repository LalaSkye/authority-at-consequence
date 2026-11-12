# Local execution receipt · 12 November 2026

Command: `python3 -I -m unittest discover -s . -p test_separation.py -v`
Python: 3.13.5
Dependencies: Python standard library only
Exit code: 0
Result: 4/4 expected scenario assertions passed.

**CRITICAL:** S1 and S3 both exhibit forbidden effects (safety_violation=True). These are intentionally exposed counterexamples, NOT protection passes. S2 denies after observed higher epoch. S4 commits before revocation.

Evidence: stderr.txt, stdout.txt, exit_code.txt, python_version.txt, SHA256SUMS.txt. The test reads the SQLite sink rows as effect oracle and captures ordered transitions in memory. Source is locally executed, not independently reviewed. The trace is checked in assertions but no separate trace log was exported. No external writes or deployments.
