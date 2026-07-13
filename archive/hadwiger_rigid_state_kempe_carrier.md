# Rigid repeated states force a labelled Kempe carrier

## 1. Purpose

The full literal edge-carrier cell is closed by
`hadwiger_flat_full_host_matching_dichotomy.md`.  For an unbounded retained
carrier, the missing input is a connected two-shore state representation.
This note extracts the first such connected object directly from the two
incompatible repeated boundary states, without assuming that the carrier
is an edge or enumerating its portals.

## 2. Boundary swap

Let `D` be a retained connected carrier.  Its six singleton boundary
labels include `A,B,C`, with `AB,AC` the only possible missing pairs, and
the other singleton colours are fixed and pairwise distinct.

Suppose the `AB` state extends.  Fix such a colouring and write

\[
       c(A)=c(B)=\alpha,\qquad c(C)=\beta.          \tag{2.1}
\]

Let `K` range over the connected components of the bichromatic graph

\[
                    D[c^{-1}(\{\alpha,\beta\})].   \tag{2.2}
\]

Define three sets of carrier vertices:

\[
\begin{aligned}
 T_A&=N_D(A)\cap c^{-1}(\beta),\\
 S_C&=N_D(C)\cap c^{-1}(\alpha),\\
 S_B&=N_D(B)\cap c^{-1}(\beta).
\end{aligned}                                      \tag{2.3}
\]

The notation records the componentwise swap constraints.  A component
meeting `S_C union S_B` must be swapped when the boundary is changed from
`AB` to `AC`; a component meeting `T_A` cannot be swapped.

### Theorem 2.1 (rigid-state Kempe carrier)

If the `AC` boundary state does not extend to `D`, then some connected
`alpha/beta` component `K` satisfies

\[
             K\cap T_A\ne\varnothing,
       \qquad K\cap(S_C\cup S_B)\ne\varnothing.    \tag{2.4}
\]

Equivalently, `K` contains an `A`-portal of colour `beta` and also either
a `C`-portal of colour `alpha` or a `B`-portal of colour `beta`.

#### Proof

Change the desired boundary assignment to

\[
       c'(A)=c'(C)=\alpha,\qquad c'(B)=\beta,       \tag{2.5}
\]

and leave all other singleton colours fixed.  On each component `K` of
(2.2), independently decide whether to interchange `alpha,beta`.

If `K` is not swapped, its old `alpha` vertices remain legal at `A`, and
its old `beta` vertices remain legal at `C`.  The only new failures are

* an old `alpha` vertex adjacent to `C`, namely a member of `S_C`; or
* an old `beta` vertex adjacent to `B`, namely a member of `S_B`.

Thus a component meeting `S_C union S_B` must be swapped.

If `K` is swapped, every old `alpha` vertex receives `beta`; it was already
nonadjacent to `B` because `B` had colour `alpha` in (2.1).  Every old
`beta` vertex receives `alpha`; it was already nonadjacent to `C`, but it
may be adjacent to `A`.  Hence the only obstruction to swapping is a
member of `T_A`.

If no component met both constraint sets, swap precisely the components
which meet `S_C union S_B`.  The preceding checks show that all edges to
`A,B,C` are proper.  Edges to every other singleton remain proper because
their colours were not changed, and a Kempe interchange preserves all
edges inside `D`.  This constructs an extension of (2.5), contrary to the
hypothesis.  Therefore (2.4) holds. \(\square\)

### Corollary 2.2 (minimal labelled alternating path)

Under Theorem 2.1, `K` contains a minimal path `P` whose first end is an
`A`-portal of colour `beta` and whose second end is either a `C`-portal of
colour `alpha` or a `B`-portal of colour `beta`.  The colours alternate
along `P`; every internal vertex is dispensable for the two named endpoint
roles.

This is a literal connected state carrier.  Its endpoint roles, rather
than the equality word alone, are the labels that must be transported
through a carrier adhesion.

## 3. Symmetric type

Suppose instead that the `AC` state extends and the `AB` state does not.
Fix

\[
       c(A)=c(C)=\alpha,\qquad c(B)=\beta.          \tag{3.1}
\]

Then some `alpha/beta` component contains both

\[
 N_D(A)\cap c^{-1}(\beta)                           \tag{3.2}
\]

and at least one of

\[
 N_D(B)\cap c^{-1}(\alpha),qquad
 N_D(C)\cap c^{-1}(\beta).                         \tag{3.3}
\]

The proof is Theorem 2.1 with `B,C` interchanged.

## 4. Failed-state list core

The failed state also has a second, complementary certificate which does
not depend on a chosen successful colouring.

### Theorem 4.1 (list-critical portal-load core)

Let `k` colours be available, and precolour the singleton boundary in a
state using exactly `k-1` colours.  For `v in D`, let

\[
 L(v)=[k]-c(N(v)\cap\partial D),                    \tag{4.1}
\]

where only distinct boundary colours are counted.  If this boundary state
does not extend through `D`, then `D` contains a connected induced
subgraph `J` which is not colourable from the restricted lists and such
that every `v in J` satisfies

\[
              d_J(v)\ge |L(v)|,
       \qquad d_J(v)+r(v)\ge k,                    \tag{4.2}
\]

where `r(v)` is the number of distinct boundary colours seen by `v`.
The unique colour absent from the boundary belongs to every `L(v)`.

#### Proof

Choose an inclusion-minimal induced subgraph `J` which is not
`L`-colourable.  It is connected, since otherwise one uncolourable
component would be smaller.  For any `v`, colour `J-v` from the lists.
If `d_J(v)<|L(v)|`, fewer than `|L(v)|` colours occur on its neighbours,
so one colour of `L(v)` remains available and extends the colouring to
`v`, a contradiction.  Thus `d_J(v)>=|L(v)|`.  Since
`|L(v)|=k-r(v)`, (4.2) follows.  The boundary-unused colour is excluded by
no boundary neighbour and hence lies in every list. \(\square\)

For `HC_7`, `k=6`.  Thus every vertex of the failed-state core satisfies

\[
                         d_J(v)+r(v)\ge6.           \tag{4.3}
\]

The literal edge carrier is the extremal low-internal-degree case: a
degree-one vertex in `J` must see all five used boundary colours.  More
generally, low-degree leaves of a path or torso come with correspondingly
high portal load, while a low-portal vertex is forced into the internally
branching part of `J`.  This converts state incompatibility into a uniform
capacity inequality suitable for the gate/cycle/3-connected Helly torso;
it is strictly stronger than recording the equality word.

## 5. Exact next split lemma

For a literal edge carrier, the minimal path in Corollary 2.2 is the
operated edge and its two endpoints give the `p/q` state shores used in
the matching dichotomy.  For an unbounded carrier, the path may have many
vertices and the two colour classes need not be connected.  The next
uniform rooted-model statement can now be phrased without Moser labels:

> **Kempe-carrier two-shore lemma.**  In a `Q`-indecomposable carrier,
> a minimal labelled alternating path forced by Theorem 2.1 either expands
> to two adjacent connected state shores with the required boundary rows,
> or one of its bridges gives a colour-gluable adhesion or one coherent
> rural rotation.

If the first outcome occurs for all carriers, Theorem 3.1 of
`hadwiger_flat_full_host_matching_dichotomy.md` closes every incompatible
transport state at once.  Thus the remaining Gate A is no longer “find
some portal split”: it is bridge stabilization around the specific
alternating path (2.4), whose endpoint roles are forced by incompatible
proper-minor colour states.
