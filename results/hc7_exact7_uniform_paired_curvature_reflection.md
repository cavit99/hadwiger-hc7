# Uniform paired-state curvature reflection

**Status:** proved and independently audited.

This theorem removes every gate, Moser, portal-distribution, and order
hypothesis from the three-connected paired-state component.  Its only
geometric input is the audited two-witness common-face lemma.

## 1. Setup

Let `G` be seven-connected, suppose every proper minor of `G` is
six-colourable, and let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\}                     \tag{1.1}
\]

be an actual separation, with both open shores nonempty.  Suppose a legal
proper-minor operation in the closed `L`-shore attains the exact boundary
partition below: a six-colouring of that minor pulls back on the untouched
closed `R`-shore with precisely these equality blocks on `S`:

\[
 \Pi=\bigl\{B_1,B_2,B_3,\{c\}\bigr\},
 \qquad B_i=\{a_i,t_i\},                              \tag{1.2}
\]

where each `B_i` is independent, every two distinct `B_i` have a literal
edge between them, and `c` has a literal neighbour in every `B_i`.

Let `C` be a three-connected `S`-full component of `G[R]`, and let
`Q subseteq R-C` be a connected `S`-full packet.  Thus `Q` is disjoint from
`C`; no edge between them is required.

### Theorem 1.1 (uniform paired-state reflection)

The attained state `Pi` reflects across the rich shore.  Consequently this
configuration cannot occur in a hypothetical minimal counterexample to
`HC_7`.

### Proof

Assume that `Pi` does not reflect.  Then no two distinct duties have
vertex-disjoint connected carriers in `C`.  Indeed, if `T_i,T_j` fund two
duties, assign `Q` to the third duty `B_k` and contract the three pairwise
disjoint connected sets

\[
                     T_i\cup B_i,\qquad
                     T_j\cup B_j,\qquad
                     Q\cup B_k.                         \tag{1.3}
\]

The literal old-block edges make the three representatives pairwise
adjacent, and the named `c-B_r` edges make each representative adjacent to
the retained singleton `c`.  Hence those four vertices form a clique with
one representative for every block of `Pi`.  This is a proper minor, so a
six-colouring pulls back to the untouched closed `L`-shore with exact
boundary partition `Pi`.  It aligns with the colouring that attained `Pi`
on the opposite shore, and the two colourings glue.  Thus two such carriers
would reflect `Pi`, as claimed.

We use the following portal-matching observation repeatedly.  If

\[
 D\subseteq S-\{c\},\qquad |D|\le |C|,                 \tag{1.4}
\]

then the incidence graph between the literal labels in `D` and their
neighbours in `C` has a matching saturating `D`.  Otherwise Hall supplies a
nonempty `U subseteq D` with

\[
                         |N_C(U)|<|U|.
\]

The inequality `|N_C(U)|<=|U|-1<=|D|-1<=|C|-1` makes
`C-N_C(U)` nonempty.  Deleting

\[
                         (S-U)\cup N_C(U)               \tag{1.5}
\]

uses at most six vertices.  A component of `C-N_C(U)` cannot reach a
surviving member of `U`, every other boundary exit was deleted, and
componenthood of `C` excludes every exit outside `S`.  The nonempty old
opposite shore survives, contradicting seven-connectivity.  This proves the
observation.

Call duty `i` **witnessed** when there are distinct nonadjacent portals

\[
                  p\in N_C(a_i),\qquad q\in N_C(t_i).  \tag{1.6}
\]

If it is not witnessed, every distinct pair from these two portal sets is
an edge.  A three-connected graph has at least four vertices.  For any two
unwitnessed duties, apply (1.4)--(1.5) to their four literal labels.  The
four distinct matched portals form two vertex-disjoint literal edges, one
funding each duty.  Together with `Q` they reflect `Pi`, contrary to the
assumption.  Therefore at least two duties are witnessed.

Apply the audited two-witness common-face lemma from
`../results/hc7_exact7_single_missing_curvature_exchange.md`.  It makes
`C` planar and places **every** portal in `C` of the six non-`c` boundary
labels on one facial cycle `F` in the unique plane embedding of `C`.  A
nonadjacent witness pair lies on `F`, so

\[
                              |F|\ge4.                  \tag{1.7}
\]

We first exclude the two small possible orders.  If `|C|=4`, then `F`
contains every vertex of `C`.  Thus `C` is outerplanar and
`|E(C)|<=2|C|-3=5`, whereas three-connectivity gives
`delta(C)>=3` and hence `|E(C)|>=6`, a contradiction.

If `|C|=5`, then `|F|` is four or five.  In the latter case `C` is
outerplanar, so `|E(C)|<=7`, while `delta(C)>=3` gives
`|E(C)|>=8`.  In the former case let `w` be the unique vertex outside
`F`.  Every neighbour in `C` of a member of `S-\{c\}` lies on `F`, so `w`
has no such boundary neighbour.  It has at most four neighbours in `C`, at
most the one boundary neighbour `c`, and no neighbour outside `C union S`.
Thus `d_G(w)<=5`, contrary to seven-connectivity.  We have proved

\[
                              |C|\ge6.                  \tag{1.8}
\]

Apply the portal-matching observation to all six labels in `S-\{c\}` and
write the resulting pairwise distinct representatives as

\[
 p_i\in N_C(a_i),\qquad q_i\in N_C(t_i)\qquad(i=1,2,3). \tag{1.9}
\]

All six lie on `F`.  The representatives of every two duties alternate on
`F`.  If two pairs did not alternate, two complementary facial subpaths
joining their respective endpoints would be vertex-disjoint connected
carriers for those duties, again reflecting `Pi` with `Q`.  Therefore the
cyclic duty word of the six representatives is, up to rotation, reflection,
and renaming,

\[
                              A\ B\ D\ A\ B\ D.          \tag{1.10}
\]

Relabel the six complete portal sets in this cyclic order.  The audited
facial portal-incidence theorem gives the upper bound

\[
                         \sum_{v\in V(F)}\lambda(v)
                              \le |F|+6,                 \tag{1.11}
\]

because no two duties have disjoint facial carriers.  Its planar-curvature
theorem applies to this same component and face.  Seven-connectivity gives
`delta(G)>=7`, so it gives the incompatible lower bound

\[
                         \sum_{v\in V(F)}\lambda(v)
                              \ge 2|F|+6.                \tag{1.12}
\]

This contradiction proves that `Pi` reflects.  The two closed-shore
colourings then glue after a palette permutation, yielding a proper
six-colouring of `G`.  \(\square\)

## 2. Exact scope

The theorem handles every possible order of `C`, arbitrary portal
multiplicities, shared portal vertices, internal gates, web strips, and
boundary graphs once the exact paired state has legally been attained.  It
does not cover a connected rich shore whose two full packets lie inside one
component rather than in `C` and `R-C`, an arbitrary demand-three equality
state, or packet vector `(1,1)`.
