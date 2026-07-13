# Independent audit: exact-seven two-gate boundary threshold

## Verdict

**GREEN AS STRENGTHENED.**  Fullness of the shores, the private-block
minor transition, the one-block colour gluing, nonsplit Corollary 2.3,
all explicit two-shore `K_7` models, the new five-defect lower threshold,
and the `K_2`-join-icosahedron survivor all check.

The strengthened source now closes every boundary with at most four
missing edges.  The exact exhaustive audit at five missing edges leaves
precisely the two isomorphism types

\[
                 C_5\dot\cup2K_1,\qquad K_3\dot\cup2K_2.       \tag{A.1}
\]

The first is realized by the coherent rural example.  The second is the
nonrural crossing-or-web cell treated in
`hc7_near_k7_exact7_k322_web_closure.md`.

## 1. Full shores and private blocks

For any component `C` of `G-S`, its neighbourhood is a subset of the
seven-cut and separates it from another component.  Seven-connectivity
therefore forces `N(C)=S`.

If `P subseteq S` is independent, `C union P` is connected.  Contracting
it gives a proper minor.  In any six-colouring of that minor, the
contracted vertex is adjacent to every vertex of `S-P` through fullness.
Expanding `P` with its colour is proper and makes `P` one exact private
block.  All edges from `P` to retained vertices were represented at the
contracted vertex, so the colouring really extends over `G-C`.

If `G[S-P]` is a clique, the contracted image plus the singleton
vertices of `S-P` form a clique of order `8-|P|<=6`.  Both full shores
therefore produce exactly the same labelled partition

\[
                       P\mid\{x\}\quad(x in S-P),
\]

and palette alignment glues their colourings.  No unproved completeness
between `P` and `S-P` is used.

## 2. Explicit two-shore models

If two vertices `x,y` cover the missing-edge graph, the other five
boundary vertices form a clique.  The bags

\[
 A union {x},\quad B union {y},\quad {s}\ (s in S-{x,y})
\]

are connected and pairwise adjacent; notably the first two see each
other through the literal full-shore edge from `A` to `y`.

For `F=3K_2 dotunion K_1`, the seven bags in (3.3) also check.  The bag
`{y_1,y_2}` is connected because only matched partners are nonadjacent,
and it sees `x_i` through the endpoint not paired with `x_i`.  All other
contacts involving `A` or `B union {y_3}` follow from fullness.  Thus all
missing-edge graphs with at most three edges are closed: if their cover
number exceeds two, they are exactly a three-edge matching.

It follows correctly that every seven-cut in a seven-connected
`K_7`-minor-free graph has at least four missing boundary edges before
Theorem 3.4 is used.

For the four-edge step, if the missing graph has cover number at most
two, the preceding model applies.  Otherwise its nontrivial components
are exactly

\[
                 K_3\dot\cup K_2,\qquad
                 P_4\dot\cup K_2,\qquad
                 P_3\dot\cup2K_2.                              \tag{A.2}
\]

The three displayed models (3.6)--(3.8) were checked bag by bag.  In
each, the only nonsingleton boundary pair joins vertices in different
components of the missing graph, and hence is an edge of the boundary;
the shore-containing bag is connected by fullness.  All seven bags are
pairwise adjacent.  Therefore every four-edge missing graph closes and
every target-free exact seven-cut has at least five missing edges.  In
particular, two specified independent gate pairs require at least three
additional defects.

The independent verifier `contact_order7_four_edge_verify.py` checks all
\(\binom{21}{4}=5985\) labelled four-edge complements by exact
connected-branch-set search.  The verifier
`contact_order7_five_edge_verify.py` checks all
\(\binom{21}{5}=20349\) labelled five-edge complements and returns 357
exceptions: 252 labelled copies of `C5+2K1` and 105 labelled copies of
`K3+2K2`, exactly their two permutation orbits.  These finite checks are
independent confirmation of the hand proof through four defects and of
the asserted five-defect classification; the four-defect theorem itself
does not depend on computation.

## 3. Nonsplitness

Corollary 2.3 is sound.  If `F=P dotunion R` is a split partition with
`P` a clique and `R` independent, then `P` is a vertex cover.  The
minor-theoretic defect threshold gives `tau(F)>=3`, hence `|P|>=3`.
Translated back to the boundary graph, `P` is independent and `R`
induces a clique.  Corollary 2.2 glues the private-block state on the two
closed shores.  This contradicts minor-critical non-six-colourability.
The standard forbidden-induced-subgraph characterization of split
graphs then supplies an induced `2K2`, `C4`, or `C5`.

There is no circularity: the lower bound on `tau(F)` comes from the
purely minor-theoretic two-shore models, not from nonsplitness.

## 4. Equality-state count

For `F=3K_2 dotunion K_1`, every colour block is either a singleton or
one of the three missing pairs, while the isolated vertex of `F` must be
singleton.  At least one pair must be identified to use at most six
colours.  The seven labelled states are therefore indexed by the
nonempty subsets of the three pairs, with three orbit types according to
their cardinality.  This agrees with Section 4.

## 5. Icosahedral survivor

Let `I` be the icosahedron and `G_0=I vee K_2`.  The join raises both
connectivity and Hadwiger number by two, giving connectivity seven and
Hadwiger number six.  A neighbourhood of an icosahedral vertex induces
`C_5`; deleting that closed neighbourhood leaves a connected six-vertex
piece, and both it and the selected vertex are full to the seven-cut
after adjoining the two universal vertices.

Consequently

\[
              G_0[S]=K_2 vee C_5,
       \qquad \overline{G_0[S]}=2K_1 dotunion C_5.
\]

The displayed triangle and two gate pairs have the required labels.
On the `C_5`, a boundary colouring uses either one nonedge pair and three
singletons (five choices), or two disjoint nonedge pairs and one
singleton (five choices).  The two universal adjacent vertices are
separate singleton colours, giving the claimed ten labelled states and
two dihedral types.

Finally deletion of the two universal vertices leaves the planar
icosahedron.  The graph is therefore a genuine coherent two-apex static
survivor, but is six-colourable and not minor-critical.  This correctly
identifies proper-minor state transitions, rather than further static
defect counting, as the missing input.
