# A common portal does not colour an intact connected shore

**Status:** explicit counterexample to an intermediate claim; deterministic
finite verification; separate internal audit GREEN in
[`hc7_order8_connected_shore_common_portal_barrier_audit.md`](hc7_order8_connected_shore_common_portal_barrier_audit.md).
This is not a counterexample to `HC_7`.

## Refuted statement

The following proposed extension of the exact three-component contraction
is false:

> Let `S` have order eight, let `d,e` be nonadjacent, and let
> `S-{d,e}=P dotcup R`, where `P,R` are nonempty independent sets.  Assume
> there is a `P`--`R` edge and each of `d,e` has a neighbour in both
> classes.  If one connected open shore contains two disjoint connected
> subgraphs adjacent to every vertex of `S`, and one of those subgraphs has
> one common portal for `d,e`, then that intact closed shore has a proper
> six-colouring inducing
> `P | R | {d} | {e}` on `S`.

The failure persists when the closed shore is `K_7`-minor-free, exactly
six-chromatic, and every one of its minors is six-colourable.  It pinpoints
why the componentwise restriction in the three-component completion
theorem cannot be reused inside one connected shore.

## Construction

Put

\[
 S=\{d,e,p_1,p_2,p_3,r_1,r_2,r_3\},\qquad
 P=\{p_1,p_2,p_3\},\quad R=\{r_1,r_2,r_3\}.
\]

Let `G[S]` consist of the two disjoint triangles

\[
                 d p_1 r_1 d,\qquad e p_2 r_2 e,
\]

with `p_3,r_3` isolated in `G[S]`.  Thus `P,R` are independent, `de` is
absent, and both roots have a neighbour in both bipartition classes.

Let the open shore `H` be a triangle on vertices `a,b,c`, with every one of
`a,b,c` adjacent to every vertex of `S`.  Take

\[
                         Q_0=\{a\},\qquad Q_1=\{b\}.
\]

These are disjoint connected `S`-full subgraphs.  Within `Q_1`, the two
root portal sets are the same singleton:

\[
 N(d)\cap Q_1=N(e)\cap Q_1=\{b\}.
\]

## Exact colouring responses

Under the equality partition

\[
                         P\mid R\mid\{d,e\},
\]

the boundary uses three distinct colours.  Give `a,b,c` the other three
colours.  This is a proper six-colouring of the closed shore.

Under

\[
                         P\mid R\mid\{d\}\mid\{e\},
\]

the four displayed blocks use four distinct colours: a `P`--`R` edge
separates the first two, and each root is adjacent to both classes.  Every
vertex of `H` is adjacent to every boundary vertex, so only two colours
remain for the triangle `H`.  No such six-colouring exists.  Hence this
closed shore has the equality response only.

## Minor and chromatic bounds

The closed shore is the join of `K_3` with

\[
                         2K_3\mathbin{\dot\cup}2K_1.
\]

The boundary has treewidth two.  Adding the three vertices of `H` to every
bag of a width-two tree decomposition gives a width-five tree decomposition
of the closed shore.  Treewidth is minor-monotone, and every graph of
treewidth at most five is six-colourable.  Hence every minor of the closed
shore is six-colourable, and in particular it has no `K_7` minor.  The
displayed equality colouring and the clique formed by `H` together with
either boundary triangle show that its chromatic number is exactly six.

Equivalently, the minor exclusion can be seen directly.  At most three
branch sets of a hypothetical `K_7` model meet `H`; the other four would
form a `K_4` minor in `G[S]`, although every connected component of
`G[S]` has order at most three.

## Why the three-component proof does not extend

The common-portal contraction contracts the edge `bd`.  It can be
restricted to a different component, because that component is untouched.
It cannot be expanded to colour the intact connected shore: the vertex
`b` has been consumed by the contraction, and the remaining vertex `c`
is precisely the third mutually adjacent boundary-full vertex that makes
the unequal boundary partition nonextendable.

Thus a theorem for the connected-shore interface must use additional
host-level information--for example an operation preserving the whole
shore, a strict labelled descent, or contraction-critical responses at
edges outside the two selected full subgraphs.  A common portal alone is
not enough.

## Scope

The example is not seven-connected and is not seven-chromatic or
contraction-critical.  Although all of its proper minors are
six-colourable, the graph itself is already six-colourable.  It does not
refute the active `HC_7` target, which is allowed to use the missing host
hypotheses.  It refutes only the direct attempt to replace the two separate
components in the completion theorem by two disjoint full subgraphs of one
connected shore.

The verifier is
[`hc7_order8_connected_shore_common_portal_barrier_verify.py`](hc7_order8_connected_shore_common_portal_barrier_verify.py).
