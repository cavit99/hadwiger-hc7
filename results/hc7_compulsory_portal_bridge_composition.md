# Composition at the compulsory Hall portal

**Status:** proved and independently audited.

This note starts from the compulsory outcome of the audited
prescribed-portal Hall descent.  It strengthens the six-fan interface by
retaining the two old packets separately.  The result is an exact
three-carrier path over a six-vertex boundary, an immediate near-`K_7`
handoff whenever that boundary has a `K_4` minor, and a precise Kempe lock
in the remaining strongly contraction-critical case.

It does **not** prove that the bridge ends are a fixed apex pair.

## 1. Setup

Use the notation and all hypotheses of
`../results/hc7_exact7_hall_descent_packet_classification.md`.  In
particular,

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

`R` contains disjoint connected `S`-full packets `P,Q` joined by a
literal edge, and the prescribed-portal descent has

\[
 X=Y\mathbin{\dot\cup}\{z\}=N_L(U),\qquad
 |Y|=|U|-1,\qquad 1\le |U|\le3.                       \tag{1.1}
\]

The set `U` is inclusion-minimal deficient, so every nonempty proper
`D subsetneq U` obeys

\[
                         |N_Y(D)|\ge |D|.              \tag{1.2}
\]

The set `C=L-X` is nonempty, connected, and full to

\[
 \Omega=(S-U)\cup Y\cup\{z\}.
\]

In the compulsory outcome, `z` has the unique neighbour `u_* in U`.
Put

\[
 W=(S-U)\cup Y,\qquad A=C\cup\{z\},\qquad O=R\cup U. \tag{1.3}
\]

Then `|W|=6`.  The companion draft
`hc7_compulsory_portal_bridge_fan.md` proves that `G-W` consists of
the connected sides `A,O` joined by the unique bridge `zu_*`, and gives a
rooted `K_2 join G[W]` minor.  The arguments below need only the literal
setup above and are included independently of that fan construction.

## 2. The old packets split over the six-core

### Lemma 2.1 (two `W`-full traces)

There is a partition

\[
                         U=T_1\mathbin{\dot\cup}T_2   \tag{2.1}
\]

such that both `T_i` dominate `Y`.  Empty sets are permitted only when
`Y` is empty.  The indexing may be chosen so that `u_* in T_1`.

#### Proof

Write `k=|U|`.

If `k=1`, then `Y` is empty; take `T_1=U,T_2=emptyset`.

If `k=2`, then `Y={y}`.  Applying (1.2) to each singleton of `U` shows
that `y` is adjacent to both members of `U`.  Use the two singleton
parts, indexed so that the first contains `u_*`.

Suppose `k=3`, so `Y={y_1,y_2}`.  Condition (1.2) applied to the
two-subsets of `U` implies that each `y_i` has at least two neighbours in
`U`.  Their two neighbourhoods therefore intersect; choose

\[
              t\in N_U(y_1)\cap N_U(y_2).
\]

Both `{t}` and `U-{t}` dominate `Y`: the first does so by the choice of
`t`, while each `y_i` has a second neighbour because its `U`-degree is at
least two.  These are the required parts, with their names interchanged
if necessary.  \(\square\)

### Theorem 2.2 (the compulsory three-carrier path)

Define

\[
                    B_1=P\cup T_1,
              \qquad B_2=Q\cup T_2.                  \tag{2.2}
\]

Then `A,B_1,B_2` are pairwise disjoint connected `W`-full sets and their
literal adjacency graph is exactly the path

\[
                         A-B_1-B_2.                   \tag{2.3}
\]

In particular, `A-B_2` is anticomplete.

#### Proof

Each `B_i` is connected: every member of `T_i subseteq S` has a neighbour
in the old `S`-full packet assigned to it.  It contacts every member of
`S-U` through that old packet and every member of `Y` through the
dominating trace `T_i`.  Hence it is `W`-full.  The old literal `P-Q`
edge gives `B_1-B_2`.

The set `A` is connected because `C` is connected and fullness of `C` to
`Omega` gives a `C-z` edge.  The set `C` itself contacts every member of
`W subseteq Omega`, so `A` is `W`-full.

There is no `C-(R union U)` edge: the old separation excludes `C-R`,
while `X=N_L(U)` excludes `C-U`.  There is no `z-R` edge, and the only
`z-U` edge is `zu_*`.  Since `u_* in T_1`, this is an `A-B_1` edge and
there is no `A-B_2` edge.  \(\square\)

## 3. A boundary `K_4` is already a near model

### Corollary 3.1 (six-core `K_4` handoff)

If `G[W]` contains a `K_4` minor, then `G` contains a literal
`K_7^-` model and hence a `K_7^vee` minor.

#### Proof

Let `D_1,D_2,D_3,D_4 subseteq W` be the four branch sets of a `K_4`
model in `G[W]`.  Use the seven disjoint bags

\[
                  A,B_1,B_2,D_1,D_2,D_3,D_4.          \tag{3.1}
\]

The four `D_i` are pairwise adjacent.  Since each of `A,B_1,B_2` is
`W`-full, it is adjacent to every nonempty `D_i`.  The carrier path
(2.3) supplies `A-B_1` and `B_1-B_2`; its sole missing pair is
`A-B_2`.  Thus (3.1) is exactly a literal `K_7^-` model.  \(\square\)

Consequently every compulsory residue not already handed to the
near-model spine satisfies

\[
                         G[W]\not\succeq K_4.          \tag{3.2}
\]

This is stronger than the `K_5`-minor exclusion obtained from the rooted
two-fan quotient.  Equivalently, the unresolved six-core has treewidth at
most two and is three-colourable.  No claim is made that this static
width-two fact selects a useful exact boundary state.

The atomic `|U|=1` case has a second, portal-rooted handoff.  It will be
useful if the six-core itself has no `K_4` minor.

### Corollary 3.2 (rooted-triangle handoff in the atomic case)

Assume `U={u_*}` and hence `Y=emptyset`.  If `G[W]` has three disjoint
connected pairwise adjacent branch sets `D_1,D_2,D_3`, each containing a
literal neighbour in `W` of `u_*`, then `G` contains a literal
`K_7^vee` model.

#### Proof

Here Theorem 2.2 may be written

\[
                         B_1=P\cup\{u_*\},
                   \qquad B_2=Q.
\]

Use the six rim bags

\[
                    \{u_*\},P,Q,D_1,D_2,D_3.          \tag{3.3}
\]

They form a `K_6` model.  The first three bags are pairwise adjacent:
the old packets are adjacent and both contact the old boundary literal
`u_*`.  The packets are `W`-full and hence meet every `D_i`; the `D_i`
are pairwise adjacent; and the rooted hypothesis makes `{u_*}` adjacent
to every `D_i`.

Take `A` as the seventh bag.  It meets `{u_*}` through the compulsory
edge and meets every `D_i` by `W`-fullness.  Its only missing rim
adjacencies are to `P,Q`, and they have the common endpoint `A`.  This is
exactly a literal `K_7^vee` model.  \(\square\)

Thus an atomic survivor has neither a `K_4` minor in the six-core nor an
`N_W(u_*)`-rooted `K_3` model there.  The latter is a labelled portal
condition, not a claim that ordinary treewidth two is sufficient.

## 4. The twin exact-seven boundary

Put

\[
                         \Sigma=W\cup\{u_*\}.          \tag{4.1}
\]

### Lemma 4.1 (strict twin descent except at `|U|=1`)

The connected set `A` has

\[
                         N_G(A)=\Sigma.                \tag{4.2}
\]

Every component `K` of `G[O-\{u_*\}]` satisfies

\[
                         N_G(K)=\Sigma.                \tag{4.3}
\]

Thus `Sigma` is a literal exact-seven boundary.  Moreover

\[
                         |A|=|L|-|Y|.                  \tag{4.4}
\]

It is a strict smaller-`L` descent whenever `|U|>=2`; at `|U|=1` it is
the old boundary with `u_*` exchanged for the bridge description and no
shore-order decrease.

#### Proof

The set `C` contacts all of `W` by `Omega`-fullness, and `z` contacts
`u_*`.  The edge exclusions used in Theorem 2.2 show that these are all
neighbours of `A` outside `A`, proving (4.2).

Let `K` be a component of `O-u_*`.  After `u_*` is deleted there is no
edge from `K` to `A`, and distinct components of `O-u_*` are anticomplete.
Hence `N_G(K) subseteq Sigma`.  Its complement contains the nonempty set
`A`.  Seven-connectivity and `|Sigma|=7` force equality, proving (4.3).

Finally

\[
 A=(L-X)\cup\{z\}=L-Y,
\]

so (4.4) follows from `|Y|=|U|-1`.  \(\square\)

The lemma gives a genuine well-founded output for the `|U|=2,3`
compulsory cases.  It does not assert that the descended packet vector or
an attained equality state is preserved.  The nondecreasing atomic case
is exactly

\[
                 U=\{u_*\},\qquad Y=emptyset,
                 \qquad W=S-\{u_*\}.                  \tag{4.5}
\]

## 5. What strong contraction-criticality forces at the bridge

Assume now that `G` is strongly `7`-contraction-critical.  Let

\[
                              e=zu_*.
\]

### Lemma 5.1 (exact Kempe lock)

For every proper six-colouring `phi` of `G-e`, put

\[
                         alpha=\phi(z)=\phi(u_*).
\]

Then, for every colour `beta != alpha`, the vertices `z,u_*` lie in the
same `alpha-beta` Kempe component.  Every corresponding bichromatic
`z-u_*` path meets `W`.

If `alpha` is absent from `phi(W)`, then `phi(W)` uses exactly the other
five colours; in particular `alpha` is the unique palette colour missing
on `W`.  More generally, if a colour `beta` is absent on `W`, every
`alpha-beta` bridge path meets an `alpha`-coloured literal of `W`.

#### Proof

The graph `G-e` is a proper minor and hence has a six-colouring.  In any
such colouring the two ends of `e` have the same colour, since otherwise
the colouring would also colour `G`.

Fix `beta != alpha`.  If the `alpha-beta` component containing `z` did
not contain `u_*`, interchange `alpha,beta` on that component.  This keeps
`G-e` properly coloured and makes the ends of `e` different, again giving
a six-colouring of `G`.  Therefore the two ends lie in the same component.
The edge `e` is the unique `A-O` edge in `G-W`, so after deleting `e`
every `z-u_*` path meets `W`.

Such a path can meet on `W` only vertices coloured `alpha` or `beta`.
If both colours were absent there, the path could not cross `W`.  Hence,
if `alpha` is absent, every other colour occurs on `W`.  There are five
such colours and six boundary vertices, proving the unique-missing-colour
statement.  If only `beta` is absent, the required boundary vertex on the
path has colour `alpha`.  \(\square\)

Lemma 5.1 is the exact obstruction to naive colour gluing over the
six-core: the bridge edge is protected, in every deletion colouring, by
five two-colour return chains through `W`.  A valid composition theorem
must decode those chains together with the width-two core (3.2), not just
permute an unused colour on one bridge side.

There is also an exact state-language version of the same lock.

### Lemma 5.2 (single-edge palette compatibility)

Let `phi_A` and `phi_O` be proper six-colourings of `G[A union W]` and
`G[O union W]`, respectively, inducing the same exact equality partition
`Pi` on `W`.  Relative to either colouring, call the endpoint type of
`z`, respectively `u_*`,

* the block `B in Pi` if the endpoint has the colour of `B`; or
* **spare** if its colour is absent from `W`.

The two closed-shore colourings can be palette-aligned and glued to a
six-colouring of `G` unless one of the following holds:

1. both endpoints have the same block type `B in Pi`; or
2. `|Pi|=5` and both endpoints have spare type.

Consequently, in a non-six-colourable host, every legally produced pair
of closed-shore colourings with a common exact boundary state is locked
in one of these two ways.

#### Proof

Align the distinct colours of corresponding blocks of `Pi`.  This fixes
a bijection on the `|Pi|` colours used on `W` and leaves an arbitrary
bijection between the two complementary sets of `6-|Pi|` spare colours.

If the endpoint block types are distinct, their aligned colours are
distinct.  If exactly one endpoint has spare type, its aligned colour is
outside the boundary-colour set and is again distinct from the other
endpoint.  If both are spare and at least two spare colours exist, choose
the remaining bijection so that their colours differ.  In all these cases
the two colourings agree on `W`, differ on the ends of the sole cross-edge
`zu_*`, and therefore glue to a six-colouring of `G`.

The only unavoidably equal cases are the same named boundary block, or the
unique spare colour when `6-|Pi|=1`.  \(\square\)

Unlike an informal “unused-colour swap”, Lemma 5.2 records exactly what a
proper-minor transition has to change: either the named endpoint blocks
must separate, or a five-block state must create a second spare colour.

## 6. A sharp warning about the bridge ends

The bridge interface alone does not make `{z,u_*}` the desired fixed
pair.  Here is a small standard family witnessing the failed implication.

Let `H` be the icosahedral graph.  It is five-connected and planar.  In
the usual NetworkX labelling, deleting

\[
                         W_0=\{0,1,2,7\}
\]

leaves the bridge `8-9`.  Put

\[
                         G=K_2\vee H,
 \qquad W=V(K_2)\cup W_0,
 \qquad z=8,\quad u_*=9.                              \tag{6.1}
\]

Then `G` is seven-connected and `zu_*` is a bridge of `G-W`.  It is
`K_7`-minor-free: a clique join satisfies

\[
                         \eta(K_r\vee F)=r+\eta(F),    \tag{6.2}
\]

and planar `H` has `eta(H)<=4`.  Nevertheless
`G-\{8,9\}` contains a literal `K_5`: the two join vertices together with,
for example, the triangle `0,1,5` of `H-\{8,9\}`.

For completeness, seven-connectivity is immediate without a connectivity
formula.  After deleting at most six vertices, either a join vertex
remains and connects every surviving vertex, or both join vertices were
deleted and at most four vertices were deleted from the five-connected
graph `H`.  For (6.2), in any clique-minor model at most `r` branch sets
contain a join vertex; deleting those bags leaves a clique-minor model
entirely in `F`.  This proves the upper bound, while adjoining the `r`
singleton join vertices to a maximum model in `F` proves equality.

In the displayed icosahedral labelling, vertex `8` has neighbours
`0,1,2,7,9`.  Hence it has the sole neighbour `9` after `W_0` is deleted,
which verifies the asserted bridge.  The edges `01,05,15` verify the
triangle used above.

Thus seven-connectivity, `K_7`-minor-freeness, saturated six-fan routing,
and the twin boundaries do **not** imply

\[
                         G-\{z,u_*\}\not\succeq K_5. \tag{6.3}
\]

The example has a different coherent apex pair (the two join vertices)
and it also has the near-model output of Corollary 3.1.  It therefore does
not refute the intended disjunction “near model or some fixed pair”; it
only rules out promoting the canonical bridge ends to that pair without
using contraction-critical state transitions.

## 7. Exact residual

After the proved outputs above, the compulsory Hall branch has one atomic
composition cell:

1. `|U|=1`, so the twin map does not decrease shore order;
2. `G[W]` is `K_4`-minor-free, otherwise Corollary 3.1 hands off a literal
   `K_7^-` model; and
3. `G[W]` has no `N_W(u_*)`-rooted `K_3` model, otherwise Corollary 3.2
   gives a labelled two-missing-spoke handoff; and
4. every colouring of `G-zu_*` has the five Kempe locks of Lemma 5.1,
   while every common exact six-core state has one of the two endpoint
   locks in Lemma 5.2.

Closing this cell requires one genuinely dynamic statement: the locked
two-colour paths through a width-two six-core must either reroute the
three-carrier path into a literal `K_7`, expose a smaller actual
seven-adhesion with a transported seed state, or identify a coherent
fixed pair not assumed to be `{z,u_*}`.  The twin-boundary and fan facts
alone are exhausted by the example in Section 6.
