# Independent audit of the four-connected paired-repair barrier

**Verdict:** GREEN for the exact revisions audited.

## Audited revisions

- statement: `hc7_four_connected_edge_rooted_pair_barrier.md`
- statement SHA-256: `bcce76fb8cd5af324e3dd94d6ad7396614cd483b75a134724d3e26f8f7efbc75`
- checker: `hc7_four_connected_edge_rooted_pair_barrier_verify.py`
- checker SHA-256: `5d5fda2a70ca2d2a4c1befe72080a1e66f6287c368f0810d861f7b3217b72876`

The checker was rerun and returned connectivity four and zero disjoint
prescribed connected pairs.  Independent graph6 decoding confirms that
`Ffznw` has exactly the displayed edge set.

Deleting any set of fewer than four vertices leaves the graph connected,
while a four-cut exists.  The set `{0,1,4,5,6}` is a literal `K_5`, so the
graph is nonplanar.  The roots `u=2,v=3` have the stated anticompleteness to
the disjoint edges `01,45`.

For the first prescribed triple, any connected enlargement disjoint from
`{3,4,5}` must connect vertex `2` to edge `01`; the only remaining possible
connector is vertex `6`.  Symmetrically, every connected enlargement of
`{3,4,5}` disjoint from `{2,0,1}` also contains `6`.  Therefore two such
connected subgraphs cannot be vertex-disjoint.  This proves the advertised
counterexample without relying only on enumeration.

The scope is exact: the example refutes a connectivity/nonplanarity/literal-
`K_5` shortcut, but it supplies neither a seven-connected host nor the
contraction-critical and five-support star data retained by the active
programme.
