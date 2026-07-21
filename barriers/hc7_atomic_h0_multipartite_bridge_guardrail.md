# A six-connected multipartite guardrail for atomic-frame bridges

**Status:** written barrier to common-apex compatibility and to an
unlabelled dominating-model exchange; separate internal audit GREEN.

This note records two exact obstructions exposed by the bridge normal form.
The first is the smallest pair of individually two-apex bridge paths with
no common planarizing pair.  Its natural saturation is the edge-maximal
`K_7`-minor-free graph `K_{3,2,2,2}`.  The saturation already regenerates a
normalized dominating `K_5` model after every two-vertex deletion, but it
fails the target hypothesis at the sharp point `kappa=6`.

Neither graph is a counterexample to `HC_7` or to the persistent atomic
rounding goal.  Seven-connectivity closes both configurations by the
[adjacent bridge result](../results/hc7_atomic_h0_bridge_quadrant_normal_form.md).

## 1. The smallest incompatible pair

Start with

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}.
\]

Replace the edge `ef` by the path `e-p-f`, and add the two edges

\[
                              xp,\qquad xg.              \tag{1.1}
\]

Call the resulting nine-vertex graph `R`.

The bridge path `xp` is individually safe: after deleting `e,f`, the
remaining graph is the planar octahedral graph `K_{2,2,2}` with a leaf.
The edge `xg` is also individually safe: after deleting `e,g`, the
remaining graph is another octahedral graph with a leaf.  Neither endpoint
support crosses `ab` or `cd`.

There is nevertheless no common planarizing pair among
`{e,f},{e,g},{f,g}` for their union.

- After deleting `e,f`, the graph contains the literal `K_{3,3}` with
  bipartition `({a,b,g},{c,d,x})`.
- After deleting `e,g`, the five sets

  \[
                  \{a,c\},\ \{b\},\ \{d\},\ \{f,p\},\ \{x\}
  \]

  form a `K_5` model.
- After deleting `f,g`, use the same model with `{e,p}` in place of
  `{f,p}`.

Thus the proposed implication

> individually safe bridge paths with incompatible clean-apex
> certificates force a `K_7` minor

is false already for two paths.

### Proposition 1.1

The graph `R` has no `K_7` minor.  It has the exact atomic common-frame
partition

\[
 \{x\},\ \{e\},\ \{a\},\ \{b\},\ \{c\},\ \{d\},\ \{f,p\},\ \{g\}, \tag{1.2}
\]

whose only absent bag adjacencies are `xe,ab,cd`.  Its connectivity is
exactly three, with the cut `N_R(p)={x,e,f}`.

#### Proof

The neighbourhood of `p` is the independent set `{e,f,x}`.  In `R-p`, a
clique containing `x` uses at most one of `a,b`, at most one of `c,d`, and
possibly `g`; a clique avoiding `x` uses at most one vertex from each of
`{a,b}`, `{c,d}`, and `{e,f}`, together with `g`.  Hence `omega(R)=4`.

Any clique-minor model in the connected graph `R` can be made spanning.  A
partition of nine vertices into seven nonempty branch sets has size pattern
`3+1+1+1+1+1+1` or `2+2+1+1+1+1+1`.  Its singleton branch sets would
therefore contain a `K_6` or a `K_5` subgraph, contradicting
`omega(R)=4`.  This proves the minor exclusion.  Direct inspection gives
(1.2).

The cut `N_R(p)` gives `kappa(R)<=3`.  The graph `R-p` is the complete
multipartite graph with parts

\[
                 \{e,f,x\},\ \{a,b\},\ \{c,d\},\ \{g\}.
\]

Deleting at most two vertices leaves it connected and leaves at least one
neighbour of `p`, so `R` minus those vertices is connected.  Thus
`kappa(R)=3`.  \(\square\)

One bridge path always has a planarizing pair by the exact 488-case
classification.  An order-eight example with two paths can only add two
unused branch-to-branch edges; the safe choices are among `xe,xf,xg`, and
deleting the corresponding two clean labels planarizes both.  Hence `R`
also has the minimum number of bridge paths and minimum order for this
compatibility failure.

## 2. The six-connected saturation

Add the four edges

\[
                              pa,pb,pc,pd               \tag{2.1}
\]

to `R`.  The resulting graph is exactly

\[
 M=K_{3,2,2,2}                                          \tag{2.2}
\]

with multipartite sets

\[
 U=\{e,f,x\},\quad A=\{a,b\},\quad C=\{c,d\},
 \quad D=\{g,p\}.                                      \tag{2.3}
\]

All the extra paths remain safe in the endpoint-support sense.  The vertex
`p` lies internally on `T_ef` and has support `{e,f}`, so none of
`xp,pa,pb,pc,pd` crosses `ab` or `cd`; neither does `xg`.

The atomic weak `K_7` immersion uses `a-x-b` and `c-x-d` as its two
colliding demand paths, uses `e-p-f`, and uses every other core edge
literally.  Partition (1.2) is still exact and retains the two contacts
from `x` to the `f`- and `g`-sets.

### Theorem 2.1 (sharp properties of the saturation)

The graph `M` has all of the following properties.

1. `M` is six-connected and has no `K_7` minor.
2. Adding any missing edge to `M` creates an explicit `K_7` minor.
3. For every two-set \(P\subseteq V(M)\), the graph `M-P` has an ordered
   dominating `K_5` model whose last three branch sets are singleton
   vertices inducing a triangle.
4. Consequently `M` has no two-vertex transversal of its dominating
   `K_5` models.

#### Proof

For a complete multipartite graph, deleting fewer than the number of
vertices outside a largest part leaves vertices in at least two parts and
therefore leaves the graph connected.  Deleting all six vertices outside
`U` disconnects its three vertices.  Hence `kappa(M)=6`.

The clique number of `M` is four.  The nine-vertex spanning-partition
argument from Proposition 1.1 again excludes a `K_7` minor.

Every nonedge lies inside one multipartite set.  If `uv` is added inside
`U`, write `U={u,v,w}` and write the other parts as
`{a_1,a_2}`, `{b_1,b_2}`, `{c_1,c_2}`.  The seven sets

\[
 \{u\},\ \{v\},\ \{w,a_1\},\ \{a_2\},\
 \{b_1,c_1\},\ \{b_2\},\ \{c_2\}                    \tag{2.4}
\]

form a `K_7` model.  If `a_1a_2` is added inside a part of order two,
write `U={u_1,u_2,u_3}` and use

\[
 \{a_1\},\ \{a_2\},\ \{u_1,b_1\},\ \{u_2,c_1\},
 \ \{u_3\},\ \{b_2\},\ \{c_2\}.                    \tag{2.5}
\]

Cross-part completeness verifies every adjacency in (2.4) and (2.5), and
symmetry covers every missing edge.

It remains to prove the dominating-model assertion.  There are four
orbits of deleted pairs.  The following tuples are ordered dominating
`K_5` models; vertices not displayed are unused.

1. After deleting two vertices of `U`, let `u` remain and write the other
   parts as `A={a_1,a_2}`, `B={b_1,b_2}`, `C={c_1,c_2}`.  Use

   \[
   (\{a_1,b_1\},\{a_2\},\{b_2\},\{c_1\},\{u\}).       \tag{2.6}
   \]

2. After deleting `u_3 in U` and `a_2 in A`, use

   \[
   (\{b_1,c_1\},\{b_2\},\{c_2\},\{u_1\},\{a_1\}).   \tag{2.7}
   \]

3. After deleting the whole part `A`, use

   \[
   (\{u_1,b_1\},\{u_2,c_1\},\{u_3\},\{b_2\},\{c_2\}). \tag{2.8}
   \]

4. After deleting `a_2,b_2` from two distinct parts of order two, use

   \[
   (\{u_1,a_1\},\{u_2,c_1\},\{b_1\},\{c_2\},\{u_3\}). \tag{2.9}
   \]

Every two-vertex set displayed in (2.6)--(2.9) meets two parts and is
connected.  In (2.8) and (2.9), each vertex of the second two-vertex branch
set has a neighbour in the first two-vertex branch set.  A later singleton
is in a part different from at least one
vertex of each earlier two-vertex set, and the singleton tails occur in
distinct parts.  Thus every vertex of every later branch set has a
neighbour in every earlier branch set, exactly as required by the
definition of a dominating model.  In each tuple the last three singleton
vertices form a triangle.  The four pair orbits are exhaustive, proving
item 3.  Item 4 is immediate.  \(\square\)

## 3. Exact scope

Theorem 2.1 refutes both of the following proof mechanisms:

- intersect the planarizing pairs obtained one bridge at a time; and
- use strong contraction-criticality only through the bare regeneration of
  a normalized dominating `K_5` model after deleting every pair.

The graph `M` already has the latter regeneration property, but it is only
four-colourable and only six-connected.  It therefore does not refute an
exchange using actual proper-minor colour responses or seven-connectivity.

Indeed, let \(S=A\cup C\cup D\), the six vertices outside `U`.  If a
supergraph `G` containing this labelled `M` has no `K_7` minor, the three
vertices of `U` must remain in distinct components of `G-S`.  Otherwise a
path in `G-S` between two consecutive visits to `U`, internally outside
`M`, contracts to a missing edge inside `U`; (2.4) then lifts to a `K_7`
model in `G`.  Thus `S` remains an actual order-six separator.  In
particular no seven-connected `K_7`-minor-free host contains `M`, as proved
abstractly by Corollary 6.2 of the adjacent result.

The reusable remaining question is therefore label-sensitive: show that a
saturated family of quadrant-confined bridges either produces this
multipartite configuration, and hence its forbidden six-separator, or
produces a missing-pair augmentation or an exact response-bearing
seven-separator directly.
