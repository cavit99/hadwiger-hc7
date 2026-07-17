# Archived independent audit: bichromatic cross-lock terminology revision

**Archive note:** superseded by the standard-terminology theorem and audit
in `results/`; retained as the detailed audit of the preceding content hash.

**Audited file:**
[`hc_bipartite_contraction_cross_lock.md`](hc_bipartite_contraction_cross_lock.md)

**Audited source SHA-256:**
`b9661505caf7c2479d6ae5874f950ed2a57fe86ae353398cc66269272c643921`

**Verdict:** **GREEN.**

Theorems 2.1 and 2.2, Corollary 3.1, and the stated `k=7`
three-witness consequence all follow from the displayed hypotheses and the
promoted palette theorem.  No mathematical repair is required.  This is a deductive audit;
no finite computation is being used as evidence for the result.

## 1. Setup and imported result

The audit checked the source against
[`../results/hc_bipartite_contraction_palette_dichotomy.md`](../results/hc_bipartite_contraction_palette_dichotomy.md),
whose SHA-256 is
`9856ce9908d2a2d6a3e36177d32ec4aa0d9f389b1e2fcd6632829db9ce08dbc6`
and whose adjacent audit records a GREEN verdict for that exact promoted
revision.

The current note uses two consequences of that result:

1. `chi(G/Q)=k-1`, so the fixed colouring exists and, in particular, uses
   all `k-1` colours; and
2. for every `i != gamma`, each side of the bipartition has an external
   neighbour of colour `i`, while for every such `i` there is a component of
   `R[psi^{-1}({gamma,i})]` containing an `i`-coloured neighbour of both
   sides.

Under the canonical identification
`V(G/Q)-{q}=R`, the condition `i != gamma` implies
`psi^{-1}(i) subseteq R`.  Consequently the terminal definitions

\[
 A_i=N_G(A)\cap\psi^{-1}(i),\qquad
 B_i=N_G(B)\cap\psi^{-1}(i)
\]

really are subsets of `R`, even though `N_G(A)` and `N_G(B)` are taken in
`G`.  They are nonempty by the imported palette assertion.  The sets
`A_i` and `B_i` may overlap when one external vertex is adjacent to both
sides; none of the proofs assumes otherwise.

## 2. Theorem 2.1

The simultaneous Kempe change is valid.  It switches whole, pairwise
disjoint components of the induced `i,j`-coloured subgraph and therefore
preserves properness on `R`.

Assume that no component meets both

\[
 S_1=A_i\cup B_j\quad\hbox{and}\quad S_2=A_j\cup B_i.
\]

Every old `i`-coloured neighbour of `A` belongs to `A_i`, so its component
meets `S_1` and is switched to colour `j`.  Conversely, a component meeting
`A_j` meets `S_2`, hence cannot meet `S_1` and is not switched.  Thus the
change creates no new `i`-coloured neighbour of `A`.  The symmetric check is
exact for `B`: all components meeting `B_j` are switched and every component
meeting `B_i` is fixed, leaving no `j`-coloured neighbour of `B`.

The expansion over `W` is consequently proper.  Assigning colour `i` to all
of `A` and colour `j` to all of `B` creates no boundary conflict; each side
is independent; and every edge of the induced bipartite graph `G[W]` joins
the two differently coloured sides.  This gives the forbidden
`(k-1)`-colouring of `G`.

Meeting both `S_1` and `S_2` expands into exactly the four listed terminal
profiles.  A profile asserts two set contacts, not two distinct terminal
vertices: for example, one vertex in `A_i cap B_i` may witness the profile
`(A_i,B_i)`.  Section 4 states this limitation correctly.

## 3. Theorem 2.2

Every terminal vertex belongs to exactly one component of the two-colour
subgraph.  Hence, if `D_{ij}` has one member, that component contains all
four nonempty terminal sets and is adjacent to both bipartition sides in
each of colours `i,j`.

Now fix any `L in D_{ij}` when `D_{ij}` has at least two members, and choose
`L' != L` in `D_{ij}`.  The terminal contact defining membership of `L`
gives `N_G(L) cap W != emptyset`.  A neighbour of `L` in `R` cannot have
colour `i` or `j`; otherwise it would be a vertex of the same connected
component of `R[psi^{-1}({i,j})]`.  This proves the asserted colour structure
of the `R`-part of the boundary.

Choose a terminal vertex `x in L'`.  Distinct components of the induced
two-colour graph are anticomplete, so

\[
 x\notin L\cup N_G(L).
\]

With

\[
 X=L\cup N_G(L),\qquad Y=V(G)-L,
\]

one has `X union Y=V(G)`, `X cap Y=N_G(L)`, and no edge joins
`X-Y=L` to `Y-X=V(G)-(L union N_G(L))`.  The first open side is the nonempty
component `L`, and the second contains `x`.  Thus this is an actual
separation, not merely a neighbourhood decomposition.  Since
`V(G)=W dotcup R`, equation (2.5) is exact, and `ell`-connectivity yields
`|N_G(L)| >= ell`.

## 4. Corollary 3.1 and the `k=7` consequence

Each selected component `C_{ij}` contains only vertices coloured `i` or
`j`.  Edges of a matching have disjoint endpoint-colour sets, so the
corresponding components have disjoint vertex sets.  Their individual
choices do not need to be coordinated.

For `k=7`, the colouring of `G/Q` uses six colours: `gamma` and exactly five
others.  A size-two matching uses four of those five and leaves a colour
`h`.  The two cross-lock components lie in the four matched colour classes,
whereas a common support component supplied by the promoted theorem lies in
the `gamma,h` subgraph of `R`.  The three connected subgraphs are therefore
pairwise vertex-disjoint.

If both matched pairs are in outcome 1 of Theorem 2.2, the two cross-lock
components are each adjacent to both `A` and `B`; commonness gives the same
property for the `gamma,h` support component.  When `Q` is the edge `ab`,
each connected witness, together with an edge from `a` into it and an edge
from it to `b`, contains an `a`--`b` path whose internal vertices lie in
that witness.  Pairwise disjointness of the witnesses makes these three
paths internally vertex-disjoint.

## 5. Assumptions and limitations

The proof uses the standard conventions that graphs are finite and simple,
that `N_G(S)` is the external open neighbourhood of a vertex set, and that
an `ell`-connected graph has no separation of order below `ell` with two
nonempty open sides.  It also relies on the exact promoted palette theorem
identified above.  Under these conventions there are no unresolved
assumptions or gaps.

The theorem does not prescribe distinct literal terminals, require a
cross-lock component to contact both bipartition sides, produce one separator
common to several diffuse components, or make witnesses chosen for different
matchings compatible.  The unconditional `k=7` conclusion is only three
pairwise vertex-disjoint connected subgraphs.  Adjacency of all three to both
sides requires outcome 1 for both matched pairs, and none of these assertions
aligns the subgraphs with the labels of an existing clique-minor model or
constructs a `K_7` minor.
