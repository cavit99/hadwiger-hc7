# Disjoint ordered replacement paths do not by themselves give `K_7`

**Status:** hand-checkable counterexample to a proposed intermediate
decoder.  It is not a counterexample to `HC_7` or to the balanced
order-eight completion theorem.

## 1. Construction

Let

\[
 A=\{a,b,r_3,r_4,r_5\},\qquad
 B=\{c,d,t_0,t_1,t_2\}
\]

be disjoint five-cliques.  Add the eight cross-edges

\[
 \{a,b\}\text{ complete to }\{t_1,t_2\},\qquad
 \{c,d\}\text{ complete to }\{r_4,r_5\},             \tag{1.1}
\]

and no other cross-edge.  Call the resulting graph `G`.  Put

\[
                         e=ab,\qquad f=cd,
 \qquad                   H=G-\{e,f\}.
\]

The graph `H` has the proper six-colouring

\[
\begin{array}{c|c}
0&a,b,t_0\\
1&t_1\\
2&t_2\\
3&c,d,r_3\\
4&r_4\\
5&r_5.
\end{array}                                             \tag{1.2}
\]

The natural cyclic supports of the two deleted clique edges are the
disjoint sets

\[
                         \Omega_e=\{0,1,2\},\qquad
                         \Omega_f=\{3,4,5\}.            \tag{1.3}
\]

Both cyclic orientations are locked for both edges.  Explicit directed
paths are

\[
\begin{array}{ll}
 a-t_1-t_2-b &(0,1,2,0),\\
 a-t_2-t_1-b &(0,2,1,0),\\
 c-r_4-r_5-d &(3,4,5,3),\\
 c-r_5-r_4-d &(3,5,4,3).
\end{array}                                             \tag{1.4}
\]

Every path from the first pair is vertex-disjoint from every path from the
second pair.  Each path avoids the other three vertices of its own
five-clique and preserves the named ends of the deleted edge.

## 2. `K_7`-minor exclusion

The following five bags, joined in the displayed path order, form a tree
decomposition of `G`:

\[
\begin{aligned}
X_1&=\{c,d,t_0,t_1,t_2\},\\
X_2&=\{c,d,r_4,r_5,t_1,t_2\},\\
X_3&=\{b,r_4,r_5,t_1,t_2\},\\
X_4&=\{a,b,r_4,r_5,t_1,t_2\},\\
X_5&=\{a,b,r_3,r_4,r_5\}.
\end{aligned}                                           \tag{2.1}
\]

More precisely, the decomposition tree has edges

\[
                         X_1X_2X_3X_4X_5.
\]

Every graph edge is contained in one displayed bag, and the bags
containing any fixed vertex form a subpath.  The maximum bag order is six,
so `G` has treewidth at most five.  Since `K_7` has treewidth six and
treewidth is minor-monotone, `G` has no `K_7` minor.

## 3. Exact scope

This example refutes the static implication

> two vertex-disjoint five-cliques plus an `(equal,equal)` colouring with
> disjoint natural three-colour supports and both ordered replacement paths
> for both deleted clique edges imply a `K_7` minor.

The graph has low connectivity, is six-colourable after suitable
recolouring, and has neither the literal balanced order-eight boundary nor
the proper-minor response incompatibility of a hypothetical `HC_7`
counterexample.  Thus it does not refute the coupled colouring theorem or
any host-level completion using those additional hypotheses.  It shows
that disjointness of the ordered paths is not itself the missing
label-preserving decoder.
