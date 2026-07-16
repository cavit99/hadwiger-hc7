# Two-root Kempe reconfiguration: exact transitions and a commuting-square barrier

**Status:** written proof and counterexample; separately internally audited in
[`hc7_two_root_kempe_causal_support_audit.md`](hc7_two_root_kempe_causal_support_audit.md).

This note studies the full Kempe reconfiguration graph suggested by the
two-singleton common-host theorem.  It proves the exact one-step contact
conditions for the transitions

\[
                 A\longrightarrow AB
                 \quad\hbox{and}\quad
                 AB\longrightarrow B,
\]

where `A` means that only the first root is colour-dominating, `B` means
that only the second root is colour-dominating, and `AB` means that both
are colour-dominating.

The main conclusion is negative but structural.  A shortest path from
`A` to `B` need not contain a connected chain of noncommuting Kempe
components.  Independent interchanges can instead span a Boolean cube all
of whose nonterminal vertices have status `AB`.  An explicit family shows
that this phenomenon is compatible with the universal two-root domination
property for every number of colours.  Consequently, a proof in the
`HC_7` setting must use an additional hypothesis such as high connectivity,
minor-criticality, or exclusion of a `K_7` minor; universal root domination
alone does not produce the proposed causal support.

## 1. The reconfiguration graph and its three statuses

Let `J` be a graph and let `a,b` be two new nonadjacent vertices with
specified neighbourhoods in `J`.  Fix a palette of `q` colours.  The
**Kempe reconfiguration graph** `R_q(J)` has as its vertices the proper
`q`-colourings of `J`.  Two colourings are adjacent when one is obtained
from the other by interchanging two colours on one component of the
subgraph induced by those colours.

A root is **colour-dominating** in a colouring if its neighbourhood in
`J` meets every colour class.  Assume throughout Sections 1--4 that

\[
 \tag{U}
 \text{every proper `q`-colouring of `J` makes at least one of `a,b`
 colour-dominating.}
\]

Thus every vertex of `R_q(J)` has exactly one of the following statuses:

* `A`: `a` is colour-dominating and `b` is not;
* `AB`: both roots are colour-dominating;
* `B`: `b` is colour-dominating and `a` is not.

### Lemma 1.1 (shortest-path normal form)

Suppose that some component of `R_q(J)` contains colourings of statuses
`A` and `B`.  Let

\[
                   c_0,c_1,\ldots,c_m
\]

be a path of minimum possible length among all paths in that component
whose first vertex has status `A` and whose last vertex has status `B`.
Then every `c_i` with `0<i<m` has status `AB`.

#### Proof

Condition (U) excludes a fourth status.  If an internal `c_i` had status
`A`, its suffix to `c_m` would be a shorter path from `A` to `B`.  If it
had status `B`, the prefix ending at `c_i` would be a shorter such path.
Therefore every internal vertex has status `AB`.  \(\square\)

The lemma is conditional on the two opposite witnesses lying in one
Kempe component.  The common-host theorem supplies opposite witnesses,
but it does not assert their Kempe equivalence.

## 2. Exact one-step contact data

Let `c'` be obtained from `c` by interchanging colours `alpha,beta` on a
component `K` of `J[c^{-1}({alpha,beta})]`.  For a root `r` and
`delta in {alpha,beta}`, put

\[
 I_r^\delta=N_J(r)\cap V(K)\cap c^{-1}(\delta),\qquad
 O_r^\delta=(N_J(r)-V(K))\cap c^{-1}(\delta).
\]

Write `bar(delta)` for the other member of `{alpha,beta}`.

### Lemma 2.1 (a root which gains domination)

Suppose that `r` is not colour-dominating in `c` and is
colour-dominating in `c'`.  Then `r` misses a unique colour
`gamma in {alpha,beta}` in `c`, and

\[
 \tag{2.1}
 I_r^\gamma=O_r^\gamma=\varnothing,
 \qquad
 I_r^{\bar\gamma}\ne\varnothing,
 \qquad
 O_r^{\bar\gamma}\ne\varnothing.
\]

### Lemma 2.2 (a root which loses domination)

Suppose that `r` is colour-dominating in `c` and is not
colour-dominating in `c'`.  Then `r` loses a unique colour
`lambda in {alpha,beta}`, and

\[
 \tag{2.2}
 I_r^\lambda\ne\varnothing,
 \qquad O_r^\lambda=\varnothing,
 \qquad I_r^{\bar\lambda}=\varnothing,
 \qquad O_r^{\bar\lambda}\ne\varnothing.
\]

### Lemma 2.3 (a root which remains dominating)

The root `r` is colour-dominating both in `c` and in `c'` if and only if
it sees every untouched colour and all four sets of alternatives below
are nonempty:

\[
 \tag{2.3}
 I_r^\alpha\cup O_r^\alpha,\quad
 I_r^\beta\cup O_r^\beta,\quad
 O_r^\alpha\cup I_r^\beta,\quad
 O_r^\beta\cup I_r^\alpha.
\]

#### Proof of Lemmas 2.1--2.3

Only contacts with `alpha` and `beta` can change.  A root which gains
domination therefore missed one of these colours.  It could not have
missed both, since an interchange cannot create a contact with either
colour when neither occurred in the root neighbourhood.  If the missing
colour is `gamma`, creation of `gamma` requires a
`bar(gamma)`-neighbour in `K`, while retention of `bar(gamma)` requires
one outside `K`.  This is exactly (2.1).

For a root to lose `lambda`, every old `lambda`-contact must lie in `K`,
and no old `bar(lambda)`-contact may lie in `K`.  It saw both colours
before the interchange, so it has a `lambda`-contact in `K` and a
`bar(lambda)`-contact outside.  This is (2.2).  The same conditions for
both colours are mutually incompatible, proving uniqueness.

Finally, the first two sets in (2.3) are precisely the two contacts before
the interchange, while the last two are precisely the two contacts after
it.  Untouched colours do not change.  This proves Lemma 2.3.  \(\square\)

Consequently, an `A -> AB` move gives (2.1) for `b` and (2.3) for `a`.
An `AB -> B` move gives (2.2) for `a` and (2.3) for `b`.  Unlike a direct
`A -> B` move, neither one-step transition by itself forces either colour
side of `K` to have neighbours in every untouched colour class: the root
which remains dominating prevents the usual recolouring argument from
producing a colouring violating (U).

## 3. What commutation actually implies

Two Kempe interchanges at a colouring `c` are **strongly commuting** if
they form a literal square in `R_q(J)`: each interchange is legal at `c`,
after either interchange the same vertex set and colour pair still define
the other interchange, and applying them in either order gives the same
colouring.  Thus there are colourings

\[
 \begin{matrix}
 c_{00}&---&c_{10}\\
 |&&|\\
 c_{01}&---&c_{11}
 \end{matrix}
 \tag{3.1}
\]

whose parallel edges are the same two interchanges.

### Proposition 3.1 (commuting squares on a shortest path)

Let `c_0,...,c_m` be the minimum path in Lemma 1.1.  Suppose two
consecutive interchanges on this path strongly commute, and let `d` be
the fourth vertex of their square.  Then `d` has status `AB`.

#### Proof

Write the relevant segment as

\[
                    c_{i-1},c_i,c_{i+1}.
\]

The fourth corner `d` is adjacent to both `c_{i-1}` and `c_{i+1}`.
If `d` had status `A`, the path from `d` through `c_{i+1}` to `c_m`
would be shorter than `m`.  If `d` had status `B`, the path from `c_0`
through `c_{i-1}` to `d` would be shorter than `m`.  Condition (U)
excludes a colouring in which neither root dominates.  Hence `d` has
status `AB`.  \(\square\)

This is the opposite of the proposed shortcut: commutation does **not**
create a colouring in which neither root dominates.  On a shortest path,
the alternate corner is forced into the overlap `AB`.

There is a useful higher-dimensional version.  Suppose `m` interchanges
generate a full commuting `m`-cube: every subset can be applied in any
order, and graph distance from the initial corner is the size of the
subset.  If opposite corners have statuses `A` and `B` and their distance
is minimum among all `A`--`B` pairs, then every other corner has status
`AB`.  Indeed, an `A` corner would have a shorter route to the terminal
`B` corner, a `B` corner a shorter route from the initial `A` corner, and
(U) again excludes a fourth status.

Thus a valid reconfiguration theorem has at least two outcomes:

1. a chain of genuinely dependent, noncommuting interchanges; or
2. a commuting overlap cube whose proper nonterminal corners all have
   status `AB`.

There is no deduction of connected support in `J` in the second outcome.

## 4. A uniform commuting-cube counterexample

The second outcome is real, not merely a logical possibility.

### Proposition 4.1 (universal domination with no direct transition)

For every `q>=2` there are a graph `J_q` and two nonadjacent external
roots `a,b` such that:

1. every proper `q`-colouring of `J_q` makes at least one root
   colour-dominating;
2. `R_q(J_q)` contains colourings of statuses `A` and `B`;
3. no Kempe edge joins a colouring of status `A` to one of status `B`;
4. the distance between the two status sets is two, realized by two
   strongly commuting interchanges whose other intermediate corner also
   has status `AB`.

#### Construction

Let `C` be a clique of order `q-2` (empty when `q=2`).  Let

\[
                 X_i=u_iv_i\qquad(1\le i\le4)
\]

be four pairwise anticomplete edges, and put

\[
                    J_q=C\vee(4K_2).
\]

Make both roots adjacent to every vertex of `C`, and set

\[
 \begin{aligned}
 N_{J_q}(a)-C&=\{u_1,u_2,u_3,u_4\},\\
 N_{J_q}(b)-C&=\{u_1,u_2,v_3,v_4\}.
 \end{aligned}                                           \tag{4.1}
\]

#### Proof

In every proper `q`-colouring, `C` uses `q-2` colours and every edge
`X_i` uses the same two remaining colours, say `alpha,beta`.  Encode its
orientation by the colour of `u_i`.

The root `a` fails to dominate exactly when all four `u_i` have one
colour.  The root `b` fails to dominate exactly when
`u_1,u_2,v_3,v_4` have one colour.  These two events are incompatible:
if all `u_i` have colour `delta`, then `v_3,v_4` have the other colour.
This proves item 1.

A colouring has status `A` precisely when, up to complementing all four
orientations,

\[
             (c(u_1),c(u_2),c(u_3),c(u_4))
                    =(\alpha,\alpha,\beta,\beta),        \tag{4.2}
\]

and it has status `B` precisely when the four entries are all equal.
The two sets of orientation vectors have Hamming distance two.

An `alpha-beta` Kempe component is one edge `X_i`, so such an interchange
flips one coordinate.  An interchange of two colours used on `C` merely
permutes colours on `C` and does not change either root status.  An
interchange using one colour of `C` and one of `alpha,beta` contains the
corresponding vertex of `C` and the endpoint of that colour on every
`X_i`; it changes the name of one of the two non-clique colours but leaves
the four relative orientations, and hence both statuses, unchanged.
Therefore no single Kempe interchange joins `A` to `B`.

Starting from (4.2), interchange `alpha,beta` first on `X_3` and then on
`X_4`.  After either single interchange both roots dominate; after both,
only `b` dominates.  The two edge-components are disjoint and
anticomplete, so the interchanges strongly commute and the other order has
the same `AB` intermediate status.  This proves items 2--4.  \(\square\)

For `q=6`, the host `J_6` is six-chromatic and four-connected.  It falls
one connectivity level below the five-connected common host forced by a
hypothetical `HC_7` counterexample.  It is not asserted to arise from a
strongly seven-contraction-critical, `K_7`-minor-free graph.  Proposition
4.1 therefore does not refute an `HC_7`-specific theorem using those
additional hypotheses.  It does refute the proposed general causal-chain
lemma based only on the universal root-domination property.

## 5. Exact remaining translation gap

The audited direct `A -> B` theorem still applies whenever the minimum
distance between the two exclusive status sets is one.  At larger
distance, the results above leave two distinct tasks:

* in a noncommuting part of a shortest path, turn overlap of successive
  Kempe components into a connected host subgraph with useful boundary
  contacts; and
* in a commuting overlap cube, use five-connectivity,
  contraction-critical colouring witnesses, or `K_7`-minor exclusion to
  rule out the parallel redundancy pattern of Proposition 4.1 or convert
  it into a minor model or a separation.

Neither task follows from the three-status cover of the colouring space.
In particular, one may not assert that moving the loss interchange before
the gain interchange produces a colouring in which neither root
dominates: the alternate colouring can, and in Proposition 4.1 does, have
status `AB`.
