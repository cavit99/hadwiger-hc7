# Independent audit: forced three-cut gives exact order eight

## Verdict

**GREEN.**  The implication in
`hadwiger_c6_threecut_lobe_exchange.md` and Corollary 6.3.4 of
`hadwiger_full_deletion_propagation.md` is valid.  The connectedness of
the complementary split side, the orientation of the exact two-piece
atlas, and the literal expansion of its positive certificate all check.

## 1. The three-cut is genuine

The preceding four-connected-atom exclusion gives a vertex cut `T` of
order exactly three because the minimum shore `D` is already
three-connected.  If `C_1,...,C_m` are the components of `D-T`, then
`m>=2`.

For every `i`, one has

\[
                              N_D(C_i)=T.                       \tag{1.1}
\]

Containment in `T` follows from the definition of the components.  If
some `t in T` had no neighbour in `C_i`, the other two vertices of `T`
would separate `C_i` from any other component of `D-T`, contrary to
three-connectivity.  Thus all three gate vertices are actual neighbours.

Since `D` is one component of `G-S`, there are no edges from `C_i` to an
opposite shore.  Hence, literally in the original graph,

\[
                     N_G(C_i)=T\mathbin{\dot\cup}N_S(C_i).       \tag{1.2}
\]

Strict atomic surplus on the connected proper set `C_i` gives

\[
  8\le |N_G(C_i)|=3+|N_S(C_i)|,
  \qquad A_i:=S-N_S(C_i),\quad |A_i|\le2.                       \tag{1.3}
\]

If `|A_i|=2`, (1.2) has order eight and is an actual separator: `C_i`
is nonempty and an old opposite shore survives outside it.  No quotient
vertex is being counted as an original separator vertex.

## 2. The split side `D-C_i` is connected and adjacent

Fix `i` and choose `j ne i`.  The induced graph `D-C_i` contains `T` and
all other components.  The subgraph `T union C_j` is connected because
`C_j` is connected and every member of `T` has a neighbour in `C_j`.
Every further component also has an edge to every member of `T`, so it
attaches to this connected subgraph.  Therefore `D-C_i` is connected.

The two sides are adjacent because every member of `T subseteq D-C_i`
has a neighbour in `C_i`.  Thus

\[
                            C_i\mid(D-C_i)                       \tag{2.1}
\]

is a legitimate connected adjacent bipartition to which the exact
two-piece atlas applies.

## 3. The second defect really has order at most one

Put

\[
                         E_i=S-N_S(D-C_i).                       \tag{3.1}
\]

For any `j ne i`, the containment `C_j subseteq D-C_i` gives

\[
                    N_S(C_j)\subseteq N_S(D-C_i),
                    \qquad E_i\subseteq A_j.                    \tag{3.2}
\]

If no lobe has defect two, every `|A_j|<=1`, and hence both coordinates
of the defect pair `(A_i,E_i)` have order at most one.

Fullness of `D` also gives

\[
                              A_i\cap E_i=\varnothing,           \tag{3.3}
\]

which is the disjoint-defect convention of the atlas.

## 4. Atlas orientation and literal lift

The maximal negative defect pairs in the exact `C_6 dotcup K_1` atlas,
up to reversal, have sizes

\[
          0|3,\quad0|4,\quad1|2,\quad2|2.                       \tag{4.1}
\]

All other negative pairs are coordinatewise enlargements of one of
those displayed pairs.  Therefore no negative pair has both coordinates
of order at most one.  The pair `(A_i,E_i)` is positive.

The positive atlas certificate contracts exactly three actual connected
sets: the two sides in (2.1) and one opposite connected shore `H` full
to `S`.  The atlas's remaining bags use literal vertices of `S`.
Expanding the three helper vertices therefore produces disjoint connected
branch sets in the original graph, and every helper adjacency lifts to
an actual edge by the two side-contact rows, their mutual adjacency, or
fullness of `H`.  Extra components of `G-S`, if any, may simply be
ignored.  Thus positivity gives a literal `K_7` minor, not merely a
quotient minor.

This contradiction proves that some `|A_i|=2`, and (1.2)--(1.3) then
give the claimed exact order-eight separator.

## 5. Dependency audit

The conclusion uses exactly:

1. three-connectivity of `D`;
2. strict atomic surplus for the minimum shore;
3. one opposite connected shore full to `S`; and
4. the audited exact two-piece contact atlas.

It does not assume that `T` is a triangle, that `D-T` has two components,
or that a whole branch bag counts as one separator vertex.
