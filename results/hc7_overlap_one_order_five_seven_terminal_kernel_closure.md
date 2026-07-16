# Seven-terminal kernel closure at overlap one

**Status:** computer-assisted local theorem; independently audited **GREEN**
in
[`hc7_overlap_one_order_five_seven_terminal_kernel_closure_audit.md`](hc7_overlap_one_order_five_seven_terminal_kernel_closure_audit.md).
This closes the normalized irredundant order-five-arm, overlap-one cell
stated below.  It does not prove the support-six transversal theorem or
`HC_7`.

The finite verifier is
[`../active/hc7_overlap_one_order_five_kernel_probe.py`](../active/hc7_overlap_one_order_five_kernel_probe.py).
The audit uses the separate verifier
[`../active/hc7_overlap_one_order_five_seven_terminal_kernel_verify.py`](../active/hc7_overlap_one_order_five_seven_terminal_kernel_verify.py),
which regenerates the local relation and returns and validates literal
branch-set witnesses.
It uses the exact six-support relation from
[`../active/hc7_cross_arm_overlap_three_kernel_decoder.py`](../active/hc7_cross_arm_overlap_three_kernel_decoder.py)
and the independently audited seven-terminal catalogue in
[`hc7_seven_terminal_irreducible_kernel_classification.md`](hc7_seven_terminal_irreducible_kernel_classification.md).

## 1. Normalized labelled cell

Use the literal labels

```text
A={0,1,2,3,4,5},       I=A cap X={0},
X={0,6,7,8},            p=9, q=10,
T={1,2,3,4,5,6,7,8,9,10}.
```

Let `G` be seven-connected.  Assume that

```text
A, (A-{0})+p, (A-{0})+q
```

are irredundant supports of spanning `K_5` models and that

```text
X+p, X+q
```

are literal `K_5` cliques.  On six vertices, irredundancy says exactly
that the spanning `K_5` model has one two-vertex edge-bag and four
singleton bags but no literal `K_5`; there are 375 labelled induced
edge/nonedge relations of this form.

Join the three exact relations on their common literal edge variables and
fix every edge in the two literal cliques.  No other edge is completed.  A
joined state is **common** when `A-{0}` contains a support-at-most-five
rooted `K_4` model every bag of which is contacted by all three of
`0,p,q`.  The audited three-rooted small-`K_4` composition theorem closes
every common state to a literal `K_7`.

## 2. Reserve three vertices before exposing the kernel

Put `H=G-0`.  This graph is six-connected.  For a three-set `R subseteq T`,
put

```text
J_R=H-R.
```

Then `J_R` is three-connected and contains the seven distinct terminals
`T-R`.  Terminal-legal contraction gives an irreducible rooted kernel of
order seven or eight.  The exact catalogue has the following safe
quantifiers.

1. In the order-seven branch, every one of the 5,495 labelled edge-minimal
   spanning three-connected carriers must close.
2. In the order-eight branch, every one of the 30,600 exact templates must
   have at least one actual neighbour of its extra bag which can absorb
   that bag and close the resulting owner quotient.

Thus `R` is chosen from the forced original-edge state before the unknown
kernel is exposed; an owner may be selected only after the actual
order-eight template is known.

## 3. Monotone finite reduction

The joined relation has exactly

```text
8,055 joined states,
2,645 common states,
5,410 noncommon states.
```

Composition uses only forced-present original edges and carrier edges.
Consequently it is monotone in the forced-present mask: if a certificate
closes a mask `F`, it closes every mask containing `F`.  It is therefore
enough to test the inclusion-minimal forced-present masks among the
noncommon states.

There are exactly 400 such masks, with edge-count profile

```text
29:10, 31:30, 33:360.
```

The category group

```text
Sym(A-I) times Sym(X-I) times Sym({p,q})
```

has order `5!*3!*2!=1,440`.  It preserves the support relation, literal
cliques, common predicate and kernel-composition question.  The 400 masks
form six full orbits, of sizes

```text
10, 30, 60, 60, 120, 120.
```

A reserve triple certified for one representative transports under the
same category permutation.  Hence six representatives suffice.

## 4. Exact finite composition

### Theorem 4.1

Every one of the six minimal-mask orbits is terminal.  One representative
admits the reserve triple

```text
{1,2,9},
```

and the other five admit

```text
{1,2,3}.
```

For each displayed reserve triple, every one of the 5,495 order-seven
carriers closes, and every one of the 30,600 order-eight templates has a
closing actual owner.  Therefore all 5,410 noncommon states are terminal;
together with the common branch, all 8,055 joined states are terminal.

The quotient has eleven objects:

```text
{0}, the three reserved singleton terminals,
and the seven terminal-rooted carrier bags.
```

The exact detector permits unused objects and arbitrary connected mergers.
Any seven-bag model on eleven objects has at least three singleton bags, so
enumerating every singleton clique of orders three through seven and every
compatible set of connected remaining bags is exhaustive.  Carrier edges
are added only in this quotient layer; they are never treated as literal
edges in a six-support relation.

The deterministic certificate digests are

```text
noncommon states:
bbcd05839b15cabb5a6d7b2ef1a7e3743154be9d12d3849903a80d479369a907

minimum masks:
1f62f3282bb2134f4e422cec810b280c059476a849d474db53f6c69129cf2343

order-seven catalogue:
16aad7592a7f5412ab7b254434ca7f02b6454b2a8ba644d962f9f283788edec1

order-eight owner catalogue:
0189701148e17b1f792e83ec1737f753c23b99dcb52c149808428602f12021e1

orbit/reserve certificates:
384761c399bd17b1c7d574801703236d3d50c8730af018e87458cbfd7511e033
```

Running the primary verifier with `--crosscheck` compares every one of its
6,578 queried quotient masks with the independent witness-returning detector.

## 5. Literal lift

### Theorem 5.1

Every seven-connected graph satisfying the normalized hypotheses of
Section 1 contains a `K_7` minor.

### Proof

The common branch was closed in Section 1.  Otherwise choose an
inclusion-minimal forced mask contained in the actual state, transport its
certified reserve triple from the appropriate category-orbit
representative, and form `J_R`.

Apply the terminal-legal kernel theorem.  In the order-seven branch retain
an edge-minimal spanning three-connected carrier.  In the order-eight
branch retain the exact template, choose its certified adjacent owner, and
unite the owner and extra preimage bags.  In both cases this yields seven
pairwise disjoint connected carrier bags in `J_R`, rooted at `T-R` and
disjoint from the four singleton objects `{0} union R`.

Every original quotient edge used by the certificate is a literal edge
between named roots.  Every carrier edge is an actual adjacency between
connected preimage bags.  Connected quotient mergers therefore lift to
connected unions, distinct quotient branch sets remain disjoint, and every
certified contact lifts.  The quotient `K_7` model is a literal `K_7`
model in `G`. \(\square\)

## 6. Trust boundary

Before selecting the critical high-transversal kernel, retain all
order-five supports and only order-six supports containing no retained
order-five support.  This preserves transversal number and makes every
subsequently used order-six support irredundant.

The theorem may be invoked globally only when the corrected private-pair
cross-arm reduction in that pruned family produces an avoided order-six
support `A`, literal order-five arms `X+p,X+q`, overlap exactly one, and the
two displayed replacement supports.  Under precisely those hypotheses the
entire normalized cell is closed.  The ambient graph remains unbounded;
only the labelled relation and terminal kernel are finite.

This result does not address order-six arms at overlap one, the separated
triple branch, or the global support-at-most-six transversal theorem.
