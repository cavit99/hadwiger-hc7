# Barrier: a seven-connected minor-free shore has no reserved full connector

## Verdict

The following local principle is false, even when the open shore itself is
seven-connected, has minimum degree seven, and is `K_7`-minor-free:

> complementary four-corner carriers in a connected `S`-full shore always
> leave a disjoint connected `S`-full connector, or expose an internal
> separation of order at most six.

The obstruction is not a thin tree or a low-cut web.  It is a highly
connected shore with **essential labelled portals**.  Consequently the
sole-exterior Moser argument must spend an actual contraction-critical state
transition, a global `K_7`-free interaction with the boundary, or a more
specific carrier-minimality hypothesis.  Shore connectivity and the
four-corner linkage/disk dichotomy alone cannot reserve the connector.

## Construction

Let `P` be the icosahedral graph and let

\[
                         C=K_2\vee P,
\]

the join of `P` with two adjacent universal vertices `a,b`.  Choose seven
distinct vertices

\[
                       p_0,p_1,\ldots,p_6\in V(P).
\]

Take a literal boundary `S={0,1,...,6}`.  The only boundary--shore edge
incident with label `s` is

\[
                              s p_s.                     \tag{1}
\]

Thus `C` is `S`-full, but every label has one essential portal.

For the pure-Moser corner sets `L={1,2}`, `R={3,4}`, both complementary
matchings have explicit adjacent disjoint carriers.  For example,

\[
\begin{array}{c|c|c}
\text{matching}&X&Y\\ \hline
13\mid24& C[\{p_1,a,p_3\}]&C[\{p_2,b,p_4\}]\\
14\mid23& C[\{p_1,a,p_4\}]&C[\{p_2,b,p_3\}].
\end{array}                                               \tag{2}
\]

Each row consists of two disjoint connected subgraphs, and `ab` makes them
adjacent.

## No reserved full connector

More strongly, let `X,Y` be **any** disjoint carriers for either matching.
If `X` contacts a literal label `s`, (1) forces `p_s in X`; the same holds
for `Y`.  Since the two matching blocks partition `{1,2,3,4}`, necessarily

\[
                 \{p_1,p_2,p_3,p_4\}\subseteq X\cup Y.   \tag{3}
\]

Every `S`-full subgraph of `C` must contain all seven essential portals,
in particular the four vertices in (3).  Hence no subgraph disjoint from
`X\cup Y` is `S`-full.  This applies to every possible rerouting of the
carriers, not only to the witnesses in (2).

## No low internal adhesion

The icosahedral graph is five-connected.  Delete at most six vertices from
`C`.  If at least one of `a,b` remains, it joins all remaining vertices.  If
both are deleted, at most four vertices were deleted from `P`, whose
remainder is connected.  Thus

\[
                              \kappa(C)\ge7.              \tag{4}
\]

In fact equality holds, but only the lower bound is needed.  There is no
proper internal vertex separation of order at most six from which a
bounded-adhesion state splice could be read.

Every old vertex has degree `5+2=7` in `C`; the two join vertices have still
larger degree.  Thus

\[
                              \delta(C)=7.                \tag{5}
\]

Finally `C` itself is `K_7`-minor-free.  In general

\[
                         \eta(K_r\vee H)=r+\eta(H).       \tag{6}
\]

The lower bound is immediate.  For the upper bound, at most `r` branch sets
of a clique model can contain the `K_r` vertices; deleting those branch sets
leaves a clique model of the remaining order wholly in `H`.  Since `P` is
planar, `eta(P)<=4`, and therefore `eta(C)<=6`.

## Exact trust boundary

This is a counterexample to a **shore-local** reserved-connector-or-small-
adhesion lemma.  The augmented graph obtained by attaching the Moser
boundary and `v` has not been asserted to be seven-contraction-critical, or
even globally seven-connected: the unique boundary portals deliberately
leave some literal boundary vertices with too small a total degree.

That limitation is informative.  To evade the example, a valid sole-
exterior theorem must use at least one of the following in a way that is not
visible in the local four-port outcome:

1. the exact proper-minor equality-state witnesses at the boundary;
2. global seven-connectivity/minimum degree applied to the **literal
   boundary vertices**, not merely to the shore;
3. a global `K_7`-minor argument involving `v` and the Moser boundary; or
4. an extremal choice of carriers which proves redundancy of an essential
   portal before asking for a reserved connector.

In particular, increasing internal connectivity or invoking a generic web
dichotomy does not solve the palette-to-labelled-carrier gap.

