# A defect-one capacity/state theorem for a near-`K_7` web

## 1. Scope and outcome

This note proves a new uniform infinite-family result for the
`K_7^\vee` backup route.  It deliberately permits the planar
`K_2`-join architectures: a globally compatible rural expansion is an
explicit two-apex outcome, not a contradiction obtained from connectivity.

The new point is a sharp **chain exchange**.  In the one-complex
`K_7^\vee` normalization, four consecutive connected pieces, each dark to
at most one singleton row, always contain a labelled `K_7`-model.  Three
pieces have only ten negative row words.  The only two length-four overlaps
are `abba,acca`, and retaining the fourth piece gives an explicit
seven-bag model in both cases.  The pieces may have arbitrary order and
arbitrary internal graph.

Combining this capacity theorem with crossed minor-colouring states gives
a finite size bound for any defect-one capacity/state web: at most three
vertex levels and branching at most 108.  Hence an arbitrarily large web must yield
one of the following concrete outcomes:

1. a labelled split and a `K_7`-minor;
2. a coherent rural expansion, hence a two-apex graph; or
3. two faithful proper-minor colourings with a common transported boundary
   state, which splice to a six-colouring.

This does not prove `HC_7`: it does not show that every complex bag admits
the defect-one web decomposition used in Section 4.  It does eliminate all
unbounded members once that structural output is available.

## 2. The sharp three-piece quotient

Let

\[
 L=\{a,b,c,q_1,q_2,q_3\}
\]

induce `K_6-{ab,ac}`.  Let `X_1,X_2,X_3` be pairwise disjoint nonempty
connected sets, with an edge from `X_1` to `X_2` and from `X_2` to
`X_3`.  Extra edges are allowed.  Put

\[
 \rho(X_i)=\{\ell\in L:E(X_i,\ell)\ne\varnothing\}.
\]

Assume `|rho(X_i)|>=5`.  Give `X_i` type `*` if it sees all six labels,
and otherwise give it the unique type

\[
                       \tau_i\in L-\rho(X_i).
\]

### Theorem 2.1 (defect-one three-piece exchange)

The graph contains a `K_7`-minor unless no type is `*` and

\[
 (\tau_1,\tau_2,\tau_3)
 \in \mathcal E,                                      \tag{2.1}
\]

where

\[
\begin{aligned}
 \mathcal E={}&
 \{(c,q_i,b),(b,q_i,c):1\le i\le3\}\\
 &\cup\{(c,c,a),(b,b,a),(a,b,b),(a,c,c)\}.           \tag{2.2}
\end{aligned}
\]

The assertion is one-way: an exceptional word may still give a `K_7`
through additional contacts or internal geometry.

#### Proof

Contract each `X_i` to a vertex `x_i`, retain the two path edges, retain
the six labelled vertices, and delete every edge not forced by its support
row.  Call the resulting nine-vertex graph `Q(tau_1,tau_2,tau_3)`;
`tau_i=*` means that `x_i` is complete to `L`.

The dependency-free verifier
`near_k7_defect_one_chain_verify.py` checks all

\[
                              7^3=343
\]

support triples.  Since every quotient is connected, any `K_7`-model can
be made spanning by absorbing each unused component into an adjacent bag.
Thus it is exhaustive to enumerate the

\[
                         {9\brace7}=462
\]

partitions of all nine vertices into seven nonempty branch bags.  For each
partition the verifier directly checks connectedness, disjointness, and
all 21 pairwise bag adjacencies.  It finds and replays a model in 333
profiles.  The ten negative profiles are exactly (2.2).
Running the verifier with `--catalogue` prints the seven branch bags for
every one of the 333 positive profiles.  For example, in the full profile
`(*,*,*)` it prints

\[
 \{a,b,X_1\}\mid\{c\}\mid\{q_1\}\mid\{q_2\}\mid
 \{q_3\}\mid X_2\mid X_3,                            \tag{2.3}
\]

while for the positive profile `(a,b,c)` it prints

\[
 \{a,b,X_3\}\mid\{c\}\mid\{q_1\}\mid\{q_2\}\mid
 \{q_3\}\mid X_1\mid X_2.                            \tag{2.4}
\]

The literal `ab` nonedge causes no problem in (2.3)--(2.4): the displayed
two-vertex labels lie in one connected bag through the adjacent piece,
and the verifier checks every external bag adjacency separately.

Every positive quotient model lifts through the three contractions to the
original connected sets.  Adding contacts or edges cannot destroy a minor,
so the verified quotient assertion proves the theorem.  QED.

The certificate is small enough to replace by a printed 333-row catalogue,
but the exact partition verifier is both shorter and stronger: it proves
negative exhaustiveness as well as replaying every positive model.

## 3. The overlap principle

### Corollary 3.1 (four-piece residue)

Let `X_1,X_2,X_3,X_4` be a chain of pairwise disjoint connected pieces,
each seeing at least five labels of `L`.  If there is no `K_7`-minor, then
all four pieces have defect one and

\[
 (\tau_1,\tau_2,\tau_3,\tau_4)
 \in\{(a,b,b,a),(a,c,c,a)\}.                        \tag{3.1}
\]

#### Proof

Apply Theorem 2.1 to the first and last consecutive triples.  Both length
three subwords must lie in `mathcal E`.  Inspecting (2.2), the only
suffix/prefix overlaps of length two are

\[
                (a,b,b)\cdot(b,b,a),\qquad
                (a,c,c)\cdot(c,c,a),
\]

which give (3.1).  QED.

### Theorem 3.2 (four-piece chain theorem)

Let `X_1,...,X_4` be pairwise disjoint nonempty connected sets such that
`X_i` is adjacent to `X_{i+1}` for `1<=i<4`.  If every piece sees at
least five labels of `L`, then the graph contains a `K_7`-minor.

#### Proof

Otherwise Corollary 3.1 makes the word either `abba` or `acca`.

For `abba`, use the seven bags

\[
 \{a,b\}\cup X_1\cup X_2\mid\{c\}\mid\{q_1\}\mid
 \{q_2\}\mid\{q_3\}\mid X_3\mid X_4.                 \tag{3.2}
\]

The first bag is connected through `bX_1`, `X_1X_2`, and `aX_2`; it
sees `X_3` through `X_2X_3` and sees `X_4` through `b`.  All remaining
pairs are forced support-row or singleton-clique edges.

For `acca`, use

\[
 \{a,c\}\cup X_1\cup X_2\mid\{b\}\mid\{q_1\}\mid
 \{q_2\}\mid\{q_3\}\mid X_3\mid X_4.                \tag{3.3}
\]

Now `cX_1`, `X_1X_2`, and `aX_2` connect the first bag; it sees `X_3`
through `X_2X_3` and sees `X_4` through `c`.  Again every remaining pair
is a forced edge.  Both cases give `K_7`, a contradiction.  QED.

The theorem is uniform in the orders and treewidths of the pieces.  It is
therefore a genuine owner-depth theorem, not a bounded quotient-order
assumption.

## 4. Capacity-state webs

We isolate the exact structural object to which the theorem applies.  A
**defect-one `K_7^\vee` web decomposition** consists of the six singleton
labels `L` above and a rooted tree `T` of pairwise disjoint connected
pieces `X_t` such that:

1. the pieces cover the whole complex bag:

   \[
                         V(B)=\mathop{\dot\bigcup}_{t\in V(T)}X_t;
   \]

2. adjacent nodes of `T` correspond to adjacent pieces;
3. every root-to-leaf path orders vertex-disjoint pieces with consecutive
   adjacencies; additional nonconsecutive edges are harmless;
4. every piece sees at least five labels of `L`;
5. for every child `s` of a branching node, let `D_s` be the union of all
   pieces in the subtree rooted at `s`.  These child-subtree unions are
   open lobes behind one actual two-cut `{x,y}` of the complex bag, are
   pairwise anticomplete, and have all external neighbours in
   
   \[
                  W=L\mathbin{\dot\cup}\{x,y\};             \tag{4.1}
   \]
6. deleting any one open child-subtree lobe `D_s` is a
   boundary-faithful proper minor.

These hypotheses retain actual vertices and sides of the original graph;
they are not a chain of quotient contractions.

### Lemma 4.1 (faithful branching bound)

Let `G` be proper-minor-minimal non-six-colourable.  At a branching
two-cut in (4.1), there are at most 108 open child lobes.

#### Proof

The five-clique

\[
                         \{b,c,q_1,q_2,q_3\}
\]

is rainbow in every six-colouring of a proper minor.  The vertex `a` is
adjacent to the three `q_i` and nonadjacent to `b,c`, so its equality
class is the class of `b`, the class of `c`, or the unique sixth class.
Each of `x,y` has at most six choices.  There are therefore at most

\[
                              3\cdot6^2=108              \tag{4.2}
\]

equality partitions of `W`.

For each child-subtree lobe `D_i`, colour the proper minor `G-D_i` and retain its
state on `W`.  If two different deleted-lobe minors induce the same state,
align their palettes on `W`.  On `D_i` use the colouring in which `D_i`
was retained, and on `D_j` use the colouring in which `D_j` was retained;
use either colouring on the common remainder.  The two lobes are
anticomplete and all their external edges end in `W`, so this splices to a
six-colouring of `G`.  Hence the selected states are pairwise distinct,
and (4.2) gives the bound.  QED.

The same proof gives the promised third outcome outside a counterexample:
two lobes with one common faithful state directly produce the global
six-colouring.

### Theorem 4.2 (finite capacity-state web theorem)

In a `K_7`-minor-free, proper-minor-minimal non-six-colourable graph, a
defect-one `K_7^\vee` web decomposition has at most

\[
             1+108+108^2=11,773                       \tag{4.3}
\]

pieces.

#### Proof

Theorem 3.2 forbids a root-to-leaf path with four pieces.  Thus `T` has at
most three vertex levels.  Lemma 4.1 gives at most 108 children per node.
The elementary rooted-tree count gives (4.3).  QED.

The numerical constant is irrelevant; the structural conclusion is that
arbitrary depth and arbitrary branching are both eliminated by one
labelled capacity certificate plus one faithful-state splice.

## 5. Coherent rural outcome

Choose two neutral labels, say `q_1,q_2`.  After deleting them, the simple
one-complex quotient on

\[
                       a,b,c,q_3,B
\]

is `K_5-{ab,ac}`, which is planar.  When the complex bag is represented by
several web pieces, **globally compatible** means more than planarity of
this coarsest quotient: the full quotient obtained by contracting each
piece separately has a plane embedding, including every parallel contact
edge, and every piece society is rural in its induced rotation.

### Lemma 5.1 (coherent web is two-apex)

If the full piece quotient has such a plane embedding and every piece
society is rural in its induced rotation, then

\[
                          G-\{q_1,q_2\}
\]

is planar.  Hence `G` is two-apex.

#### Proof

Take the plane quotient drawing, choose disjoint disks about all expanded
vertices, and substitute the prescribed rural drawings, matching every
portal occurrence in its recorded cyclic order.  Compatibility at both
ends of every parallel bundle draws every original edge.  This is a plane
drawing of the displayed deletion, not merely of its simple contracted
quotient.  QED.

In a hypothetical `HC_7` counterexample this outcome is impossible: the
planar remainder is four-colourable, and the two deleted vertices can be
given two fresh colours.

### Corollary 5.2 (large-web split/rural/state trichotomy)

Let a seven-connected, proper-minor-minimal non-six-colourable graph with
the one-complex `K_7^\vee` normalization admit a defect-one web
decomposition.  If the decomposition has more than the bound (4.3), or if
its rotations are globally coherent, then at least one of the following
holds:

1. four consecutive pieces give the labelled `K_7` split of Theorem 3.2;
2. the compatible rural expansion of Lemma 5.1 makes the graph two-apex;
3. two open lobes have a common faithful proper-minor boundary state and
   crossed splicing six-colours the graph.

#### Proof

The coherent case is Lemma 5.1.  Otherwise, if the tree exceeds (4.3), it
   has either a four-vertex root-to-leaf path or a node with at least 109
children.  Apply Theorem 3.2 in the first case and the pigeonhole/splicing
argument of Lemma 4.1 in the second.  QED.

This is the desired safe alternative.  It allows the `K_2`-join-planar
architectures in outcome 2, and it uses minor-criticality only for the
faithful state outcome.  It does not claim that seven-connectivity alone
forces a labelled split.

## 6. Exact frontier

The near-`K_7` backup now has a new bounded residue.  A surviving
one-complex `K_7^\vee` web must:

* have at most three consecutive defect-one pieces;
* have at most 108 lobes at every actual two-cut;
* have no globally compatible rural rotation; and
* every three-piece run has one of the ten exceptional profiles (2.2).

Thus the former `abba/acca` four-piece residue is closed.  What remains
unproved is the local exchange at one of the ten three-piece profiles, when
some intervening piece has defect at least two, or when the web decomposition
itself fails.  The present theorem does not silently call those states a
split.

## 7. Adversarial scope audit

### 7.1 Exact status of the defect-one hypothesis

Condition 4 in the web definition is a genuine hypothesis.  It is
automatic for a **whole** lobe `D` behind one two-cut `{x,y}` when all its
other external neighbours are among `L`: another lobe or the far side lies
beyond its neighbourhood, so seven-connectivity gives

\[
 7\le |N_G(D)|\le2+|\rho(D)|,
\]

and hence `|rho(D)|>=5`.

It is not automatic for every annular difference in a nested web.  Such a
piece may have vertices from both a parent and a child adhesion in its
external neighbourhood; four or more nonlabel boundary vertices leave
room for two or more dark singleton rows.  Neither seven-connectivity nor
the Norin--Totschnig `K_7^\vee` minor by itself supplies condition 3.

Consequently Theorems 2.1 and 3.2 are unconditional once the displayed
pieces exist, and Lemma 4.1 is unconditional at each actual two-cut, but
Theorem 4.2 applies only to a decomposition whose **individual node
pieces**, not merely its child-subtree unions, satisfy defect at most one.
Proving that every hypothetical counterexample has such a decomposition,
or controlling a defect-at-least-two annulus, remains open.

### 7.2 Chain certificate audit

The quotient is connected, so spanning partition enumeration loses no
minor: every unused connected component can be absorbed into an adjacent
branch bag.  There are exactly `{9\brace7}=462` spanning partitions.  The
verifier enumerates all of them for all 343 profiles, and its independent
replay checks:

* seven nonempty disjoint bags covering all nine quotient vertices;
* connectedness of each bag; and
* all 21 pairwise bag adjacencies.

The output is reproducible:

```
profiles 343
K7-positive 333
K7-negative 10
length-four words 2
length-five words 0
```

The word overlap proof uses only the verified negative set and has no
graph-theoretic hidden assumption.  Extra contacts, extra edges between
pieces, and unused vertices are monotone additions and cannot invalidate a
positive certificate.

### 7.3 State-bound audit

The 108 count is an upper bound on equality partitions, not on named
colourings.  The five-clique fixes five distinct blocks; `a` has at most
three possible blocks and each cut vertex at most six.  Equality of states
therefore permits a palette alignment on all of `W`.

The splice uses deletions of the entire child-subtree lobes `D_i,D_j`.
After alignment, colour `D_i` from the minor in which `D_j` was deleted,
colour `D_j` from the minor in which `D_i` was deleted, and use either
colouring on the common remainder.  The lobe unions are anticomplete and
all external edges end in `W`, so every restored edge is proper.  This
justifies both the branching bound and the common-faithful-state outcome.

With at most three vertex levels and at most 108 children at each node, the
rooted-tree bound is exactly

\[
                  \sum_{i=0}^{2}108^i=11,773.
\]

### 7.4 Final verdict

**GREEN under the stated defect-one web-decomposition hypotheses.**  The
result is a real infinite-family closure and is safe against planar
two-apex joins.  **The existence of the required decomposition for an
arbitrary Norin--Totschnig `K_7^\vee` model is not proved.**
