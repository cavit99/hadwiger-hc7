# Connected-piece transfers do not induce permutation holonomy

**Status:** written structural barrier; separate internal audit GREEN in
[`hc7_order8_transfer_holonomy_barrier_audit.md`](hc7_order8_transfer_holonomy_barrier_audit.md).
This note concerns the exact connected-piece transfers used in the
order-eight opposite-response programme.  It does not prove `HC_7` and is
not a counterexample to `HC_7`.

## 1. The canonical data of one transfer

Fix five pairwise disjoint connected pairwise adjacent branch sets

\[
                              F_1,\ldots,F_5.
\]

Let `X,U` be disjoint connected sets, disjoint from all `F_i`, and suppose
the old seven-set minor model is

\[
                         X,\ U,\ F_1,\ldots,F_5.       \tag{1.1}
\]

The set `X` may miss a specified set `D` of the five fixed branch sets,
while `U` is adjacent to all five.  A legal single connected-piece transfer
has

\[
                         U=Z\mathbin{\dot\cup}W,       \tag{1.2}
\]

where `Z,W` are nonempty connected adjacent sets, `Z` is moved to `X`, and

\[
                         X'=X\cup Z                  \tag{1.3}
\]

is connected.  The new seven-set model is

\[
                         W,\ X',\ F_1,\ldots,F_5.     \tag{1.4}
\]

This is the transfer datum of the audited exact-reversibility theorem.  In
the order-eight application it is overlaid on one closed shore of the
literal boundary

\[
 S=\{d,e\}\mathbin{\dot\cup}X_S\mathbin{\dot\cup}Y_S,
\]

where the two closed shores have the opposite merged-root and split-root
equality-partition responses.  The boundary labels are literal vertices and
are never renamed by (1.2)--(1.4).

### Definition 1.1 (literal inheritance relation)

For one transfer, define

\[
 \Gamma_Z\subseteq
 \{X,U,F_1,\ldots,F_5\}\times
 \{W,X',F_1,\ldots,F_5\}
\]

by

\[
                    (A,B)\in\Gamma_Z
       \quad\Longleftrightarrow\quad A\cap B\ne\varnothing.     \tag{1.5}
\]

This is the strongest label transport determined solely by literal branch
set membership: any literal vertex retained across the transfer witnesses
exactly one pair in (1.5).

### Proposition 1.2 (the canonical transport is not a map)

One has exactly

\[
 \Gamma_Z=
 \{(F_i,F_i):1\le i\le5\}
 \cup\{(X,X'),(U,W),(U,X')\}.                       \tag{1.6}
\]

Consequently `Gamma_Z` is neither the graph of a partial function from old
branch sets to new branch sets nor the inverse graph of such a function.
In particular it cannot be a permutation of the seven named branch-set
identities.

#### Proof

The fixed branch sets are unchanged and disjoint from every other displayed
set, giving the first five pairs.  Since `X subseteq X'`, the pair
`(X,X')` occurs.  Since `U=Z dotcup W`, with both parts nonempty, and
`Z subseteq X'`, both `(U,W)` and `(U,X')` occur.  There are no further
intersections because the old seven sets and the new seven sets are each
pairwise disjoint.

Thus the old donor `U` has two images, while the new set `X'` has two old
preimages.  No function, and hence no permutation, has this incidence
graph. \(\square\)

The obstruction is not caused by colour names.  It is the literal split of
one old branch set and the simultaneous amalgamation of part of it with a
different old branch set.

### Corollary 1.3 (the exact order-eight cover has only identity transport)

Let a connected open shore have an anchored adjacent connected partition

\[
                    R=Q_0\mathbin{\dot\cup}Q_1,
 \qquad P_i\subseteq Q_i\quad(i=0,1),                         \tag{1.7}
\]

where `P_0,P_1` are the two prescribed disjoint boundary-full connected
subgraphs.  A legal repartition transfer replaces (1.7) by

\[
       (Q_0-Z)\mathbin{\dot\cup}(Q_1\cup Z)                  \tag{1.8}
\]

for a nonempty `Z subseteq Q_0-P_0`, while both new parts remain connected,
boundary-full, and contain their prescribed `P_i`.

On the literal labels

\[
                           S\cup\{P_0,P_1\},                    \tag{1.9}
\]

the transfer (1.8) induces only the identity: every boundary vertex and
both prescribed connected subgraphs are unchanged.  The changed datum is
the ownership of the vertices of `Z`, not a permutation of the labels in
(1.9).

#### Proof

The operation changes neither `S` nor either set `P_i`; the containment
condition in (1.7)--(1.8) keeps the same anchor in the correspondingly
named part.  Thus every literal label in (1.9) is fixed.  Exactly the
vertices of `Z` change sides, and those vertices are not named labels in
(1.9). \(\square\)

Consequently the maximal adjacent connected-cover normalization does not
create a nontrivial gauge variable.  To obtain one, a proof would first
have to overlay a new labelled minor model, and its label transport is then
the split-and-amalgamate relation (1.6), not a permutation.

## 2. Forced positional permutations are convention-dependent

One can force a permutation only by discarding part of the literal
inheritance relation.  A common convention lets the old centre identity
follow `X` into `X'` (the new donor position) and lets the old donor identity
follow the residual set `W` (the new centre position), ignoring the fact
that `Z subseteq U cap X'`.  This convention exchanges the two roles and
fixes the five `F_i`.  Write

\[
                       \tau=(\mathsf C\ \mathsf U)               \tag{2.1}
\]

for this transposition.  It is not canonical: naming bags solely by their
current roles instead gives the identity permutation, while following every
literal intersection gives the nonfunctional relation (1.6).

### Proposition 2.1 (the transposition convention records only parity)

Under the convention above, a walk of `k` legal connected-piece transfers
has composite `tau^k`.  It is independent of

- the old and new missing-label sets `D,E`;
- every portal set inside the transferred pieces;
- the two boundary equality-partition response languages;
- the presence of a rooted connected-subgraph split; and
- whether the host has a `K_7` minor.

Hence this forced positional “holonomy” contains exactly the parity of the
length of the chosen transfer word and no label-allocation information.

#### Proof

By convention, every edge of the walk is assigned the same transposition
`tau`, so composition gives `tau^k`.  None of the listed data occurs in
(2.1). \(\square\)

This is not a transport of physical branch-set labels.  It is a chosen
resolution of the split-and-amalgamate relation.  The distinction matters
on a closed walk: this convention can return a nontrivial permutation even
when the literal configuration is identical.

### Concrete barrier

The audited reduced rotation triangle in
[`hc7_global_invariant_rotation_triangle.md`](hc7_global_invariant_rotation_triangle.md)
consists of three literal legal transfers on one fixed five-branch-set frame
and returns to its starting configuration.  The transposition convention
assigns it the nontrivial value `tau^3=tau`, whereas the current-role
convention assigns the identity.  Thus even the presence of “nontrivial
holonomy” depends on the convention rather than on the literal transfer
cycle.

The host is `K_2` joined with the icosahedron (and the same construction
persists in arbitrarily long pentagonal tubes).  It is seven-connected and
`K_7`-minor-free.  It has the coherent two-vertex planar remainder given by
the displayed `K_2`.  Thus the nontrivial positional value does not by
itself construct a `K_7` model; the coherent two-vertex structure is extra
literal host information, not something decoded by `tau`.

The same audited example has one fixed frame and one fixed active vertex
union throughout the triangle.  Consequently adding those two coarse data
to `tau` still does not distinguish which contacts or boundary response
must be used at the end of the walk.

## 3. Quotienting colour names does not create an action

A proper six-colouring modulo global permutation of the six colour names
is exactly its equality partition of the literal boundary.  Let
`Ext(H,S)` be the set of equality partitions of `S` extending through a
closed shore `H`.

### Proposition 3.1 (the canonical colour-gauge action is trivial)

A legal connected-piece transfer changes a selected minor model inside one
fixed closed-shore graph `H`; it changes neither `H`, the literal boundary
`S`, nor `Ext(H,S)`.  Consequently its only canonical action on colourings
modulo global colour renaming is the identity map on `Ext(H,S)`.

This identity does not transport one selected proper-minor response to the
response of a different operation.  In the opposite-response interface the
available operation-specific response languages can instead lie in the two
disjoint set differences

\[
 Ext(H_1,S)\setminus Ext(H_2,S),
 \qquad
 Ext(H_2,S)\setminus Ext(H_1,S).                                 \tag{3.2}
\]

Therefore quotienting colour names removes gauge redundancy but supplies no
nontrivial permutation action relating the required responses.

#### Proof

The transfer (1.2)--(1.4) changes only a selected minor model.  Thus the
ambient equality-partition language is literally unchanged, proving the
identity assertion.  The transfer neither selects a six-colouring nor
specifies a Kempe sequence, so it gives no rule carrying a response of one
deleted or contracted edge to a response of another.

More sharply, the audited opposite-side response theorem places the
response of the donor-interface edge in
`Ext(H_2,S) setminus Ext(H_1,S)` and the response of every newly lost
labelled contact edge in
`Ext(H_1,S) setminus Ext(H_2,S)`.  These sets are disjoint.  Identifying one
operation-specific response with another would therefore require an
additional theorem; it is not induced by the identity action of the
connected-piece transfer. \(\square\)

## 4. Exact conclusion

For a legal connected-piece transfer, the strongest canonical composable
object on literal branch sets is the nonfunctional inheritance relation
(1.6), together with the actual portal sets and operation-specific boundary
response languages.  It is a correspondence, not a permutation.

If literal inheritance is discarded, one may impose the fixed
transposition convention (2.1), but its composite records only word-length
parity and a different natural convention gives the identity.  If colour
names are quotiented out, one obtains
boundary equality partitions on which the transfer acts only as the
identity; that action does not identify the opposite operation-specific
responses.

Accordingly, permutation holonomy adds no proof-closing information to the
exact opposite-response interface.  A viable global composition theorem
must retain the full literal correspondence--portal ownership, transferred
vertex support, and the particular proper-minor response--and prove that a
closed strongly connected transition component has a `K_7` model or one
common compatible separator.  Calling that enriched transition system a
holonomy object does not shorten the remaining theorem.

## 5. Dependencies and trust boundary

The literal relation calculation is self-contained.  The concrete
three-transfer barrier uses the separately audited
[reduced rotation triangle](hc7_global_invariant_rotation_triangle.md).
The response-language statement uses the audited
[opposite-side response theorem](../results/hc7_rotation_opposite_boundary_responses.md).

The reduced triangle already has the coherent two-vertex outcome, so it
does not refute a theorem whose conclusion explicitly allows that outcome.
This note proves only that such an outcome cannot be inferred from a
permutation of transfer roles: the literal host certificate remains
indispensable.
