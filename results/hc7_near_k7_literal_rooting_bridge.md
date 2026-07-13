# From an arbitrary `K_7^vee` model to a literal near-clique shell

## Status

This note does not prove `HC_7`.  It proves two pieces of the missing
rooting step.

1. A literal `K_6^-` subgraph is already exactly the singleton-core shell:
   seven-connectivity supplies all of the connected remainder and portal
   hypotheses automatically.  Thus no spanning-model or bag-assignment
   argument remains after the six literal roots have been found.
2. In a labelled `K_7^vee` model one neutral bag can be chosen as a
   **source bag**.  Every detachable part of that bag owns at least two of
   its six labelled model adjacencies.  In particular a two-connected
   source bag has at most three vertices; the order-three case is a
   triangle with an exact `2+2+2` portal partition.

The second statement is a genuine label-preserving normalization of an
arbitrary near model.  It shows that the obstruction to literal rooting is
not an arbitrary large two-connected neutral bag.  What remains unbounded
is a cutvertex tree of at most three multi-label warehouse branches, or
transport of the other three neutral labels into the source.

## 1. A literal `K_6^-` is the exact shell

### Theorem 1.1 (literal-shell extraction)

Let `G` be seven-connected and let

\[
                       Q=\{q_1,q_2,q_3,q_4\}
\]

induce `K_4`.  Suppose two further vertices `x,y` are each adjacent to
every member of `Q`.  Then either `G` contains a `K_7` minor, or

\[
 x y\notin E(G),\qquad
 D=G-(Q\cup\{x,y\})
\]

is connected, is adjacent to each of `x,y`, and is collectively adjacent
to every vertex of `Q`.  Consequently the singleton-core split/exact-seven
theorem in `../archive/hadwiger_near_k7_singleton_core_split_exact7.md` applies
literally to `Q,x,y,D`.

#### Proof

A seven-connected graph has at least eight vertices, so `D` is nonempty.
Deleting the six vertices `Q\cup\{x,y\}` leaves a connected graph, since
six is below the connectivity.  This proves that `D` is connected.

For any `s in Q\cup\{x,y\}`, delete the other five displayed vertices.
The remaining graph is connected.  It contains the nonempty set `D`, so
`s` cannot be isolated from `D`.  Hence `s` has a neighbour in `D`.

If `xy` is an edge, the six displayed vertices induce `K_6`.  The
connected graph `D` is adjacent to every one of them, and therefore

\[
              \{q_1\},\ldots,\{q_4\},\{x\},\{y\},D
\]

is a `K_7` model.  In the target-free branch `xy` is consequently absent,
and all hypotheses of the singleton-core theorem have just been proved.
\(\square\)

### Corollary 1.2 (the exact transversal required from a model)

Let

\[
                 A,B,C,U_1,U_2,U_3,U_4
\]

be a `K_7^vee` model, with deficient pairs `AB,AC`.  If there are vertices

\[
 q_i\in U_i\quad(1\le i\le4),\qquad x\in A,\qquad y\in C
\]

such that the `q_i` form a clique and both `x,y` are adjacent to all four
`q_i`, then Theorem 1.1 gives `K_7` or the literal singleton-core
split/exact-seven outcome.

No adjacency between `x` and `y` is assumed.  If it happens to be present,
Theorem 1.1 gives `K_7` immediately; in the target-free branch the theorem
itself forces `xy` to be absent.

No condition on unused vertices or on the connectedness of the old model
remainder is needed: seven-connectivity supplies it after the six roots
are selected.

## 2. An ordered source bag in every arbitrary model

Write `V_1,V_2,V_3,V_4,V_5,V_6,V_7` for the labels

\[
                    U_1,U_2,U_3,U_4,A,B,C
\]

in this order.  Among all labelled `K_7^vee` models in `G` choose one
minimizing

\[
       (|U_1|,|U_2|,|U_3|,|U_4|,|A|,|B|,|C|)             \tag{2.1}
\]

lexicographically.  The models in this minimization need not be spanning;
this is essential because deleting an inessential branch part must be an
allowed move.

For a label bag `V_i` and a nonempty proper set `X subset V_i`, call `X`
detachable when both `G[X]` and `G[V_i-X]` are connected.  Its monopoly
set is

\[
 \Omega_i(X)=\{j:\ V_iV_j\hbox{ is required in }K_7^vee
       \hbox{ and every }V_iV_j\hbox{ edge has its }V_i
       \hbox{-end in }X\}.                                    \tag{2.2}
\]

### Theorem 2.1 (acyclic portal ownership)

For every detachable `X subset U_i`:

1. `Omega_i(X)` is nonempty;
2. if `Omega_i(X)={j}`, then `j<i`.

In particular every detachable part of the first neutral bag `U_1`
monopolizes at least two of its six required model neighbours.

#### Proof

If `Omega_i(X)` is empty, replace `U_i` by `U_i-X` and leave `X` outside
the model.  All required adjacencies survive, while the `i`th coordinate
of (2.1) decreases and all earlier coordinates are unchanged.  This is a
contradiction.

Suppose `Omega_i(X)={j}`.  All old `U_iV_j` edges have their `U_i` end in
`X`, so `V_j union X` is connected.  Replace

\[
             U_i\longmapsto U_i-X,
             \qquad V_j\longmapsto V_j\cup X.                 \tag{2.3}
\]

The two new bags are adjacent through an `X-(U_i-X)` edge.  The residual
source retains every required adjacency except possibly the one to `V_j`,
and that adjacency is restored by the same cut edge.  The enlarged target
retains all of its old model adjacencies.  Thus (2.3) is a labelled
`K_7^vee` model.

If `j>i`, all coordinates before `i` are unchanged and the `i`th
coordinate decreases, again contradicting (2.1).  Hence `j<i`.  There is
no earlier label when `i=1`, so the last assertion follows. \(\square\)

This is stronger than merely bounding the number of leaves of an
essential portal tree.  A unique-owner obstruction is forced to travel
strictly backwards among the neutral labels; it can never cycle and it
cannot terminate in one of the three deficient labels `A,B,C`.
It does **not** say that all four neutral bags have only multi-label
pieces: later bags may have singleton monopoly sets, but only on earlier
neutral labels.

### Corollary 2.2 (uniform neutral-bag bounds)

Let `X_1,...,X_m` be pairwise disjoint detachable parts of `U_i`.  Then

\[
                         m\le 3,3,4,4
             \quad\hbox{for }i=1,2,3,4,                 \tag{2.4}
\]

respectively.  If `G[U_i]` is two-connected, its order satisfies the same
bound.

#### Proof

The monopoly sets of the disjoint parts are disjoint: for a label `j`,
the nonempty set of all `U_i`-ends of `U_iV_j` edges cannot be contained
in two disjoint parts.  By Theorem 2.1 every monopoly set is nonempty, and
a singleton monopoly set can use only one of the `i-1` earlier neutral
labels.  If there are `s` singleton sets, the remaining parts consume at
least two of the remaining `6-s` labels.  Hence

\[
                 m\le s+\left\lfloor{6-s\over2}\right\rfloor,
                 \qquad 0\le s\le i-1.                         \tag{2.5}
\]

For `i=1,2,3,4`, the maxima are `3,3,4,4`.

If `U_i` is two-connected and has at least three vertices, every singleton
vertex is detachable.  Apply the first part to those pairwise disjoint
singletons. \(\square\)

### Corollary 2.3 (the source bag has at most three leaf warehouses)

Let `K_1,...,K_m` be pairwise disjoint detachable parts of `U_1`.  Then
their monopoly sets are pairwise disjoint, and hence

\[
                              m\le3.                           \tag{2.6}
\]

In particular the interiors of the leaf blocks of `G[U_1]` form at most
three such parts.

#### Proof

For every required label `j`, let `P_j` be the nonempty set of endpoints
in `U_1` of the old `U_1V_j` edges.  If `j in Omega_1(K_s)`, then
`P_j subset K_s`.  Two disjoint parts cannot both contain `P_j`, so their
monopoly sets are disjoint.  Theorem 2.1 gives at least two labels to each
part, while `U_1` has six required neighbours.  This proves (2.6).
The interior of a leaf block is detachable, and distinct leaf-block
interiors are disjoint. \(\square\)

### Corollary 2.4 (a two-connected source is a literal triangle cell)

If `G[U_1]` is two-connected, then either `|U_1|=1` or

\[
                              |U_1|=3.                         \tag{2.7}
\]

In the latter case `G[U_1]` is a triangle, and its three vertices own a
partition of the six other labels into three pairs.  More explicitly, for
each required label all `U_1`-ends of its model edges are one specified
vertex of the triangle, and each triangle vertex is specified by exactly
two labels.

#### Proof

Assume `|U_1|>=3`.  For every `u in U_1`, the singleton `{u}` is
detachable because `U_1-u` is connected.  Theorem 2.1 gives

\[
                         |Omega_1(\{u\})|\ge2.                 \tag{2.8}
\]

The monopoly sets of distinct vertices are disjoint: a nonempty portal
endpoint set cannot be contained in two distinct singleton sets.  There
are only six required labels, so `2|U_1|<=6`.  Hence `|U_1|=3`, and
two-connectivity makes it a triangle.

Equality holds in every count.  Thus the three monopoly sets are disjoint
pairs whose union is all six labels.  If label `j` belongs to the pair at
`u`, every `U_1V_j` edge has its `U_1`-end at `u`; since every label occurs
in one pair, these are exactly the asserted portal rows. \(\square\)

For the bridge convention in which `K_2` is treated as a nonseparable
block, the same singleton-deletion proof says that each end owns at least
two labels.  The only genuinely unbounded source architecture is therefore
a cutvertex chain/tree with at most three multi-label terminal branches.

### Corollary 2.5 (only constant-owner corridors are unbounded)

Root the block--cutvertex tree of `G[U_1]` at any block.  If `K subset L`
are two nested descendant lobes, then

\[
                         \Omega_1(K)\subseteq\Omega_1(L).       \tag{2.9}
\]

Consequently a root-to-leaf chain has at most five distinct monopoly
sets.  Every unbounded subchain contains a consecutive interval on which
the same set of at least two labels is monopolized at every cut.

At every cutvertex there are at most three descendant components.

#### Proof

For a label `j`, let `P_j` again be the nonempty set of all `U_1`-ends of
the `U_1V_j` edges.  Membership `j in Omega_1(K)` says exactly
`P_j subset K`.  If `K subset L`, then also `P_j subset L`, proving
(2.9).

Every lobe monopoly set has order at least two by Theorem 2.1.  A strict
inclusion raises its order, and the largest possible order is six.  Thus
the only possible strict sizes are `2,3,4,5,6`, giving at most five
distinct sets on a chain.  Repetition between two equal sets is constant
throughout the interval by monotonicity.

The descendant components at one cutvertex are disjoint detachable sets.
Corollary 2.2 bounds their number by three. \(\square\)

Thus arbitrary SPQR length has disappeared already at the label level:
the sole unbounded source residue is a constant multi-owner corridor.  A
faithful minor-state exchange is still needed to pump such a corridor;
ordinary portal counting cannot distinguish two consecutive cuts with
the same owner set.

The constant interval has now been sharpened in
`../active/hc7_near_k7_constant_owner_corridor.md`.  Every block internal to it
is a `K_2` bridge, there are no off-corridor source branches, and every
internal interval is behind an actual gate of order at least seven.  At
gate order seven this is the existing exact-seven descent.  At larger
gate order, every internal edge carries at least three externally started
and externally ended Kempe layers in one contraction colouring.  An
explicit arbitrary-length forcing family shows why repetition of those
palette states is not yet a label-preserving pump: palette colours need
not name the six other model bags.

In the sole-complex nonspanning cell, the same continuation gives a
stronger ambient conclusion.  After all unused vertices are absorbed into
the unique complex envelope, any component behind a two-cut has boundary
inside its two gates plus the six literal shell vertices.  It is therefore
an exact-seven shore or a full exact-order-eight lobe; two full lobes give
`K_7` explicitly.  Hence exact-seven descent or one three-connected torso
replaces the entire nonspanning ear chain.

## 3. Interaction with active-root facial coherence

Theorem 2.1 identifies the correct place to use the active-root theorem.
Suppose four pairwise disjoint private extensions have been extracted from
the ordered source architecture and meet one four-connected or planar
three-connected torso `W`.  If their four portal sets have rank four, the
fixed-extension active-face theorem gives one of the following.

1. A rooted `K_4` in `W`; whenever the retained pool/reserve contacts are
   those of the uniform biportal completion, this is a labelled `K_7`.
2. Every usable portal occurrence lies on one common face of `W`.

The unusable-occurrence theorem strengthens the second statement in a
literal one-complex shell: both poles of every selected exact-seven lobe
are usable, unless `K_7` already occurs.  Rural expansion of all the
resulting societies is then precisely the coherent two-apex alternative;
a nonrural occurrence is an alternating port cross, and a shared extension
role is the exact carrier-splitting/exact-seven residue.

What is not yet proved is that the four private extensions and the three
pool/reserve bags can always be extracted from the arbitrary ordered
source architecture.  Theorem 2.1 makes that missing statement finite at
the first two-connected source block (`K_1`, `K_2`, or the exact
`2+2+2` triangle), but cutvertex chains still require a faithful
operation-state transfer.  This is the exact boundary-faithful lift not
provided by contracting the seven old bags.

## 4. Why the coherent alternative and model realignment are necessary

Let `I` be the icosahedron and let `G=K_2 vee I`, with universal vertices
`p,q`.  In the spanning `K_7^vee` model from
`../archive/hadwiger_near_k7_two_complex_bag_round.md`, take

\[
 A=\{b\},\quad B=\{t\},\quad C=\{u_0\},\quad
 U_1=\{p\},\quad U_2=\{q\},
\]

and the two remaining neutral bags

\[
 U_3=\{u_1,w_0\},\qquad
 U_4=\{u_2,u_3,u_4,w_1,w_2,w_3,w_4\}.
\]

The only missing model pairs are `AB,AC`.  However

\[
                         N(b)\cap N(t)\cap N(u_0)=\{p,q\}.      \tag{4.1}
\]

Indeed the neighbours of `b` in `I` are the five lower vertices, while
the neighbours of `t` in `I` are the five upper vertices.  Thus the two
displayed complex neutral bags cannot be shrunk *in place* to singleton
vertices which still see the three displayed singleton deficient bags.

Nevertheless the graph admits a different literal shell, for example

\[
 Q=\{p,q,t,u_0\},\qquad x=u_1,qquad y=u_4.              \tag{4.2}
\]

The four vertices in `Q` form a clique, `x,y` are nonadjacent and complete
to `Q`, and Theorem 1.1 supplies the remainder.  Here the singleton-core
theorem lands in its coherent alternative: `p,q` are universal core rows,
and deleting them leaves the planar icosahedron.  The graph is
seven-connected and `K_7`-minor-free, but is six-colourable.

Thus a correct bridge cannot insist on shrinking one initially displayed
model in place, and it cannot replace the coherent conclusion by `K_7`.
It must permit a global label realignment such as (4.2), or output the
coherent two-apex structure.

## 5. Exact remaining rooting statement

The arbitrary-model gap has now been reduced to the following precise
principle.

> Starting with the ordered source model of Theorem 2.1, either realign
> its at most three multi-owner source branches to obtain six vertices
> inducing `K_6^-`, or expose four fixed private extensions in one active
> torso.  In the latter case, the active-face/occurrence theorems give a
> labelled split, a coherent rural two-apex expansion, or a shared lobe
> behind a literal exact-seven adhesion.

The theorem is complete for the first literal alternative by Theorem 1.1
and for the active rank-four/facial step once the private extensions and
pool bags exist.  The missing part is the simultaneous extraction of
those extensions from a cutvertex source chain while preserving the
proper-minor operation state.  This is strictly narrower than the original
request to make four arbitrary branch bags singleton.
