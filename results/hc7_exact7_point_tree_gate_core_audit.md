# Independent audit: portal-choice-invariant attained-duty gate core

Audited file: `results/hc7_exact7_point_tree_gate_core.md`.

## Verdict

**GREEN.**  The abstract point--tree theorem, its attained-duty
specialization, and the stated limitations are correct.  The conclusion is
relative to one fixed spanning tree of one full packet.  It gives either a
literal vertex common to every attainable tree hull, or one exceptional
duty with disjoint leaf-witness hulls while both other duty families contain
an entire common subtree.  It does not give a separator, a bounded core, or
control of carriers using non-tree packet edges.

The sole external input was checked against Theorem 2.1 of Aharoni--Berger--
Ziv, *A tree version of Koenig's theorem*, arXiv:math/9912134v2.

## 1. Point--tree encoding and `sigma`

For the hypergraph

\[
 \mathcal A=\{\{i\}\cup V(K):i\in\{1,2,3\},
                         K\in\mathcal H_i\},
\]

the artificial point set is disjoint from `V(T)`, and every tree part is a
subtree of the same tree `T`.  This is exactly the paper's definition of a
point--tree hypergraph.

Two edges carrying the same point intersect at that point.  Two edges with
different points intersect in their tree parts by cross-intersection.
Thus `nu(mathcal A)=1`: it is at most one, and it is at least one because
all three families are nonempty.

The paper defines `sigma(mathcal A)` as the minimum number of members of

\[
 \mathcal F(\mathcal A)=
 \{\{i\}:\{i\}\cup V(K)\in\mathcal A\}
 \cup
 \{V(K):\{i\}\cup V(K)\in\mathcal A\}
\]

whose union meets every hyperedge.  Its Theorem 2.1 gives
`sigma(mathcal A)<=nu(mathcal A)=1`.  The empty family cannot cover the
nonempty hypergraph.  A single artificial point `{i}` misses every edge
from either of the other two nonempty families.  Therefore the one-member
cover is necessarily `V(K_0)` for an occurring subtree `K_0`, and `K_0`
meets every member of all three families.  This verifies both the cover
semantics and the fact that the dominant object is itself an attainable
hull, rather than an arbitrary subtree.

## 2. Minimal-core leaf witnesses

An inclusion-minimal transversal subtree `R subseteq K_0` exists because
the tree is finite.  If `r` is a leaf of nontrivial `R`, then `R-r` is a
proper subtree and fails to meet some family member `L_r`.  Since `R`
still meets `L_r`, this gives exactly

\[
                         L_r\cap R=\{r\}.
\]

For distinct leaves `r,s`, the witnesses `L_r,L_s` are disjoint.  If they
met at a vertex `x`, their unique `r-x` and `x-s` paths would lie in their
union.  A tree has a unique `r-s` path, namely `rRs`; hence the union would
contain an edge of `rRs` incident with more than its permitted singleton
intersection with `R`.  This also covers the case in which `R` is the
single edge `rs`: one witness would have to contain both ends of that
edge.  Thus the leaf witnesses are genuinely vertex-disjoint.

Cross-intersection then forces all leaf witnesses into one family
`mathcal H_j`; witnesses in distinct families would have to meet.  If
`K in mathcal H_i`, `i ne j`, choose `x_r in K cap L_r` for every leaf.
The unique path between `x_r` and `x_s` enters `R` at `r`, contains all of
`rRs`, and leaves at `s`, because each witness meets `R` only at its named
leaf and the two witnesses are disjoint.  Connectedness of `K` forces it
to contain this unique path.  The union of leaf-to-leaf paths in a
nontrivial finite tree is the whole tree, so `R subseteq K`.  The claimed
"all of `R`" conclusion, rather than mere intersection with `R`, is valid.

## 3. Attained-duty specialization

Fixing a spanning tree `T` of the packet puts every literal portal vertex
in the common host tree.  For each duty, every duty-specific portal choice
has a well-defined nonempty minimal `T`-hull, and fullness makes each of
the three hull families nonempty.  A hull contains a packet neighbour of
every literal duty vertex, so it is a connected duty-correct carrier.

If hulls from two distinct duty families were disjoint, select arbitrary
portals for the third duty.  The audited attained-duty tree-split theorem
uses the two disjoint hulls, cuts their joining path into adjacent carriers,
and uses the other full packet for the third duty.  It therefore reflects
the state.  Under nonreflection the three full attainable families are
cross-intersecting, so the abstract theorem applies without changing any
portal quantifier.

## 4. Trust boundary

The result is invariant under portal choice only **after `T` is fixed**.
Changing the spanning tree may change the dominant hull and its minimal
core.  Moreover, a connected carrier in the packet can avoid `R` by using
non-tree edges even when its corresponding `T`-hull passes through `R`.
The theorem therefore proves none of the following:

* that `R` is bounded or is a vertex separator;
* that one core works for all packet spanning trees;
* that the exceptional leaf hulls are adjacent; or
* that deleting one or two vertices produces the fixed-pair endgame.

The draft states all of these limitations accurately.  Its reference to
Perfect--Pym augmentation is a proposed next mechanism, not part of the
proved result.
