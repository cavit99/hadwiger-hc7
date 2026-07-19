# Opposite colouring responses forced by an unresolved two-cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_opposite_response_audit.md`](hc7_order8_two_cut_opposite_response_audit.md).
This statement is not a proof of `HC_7`.

## Theorem (two-cut defect-pair response normal form)

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
 \tag{1}
\]

Let `S` have order eight and suppose `G-S` has exactly three components

\[
                         C,Q_0,Q_1,                    \tag{2}
\]

all adjacent to every literal vertex of `S`.  Suppose `G[S]` contains two
vertex-disjoint odd cycles.  Assume `G[C]` is two-connected and has a
two-vertex cut `{x,y}` for which `G[C]-{x,y}` has exactly two components
`L_d,L_e`, where `d,e` are distinct vertices of `S` and

\[
 N_G(L_d)\cap S=S-\{d\},\qquad
 N_G(L_e)\cap S=S-\{e\}.                              \tag{3}
\]

Then all of the following hold.

1. Neither `x` nor `y` is adjacent to `d` or `e`.
2. The two sets

   \[
              A_d=L_d\cup\{x\},\qquad A_e=L_e\cup\{y\} \tag{4}
   \]

   are disjoint, connected, adjacent, cover `C`, and have the exact
   boundary neighbourhoods

   \[
    N_G(A_d)\cap S=S-\{d\},\qquad
    N_G(A_e)\cap S=S-\{e\}.                            \tag{5}
   \]

3. The graph `G[S-\{d,e\}]` is bipartite and `de` is not an edge.
4. Writing

   \[
                  S-\{d,e\}=P\mathbin{\dot\cup}R       \tag{6}
   \]

   for its bipartition, the two closed shores have opposite singleton
   response sets for the two boundary partitions

   \[
             P\mid R\mid\{d,e\},
             \qquad
             P\mid R\mid\{d\}\mid\{e\}.              \tag{7}
   \]

   In particular, exactly one closed shore realizes only the first type
   and the other realizes only the second type.  Every colouring of the
   second type has a bichromatic `d`--`e` path whose internal vertices lie
   in its open shore.  If the `Q_0\cup Q_1` shore is the second-type shore,
   every such path meets `Q_0\cup Q_1` internally.

Thus an unresolved two-cut does not merely yield two adjacent defect-one
pieces: contraction-critical colouring forces the existing audited
opposite-response normal form.

## Proof

Two-connectivity implies that each of `L_d,L_e` has a neighbour of both
`x` and `y`.  Indeed, if one lobe had no neighbour of `x`, deleting `y`
would disconnect `G[C]`.

We first prove item 1.  Suppose, by symmetry, that some
`z\in\{x,y\}` is adjacent to `d`.  The connected subgraph

\[
                              F=L_d\cup\{z\}            \tag{8}
\]

is then adjacent to every vertex of `S`.  It is adjacent to the other
lobe `L_e`, because `z` has a neighbour in `L_e`.

Of the two vertex-disjoint odd cycles in `G[S]`, at least one, say `O`,
avoids `e`.  Since `S` has order eight, `O` has order three or five.
Choose

\[
                  f\in S-(V(O)\cup\{e\}).             \tag{9}
\]

Such an `f` exists.  Treat the full subgraph `F` as a one-defect subgraph
with artificial defect `f`; that is, it is adjacent to every vertex of
`S-\{f\}`.  The lobe `L_e` is adjacent to every vertex of `S-\{e\}`,
the two are adjacent, and `O` lies in `S-\{f,e\}`.  Together with the two
full components `Q_0,Q_1`, all hypotheses of the audited short-cycle
branch-set lemma are satisfied.  That lemma gives an explicit `K_7`-minor
model, contrary to (1).  Thus neither cut vertex is adjacent to `d`.
Interchanging the two lobes proves that neither is adjacent to `e`.

Now (4) consists of disjoint connected sets and covers `C`.  They are
adjacent because `x` has a neighbour in `L_e` (equivalently, `y` has a
neighbour in `L_d`).  Equations (3) and item 1 give the exact equalities
in (5).  This proves item 2.

If `G[S-\{d,e\}]` were nonbipartite, its shortest odd cycle would have
order three or five.  The two full components `Q_0,Q_1`, the adjacent
one-defect subgraphs `A_d,A_e`, and that cycle satisfy the same audited
short-cycle lemma, again giving a `K_7` minor.  Hence the graph in (6) is
bipartite.

Both classes in (6) are nonempty, and each of `d,e` has a neighbour in
both.  To see this, each of the two disjoint odd cycles must meet
`\{d,e\}`, since deleting `d,e` leaves a bipartite graph.  Disjointness
then shows that one cycle contains `d` and not `e`, while the other contains
`e` and not `d`.  Deleting the distinguished vertex from either odd cycle
leaves an odd-length path in `G[S-\{d,e\}]`; its ends lie in opposite
bipartition classes and are both neighbours of the distinguished vertex.

If `de` were an edge, apply the audited adjacent-defect reflection theorem
to the adjacent subgraphs in (4), the full components `Q_0,Q_1`, the
bipartition (6), and the two disjoint odd cycles.  It would give a proper
six-colouring of `G`, contrary to (1).  Therefore `de` is not an edge,
proving item 3.

Finally put

\[
 L=C,\qquad R'=Q_0\cup Q_1,
 \qquad V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R'. \tag{10}
\]

The open sides are anticomplete.  The `L`-side contains the two adjacent
one-defect subgraphs (4), while the `R'`-side contains the two disjoint
`S`-full connected subgraphs `Q_0,Q_1`.  Item 3 and the paragraph following
(6) verify every boundary hypothesis of the audited opposite-response
theorem.  Since `G` is not six-colourable, that theorem says that the two
nonempty response sets are opposite singletons and supplies the stated
bichromatic path on the unequal-response shore.  Its localization theorem
additionally says that, when the `R'`-shore is unequal, every such path
meets `Q_0\cup Q_1` internally.  This proves item 4. \(\square\)

## Exact gain and trust boundary

The theorem converts the final two-lobe contact residue into a dynamic,
operation-supported colouring normal form and works for both the `(3,3)`
and `(3,5)` odd-cycle packing types.  It is strictly stronger than a static
contact conclusion, and the width-five quotient barrier does not refute it
because that quotient is six-colourable and carries no proper-minor
response data.

The theorem does not eliminate the opposite-response normal form, split
either full component at the forced path's first intersections, or return
an order-seven separation.  Those are the remaining host-level tasks.

## Dependencies

- the short-cycle branch-set lemma, Lemma 1.1 of the audited strict-reversal
  completion;
- the audited adjacent-defect reflection theorem; and
- the audited opposite-response and path-localization theorems.
