# Independent audit: contracted five-chromatic boundary

**Audited source:**
`results/hc7_contracted_five_chromatic_boundary.md`.

**Source SHA-256:**
`9502143a9a003193bc1c405f9c95eb9cb2f547925e3e26204915e4dc36c04d5c`.

**Verdict:** **GREEN.**  Lemmas 2.1, 2.2, 3.1, 4.1, 6.1,
Corollary 6.2 and Theorem 5.1 are correct under their stated hypotheses.
The source correctly confines five-connectivity of the lifted graph to the
intended seven-connected counterexample application.  The result is a
planarizing-pair theorem in the contracted graph and a split-planar normal
form in the original graph; it does not prove `HC_7`.

Relative to the frozen mathematical revision checked independently, the
hash above changes only because the source status line now links this audit.

The external input was checked against Lemma 3.1 of Anders Martinsson and
Raphael Steiner, *Strengthening Hadwiger's conjecture for 4- and
5-chromatic graphs*, Journal of Combinatorial Theory, Series B 164 (2024),
1--16.  The source quotes its hypotheses and conclusion accurately.

## 1. Deleting a boundary vertex

Let `Q_1,...,Q_5` be a `K_5`-minor model in `F-s`.  The seven proposed
branch sets

\[
                    A\cup\{s\},\quad D,\quad Q_1,\ldots,Q_5
\]

are pairwise disjoint.  The set `A union {s}` is connected because
`N_H(A)=S`, and it is adjacent to `D` through an edge from `s` to `D`.
Every `Q_i` contains a literal boundary vertex; fullness of both `A` and
`D` therefore supplies their contacts with every `Q_i`.  The remaining
contacts are those of the original `K_5` model.  Hence the construction is
a valid `K_7`-minor model, and Lemma 2.1 follows.

## 2. Density and four-degeneracy

The six-vertex density claim is correct.  A graph on six vertices with at
least thirteen edges has at most two nonedges.  If the two nonedges share
an endpoint, deleting that endpoint leaves a `K_5`; if they are disjoint,
say `ab` and `cd`, then

\[
                       \{a,c\},\{b\},\{d\},\{e\},\{f\}
\]

is a `K_5`-minor model.  The first set is connected because `ac` is not one
of the two nonedges, and its two vertices supply both formerly missing
contacts.

Lemma 2.1 therefore gives `e(F-s)<=12` for every boundary vertex `s`.  If
`F` were not four-degenerate, an induced subgraph of minimum degree at
least five would have order six or seven.  At order six it is `K_6`, and
after choosing the omitted boundary vertex some `F-s` contains a `K_5`.
At order seven it is all of `F`, so `e(F)>=18`, whereas double counting
gives

\[
             5e(F)=\sum_{s\in S}e(F-s)\le 7\cdot12=84,
\]

and hence `e(F)<=16`.  Both cases are impossible.  Finally, established
`HC_5` makes every `F-s` four-colourable, so adding a fifth colour for `s`
proves `chi(F)<=5`.

## 3. Classification of the five-chromatic boundary

When `chi(F)=5`, the preceding vertex-deletion colourings make `F`
five-vertex-critical, so `delta(F)>=4`.  Its complement `R` consequently
has maximum degree at most two and is a disjoint union of paths, cycles and
isolated vertices.

A colour class of `F` is a clique of `R`, so the clique-partition saving

\[
                     \sigma(J)=|V(J)|-\theta(J)
\]

is additive over components and satisfies

\[
                    \sigma(R)=2,\qquad \sigma(R-s)\ge2
\]

for every `s`.  The stated savings for paths and cycles are correct.  Two
components of saving one fail the deletion test.  Among the connected
graphs of saving two, deleting the indicated vertex reduces the saving to
one for `P_4,P_5,C_3,C_4`, while every vertex deletion of `C_5` leaves
`P_4` and preserves saving two.  Thus

\[
                         R=C_5\mathbin{\dot\cup}2K_1,
\]

whose complement is exactly `K_2\vee C_5`.  Lemma 3.1 is exhaustive.

## 4. Excluding a third complementary component

Six-connectivity makes any third component `E` of `H-S` adjacent to at
least six of the seven boundary vertices.  The two displayed minor models
cover all possibilities for the one vertex that `E` may miss.

If that vertex is `c_i`, the nonsingleton branch sets in (4.2) are
connected and mutually adjacent by fullness.  The `E` branch set reaches
`c_i` through `c_{i-1}c_i`, and the four singleton branch sets
`c_i,c_{i+1},a,b` form a clique.  If `E` instead misses `a`, `b`, or no
vertex, (4.3) works: `c_2` supplies the contact with a possibly missed
universal vertex, and the remaining contacts follow from fullness, cycle
edges and the join.  Hence either case yields an explicit `K_7`-minor
model, so `A,D` are the only two components of `H-S`.

## 5. The planarizing pair in the contracted graph

Put `P=H-{a,b}`.  It is four-connected because `H` is six-connected.
For `J_A=H[A union V(C)]`, deletion of at most two vertices cannot leave a
component disjoint from `C`: such a component would have its full
neighbourhood in a set of order at most two in `P`.  If a deleted vertex
lies in `A`, at most one cycle vertex is deleted and the remaining cycle
is connected.  If all deleted vertices lie on `C`, the untouched connected
component `A`, which has a neighbour at every remaining cycle vertex,
joins the surviving cycle pieces.  Thus `J_A` is three-connected.  The
same proof applies to `J_D`.

The cycle vertex set is spread out across every order-three separation.
If one side contained all of `C`, the nonempty opposite open side would
lie in `A` (or `D`) and have a neighbourhood of order at most three in
`P`; the other component survives because there are no edges between
`A` and `D`.  This contradicts four-connectivity.

A `C`-rooted `K_4` model in `J_A`, together with `D,{a},{b}`, is an
explicit `K_7`-minor model: fullness of `D` supplies its four root contacts
and its contacts with `a,b`, while the universal pair is adjacent to every
rooted branch set and to each other.  Therefore neither shore graph has a
`C`-rooted `K_4` model.

Martinsson--Steiner Lemma 3.1 now applies exactly.  After adjoining an
artificial vertex complete to `C`, each shore graph is planar.  The wheel
formed by the artificial vertex and `C` separates the embedding into its
faces.  The connected open shore cannot lie in a hub-triangle: it has no
edge to the artificial vertex and has neighbours at all five rim vertices,
whereas only two rim vertices are incident with such a face.  It therefore
lies in the face on the other side of `C`.  Removing the artificial vertex
gives a disc embedding with boundary `C`.  Reflecting one disc and gluing
the two copies along the induced cycle is legitimate because `A,D` are all
the components of `H-S` and are anticomplete.  This proves that
`H-{a,b}` is planar.

## 6. Split-edge colour saturation and the lifted model statements

Every six-colouring of `H=G/pv` expands to a six-colouring of `G-pv` in
which `p,v` have the same colour.  If either endpoint missed another
colour in its neighbourhood, recolouring that endpoint would separate the
colours of `p,v` and restore the deleted edge, producing a six-colouring
of `G`.  Lemma 6.1 is therefore correct.

When the contraction image `x` is outside the universal pair `U={a,b}`,
four-colour `H-U` and give `a,b` two distinct unique colours.  Saturation
forces all four edges `pa,pb,va,vb`.  If a `K_5` model in `G-U` used at
most one of `p,v`, or used both in the same branch set, contracting `pv`
would preserve five disjoint connected branch sets and give a `K_5` minor
in the planar graph `H-U`.  Thus every such model uses `p,v` in distinct
branch sets.

When `x=a`, the identity

\[
                     G-\{p,v,b\}=H-\{x,b\}
\]

is correct and planar.  The same unique-colour argument forces `pb,vb`.
A `K_5` model in `G-{p,b}` that avoided `v` would lie in that planar
triple deletion; the symmetric assertion follows identically.  If
`chi(G)=7`, deletion of any two vertices leaves chromatic number at least
five, and established `HC_5` makes each claimed family of `K_5` models
nonempty.

## 7. Trust boundary

The conclusion `H-U` planar does not lift to planarity of `G-U`: undoing
the contraction is an adjacent vertex split, which need not preserve
planarity.  In the intended application only, seven-connectivity of `G`
makes `G-U` five-connected; the standalone hypotheses in Section 6 do not
assert this.  The source now states that qualification explicitly.

The audit does not infer a common boundary colouring, an `S`-meeting
`K_6`-minor model, or a two-vertex planarizing set in `G`.  In the
`x notin U` case one still needs a label-preserving construction ensuring
that the remaining three branch sets of a `K_5` model have the required
contacts with `a,b`.  In the `x in U` case the two oppositely rooted
`K_5`-model obligations remain.  These are genuine open obligations, not
consequences of the audited theorem.
