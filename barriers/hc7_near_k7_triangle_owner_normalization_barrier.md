# A triangle owner cannot be normalized to a role-preserving bipartite carrier

## Status

This small `K_7`-minor-free graph falsifies the direct normalization

\[
 \text{arbitrary }K_7^\vee\text{ bag}
   \Longrightarrow
 \text{induced bipartite carrier preserving all six foreign roles}.
\]

It does not falsify P1 as stated, because the graph is two-apex.  Rather,
it proves that P1's rural alternative is logically indispensable before
criticality and seven-connectivity are used.

## 1. Construction

Let

\[
 U=\{u_0,u_1,u_2\},\qquad
 L=\{A,B,C,D_2,D_3,D_4\}.                                  \tag{1.1}
\]

Make `U` a triangle.  On `L`, take `K_6-{AB,AC}`.  Add exactly the
following edges between the two sets:

\[
 u_0A,u_0B,\qquad u_1C,u_1D_2,\qquad u_2D_3,u_2D_4.       \tag{1.2}
\]

There are no other edges.

### Proposition 1.1

The graph has a spanning labelled `K_7^vee` model, has no `K_7` minor,
and no connected induced bipartite subset of the complex bag `U` retains
all six foreign label roles.

#### Proof

Use the seven bags

\[
             U,\{A\},\{B\},\{C\},\{D_2\},\{D_3\},\{D_4\}. \tag{1.3}
\]

The bag `U` is connected and is collectively adjacent to all six other
bags.  The only missing required pairs among the singleton labels can be
chosen as `AB,AC`.  Thus (1.3) is a spanning `K_7^vee` model.

Suppose there were a `K_7` model.  Seven branch sets on nine vertices
leave at most two vertices beyond one per branch set, so at least five
branch sets are singletons.  These singleton vertices form a clique.  The
graph has a unique five-clique,

\[
                         Q=\{B,C,D_2,D_3,D_4\}.             \tag{1.4}
\]

(The six-vertex graph on `L` has this unique `K_5`.  A clique containing
one vertex `u_i` uses at most its two neighbours in `L`; a clique
containing two vertices of `U` uses no vertex of `L`, because the three
displayed foreign-neighbour pairs in (1.2) are disjoint.)  Hence the other
two branch sets must be
disjoint connected subsets of

\[
                         R=\{u_0,u_1,u_2,A\},               \tag{1.5}
\]

each adjacent to every vertex of `Q`.

But every `Q`-full subset of `R` contains both `u_0` and `u_1`:
`B` has the sole neighbour `u_0` in `R`, and `C` has the sole neighbour
`u_1` in `R`.  Two such subsets cannot be disjoint.  This excludes the
`K_7` model.

Finally, each of the three vertices of `U` is the unique owner in `U` of
its displayed pair of foreign labels.  A subset retaining all six roles
therefore contains all three vertices.  Its induced graph is the triangle
`G[U]`, which is not bipartite.  Every induced bipartite subset omits a
vertex and loses its two roles.  \(\square\)

## 2. Exact failed axioms

The graph is only four-connected and five-colourable.  For example, give
`D_2,D_3,D_4,B,C` five distinct colours, give `A` the colour of `B`,
and then colour `u_0,u_1,u_2` with the colours of `D_2,D_3,B`,
respectively.  (The literal `K_5` in (1.4) shows that five colours are
necessary.)  It is also
two-apex (the verifier lists several planarizing pairs).  Thus it does not
contradict the proof-spine target.  It identifies the legitimate P1
dichotomy:

* the triangle cannot be pushed into the audited bipartite singleton
  theorem without losing labels;
* it must instead be recognized as a rural expansion, or be destroyed by
  a colour-critical labelled exchange which is absent here.

This is the finite triangle-owner endpoint of the acyclic portal-ownership
normalization, not an unbounded case catalogue.
