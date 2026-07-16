# Independent audit: seven-terminal kernel closure at overlap one

## Verdict

**GREEN.**  The theorem in
[`hc7_overlap_one_order_five_seven_terminal_kernel_closure.md`](hc7_overlap_one_order_five_seven_terminal_kernel_closure.md)
is valid for the exact normalized cell stated there.  It closes that
unbounded ambient-graph cell to a literal `K_7` minor.  It does not prove the
support-six transversal theorem or `HC_7`.

The primary verifier is
[`../active/hc7_overlap_one_order_five_kernel_probe.py`](../active/hc7_overlap_one_order_five_kernel_probe.py).
The independent verifier is
[`../active/hc7_overlap_one_order_five_seven_terminal_kernel_verify.py`](../active/hc7_overlap_one_order_five_seven_terminal_kernel_verify.py).
The second program does not import the first.  It regenerates the local
relation, uses a different natural join and generator-orbit traversal, and
returns literal branch-set witnesses for every positive `K_7` decision.

## 1. Exact normalized relation

The labels are

```text
A={0,1,2,3,4,5},  I={0},  X={0,6,7,8},  p=9, q=10.
```

The two sets `X+p` and `X+q` are fixed literal `K_5` cliques.  The three
six-sets

```text
A, (A-{0})+p, (A-{0})+q
```

are irredundant supports of spanning `K_5` models.  On six vertices such a
model uses one two-vertex connected bag and four singleton bags.  Conversely,
an edge-bag, a singleton `K_4`, and one contact from the edge-bag to each
singleton give the model.  Excluding a literal `K_5` gives exactly 375 complete
labelled edge/nonedge relations.

The primary program imports the previously used 375-relation.  The independent
program regenerates it by examining all `2^15` six-vertex edge masks and
checking the displayed condition directly.  It then joins the three supports
in a fixed order, rather than using the primary program's recursive
minimum-domain join.  Both computations give

```text
8,055 joined states,
2,645 common states,
5,410 noncommon states.
```

The common predicate was also reimplemented independently: it enumerates every
four-bag model supported on four or five vertices of `A-{0}` and checks literal
contacts from all of `0,p,q`.  This is exactly the hypothesis of the audited
three-rooted small-`K_4` composition theorem.  Thus the common branch is
legitimately terminal.

The deterministic digest of the complete noncommon state list is

```text
bbcd05839b15cabb5a6d7b2ef1a7e3743154be9d12d3849903a80d479369a907.
```

## 2. Monotone reduction and symmetry

The final composition uses only forced-present original edges.  Its truth is
therefore monotone under adding original edges.  Every one of the 5,410
noncommon states contains one of exactly 400 inclusion-minimal forced-present
masks.  Their edge-count profile is

```text
29:10, 31:30, 33:360.
```

The minimum-mask digest is

```text
1f62f3282bb2134f4e422cec810b280c059476a849d474db53f6c69129cf2343.
```

The exact category group is

```text
Sym({1,2,3,4,5}) x Sym({6,7,8}) x Sym({9,10}),
```

of order `1,440`.  It fixes `0` and preserves all three support constraints,
both literal cliques, and the common predicate.  The primary program enumerates
all 1,440 images.  The independent program instead closes orbits under adjacent
transposition generators.  Both partition all 400 masks into six full orbits
of sizes

```text
10, 30, 60, 60, 120, 120.
```

No minimum is omitted, two orbits do not overlap, and the monotone cover of all
5,410 noncommon states is asserted directly.

## 3. Connectivity and kernel quantifiers

Put `H=G-0`.  Seven-connectivity of `G` makes `H` six-connected.  After a
reserve triple `R` is selected from the ten vertices `T={1,...,10}`, the graph

```text
J_R=H-R
```

is three-connected and contains the seven protected terminals `T-R`.
Terminal-legal contraction therefore yields an irreducible rooted kernel of
order seven or eight.

The reserve triple is selected from the original forced-edge orbit before the
kernel is exposed.  The finite test uses the correct quantifiers:

* every one of the 5,495 labelled edge-minimal order-seven carriers must close;
* for every one of the 30,600 labelled order-eight templates, at least one
  actual neighbour of the extra vertex may be selected as its owner.

The catalogue profiles are

```text
order seven edges: 11:5040, 12:455;
order-eight owner-family sizes: 4:2520, 5:10080, 6:12600, 7:5400.
```

Their deterministic digests are

```text
order seven:
16aad7592a7f5412ab7b254434ca7f02b6454b2a8ba644d962f9f283788edec1

order eight:
0189701148e17b1f792e83ec1737f753c23b99dcb52c149808428602f12021e1.
```

These are the complete catalogues from the independently audited exact
seven-terminal kernel classification.  The dynamic guard lists merely reject
bad reserve triples early; they do not replace either universal catalogue
loop.

## 4. Exact `K_7` detection

The quotient has eleven objects: the singleton `{0}`, three reserved singleton
vertices, and seven rooted carrier bags.  Seven nonempty disjoint branch sets
on eleven objects have at least three singleton branch sets.  Indeed, if `s`
of the seven bags are singletons, their total size is at least

```text
s+2(7-s)=14-s,
```

so `14-s<=11` gives `s>=3`.

The primary detector exhausts singleton clique sizes seven down to three.  For
each singleton clique it enumerates every connected subset of the remaining
objects which meets every singleton, then searches every pairwise disjoint,
pairwise adjacent collection of the required size.  Unused quotient objects
are permitted.  This proves both directions of the detector.

The independent detector is a separate implementation.  It returns the seven
bit-mask bags rather than a Boolean, and after every positive decision checks
directly that:

1. there are seven nonempty pairwise disjoint bags;
2. every bag is connected; and
3. every pair of bags has a quotient edge between it.

With the primary verifier's `--crosscheck` option, the two implementations
agreed on every one of the 6,578 distinct quotient masks queried by the
complete CEGAR run, including all negative guard decisions.  Thus the closure
does not rely on an unvalidated Boolean false positive.

## 5. Exhaustive closure

The six orbit representatives admit reserve triples

```text
orbit 0: {1,2,9};
orbits 1--5: {1,2,3}.
```

For each representative and its displayed triple, all 5,495 order-seven
carriers close and all 30,600 order-eight owner families have a closing owner.
The category action transports the reserve triple and the quotient model to
every mask in that representative's full orbit.  Monotonicity transports it
further to every noncommon state containing that mask.

The representative/orbit/reserve certificate digest is

```text
384761c399bd17b1c7d574801703236d3d50c8730af018e87458cbfd7511e033.
```

The independent verifier reproduces the same six representatives, orbit
sizes, reserve triples, catalogue counts, and all five digests.

## 6. Literal lift and trust boundary

Kernel preimages are connected, mutually disjoint, and contain their distinct
named terminals.  In the order-eight branch the extra preimage bag is adjacent
to its selected owner bag, so their union is connected.  Each forced original
edge is a literal edge between named roots, and each carrier edge is an actual
contact between kernel preimage bags.  A connected quotient merger therefore
lifts to a connected branch set, distinct quotient bags stay disjoint, and all
certified adjacencies lift.  The returned quotient model is consequently a
literal `K_7` minor in `G`.

This audit establishes only the normalized overlap-one, order-five-arm cell.
Its global use still requires the pruned high-transversal reduction to supply
the displayed avoided support, literal arms, and replacement supports.  It
does not treat the overlap-one order-six-arm cell, the separated-triple branch,
or the global support-at-most-six transversal theorem.
