# Cold audit of the overlap-three five-good decoder

## Verdict

**GREEN.**  The normalized relation, the unique five-good residue, the
four-connected carrier split, and the ten-object branch-set lift in
[`hc7_overlap_three_five_good_decoder.md`](hc7_overlap_three_five_good_decoder.md)
are correct.  The retained scripts replay all stated counts and use no
virtual edge in an original six-support constraint.

This closes the normalized **order-five-arm, overlap-three** cell only.
It does not cover order-six arms or other overlap sizes.

## 1. Independent finite replay

An independent complement-language reconstruction gave the same local
numbers before this theorem was written:

```text
375 irredundant six-support relations,
435 joined partial states,
6960 original completions,
6576 common states,
312 further original K7 states,
72 residues.
```

Running

```text
python3 active/hc7_overlap_three_order_five_verify.py
python3 active/hc7_cross_arm_overlap_three_kernel_decoder.py \
  --arm-order 5 --carrier split-wheel
```

reproduces those counts and reports respectively all 48 feasible
off-face states and all 864 split-wheel state/order pairs closed.

For each residue, exactly one member `b` of `{3,4,5}` misses `I`; its
defect has order two in 54 states and three in 18.  The other five
terminals are complete to all three members of `I`.  Therefore a `K_4`
rooted at any four good terminals, together with the singleton bags in
`I`, is a literal `K_7`.  Omitted exterior terminals are not separate
bags, so their possible absorption by the rooted model is harmless.

## 2. Cofacial branch

If the bad terminal lies on the facial cycle through the five good roots,
the peripheral construction gives one fixed six-root cycle and allows
**any** of its six rooted bags to absorb the connected remainder.  The
checker correctly tests the six hub choices for each of the 60 unoriented
cyclic orders.  Individual labelled fans are not all sufficient; the
proof uses exactly the available adaptive-hub freedom.

If the bad terminal is off the face, every literal edge between two good
roots must join consecutive roots in the facial order, since a facial
cycle of a three-connected plane graph is induced.  The checker uses this
only as a necessary filter.  It finds 24 impossible residues and 48
feasible residues; in each feasible residue the literal good-root graph
is `P_5` and the facial order is unique up to reversal.

## 3. The split peripheral remainder

Put `H=G-I`, let `C` be the facial cycle, and suppose `b notin C`.
Four-connectivity of `H` makes `H-b` three-connected.  Deleting an
off-cycle vertex does not destroy the face bounded by `C`, so `C` remains
a facial cycle in `H-b`.  Hence

```text
D=(H-b)-V(C)
```

is connected.  It is nonempty, since otherwise `H-b=C` with
`|C|>=5`, contrary to three-connectivity.  Peripheral inducedness and
minimum degree three show that every vertex of `C` has a neighbour in
`D`.

The remainder `H-V(C)=D union {b}` is connected by peripheral
nonseparation in `H`; since `D` is nonempty, this implies an actual edge
from `b` to `D`.  Thus `{b}` and `D` are two disjoint connected carrier
bags, `D` is adjacent to every boundary-arc bag, and `{b}` is adjacent to
`D`.

## 4. Ten-object lift

The expanded finite layer uses labels `0,...,8` for the original local
vertices and label `9` only for `D`.  Besides original edges it inserts
exactly:

* the five facial-rim adjacencies between consecutive good-root bags;
* the five adjacencies from `D` to those bags; and
* the edge `bD`.

It assumes no `I-D` or `b-W` edge.  Replace every good terminal in a
finite certificate by its entire boundary-arc bag and replace label `9`
by `D`.  Original root-incident edges remain literal, rim and `D` contacts
are the edges just proved, and all objects are disjoint from `I`, from
`b`, and from one another.  Connectivity and every inter-bag adjacency
therefore lift exactly.  The exhaustive partition routine finds a
`K_7` model for all 48 feasible states.

## 5. Global normalization

Corollary 4.2 is valid provided the order of operations is retained.  Let
`S^irr` contain every five-support and only those six-supports containing no
five-support.  Then

```text
tau(S^irr)=tau(S_{<=6}(G)),
```

because each deleted member contains a retained member.  Choose the
critical kernel only after this pruning.  The private-pair and cross-arm
theorems then return the avoided support, both arms, and all forced
replacements inside this same kernel.  For order-five arms `|X|=4`; positive
overlap excludes an order-five avoided support, and overlap three supplies
exactly the seven irredundant support-six constraints and two literal arms
used by the decoder.

An arbitrary critical kernel chosen before pruning cannot silently be
declared irredundant.  This ordering caveat is now explicit in the source
corollary.

## 6. Scope

The proof is computer-assisted only in the fixed labelled composition.
The exterior has arbitrary order; four-connectivity and peripheral-cycle
structure reduce it to the certified carrier objects.  No finite-order
assumption on `H` is present.
