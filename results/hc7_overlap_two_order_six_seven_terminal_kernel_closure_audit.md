# Audit of the overlap-two order-six kernel closure

## Verdict

**GREEN.**  The computer-assisted local theorem in
[`hc7_overlap_two_order_six_seven_terminal_kernel_closure.md`](hc7_overlap_two_order_six_seven_terminal_kernel_closure.md)
is correct under its stated normalized hypotheses.  The exact joined-state
census, common/noncommon split, monotone-minimum reduction, category
symmetry, order-seven and order-eight carrier catalogues, adaptive-owner
quantifier, `K_7`-minor detector, and literal lift were all checked
independently.

The complete replay found no counterstate.  This closes the stated
order-six-arm, overlap-two cell; it does not close overlap one, the
separated-triple branch, the support-six transversal theorem, or `HC_7`.

## 1. Independent reconstruction of the local relation

On six labelled vertices, a spanning five-bag model has exactly one
two-vertex bag and four singleton bags.  The two-vertex bag must induce an
edge, the four singleton vertices must induce a clique, and every singleton
must have an edge to the double bag.  Excluding every literal `K_5` gives
exactly `375` full edge/nonedge assignments.  An independent enumeration of
all `2^15` six-vertex masks reproduced this number without importing the
project's local-state list.

The seven normalized supports were then joined using a separate relational
join.  Each local assignment specifies all edges of its six-set, so the
independent implementation stored only the present-edge mask on the union
of the already processed supports and indexed the next relation by its exact
overlap assignment.  The intermediate state counts were

```text
375,
92,573,
409,847,
1,160,060,
4,023,248,
1,348,212,
762,738.
```

The union of the seven support edge sets contains `42` of the `55` possible
edges on eleven labels.  Thus every final joined state leaves exactly
thirteen edges unspecified, as claimed.

An independently written common-state test enumerated every four-bag model
on four or five vertices of `A-{i}` and checked literal contact from
`i,p,q` to every bag.  It returned

```text
joined states       762,738
common states       614,250
noncommon states    148,488.
```

Every noncommon state had a distinct forced-present mask.  These numbers
agree exactly with the canonical verifier.

## 2. Minimal masks and symmetry

The monotonicity argument in Lemma 3.1 is sound.  A certificate uses only
present original edges and carrier adjacencies.  Adding original edges
cannot destroy connected branch sets, their disjointness, or any required
inter-bag adjacency.  The reserve pair and the universal carrier checks are
therefore unchanged when a minimal present-edge mask is enlarged.

It is irrelevant that the absent-edge assignment belonging to a minimal
mask may differ from the absent-edge assignment of a larger state: no
absent edge is used by the composition certificate or by the kernel theorem.

Independent subset-minimality computation gave exactly `8,220` masks with
profile

```text
30 edges:  138
31 edges: 3420
32 edges: 4302
33 edges:  360.
```

The category group

```text
Sym({0,1}) x Sym({2,3,4,5}) x Sym({6,7,8}) x Sym({9,10})
```

has order `576`.  It preserves `A`, `X`, the unordered arm pair, all four
replacement supports, the local relation, and the common-state predicate.
It also maps terminal reserve pairs to terminal reserve pairs and merely
relabels each complete kernel catalogue.  Hence it preserves the exact
composition question.

For every independently computed minimal mask, all `576` images were
formed and checked to remain minimal.  They partition the `8,220` masks
into exactly `67` orbits.  The orbit-size profile was

```text
6:1, 18:1, 24:1, 36:9, 72:23, 144:23, 288:8, 576:1.
```

The orbit sizes sum to `8,220`.  Thus no orbit image is silently discarded
by the representative computation.

## 3. Reserve-before-kernel quantifier

Deleting `I={0,1}` from a seven-connected graph leaves the five-connected
graph `H`.  Once an unordered terminal pair `R` is reserved, `J_R=H-R` is
three-connected and contains the seven literal terminals `T-R`.  The
terminal-kernel theorem therefore applies exactly as stated.

The quantifier order used by the verifier is the safe one:

```text
there exists R such that
  every order-seven carrier closes, and
  for every order-eight template there exists a legal owner that closes.
```

The reserve pair is fixed before the unknown rooted kernel is exposed.  The
owner is chosen only after the exact order-eight template, including its
terminal chords and full extra-vertex neighbourhood, is known.  This is
precisely what owner absorption permits.

## 4. Independent carrier catalogues

### Order seven

An independent `geng` enumeration found the same five unlabelled
edge-minimal spanning three-connected graphs.  Relabelling them generated
`5,495` distinct masks, with profile

```text
11 edges: 5040
12 edges:  455.
```

The resulting mask set was compared directly with
`minimal_seven_terminal_carriers()` and was identical.  Every
three-connected graph on the seven terminal bags contains one of these as
an edge-minimal spanning subgraph, so universality over this catalogue is
complete.

### Order eight

The canonical generator reconstructs terminal-irreducible kernels from a
Hamilton cycle, the exact degree-two charged set, all permitted terminal
chords, and the exact neighbourhood of the extra vertex.  It then directly
checks three-connectivity and noncontractibility of every edge at the extra
vertex.  This produced `30,600` exact labelled kernels.

A second generator used only the three proved structural families—wheel,
one-chord, and two-chord—and independently generated all labelled
`(terminal mask, extra-neighbour mask)` pairs.  After forming every actual
owner quotient, the two generators produced identical sets of `30,600`
owner families.

Within a template, replacing duplicate owner quotients by a set is safe
because the required condition is existential over owners.  Across
templates, the canonical mapping to owner-family sets is in fact injective:

```text
number of exact kernels       30,600
number of owner-family sets   30,600.
```

Even without injectivity, deduplicating identical owner-family sets would
preserve the universal-template/existential-owner formula.  No template is
lost logically or computationally.

## 5. Exactness of the `K_7` detector

Seven nonempty disjoint branch sets on at most eleven quotient objects must
include at least three singleton branch sets.  If there are `s` singleton
bags, the other `7-s` bags use at least two objects each, so

```text
s+2(7-s) <= 11,
```

which gives `s>=3`.

`FastK7` enumerates every clique of three through seven possible singleton
bags.  Outside that clique it enumerates every nonempty connected subset
which contacts every singleton, and then every collection of the required
number of pairwise disjoint, pairwise adjacent such subsets.  Objects not
used by the model are allowed.  Therefore every returned certificate is a
literal branch-set model, and every possible seven-bag model is considered.
The detector is exact, not merely sufficient.

As a cold implementation check, the canonical verifier was run with
`--crosscheck`.  Every one of the `176,081` distinct quotient masks queried
while establishing the certificates was compared with the independent
recursive contraction detector in
[`../active/hc7_overlap_two_order_six_wheel_guardrail.py`](../active/hc7_overlap_two_order_six_wheel_guardrail.py).
All answers agreed.

That contraction detector is exact on this test set.  Every forced state
graph is connected: each local support contains a spanning `K_5` model, and
the seven supports overlap through `A` and `X`.  Adding carrier edges
preserves connectedness.  In a connected graph, any unused component of a
minor model's complement can be assigned along a spanning forest to one of
the model bags.  Hence a `K_7` model can be made spanning and obtained using
contractions alone.  The independent detector's omission of explicit
vertex deletion cannot create a discrepancy here.

## 6. Guards and complete finite outcome

The initial order-seven guard masks are all members of the complete
`5,495`-mask catalogue.  Any later order-seven guard is appended only after
being returned by that catalogue.  The order-eight guard list begins empty
and may receive only a family returned by the complete order-eight
catalogue.  A guard can therefore only reject a reserve pair earlier than
the full scan would reject it; it cannot accept a pair or create a false
positive.  Every accepted pair is subsequently tested against both complete
catalogues.

The cold full run reported

```text
adaptive full-kernel probe: no counterstate
minimal masks              8,220
minimal orbits                67
closed minimal orbits         67
order-seven catalogue      5,495
order-eight families      30,600
distinct detector masks  176,081
```

with the exact closure profile

```text
21 representatives: direct K7 model
45 representatives: reserve pair {2,3}
 1 representative: reserve pair {2,9}.
```

The run reproduced the canonical digests

```text
noncommon  1a36036950bdad0d521ce65052f150ed7a878a5887dd295a13bda0cdaea05b92
minima     87f671250a4f36e1a1f5339a4136a71a6c4da437c651644d250aa9f2ae50a448
orbits     0b7f574707a7346aa816049bb8a3b63502019262fcecddc8da9be3dfbc487697
order7     c3c80f979e41cffff8ae04d3bc82c04ca0b72e2f42bfe7b6b08964272c5b8724
order8     1df0164c93f886cc23ecac8dcb3646c6bc665a5ec77cb54a13a17bce711b2f8d
closure    5e4029b594fc0d7d69f28efa804e9261829c5d59c307758e2e28cc7a4254f677
```

## 7. Literal branch-set lift

The final eleven quotient objects are the singleton vertices of `I`, the
two reserved singleton terminals, and seven terminal-rooted carrier bags in
`J_R`.  The carrier bags avoid `I union R`, are pairwise disjoint and
connected, and contain their seven distinct literal terminal labels.

Every forced original quotient edge is an actual edge between named roots.
If a root lies in a carrier bag, that literal edge remains incident with the
bag.  Every carrier edge comes from an actual adjacency between two rooted
preimage bags and is introduced only in the composition layer.  It is never
fed back into a six-support relation.

For an order-eight kernel, the owner is adjacent to the extra kernel vertex,
so merging their preimage bags is connected.  The merged bag retains all
terminal-graph edges and gains exactly the contacts from the extra vertex to
its other neighbours.  This is precisely the owner quotient checked by the
finite certificate.

A connected quotient branch set lifts to the union of its connected object
preimages and the actual edges witnessing its quotient connectivity.
Different quotient branch sets use disjoint objects and hence disjoint
preimages.  Every certified inter-bag adjacency also has an actual witnessing
edge.  Thus each finite `K_7` certificate lifts to a literal `K_7` model in
`G`.

## 8. Trust boundary

The local theorem may be invoked only after the normalized rigid cell has
supplied all seven irredundant support-six relations.  Pruning an order-six
support which contains an order-five support is legitimate because that
larger support is redundant for every transversal; retaining all order-five
supports preserves the transversal number.  On six vertices, an internal
five-supported `K_5` model is necessarily a literal `K_5`, so the retained
order-six supports have exactly the irredundancy used by the `375`-state
relation.

No finite count here establishes that the global support kernel must enter
this cell.  Subject to the displayed normalized hypotheses, however, the
cell closure itself is complete and audited.
