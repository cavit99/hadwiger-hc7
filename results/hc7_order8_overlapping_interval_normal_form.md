# Overlapping demand intervals in a path component

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_overlapping_interval_normal_form_audit.md`](hc7_order8_overlapping_interval_normal_form_audit.md).
This note gives an exact normal form for the special boundary-full
order-eight case in which the selected component itself is an induced path.
It does not assert that an arbitrary fan spine contains every vertex of its
component, align a regenerated clique-minor model with inherited branch-set
labels, or prove `HC_7`.

## 1. Literal setting and the exact split criterion

Let `G` be seven-connected, let `S` be an eight-vertex set, and suppose
that `G-S` has at least two components.  Let one component be the induced
path

\[
                         C=p_0p_1\cdots p_m,
                         \qquad m\ge 1,                 \tag{1.1}
\]

and assume that `C` is adjacent to every literal vertex of `S`.  Let
`D,E` be disjoint two-element subsets of `S`.  The two requested connected
subgraphs are required to be disjoint, the first to contain `p_0` and have
an edge to both members of `D`, and the second to contain `p_m` and have an
edge to both members of `E`.

For `s in S`, put

\[
 N_P(s)=\{i:p_is\in E(G)\},\qquad
 \ell(s)=\min N_P(s),\qquad r(s)=\max N_P(s).          \tag{1.2}
\]

These quantities exist by boundary-fullness.  Define

\[
                 a=\max_{d\in D}\ell(d),\qquad
                 b=\min_{e\in E}r(e).                 \tag{1.3}
\]

### Lemma 1.1 (exact rooted split criterion)

The two requested connected subgraphs exist inside `C` if and only if

\[
                              a<b.                     \tag{1.4}
\]

#### Proof

Every connected vertex set of the path containing `p_0` is a prefix, and
every connected vertex set containing `p_m` is a suffix.  Thus the
requested objects exist precisely when some cut index
`q` has

\[
 \{p_0,\ldots,p_{q-1}\}\sim D,
 \qquad
 \{p_q,\ldots,p_m\}\sim E.                            \tag{1.5}
\]

The first condition is equivalent to `q>=a+1`, and the second to `q<=b`.
Such an integer exists exactly when `a<b`. \(\square\)

This criterion uses all literal `C-S` edges, not merely the attachment
points of one selected fan.  Consequently an overlap surviving Lemma 1.1
is a host obstruction rather than an artefact of a poorly chosen fan.
Moreover, when `b<=a`, every left rooted set contains `P[0,a]` and every
right rooted set contains `P[b,m]`.  Their two minimum connected hulls
therefore intersect in exactly the compulsory subpath `P[b,a]`.

## 2. Strict reversal

Assume

\[
                              a>b.                     \tag{2.1}
\]

Choose `d in D` and `e in E` with

\[
                         \ell(d)=a,\qquad r(e)=b.       \tag{2.2}
\]

Put

\[
 \begin{aligned}
 L&=\{p_0,\ldots,p_b\},\\
 Z&=\{p_b,\ldots,p_a\},\\
 R&=\{p_a,\ldots,p_m\}.
 \end{aligned}                                        \tag{2.3}
\]

The sets `L,R,Z` are connected.  The two tails `L,R` are disjoint, while
the displayed overlap between a tail and `Z` is intentional.  Write

\[
                   \Gamma(Q)=N_G(Q)\cap S             \tag{2.4}
\]

for a subpath `Q` of `C`.

### Theorem 2.1 (strict-reversal separator normal form)

In the setting above:

1. `d notin Gamma(L)` and `e notin Gamma(R)`.
2. Each tail gives exactly one of the following alternatives:

   \[
   \begin{array}{ll}
   |\Gamma(L)|=6,&N_G(L)=\Gamma(L)\mathbin{\dot\cup}\{p_{b+1}\}
        \text{ is an actual order-seven boundary};\\
   |\Gamma(L)|=7,&\Gamma(L)=S-\{d\};
   \end{array}                                         \tag{2.5}
   \]

   and symmetrically

   \[
   \begin{array}{ll}
   |\Gamma(R)|=6,&N_G(R)=\Gamma(R)\mathbin{\dot\cup}\{p_{a-1}\}
        \text{ is an actual order-seven boundary};\\
   |\Gamma(R)|=7,&\Gamma(R)=S-\{e\}.
   \end{array}                                         \tag{2.6}
   \]

3. Let

   \[
        \eta={\bf1}_{b>0}+{\bf1}_{a<m}.               \tag{2.7}
   \]

   Then

   \[
          |N_G(Z)|=|\Gamma(Z)|+\eta\ge7.              \tag{2.8}
   \]

   Equality gives an actual order-seven separation whose boundary
   contains `d,e` and for which the two edges

   \[
                         f=p_be,qquad g=p_ad           \tag{2.9}
   \]

   both cross from `Z` to its boundary.  If equality does not hold, then

   \[
                         |\Gamma(Z)|\ge8-\eta.         \tag{2.10}
   \]

In particular, if none of the three displayed subpaths returns an
order-seven separation, the interval obstruction has the following exact
form: the left and right tails are opposite one-defect connected
subgraphs, the middle subpath meets at least `8-eta` boundary vertices,
the tails respectively miss `d,e`, and the two corresponding contact
edges in (2.9) are independent.

#### Proof

The definitions in (2.2) say that `d` has no neighbour among
`p_0,...,p_{a-1}` and that `e` has no neighbour among
`p_{b+1},...,p_m`.  Since `b<a`, this proves item 1 and also shows that the
two edges in (2.9) exist and are vertex-disjoint.

Because `C` is a component of `G-S` and is an induced path,

\[
 N_G(L)=\Gamma(L)\mathbin{\dot\cup}\{p_{b+1}\},
 \qquad
 N_G(R)=\Gamma(R)\mathbin{\dot\cup}\{p_{a-1}\}.      \tag{2.11}
\]

Each displayed neighbourhood separates its nonempty tail from the other
component of `G-S`.  Seven-connectivity gives
`|Gamma(L)|,|Gamma(R)|>=6`.  Item 1 bounds each order by seven.  Equality
at six gives an actual order-seven separation.  Equality at seven means
that the one already identified missing boundary vertex is the only one,
which proves (2.5)--(2.6).

The same component and induced-path observations give

\[
 N_G(Z)=\Gamma(Z)\mathbin{\dot\cup}
       (\{p_{b-1}:b>0\}\cup\{p_{a+1}:a<m\}).          \tag{2.12}
\]

This is again a genuine separator: the other component of `G-S` is wholly
outside `Z` and its neighbourhood.  Seven-connectivity proves (2.8).
Both `d,e` lie in `Gamma(Z)` by (2.2), and (2.9) then verifies the claimed
operation placement in the equality case.  If (2.8) is strict, integrality
and (2.12) give (2.10). \(\square\)

### Corollary 2.2 (the critical two-edge fork is canonical)

Assume additionally that

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
                                                               \tag{2.13}
\]

For the independent edges `f,g` in (2.9), the common deletion
`H=G-\{f,g\}` has the three endpoint signatures

\[
 ({\rm equal},{\rm equal}),\quad
 ({\rm equal},{\rm proper}),\quad
 ({\rm proper},{\rm equal}),                           \tag{2.14}
\]

and has no `(proper,proper)` six-colouring.  Moreover, one of the following
holds:

1. `G` has an actual order-seven separation placing `f` and `g` on
   opposite closed shores; or
2. `H` contains a `K_4`-minor model rooted at the four literal vertices
   `p_b,e,p_a,d`.

#### Proof

The signature assertion follows by contracting either or both independent
edges and expanding a six-colouring of the resulting proper minor.  A
six-colouring proper on both edges would six-colour `G` after the edges
were restored.  The stated placement/rooted-model alternative is exactly
the audited two-independent-critical-edge theorem applied to `f,g`.
\(\square\)

Thus strict interval reversal is not an unstructured ordering residue.  It
canonically exposes the four roots of the existing label-preserving
absorption problem.  Outcome 2 is still unlabelled: its four rooted branch
sets may traverse any of the five inherited common branch sets.

## 3. A shared portal

It remains to consider

\[
                              a=b=q.                   \tag{3.1}
\]

Choose `d,e` as in (2.2).  Then the two edges

\[
                              p_qd,\qquad p_qe         \tag{3.2}
\]

share their `C`-end.  This is a different operation mode from the
independent-edge fork.

### Theorem 3.1 (shared-portal response normal form)

Assume (2.13), and put

\[
                         H=G-\{p_qd,p_qe\}.            \tag{3.3}
\]

Then

\[
                              \chi(H)=6.               \tag{3.4}
\]

Consequently `H` contains a `K_6` minor, and that model can be enlarged to
a spanning `K_6`-minor model of `H`.  The common deletion always has the
two exclusive signatures

\[
                 ({\rm equal},{\rm proper}),\qquad
                 ({\rm proper},{\rm equal}),           \tag{3.5}
\]

and has no `(proper,proper)` six-colouring.  If `de` is not an edge, it
also has the simultaneous `(equal,equal)` signature.  No such simultaneous
signature is asserted when `de` is an edge.

If `q>0`, the prefix `P[0,q-1]` either has an actual order-seven full
neighbourhood or is adjacent to all of `S-\{d\}`.  If `q<m`, the suffix
`P[q+1,m]` either has an actual order-seven full neighbourhood or is
adjacent to all of `S-\{e\}`.

#### Proof

The graph `H` is a proper minor and hence is six-colourable.  If it had a
proper colouring with at most five colours, recolour `p_q` with a new sixth
colour.  Restoring both deleted incident edges would then give a proper
six-colouring of `G`, contrary to (2.13).  This proves (3.4).  The known
parameter-six case of Hadwiger's conjecture gives a `K_6` minor.  Since
`kappa(G)<=lambda(G)`, deleting two edges from the seven-connected graph
`G` leaves `H` connected.  Components outside that model can therefore be
absorbed into adjacent branch sets, making it spanning.

Contracting either edge separately and expanding a proper-minor colouring
gives the two signatures in (3.5): the other incident edge remains present
and is therefore proper.  A `(proper,proper)` colouring would remain proper
after both edges were restored.  When `de` is absent, contracting both
incident edges and expanding gives a proper `(equal,equal)` colouring of
`H`.  If `de` is present, that contraction identifies its two ends and the
expanded assignment is not proper on `H`; this is why no simultaneous
claim is made in that case.

For the prefix, componenthood and the induced-path hypothesis give

\[
 N_G(P[0,q-1])=
   \Gamma(P[0,q-1])\mathbin{\dot\cup}\{p_q\}.         \tag{3.6}
\]

It misses `d`, by `ell(d)=q`.  Seven-connectivity therefore says that its
boundary-contact set has order six or seven, giving the two stated
alternatives.  The suffix argument uses `r(e)=q` and is symmetric.
\(\square\)

The spanning `K_6` model in Theorem 3.1 is not aligned with the inherited
five common branch-set labels.  Absorbing the shared portal into that model
without destroying one of the two selected edge responses is therefore a
literal label-allocation problem, not a palette-colour consequence.

## 4. Consequence and trust boundary

For a spanning path component, the overlap obstruction has only two host
modes:

1. a strict reversal, which gives opposite one-defect tails, a highly
   exposed middle subpath, and a canonical independent-edge rooted-`K_4`
   fork; or
2. one shared portal, whose common two-edge deletion is six-chromatic and
   regenerates a spanning but unlabelled `K_6` model.

This eliminates arbitrary attachment order as a further issue in the path
component.  It does not handle vertices of `C-P`, turn either regenerated
rooted model into the required five named branch-set contacts, or make an
order-seven boundary partition extend through both intact closed shores.
Those are exactly the label-preserving and colouring-compatibility steps
left by the active theorem.

## 5. Sharpness outside the path-component hypothesis

The induced-path-component hypothesis cannot simply be replaced by the
existence of an all-boundary fan with a path spine.  The audited graph
`K_2 vee I`, where `I` is the icosahedral graph, from the
[paired-fan barrier](../barriers/hc7_common_label_paired_fan_k7_barrier.md)
already gives a sharp witness.

Use its boundary

\[
 S=\{p,q,t,d,u_0,w_0,u_2,w_2\},
\]

its component `C={u_3,u_4,w_3,w_4}`, and the spanning path

\[
                         P=u_4u_3w_3w_4.              \tag{5.1}
\]

Take roots `u_4,w_4` and demand sets

\[
                         D=\{q,d\},\qquad
                         E=\{w_0,u_2\}.               \tag{5.2}
\]

Every boundary vertex has an edge to `P`, so eight direct edges form an
all-boundary fan.  Along (5.1), the latest first `D`-contact is the
`d`-contact at `w_3`, while the earliest last `E`-contact is the `u_2`
contact at `u_3`.  The selected intervals are strictly reversed.

Nevertheless no two requested connected subgraphs exist even after all
edges of `G[C]` are allowed.  A left set containing `u_4` and meeting `d`
must contain `w_3` or `w_4`.  A right set containing `w_4` and meeting
`u_2` must contain `u_3`.  Since `u_3w_4` is absent, that right connected
set must additionally contain `u_4` or `w_3`.  It cannot contain `u_4`,
so it contains `w_3`; the left set must then contain `w_4`.  Disjointness
is impossible.

The graph is seven-connected and `K_7`-minor-free, but it is
six-colourable and the barrier records a compatible order-seven
separation.  Thus seven-connectivity, `K_7`-minor exclusion and an
all-boundary fan do not themselves reroute overlapping intervals.  A
positive theorem must use the proper-minor response prohibition and retain
the compatible-separator alternative.

## 6. Dependencies

- seven-connectivity and the fan-independent literal contact sets in
  (1.2);
- the [two-independent-critical-edge placement/rooted-model fork](../results/hc7_two_edge_opposite_shore_or_rooted_k4.md);
- the established parameter-six case of Hadwiger's conjecture.
