# Independent audit of deficient-singleton joint persistence

**Verdict:** GREEN for Theorem 1.1, its exact maximum-capacity and
complement-matching conclusions, and the conditional `HC_7` colouring and
dense-alternative consequences, including the two degree-nine exclusions,
at the source revision identified below.

**Audited source:** `hc7_deficient_singleton_joint_persistence.md`,
SHA-256

```text
2f413fa679fc7366920b9adbd1cdc9c419e7f2ff26c871ba8757ce2d8510c409
```

This hash is the promoted source after insertion of the two explicit
degree-nine `K_7`-minor constructions.  The audit below checks those
constructions directly rather than inheriting the earlier provisional
degree-ten threshold.

This is a separate internal mathematical audit, not external peer review.
The audit reconstructed the deletion-capacity argument independently,
including `t=3`, inclusion of a prescribed edge in a maximum deletion,
the exact non-joint-persistence graph, the degree-seven separator, and the
five-colour/label bijection in the nonadjacent maximum-pair trace.  It also
reconstructed the complete-graph-minus-matching minor argument, classified
the two provisional degree-nine equality cases, and checked both new
`K_7`-minor constructions branch set by branch set.  No unproved
colouring-to-model-label correspondence is used.

## 1. Neighbours of the deficient singleton

The model has labels of `F=K_t-rs`, with `B_r={x}`.  If `x` had an edge
to `B_s`, the same `t` branch sets would realize the sole missing model
adjacency and hence form a `K_t`-minor model.  Thus `x` is anticomplete to
`B_s`.

Because the model is spanning, every neighbour of `x` lies in a foreign
branch set.  The only possible foreign bags are therefore the `t-2` bags

\[
                     B_y\quad(y\notin\{r,s\}).
\]

Every corresponding model edge `ry` is required, so the singleton branch
set forces

\[
              n_y=|N_G(x)\cap B_y|\ge1.
\]

These bags partition `N_G(x)`, proving the exact degree identity in item
1.  This argument uses both spanning and `K_t`-minor exclusion; neither is
silently omitted.

## 2. Exact maximum deletion capacity

Deleting edges incident with the singleton cannot disconnect a branch
set.  For one label `y`, it destroys the required `B_r-B_y` adjacency
exactly when all `n_y` edges are deleted.  Operations at different labels
are independent.  Therefore a set `Z` is model-preserving exactly when

\[
       |Z\cap E_G(x,B_y)|\le n_y-1
       \quad\text{for every }y\notin\{r,s\},
\]

which is item 2.

Put `c_y=n_y-1`.  A `t`-connected graph has minimum degree at least `t`,
and hence

\[
 \sum_y c_y
   =\sum_y n_y-(t-2)
   =d_G(x)-(t-2)
   \ge2.                                                   \tag{A.1}
\]

Retaining one edge at each of the `t-2` labels and deleting all other
edges at `x` realizes a simultaneous deletion of exactly

\[
                         d_G(x)-(t-2)                       \tag{A.2}
\]

edges.  Conversely, every model-preserving deletion must retain at least
one edge at each required label and hence at least `t-2` incident edges in
total.  Thus (A.2) is both attainable and an upper bound.  This verifies
the word **maximum** in item 3, rather than only the existence of a set of
that order.

### The case `t=3`

There is one common-neighbour label `y`.  Equation (A.1) becomes

\[
                     c_y=d_G(x)-1\ge2,
\]

so `n_y=d_G(x)>=3`; retaining one edge and deleting all others gives the
claimed maximum.  Thus the proof remains valid at the smallest stated
parameter.  It does not rely on the possibility that the combined
connectivity and minor-exclusion hypotheses make some small-parameter
instances vacuous.

## 3. A prescribed edge in a maximum deletion

For a prescribed edge `xu` with `u in B_y`, deletion preserves the model
if and only if another `x-B_y` edge remains, equivalently `n_y>=2`.

When this holds, retain a different edge at label `y`, retain one arbitrary
edge at every other label, and delete every remaining incident edge.  The
deleted set has the maximum order (A.2) and contains `xu`.  This proves the
stronger inclusion-in-a-maximum-set assertion, including the case in
which all other capacity lies at the prescribed label.

If `xu` is not persistent, then `n_y=1`, giving exactly

\[
                         N_G(x)\cap B_y=\{u\}.
\]

This verifies both directions of item 4.

## 4. At least three persistent edges and the complement matching

The individually persistent incident edges are precisely the edges in
classes with `n_y>=2`.  Under (A.1), either

- one class has `n_y>=3`, supplying at least three persistent edges; or
- at least two classes have `n_y>=2`, supplying at least four.

Edges at different labels are jointly persistent.  Within one label,
two persistent edges fail to be jointly persistent exactly when
`n_y=2`; they are then the entire two-edge class.  If `n_y>=3`, every
pair leaves a surviving edge.  Consequently the graph whose vertices are
the persistent incident edges and whose edges are the non-jointly-
persistent pairs is a matching, with one matching edge for each label of
multiplicity exactly two.  An incident edge cannot occur in two such
pairs because the label classes partition the edges at `x`.

This verifies the exact complement-matching assertion, not merely an
upper bound on the number of exceptional pairs.

## 5. The `HC_7` application before the equality case

Section 2 of the source continues under all hypotheses of the uniform
theorem, and adds

\[
              t=7,\qquad \chi(G)=7,
 \qquad\text{every proper minor of }G\text{ is six-colourable}.
\]

Thus seven-connectivity and `K_7`-minor exclusion remain available.  A
maximum model-preserving deletion at `x` has order `d_G(x)-5`; any two
members can be retained as the selected jointly persistent pair.  The
common deletion graph is a proper minor, is six-colourable, and retains
the fixed labelled near-clique model.

If the two outer endpoints are nonadjacent, contracting their two-edge
star through `x` is a proper minor.  Expanding its colouring to the common
deletion graph is proper and gives the exact trace `{a,b}` on `N_G(x)`.
If they are adjacent, the minor-minimality, connectivity, minor exclusion,
and retained spanning model are precisely the hypotheses of the cited
jointly persistent incident-edge colouring theorem.  Its stated response,
separator, and dominating-core alternatives therefore apply.

## 6. Degree seven and the exact colour/label bijection

Assume `d_G(x)=7`.  The set `N_G(x)` has order seven.  The nonempty branch
set `B_s` is anticomplete to `x`, so it lies outside `N_G[x]`.  Deleting
`N_G(x)` therefore leaves the singleton component `{x}` and a nonempty
opposite side containing `B_s`.  Hence `N_G(x)` is the boundary of an
actual order-seven separation.

Now also suppose the maximum deleted pair `xa,xb` has nonadjacent outer
endpoints.  Since a maximum deletion at degree seven has order

\[
                         7-(7-2)=2,
\]

exactly five incident edges survive.  Model preservation requires one
survivor at each of the five common labels, so there is **exactly one**
surviving neighbour of `x` in each common branch set.

The star-contraction colouring gives `x,a,b` one colour `alpha`.  Each of
the five surviving neighbours is adjacent to `x` and hence uses a colour
different from `alpha`.  If one of the five alternate palette colours were
absent from those five neighbours, recolouring `x` with it would preserve
all surviving incident edges; restoring `xa,xb` would also be proper
because `a,b` retain colour `alpha`.  This would six-colour `G`, contrary
to `chi(G)=7`.

All five alternate colours therefore occur on five vertices and hence
occur bijectively.  Combining this with the exactly-one-survivor-per-label
fact gives a genuine bijection between the five common branch-set labels
and the five alternate colours.  This is not an implicit palette-to-label
inference: it follows from the degree-seven equality and maximum deletion.

Excluding an actual order-seven separation rules out `d_G(x)=7`.
Seven-connectivity then gives `d_G(x)>=8`, and (A.2) gives maximum deletion
capacity at least three, exactly as stated.

## 7. The deficient-singleton dense alternative

Let `P` be the outer endpoints of the persistent incident edges and put
`p=|P|`.  The persistent edges are partitioned by the five common labels.
Every pair from different repeated label classes is jointly persistent, as
is every pair within a class of order at least three.  Under the assumption
that all jointly persistent pairs have adjacent outer endpoints, the only
possible nonedges in `G[P]` are therefore pairs belonging to a class of
order exactly two.  Such pairs are disjoint, so

\[
                           G[P]=K_p-M'
\]

for a possibly proper submatching `M'` of those order-two pairs.  The word
“possibly proper” is essential: persistence alone does not determine
whether a nonjoint pair is adjacent in `G`.

### The bound `p<=6`

If `p>=8`, any eight vertices induce `K_8` minus a matching of order at
most four.  The audited support-class theorem gives an explicit `K_6`
minor in every such graph.  Since `{x}` is adjacent to every vertex of
`P`, adjoining it gives a `K_7`-minor model, contrary to the host
hypothesis.

Suppose `p=7`.  There can be at most two order-two label classes.  Indeed,
three such classes use six persistent edges; the seventh either enlarges
one class to order three, leaving only two order-two classes, or would have
to belong to another repeated class, which contributes at least two edges
and makes `p>=8`.  Hence `|M'|<=2`.  The graph `K_7-M'` has a `K_6` minor:
for two missing pairs, use one endpoint from each pair and the three
unmatched vertices as five singleton branch sets, and put the two unused
mates in one connected sixth branch set.  The cases of zero or one missing
pair are immediate.  Again adjoining `{x}` gives a `K_7` minor.  Therefore

\[
                                p\le6.                    \tag{A.3}
\]

### Degree and equality cases

Let `r_0` be the number of the five common labels with multiplicity at
least two.  Their incident edges are precisely the `p` persistent edges;
each remaining label contributes one nonpersistent edge.  Thus

\[
                          d_G(x)=p+5-r_0.                 \tag{A.4}
\]

If `r_0>=2`, equations (A.3)--(A.4) give `d_G(x)<=9`.  If
`r_0=1` and `p=6`, all six persistent endpoints lie in one label class of
order six.  Every pair is jointly persistent and hence adjacent under the
dense assumption, so they form a `K_6`; together with `{x}` this is a
`K_7`.  Thus `p<=5` when `r_0=1`, again giving `d_G(x)<=9`.

Equality in (A.4) can now occur only at

\[
             (r_0,p)=(1,5)\quad\text{or}\quad(2,6).
\]

The first case gives multiplicities `(5,1,1,1,1)`.  In the second, the
two repeated multiplicities sum to six and are either `2+4` or `3+3`.
The latter makes all six persistent endpoints pairwise adjacent, because
within-class and cross-class pairs are all jointly persistent; this gives
the forbidden `K_7` together with `x`.  Hence only
`(4,2,1,1,1)` remains.  In that case the two endpoints of the order-two
class must be nonadjacent, since otherwise the same six-vertex clique
occurs.

This proves the two provisional equality patterns.  The next section checks
that neither can occur in the `K_7`-minor-free host, strengthening the dense
bound from degree nine to degree eight.

## 8. Eliminating both degree-nine equality patterns

This section audits source lines 218--249 independently.  Throughout, the
outer endpoint set consists of neighbours of `x`, and the dense-alternative
hypothesis makes every jointly persistent pair of outer endpoints adjacent.

### 8.1 The pattern `(4,2,1,1,1)`

Let `A` be the four outer endpoints in the multiplicity-four class, and let
`u,v` be the two endpoints in the multiplicity-two class.

1. Any two members of `A` are jointly persistent: deleting two of the four
   contacts leaves two contacts to that label.  Hence the dense hypothesis
   makes `A` a clique.
2. Each of `u,v` is jointly persistent with every member of `A`, because
   the two edges have different branch-set labels.  Thus both `u` and `v`
   are complete to `A`.
3. The vertices `u,v` cannot be adjacent.  Otherwise `A union {u,v}` is a
   `K_6`, and the adjacent singleton `{x}` completes a `K_7` subgraph.

Put `S={x} union A`, so `|S|=5`.  Seven-connectivity implies that `G-S` is
connected; indeed, if it were disconnected then `S` would be a vertex cut
of order five.  The stronger assertion in the source that `G-S` is
two-connected also holds: a cut vertex of `G-S`, together with `S`, would
be a vertex cut of `G` of order six.  Both `u` and `v` lie in `G-S`, so a
simple `u`--`v` path `Q` exists there.  Because `uv` is absent, `Q` has at
least two edges, although the construction only needs one edge on which to
split it.

Choose an edge of `Q` and let `Q_u,Q_v` be the two nonempty connected
vertex sets on the two sides of that edge, with `u in Q_u` and `v in Q_v`.
The following seven sets are pairwise disjoint and connected:

\[
          \{x\},\qquad \{a\}\ (a\in A),\qquad Q_u,\qquad Q_v.
\]

Every required adjacency is literal:

- the four singleton sets from `A` are pairwise adjacent because `A` is a
  clique;
- `{x}` is adjacent to every `{a}`, to `Q_u` through `xu`, and to `Q_v`
  through `xv`;
- every `{a}` is adjacent to `Q_u` through `au` and to `Q_v` through `av`;
  and
- `Q_u` and `Q_v` are adjacent through the chosen path edge.

Thus these sets are a `K_7`-minor model.  No vertex of `A` or `x` can occur
inside either path branch set because `Q` was chosen in `G-S`.  This
contradicts the standing `K_7`-minor exclusion and eliminates the first
degree-nine pattern.

### 8.2 The pattern `(5,1,1,1,1)`

Let `P` be the five outer endpoints in the multiplicity-five class.  Any
two edges of that class are jointly persistent, since three contacts remain
after their deletion.  Hence the dense hypothesis makes `P` a five-vertex
clique.  Every member of `P` is a neighbour of `x`.

Choose one of the four singleton-multiplicity common labels and let `y` be
its unique neighbour of `x`.  The label classes are disjoint, so
`y notin {x} union P`.  Seven-connectivity of `G` implies six-connectivity
of `G-x`: any separator of `G-x` of order at most five, together with `x`,
would be a separator of `G` of order at most six.

Apply the Fan Lemma in `G-x` to the vertex `y` and the five-vertex set `P`.
Six-connectivity is stronger than the required five-connectivity, so there
are five paths from `y` to distinct vertices of `P` which meet pairwise only
at `y`.  Since there are five paths and five vertices of `P`, every member
of `P` is an endpoint.  Consequently no path contains a different member
of `P` internally: that would create an intersection with the path ending
there.  Equivalently, one may truncate each path at its first encounter
with `P`.

Let `T` be the union of these five paths after deleting their endpoints in
`P`.  Then:

- `T` is nonempty and connected because it contains the common vertex `y`;
- `T` is disjoint from `{x} union P`, since the fan lies in `G-x` and all
  its vertices in `P` were removed;
- `T` is adjacent to every member of `P` through the last edge of the
  corresponding fan path; and
- `T` is adjacent to `{x}` through the edge `xy`.

Therefore

\[
                       \{x\},\qquad T,\qquad \{p\}\ (p\in P)
\]

are seven disjoint connected branch sets.  The five singleton sets from
`P` are pairwise adjacent, `{x}` is adjacent to all of them, `T` is
adjacent to all of them, and `{x}` is adjacent to `T`.  They form a
`K_7`-minor model, eliminating the second degree-nine pattern.

### 8.3 The strengthened threshold

Section 7 independently established that the dense alternative implies
`d_G(x)<=9` and that equality has exactly the two patterns just eliminated.
Degrees are integral, so the dense alternative now implies

\[
                              d_G(x)\le8.
\]

Taking the contrapositive, if `d_G(x)>=9` then not every jointly persistent
pair has adjacent outer endpoints.  Hence there is a jointly persistent
pair whose outer endpoints are nonadjacent, exactly as claimed in source
lines 177--179 and 247--249.  Deleting that pair preserves the labelled
near-clique model, and its induced two-edge star is therefore available for
the exact star-contraction trace.  This implication uses no assumption that
the degree-nine dense patterns exhaust lower degrees.

## 9. Trust boundary

The source proves an unbounded model-preserving maximum-deletion theorem
and a conditional colouring reduction.  It does not prove that an
arbitrary prescribed edge is persistent, that a second selected edge has
a prescribed branch label, that a returned separator has order at most
seven, or that palette colours identify branch-set labels outside the
degree-seven maximum-pair equality case.  The complement-matching statement
is only about the incident edges at the singleton `x` for the fixed
displayed model.  These limitations agree with the source's trust
boundary.  The strengthened degree bound leaves the dense degree-eight
contact patterns unresolved; the audit does not infer a labelled repair
from their existence.
