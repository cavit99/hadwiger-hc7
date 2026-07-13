# Independent audit: load-minimal literal Kempe packets

## Verdict

**GREEN.**  The Kempe switch is performed on genuine two-colour
components of the unchanged opposite shore, extends to the contracted
minor with `z` fixed, and decreases the selected literal load by exactly
one.  The lexicographic warning example and the one-sum nonsingleton-bag
falsifier realize exactly the claimed limitations; the latter is
indeed `K_7`-minor-free.

## 1. The switch is a switch in the whole minor

Contracting the connected set `K` produces a vertex `z` whose neighbours
are exactly the actual boundary `S=N_G(K)`.  If colours `i,j` are seen at
the fixed literal vertex `x`, each occurs on a vertex of `S`.  Since `z`
is adjacent to every member of `S`, properness gives

\[
                         c(z)\notin\{i,j\}.
\]

Consequently the `i,j`-components in `M` are exactly the `i,j`-components
in `O=G-K`; the fixed vertex `z` belongs to none of them.  Switching a
union of whole components preserves all edges inside `O`.  Every edge
from `z` to a switched vertex still has endpoint colour `i` or `j`, both
different from `c(z)`.  Thus leaving `z` fixed extends the switch to a
proper colouring of all of `M`, not merely of the open shore.

## 2. Exact load decrease

Let `U` be the union of every `i,j`-component meeting
`P_i(x,c)`.  Every literal `i`-coloured boundary neighbour of `x`
belongs to `P_i(x,c)`, so every such vertex lies in `U` and changes to
colour `j`.  Under the contradictory assumption, no component meeting
`P_i(x,c)` meets `P_j(x,c)`.  Hence no old literal `j`-portal lies in
`U`, and every one remains colour `j`.

The switch changes no boundary neighbour having a third colour.  Thus
colour `i` disappears completely from `N_G(x) cap S`, colour `j`
remains represented, and no new colour appears.  The new load is exactly
`lambda_x(c)-1`, contradicting minimality.  A component meeting both
portal sets contains a literal bichromatic path between chosen members
of them, so the path formulation is equivalent.

The corollary is scoped correctly.  Minimizing at one fixed vertex gives
all pairwise connections for the colours seen at that vertex, but a
switch may raise another vertex's load.  The active-face theorem only
asserts that each colouring has some heavy facial vertex and does not
make the fixed minimum load at an arbitrarily chosen vertex at least
four.

## 3. Lexicographic warning

In Proposition 2.3, first-coordinate load one forces `a,d` to share a
colour, while the edge `bd` forces `b` to use another.  Hence the
lexicographic minimum is `(1,2)`.  The relevant two-colour graph has
components `{a}` and `{b,d}`; switching `{a}` changes the vector to
`(2,1)`.  This verifies that later coordinates of a lexicographic load
vector need not enjoy the single-coordinate packet theorem.

## 4. Nonsingleton-bag falsifier

The four vertices of `B` induce `K_4` and are all adjacent to the one
carrier vertex `x`.  After contracting the carrier, `B union {z}` is
`K_5`.  Therefore every proper colouring assigns four distinct colours
to `B`, all different from `c(z)`, and the literal load at `x` is
exactly four in every state.  For every colour pair the corresponding
edge of `B` is the required bichromatic path, so the full pairwise
packet is present entirely inside one foreign connected bag.

The four named carrier terminals alternate on one facial cycle of the
plane square-antiprism.  The planar cross obstruction therefore forbids
disjoint paths for the two prescribed pairs inside the carrier.

The whole example is a one-sum at `x` of the planar square-antiprism and
the clique `K_5=G[B union {x}]`.  In a clique-minor model of order at
least three in a one-sum, at most one branch set contains the cutvertex.
Every other branch set must lie on one side, and branch sets on opposite
sides would be nonadjacent.  Hence all non-cutvertex branch sets lie in
one summand, and the possible cutvertex branch set can be pruned to that
same summand.  The Hadwiger number of a one-sum is therefore the maximum
of those of its summands.  Here it is at most `max(4,5)=5`, so the graph
is certainly `K_7`-minor-free.

## Scope

The theorem produces literal opposite-shore bichromatic paths, but does
not make their portal colours distinct model-row labels, make paths for
different pairs mutually disjoint, or force them to leave one
nonsingleton foreign bag.  Any use at the locked gate still needs a
label-distribution theorem, a protected linkage, or a faithful crossed
boundary-state collision.
