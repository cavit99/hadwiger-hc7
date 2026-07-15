# Five-good decoder at overlap three

**Status:** computer-assisted theorem; independently audited **GREEN** in
[`hc7_overlap_three_five_good_decoder_audit.md`](hc7_overlap_three_five_good_decoder_audit.md).
This closes the normalized irredundant order-five-arm, overlap-three rigid
cell stated in Section 1.  To invoke it globally, prune reducible
six-supports before choosing the critical kernel, as in Corollary 4.2 below.
It does not close the order-six-arm overlap-three cell, the support-six
rung, or `HC_7`.

The exhaustive checker is
[`../active/hc7_overlap_three_order_five_verify.py`](../active/hc7_overlap_three_order_five_verify.py).
Its local relation and branch-model enumerator are in
[`../active/hc7_cross_arm_overlap_three_kernel_decoder.py`](../active/hc7_cross_arm_overlap_three_kernel_decoder.py).
Both use only the Python standard library.

## 1. Normalized cell

Use the labels

```text
A={0,1,2,3,4,5},       I=A cap X={0,1,2},
X=I union {6},          p=7, q=8,
T={3,4,5,6,7,8}.
```

Assume that `X union {p}` and `X union {q}` are literal `K_5`s and that
each of the following seven six-sets is an irredundant support of a
spanning `K_5` model:

```text
A,
(A-{i}) union {p}, (A-{i}) union {q}  for i in I.
```

As in the overlap-four decoder, an irredundant six-support has complement
equal to two nonempty vertex-disjoint stars.  There are 375 labelled local
relations.  The checker joins the seven copies on their literal common
edges and imposes the two literal arms before adding any rooted-carrier
adjacency.

Call a completion **common** if, for some `i in I`, `A-{i}` contains a
support-at-most-five `K_4` model contacted by each of `i,p,q`.  The audited
three-rooted small-`K_4` theorem turns this into `K_7` in a seven-connected
host.  Call a completion **direct** if its nine literal labels already
contain a `K_7` model.

## 2. Exact finite theorem

### Theorem 2.1

The normalized relation has exactly

```text
435 joined partial states,
6960 complete original-edge states,
6576 common states,
312 further direct K7 states,
72 residual states.
```

In every residual state there is a unique terminal

```text
b in {3,4,5}
```

which is not complete to `I`.  It misses exactly two or all three vertices
of `I`, in 54 and 18 states respectively.  The five-set

```text
W=T-{b}
```

is complete to every vertex of `I`.

Consequently, if any four members of `W` root a `K_4` model in `G-I`, then
the four rooted bags together with the three singleton bags of `I` form a
literal `K_7` model.  This conclusion is safe even if the rooted bags
absorb `b` or the fifth member of `W`: each bag contains its prescribed
root in `W`, and every member of `I` is adjacent to that root.

### Proof certificate

The checker directly tests the 375 local relations, joins all fixed edge
and nonedge variables, completes every unknown original edge, and
enumerates every relevant branch-set partition.  It then checks the unique
bad-terminal assertion edge by edge.  No virtual rooted edge participates
in an irredundancy constraint or in the definition of a common state.

## 3. Four-connected carrier consequences

Put `H=G-I`.  Seven-connectivity of `G` makes `H` four-connected.  Apply
the rooted clique-or-fan theorem
[`hc7_four_connected_terminal_fan_or_k4.md`](hc7_four_connected_terminal_fan_or_k4.md)
to the five good terminals `W`.

* If four members of `W` root `K_4`, Theorem 2.1 gives `K_7`.
* Otherwise `H` is planar and the five members of `W` lie on one facial
  cycle `C`.

There are two subcases.

### 3.1 The bad terminal is on the face

If `b in V(C)`, all six terminals lie on one facial cycle.  The peripheral
cycle construction gives the same rooted six-cycle with **any prescribed
terminal bag made universal**.  For every one of the 60 cyclic orders on
`T` and every one of the 72 residual states, the checker finds at least one
of the six choices of universal terminal for which the resulting rooted

```text
F_6=K_1 join P_5
```

composes to an explicit `K_7` model.  Thus this entire unbounded branch is
closed.

The freedom to choose the universal terminal is essential: 30 individual
labelled `F_6` carriers fail, but no fixed facial order fails for all six
choices.

### 3.2 The bad terminal lies behind the face

Suppose `b notin V(C)`.  The peripheral remainder `R=H-V(C)` is connected,
contains `b`, and meets every vertex of `C`.  The five `W`-rooted boundary
arcs and the bag `R` therefore form a rooted wheel

```text
K_1 join C_5
```

with hub rooted at `b`.

As a diagnostic, facial inducedness says that every literal `W-W` edge must
join consecutive members of the facial order.  This eliminates 24 residual
states.  In each of the other 48 states:

1. `G[W]` is a literal `P_5`;
2. that path determines the facial order uniquely up to reversal;
3. the `b`-hub wheel quotient has no `K_7` model; and
4. adding **any one** of the five missing rim chords gives an explicit
   `K_7` model.

The checker verifies all 48 collapsed-wheel survivors and all 240
single-chord repair certificates.  The quotient is not the end of the
argument, because it has incorrectly merged the terminal `b` with the whole
peripheral remainder.

Delete `b` from `H`.  The graph `H-b` is three-connected and `C` remains a
facial cycle.  Therefore

```text
D=(H-b)-V(C)
```

is nonempty and connected, and every vertex of `C` has a neighbour in `D`.
Here nonemptiness follows because otherwise `H-b=C` would not be
three-connected; connectivity and full boundary contact are the standard
peripheral-cycle properties (the contact also follows from minimum degree
three and inducedness of `C`).  The original remainder `H-V(C)` is
connected, so the singleton vertex `b` has a neighbour in `D`.

Keep `{b}` and `D` as two distinct bags.  The bag `D` is universal to the
five `W`-rooted boundary arc bags and is adjacent to `{b}`.  The checker
adds exactly this seventh exterior object--no unspecified edge from `I` to
`D`--and finds an explicit `K_7` model for all

```text
72 residual states times 12 cyclic orders = 864
```

split-wheel inputs.  Thus the off-face branch closes without needing the
facial-edge filter; the 24/48 calculation merely explains why the collapsed
hub looked sharp.

## 4. Closure theorem

### Theorem 4.1

Let `G` be seven-connected and satisfy the normalized order-five-arm,
overlap-three support hypotheses of Section 1.  Then `G` contains a `K_7`
minor.

### Proof

The finite theorem gives a common three-rooted `K_4`, a direct `K_7`, or a
unique five-good residual.  The first outcome gives `K_7` by the audited
three-rooted small-`K_4` theorem.  In the residual, apply the
four-connected rooted clique-or-fan theorem to `W`.  A rooted `K_4` gives
the seven bags consisting of its four bags and the three singleton members
of `I`.  Otherwise the planar facial alternatives of Sections 3.1 and 3.2
give `K_7` by the certified fan or preserved-`b`/`D` decoder.  These cases
are exhaustive.  \(\square\)

### Corollary 4.2 (the global rigid subcell)

Suppose `tau(S_{<=6}(G))>2`.  Retain every order-five support and only those
order-six supports that contain no order-five support, and then choose an
inclusion-minimal transversal-three subfamily `F`.  If the private-pair
cross-arm theorem applied inside `F` returns rigid arms of order five with
overlap three, then `G` contains a `K_7` minor.

### Proof

Deleting a reducible six-support does not change the transversal number,
because its contained five-support is retained.  Thus `F` exists and every
six-member of `F` is irredundant.  In the stated rigid cell `|X|=4` and the
two arms `X+p,X+q` are literal `K_5`s.  Positive overlap has already been
excluded when `|A|=5`, so `|A|=6`.  Writing `I=A cap X`, the cell parameter
is `|I|=3`; the forced replacement conclusion of the cross-arm theorem
places

```text
A, (A-{i})+p, (A-{i})+q  for i in I
```

inside the same pruned family `F`.  These are the seven irredundant
six-supports of Section 1, while the two arms are its literal `K_5`s.
Theorem 4.1 applies after relabelling. \(\square\)

The proof uses finite enumeration only for the fixed nine- and ten-object
labelled composition.  It places no bound on the order of the exterior
`H`; the peripheral argument compresses every such exterior into the
certified carrier objects.
