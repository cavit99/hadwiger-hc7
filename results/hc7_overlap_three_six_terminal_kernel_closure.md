# Six-terminal kernel closure at overlap three

**Status:** computer-assisted theorem; independently audited **GREEN** in
[`hc7_overlap_three_six_terminal_kernel_closure_audit.md`](hc7_overlap_three_six_terminal_kernel_closure_audit.md).
This closes the normalized irredundant arm-order-six, overlap-three rigid
cell.  It does not prove the support-six transversal theorem or `HC_7`.

The exhaustive verifier is
[`../active/hc7_overlap_three_six_terminal_kernel_verify.py`](../active/hc7_overlap_three_six_terminal_kernel_verify.py).
It uses only the Python standard library.  The local relation is supplied
by
[`../active/hc7_cross_arm_overlap_three_kernel_decoder.py`](../active/hc7_cross_arm_overlap_three_kernel_decoder.py).

## 1. Normalized cell

Use the labels

```text
A={0,1,2,3,4,5},       I=A cap X={0,1,2},
X=I union {6,7},        p=8, q=9,
T={3,4,5,6,7,8,9}.
```

Let `G` be seven-connected.  Assume that each of the nine six-sets

```text
A, X+p, X+q,
(A-{i})+p, (A-{i})+q  for i in I
```

is an irredundant support of a spanning `K_5` model.  Thus none contains a
literal `K_5`.  On six vertices this is an exact finite relation: a
spanning `K_5` model has one edge-bag and four singleton bags.  There are
375 labelled local relations.

Join the nine local relations on their common literal edge and nonedge
variables.  A state is **common** when, for some `i in I`, the set `A-{i}`
contains a support-at-most-five `K_4` model contacted by each of `i,p,q`.
The audited three-rooted small-`K_4` composition theorem makes every common
state terminal.

## 2. Six-terminal kernel guarantee

Put

```text
H=G-I.
```

The graph `H` is four-connected.  Fix a reserved terminal `r in T`.  Then
`H-r` is three-connected: deleting at most two further vertices from it
amounts to deleting at most six vertices from `G`.

Apply the audited terminal-legal contraction theorem in `H-r` to the six
labelled terminals `T-{r}`.  It produces a three-connected rooted minor
`M`, obtained without identifying terminals, such that

```text
6 <= |M| <= 6+floor(6/4)=7
```

and `M` is terminal-irreducible.

There are two exact carrier types.

1. If `|M|=6`, all vertices are terminals.  Deleting edges until
   three-connectivity is edge-minimal gives one of exactly 142 labelled
   carriers: 70 have nine edges and 72 have ten.
2. If `|M|=7`, write `x` for the nonterminal.  Every edge incident with
   `x` is noncontractible.  Wu's theorem supplies at least four
   degree-three terminal neighbours of `x`.  Direct enumeration of all
   labelled simple graphs subject to these necessary conditions,
   three-connectivity, and the noncontractibility of every `xt` gives
   exactly 780 kernels.  Their profile

   ```text
   (d(x), sorted terminal degrees) : labelled kernels
   (4,(3,3,3,3,3,3)):180
   (5,(3,3,3,3,3,4)):360
   (6,(3,3,3,3,3,3)):60
   (6,(3,3,3,3,4,4)):180.
   ```

   For any neighbour `y` of `x`, the two rooted bags represented by `x,y`
   may be united.  This gives a six-bag terminal-rooted carrier whose
   adjacencies are exactly the terminal-terminal edges of `M`, together
   with the contacts from `x` transferred to the bag rooted at `y`.
   Three-connectivity of this contracted carrier is neither asserted nor
   needed.

   The independent hand classification in
   [`hc7_six_terminal_kernel_classification.md`](hc7_six_terminal_kernel_classification.md)
   gives the same four rooted types and the same 780 labelled kernels; the
   exhaustive verifier does not depend on that classification.

## 3. Exact finite composition

### Theorem 3.1

The joined relation has exactly

```text
60,162 joined states,
52,284 common states,
7,878 noncommon states in 140 category-automorphism orbits.
```

For every one of the 140 noncommon orbits there is at least one reserved
terminal `r in T` with the following universal property.

* Every labelled edge-minimal order-six carrier on `T-{r}` composes with
  the forced original edges to a `K_7` model.
* For every labelled order-seven terminal-irreducible kernel on `T-{r}`,
  some neighbour of its nonterminal can absorb that nonterminal so that
  the resulting six-bag carrier composes to a `K_7` model.

Thus all 7,878 noncommon states are terminal.  The number of universally
valid choices of `r`, weighted over the original states, has distribution

```text
one:153, two:180, three:513, four:513,
five:3798, six:1416, seven:1305.
```

Together with the 52,284 common states, this closes all 60,162 joined
states.

### Finite certificate

The checker first verifies the 60,162/7,878/140 relation and orbit counts.
The category automorphism group has order

```text
3! times 3! times 2! times 2! = 144
```

and preserves `I`, `A-I`, `X-I`, and `{p,q}`.  The universal-reserve
property is invariant under this group.

The 142 order-six carriers are generated directly from all `2^15`
labelled graphs.  The 780 order-seven kernels are generated directly from
all `2^21` labelled graphs with the nonterminal fixed as label six.  The
program checks three-connectivity and every incident contraction rather
than relying on an isomorphism catalogue.

For the final quotient, the program uses an explicit exact `K_7` detector
on ten objects.  Any seven-bag model on at most ten objects has at least
four singleton bags, which form a clique.  The detector exhausts the four
possibilities:

```text
7 singleton bags;
6 singleton bags plus one connected bag;
5 singleton bags plus two connected adjacent bags;
4 singleton bags plus three two-vertex bags.
```

Unused objects are allowed in the first three cases.  No generic graph
completion is performed, and the seven unknown original edges are never
assumed present.  The deterministic catalogue and noncommon-state digests
are

```text
catalogue SHA-256:
02672ee56c859e9f45d3ab7b5a8bf82562fac14bf844f524101a1834954c43fe

noncommon-state SHA-256:
6017357f84a3ebfd812d7e282d865ba6eab4cad2f6d33d4103f08dd6678560c1
```

With `--crosscheck`, the retained checker compares the specialized detector
with the generic branch-partition enumerator on 8,204 deterministic carrier
compositions and finds exact agreement.  That crosscheck has digest

```text
b831df578ec60a78b49328ae7b0a8e9fa806b05b8e0210bd93325b3a692845ca.
```

## 4. Branch-set lift

### Theorem 4.1

Every seven-connected graph satisfying the normalized hypotheses of
Section 1 contains a `K_7` minor.

### Proof

A common state closes by the audited three-rooted small-`K_4` composition
theorem.  Otherwise choose the reserved terminal `r` certified by Theorem
3.1 and apply the terminal-legal kernel theorem in `H-r`.

If the resulting kernel has order six, retain an edge-minimal spanning
three-connected subgraph.  Its labelled carrier is one of the 142 tested
carriers, so the finite certificate supplies a seven-bag quotient model.

If the kernel has order seven, it is one of the 780 tested labelled
kernels.  The certificate selects a neighbour `y` of its nonterminal `x`.
Unite the rooted preimage bags represented by `x` and `y`.  They are
adjacent and hence have connected union; the union remains disjoint from
the other five terminal bags and has exactly the contacts used by the
tested quotient.

In both cases the six carrier bags lie in `H-r`, are pairwise disjoint,
and each contains exactly its named terminal.  The three singleton members
of `I` and the singleton `{r}` are disjoint from them.  Every original
quotient edge is a literal edge between named roots, and every carrier edge
is an actual adjacency between preimage bags.  Replacing each quotient
object by its connected preimage therefore lifts every connected quotient
bag and every inter-bag adjacency.  The certified quotient `K_7` model is
a literal `K_7` model in `G`.  \(\square\)

## 5. Global rigid subcell

Prune the family of support-at-most-six `K_5` models by retaining every
order-five support and only those order-six supports which contain no
order-five support.  This does not change its transversal number.  Choose
the critical transversal-three kernel only after this pruning.

If the private-pair cross-arm theorem in this pruned kernel returns rigid
arms of order six with overlap three, while the avoided support has order
six, then its forced replacements are precisely the nine irredundant
supports of Section 1 after relabelling.  Theorem 4.1 closes this entire
rigid subcell.

The conclusion is unbounded in the order of `G`: only the terminal-legal
kernel in the three-connected deletion is finite.  The result does not
close arm overlaps one or two, the separated-triple branch, or the global
support-six transversal theorem.
