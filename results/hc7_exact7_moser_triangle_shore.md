# The triangular exterior shore in the pure-Moser crossing

**Status:** proved, computer-assisted, and independently audited.

## 1. Exact setting

Let `G` be seven-connected and let `v` have the seven-vertex Moser
neighbourhood

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Suppose one component of `G-N[v]` contains two vertex-disjoint paths
`P_05,P_24`, with interiors outside `N[v]`, joining respectively `0` to `5`
and `2` to `4`.  Suppose a different component is a triangle

\[
                         D=\{x_1,x_2,x_3\},
\]

and is `N(v)`-full.  Assume `delta(G)>=7`.  These are exactly the tiny-shore
hypotheses left by the audited pure-Moser crossing and low-cut theorems.

### Theorem 1 (triangular shore closure)

Under these hypotheses, `G` contains a literal `K_7` model.

## 2. Finite crossed-page lemma

For `i=1,2,3`, put

\[
                 D_i=N(v)-N_G(x_i).
\]

Each `x_i` has two neighbours in its triangle.  Minimum degree seven gives

\[
                         |D_i|\le2.                       \tag{2.1}
\]

Fullness of the triangle is exactly

\[
                         D_1\cap D_2\cap D_3=\varnothing. \tag{2.2}
\]

Contract the interiors of `P_05` and `P_24` separately, retaining one
internal vertex on each path.  This produces the ten-vertex **crossed page**
`W`: the seven literal boundary vertices, `v`, and length-two paths

\[
                         0-p_{05}-5,
                 \qquad 2-p_{24}-4.                      \tag{2.3}
\]

The following finite statement is certified exhaustively.

### Lemma 2 (three-defect transversal `K_4`)

For every unordered triple `(D_1,D_2,D_3)` of subsets of the seven-set,
each of order at most two and satisfying (2.2), the crossed page `W` has
four pairwise disjoint connected pairwise adjacent bags

\[
                         B_1,B_2,B_3,B_4                 \tag{2.4}
\]

such that, for every `i`, every bag contains a literal boundary vertex
outside `D_i`.  Equivalently, each `x_i` has a neighbour in every `B_j`.

#### Exhaustive certificate

`../results/hc7_exact7_moser_triangle_shore_verify.py` is dependency-free.
It enumerates every nonempty connected subset of `W` meeting the literal
boundary, and then every four-tuple of disjoint such sets.  It retains a
tuple exactly when all six bag adjacencies are literal edges of `W`.
There are 598 distinct boundary traces of such `K_4` models.

There are 29 possible defects of order at most two.  The verifier then
checks all unordered triples, discarding precisely those with nonempty total
intersection.  For each remaining triple it requires every one of the four
model traces to meet each of the three literal contact sets.  It checks 3928
triples and finds no failure.  No graph-minor oracle or external package is
used.

Run

```text
python3 results/hc7_exact7_moser_triangle_shore_verify.py
```

from the repository root.  The script prints exact counts and a SHA-256 hash
of the canonical state-to-witness table.  The current output is

```text
boundary_K4_models=598
defect_triples=3928 failures=0
certificate_sha256=f98e3da2c226d53104ba3bfb877cb18b1be9dd65c50363201414d939f63f123e
```

## 3. Literal lift and proof of Theorem 1

For the actual defect triple, choose the four bags from Lemma 2.  Before the
contractions defining `W`, pass to the subgraph consisting of `N[v]` and the
two selected paths, deleting every unused vertex and edge.  The inverse image
of `p_05` is the whole nonempty connected
interior of `P_05`, and similarly for `p_24`.  Replace either quotient vertex
which occurs in a bag by its entire inverse image.  Minor-model lifting then
preserves bag disjointness, connectivity, and every bag adjacency.  Thus
(2.4) lifts to four literal bags in the original crossed component together
with `N[v]`.

Use the three singleton bags

\[
                         \{x_1\},\{x_2\},\{x_3\}.        \tag{3.1}
\]

They are pairwise adjacent because `D` is a triangle.  By Lemma 2, each is
adjacent to every lifted `B_j` through a literal boundary contact.  Hence the
four lifted bags and the three bags in (3.1) are seven disjoint connected
pairwise adjacent sets: a literal `K_7` model.  This proves Theorem 1.

## 4. Trust boundary

The theorem closes the entire order-three exterior component in the
favourable pure-Moser crossing; it does not use or prove any statement about
a 3-connected shore of order at least four.  The only finite input is the
explicit ten-vertex crossed-page lemma.
