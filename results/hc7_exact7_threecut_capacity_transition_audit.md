# Audit: a capacity transition at a support-four three-gate

**Final verdict:** GREEN.  The repaired mathematical source was audited at
SHA-256
`2f9ebdf3a6dd795cf47f14c503901d53d39e25401f7f719cd0dd459c722d5afd`.
The promoted source has SHA-256
`e1508484bee951b55e5595f6a7a55166ed6aeb13d4a8c984dcda07fb693bfbce`;
the only intervening edit changes the status line from draft to audited.

The false converse identified in the first audit has been removed from the
unqualified statement.  Lemma 3.1 now states the valid forward implication
and restricts its converse to resource partitions in which each class
contains a lobe.  Every downstream use needs only the forward implication.
The new Lemma 5.3 correctly eliminates the gate-centred star by a literal
five-vertex cut.

The theorem remains a state-free transition: it does not transport an
equality partition across the descended boundary and does not claim that
every remaining matching-one support pattern lacks some other near-model
construction.

## 1. Repaired capacity lemma

### 1.1 Matching implies carrier split

Every capacity edge has a real lobe endpoint: it is either a lobe-dummy,
lobe-lobe, or lobe-gate edge.  Two disjoint capacity edges therefore seed
two resource classes, each already containing a distinct lobe and each
having support at least five.

At most one gate lies on each matching edge.  The three literal gates can
therefore be distributed so that each class contains a gate.  Since every
lobe meets every gate, each class union is connected.  A lobe in either
class meets a gate in the other, so the two unions are literally adjacent.
Assigning all remaining real resources preserves connectedness, adjacency,
and the support lower bounds.  The classes partition `L`; because `L` is
`S`-full, their supports cover `S`.

Thus the forward half of Lemma 3.1 is correct.  Together with the fixed
adjacent full packets `P,Q` and the allowed boundary graph, the audited
two-defect anchored theorem gives the claimed labelled `K_7^vee` model.

### 1.2 Qualified converse

Suppose a carrier resource partition satisfies (3.3) and each class
contains a lobe.  Choose one lobe `D` in each class.

* If `|sigma(D)|>=5`, its private dummy edge is a capacity witness.
* Otherwise lobe support is exactly four.  Since the support union of its
  class has order at least five, another real resource `Z` in that class
  contributes a label outside `sigma(D)`, so `DZ` is a capacity edge.

The two selected edges are disjoint because their real endpoints lie in
disjoint resource classes and all dummies are private.  This proves the
qualified converse exactly as stated.

### 1.3 Previous falsifier is now absorbed

The first audit exhibited an exactly seven-connected nineteen-vertex
architecture whose capacity graph is the triangle `D,E,t_1`, while

\[
 X=\{t_1\},\qquad Y=L-\{t_1\}
\]

is a valid near-full carrier split.  That architecture no longer refutes
Lemma 3.1: the class `X` contains no lobe, precisely the case excluded from
the converse.  The repaired text also explicitly says that gate-only
carriers are not encoded by `C_T`.  This is the correct trust boundary.

## 2. Capacity matching obstruction

Lemma 3.2 remains correct.  If `C_T` were empty, every lobe would have
support exactly four, all lobe supports would be the same four-set, and
every gate support would lie in that set.  Their union could not be all of
`S`, contradicting fullness of `L`.

A nonempty simple graph with matching number one has non-isolated part a
star or triangle.  The proof using a fixed edge and two possible crossing
edges is complete.  The repaired title and conclusion correctly call this
an exact **matching** obstruction rather than a complete characterization
of carrier splits.

## 3. Literal constructions and packet transition

The checks from the initial audit remain unchanged.

### 3.1 Barrier `K_7`

The three bags

\[
 \{x,z_1\},\quad\{y,z_2\},\quad\{z_3\}
\]

are connected and pairwise adjacent through the three gate rows.  The
four outer bags

\[
 \{b_1\},\quad\{b_2\},\quad
 \{b_3,a_2,q\},\quad\{a_3,a_1,p\}
\]

are disjoint, connected, and pairwise adjacent by the boundary triangles,
crossed edges, packet fullness, and `pq`.  The recorded literal portal
lists supply every cross adjacency.  These are seven literal clique branch
sets; no web-completion or quotient edge is used.

### 3.2 Exit matching

A self-full sibling is itself `Omega`-full.  For a non-self-full sibling
`J`, its exit set in the three-set `B` is nonempty, and

\[
 F\cup\{b\}\cup J
\]

is connected and `Omega`-full for any old full packet `F` and any
`b in E(J)`.  Two self-full siblings, one self-full sibling plus another,
or two distinct exit representatives yield two disjoint packets.  Failure
for at least two siblings forces every exit set to be the same singleton.

In that common-exit case, choose distinct siblings `J_1,J_2`.  The edges

\[
 D_0J_1,\qquad J_2t
\]

are disjoint capacity edges: the first support union is `A union {b}`, and
the second is certified by a label `b' in B-{b}` which fullness forces onto
a gate.  Only the valid forward half of Lemma 3.1 is invoked.

### 3.3 Strict packet-vector descent

Theorem 5.1 is an exhaustive, nonexclusive trichotomy.  With at least two
siblings, exit matching yields either the two-packet descendant or the
common-exit near model.  With one sibling, a capacity matching gives the
near model; otherwise Lemma 3.2 gives the two-lobe matching-one residue.

In the two-packet outcome, `D_0` is a nonempty connected `Omega`-full shore
strictly smaller than `L`, and the opposite shore contains at least two
disjoint full packets.  The exact-seven packet theorem forces vector
`(1,2)` or `(1,3)` with `D_0` first.  Audited adaptive reflection eliminates
`(1,3)`, leaving a strict `(1,2)` transition.  No packet adjacency or state
pullback is silently assumed here.

## 4. Two-lobe normal forms

Lemma 5.2 remains exhaustive conditional on the matching-one item.

* A capacity triangle cannot use two gates, because gate-gate edges are
  absent, or a dummy, because a dummy has degree one.  It is therefore
  exactly `D_0,E,t`; both lobe supports have order four, and every unused
  gate support lies in their intersection.
* In a gate-centred star, absence of the lobe-lobe edge forces the two
  four-supports to agree, and the centre gate is the unique resource
  carrying labels outside that four-set.
* In a `D_0`-centred star, `E` has no dummy and hence has support four;
  all gate supports lie in `A(E)`, the lobe-lobe edge is present, and
  fullness gives `A union A(E)=S`.
* In an `E`-centred star, every gate support lies in `A`, the lobe-lobe edge
  is present, and fullness again gives union `S`; the private dummy at `E`
  is allowed.

The possible one-edge star is correctly handled by choosing a real lobe
endpoint as centre, and the lobe-centred descriptions need not be disjoint.

## 5. New gate-star five-cut

Lemma 5.3 is GREEN.  In the gate-star form, both lobes have common support
`A`, every gate other than the centre `t` has support inside `A`, and `t`
is the unique resource meeting `S-A`.  Therefore after deleting

\[
                         A\cup\{t\},
\]

no surviving vertex of `L-{t}` has a neighbour in `S-A`.  All vertices of
`A` have been deleted, and the old separation has no `L-R` edge.  Hence the
nonempty set `L-{t}` is separated from the nonempty old shore `R` by five
vertices, contradicting seven-connectivity.

There is no hidden assumption that `L-{t}` is connected: at least one of
its components is separated, which is enough.  It is nonempty because the
two lobes are nonempty.

## 6. Exact promoted scope

The repaired theorem proves:

* every support-four three-cut with at least three lobes gives a labelled
  near-model handoff or a strict packet-vector `(1,2)` descent; and
* in the two-lobe matching-one branch, the gate-centred star is impossible,
  leaving only the two lobe-centred star descriptions and the capacity
  triangle.

Those remaining patterns may still admit a gate-only carrier split or a
different labelled near model.  The theorem correctly does not claim the
contrary.  Equality-state selection across the strict descent and the
remaining two-lobe dynamic transition are still open obligations.
