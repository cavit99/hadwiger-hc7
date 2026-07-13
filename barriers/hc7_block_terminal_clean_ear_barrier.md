# Block-terminal clean-ear barrier

**Status:** explicit verified counterarchitecture to a connectivity-only
clean-ear or gate-bypass principle.  It is not a counterexample to `HC_7`.

Take two icosahedra, delete one vertex from each, and identify the two
resulting five-cycles with reversed orientation.  The resulting planar tube
is five-connected.  Joining two adjacent apices to every tube vertex gives
a seven-connected host whose deletion of the two apices is planar.

Inside the tube, the verifier selects an induced three-connected carrier
with a facial three-gate and two three-vertex terminal blocks.  All nine
prescribed block-terminal crosses fail, even though the carrier has an
explicit same-vertex web completion.  The gate cell has four unavoidable
first neighbours outside the carrier.  Thus seven-connectivity plus the
local web certificate does not by itself produce a clean gate bypass or a
two-vertex transversal inside the carrier.

Any usable `HC_7` clean-ear theorem must therefore retain the attained-duty
state, the literal first-hit identities, or a proper-minor transition; it
cannot be a connectivity-only statement about the carrier.

Reproduce from the repository root with:

```text
PYTHONPATH=active/runtime/deps python3 \
  barriers/hc7_block_terminal_clean_ear_barrier_verify.py
```

The companion verifier checks planarity and connectivity, the exact gate,
all nine failed linkages, and the explicit web completion.
