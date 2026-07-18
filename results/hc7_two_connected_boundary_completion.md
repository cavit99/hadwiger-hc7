# Completion across a two-connected boundary core

**Status:** written proof; separate internal audit GREEN.  This note proves a
rooted-minor/planarity closure theorem for one structural family of bounded
two-shore interfaces.  It does not prove `HC_7` and does not synchronize
arbitrary four-colour boundary-extension relations.

## 1. The theorem

### Theorem 1 (two-connected-core completion)

Let `G` be a seven-connected graph with a vertex partition

\[
             V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}
                    \{p,q\}\mathbin{\dot\cup}B .       \tag{1.1}
\]

Assume that:

1. `A` and `B` are nonempty and connected, and there is no edge between
   `A` and `B`;
2. every vertex of `X union {p,q}` has a neighbour in `A` and a neighbour
   in `B`;
3. `pq` is an edge and each of `p,q` is adjacent to every vertex of `X`;
4. `|X|>=4` and `G[X]` is two-connected; and
5. `G-{p,q}` contains a `K_5` minor.

Then `G` contains a `K_7` minor.

The external input is Lemma 3.1 of Anders Martinsson and Raphael Steiner,
*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*,
Journal of Combinatorial Theory, Series B 164 (2024), 1--16,
<https://doi.org/10.1016/j.jctb.2023.08.009>:

> If `F` is three-connected, `Y subseteq V(F)` has order at least four and
> is spread out across every order-three separation of `F`, and `F` has no
> `Y`-rooted `K_4` minor, then the graph obtained from `F` by adding a new
> vertex adjacent to every vertex of `Y` is planar.

Here a set `Y` is *spread out* when neither closed side of an order-three
separation contains all of `Y`.  A `Y`-rooted `K_4` model has four disjoint,
pairwise adjacent connected branch sets, each meeting `Y`.

## 2. Connectivity and spread of the boundary core

Put

\[
 H=G-\{p,q\},\qquad F_A=H[A\cup X],\qquad F_B=H[B\cup X]. \tag{2.1}
\]

The graph `H` is five-connected because `G` is seven-connected.

We first show that `F_A` is three-connected.  Let
`Z subseteq V(F_A)` have order at most two.  Every component of `F_A-Z`
meets `X-Z`.  Indeed, a component `D` which did not meet `X-Z` would lie
in `A`, and every neighbour of `D` in `H` would lie in `Z`: there are no
`A-B` edges, and all remaining vertices of `A union X` outside `D` are
separated from it in `F_A-Z`.  Since `B` is nonempty, `Z` would separate
`D` from `B` in the five-connected graph `H`, a contradiction.

If `Z` contains no vertex of `A`, then `A` remains connected and is
adjacent to every vertex of `X-Z`; hence `F_A-Z` is connected.  If `Z`
contains a vertex of `A`, then at most one vertex of `X` was deleted.
Two-connectivity of `G[X]` makes `G[X-Z]` connected, and every component
of `F_A-Z` meets that one connected subgraph.  Again `F_A-Z` is connected.
Thus `F_A` is three-connected.  The same proof applies to `F_B`.

The set `X` is spread out across every order-three separation of `F_A`.
Suppose instead that `(U,W)` is such a separation with `X subseteq U`.
Then the nonempty set `W-U` lies in `A`, and

\[
                         N_H(W-U)\subseteq U\cap W .   \tag{2.2}
\]

There are no edges from `A` to `B`, and the separation excludes edges from
`W-U` to `U-W`.  Hence the three vertices of `U cap W` separate `W-U`
from the nonempty set `B` in `H`, contrary to five-connectivity.  The
opposite orientation is symmetric.  Thus `X` is spread out in `F_A`, and
symmetrically in `F_B`.

## 3. The rooted-model outcome

Suppose `F_A` has an `X`-rooted `K_4` model with branch sets
`M_1,M_2,M_3,M_4`.  Then

\[
           M_1,M_2,M_3,M_4,\qquad B,\qquad \{p\},\qquad\{q\} \tag{3.1}
\]

are the branch sets of a `K_7` minor in `G`.

The first four branch sets form a `K_4` model and each meets `X`.
Fullness of `B` makes it adjacent to each of them and to both singleton
branch sets.  Each of `p,q` is complete to `X`, so both singleton branch
sets are adjacent to every `M_i`; they are adjacent to each other through
the edge `pq`.  All seven sets in (3.1) are disjoint and connected.
The same construction applies with `A,B` interchanged.

It remains to assume that neither `F_A` nor `F_B` has an `X`-rooted
`K_4` minor.

## 4. The planar outcome and cofacial gluing

Apply Martinsson--Steiner's lemma to `F_A` and `F_B`.  For each shore, add
a new vertex adjacent to every vertex of `X`; denote the resulting planar
graphs by `F_A^+` and `F_B^+`.

We record the elementary planar consequence needed for gluing.  In a
planar embedding of `F_A^+`, delete the new vertex.  All vertices of `X`
are incident with the resulting common face.  Restricting this embedding
further to `G[X]` gives an outerplane embedding of `G[X]`.  Since `G[X]`
is two-connected, the boundary of its outer face is a Hamiltonian cycle
`C` through all vertices of `X`.

This Hamiltonian cycle is intrinsic.  We use the standard outerplanar
fact that every two-connected outerplanar graph has a unique Hamiltonian
cycle, namely the boundary cycle of its outer face.  (Equivalently, an
outer-face chord separates the two open boundary arcs, so no Hamiltonian
cycle can use that chord and still traverse both arcs.)
Consequently the planar embeddings obtained from `F_A^+` and `F_B^+`
give the same cycle `C`, up to reversal.

There is also a direct way to locate each open shore.  In the embedding of
`F_A^+`, the new vertex together with `C` is a wheel.  The connected set
`A`, which is disjoint from the wheel vertices, lies in one face of this
wheel.  It cannot lie in a triangular face incident with the new vertex:
such a face has only two vertices of `X` on its boundary, whereas `A` has
a neighbour at every vertex of `X` and `|X|>=4`.  Hence `A` lies in the
closed disc bounded by `C` on the side opposite the new vertex.  Deleting
the new vertex therefore gives a planar disc drawing of `F_A` with `C` as
its boundary.  Every chord of `C` in `G[X]` lies in this same disc: the
other side is divided by the wheel spokes into triangular faces, and a
nonconsecutive chord cannot be drawn inside one of them.  The same
argument gives such a disc drawing of `F_B`.

Reflect one disc and identify the two boundary copies of `C`.  Retain the
drawings of all edges of `G[X]` in the `A`-disc.  In the `B`-disc erase
only the duplicate drawings of the chords
`E(G[X])-E(C)` before gluing; deleting those curves cannot create a
crossing, and the same graph edges are already represented in the other
disc.  Because there are no `A-B` edges, the glued drawing is a planar
embedding of the whole graph

\[
                              H=G-\{p,q\}.             \tag{4.1}
\]

This contradicts hypothesis 5, since a planar graph has no `K_5` minor.
Thus one of the rooted-model outcomes in Section 3 must occur, and its
seven displayed branch sets prove the theorem.  \(\square\)

## 5. Consequence for a hypothetical minimal counterexample

Assume the established case `HC_5`.  In a seven-chromatic graph, deleting
two vertices leaves chromatic number at least five.  Therefore, in a
hypothetical minor-minimal counterexample to `HC_7`, the `K_5`-minor
hypothesis of Theorem 1 is automatic for every pair `p,q`: `HC_5` applies
to `G-{p,q}`.

Consequently an exact two-shore separation in such a graph cannot have a
boundary of the form

\[
                         G[\{p,q\}\cup X],             \tag{5.1}
\]

where `pq` is an edge, `p,q` are complete to the two-connected remainder
`X`, and both open shores are connected and full to the boundary.

This strictly extends the induced-cycle completion mechanism: extra edges
inside the two-connected core `X` are allowed, and the Hamiltonian rim is
recovered from the planar alternative rather than assumed in advance.

## 6. Exact scope

The theorem requires an **adjacent** universal pair on the boundary and a
two-connected remainder.  It does not apply merely because contracting
the two anticomplete shores produces the minor
`I_2 join G[S]`; those two contracted vertices are nonadjacent.  It also
does not align arbitrary boundary-colouring responses when
`chi(G[S])<=4`.

In particular, the even/odd matching-language barrier on
`K_4 dotunion K_4` has a four-colourable boundary, independence number
two, a `K_7`-minor-free quotient `I_2 join G[S]`, and every exact
independent-block response on both abstract shores, while its two response
families remain disjoint.  Therefore any closure of the remaining general
bounded interface must use full host-level contraction-critical
transitions or additional labelled minor-model geometry; the static
boundary data alone cannot supply a common partition.
