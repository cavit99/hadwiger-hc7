# Exact-block responses do not connect opposite shore languages

**Status:** written finite barrier with deterministic verifier; realization
strengthening proved from Dvořák--Swart; separate internal audit GREEN in
[`hc7_order9_operation_response_reconfiguration_barrier_audit.md`](hc7_order9_operation_response_reconfiguration_barrier_audit.md).
This is not a counterexample to `HC_7`.

This note separates two facts which must not be conflated in the order-nine
two-shore programme:

1. every independent boundary set can occur as an exact colour class in a
   colouring extending through either shore; and
2. the colourings returned by proper-minor operations form a connected set
   in the single-vertex reconfiguration graph.

The first assertion, even when its witnesses are attached to designated
edge deletions and contractions in actual connected boundary-full shores,
does not imply the second.

## 1. A finite boundary barrier

Let `H` be the eight-vertex forest

\[
       H=3K_2\mathbin{\dot\cup}2K_1,
\tag{1.1}
\]

with edges `04,13,56` and isolated vertices `2,7`.  Its graph6 code is
`GA_?G?`.  Let `Omega` be the equality partitions induced by proper
five-colourings of `H`; unused colours are allowed.  Two members of `Omega`
are **one-vertex adjacent** when they are induced by two labelled proper
five-colourings which differ at exactly one literal vertex.

Let `L` consist of

- every proper partition of `V(H)` into five nonempty blocks; and
- for every independent five-set `I`, the four-block partition consisting
  of `I` and the three singleton vertices of `V(H)-I`.

Let `R` consist of every proper partition into at most three nonempty blocks
which is not one-vertex adjacent to any member of `L`.

### Theorem 1.1 (finite partition barrier)

The families `L,R` have the following properties.

1. They are nonempty and disjoint.  Every proper surjective five-colouring
   of `H` induces a member of `L`, and none induces a member of `R`.
2. For every nonempty independent set `I` of `H`, each of `L,R` contains a
   partition having `I` as an exact block.
3. No member of `L` is one-vertex adjacent to a member of `R`.
4. The full single-vertex five-colouring graph of `H` is connected.

The exact finite counts are

\[
\begin{array}{c|c}
\text{object}&\text{count}\\ \hline
\text{proper partitions with at most five blocks}&1834\\
\text{five-block partitions}&674\\
\text{independent five-sets}&8\\
|L|&682\\
|R|&300\\
\text{nonempty independent sets}&107\\
\text{one-vertex adjacency edges}&20232.
\end{array}
\tag{1.2}
\]

#### Proof

All statements except item 4 are the finite assertions checked by the
deterministic verifier.  The definitions make the disjointness and the
absence of an `L`--`R` edge immediate; the substantive finite assertion is
that both families meet every exact-block query.

For item 4, repeatedly delete a vertex of degree at most one.  The standard
five-colour lifting argument applies: lift a single-vertex recolouring path
from the smaller graph, temporarily recolouring the deleted vertex whenever
its current colour would obstruct the next move.  If the next move recolours
the unique possible neighbour from `a` to `b`, first give the deleted vertex
a colour different from both `a` and `b`; three such colours remain
available.  The one-vertex graph is trivially connected.  Induction proves
the assertion.
\(\square\)

Thus connectivity of the ambient recolouring graph does not help unless the
operation-attained traces themselves enter the connecting path.  Here every
full trace belongs to `L`, while `R` answers all exact-block queries only at
palettes of order at most three.  Every path from `R` to `L` therefore runs
through boundary traces belonging to neither language before it reaches
`L`.

## 2. Actual connected full shore realizations

The finite barrier is not merely a formal set system.  We next realize it
by actual graph colour-extension relations.

Add a new vertex `d` complete to `H`, and put

\[
                         F=K_1\vee H,
             \qquad S=V(F).
\tag{2.1}
\]

For `C in {L,R}`, let `C^+` be the equality partitions of `S` obtained by
adjoining the singleton block `{d}` to a member of `C`.  Take all labelled
six-colourings inducing these partitions.  This is a set of six-colourings
closed under every permutation of the six colour names.

Dvořák--Swart, Theorem 3 of *A note on extendable sets of colorings and
rooted minors* (arXiv:2504.07764), says that every such permutation-closed
boundary-colouring relation has a finite graph realizer.  Applying their
theorem to `L^+` and `R^+`, adding the edges of `F` on the common boundary,
and using the connected-full augmentation below gives two actual closed
shores whose exact boundary extension relations are `L^+` and `R^+`.

The augmentation is elementary.  Add an open vertex `c`; for every
`s in S`, add a new length-two path `s-l_s-c`; and join `c` by a new
length-two path to one selected vertex of every old open-interior component.
Every old six-colouring extends, because each new middle vertex has to avoid
at most two colours.  Conversely every colouring of the augmentation
restricts to the old realizer.  The relation is unchanged, while the open
interior becomes connected and adjacent to every literal member of `S`.

There is no hidden extra boundary edge.  For every nonedge `xy` of `F`, the
set `{x,y}` is an independent set of `H`, and both languages contain a
partition having it as a block.  Hence no realizer admitting the prescribed
relation can contain `xy`.  The edges added on `S` therefore induce exactly
`F`.

Gluing the two closed shores on `S` produces a graph which is not
six-colourable: a six-colouring would induce one boundary partition in both
disjoint relations.  The open shores are connected, anticomplete, and full
to the literal nine-vertex boundary.  Nevertheless there is no common
trace and no one-vertex transition from one shore language to the other.

## 3. Designated deletion and contraction responses

The realization can be strengthened so that every trace of the opposite
language is returned by a designated internal edge operation.  We give the
construction because this is the exact distinction between static anchors
and operation-coupled anchors.

Let `Omega_F` be all proper equality partitions of `F` into at most six
blocks.  Fix `tau in Omega_F-C^+` and introduce two new vertices
`u_tau,v_tau`.  On the enlarged boundary
`S union {u_tau,v_tau}`, prescribe the following permutation-closed relation:

- when the partition on `S` is `tau`, require
  `u_tau,v_tau` to have equal colours;
- for every other member of `Omega_F`, require them to have distinct
  colours.

Dvořák--Swart realizes this relation.  The realizer cannot already
contain `u_tau v_tau`, because it admits a colouring in which those two
vertices are equal.  Add the edge

\[
                         e_\tau=u_\tau v_\tau.
\tag{3.1}
\]

With `e_tau` present, the gadget accepts every proper boundary partition
except `tau`.  Take the union, intersecting their extension relations, of
one such gadget for every `tau in Omega_F-C^+`, with different control
vertices and with only `S` shared.  The intact union realizes exactly
`C^+`.

Deleting `e_tau` makes its gadget accept every member of `Omega_F`; all
other gadgets already accept `tau`.  Hence the operated union realizes
`C^+ union {tau}`.  Contracting `e_tau` forces its ends equal, so the
operated gadget, and therefore the whole union, realizes exactly `tau`.
The connected-full augmentation preserves these conclusions after either
operation, since every colouring of the old operated graph extends over
the new length-two paths.

Apply this controlled construction to both shores.  For every
`tau in R^+`, the `L^+`-shore has an internal edge whose deletion or
contraction makes `tau` extend there, and it already extends through the
intact `R^+`-shore.  Thus both proper minors of the glued graph are
six-colourable.  Symmetrically, every member of `L^+` is an
operation-specific response at a designated edge in the `R^+`-shore.
In particular, every exact independent-block query on either orientation
can be represented by a genuine deletion and contraction response from the
opposite orientation.

The intact glued graph has chromatic number exactly seven.  It is not
six-colourable by disjointness of the relations.  Choose a partition `tau`
in the nonempty opposite shore language and delete the displayed control
edge for `tau`.  The resulting graph has a six-colouring, and recolouring
one endpoint of that edge with a seventh colour gives a seven-colouring of
the intact graph.

## 4. Exact trust boundary

The construction proves that the following information does not by itself
force a common trace or an ownership-changing one-vertex transition:

- a `K_5`-minor-free eight-vertex residual boundary;
- connected open shores adjacent to every literal boundary vertex;
- connectedness of the full five-colouring reconfiguration graph;
- every independent boundary set attained exactly from both orientations;
  and
- designated internal edge deletions and contractions returning all
  opposite-language anchor traces.

The constructed host is **not** asserted to be seven-connected,
`K_7`-minor-free, or six-colourable after every proper minor.  The controlled
realizers may contain a `K_7` minor or expose a full-neighbourhood separator
of order at most seven.  Dvořák--Swart supplies `K_8`-minor exclusion and an
`S`-rooted-`K_7` exclusion for each individual primitive realizer, but these
properties are not preserved by the union and gluing used here and are not
claimed for the final host.

Consequently this barrier does not refute a theorem whose alternatives
include an explicit `K_7`-minor model or an order-at-most-seven
full-neighbourhood separator.  It shows exactly why those geometric
alternatives, or a much stronger connectivity theorem for the entire set of
proper-minor response traces, are indispensable.  Isolated
operation-specific anchors are not a substitute for such a theorem.

## 5. Verification

Run

```sh
python3 barriers/hc7_order9_operation_response_reconfiguration_barrier_verify.py
```

The checker enumerates every proper partition, every independent set, and
every one-vertex partition adjacency.  Its final line is

```text
PASS partitions=1834 full=674 maximum_independent=8 left=682 right=300 anchors=107 adjacencies=20232
```
