# Independent audit: biportal rooted-`K_4` web exchange

## Verdict

**GREEN AS PATCHED.**  The parameter-uniform `r+3` displayed branch sets
are nonempty, connected, pairwise disjoint and pairwise adjacent under
exactly the stated literal placement hypotheses.  Two residual occurrences
of “four” in the general hypotheses were replaced by `r`; the four- and
three-connected selection corollaries correctly remain specialized to
rooted `K_4`.  The note does not infer disjoint portal extensions from
torso data; it correctly leaves their selection as the finite
capacity-state problem.

## 1. Rooted bags and extensions

Let `L_i` be the `r` disjoint rooted branch sets in `W`.  Since
`E_i cap W={p_i}` and `p_i in L_i`, each `F_i=L_i union E_i` is
connected.  Distinct `F_i` are disjoint: the `L_i` are disjoint, the
`E_i` are pairwise disjoint, and an `E_i` meets the whole torso only in
its own distinct root.  Rooted-`K_r` adjacency makes the `r` sets `F_i`
pairwise adjacent.  Their named extension edges give literal adjacency
to each of `B,T,U`; no quotient or virtual edge is used.

Consequently `F_1,...,F_r,U` is a `K_{r+1}` model: the first `r` bags are
pairwise adjacent, each sees `U`, and all `r+1` see both boundary pools.

## 2. The two boundary bags

The bag `R union T` is connected even when `T` is disconnected, because
condition 3 gives every vertex of `T` a neighbour in connected `R`.
It is disjoint from `B,U,F_1,...,F_r` by condition 1.  Its adjacencies to
the `r+1` frame bags are the `T-E_i` and `T-U` edges; its adjacency to
`B` is supplied by `R`.  The other boundary bag `B` is connected and
sees the same `r+1` frame bags by the `B-E_i` and `B-U` edges.  Finally
`B` sees `R union T` through `R`.  Thus

```text
F_1,...,F_r,U,B,R union T
```

is a literal `K_{r+3}` model.  No vertex is assigned twice; the bag count
is `r+1+2=r+3`.

## 3. Rooted-`K_4` obstruction wording

For a four-connected graph, Fabila-Monroy--Wood Theorem 6 gives a rooted
`K_4` unless the graph is planar and the four roots are cofacial.  Hence
Corollary 1.2 is exact.

For a three-connected graph, their Theorem 8 says that a rooted `K_4`
exists exactly when the graph is not a spanning subgraph of a web with
the four nominated vertices on its outer frame.  Such a web may contain
the permitted clique pieces inserted at facial triangles and need not be
planar.  Their planar specialization (Theorem 9) gives the common-face
form.  Corollary 1.3 and its qualification therefore use no stronger
statement.

## 4. Exact scope in a torso

The general theorem requires `r` pairwise disjoint extensions, each meeting the
torso only at its own root and each carrying all three named adjacencies
to `B,T,U`.  An adhesion-two lobe may meet two roots or be indispensable
for two extensions; the theorem does not silently duplicate it.  Such a
shared lobe is explicitly a failure of the placement hypotheses.

Likewise, if `W` is a Tutte torso, a rooted model may use virtual edges.
It must first be expanded through the corresponding pairwise disjoint
decomposition bridges before Theorem 1.1 is applied in the original
graph.  The source states this limitation correctly.
