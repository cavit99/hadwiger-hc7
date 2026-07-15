# Six-terminal kernel closure at overlap two

**Status:** computer-assisted local theorem; independently audited GREEN.
The theorem closes the normalized irredundant order-five-arm,
overlap-two cell stated below.  It does not prove the support-six
transversal theorem or `HC_7`.

The exhaustive verifier is
[`../active/hc7_overlap_two_order_five_six_terminal_kernel_verify.py`](../active/hc7_overlap_two_order_five_six_terminal_kernel_verify.py).
It uses the exact local relation from
[`../active/hc7_cross_arm_overlap_three_kernel_decoder.py`](../active/hc7_cross_arm_overlap_three_kernel_decoder.py)
and the independently audited six-terminal catalogue and exact `K_7`
detector in
[`../active/hc7_overlap_three_six_terminal_kernel_verify.py`](../active/hc7_overlap_three_six_terminal_kernel_verify.py).
All three programs use only the Python standard library.
The independent audit is
[`hc7_overlap_two_order_five_six_terminal_kernel_closure_audit.md`](hc7_overlap_two_order_five_six_terminal_kernel_closure_audit.md).

## 1. Normalized labelled cell

Use the literal labels

```text
A={0,1,2,3,4,5},       I=A cap X={0,1},
X={0,1,6,7},            p=8, q=9,
T={2,3,4,5,6,7,8,9}.
```

Let `G` be seven-connected.  Assume that each of the five six-sets

```text
A,
(A-{0})+p, (A-{0})+q,
(A-{1})+p, (A-{1})+q
```

is an irredundant support of a spanning `K_5` model, and that

```text
X+p, X+q
```

are literal `K_5` cliques.  Irredundancy means that a six-support contains
no literal `K_5`.  On six vertices its spanning `K_5` model therefore has
one two-vertex edge-bag and four singleton bags.  Exactly 375 labelled
edge/nonedge relations have this property.

Join those five exact relations on their common literal edge variables,
while fixing every edge of the two literal cliques.  No other edge is
completed.

A joined state is **common** when, for some `i in I`, the five-set
`A-{i}` contains a support-at-most-five `K_4` model every bag of which is
contacted by each of `i,p,q`.  The audited three-rooted small-`K_4`
composition theorem makes a common state terminal: after deleting its at
most five model vertices, seven-connectivity supplies a triangle model
rooted at `i,p,q`, and the two rooted models compose to a literal `K_7`.

## 2. A fixed reserved pair

Put

```text
H=G-I.
```

The graph `H` is five-connected.  Reserve the **fixed** private pair
`p,q`.  Then

```text
J=H-{p,q}=G-(I union {p,q})
```

is three-connected and contains the six labelled terminals

```text
T-{p,q}={2,3,4,5,6,7}.
```

Apply the audited terminal-legal contraction theorem in `J`.  It gives a
terminal-rooted, terminal-irreducible three-connected minor `M` such that

```text
6 <= |V(M)| <= 6+floor(6/4)=7.
```

The complete labelled guarantee has two cases.

1. If `|M|=6`, delete edges until three-connectivity is edge-minimal.
   There are exactly 142 labelled carriers: 70 with nine edges and 72
   with ten.
2. If `|M|=7`, write `x` for its unique nonterminal.  There are exactly
   780 labelled terminal-irreducible kernels.  For every such kernel the
   finite composition may choose a neighbour `y` of `x` and unite the two
   adjacent preimage bags represented by `x,y`.  This transfers every
   `x` contact to the bag rooted at `y` and leaves six disjoint labelled
   carrier bags.

The 142/780 classification, its published inputs, and its independent
census are recorded in
[`hc7_overlap_three_six_terminal_kernel_closure.md`](hc7_overlap_three_six_terminal_kernel_closure.md)
and its audit.  The present computation regenerates the complete labelled
catalogues rather than importing an isomorphism list.

## 3. Exact composition theorem

### Theorem 3.1

The joined relation in Section 1 has exactly

```text
1,419 joined states,
1,179 common states,
240 noncommon states in 9 category-automorphism orbits.
```

For every noncommon state, reserve the same literal pair `p,q`.  Then:

* every one of the 142 labelled order-six carriers on
  `{2,3,4,5,6,7}` composes with the forced original edges to a `K_7`
  model; and
* for every one of the 780 labelled order-seven kernels, some neighbour
  of its nonterminal can absorb that nonterminal so that the resulting
  six-bag carrier composes with the forced original edges to a `K_7`
  model.

Consequently all 240 noncommon states, and hence all 1,419 joined states,
are terminal.

The stronger diagnostic which allows any reserved pair in `T` gives the
following number of valid pairs, weighted over the 240 original states:

```text
10:12, 13:48, 14:24, 16:108, 18:24, 19:24.
```

In particular every orbit contains the fixed valid pair `{p,q}`; no
state-dependent choice is used in the proof.

### Finite certificate and exact quantifiers

The category automorphism group is

```text
Sym(I) times Sym(A-I) times Sym(X-I) times Sym({p,q}),
```

of order `2!*4!*2!*2!=192`.  The verifier constructs the full orbit of
every representative and checks that it lies in the noncommon state set
and has exactly the recorded weight.  The fixed pair `{p,q}` is invariant
as an unordered set under this group.  As a separate guard, the verifier
also bypasses orbit compression and tests the fixed pair `{p,q}` directly
on all 240 literal noncommon states against the complete 142/780
catalogue.

Each noncommon state has nine unspecified original edges.  The final
certificate uses only forced-present original edges.  Thus setting an
unspecified edge present in the host graph cannot destroy the returned
minor.

The final quotient has ten labelled objects:

```text
{0}, {1}, {p}, {q}, and the six terminal-rooted carrier bags.
```

The exact `K_7` detector permits unused objects and every possible
connected merger.  On ten objects any seven-bag model has at least four
singleton bags, so the detector exhausts the four possible singleton
counts `7,6,5,4`.  It never identifies terminal labels inside the carrier
and never treats an unspecified original edge as present.

The deterministic digests are

```text
six-terminal catalogue SHA-256:
02672ee56c859e9f45d3ab7b5a8bf82562fac14bf844f524101a1834954c43fe

noncommon-state SHA-256:
fda41d193855cc87de35746a5d567f53093a4ec8b2354b0caaadcac0d6d042e8

all 240 literal noncommon states SHA-256:
90f42c0edf0e6b5b6c424810fe19ce31f5e84ef1079feea0fd3a5c1454cf7ef5

state/reserved-pair certificate SHA-256:
17ce12fd03734d53af37deae840662b1744ecda8b86ef2fdd9934c5b5fff568a
```

## 4. Branch-set lift

### Theorem 4.1

Every seven-connected graph satisfying the normalized hypotheses of
Section 1 contains a `K_7` minor.

### Proof

If the joined state is common, apply the audited three-rooted small-`K_4`
composition theorem.

Otherwise reserve `p,q` and apply the terminal-legal kernel theorem in
the three-connected graph `J`.  If its kernel has order six, retain an
edge-minimal spanning three-connected subgraph; it is one of the 142
tested labelled carriers.  If it has order seven, it is one of the 780
tested kernels; choose the absorbing owner certified by Theorem 3.1 and
unite the two adjacent preimage bags.

In either case the resulting six carrier bags lie in `J`, are pairwise
disjoint, and contain their six distinct named terminals.  They are
therefore disjoint from the four singleton vertices `0,1,p,q`.  Every
original quotient edge used by the certificate is a literal edge between
named roots.  Every carrier edge is an actual adjacency between connected
preimage bags.  Replacing each quotient object by its connected preimage
preserves disjointness, connectivity, and every certified inter-bag
adjacency.  The quotient model therefore lifts to a literal `K_7` model
in `G`.  \(\square\)

## 5. Trust boundary

This theorem is local to the exact normalized cell in Section 1.  It does
not assert that every order-five rigid cell has this form, does not close
the live overlap-one cells, and does not establish the global
support-at-most-six transversal theorem.  Any global invocation must
first derive all five irredundant six-supports and both literal cliques
with the displayed labels.
