# Kempe-component parity obstruction for deleted edges

**Status:** proved and independently cold-audited
([audit](hc7_kempe_component_odd_cycle_audit.md)).

This note isolates a uniform parity invariant for a colouring of an
edge-deleted graph.  Its useful object is not the deleted edge set by
itself, but the multigraph obtained after contracting the relevant
two-colour components.  Loops and parallel edges must be retained.

## 1. The monochromatic quotient

Let `G` be a graph which is not `p`-colourable, let `F` be a set of
edges, and put

\[
                         K=G-F.
\]

Let `c` be a proper `p`-colouring of `K`.  Suppose that every endpoint
of every edge of `F` receives one fixed colour `alpha`.  Fix a colour
`beta != alpha`, and let

\[
             \mathcal C_{\alpha\beta}
       =\operatorname{comp}\bigl(K[c^{-1}(\{\alpha,\beta\})]\bigr).
\]

Define the multigraph `Gamma_beta` as follows.  Its vertices are the
members of `mathcal C_{alpha beta}`, and every edge `xy in F` becomes an
edge between the components containing `x` and `y`.  If those
components coincide, the resulting edge is a loop.  Different edges of
`F` are retained as different edges.

### Theorem 1.1 (Kempe-component odd-cycle obstruction)

For every `beta != alpha`, the multigraph `Gamma_beta` is not bipartite.
Equivalently, it contains an odd cycle, where a loop counts as a cycle
of length one.

#### Proof

Suppose that `Gamma_beta` is bipartite, with bipartition `(X,Y)`.
Interchange `alpha` and `beta` on every component belonging to `X`.
The components are pairwise disjoint two-colour components of `K`, so
performing all these Kempe interchanges preserves properness on `K`.

For an edge `xy in F`, the components containing `x` and `y` lie on
opposite sides of the bipartition.  Exactly one of its endpoints is
therefore changed from `alpha` to `beta`; the other remains `alpha`.
Thus every edge of `F` becomes proper.  Since every edge of `G` belongs
to `K` or to `F`, this gives a proper `p`-colouring of `G`, a
contradiction.  Hence `Gamma_beta` is not bipartite.  A multigraph is
bipartite exactly when it has no odd cycle, with loops treated as odd
cycles of length one.  \(\square\)

The proof gives the following exact repair criterion, which is sometimes
more useful than the contradiction formulation.

### Proposition 1.2 (repair criterion)

There is a union of `alpha,beta` components of `K` whose simultaneous
Kempe interchange makes every edge of `F` proper if and only if
`Gamma_beta` is bipartite.

#### Proof

The forward direction assigns bit one to an interchanged component and
bit zero to an unchanged component.  Since both ends of every row start
with colour `alpha`, that row is repaired exactly when its two component
bits differ.  These bits are a proper two-colouring of `Gamma_beta`.
The reverse direction is the construction in Theorem 1.1.  \(\square\)

### Corollary 1.3 (labelled odd-cycle carrier)

For every `beta != alpha`, there are pairwise vertex-disjoint connected
`alpha,beta` subgraphs

\[
                       C_1,\ldots,C_{2r+1}
\]

and distinct named rows `f_1,...,f_{2r+1} in F` such that, cyclically,
`f_i` has one endpoint in `C_i` and one endpoint in `C_{i+1}`.  The case
`r=0` means that one row has both endpoints in `C_1`.

#### Proof

Take a shortest odd cycle in `Gamma_beta`.  Its quotient vertices are
distinct unless it is a loop, so the corresponding two-colour
components are pairwise disjoint and connected.  Its quotient edges are
distinct retained edges of `F` and give the claimed literal cyclic
adjacencies.  \(\square\)

Thus the general edge-set conclusion is a labelled odd-cycle model,
not necessarily a path or triangle.  The theorem makes no assertion
that this odd cycle is induced in `G`.

## 2. Three deleted matching edges

Assume in addition that

\[
                         F=\{e_1,e_2,e_3\}
\]

is a three-edge matching.

### Corollary 2.1 (loop-or-literal-triangle)

For every `beta != alpha`, at least one of the following alternatives is
available (they need not be mutually exclusive if more than one odd
cycle is present).

1. Some row `e_i=x_i y_i` has both ends in one
   `alpha,beta` component of `K`.  In particular, `K` contains an
   `alpha,beta` path from `x_i` to `y_i`.
2. There are three pairwise vertex-disjoint connected
   `alpha,beta` subgraphs `C_1,C_2,C_3` such that, cyclically, `e_i`
   has one endpoint in `C_i` and one endpoint in `C_{i+1}` (after
   relabelling the rows).  Consequently the three carriers are pairwise
   adjacent in `G` through the three distinct named rows of `F`.

#### Proof

The quotient has three edges.  If it has a loop, item 1 follows from the
definition of a two-colour component.  If it has no loop, Theorem 1.1
gives an odd cycle of length at least three.  Since the quotient has only
three edges, this cycle is a literal triangle and uses all three rows.
Its three vertices correspond to three distinct, hence vertex-disjoint,
connected components of the two-colour graph.  The matching hypothesis
ensures that the six row endpoints are literal distinct vertices; the
three quotient edges give exactly the adjacencies asserted in item 2.
\(\square\)

Thus a three-row common-colour lock cannot consist of three unrelated
Kempe failures.  For each second colour it either yields an ordinary
row path or packages all three rows into a triangle of disjoint labelled
carriers.

More generally, if `|F|=m`, then `Gamma_beta` contains an odd cycle of
length at most the largest odd integer not exceeding `m`.  In particular,
for `m <= 4` it contains a loop or a triangle.  For larger `m`, genuine
odd cycles of length five or more cannot be replaced by triangles
without additional hypotheses.

## 3. Signed two-colour form

The common-colour hypothesis has a precise signed generalisation.  It is
also the correct way to handle rows which are already proper under `c`.

Fix two colours `alpha,beta`.  Let `F_{alpha beta}` consist of the edges
of `F` both of whose endpoint colours lie in `{alpha,beta}`.  Every edge
of `F-F_{alpha beta}` has invariant equality status under interchanges
of `alpha,beta` components.  Indeed, either neither endpoint changes, or
exactly one endpoint has a colour in `{alpha,beta}` and the other has a
third colour, in which case the edge is proper before and after every
such interchange.

Form a multigraph `Gamma_{alpha beta}` on the components of the
`alpha,beta` subgraph of `K`, retaining the edges of `F_{alpha beta}`.
Encode `alpha` by zero and `beta` by one.  Give a quotient edge
`e=uv` the label

\[
  \rho(e)=1\mathbin\oplus\bigl(c_2(u)\mathbin\oplus c_2(v)\bigr),
                                                               \tag{3.1}
\]

where `c_2` is the zero-one encoding.  Thus `rho(e)=1` when the row is
currently equal and `rho(e)=0` when it is currently proper.

### Theorem 3.1 (signed Kempe repair criterion)

There is a union of `alpha,beta` components whose simultaneous
interchange makes every edge of `F_{alpha beta}` proper if and only if the equations

\[
       s(C_u)\mathbin\oplus s(C_v)=\rho(uv),
              \qquad uv\in F_{\alpha\beta},                  \tag{3.2}
\]

have a solution over `GF(2)`.  Equivalently, the xor of the labels
`rho` around every quotient cycle is zero.  When a solution is used, the
resulting exact equality set on all of `F` is

\[
            \operatorname{Eq}_F(c)-F_{\alpha\beta}.          \tag{3.3}
\]

Consequently, if `G` is not `p`-colourable and every currently equal row
belongs to `F_{alpha beta}`, then `Gamma_{alpha beta}` contains an
**unbalanced** cycle: a cycle on which the label xor is one.

#### Proof

Let `s(C)` record whether component `C` is interchanged.  For
`uv in F_{alpha beta}`, its final endpoint-colour difference is

\[
 (c_2(u)\oplus s(C_u))\oplus
 (c_2(v)\oplus s(C_v)).
\]

The edge is proper exactly when this value is one, which is equivalent
to (3.2).  As observed above, equality status outside
`F_{alpha beta}` is invariant.  Hence a solution of (3.2) gives exactly
(3.3), and every union repairing `F_{alpha beta}` supplies such a
solution.

A zero-one difference system on a multigraph is soluble exactly when
the xor of its right-hand sides around every cycle is zero.  This
includes loops and two-edge cycles formed by parallel edges.  If all
cycles were balanced and every equal row belonged to
`F_{alpha beta}`, (3.3) would be empty and the switched colouring would
extend to a `p`-colouring of `G`.  Therefore some unbalanced cycle exists
under the stated final hypothesis.  \(\square\)

Theorem 1.1 is the special case in which every quotient edge has label
one.  Then an unbalanced cycle is exactly an odd cycle.  With three
quotient edges, the signed obstruction can instead be

* a label-one loop;
* two parallel edges with different labels (an unbalanced two-cycle); or
* a triangle whose three labels have xor one.

This signed trichotomy is the exact small-row statement.  In particular,
parallel quotient edges cannot simply be discarded.

### Corollary 3.2 (two defect colours)

Suppose every edge of `F` is monochromatic under `c` and all endpoints
of `F` use colours from one pair `{alpha,beta}`.  Then every quotient
edge has label one, so `Gamma_{alpha beta}` is nonbipartite and contains
an odd cycle.  If `F` is a three-edge matching, the loop-or-literal-
triangle conclusion of Corollary 2.1 holds with these
`alpha,beta` components.

#### Proof

Here `F_{alpha beta}=F` and `Eq_F(c)=F`.  If the signed quotient were
balanced, Theorem 3.1 would make every row proper and would
`p`-colour `G`.  Thus it has an unbalanced cycle.  Every row is
monochromatic, so every label is one and an unbalanced cycle is exactly
an odd cycle.  The three-edge conclusion follows as in Corollary 2.1.
\(\square\)

### Corollary 3.3 (defect peeling)

Let `D=Eq_F(c)`.  For any colour pair `alpha,beta`, exactly one of the
following holds.

1. `Gamma_{alpha beta}` has an unbalanced cycle.
2. A simultaneous union of literal `alpha,beta` Kempe interchanges
   produces, from the same colouring `c`, a proper colouring `c'` of
   `K` with

   \[
                 \operatorname{Eq}_F(c')=D-F_{\alpha\beta}.
   \]

#### Proof

If the signed system is inconsistent, the cycle criterion in Theorem
3.1 gives item 1.  If it is consistent, a solution gives item 2 by
(3.3).  \(\square\)

If `F` is a matching and the residual set
`D-F_{alpha beta}` in item 2 is nonempty, the resulting colouring also
descends to the proper contraction minor

\[
                    G/(D-F_{\alpha\beta}).
\]

Indeed, the residual equal rows are pairwise disjoint and may be
contracted, while every deleted row outside the residual is proper under
`c'`.  Thus the peeling alternative is a legal contraction state in the
matching-deletion setting.

For a three-edge matching whose three rows are all equal under `c`, this
has two useful specialisations.

* If `p >= 3`, exactly two rows have common endpoint colour `alpha`, and
  the third has a different common endpoint colour `delta`, choose
  `beta` different from both `alpha` and `delta`.  The quotient contains
  precisely the two repeated-colour rows, both with label one.  Hence
  either one of those rows is a loop and has an `alpha,beta` path in
  `K`, or a simultaneous Kempe interchange reaches the exact singleton
  state consisting of the `delta`-coloured row.  Two parallel label-one
  quotient edges form a balanced two-cycle, so there is no additional
  obstruction.
* If `p >= 4` and the three equal rows have three distinct common endpoint
  colours, fix one row of colour `alpha` and choose `beta` outside those
  three colours.  The quotient contains just that one label-one row.  Hence
  either its ends have an `alpha,beta` path in `K`, or a simultaneous
  Kempe interchange reaches the exact double state consisting of the
  other two rows.

These are state-preserving facts about one chosen colouring.  They are
strictly stronger than knowing abstractly that separate singleton and
double contraction colourings exist.  They still do not supply
disjointness between carriers belonging to different choices of
`beta`.

## 4. Palette-component chromatic obstruction

The parity theorem is the two-colour case of a broader componentwise
palette-shift principle.

Let `A` be a set of `q >= 2` colours.  Suppose every edge of `F` is
monochromatic under `c` and its common endpoint colour belongs to `A`.
Let

\[
       \mathcal C_A
       =\operatorname{comp}\bigl(K[c^{-1}(A)]\bigr),
\]

and form the multigraph `Gamma_A` by retaining every row of `F` between
the components containing its endpoints.

### Theorem 4.1 (palette-component obstruction)

The multigraph `Gamma_A` is not `q`-colourable.  Consequently:

1. if
   \[
                       |F|<\binom{q+1}{2},
   \]
   then `Gamma_A` has a loop, and some row of `F` has its endpoints
   joined in `K` by a path using only colours from `A`;
2. if `|F|=binom(q+1,2)`, then either the same loop conclusion holds or
   `Gamma_A` consists, on its nonisolated simple core, of a literal
   `K_{q+1}` whose edges are the distinct named rows of `F`.  Its
   `q+1` vertices lift to pairwise vertex-disjoint connected `A`-colour
   carriers which are pairwise adjacent through those rows.

#### Proof

Identify the colours in `A` with the cyclic group `Z_q`.  Suppose that
`Gamma_A` has a proper `q`-colouring `s`.  For every component
`C in mathcal C_A`, add `s(C)` modulo `q` to the colour of every vertex
of `C`; leave vertices whose colours lie outside `A` unchanged.

This preserves properness on `K`.  Indeed, the operation on one
`A`-component is a permutation of `A`.  Every `K`-edge with both endpoint
colours in `A` has both endpoints in the same component and hence sees
the same permutation; an edge with just one endpoint colour in `A`
remains proper because its other colour lies outside `A`; and all other
edges are unchanged.

For a row `xy in F`, both endpoints initially have the same colour in
`A`.  Properness of `s` on the corresponding quotient edge gives
`s(C_x) != s(C_y)`, so the two shifted endpoint colours are different.
Thus all rows of `F` become proper and the shifted colouring is a proper
`p`-colouring of `G`, a contradiction.  Therefore `Gamma_A` is not
`q`-colourable.

If `Gamma_A` is loopless, its underlying simple graph has chromatic
number at least `q+1`.  It contains a `(q+1)`-critical subgraph `J`, for
which `delta(J) >= q`; hence

\[
 |E(J)|\ge \frac{q|V(J)|}{2}
          \ge \frac{q(q+1)}2=\binom{q+1}{2}.        \tag{4.1}
\]

Every simple edge of `J` uses at least one distinct retained row of
`F`.  This proves item 1.  At equality throughout (4.1), `J` has exactly
`q+1` vertices, all of degree `q`, and is therefore `K_{q+1}`.  There is
no room in `F` for an additional quotient edge or a parallel duplicate,
which proves item 2 and its literal carrier interpretation.  \(\square\)

### Corollary 4.2 (uniform three-colour row path)

Assume `p >= 3`.  Let `F` consist of three edges and suppose all three
rows are equal in one proper colouring `c` of `K=G-F`.  Then some row
has its endpoints joined in `K` by a path using at most three colours.

If `F` is a matching, this is a literal path between one of the three
named pairs.  In addition, the finer colour-pattern conclusions are as
follows.

* If the three common row colours use at most two palette labels, the
  relevant two-colour quotient has a loop or a literal carrier triangle
  (when only one label occurs, adjoin any second palette label).
* If they use three distinct labels, let `A` be those three labels.
  Since
  \[
                          3<\binom42=6,
  \]
  some row has its endpoints joined in `K` by a path using only the
  three labels in `A`.

#### Proof

Choose a three-colour set `A` containing the common endpoint colour of
every row.  This is possible because there are three rows.  Theorem 4.1
applies with `q=3`, and

\[
                          |F|=3<\binom42=6.
\]

Thus the quotient has a loop, which is the asserted three-colour path.
The two finer bullets are Corollary 3.2 and the same application of
Theorem 4.1, respectively.  \(\square\)

Thus every all-equal three-row colouring supplies a literal bounded-
palette carrier.  The theorem does not say that the path in the
three-distinct case is bichromatic, or that a carrier avoids one of the
named `K_4` cores.

## 5. What the theorem does and does not say

1. The theorem is uniform in `p`, does not use criticality, and does not
   require `F` to be a matching.  The matching hypothesis in Corollary
   2.1 is used only to obtain six distinct literal row endpoints and the
   clean named-carrier interpretation.
2. A forest in the original graph `(V(F),F)` is irrelevant.  Even when
   `F` is a matching, contracting two-colour components can turn it into
   a triangle.  The correct forest/bipartiteness test is on the
   component quotient `Gamma_beta`.
3. An even quotient cycle is not an obstruction: alternating component
   switches repair all of its all-`alpha` rows.  The parity, not merely
   the existence of a cycle, is essential.
4. In an `HC_7` matching-deletion state, saying that all three rows are
   **equal** means only that the two ends of each row share a colour.
   It does not imply that the three rows share one common colour.  The
   all-`alpha` theorem may therefore be invoked only when that stronger
   common-colour conclusion has actually been proved.  Corollary 3.2
   handles two defect colours, while Theorem 4.1 handles three distinct
   defect colours only by a three-colour path, not by a bichromatic
   triangle.  Three distinct defect colours remain outside any single
   simultaneous two-colour treatment.
5. The triangle alternative supplies three disjoint pairwise-adjacent
   carriers, but only a literal `K_3` model by itself.  Turning it into a
   `K_7` requires independent labelled contacts to the named `K_4`
   cores or another composition theorem.
