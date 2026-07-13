# Promoting the common missing row to the seventh branch set

## Status and proof-spine role

This is an active literal-model lemma awaiting independent audit.  It
changes the capacity count in the one-shared-label `q=2 <-> q=2` cell.
Instead of asking both endpoint carriers to meet the same common portal
class, it promotes that fixed row, together with one middle carrier, to a
third branch set.  The two endpoint carriers then need only the two
exclusive missing rows.

This is the label-preserving mechanism exposed by the square-antiprism
barrier: if it fails, the remaining obstruction is a genuine crossed
two-shore/web order, not a tautological collision at the common portal.

## Theorem 1 (three-carrier common-row promotion)

Use the exact rotation datum of
`../results/hc7_near_k7_rotation_edge.md`, with

\[
                    D=\{a,b\},\qquad E=\{a,c\},          \tag{1.1}
\]

where `a,b,c` are distinct.  Thus `X` misses exactly `F_a,F_b`, `W`
misses exactly `F_a,F_c`, `XW` is a literal edge, and
`F_1,...,F_5` are pairwise disjoint connected pairwise adjacent rows.

Suppose `G[Z]` contains three pairwise vertex-disjoint nonempty connected
subgraphs `L,K,R` satisfying

\[
\begin{array}{c|c}
L & E(L,X)\ne\varnothing,\quad E(L,F_b)\ne\varnothing,\\
K & E(K,F_a)\ne\varnothing,\\
R & E(R,W)\ne\varnothing,\quad E(R,F_c)\ne\varnothing,
\end{array}                                             \tag{1.2}
\]

and

\[
                         E(L,K)\ne\varnothing,
             \qquad     E(K,R)\ne\varnothing.           \tag{1.3}
\]

Then `G` contains a literal `K_7` minor.

### Proof

Use the seven branch sets

\[
       X\cup L,\qquad F_a\cup K,\qquad W\cup R,
                    \qquad F_i\quad(i\ne a).             \tag{1.4}
\]

They are nonempty, pairwise disjoint, and connected: the three unions are
connected by the three corresponding contact edges in (1.2), and the four
unchanged rows were already connected.

The first three bags are pairwise adjacent.  The middle bag meets the
other two through (1.3), while `X union L` meets `W union R` through the
literal old edge `XW` from the rotation datum.

The bag `X union L` meets every unchanged row.  The old centre `X`
already meets every `F_i` outside `{a,b}`; row `F_a` is now part of the
middle bag, and `L` supplies the only missing unchanged row `F_b`.
Symmetrically, `W union R` meets every unchanged row because `W` already
meets all rows outside `{a,c}` and `R` supplies `F_c`.  Finally,
`F_a union K` meets every unchanged row through the old clique-model edges
from `F_a`.  The four unchanged rows remain pairwise adjacent.

Every pair among the seven bags in (1.4) therefore has a literal host
edge, so they form a `K_7` model.  \(\square\)

## Corollary 2 (singleton common portal)

If `P_a=N_Z(F_a)={p}`, Theorem 1 applies with `K={p}` whenever `Z-p`
contains disjoint connected subgraphs `L,R` such that

* `L` meets `X,F_b` and has a neighbour of `p`; and
* `R` meets `W,F_c` and has a neighbour of `p`.

Thus the common portal no longer has to be duplicated across the two
endpoint carriers.  It becomes the attachment vertex of the promoted
branch set `F_a union {p}`.

## Uniform form

The proof is independent of the number five.  In a missing-star model of
order `r+2`, suppose two endpoint centres have defect sets `{a,b}` and
`{a,c}` against a fixed clique model of `r` rows and are literally
adjacent.  Three disjoint carriers in the connecting donor—an old-side
`b` carrier, a middle `a` carrier, and a new-side `c` carrier, with the
middle adjacent to both sides—promote row `a` and give a clique model one
order larger.  All rows outside `{a,b,c}` are inherited unchanged.

## Trust boundary

The theorem supplies the literal `K_7` once the three connected carriers
exist.  It does not assert that connectivity alone produces them.  The
audited square-antiprism barrier shows that even a four-connected planar
connector can force the two endpoint duties into an alternating face.
The next composition theorem must turn that failure into a faithful rural
page, a matching actual-adhesion state, or the same global two-apex pair.
