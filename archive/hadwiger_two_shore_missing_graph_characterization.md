# Two full shores: an exact missing-graph characterization

## Status

Let `F` be a graph on seven labelled boundary vertices and define

\[
 H(F)=\overline F\vee\overline{K_2},                            \tag{0.1}
\]

where the two vertices of `overline{K_2}` are the contractions of two
disjoint full shores.  This note gives an exact, label-free criterion for
`H(F)` to contain `K_7`.  It then combines that criterion with the
private-block transition at a minor-critical exact cut.

The answer to the proposed “all survivors are cyclic/rural” question is
**no at the static quotient level**.  Besides the rural
`C_5 dotunion 2K_1` missing graph, the graph

\[
                         F=2K_3\mathbin{\dot\cup}K_1            \tag{0.2}
\]

is a sharp target-free triangle-plus-two-gates survivor.  Its two-shore
quotient is `K_1 vee K_{2,3,3}`, has no `K_7` minor, and is not two-apex.
It also survives all abstract private-block incidence requirements.  Thus
minor-critical operation states must do more than supply private blocks:
they must create compatible residual blocks, labelled columns, or a
faithful rural decomposition.

## 1. Exact compression criterion

Let

\[
              U=V(F)\mathbin{\dot\cup}\{a,b\},\qquad
              M=F\mathbin{\dot\cup}ab.                         \tag{1.1}
\]

Thus `M=overline{H(F)}`.  For disjoint sets, “complete in `M`” and
“anticomplete in `H(F)`” have their literal meanings.

### Theorem 1.1 (defect-two clique-minor criterion)

The graph `H(F)` contains a `K_7` minor if and only if at least one of
the following four certificates exists.

1. **Seven singletons.**  `M` has a vertex cover of order at most two.
2. **One pair and one deletion.**  There are distinct vertices `d,x,y`
   such that
   
   \[
   xy\notin E(M),\quad M-(d,x,y)\text{ is edgeless},\quad
   N_M(x)\cap N_M(y)\subseteq\{d\}.                            \tag{1.2}
   \]
3. **One triple.**  There is a three-set `X` such that
   
   \[
   |E(M[X])|\le1,\quad M-X\text{ is edgeless},\quad
   X\nsubseteq N_M(v)\quad(v\in U-X).                          \tag{1.3}
   \]
4. **Two pairs.**  There are disjoint pairs `X,Y` such that
   
   \[
   \begin{gathered}
   E(M[X])=E(M[Y])=emptyset,\qquad
   M-(X\cup Y)\text{ is edgeless},\\
   X\nsubseteq N_M(v),\quad Y\nsubseteq N_M(v)
       \quad(v\in U-(X\cup Y)),\\
   M[X,Y]\ne K_{2,2}.
   \end{gathered}                                                \tag{1.4}
   \]

Every condition is invariant under relabelling.  In particular, the
criterion is a structural characterization rather than an enumeration of
graphs `F`.

#### Proof

Any `K_7` model in a nine-vertex graph uses between seven and nine
vertices.  Since it has seven nonempty branch sets, the multiset of branch
set orders is exactly one of

\[
 1^7,\qquad 2,1^6,\qquad 3,1^6,\qquad 2,2,1^5.                  \tag{1.5}
\]

Conversely, branch sets of one of these four forms give a `K_7` model
precisely when they are connected and pairwise adjacent.  We translate
those two requirements into the complement `M`.

For `1^7`, two vertices may be discarded and the seven retained vertices
must be pairwise adjacent in `H(F)`.  Equivalently, the discarded vertices
cover every edge of `M`, which is certificate 1.

For `2,1^6`, discard `d` and let `{x,y}` be the two-vertex bag.  It is
connected exactly when `xy notin E(M)`.  The six singleton bags form a
clique exactly when `M-(d,x,y)` is edgeless.  A singleton `v` is adjacent
to the pair bag exactly when at least one of `vx,vy` is absent from `M`;
this is the last condition in (1.2).

For `3,1^6`, the three-vertex bag `X` is connected in `H(F)` exactly when
its complement has at most one edge: on three vertices, deleting zero or
one edge from a clique leaves a connected graph, while deleting two or
three does not.  The singleton condition is `M-X` edgeless.  A singleton
`v` sees the triple bag exactly when it is not `M`-complete to `X`.  This
is (1.3).

Finally, in the `2,2,1^5` form, the internal nonedges in `M` make both
pairs connected, the edgeless remainder makes the five singletons a
clique, the two noncontainment conditions make every singleton adjacent
to both pair bags, and `M[X,Y] ne K_{2,2}` is exactly adjacency between
the two pair bags.  This proves both directions of certificate 4 and
exhausts (1.5).  \(\square\)

### Corollary 1.2 (quick sufficient conditions)

The vertex-cover and three-matching completions from
`hadwiger_exact_seven_two_gate_boundary_threshold.md` are the following
special cases of Theorem 1.1.

* If `tau(F)<=2`, use certificate 4 with the pairs `{a,x},{b,y}` after
  choosing a two-vertex cover `{x,y}` of `F`.
* If `F=3K_2 dotunion K_1`, use the explicit two-pair compression (3.3)
  in that note.

The exact criterion also handles models which delete a boundary vertex or
put both full-shore images into one three-vertex branch set; neither move
is visible from `tau(F)` alone.

## 2. What minor-criticality removes uniformly

Suppose `S` is an exact seven-cut in a non-six-colourable graph every
proper minor of which is six-colourable.  Every component behind `S` is
full.  Continue to write `F=overline{G[S]}`.

### Theorem 2.1 (split missing graphs colour-glue)

The missing graph `F` is not a split graph.

#### Proof

Suppose `V(F)=P dotunion R`, where `P` is a clique of `F` and `R` is
independent in `F`.  If `F` has an edge, choose the split partition with
`|P|>=2`: if an initial clique side is a singleton, move one of its
neighbours from the independent side into it.  Then `P`
is independent in `G[S]` and `G[R]` is a clique.  Corollary 2.2 of
`hadwiger_exact_seven_two_gate_boundary_threshold.md` contracts a full
shore with `P` on each side, produces the same exact state

\[
                     P\mid\{r\}\quad(r\in R),                  \tag{2.1}
\]

and colour-glues the two sides, a contradiction.

If `F` is edgeless, `G[S]` is a clique.  Colourings of the two proper
closed sides induce the all-singleton state and glue directly.  Thus no
split `F` occurs.  \(\square\)

By the Földes--Hammer characterization of split graphs, the theorem has
the label-free consequence

\[
        F\text{ contains an induced }2K_2, C_4,	ext{ or }C_5. \tag{2.2}
\]

This is the correct cyclic-frame reduction supplied by private-block
states.  It does **not** say that only the `C_5` case survives: induced
`2K_2` and `C_4` frames can live inside a nonrural warehouse.

## 3. A sharp nonrural triangle-plus-two-gates survivor

Let

\[
 X=\{x_1,x_2,x_3\},\qquad Y=\{y_1,y_2,y_3\},\qquad R=\{r\},
                                                                    \tag{3.1}
\]

and take

\[
                         F=K_X\mathbin{\dot\cup}K_Y
                              \mathbin{\dot\cup}K_R.             \tag{3.2}
\]

Then

\[
                  H(F)=K_1\vee K_{2,3,3}.                       \tag{3.3}
\]

The universal vertex in (3.3) is the boundary vertex `r`; the three
parts of the complete multipartite graph are `{a,b}`, `X`, and `Y`.

### Proposition 3.1 (target-free and not two-apex)

The graph `H(F)` has no `K_7` minor, and deleting any two of its vertices
leaves a nonplanar graph.

#### Proof

If a `K_7` model in `H(F)` uses its universal vertex `r`, delete the
branch set containing `r`; the six remaining branch sets give a `K_6`
model in `K_{2,3,3}`.  If the model does not use `r`, all seven bags
already lie in `K_{2,3,3}`, and discarding any one of them again gives a
`K_6` model there.

There is no such model.  A connected branch set contained in one
multipartition class is a singleton, and a clique model has at most one
such singleton branch set from each of the three classes.  Thus a
six-bag clique model has at most three singleton bags; every other bag has
at least two vertices.  It would use at least

\[
                  s+2(6-s)=12-s\ge9                              \tag{3.4}
\]

vertices, where `s<=3`, but `K_{2,3,3}` has only eight vertices.

For the two-apex assertion, first delete `r` and one other vertex.  The
remaining complete multipartite graph is either `K_{1,3,3}` or
`K_{2,2,3}` and contains `K_{3,3}` as a subgraph (surplus edges within
one chosen bipartition side may be deleted).

Now retain `r` and delete any two vertices of `K_{2,3,3}`.  The remaining
multipartite graph contains `K_{2,3}`: one surviving part has two
vertices and at least three vertices survive outside that part.  A planar
graph with a universal vertex has an outerplanar graph after deleting
that vertex, whereas `K_{2,3}` is not outerplanar.  Hence the cone remains
nonplanar.  These cases exhaust every two-vertex deletion.  \(\square\)

### Corollary 3.2 (literal triangle and two gate pairs)

Put

\[
 Q=\{x_1,y_1,r\},\qquad
 Z_D=\{x_2,x_3\},\qquad Z_E=\{y_2,y_3\}.                       \tag{3.5}
\]

The set `Q` is independent in `F` and hence a triangle in `overline F`;
both `Z_D,Z_E` are edges of `F` and hence independent gate pairs in the
boundary graph.  Thus (3.2) has exactly the labelled shape of the
two-carrier exact adhesion, but its target-free quotient is nonrural.

This quotient is not itself seven-connected (contraction of full shores
need not preserve connectivity).  The proposition is therefore a sharp
obstruction to a quotient-only rural theorem, not a counterexample to a
theorem which uses the uncontracted seven-connected sides.

## 4. Why private blocks alone do not remove the survivor

In (3.2), a boundary equality state consists of a partition `pi_X` of
`X`, a partition `pi_Y` of `Y`, and the singleton `{r}`; it is a
six-colour state unless both `pi_X` and `pi_Y` are discrete.  There are
24 labelled states.

The private-block transition says that for every nonempty subset `P` of
`X` or of `Y`, each closed-side extension family contains some state in
which `P` is an exact block.  These incidence requirements admit two
disjoint abstract state families.  One explicit two-colouring of the
state universe is as follows.  Put a state in `mathcal B` exactly when

* `pi_X` is discrete and `pi_Y` has one pair and one singleton; or
* `pi_Y={Y}` and `pi_X` is nondiscrete.

Put every other state in `mathcal A`.

For a singleton `P subseteq X`, both colours occur by taking `pi_X`
discrete and choosing `pi_Y` respectively as a pair partition or the
one-block partition.  For a two-set or the three-set `P subseteq X`, keep
`P` as a block and vary `pi_Y` between `{Y}` and a pair/discrete
partition.  The symmetric checks for subsets of `Y` follow by using a
discrete `pi_X` for `mathcal B` pair witnesses, a nondiscrete `pi_X` for
the other `mathcal B` witnesses, and the complementary choices for
`mathcal A`.  Thus every private-block requirement is met on both sides,
while `mathcal A cap mathcal B=emptyset`.

This is not asserted to realize two minor-critical boundaried graphs.  It
proves the exact logical limitation: private-block existence and state
disjointness alone do not force a common state.  A successful exclusion
of (3.2) must use the **operation attached to the private witness**--for
example its equal-endpoint Kempe saturation--to build protected columns
or a labelled rerouting.

## 5. Structural conclusion

For the exact order-seven programme, the current uniform picture is now:

1. Theorem 1.1 decides the static two-shore quotient exactly.
2. Minor-critical colour gluing excludes every split missing graph.
3. Hence a surviving boundary contains an induced `2K_2`, `C_4`, or
   `C_5` frame.
4. The `C_5` frame is realized by the coherent two-apex icosahedral join.
5. The `2K_2` branch has a sharp nonrural quotient warehouse,
   `2K_3 dotunion K_1`, so cyclic order cannot be inferred from `F`
   alone.

The missing graph-theoretic transition is therefore sharply localized:
use the minor operation and Kempe saturation behind a private block to
defeat the `2K_3` warehouse (or turn its induced `2K_2` into four
protected columns).  More finite boundary classification cannot supply
that implication.
