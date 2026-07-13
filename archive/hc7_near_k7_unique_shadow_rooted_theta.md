# The unique-shadow rainbow connector always extends to a theta

## Status

This note closes the `d=1` non-rainbow crossed-theta residue in
`hc7_near_k7_bipartite_shadow_exchange.md`.  The missing input is a
standard prescribed-end fan extension, not a new path-exchange theorem.

The proof is label-free and uniform.

## 1. A prescribed neighbour lies on a pole theta

### Lemma 1.1 (rooted-neighbour theta)

Let `K` be a 3-connected graph, let `u,w` be distinct nonadjacent
vertices, and let

\[
                     x\in N_K(u)-\{w\}.                       \tag{1.1}
\]

Then `K` contains three internally vertex-disjoint `u-w` paths, one of
which contains the edge `ux`.

#### Proof

Put `H=K-u` and `Y=N_K(u)`.  We first show that `H` contains a
`w-Y` fan of order three.  Otherwise set-Menger gives a set `S` of at
most two vertices meeting every path in `H` from `w` to `Y`.  In
`K-S`, the vertex `w` cannot reach `u`: the last edge of any such path
would enter `u` from a vertex of `Y-S`, and its preceding part would be
a `w-Y` path in `H-S`.  Since `uw` is absent, there is no exceptional
one-edge path.  Thus `S` separates `u,w` in `K`, contrary to
3-connectivity.

There is also a `w-Y` fan of order one with endpoint `x`: the graph
`H=K-u` is connected, so it contains a `w-x` path.  Apply the standard
Perfect fan-extension theorem (equivalently, augment the corresponding
strict-gammoid independent set).  The one prescribed endpoint `x` can
be retained while extending to a `w-Y` fan of order three.  Hence there
are internally disjoint paths

\[
                    Q_x,Q_y,Q_z                              \tag{1.2}
\]

from `w` to three distinct vertices `x,y,z in Y`, with common vertex
only `w` and with the first path ending at the prescribed `x`.
Appending the three distinct edges

\[
                         ux,uy,uz                            \tag{1.3}
\]

gives three internally vertex-disjoint `u-w` paths.  The first contains
`ux`.  \(\square\)

For completeness, the Perfect step can be viewed directly as a gammoid.
Delete `w`, add three source clones whose out-neighbourhood is
`N_H(w)`, direct every remaining edge both ways, and put unit capacity on
the original vertices.  Endpoint sets in `Y` reachable by disjoint paths
from source clones are the independent sets of a strict gammoid.  The
rank is at least three by the preceding Menger argument, and `{x}` is
independent because `H` has a `w-x` path.  The matroid extension axiom
extends `{x}` to an independent three-set, which translates back to the
fan used above.

## 2. Closure of the unique-shadow cell

Use the notation of
`hc7_near_k7_bipartite_shadow_exchange.md`.  Thus `r>=3`,

\[
                       C=S-\{b_j\},                           \tag{2.1}
\]

the apex `v` has the unique non-neighbour `b_j` in the singleton clique,
and the induced pole graph is

\[
                             K=G-C.                           \tag{2.2}
\]

### Theorem 2.1 (unique-shadow theta completion)

If `K` is 3-connected, then `G` contains a `K_{r+1}` minor.

#### Proof

Lemma 5.3 of the shadow-exchange note supplies a saturated vertex
`x in B` such that

\[
              x\sim b_i\quad(i\ne j),qquad
              x\sim v\ \hbox{or}\ x\sim b_j.               \tag{2.3}
\]

The poles `v,b_j` are nonadjacent.  If `x~v`, apply Lemma 1.1 in `K`
with `(u,w)=(v,b_j)`.  It gives three internally disjoint pole paths one
of which contains `x`.  If `x~b_j`, interchange the poles and apply the
same lemma.  In either case one member of the pole theta contains `x`
internally.

Because `x` is adjacent to every ordinary singleton `b_i`, `i!=j`, the
internal vertex set of that theta branch meets every portal class `P_i`.
It is therefore the rainbow branch required by Lemma 5.2 of the
shadow-exchange note.  That lemma gives the explicit `K_{r+1}` model.
\(\square\)

### Corollary 2.2 (`HC_7` unique shadow is empty)

In the seven-connected spanning singleton shell, the unique-shadow
outcome is impossible in a `K_7`-minor-free graph.

#### Proof

Here `r=6` and `|C|=4`.  The standard connectivity inequality gives

\[
                  \kappa(G-C)\ge\kappa(G)-|C|\ge3.          \tag{2.4}
\]

Apply Theorem 2.1.  \(\square\)

Thus outcome 4 of Theorem 6.1 in the shadow-exchange note is not a real
residue under its stated connectivity hypothesis.  Every rainbow pole
connector supplied by a saturated pole-adjacent vertex can be chosen as
one branch of a theta.

## 3. Audit boundary

1. The nonedge `uw` is used in the separator proof.  If `uw` is an edge,
   the conclusion is still easy in the intended application, but it is
   not needed: the unique shadow is precisely the nonedge `vb_j`.
2. Ordinary 2-connectivity is insufficient.  The proof spends
   3-connectivity exactly in the order-three fan.
3. The lemma prescribes the neighbour `x`, not an arbitrary preselected
   `u-w` path through `x`.  This is exactly enough here, because the one
   vertex `x` already carries every ordinary label.
4. No collective-contact error occurs: one literal branch contains the
   single vertex `x`, and that vertex itself lies in every ordinary
   portal class.

