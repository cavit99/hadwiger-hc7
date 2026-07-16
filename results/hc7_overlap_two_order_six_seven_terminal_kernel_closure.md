# Seven-terminal kernel closure at overlap two

**Status:** computer-assisted local theorem; independently audited **GREEN**
in
[`hc7_overlap_two_order_six_seven_terminal_kernel_closure_audit.md`](hc7_overlap_two_order_six_seven_terminal_kernel_closure_audit.md).
This closes the normalized irredundant order-six-arm, overlap-two cell
stated below.  It does not prove the support-six transversal theorem or
`HC_7`.

The finite verifier is
[`../active/hc7_overlap_two_order_six_adaptive_kernel_probe.py`](../active/hc7_overlap_two_order_six_adaptive_kernel_probe.py).
It uses the exact local relation from
[`../active/hc7_cross_arm_overlap_three_kernel_decoder.py`](../active/hc7_cross_arm_overlap_three_kernel_decoder.py),
the elementary connectivity helper in
[`../active/hc7_overlap_three_six_terminal_kernel_verify.py`](../active/hc7_overlap_three_six_terminal_kernel_verify.py),
and the proved exact seven-terminal kernel classification in
[`hc7_seven_terminal_irreducible_kernel_classification.md`](hc7_seven_terminal_irreducible_kernel_classification.md).

## 1. Normalized labelled cell

Use the literal labels

```text
A={0,1,2,3,4,5},       I=A cap X={0,1},
X={0,1,6,7,8},          p=9, q=10,
T={2,3,4,5,6,7,8,9,10}.
```

Let `G` be seven-connected.  Assume that each of the seven six-sets

```text
A, X+p, X+q,
(A-{0})+p, (A-{0})+q,
(A-{1})+p, (A-{1})+q
```

is an irredundant support of a spanning `K_5` model.  Irredundancy means
that none contains a literal `K_5`.  On six vertices a spanning `K_5`
model has one two-vertex edge-bag and four singleton bags.  There are
exactly `375` labelled edge/nonedge relations of this kind.

Join the seven exact relations on their common literal edge variables.
No other edge is completed.  A joined state is **common** when, for some
`i in I`, the five-set `A-{i}` contains a support-at-most-five rooted
`K_4` model every bag of which is contacted by all three of `i,p,q`.
The audited three-rooted small-`K_4` composition theorem makes every common
state terminal.

## 2. The reserve-before-kernel mechanism

Put

```text
H=G-I.
```

The graph `H` is five-connected.  For an unordered pair `R subseteq T`,
`|R|=2`, put

```text
J_R=H-R.
```

Then `J_R` is three-connected and contains the seven distinct terminals
`T-R`.  Apply the terminal-legal contraction theorem in `J_R`.  It returns
a terminal-rooted, terminal-irreducible three-connected minor `M` with

```text
7 <= |V(M)| <= 7+floor(7/4)=8.
```

The complete labelled guarantee has two cases.

1. If `|M|=7`, delete edges until three-connectivity is edge-minimal.
   There are five unlabelled and `5,495` labelled carriers on the seven
   terminal bags.
2. If `|M|=8`, write `x` for the unique nonterminal.  The exact structural
   theorem gives one of `30,600` labelled templates of wheel, one-chord,
   or two-chord type.  Once the actual template is known, **any** neighbour
   `w of x` may own `x`: unite the two adjacent preimage bags represented
   by `w,x`.  This gives the owner quotient

   ```text
   Q(M,w)=M[T-R]+{wu : u in N_M(x)-{w}}.
   ```

The pair `R` must be selected before the unknown kernel `M` is exposed.
The owner `w` may be selected afterwards.  Thus the safe quantifier is

```text
there exists R such that
  every order-seven carrier closes, and
  for every order-eight template some actual owner closes.
```

Neither a bare rooted `C_7` nor an arbitrary four-charge star has this
quantifier.  The verifier retains every terminal chord and the exact
neighbourhood of `x` from the structural classification.

## 3. Monotone reduction of the finite relation

### Lemma 3.1 (minimal forced-edge masks suffice)

Let `E(s)` be the forced-present original-edge mask of a noncommon joined
state `s`.  Let \(\mathcal M\) be the inclusion-minimal members of

```text
{E(s) : s is noncommon}.
```

If the kernel composition closes every mask in \(\mathcal M\), then it closes
every noncommon joined state.

### Proof

Given a noncommon state `s`, the finite nonempty set of noncommon masks
contained in `E(s)` has an inclusion-minimal member \(F\in\mathcal M\).
Every branch-set certificate using `F` and a rooted carrier remains valid
after adding the edges in `E(s)-F`.  Therefore any reserve pair which
closes `F` also closes `s`, with exactly the same universal quantifier over
kernel carriers and the same adaptive owner rule. \(\square\)

The exact joined relation has

```text
762,738 joined states,
614,250 common states,
148,488 noncommon states.
```

Every noncommon state leaves thirteen original edges unspecified.  Among
the noncommon forced-present masks there are exactly `8,220`
inclusion-minimal masks, with edge-count profile

```text
30:138, 31:3420, 32:4302, 33:360.
```

The category-preserving group is

```text
Sym(I) times Sym(A-I) times Sym(X-I) times Sym({p,q}),
```

of order `2!*4!*3!*2!=576`.  It preserves the seven local relations, the
common-state predicate, and the labelled composition question.  The
`8,220` minimal masks form exactly `67` orbits under this group.  For an
orbit image, the image of a certified reserve pair has the same universal
kernel property.  Hence it is enough to test one representative of each
of the `67` orbits.

## 4. Exact finite composition

### Theorem 4.1

Every one of the `67` minimal forced-edge orbits is terminal.  More
precisely:

```text
21 orbit representatives already contain a literal K7 model;
45 admit reserve pair {2,3};
 1 admits reserve pair {2,9}.
```

For each of the latter `46` representatives, its displayed reserve pair
has both properties below.

* Every one of the `5,495` labelled edge-minimal order-seven carriers on
  the remaining seven terminal labels composes with the forced original
  edges to a `K_7` model.
* For every one of the `30,600` labelled exact order-eight templates,
  at least one of its actual neighbours of `x` can own `x` so that the
  resulting seven-bag owner quotient composes with the forced original
  edges to a `K_7` model.

It follows by category symmetry and Lemma 3.1 that all `148,488`
noncommon states are terminal.  Together with the common branch, all
`762,738` joined states are terminal.

### Finite certificate

The verifier constructs the joined relation from the `375` local
relations, rather than importing a state list.  It checks the common
predicate, computes the inclusion-minimal forced masks, and verifies the
full category orbit of every representative.

The order-seven catalogue consists of every labelled edge-minimal simple
three-connected graph on seven vertices.  The order-eight catalogue is
generated from the three exact structural families; templates with the
same set of owner quotients may be deduplicated for computation, but the
universal check is logically over all `30,600` labelled templates.

The reproduced complete run reports

```text
closed minimal orbits: 67/67
order-seven catalogue: 5,495
exact order-eight families: 30,600
profile: direct 21, reserve {2,3} 45, reserve {2,9} 1
```

The independent verifier and audit reproduce the deterministic
state/catalogue/certificate digests recorded below; they are part of the
finite replay certificate, not a substitute for the structural proof.

The final quotient has eleven labelled objects:

```text
{0}, {1}, the two reserved singleton terminals,
and the seven terminal-rooted carrier bags.
```

Any seven-bag minor model on at most eleven objects has at least three
singleton bags.  The exact detector enumerates every singleton clique of
orders three through seven and then every collection of disjoint,
connected, pairwise adjacent remaining bags which is complete to that
singleton clique.  Unused quotient objects are allowed.  Carrier edges
are introduced only at the final composition layer and are never fed back
into a six-support relation.

Every one of the `176,081` distinct quotient masks queried by the closing
run was also tested by an independently implemented exact contraction
search.  The two `K_7` detectors agreed on every mask.  Deterministic replay
digests are

```text
noncommon states:
1a36036950bdad0d521ce65052f150ed7a878a5887dd295a13bda0cdaea05b92

minimal masks:
87f671250a4f36e1a1f5339a4136a71a6c4da437c651644d250aa9f2ae50a448

orbit representatives:
0b7f574707a7346aa816049bb8a3b63502019262fcecddc8da9be3dfbc487697

order-seven catalogue:
c3c80f979e41cffff8ae04d3bc82c04ca0b72e2f42bfe7b6b08964272c5b8724

order-eight owner families:
1df0164c93f886cc23ecac8dcb3646c6bc665a5ec77cb54a13a17bce711b2f8d

closure records:
5e4029b594fc0d7d69f28efa804e9261829c5d59c307758e2e28cc7a4254f677
```

## 5. Literal branch-set lift

### Theorem 5.1

Every seven-connected graph satisfying the normalized hypotheses of
Section 1 contains a `K_7` minor.

### Proof

If the state is common, use the audited three-rooted small-`K_4`
composition theorem.  Otherwise choose an inclusion-minimal forced mask
contained in its original-edge mask.  Transport the reserve pair certified
for its category-orbit representative back to the literal labels, and
form the three-connected graph `J_R`.

Apply the terminal-legal kernel theorem in `J_R`.  In the order-seven case,
retain an edge-minimal spanning three-connected subgraph.  Theorem 4.1
closes every such labelled carrier.  In the order-eight case, retain its
exact classified template and choose the adjacent owner certified for
that template by Theorem 4.1.  Unite the owner and nonterminal preimage
bags.

The resulting seven carrier bags lie in `J_R`, are pairwise disjoint, and
contain their seven distinct named terminals.  They avoid the four
singleton objects consisting of `I` and `R`.  Every original quotient edge
used by the certificate is a literal edge between named roots.  Every
carrier edge is an actual adjacency between connected preimage bags.
For an order-eight kernel, the owner merger is connected and transfers
exactly the contacts used by its owner quotient.

Replacing every quotient object by its connected preimage therefore
preserves disjointness, connectivity, and every certified inter-bag
adjacency.  The quotient `K_7` model lifts to a literal `K_7` model in
`G`. \(\square\)

## 6. Global normalization and trust boundary

Before choosing the critical transversal-three kernel, prune the support
family by retaining every order-five support and only those order-six
supports which contain no order-five support.  This preserves the
transversal number and ensures that every order-six support subsequently
used in a normalized cell is irredundant.

The theorem may be invoked globally only after the corrected private-pair
cross-arm theorem, applied to that pruned kernel, has produced:

* an avoided support `A` of order six;
* two rigid arms `X+p,X+q` of order six;
* overlap `A cap X` of order exactly two; and
* all four displayed replacement supports.

Under those hypotheses all seven supports in Section 1 are irredundant,
so Theorem 5.1 closes this entire rigid cell.  The conclusion is unbounded
in `|G|`; only the terminal-rooted kernel and the eleven-object
composition layer are finite.

The theorem does not address overlap one, the separated-triple branch, or
the global support-at-most-six transversal theorem.  The adjacent audit
independently reproduces the finite relation, monotone reduction, catalogue
and detector checks.
