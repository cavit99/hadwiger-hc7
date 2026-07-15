# Exterior-connectivity closure in the overlap-four cross-arm cell

## Status and scope

This theorem is proved, using the independently audited rooted-`K_4` and
five-terminal cycle decoders for the same normalized cell.  An independent
cold audit is **GREEN**; see
[`hc7_cross_arm_overlap_four_exterior_connectivity_closure_audit.md`](hc7_cross_arm_overlap_four_exterior_connectivity_closure_audit.md).
The decoder inputs are computer-assisted finite theorems; all exterior
structure and all branch-set operations below are proved directly.

The result eliminates the entire four-connected exterior.  In the
`K_7`-minor-free branch it returns an actual order-seven separation whose
components are literal full packets.  That separation is an **unranked
handoff**.  In the strongly contraction-critical specialization its
packing vector normalizes to `(1,1)` or `(1,2)`, but no colouring state or
strict recursive measure is asserted.

## 1. Normalized cell

Let `G` be seven-connected and use the labels

```text
A={0,1,2,3,4,5},        I={0,1,2,3},
X=I union {6},           p=7, q=8,
T={4,5,6,7,8}.
```

Assume that each of the following eleven six-sets is an irredundant
support of a spanning `K_5` model:

```text
A, X union {p}, X union {q},
(A-{i}) union {p}, (A-{i}) union {q}    for i in I.
```

Put

\[
                              H=G-I.                    \tag{1.1}
\]

### Lemma 1.1

The graph `H` is three-connected.

#### Proof

If a set `Z` of order at most two separated `H`, then `I union Z`, of
order at most six, would separate `G`, because

\[
                       G-(I\cup Z)=H-Z.
\]

This contradicts seven-connectivity.  Notice also that `H` contains the
five distinct vertices of `T`, so no small complete-graph convention is
involved.  \(\square\)

## 2. Four-connected exterior closure

### Theorem 2.1

If `H` is four-connected, then `G` contains a `K_7` minor.

#### Proof

We first apply the rooted-`K_4` theorem of Fabila-Monroy and Wood to each
four-set `T-{t}`, for `t in T`.  In a four-connected graph, that theorem
says that the four nominated vertices root a `K_4` model, or the graph is
planar and the four vertices occur on one face.

If any `T-{t}` roots a `K_4` model in `H`, Theorem 1.1 of
[`hc7_cross_arm_overlap_four_rooted_k4_decoder.md`](hc7_cross_arm_overlap_four_rooted_k4_decoder.md)
applies.  Its direct outcome is already a `K_7` model.  Its other outcome
is a support-at-most-five `K_4` contacted by three prescribed roots, and
the independently audited three-rooted composition theorem then gives a
`K_7`.  We may therefore assume that no four-subset of `T` roots a
`K_4` in `H`.

It follows that `H` is planar and every four-subset of `T` is cofacial.
Fix its plane embedding, which is unique up to reflection because `H` is
three-connected.  Let `F_6` contain

```text
T-{6}={4,5,p,q}
```

and let `F_4` contain

```text
T-{4}={5,6,p,q}.
```

The two faces share the three distinct vertices `5,p,q`.  Distinct faces
of a three-connected plane graph share at most two vertices, so
`F_4=F_6`.  Hence all five vertices of `T` lie on one face.  Denote its
boundary cycle by `C`.

We use the standard peripheral-cycle theorem: every facial cycle of a
three-connected plane graph is induced, and deleting its vertices leaves
a connected graph (possibly empty).  For clarity, both conclusions are
exactly where three-connectivity is used.  A chord of a facial cycle,
or two distinct components behind the same facial cycle, gives by the
Jordan curve theorem a separation through at most two boundary vertices.

Here the remainder is not empty.  Since `H` is four-connected,
`delta(H)>=4`.  Since `C` is induced, each vertex of `C` has exactly its
two cycle neighbours inside `C`, and therefore has a neighbour outside
`C`.  Thus

\[
                         R=H-V(C)                       \tag{2.1}
\]

is nonempty and connected, and every vertex of `C` has a neighbour in
`R`.

Read the five terminals of `T` in their cyclic order on `C`.  Partition
`C` into five vertex-disjoint path bags by assigning to each terminal the
oriented arc starting at it and ending immediately before the next
terminal.  These bags are connected, are rooted at the five terminals,
and consecutive bags are adjacent.  They therefore form a rooted
five-cycle in `H`.

Apply Theorem 2.1 of
[`hc7_cross_arm_overlap_four_cycle_decoder.md`](hc7_cross_arm_overlap_four_cycle_decoder.md).
For ten of the twelve cyclic orders, the decoder gives either a direct
`K_7` model or the common rooted-`K_4` outcome, which again gives `K_7` by
the three-rooted composition theorem.

It remains to consider one of the two crossed orders.  After possibly
interchanging `p,q`, write it as

```text
l_1,l_2,r,6,s.
```

The only decoder residue has the four fixed gate defects

```text
l_1 6,   l_1 r,   l_2 6,   l_2 s.
```

Let `B_6` be the cycle bag rooted at `6`, and replace it by

\[
                            B_6'=B_6\cup R.             \tag{2.2}
\]

This is a connected bag: `R` is connected and contacts every vertex of
`C`, hence it contacts `B_6`.  It is disjoint from the other four cycle
bags.  Moreover, `R` contacts every one of those bags, so `B_6'` is
adjacent to all four of them.  In particular, (2.2) supplies the virtual
adjacencies `l_1 6` and `l_2 6`.

The crossed-frame certificate is edge-maximal in each of its four fixed
gate defects: supplying any one of them gives an explicit `K_7` model in
all twenty-seven residual states.  Supplying `l_1 6` through the actual
bags `B_{l_1}` and `B_6'` therefore closes the residue.  The decoder's
branch-set lift replaces terminal labels by these literal rooted bags, so
no virtual edge is being treated as an edge of `G`.

Every possible cyclic order has now produced a `K_7` minor.  \(\square\)

## 3. Exact separator corollary

Call a connected subgraph `P` of an open shore with boundary `S`
**`S`-full** if every literal vertex of `S` has a neighbour in `P`.

### Corollary 3.1

If `G` has no `K_7` minor, then there is a three-vertex cut `Z` of `H`
such that

\[
                              S=I\cup Z                 \tag{3.1}
\]

is an actual order-seven separator of `G`.  Every component of `G-S` is
an `S`-full packet.  Consequently, any partition of the components of
`G-S` into two nonempty classes gives an actual seven-separation whose
two open shores each contain an `S`-full packet.

#### Proof

By Theorem 2.1, `H` is not four-connected.  Lemma 1.1 says that it is
three-connected, so it has a vertex cut `Z` of order exactly three.
Since `Z subseteq V(H)` is disjoint from `I`, the set `S=I union Z` has
order seven, and

\[
                         G-S=H-Z
\]

is disconnected.  Choosing any nonempty proper union of its components
as one open shore, and the remaining components as the other, gives an
actual separation with literal boundary `S` and two nonempty open shores.

Let `D` be a component of `G-S`.  Its external neighbourhood is contained
in `S`.  If some `s in S` had no neighbour in `D`, then

\[
                         N_G(D)\subseteq S-\{s\}
\]

would have order at most six.  Deleting `N_G(D)` separates the nonempty
component `D` from any other component of `G-S`, contradicting
seven-connectivity.  Hence every literal member of `S` has a neighbour in
`D`; the connected graph `D` is an `S`-full packet.

This proves the packet assertion.  It does not select a returned colouring
state, determine the exact packing vector, or make the handoff strict.
\(\square\)

### Corollary 3.2 (critical packet normalization)

Assume additionally that `G` is strongly seven-contraction-critical:

\[
 \chi(G)=7\quad\hbox{and every proper minor of }G\hbox{ is
 six-colourable}.                                      \tag{3.2}
\]

Then `H-Z` has exactly two or three components.  Every grouping of its
components into two nonempty open shores, after orientation, has packet
vector

```text
(1,1) or (1,2).
```

This remains an unranked handoff.  It does not supply an attained boundary
colouring state or identify a packet-thin component with any pre-existing
named shore or labelled local object.

#### Proof

Use the cut `Z` from Corollary 3.1.  Let its components be
`C_1,...,C_m`.  Each `C_i` is an `S`-full packet, so `m>=2`.  If `m>=4`,
put two components in one open shore and all remaining components in the
other.  Each shore then contains at least two disjoint `S`-full packets,
contradicting the independently audited exact-seven packet theorem,
which says that the smaller of the two packet maxima equals one.  Hence

\[
                              m\in\{2,3\}.              \tag{3.3}
\]

For precision, let `c_i` be the maximum number of disjoint `S`-full
packets contained in `C_i`.  A connected packet cannot use two distinct
components of `G-S`, so the packet maximum of a union of components is
the sum of their `c_i`.

If `m=3` and some `c_i>=2`, orient the separation with `C_i` on one side
and the other two components on the other.  Both packet maxima would be at
least two, again contradicting the exact-seven packet theorem.  Thus
`c_1=c_2=c_3=1`, and grouping one component against the other two gives
the exact vector `(1,2)`.

If `m=2`, the exact-seven packet theorem leaves the vectors `(1,1)`,
`(1,2)`, and `(1,3)`, up to orientation.  The independently audited
adaptive `(1,3)` packet-reflection theorem excludes the last vector under
(3.2): one full packet on one shore and three on the other yield either a
literal `K_7` or two proper-minor colourings with the same exact boundary
partition, hence a six-colouring of `G`.  Both alternatives contradict
the present hypotheses.  Therefore only `(1,1)` and `(1,2)` remain.
\(\square\)

## 4. Dependencies and trust boundary

The proof uses:

1. Fabila-Monroy--Wood, *Rooted `K_4`-Minors*, Theorem 6;
2. the standard peripheral-cycle theorem for three-connected plane
   graphs;
3. the independently audited overlap-four rooted-`K_4` decoder;
4. the independently audited overlap-four five-terminal cycle decoder;
   and
5. the independently audited three-rooted small-`K_4` composition
   theorem;
6. for Corollary 3.2 only, the independently audited exact-seven packet
   theorem; and
7. for exclusion of its `(1,3)` branch, the independently audited adaptive
   packet-reflection theorem.

The conclusion is an infinite-family closure: no four-connected exterior
survives.  In the `K_7`-minor-free branch it exposes an actual
exact-seven, componentwise-full packet interface.  It does **not** close
that interface or prove the support-six transversal theorem.
