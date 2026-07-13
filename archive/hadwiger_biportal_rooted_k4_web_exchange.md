# Biportal rooted-model exchange: clique completion or one rooted web

## 1. The labelled completion theorem

This theorem composes two uniform ideas: a rooted clique inside one
carrier torso and pooling all boundary vertices into two connected bags.
It is the precise form in which a crossing/rooted-model outcome closes;
no portal label is inferred from a quotient contraction.

Let `r>=1`, and let `B,T,R,U,W,E_1,...,E_r` satisfy the following
conditions in a graph `G`.

1. The sets are disjoint except that
   `E_i cap V(W)={p_i}`, where `p_1,...,p_r` are distinct vertices of
   `W`.
2. `B,R,U,E_1,...,E_r` are connected; `T` is nonempty (it need not be
   connected).
3. `R` is adjacent to every vertex of `B union T`.
4. The extensions `E_i` are pairwise disjoint, and each `E_i` is
   adjacent to `B`, to `T`, and to `U`.
5. `U` is adjacent to both `B` and `T`.

Here adjacency to a set means that at least one literal edge has its
other end in that set.

### Theorem 1.1 (uniform biportal rooted-core exchange)

If `W` contains a `K_r` minor rooted at `p_1,...,p_r`, then `G`
contains a `K_{r+3}` minor.

#### Proof

Let `L_i` be the `r` rooted branch sets in `W`, with `p_i in L_i`.
Put

\[
                              F_i=L_i union E_i.
\]

The sets `F_i` are connected, pairwise disjoint and pairwise adjacent.
They are disjoint because the rooted bags are disjoint and each extension
meets `W` only at its own root.  Each `F_i` is adjacent to `U`, `B`, and
`T`.  The set `U` is adjacent to `B` and `T` as well.  Hence

\[
             F_1,\ldots,F_r,U
\]

is a protected `K_{r+1}` frame whose every bag sees both boundary pools.

The set `R union T` is connected: every vertex of `T` has a neighbour in
the connected set `R`.  It is adjacent to `B` through `R`, to every
`F_i` through the named `T`-portal, and to `U` through its `T`-portal.
The connected bag `B` is adjacent to all `r+1` frame bags by their named
`B`-portals.  Thus

\[
                    F_1,\ldots,F_r,U,B,R union T
\]

are `r+3` disjoint connected pairwise adjacent bags.  QED.

### Corollary 1.2 (four-connected torso dichotomy)

In the specialization `r=4`, if `W` is four-connected, then either `G`
contains a `K_7` minor or `W`
is planar with `p_1,p_2,p_3,p_4` on one face.

#### Proof

The four-connected case of the Fabila-Monroy--Wood rooted-`K_4` theorem
gives the rooted model unless `W` is planar and the four roots are
cofacial.  Apply Theorem 1.1 in the first outcome.  QED.

### Corollary 1.3 (three-connected rooted-web dichotomy)

In the specialization `r=4`, if `W` is three-connected, then either `G`
contains a `K_7` minor or
`W`, with the four named roots, lies in the rooted-web obstruction class
of the three-connected rooted-`K_4` theorem.  In particular, in the
planar subcase all four roots lie on one face.

#### Proof

Apply the three-connected characterization of rooted `K_4` minors.  Its
rooted-model outcome closes by Theorem 1.1; its other outcome is exactly
the stated rooted web (a spanning subgraph of the corresponding planar
rib with the permitted facial clique pieces).  QED.

## 2. Carrier interpretation

In the torso--Helly reduction, an extension `E_i` may consist of the root
`p_i` together with one or more named dark lobes on adhesions at `p_i`.
The hypotheses above are therefore literal placement conditions:

* every selected root extension must have one portal to each of the two
  boundary pools;
* the `r` extensions must be disjoint; and
* one reserved connected bag `U` must contact all `r` extensions and
  both pools.

When these conditions hold, the entire 3-connected carrier core is
closed at arbitrary order.  For fixed `r`, when they fail, the failure is
a finite capacity state on the root extensions (a missing pool contact,
a shared lobe, or a missing reserve adjacency), not a failure of the
rooted-`K_r` theorem itself.

## 3. Audit boundary

The web alternative is not declared planar when facial clique pieces are
present; only the four-connected or explicitly planar subcase has the
plain cofacial conclusion.  Virtual torso edges are also not used as
literal edges: any rooted model in a torso must first be expanded through
the corresponding decomposition bridges before Theorem 1.1 is applied
in the original graph.
