# Five-attachment carrier peels

**Status:** proved and independently audited, including the corrected
outside-core Theorem 3.3.  That theorem eliminates raw rank-one locking for
a two-connected singleton-trace carrier with one connected `w`-attached
region; it does not combine attachments split among several components.
The results do not close a carrier of low internal connectivity or the
residual pair-trace portal-distribution lock described in Section 5.

## 1. Labelled carrier setting

Let `K,A,B` be three pairwise disjoint, connected, pairwise adjacent
branch sets in one closed terminal shore.  Their intersections with the
literal adhesion are fixed independent traces.  Assume that `K` has one
of the following two traces:

\[
       K\cap T=\{r\},
       \qquad\hbox{or}\qquad
       K\cap T=\{x,y\}.                              \tag{1.1}
\]

In the second case `xy` is a missing edge.  In both cases every other
vertex of `K` is an open-shore vertex.  Assume also that the literal trace
of `K` has an edge to the trace of each of `A` and `B`.  This condition is
automatic for each of the three blocks of a supported Moser frame: the
present complementary five-cycle supplies an edge from each frame trace to
each of the other two traces.  A peel toward `A` uses only the retained
trace edge to `B`; the symmetric condition permits either target.

Let `L` be connected and disjoint from `K\cup A\cup B`, and put

\[
                         P=N(L)\cap K.               \tag{1.2}
\]

The application has `|P|>=5` and `W={w}\cup L`.  Only `|P|>=2` is needed
below.

A **labelled peel of `K` toward `A`** is a partition

\[
                         V(K)=X\mathbin{\dot\cup}Y   \tag{1.3}
\]

such that

* `K[X]` and `K[Y]` are connected;
* the whole trace of `K` lies in `Y`;
* `X` has an edge to `A`;
* both `X` and `Y` meet `P`.

If (1.3) exists, replace

\[
                         A\longmapsto A\cup X,
                         \qquad K\longmapsto Y.      \tag{1.4}
\]

The two new blocks are connected and adjacent: an edge between `X` and
`Y` exists because `K` is connected.  The block `A\cup X` remains adjacent
to `B` through the old `A-B` edge, while `Y` remains adjacent to `B`
through the retained literal trace.  No adhesion vertex changes block.
Finally `L`, and hence `W`, is adjacent to both new named blocks through
the two nonempty parts of `P`.  Thus (1.4) is exactly a label-preserving
promotion from raw contact rank one to raw contact rank at least two.

The promotion is geometric.  If the two enlarged traces are also
independent from `w`, it is an admissible rank promotion; otherwise it
converts the five-attachment lock into the already isolated literal
boundary-incompatibility certificate.

## 2. A marked bipolar split

### Lemma 2.1 (two-root connected partition)

Let `J` be a two-connected graph, let `s,t` be distinct vertices, and let
`P_0\subseteq V(J)` have at least two vertices.  There is a partition

\[
                         V(J)=X\mathbin{\dot\cup}Y
\]

such that `J[X]` and `J[Y]` are connected, `s\in X`, `t\in Y`, and both
`X,Y` meet `P_0`.

#### Proof

Add the edge `st` if it is absent.  A standard bipolar ordering of the
resulting two-connected graph gives

\[
                         v_1=s,v_2,\ldots,v_n=t
\]

in which every internal vertex has both an earlier and a later neighbour.
Consequently every proper initial segment and every proper terminal
segment is connected.  The added edge `st` is not used to establish either
of these two assertions: `t` is absent from a proper initial segment and
`s` is absent from a proper terminal segment.

Let `i_-` and `i_+` be the least and greatest positions occupied by
`P_0`.  Since `|P_0|>=2`, `i_-<i_+`.  Choose any
`i_-<=i<i_+` and take

\[
             X=\{v_1,\ldots,v_i\},\qquad
             Y=\{v_{i+1},\ldots,v_n\}.
\]

These are the required two connected parts. \(\square\)

## 3. Singleton-trace peel

### Theorem 3.1 (two-connected singleton carrier peel)

Suppose `K\cap T={r}`, `K` is two-connected, and some

\[
                   q\in V(K)-\{r\}                 \tag{3.1}
\]

has an edge to `A`.  If `|P|>=2`, then `K` has a labelled peel toward
`A`.

#### Proof

Apply Lemma 2.1 to `J=K`, with `s=q`, `t=r`, and marked set `P`.  It gives
connected parts `X,Y` with `q\in X`, `r\in Y`, and both meeting `P`.
The edge from `q` to `A` supplies the remaining condition in the definition
of a labelled peel.  Apply (1.4). \(\square\)

### Corollary 3.2 (exact residual singleton gate)

If a two-connected singleton-trace carrier with `|P|>=2` admits no
labelled peel toward either other core block, then every edge from
`K-\{r\}` to `A\cup B` is absent.  Equivalently, all direct adjacencies
from `K` to the other two named blocks are gated at its literal root `r`.

This is substantially sharper than a generic five-attachment lock: any
surviving two-connected singleton carrier is a literal one-vertex
cross-block gate.  Seven-connectivity must therefore be supplied by
bridges outside the three chosen blocks, and those bridges---not the five
attachments themselves---are the next exchange objects.

In the actual exact-order-six cell, those bridges can be used immediately.

### Theorem 3.3 (seven-connected singleton lock promotion)

Work in the exact terminal-shore setting of
`../results/hc7_exact7_moser_order6_decorated_exchange.md`.  Thus the
opposite open shore is anticomplete to the present open shore, `t` is its
side terminal, and `v` has no neighbour in the open shore.  Suppose the
five-attachment block `K` has singleton trace `{r}` and is two-connected.
Assume, as in Section 1, that `P=N(L) cap K` has order at least five, that
`L` is a nonempty connected subgraph of the present open shore, and that
`w` has a neighbour in `L`.  Thus `W={w} union L` is connected.  Then
either a labelled peel exists toward `A` or `B`, or one of those two blocks
can be enlarged through vertices outside the core so that it becomes
adjacent to `L`.  In either case the raw contact rank of `W={w} union L`
is promoted from one to at least two.

#### Proof

If a vertex of `K-{r}` has an edge to `A\cup B`, apply Theorem 3.1 (with
the block at the other end of that edge as target).  Assume therefore that

\[
                       E(K-\{r\},A\cup B)=\varnothing.           \tag{3.2}
\]

Let `X_0` be the component containing `L` of

\[
                 G-(A\cup B\cup\{r,w,t\}).                      \tag{3.3}
\]

This component contains a vertex of `K-{r}`: at most one member of the
at-least-five-element set `P` is `r`.  If `X_0` had no neighbour in
`A\cup B`, then

\[
                             N_G(X_0)\subseteq\{r,w,t\}.          \tag{3.4}
\]

Indeed the traces of `A,B`, together with `r`, are all of `U`; with `w,t`
they are every boundary neighbour of the present open shore.  Hence `X_0`
lies inside that open shore, cannot contain `v`, and has no neighbour in
the opposite shore.  The
nonempty set `X_0` is separated from `v` by the at-most-three vertices in
(3.4), contrary to seven-connectivity.  Hence `X_0` has an edge to one of
`A,B`; call that target block `A_0`.

Choose a shortest `A_0-L` path whose internal vertices lie in `X_0`, and
choose it to first enter `L` at its final vertex.

If this path does not meet `K`, absorb all its vertices except its final
vertex into `A_0`.  The enlarged target remains connected, disjoint from
the core and `L`, and has the same literal trace; its last path edge makes
it adjacent to `L`.  Since `L` was already adjacent to `K`, this is the
claimed raw rank-two promotion.

Otherwise let `q` be its first vertex in `K`.  Then `q in K-{r}`.  The
prefix from `A_0` to `q`, with `q` omitted, is disjoint from all three core
blocks and from `L`: the path first enters `L` only at its final vertex,
while `X_0` was defined after deleting
`A\cup B\cup\{r,w,t\}`.  Absorb that prefix into `A_0`.  This preserves
its connectivity and literal trace and creates a direct edge from the
enlarged target block to `q`.

Now apply Theorem 3.1 to the unchanged two-connected carrier `K`, using
the new non-root portal `q`.  The resulting bipolar split is a labelled
peel. \(\square\)

Theorem 3.3 eliminates raw rank-one locking for the entire two-connected
singleton-trace family with one connected attachment region.  A survivor
with the singleton block locked must therefore expose an actual cutvertex
inside every label-faithful choice of that carrier, split the attachments
among different connected regions, or move into the already isolated
boundary-incompatibility case.  Mere root-gating is not stable under
outside-core bypasses.

## 4. Pair-trace peel

The pair-trace case needs one more unit of internal connectivity.  The
reason is exact: the retained block must still connect both trace roots.

### Theorem 4.1 (three-connected pair carrier peel)

Suppose `K\cap T={x,y}`, `K` is three-connected, and there is a vertex

\[
               q\in P-\{x,y\}                     \tag{4.1}
\]

having an edge to `A`.  If `|P|>=2`, then `K` has a labelled peel toward
`A`.

#### Proof

Use Tutte's nonseparating-path theorem in the following standard form:
in a three-connected graph, for prescribed distinct vertices `x,y,q`,
there is an `x-y` path `Q` avoiding `q` such that `K-V(Q)` is connected.
This is Theorem 1.2.1 in Yingjie Qian, *Non-Separating Paths in Graphs*
(Georgia Tech dissertation, 2022), where it is cited to W. T. Tutte,
*How to draw a graph*, Proc. London Math. Soc. (3) 13 (1963), 743--767.

Contract the connected path `Q` to a vertex `z`, suppressing parallel
edges, and call the resulting graph `\bar K`.  The graph `\bar K` is
two-connected.  Indeed, deleting `z` leaves the connected graph
`K-V(Q)`.  Deleting any other vertex `c` gives a contraction of the
connected graph `K-c`, and hence remains connected.  (If the contraction
has only two vertices, the connected partition used below is immediate.)

Let `\bar P` be the set of images of the vertices of `P`.  The vertex `q`
is a member of `\bar P` outside `z`, because `q\notin V(Q)`.  Since
`|P|>=2`, the image of any other member of `P` is either `z` or another
vertex different from `q`.  Hence

\[
                            |\bar P|>=2.             \tag{4.2}
\]

Apply Lemma 2.1 in `\bar K` with `s=q`, `t=z`, and marked set `\bar P`.
Let `\bar X,\bar Y` be the resulting connected parts.  Lift them by

\[
 X=\bar X,
 \qquad
 Y=(\bar Y-\{z\})\cup V(Q).                         \tag{4.3}
\]

The set `X` is connected.  The set `Y` is connected because every edge to
`z` in the contracted graph lifts to an edge to the connected path `Q`.
It contains both `x,y`.  The marked-set conclusion and (4.2) say that
both parts meet the original set `P`.  Finally `q\in X` has an edge to
`A`.  Thus (4.3) is a labelled peel, and (1.4) performs the required
carrier surgery. \(\square\)

The same proof gives a slightly more general version.  It is enough to
have a non-root portal `q` to `A` and a nonseparating `x-y` path `Q`
avoiding `q` which does **not** contain all of `P`: after contraction the
marked set again has at least two images.  Condition (4.1) guarantees this
automatically for every Tutte path avoiding `q`.

### Corollary 4.2 (exact residual pair lock)

If a three-connected pair-trace carrier with `|P|>=2` admits no labelled
peel toward either other core block, then

\[
 P-\{x,y\}
 \quad\hbox{is anticomplete to}\quad A\cup B.       \tag{4.4}
\]

More generally, for every non-root cross-block portal `q`, every
nonseparating `x-y` path avoiding `q` contains all of `P`; otherwise the
general version of Theorem 4.1 peels the carrier.  This is the precise
one-rail capture obstruction left by the theorem.

Thus five attachments cannot remain diffusely mixed with the other two
named blocks.  In a three-connected pair carrier they must be spatially
separated from every movable cross-block portal, or all lie on every
label-preserving nonseparating trace rail.

## 5. Sharpness and the recursive alternative

The connectivity and portal hypotheses above cannot simply be omitted.
For `m>=2`, take

\[
 K=xp_1p_2\cdots p_my
\]

to be a path, let `A={alpha}`, `B={beta}`, and add the three core edges

\[
                         alpha x,\quad beta y,\quad alpha beta.
\]

Let `L={ell}` with neighbours `p_1,\ldots,p_m,w,t`.  Then `K,A,B` are
connected and pairwise adjacent, `K` has exact pair trace `{x,y}`, and

\[
                         P=\{p_1,\ldots,p_m\}
\]

can be arbitrarily large.  Nevertheless no labelled peel exists: every
connected subgraph of the path containing both `x,y` contains all of
`P`, leaving no attachment for the target block.  This is the elementary
alternating-rail web obstruction, not a shortage of attachments.

The example also displays the correct recursive output.  The literal set

\[
                         Q=N(L)=P\cup\{w,t\}         \tag{5.1}
\]

is the adhesion of the actual separation

\[
              (L\cup Q,\;V(J)-L)                    \tag{5.2}

\]

in the closed shore `J`.  The HC7 five-attachment lock always has this
actual separation, with `Q\subseteq K\cup\{w,t\}`; what Sections 3--4 add
is that large internally well-connected portions of the `K` side cannot
remain locked unless their cross-block portals obey the explicit gate or
capture conditions above.

Connectivity alone cannot eliminate the recursive web alternative.  If
`T` is a five-connected planar triangulated tube with a separating
five-cycle `C`, then `K_2\vee T` is seven-connected and has no `K_7`
minor, while each side of `C` is separated by the exact seven-set
`K_2\cup C`.  Hence the remaining step really must use
contraction-critical state transfer across (5.2), or a labelled bridge
which violates (3.2)/(4.4); a stronger connectivity-only peel statement
would be false.

## 6. Proof-spine consequence

In the exact-order-six Moser cell, a five-attachment lock in a named core
block is eliminated geometrically in either of the following reusable
cases:

1. the block has singleton trace, is two-connected, and the attachment
   region is connected (Theorem 3.3 produces either a direct outside-core
   raw promotion or a movable non-root portal);
2. the block has pair trace, is three-connected, and one of its at least
   five `L`-attachments is also a movable portal to either other named
   block.

Any survivor must therefore expose one of four literal certificates:

* an internal cutvertex/2-cut of the named carrier, or several connected
  attachment regions whose union supplied the five-attachment count;
* complete separation of the five attachment vertices from all movable
  cross-block portals; or
* a pair-trace rail which captures all five attachments for every
  nonseparating path avoiding a chosen movable portal.

These are exactly the hypotheses a subsequent bridge/web exchange has to
contradict.  Mere attachment cardinality is exhausted by the two peel
theorems above.
