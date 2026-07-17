# Audit of the contracted-path list-lock theorem

**Verdict:** GREEN (separate internal audit)

**Audited theorem revision:** SHA-256
`804550a76c1566f6867d21d3254a67b881bac9370556c9b9d84fe6eabce5c634`
of `hc_contracted_path_list_lock.md`.

## Checks performed

After contracting the induced path, the contracted vertex's colour is
absent from every outside neighbourhood, so it belongs to every path
list.  A list-colouring of the path would combine with the proper-minor
colouring to colour the original graph, making the list assignment
uncolourable.

The reachable-colour recurrence for path prefixes is exact.  Its first
empty set forces the preceding reachable set and current list both to be
the singleton contracted colour.  Tracing backwards to the last earlier
singleton list, and excluding another such list internally, forces all
intermediate reachable sets to remain singletons.  The lists consequently
occur in equal pairs `{0,c_i},{0,c_i}`, giving an odd-length locked
subpath with singleton endpoint lists.  The translation to outside colour
contacts is correct.

For the `HC_7` corollary, every chord of a lexicographically chosen repair
path lies in the same induced two-colour graph and provides a shortcut
which cannot increase protected-branch-set usage.  Thus the path is
induced.  Its alternating original colours and the odd locked length put
the two saturated endpoints on opposite sides.

## Scope

The theorem gives a uniform, exact list obstruction and saturated colour
contacts.  It does not identify those colours with prescribed branch-set
labels and therefore does not itself construct a clique minor.  No
unresolved gap remains within the stated theorem and corollary.
