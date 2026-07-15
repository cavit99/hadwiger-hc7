# Audit: nine-vertex support-six closure

## Verdict

**GREEN.**  The supplied exhaustive `geng` certificate was independently
replayed: it generated `120314` graphs, found `614` with support
transversal greater than two, retained the unique `K_7`-minor-free graph
`HUzvvx}`, and verified all thirty-six rooted `K_6` instances.  The
mathematical reduction, graph encoding, minor-model test, exceptional
rooted models, and seven-connectivity lift all pass audit.  No conclusion
for support unions of order at least ten is claimed.

## 1. Exhaustive range

If an exact six-support avoids a pair `P`, it lies in the seven-vertex
graph `J-P` and contributes at least eleven distinct edges there.  Summing
over all thirty-six pairs counts every edge exactly twenty-one times.
Thus `21e(J)>=396` and `e(J)>=19`.  Consequently `geng -q 9 19:36`
really covers every possible local graph.

The expected generator count is `120314`.  The script asserts that count,
so a truncated generator stream is rejected.

## 2. Exact-support test

A spanning `K_5` model on six vertices necessarily has one two-vertex
bag and four singleton bags.  The two-vertex bag must be an edge; the
singletons form a literal `K_4`; and each singleton is adjacent to at
least one endpoint of the edge.  Conversely those conditions display the
model.  The predicate `is_exact_six_support` is therefore exact.

The transversal predicate says that for every pair there is a support
whose bitmask is disjoint from that pair, which is precisely
`tau>2` for a nonempty family.

## 3. Minor-model test

Every `K_7` model in a nine-vertex graph uses seven, eight, or nine
vertices.  The script enumerates every set partition of every such used
set into seven nonempty bags exactly once.  It then tests connectivity of
each bag and a literal edge between every pair of bags.  Thus it is an
exact minor-model test, not a density proxy.

The sole survivor is graph6 `HUzvvx}`, with twenty-seven edges and
twenty-seven exact six-supports.  Direct decoding gives the complement of
the nine-cycle.  The script separately asserts all of these facts.

## 4. Rooted exception

For each of the thirty-six seven-subsets of the exception, the script
enumerates all `K_6` models and asserts that one meets the prescribed set
in every bag.  Formula (3.2) in the theorem note gives a short human
certificate for the four dihedral orbits.  Direct inspection in
`complement(C_9)` verifies connectivity and all fifteen interbag
adjacencies in each row.

## 5. Host-graph lift

If the seven-connected host had no vertex outside `X`, it would equal
`complement(C_9)`, whose vertex-connectivity is six.  For a component
`C` outside `X`, either `N(C)=X` or `N(C)` is a genuine cut; hence it has
at least seven members.  An `N(C)`-meeting `K_6` model in `X`, together
with `C`, gives seven pairwise adjacent connected branch bags.  No
contraction changes the literal boundary labels.

This proves exactly the advertised nine-vertex closure.
