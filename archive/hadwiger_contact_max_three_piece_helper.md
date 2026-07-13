# A three-piece helper upgrade for the contact-maximal two-root lock

## 1. Setup

Let (G) be a graph, let (vin V(G)), and put (H=G-v).  Let

\[
                    (B,B_1,B_2,B_3,B_4,B_5)              \tag{1.1}
\]

be a contact-maximal labelled (K_6)-model in (H).  Assume that (B)
contains distinct roots (a,z\in N_G(v)), exactly four of the other five
bags are contacted, and the remaining bag (B_u) is uncontacted.  This is
the sharp five-contact terminal cell after multiply-root promotion.

Let

\[
                        B=Z_a\mathbin{\dot\cup}Z_z
                              \mathbin{\dot\cup}Z_h       \tag{1.2}
\]

be a partition into three nonempty connected pairwise adjacent sets with
(a\in Z_a), (z\in Z_z).  Let (h\ne u) be a contacted label and
assume (Z_h\sim B_h).  Such a partition exists whenever a chosen portal
(w\in N_B(B_h)) is distinct from (a,z) and (B) is 2-connected: use
the rooted-triangle lemma at (a,z,w), then extend the three rooted sets
over the remaining vertices by a rooted spanning forest.

For a label (i\notin\{h,u\}), call (i) **pole-crossing** when

\[
                         Z_a\sim B_i\quad\hbox{and}\quad Z_z\sim B_i.
                                                               \tag{1.3}
\]

## 2. The helper-packing theorem

### Theorem 2.1 (contacted helper plus three far blocks)

In the setup above, the model (1.1) was not contact-maximal if either

1. all three contacted labels in
   \([5]-\{h,u\}\) are pole-crossing; or
2. exactly two of those labels are pole-crossing and, for the remaining
   contacted label (k),

   \[
       \{Z_a,Z_z\}
       =\{Z\in\{Z_a,Z_z\}:Z\sim B_u\text{ or }Z\sim B_k\}.     \tag{2.1}
   \]

In either case there is an explicit (K_6)-model with all six bags
contacted.

#### Proof

Absorb (B_h) into (Z_h).  The set

\[
                              Z_h^+=Z_h\cup B_h             \tag{2.2}
\]

is connected, is contacted by the old root in (B_h), and is adjacent to
every old bag with a label different from (h), because the old bags form
a clique model.  The sets (Z_a,Z_z,Z_h^+) remain pairwise adjacent and
are all contacted.

It remains to turn the four old bags with labels in ([5]-\{h\}) into
three contacted far carriers, each adjacent to both pole pieces.  The
three far blocks must have sizes (1,1,2).  Put two pole-crossing
contacted labels into the singleton blocks.  Put (u) and the remaining
contacted label (k) into the double block.  Its union is connected and
contacted, and it is adjacent to both pole pieces precisely when (2.1)
holds.  In outcome 1 choose any two of the three crossing labels as the
singletons; the remaining crossing label (k) makes (2.1) automatic.

The three old-bag blocks are connected, disjoint and pairwise adjacent.
They all see (Z_h^+) through (B_h), and the construction makes each
see (Z_a,Z_z).  Consequently

\[
 Z_a,\quad Z_z,\quad Z_h^+,\quad
 B[J_1],\quad B[J_2],\quad B[J_3]                         \tag{2.3}
\]

are six disjoint pairwise adjacent connected sets, every one containing a
neighbour of (v).  This is a six-contact (K_6)-model, contradicting
contact maximality. \(\square\)

### Corollary 2.2 (exact triangle residue)

In a surviving five-contact model, every spanning triangle (1.2) and
every contacted helper label (h) meeting (Z_h) satisfy one of:

1. at most one of the other three contacted labels is pole-crossing; or
2. exactly two are pole-crossing, and the support masks of (B_u) and the
   remaining contacted bag both miss one common pole.

Thus the terminal obstruction is strictly narrower than the two-piece
width-two web: after spending one contacted clique bag as a helper, every
rooted triangle has a named common-dark pole.

## 3. Scope and audit boundary

The proof uses only the clique adjacency of the old model bags, the exact
contact count, and the displayed connected pieces.  It is uniform in the
orders and internal structures of all bags.  It does not assume that a
contracted old bag is a literal singleton in (G).

The result does not prove that every relevant contacted label has a portal
different from (a,z), nor does it eliminate the common-dark-pole residue.
Those are the two dynamic tasks left for minor-criticality and ambient
connectivity.
