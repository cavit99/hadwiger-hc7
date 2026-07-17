# Pentagonal order-seven separation completion

**Status:** written proof; separate internal audit GREEN.

## Theorem

Let `G` be a 7-connected graph.  Suppose that

\[
S=\{p,q,c_1,c_2,c_3,c_4,c_5\}
\]

induces the join of the edge `pq` and the chordless cycle

\[
C=c_1c_2c_3c_4c_5c_1.
\]

Suppose also that `G-S` has exactly two nonempty connected components `A`
and `B`.  If `G-\{p,q\}` contains a `K_5` minor, then `G` contains a
`K_7` minor.

The proof uses the following established result.

> **Martinsson--Steiner, Lemma 3.1.**  Let `F` be a 3-connected graph and
> let `X\subseteq V(F)`, with `|X|\ge 4`, be *spread out*: every separation
> `(U,W)` of `F` of order three satisfies
> `X\setminus U\ne\varnothing\ne X\setminus W`.  If `F` has no `X`-rooted
> `K_4` minor, then the graph obtained from `F` by adding a new vertex
> adjacent to every vertex of `X` is planar.

Here an `X`-rooted `K_4` minor means four pairwise disjoint connected
branch sets, pairwise adjacent, each meeting `X`.  The cited statement is
Lemma 3.1 of Anders Martinsson and Raphael Steiner, *Strengthening
Hadwiger's conjecture for 4- and 5-chromatic graphs*, Journal of
Combinatorial Theory, Series B 164 (2024), 1--16; see also
<https://arxiv.org/abs/2209.00594>.

## Proof

Put

\[
H=G-\{p,q\},\qquad F_A=H[A\cup V(C)],\qquad
F_B=H[B\cup V(C)].
\]

### 1. Full attachment and connectivity of the shore graphs

Each of `A` and `B` is adjacent to every vertex of `S`.  Indeed, if, say,
`A` had no neighbour at some `s\in S`, then

\[
N_G(A)\subseteq S-\{s\},
\]

and the nonempty component `B` would lie on the other side of a separation
of order at most six, contrary to 7-connectivity.

Deleting two vertices from a 7-connected graph leaves a 5-connected graph,
so `H` is 5-connected.

We next show that each of `F_A,F_B` is 3-connected.  By symmetry, consider
`F_A`, and let `Z\subseteq V(F_A)` with `|Z|\le 2`.  Every component of
`F_A-Z` meets `V(C)-Z`: otherwise such a component `D\subseteq A` has
`N_H(D)\subseteq Z`, contradicting 5-connectivity of `H`.

If `Z` contains a vertex of `A`, then `Z` contains at most one vertex of
`C`, and `C-Z` is connected.  Hence all components of `F_A-Z` that meet
`C-Z` coincide.  If `Z\subseteq V(C)`, then `A` is untouched, remains
connected, and has a neighbour at every vertex of `C-Z`; again `F_A-Z` is
connected.  Thus `F_A` is 3-connected, and the same proof applies to
`F_B`.

The set `V(C)` is spread out in each shore graph.  For suppose that
`(U,W)` is a separation of `F_A` of order three and, for example,
`V(C)\subseteq U`.  Then the nonempty set `W-U` lies in `A`, has no edge to
`B`, and has all its neighbours in `U\cap W`.  This contradicts
5-connectivity of `H`.  The case `V(C)\subseteq W` is symmetric, as is the
argument for `F_B`.

### 2. A rooted `K_4` on either shore gives the seven branch sets

Suppose `F_A` has a `V(C)`-rooted `K_4` minor with branch sets
`M_1,M_2,M_3,M_4`.  Then

\[
M_1,M_2,M_3,M_4,\quad B,\quad \{p\},\quad \{q\}
\]

are the branch sets of a `K_7` minor in `G`:

- the first four branch sets form a `K_4` model;
- `B` is connected and, because it is adjacent to every vertex of `C`, is
  adjacent to every `M_i`;
- `p` and `q` are adjacent to each other and to every `M_i`, since each
  `M_i` meets `C`; and
- full attachment of `B` to `S` gives edges from each of `p,q` to `B`.

The same conclusion holds if `F_B` has a `V(C)`-rooted `K_4` minor.

Consequently, if `G` has no `K_7` minor, then neither shore graph has a
`V(C)`-rooted `K_4` minor.

### 3. If neither rooted model exists, both shores lie in discs

Apply Martinsson--Steiner Lemma 3.1 to each of `F_A,F_B` with root set
`V(C)`.  The preceding section verifies its connectivity and spread
hypotheses.  We obtain planar graphs `F_A^+` and `F_B^+`, where `F_X^+` is
formed from `F_X` by adding a new vertex `a_X` adjacent to all five
vertices of `C`.

We record why this gives a disc embedding of `F_X` whose boundary is `C`,
rather than merely an unspecified planar embedding.  In a planar drawing
of `F_X^+`, the cycle `C`, the vertex `a_X`, and the five incident edges
contain the wheel with rim `C`.  The five triangular regions on the
`a_X`-side of the rim have boundaries

\[
a_Xc_ic_{i+1}a_X \qquad (i\pmod 5).
\]

No vertex of `F_X-C` can lie in one of those regions.  Otherwise a
component drawn there has no neighbour outside the two rim vertices
`c_i,c_{i+1}`: the added vertex `a_X` has no neighbour outside `C`.
Those two rim vertices would separate that component in `F_X`, contrary
to 3-connectivity.  It follows that all of `F_X-C` lies on the side of
`C` opposite `a_X`.  After deleting `a_X` and reversing the outer face if
necessary, `F_X` has a planar disc embedding with the chordless cycle `C`
as its boundary.

Choose such disc embeddings of `F_A` and `F_B`, reverse one cyclic
orientation, and glue their boundary copies of `C`.  There are no edges
between `A` and `B`, so this gives a planar embedding of `H`.

But `H` contains a `K_5` minor by hypothesis, whereas every minor of a
planar graph is planar and `K_5` is not planar.  This contradiction proves
that one shore has a `V(C)`-rooted `K_4` minor, and Section 2 then gives an
explicit `K_7` minor in `G`.  \(\square\)

## Corollary for a minimal `HC_7` counterexample

No minor-minimal 7-chromatic graph with no `K_7` minor has a separation
satisfying the theorem's hypotheses except for the displayed assumption
that `G-\{p,q\}` contains a `K_5` minor.

Indeed, if `G-\{p,q\}` were 4-colourable, those four colours together with
two new colours on the adjacent vertices `p,q` would give a 6-colouring of
`G`.  Hence

\[
\chi(G-\{p,q\})\ge 5.
\]

Hadwiger's conjecture for `t=5` (equivalently, the Four Colour Theorem
together with Wagner's reduction) then supplies a `K_5` minor in
`G-\{p,q\}`.  The theorem supplies the forbidden `K_7` minor.

## Scope

This theorem is host-level and unbounded.  It does not assert the stronger
standalone statement that every 5-connected graph with two full shores
behind an induced 5-cycle has a `V(C)`-rooted `K_5` minor.  The two extra
boundary vertices `p,q`, including their full attachment to both shores,
are used essentially in the seven-branch-set construction.
