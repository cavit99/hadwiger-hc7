# Independent audit: one-defect two-root `K_5` separator theorem

## Verdict

**GREEN** at the exact strengthened source revision

```text
87e08e0a151f0aca4c168995a906b60b0a95d9023e8076d4fa92b8982a002179  results/hc7_one_defect_two_root_k5_separator.md
```

This is a fresh audit of the arbitrary-connected-root version.  It does not
rely on the verdict for the earlier singleton-root statement.  The spanning
normalization, connected-centre tree split, explicit `K_7` model and
orientation-symmetric two-root reduction are correct.

The only change after the mathematical audit was replacing the source's
pending-audit status line with the link to this audit; no theorem, proof or
trust-boundary text changed.

The separation conclusion remains deliberately nonterminal: its order is
only lower-bounded by seven, and no common boundary colouring is produced.

## 1. Spanning normalization with two connected deficient branch sets

The given one-defect model makes the maximizing class nonempty, and finiteness
of `G` gives a model covering the maximum possible number of vertices.  In
the no-`K_7` branch, the two exceptional connected branch sets `C,D` are
anticomplete, because one edge between them would supply the only missing
model adjacency.

Let `K` be a component outside the seven branch sets.  Connectedness of `G`
makes its contact family `I_K` nonempty.  If `K` contacts both `C` and `D`, a
path through `K` has one end in each branch set and all internal vertices in
`K`.  Adding those internal vertices to `D` preserves connectedness,
disjointness and every old contact, while creating the missing `CD` contact.
This is an explicit `K_7`-minor model.

Otherwise `I_K` does not contain both members of the only nonadjacent pair,
so it is a clique in the branch-set contact graph.  For any `Q in I_K`, the
set `Q union K` is connected and disjoint from the six other branch sets.
Every new contact supplied through `K` is with another member of `I_K`, which
was already adjacent to `Q`; every old contact of `Q` is retained.  Replacing
`Q` by `Q union K` therefore gives a larger model of the same labelled form.
Maximality excludes all exterior components, so the seven connected branch
sets partition `V(G)`.  No singleton hypothesis is used.

## 2. The connected-centre two-mark split

For a spanning one-defect model, the full neighbourhood `N_G(C)` separates
the nonempty connected set `C` from the nonempty set `D`.  Seven-connectivity
therefore gives `|N_G(C)|>=7`.  Spanningness and anticompleteness of `C,D`
place all of `N_G(C)` in the five common branch sets `U_1,...,U_5`; hence one
of them contains two distinct vertices with neighbours in `C`.

The minimal-subtree argument in `U_1` is valid with a connected centre.  Its
terminals are an arbitrary protected vertex `rho` and all marked vertices
of `U_1` that have neighbours in `C`.  A minimal subtree containing at least
two marked vertices has a marked leaf `m ne rho`.  Removing the incident
tree edge from the full spanning tree partitions `U_1` into adjacent,
nonempty connected sets `Z,W`, with `rho in W`, a marked vertex in `Z`, and
another marked vertex in `W`.  Thus both parts are adjacent to the connected
branch set `C`; the contacts need not use the same vertex of `C`.

If `Z` misses `D`, then `N_G(Z)` is the boundary of an actual separation:
the two open sides contain `Z` and `D`.  If `W` misses some `U_j`, then
`N_G(W)` analogously separates `W` from that nonempty branch set.

In the remaining case the seven displayed branch sets

\[
C,\quad D\cup Z,\quad W,\quad U_2,U_3,U_4,U_5
\]

are pairwise disjoint and connected.  The assumed `DZ` contact makes
`D union Z` connected; the cut tree edge gives its contact with `W`; `D`
supplies all contacts from `D union Z` to the four untouched bags; `W`
retains its contacts to those bags; and the marked vertices in `Z,W` give
the two required contacts from `C`.  All other contacts come from the
original clique model.  Hence this is a literal seven-branch-set
`K_7`-minor model.

The first sentence of Theorem 2 already shows that `N_G(C)` itself is a
valid full-neighbourhood separation.  Thus the subsequent two-mark split is
stronger than is needed for the theorem's stated separation alternative,
but it is correct and introduces no circularity.

## 3. Separator order and fullness

Every returned set is the full neighbourhood of a nonempty proper connected
set and has another nonempty branch set outside the connected set and its
neighbourhood.  It is therefore the boundary of an actual separation with
two nonempty open sides.

Seven-connectivity gives boundary order at least seven.  At order seven, if
a component of the boundary deletion missed a boundary vertex, all of its
neighbours would lie among the other six boundary vertices.  Since the
separation is actual, deleting those at most six vertices would disconnect
the graph, contradicting seven-connectivity.  Thus every component meets
every boundary vertex at equality.

## 4. Symmetric two-root reduction

Theorem 3 assumes that one of the two disjoint adjacent connected roots meets
all five `K_5` bags and the other meets at least four.  If both meet all five,
the roots and the five bags directly form a `K_7` model.  Otherwise the names
may be oriented so `R_0` meets all five, while `R_1` meets exactly four and is
anticomplete to `M_5`.

Then

\[
R_1,\quad M_5,\quad R_0,\quad M_1,M_2,M_3,M_4
\]

are seven disjoint connected branch sets with only the `R_1M_5` contact
missing.  Theorem 1 supplies either `K_7` or a spanning one-defect model with
two connected exceptional branch sets.  Theorem 2 applies directly; it does
not require either exceptional branch set to be a singleton.  Therefore the
argument is invariant under interchanging the original two roots.

For the pentagonal-bipyramid consequence, a model bag meeting
`A=N_G(R_0) intersect V(F)` is exactly a bag adjacent to `R_0`, and similarly
for `B` and `R_1`.  Five contacts to either one of `A,B` and four to the other
therefore satisfy Theorem 3 in the corresponding orientation.

## Trust boundary

The strengthened theorem does **not** prove:

- that the returned separation has order at most seven or is minimum;
- that either original root survives as a prescribed branch set after the
  spanning maximization;
- that both closed shores induce a common equality partition on the
  boundary;
- that proper-minor colourings align across the separation; or
- that the separation outcome closes the live `HC_7` branch.

The source states the first, third, fourth and fifth limitations accurately.
Its conclusion needs no preservation of the original root labels: it uses
the spanning model only to invoke the connected-centre theorem.
