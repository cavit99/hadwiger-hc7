# Missing-pair overlap across an exact rotation

## Status

This is a literal quotient-free consequence of the audited rotation datum.
It does not terminate a rotation chain, but it constrains every edge in the
no-`K_7^-` branch by a reusable exchange: two disjoint two-spoke deficiency
sets already assemble a `K_7^-` model without splitting the connector.

## Theorem 1 (the combined-centre model)

Use the rotation datum of
`../results/hc7_near_k7_rotation_edge.md`.  Thus

\[
 X,U,F_1,\ldots,F_5,
 \qquad U=Z\mathbin{\dot\cup}W,
\]

are literal connected bags, `F_1,...,F_5` form a clique model,
`E(X,W)\ne\varnothing`, and the missing-row sets of `X` and `W` are
respectively `D,E`.  The connector `Z` meets every row in `D\cup E`.

The seven bags

\[
                 X\cup W,\quad Z,\quad F_1,\ldots,F_5        \tag{1.1}
\]

form a labelled near-clique model in which the only possibly absent
adjacencies are

\[
 \{(X\cup W,F_i):i\in D\cap E\}
 \ \cup\
 \{(Z,F_j):j\notin D\cup E\text{ and }E(Z,F_j)=\varnothing\}. \tag{1.2}
\]

Consequently, if

\[
                    |D|=|E|=2,\qquad D\cap E=\varnothing,
\]

then `G` contains a `K_7^-` minor.  If `Z` also meets the unique row
outside `D\cup E`, then `G` contains a `K_7` minor.

### Proof

The first bag is connected because `XW` is a literal edge in the
rotation datum.  For `i\notin D` the old centre `X` meets `F_i`; if
`i\in D-E`, the new centre `W` meets `F_i`.  Hence `X\cup W` can miss
only the rows in `D\cap E`.

The connector `Z` is connected, is adjacent to `X\cup W`, and meets the
rows in `D\cup E`.  This proves (1.2), since the five fixed rows are
pairwise adjacent and all remaining pairs in (1.1) have just been
checked.

When `D,E` are disjoint pairs, `X\cup W` misses no row and `Z` is
guaranteed to meet four rows.  Hence only the unique fifth connector--row
edge can be absent.  This is `K_7^-`, or `K_7` if that last edge is
present.  Every bag and adjacency is literal; no contracted quotient is
lifted.  \(\square\)

### Corollary 1.1 (one-hole/two-hole median)

If `|D|=1`, `|E|=2`, and `D\cap E=\varnothing`, (1.1) is a labelled
`K_7^vee` model whose centre is `Z` and whose only potentially missing
spokes go to the two rows outside `D\cup E`.  If `Z` meets either of
those rows, the model is `K_7^-` or `K_7`.

This is a third, literal model attached to the rotation edge; it is not a
choice of direction between the two inverse endpoint models.

## Corollary 2 (overlap constraint in the two-hole branch)

If `G` has no `K_7^-` minor, every two-hole-to-two-hole rotation satisfies

\[
                              D\cap E\ne\varnothing.          \tag{2.1}
\]

If `|D\cap E|=1`, write `h_1,h_2` for the two row labels outside
`D\cup E`.  Then `Z` is anticomplete to at least one of `F_{h_1},F_{h_2}`.

### Proof

The first assertion is Theorem 1.  For the second, the same seven bags
(1.1) have only the possibly absent spoke from `X\cup W` to the common
row in `D\cap E`, because every other row is met by at least one of
`X,W`.  The connector already meets all three rows in `D\cup E`.  If it
also met both remaining rows, (1.1) would be a `K_7^-` model.  \(\square\)

## Exact use

Missing pairs along a target-free two-hole rotation chain are therefore
edges of the five-label complete graph which meet at every consecutive
step.  A non-overlapping jump is already terminal.  This does **not**
make the chain globally coherent: intersecting pairs can still wind around
a triangle or a five-cycle, and the latter occurs in coherent two-apex
architectures.  The remaining holonomy theorem must use the connector
webs or proper-minor states, not pair overlap alone.
