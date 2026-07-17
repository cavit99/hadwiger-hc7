# Bichromatic component constraints after a bipartite contraction

**Status:** written proof; separate internal audit GREEN.  This note
strengthens the promoted bipartite-contraction palette
theorem.  It does not by itself construct a clique minor.

## 1. Setup

Let `k >= 4`, and let `G` be a `k`-chromatic graph such that every proper
minor of `G` is `(k-1)`-colourable.  Let

\[
                         Q=G[W]
\]

be a nontrivial connected induced bipartite subgraph, with fixed
bipartition `(A,B)`.  Contract `Q` to a vertex `q`, put `R=G-W`, and fix a
proper `(k-1)`-colouring `psi` of `G/Q`.  Write

\[
                         \gamma=\psi(q).
\]

For every colour `i != gamma`, define four terminal sets in `R` by

\[
 A_i=N_G(A)\cap \psi^{-1}(i),\qquad
 B_i=N_G(B)\cap \psi^{-1}(i).                         \tag{1.1}
\]

The promoted contraction-palette theorem proves that every `A_i` and
`B_i` is nonempty.

## 2. Diagonal component theorem

### Theorem 2.1 (diagonal bichromatic component)

For any two distinct colours `i,j != gamma`, some component `C` of

\[
                       R[\psi^{-1}(\{i,j\})]           \tag{2.1}
\]

meets both of the sets

\[
             A_i\cup B_j
             \quad\hbox{and}\quad
             A_j\cup B_i.                             \tag{2.2}
\]

Equivalently, one connected `i,j`-coloured subgraph has at least one of
the following four terminal profiles:

\[
 (A_i,A_j),\quad (A_i,B_i),\quad
 (B_j,A_j),\quad (B_j,B_i),                            \tag{2.3}
\]

possibly together with additional terminal contacts.

#### Proof

Suppose no component of (2.1) meets both sets in (2.2).  Interchange the
colours `i,j` on every component of (2.1) that meets `A_i\cup B_j`, and on
no other component.

After these interchanges, `A` has no external neighbour of colour `i`.
Indeed, every old `i`-coloured neighbour of `A` lies in `A_i` and was
changed to colour `j`.  No old `j`-coloured neighbour of `A` was changed
to `i`, because every component meeting `A_j` is disjoint from
`A_i\cup B_j` by the supposition.

Similarly, `B` has no external neighbour of colour `j`: every component
meeting `B_j` was interchanged, while every component meeting `B_i` was
left fixed.

Keep the changed colouring on `R`, colour every vertex of `A` with `i`,
and colour every vertex of `B` with `j`.  The two sides are independent,
every edge of `G[W]` joins the two sides, and `i != j`.  The preceding two
paragraphs show that no monochromatic edge joins `W` to `R`.  We have
therefore obtained a proper `(k-1)`-colouring of `G`, a contradiction.
\(\square\)

### Theorem 2.2 (full boundary component or separation)

For distinct `i,j != gamma`, let `D_{ij}` be the set of components of
(2.1) which meet at least one of

\[
                         A_i,A_j,B_i,B_j.              \tag{2.4}
\]

Then exactly one of the following holds.

1. `D_{ij}` consists of one component `K_{ij}`.  This component contains
   all four nonempty terminal sets in (2.4), and hence is adjacent to both
   bipartition sides in both colours.
2. `D_{ij}` has at least two members.  For every `L in D_{ij}`, the set
   `N_G(L)` is the boundary of an actual separation with two nonempty open
   sides.  Moreover,

   \[
       N_G(L)=\bigl(N_G(L)\cap W\bigr)
                \mathbin{\dot\cup}
                \bigl(N_G(L)\cap R\bigr),             \tag{2.5}
   \]

   the first set is nonempty and the second uses only colours outside
   `{i,j}`.  In particular, if `G` is `ell`-connected, then
   `|N_G(L)| >= ell`.

#### Proof

Every set in (2.4) is nonempty and every one of its vertices belongs to a
member of `D_{ij}`.  If there is only one such member, it therefore
contains all four sets, which proves the first outcome.

Suppose there are two members `L,L'`.  The component `L` is connected and
nonempty.  It has a neighbour in `W`, because it meets one of the terminal
sets in (2.4), so the first set in (2.5) is nonempty.  Every neighbour of
`L` in `R` has colour outside `{i,j}`, or it would belong to the same
component of (2.1).  Finally, a terminal vertex in `L'` belongs neither to
`L` nor to `N_G(L)`, since distinct components of (2.1) are anticomplete.
Thus

\[
        L\cup N_G(L),\qquad V(G)-L
\]

is a separation with `L` on one open side and that terminal vertex on the
other.  The connectivity bound follows. \(\square\)

## 3. Simultaneous disjoint witnesses

### Corollary 3.1 (matching of disjoint bichromatic components)

Let `M` be a matching on the set of colours different from `gamma`.  For
each edge `ij` of `M`, choose a component `C_{ij}` supplied by Theorem
2.1.  Then the subgraphs `C_{ij}` are pairwise vertex-disjoint.

#### Proof

The component `C_{ij}` uses only colours `i,j`.  Distinct edges of `M`
have disjoint endpoint-colour sets.  Hence their corresponding vertex
sets are disjoint. \(\square\)

For `k=7`, a matching of size two leaves one colour `h` other than the
contracted colour.  The two diagonal bichromatic components and any common `gamma,h` support component from
the promoted palette theorem are three pairwise vertex-disjoint connected
subgraphs.  This is the first simultaneous conclusion in which the five
colours other than `gamma` interact with one another rather than only with the
contracted colour.

If both matching edges have the first outcome of Theorem 2.2, their two
components are each adjacent to both `A` and `B` in both of their colours.
Together with a common `gamma,h` support component, this gives three
pairwise vertex-disjoint connected subgraphs, each adjacent to both sides
of the contracted bipartition.  When `Q` is one edge, adjoining that edge
produces three internally disjoint external paths between its endpoints.
This conclusion still carries colours rather than the five labels of an
arbitrary clique-minor model.

## 4. Exact interpretation and limitation

A diagonal bichromatic component need not meet both bipartition sides.  If it meets
only `A`, then it contains neighbours of `A` in both of its colours; the
analogous statement holds for `B`.  If it meets both sides, it may do so
through two terminals of the same colour.  Thus Theorem 2.1 does **not**
give a prescribed pairing of four literal terminals.

The witnesses for different matchings also need not be compatible with
one another, and none is automatically aligned with the branch sets of a
pre-existing clique-minor model.  The next model-theoretic question is
whether, when `Q` lies in one named branch set, the matching of two
diagonal bichromatic components and the remaining common support component can be chosen so
that either a branch-set split preserves all five external labels or the
failure exposes one common separator.

## 5. Relation to the promoted palette theorem

The common `gamma,i` support theorem records the obstruction to colouring
the two bipartition sides with `gamma` and `i`.  Theorem 2.1 records the
obstruction to colouring them with two distinct colours `i` and
`j`.  Together, the two results cover every ordered pair of distinct
colours available to the two sides after the contraction is expanded.

The proof uses only minor-minimal chromaticity and the displayed induced
bipartition.  In particular, it is uniform in `k` and is independent of a
Moser boundary, an exact-seven separation, or a chosen clique-minor
model.
