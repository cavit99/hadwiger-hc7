# Local planar pieces do not imply a coherent planar union

## Status

This is a sharp one-connectivity-unit-short barrier for P5 of the proof
spine.  It shows that even `K_7`-minor exclusion and a *fixed* deletion
pair which planarizes every selected local page do not imply that the
union of those pages is planar.  An interface/rotation compatibility
theorem is indispensable.

The example is not a counterexample to `HC_7`: it is only six-connected
and is 3-colourable.

## 1. Construction

Let

\[
                 G=K_{3,3,3}
\]

with independent parts `A,B,C`, each of order three.  For each pair of
parts, let

\[
                 G_{AB}=G[A\cup B],\quad
                 G_{BC}=G[B\cup C],\quad
                 G_{CA}=G[C\cup A].                         \tag{1.1}
\]

Each page is a copy of `K_{3,3}`.

### Proposition 1.1 (coherence barrier)

The graph `G` has the following properties.

1. `G` is six-connected and `K_7`-minor-free.
2. No deletion of two vertices makes `G` planar.
3. Nevertheless, for any `a in A` and `b in B`, every one of the three
   pages in (1.1) becomes planar after deleting the same fixed pair
   `{a,b}`.

Thus local planarity, even with a common named deletion pair, does not
glue without control of all cross-page edges and boundary rotations.

#### Proof

The connectivity of a complete multipartite graph is its order minus
the largest part, so `kappa(G)=9-3=6`.

Suppose a `K_7` model existed.  Seven nonempty branch sets on nine
vertices leave at most two vertices beyond one per bag, so at least five
branch sets are singletons.  But two singleton branch sets in the same
part are nonadjacent.  Hence at most one singleton bag can lie in each of
the three parts, for a total of at most three, a contradiction.  Thus
`G` is `K_7`-minor-free.

After deleting any two vertices, the three residual part sizes are,
up to order,

\[
                            (1,3,3)\quad\hbox{or}\quad(2,2,3). \tag{1.2}
\]

In the first case the two order-three parts induce `K_{3,3}`.  In the
second case the order-three part and any three vertices from the union of
the other two parts give a `K_{3,3}` subgraph.  Thus every two-vertex
deletion remains nonplanar.

Finally, delete fixed `a in A,b in B`.  The three pages become

\[
                    K_{2,2},\qquad K_{2,3},\qquad K_{3,2}, \tag{1.3}
\]

respectively, and all are planar.  This proves the proposition.
\(\square\)

## 2. Exact implication for P5

The example rules out either of the following unqualified inferences:

\[
 \begin{split}
 &\text{every local page is two-apex}\Longrightarrow
       \text{the union is two-apex},\\
 &\text{all local pages use one common apex pair}\Longrightarrow
       \text{the union minus that pair is planar}.
 \end{split}                                               \tag{2.1}
\]

P5 must retain the hypotheses already visible in the audited annular
composition theorem: the pages and annuli must cover **every** edge, the
attachment occurrences must use compatible cyclic orders, and expansions
must be rural in those prescribed rotations.

The construction misses the active target by two exact axioms:

* its connectivity is six rather than seven; and
* `chi(G)=3`, so it has none of the proper-minor state rejection of a
  7-contraction-critical graph.

The first failure is structural rather than cosmetic: each independent
part is exposed by a six-cut consisting of the other two parts.  Those
three crossing six-cuts are precisely why the three planar pages do not
form an annular/rural decomposition of their union.

