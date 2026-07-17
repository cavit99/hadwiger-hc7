# Cycle-boundary completion theorem

**Status:** written proof; separate internal audit GREEN.

## Theorem

Let `G` be a 7-connected graph, let `C` be an induced cycle of length at
least four, and let `p,q\in V(G)-V(C)` be adjacent vertices, each adjacent
to every vertex of `C`.  Suppose

\[
G-(V(C)\cup\{p,q\})
\]

has exactly two nonempty connected components `A,B`, and each of `A,B` is
adjacent to every vertex of `V(C)\cup\{p,q\}`.  If `G-\{p,q\}` contains a
`K_5` minor, then `G` contains a `K_7` minor.

The theorem uses Lemma 3.1 of Anders Martinsson and Raphael Steiner,
*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*,
Journal of Combinatorial Theory, Series B 164 (2024), 1--16,
<https://doi.org/10.1016/j.jctb.2023.08.009>:

> If `F` is 3-connected, `X\subseteq V(F)` has order at least four and is
> spread out across every order-three separation of `F`, and `F` has no
> `X`-rooted `K_4` minor, then adding a new vertex adjacent to every member
> of `X` produces a planar graph.

Here `X` is *spread out* if every order-three separation `(U,W)` satisfies
`X\setminus U\ne\varnothing\ne X\setminus W`; an `X`-rooted `K_4` minor
has four pairwise adjacent, pairwise disjoint connected branch sets, each
meeting `X`.

## Proof

Set

\[
H=G-\{p,q\},\qquad F_A=H[A\cup V(C)],\qquad
F_B=H[B\cup V(C)].
\]

Deleting two vertices from a 7-connected graph leaves a 5-connected
graph, so `H` is 5-connected.

We first verify the hypotheses of Martinsson--Steiner for each shore
graph.  Consider `F_A`.  If `Z\subseteq V(F_A)` and `|Z|\le2`, every
component of `F_A-Z` meets `C-Z`; otherwise such a component lies in `A`
and has all its neighbours in `H` contained in `Z`, contradicting
5-connectivity.  If `Z` meets `A`, then at most one cycle vertex is
deleted, so `C-Z` is connected.  If `Z\subseteq V(C)`, the connected graph
`A` is untouched and has a neighbour at every remaining cycle vertex.
Thus `F_A-Z` is connected in either case, and `F_A` is 3-connected.

Moreover, `V(C)` is spread out in `F_A`.  If an order-three separation
`(U,W)` had `V(C)\subseteq U`, then the nonempty set `W-U\subseteq A`
would have all its neighbours in `H` contained in `U\cap W`: it has no
edge to `B`, and the separation excludes edges to `U-W`.  This contradicts
5-connectivity of `H`.  The case `V(C)\subseteq W` is symmetric.  The same
arguments apply to `F_B`.

If `F_A` has a `V(C)`-rooted `K_4` model with branch sets
`M_1,M_2,M_3,M_4`, then

\[
M_1,M_2,M_3,M_4,\quad B,\quad\{p\},\quad\{q\}
\]

form a `K_7` minor in `G`.  The four `M_i` form a `K_4` model; `B` is
connected and is adjacent to every `M_i` through a cycle vertex in that
branch set; `p` and `q` are adjacent to each `M_i`, to `B`, and to each
other.  The same construction works with `A,B` interchanged.

It remains to suppose that neither shore graph has a `V(C)`-rooted `K_4`
minor.  Martinsson--Steiner Lemma 3.1 then says that each graph obtained
from `F_A,F_B` by adding a new vertex complete to `V(C)` is planar.

In such a planar embedding, the added vertex together with `C` forms a
wheel.  The connected shore lies in one face of this embedded wheel.  It
cannot lie in a triangular face incident with the added vertex: that face
has only two cycle vertices on its boundary, whereas the shore is adjacent
to every vertex of `C`.  Hence the shore lies on the side of `C` opposite
the added vertex.  Deleting the added vertex gives a planar disc embedding
of the shore graph with `C` as its boundary.

Take these disc embeddings of `F_A,F_B`, reflect one, and identify their
boundary copies of `C`.  Since there are no edges between `A` and `B`, this
is a planar embedding of `H`.  This is impossible because `H` contains a
`K_5` minor.  Therefore one shore has the rooted `K_4` model above, and its
seven displayed branch sets give a `K_7` minor in `G`.  \(\square\)

## Scope

The theorem does not assert a cycle-rooted `K_5` minor in `G-\{p,q\}`.
The two additional vertices `p,q` and their adjacencies to the two shores
are used in the explicit `K_7` model.  The result requires the two open
shores to be connected and fully adjacent to the displayed boundary; it
does not cover an arbitrary separation with more components or incomplete
boundary attachment.
