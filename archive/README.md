# Archive

This directory preserves superseded, retracted, frozen, and exploratory
research artifacts.  Nothing here belongs to the current proof spine merely
because it is retained.  Current status is recorded only in
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md), and live targets are listed
in [`../active/INDEX.md`](../active/INDEX.md).

Historical scripts were written while they lived under `active/`.  A script
that imports a retained helper from that directory, or expects the bundled
dependency runtime there, should be invoked from the repository root with:

```sh
PYTHONPATH=active:active/runtime/deps python3 archive/<script>.py
```

An archived script may also depend on an environment or optional solver that
is no longer part of the current verification suite.  Its source is preserved
for provenance; only scripts named by a current result or audit are required
to run in continuous integration.
