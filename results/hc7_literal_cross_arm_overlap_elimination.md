# Literal-support elimination in the rigid cross-arm outcome

**Status:** proved and independently cold-audited.

This is a graph-specific composition consequence of the corrected
private-pair cross-arm dichotomy.  It eliminates every rigid common-core
outcome in which a literal avoided `K_5` meets the common core, regardless
of whether the two arms have order five or six.

## Theorem 1 (literal avoided support is disjoint from the common core)

Let `G` be seven-connected and `K_7`-minor-free.  Suppose the rigid outcome
of the corrected cross-arm theorem consists of

\[
 A,\qquad B=X\cup\{p\},\qquad C=X\cup\{q\},           \tag{1.1}
\]

where `|A|=5`, `p,q notin A union X`, and `A,B,C` support `K_5`
models on at most six vertices.  Suppose moreover that for every
`a in A cap X` the two forced replacement supports

\[
                  (A-\{a\})\cup\{p\},\qquad
                  (A-\{a\})\cup\{q\}                 \tag{1.2}
\]

occur.  Then

\[
                              A\cap X=\varnothing.     \tag{1.3}
\]

### Proof

Assume that `a in A cap X` and put `U=A-{a}`.  A `K_5` model supported
on five vertices is a literal `K_5`.  Hence `A`, `U union {p}`, and
`U union {q}` are cliques.  In particular, each of the three vertices
`a,p,q` is complete to the four-clique `U`.

Deleting four vertices from a seven-connected graph leaves a
three-connected graph.  Thus `G-U` is three-connected.  Any three vertices
of a three-connected graph lie on a common cycle, so there is a cycle `D`
in `G-U` containing `a,p,q`.

For completeness, the cited three-vertex cycle fact follows directly from
the fan lemma.  Start with a cycle through two of the vertices.  If the
third is not already on it, a three-fan from the third vertex has three
distinct ends on the cycle.  Of the three cyclic intervals between those
ends, one has open interior containing neither of the first two vertices.
The complementary closed arc contains both (including either one that is
a fan end); together with the two corresponding fan paths, it is a cycle
through all three.

Partition `D` at `a,p,q` into three nonempty, pairwise disjoint connected
bags, rooted respectively at `a,p,q`.  Consecutive bags meet across the
three cut edges of `D`, so the three bags are pairwise adjacent.  Each bag
is adjacent, through its root, to every singleton vertex of `U`.  The
three cycle bags together with the four singleton bags of the clique `U`
therefore form a `K_7` model, a contradiction.  Hence (1.3) holds.
\(\square\)

## Corollary 2 (remaining rigid literal cell)

In the rigid outcome of the corrected cross-arm theorem, an avoided
support of order five is disjoint from the common arm core.  Thus every
positive-overlap rigid outcome has all avoided supports of order six.

## Trust boundary

The theorem uses only the forced replacement supports, seven-connectivity,
and the fact that an order-five support is a literal clique.  It says
nothing about split-row adjacencies inside order-six supports.  It does
not close the disjoint-core case or a rigid outcome in which every avoided
support has order six.  Those remain the exact cross-arm composition gap.
