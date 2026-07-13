# Contact-maximal two-root bags: block packing and double-root rotation

## 1. Setup

Let \(G\) be a graph, let \(v\in V(G)\), and put \(H=G-v\).  Fix a
contact-maximal labelled \(K_6\)-model

\[
                         (B,B_1,\ldots,B_5)              \tag{1.1}
\]

in \(H\), where a bag is contacted when it meets \(N_G(v)\).  Assume
that

* \(B\) contains two distinct roots \(a,z\in N_G(v)\); and
* every other contacted bag \(B_i\) contains exactly one root.

At least one \(B_i\) is uncontacted, since otherwise (1.1), after
splitting \(B\) only at the level of contacts, is already beyond the
non-meeting terminal cell.  More directly, this is the output of the
multiply-root promotion in Section 4 of
`hadwiger_relative_deficit_circuit_promotion.md`.

Let

\[
                         B=L\mathbin{\dot\cup}R           \tag{1.2}
\]

be any partition into nonempty connected adjacent sets with
\(a\in L\) and \(z\in R\).  Such a partition always exists by deleting
an edge of the \(a\)-to-\(z\) path in a spanning tree of \(B\).

For \(i\in[5]\), record its support mask

\[
 \mu(i)=\{L:E(L,B_i)\ne\varnothing\}
       \cup\{R:E(R,B_i)\ne\varnothing\}.                \tag{1.3}
\]

Every mask is nonempty because the unsplit bag \(B\) is adjacent to
every \(B_i\).  Put

\[
 \begin{aligned}
 C&=\{i:\mu(i)=\{L,R\}\},\\
 A&=\{i:\mu(i)=\{L\}\},\\
 Z&=\{i:\mu(i)=\{R\}\}.
 \end{aligned}                                           \tag{1.4}
\]

Thus \([5]=C\dot\cup A\dot\cup Z\).

## 2. One unit of clique-bag recycling

### Theorem 2.1 (four-block packing)

The split (1.2) gives a \(K_6\)-model with \(L,R\) as distinct branch
sets whenever either

1. \(|C|\ge4\); or
2. \(|C|=3\) and \(A,Z\) are both nonempty.

#### Proof

We partition the five old clique bags into four nonempty groups.  Three
groups will be singleton labels from \(C\).  In outcome 1, put the two
remaining labels into the fourth group; that group contains a crossing
label and hence is adjacent to both \(L,R\).  In outcome 2, the three
crossing labels are the singleton groups and the fourth group is the
pair consisting of the unique label of \(A\) and the unique label of
\(Z\).

For every group, take the union of its old bags.  This union is connected
because the old bags are pairwise adjacent.  Different group carriers
are disjoint and adjacent.  By construction every group carrier is
adjacent to both \(L\) and \(R\); the two latter sets are connected,
disjoint, and adjacent by (1.2).  Hence

\[
               L,\ R,\ \text{the four group carriers}    \tag{2.1}
\]

are six disjoint pairwise adjacent connected sets, as claimed.
\(\square\)

The theorem is the precise improvement over “drop one bag and preserve
four named adjacencies.”  The one dropped slot is not discarded: it is
merged into one of the four retained clique carriers and can repair one
defect on each opposite side.

## 3. Contact accounting

### Theorem 3.1 (contact increase or double-root rotation)

Under the contact assumptions of Section 1:

1. if \(|C|\ge4\), the model in Theorem 2.1 can be chosen with strictly
   more contacted bags than (1.1);
2. if \(|C|=3\), \(A=\{i\}\), and \(Z=\{j\}\), then it has strictly
   more contacted bags unless both \(B_i,B_j\) are contacted;
3. in that sole exceptional case, the construction preserves the number
   of contacted bags and replaces the double-root bag \(B\) by the
   double-root group carrier \(B_i\cup B_j\).  Its two roots are the old
   roots of \(B_i,B_j\).

#### Proof

Splitting \(B\) replaces one contacted bag by the two contacted bags
\(L,R\), a gain of one.  Grouping old bags loses one contacted bag
exactly when the unique doubleton group consists of two contacted bags.

When \(|C|\ge4\), choose an uncontacted label \(u\).  Make the
doubleton group consist of \(u\) and one other label, choosing the three
crossing singleton groups among the remaining labels.  This is always
possible: if exactly four labels cross and \(u\) is crossing, pair it
with the unique noncrossing label; if \(u\) is noncrossing, pair it with
one crossing label; if all five cross, pair it arbitrarily.  Thus the
doubleton contains at most one contacted bag, so no contact is lost in
grouping, while the split gains one.

When \(|C|=3\) with opposite exclusive labels, the doubleton group is
forced to be \(\{i,j\}\).  It loses a contact precisely when both old
bags are contacted.  If not, the split gives the strict increase.  If
both are contacted, their group carrier is connected and contains their
two distinct old roots.  The contact loss from merging them exactly
cancels the contact gain from splitting \(B\), proving item 3.
\(\square\)

### Corollary 3.2 (exact contact-maximal split states)

In a contact-maximal model, every connected \(a\)-\(z\) split of \(B\)
has one of the following forms.

1. At most two labels are crossing.
2. Exactly three labels are crossing and the other two are exclusive to
   the same side.
3. Exactly three labels are crossing, the other two are exclusive to
   opposite sides, both exclusive bags are contacted, and Theorem 3.1(3)
   gives a same-contact **double-root rotation**.

No split has four or five crossing labels.

This is a complete finite support classification for every rooted split;
it has no assumption on the order or internal structure of any bag.

## 4. The resulting directed exchange problem

Outcome 3 of Corollary 3.2 is not a dead end.  It replaces the current
double-root label by the unordered pair of the two opposite exclusive
contacted labels.  Define a directed arc

\[
                    B\longrightarrow B_i\cup B_j         \tag{4.1}
\]

for every such split.  The new six bags in (2.1) are explicit, so (4.1)
is a genuine model exchange, not merely a quotient state.

Every terminal same-contact obstruction therefore has one of two exact
forms:

* all rooted splits have at most two crossing label classes (or the
  one-sided three-crossing state); or
* the double-root carrier can be rotated to another contacted carrier.

A lexicographic potential may orient some rotations, but an arbitrary
cycle cannot be excluded solely by bag sizes.  In fact the exchange has
an exact involutive quotient.

### Lemma 4.1 (the rotation frame is \(K_3\vee C_4\))

In the exceptional rotation state, write the three crossing bags as
\(K_1,K_2,K_3\), and the opposite exclusive bags as \(B_i,B_j\), where
\(L\sim B_i\), \(R\sim B_j\).  Then

\[
                   L,R,B_j,B_i,L                         \tag{4.2}
\]

is a four-cycle of branch sets, each \(K_s\) is adjacent to every member
of that cycle, and the \(K_s\)'s are pairwise adjacent.  Thus the seven
unmerged pieces form a rooted

\[
                         K_3\vee C_4
                    \cong K_7-2K_2                         \tag{4.3}
\]

minor model, where the two missing adjacencies are precisely
\(LB_j\) and \(RB_i\).

Moreover the rotation is automatically reversible: in the rotated model,
split the double-root carrier \(B_i\cup B_j\) back into \(B_i,B_j\).
The bags \(L,R\) are then the two opposite exclusive labels and the same
three \(K_s\)'s cross.  Hence every rotation arc belongs to a directed
two-cycle.

#### Proof

The edge \(LR\) comes from the connected split of \(B\), and
\(B_iB_j\) is an old clique-bag edge.  The two support masks give
\(LB_i\) and \(RB_j\).  Every crossing bag sees both \(L,R\), and old
clique adjacency makes it see \(B_i,B_j\) and the other crossing bags.
These are exactly the asserted edges.  The two unasserted diagonals are
the exclusive defects.  The reverse split has the support masks just
described, proving reversibility. \(\square\)

Thus rotation is a normalization, not a well-founded descent.  The
correct dynamic target is the strictly smaller statement:

> **Rooted two-diagonal repair lemma.**  In a proper-minor-minimal
> non-six-colourable host, a rooted \(K_3\vee C_4\)-model arising from a
> contact-maximal rotation either repairs one of the two missing
> diagonals by a label-preserving rerouting and then repairs the other,
> or exposes an adhesion of order at most six / two compatible faithful
> operation states.

Every object in this target is named: the four cyclic root carriers, the
three universal clique carriers, and the two missing diagonals.

## 5. Bipolar sweep form

If \(B\) is 2-connected, take an \(a\)-\(z\) bipolar ordering

\[
                         b_1=a,b_2,\ldots,b_n=z.          \tag{5.1}
\]

Every prefix and complementary suffix is connected.  For label \(i\),
let

\[
 \ell_i=\min\{s:b_s\in N_B(B_i)\},\qquad
 r_i=\max\{s:b_s\in N_B(B_i)\}.                         \tag{5.2}
\]

At cut \(t\), label \(i\) is crossing exactly when
\(\ell_i\le t<r_i\).  Corollary 3.2 says that every cut has at most
three active intervals; a three-active cut is either one-sided, or its
two inactive intervals belong to opposite sides and name a
double-root rotation between two contacted bags.

Thus the genuine contact-maximal obstruction is a width-two interval web
with explicitly named rotation cuts.  This is the correct input for an
operation-state proof: a repeated rotation state can be compared across
an actual connected prefix/suffix separation, while a transition from
past to future through four active labels would already contradict
contact maximality by Theorem 3.1.

## 6. Scope and countertests

Theorems 2.1 and 3.1 use only clique-bag grouping and contact accounting;
they do not invoke contraction-criticality.  They therefore apply to the
known static counterarchitectures as a classification, not as a false
closure theorem.  In particular, the promoted icosahedral example may
remain in the at-most-two-crossing web or undergo a same-contact rotation.

The new information is exact and reusable:

\[
 \boxed{\text{four crossings}\Rightarrow\text{contact augmentation},
 \quad
 \text{three opposite crossings}\Rightarrow
 \text{augmentation or named rotation}.}
\]

Closing the width-two/rotation web still requires the all-operation
minor-critical state, an ambient separator, or a proof that every
rotation cycle composes to a rooted model.

## 7. A three-piece helper upgrade

The five old clique labels provide enough capacity for a stronger move
when the double-root bag contains a rooted triangle.

Let \(h\in[5]\) index a contacted bag \(B_h\).  Suppose \(B\) contains
three pairwise disjoint, pairwise adjacent connected sets

\[
                         D_a,D_z,D_w                       \tag{7.1}
\]

with \(a\in D_a\), \(z\in D_z\), and with an edge from \(D_w\) to
\(B_h\).  Absorb \(B_h\) into \(D_w\), putting

\[
                         W=D_w\cup B_h.                    \tag{7.2}
\]

The set \(W\) is connected and contains the old root of the contacted
bag \(B_h\).

For the four remaining labels \(J=[5]-\{h\}\), record only their support
on the two pole pieces:

\[
 \sigma(j)=\{a:E(D_a,B_j)\ne\varnothing\}
          \cup\{z:E(D_z,B_j)\ne\varnothing\}.             \tag{7.3}
\]

The mask is allowed to be empty: a label may meet the old bag \(B\) only
through vertices outside \(D_a\cup D_z\).  Call \(j\) **pole-crossing**
when \(\sigma(j)=\{a,z\}\).

### Theorem 7.1 (rooted-triangle helper packing)

The rooted triangle (7.1) gives a new \(K_6\)-model if either

1. at least three labels in \(J\) are pole-crossing; or
2. exactly two labels are pole-crossing and the union of the support
   masks of the other two labels is \(\{a,z\}\).

#### Proof

Partition the four labels in \(J\) into three nonempty far blocks.  Two
blocks are singleton pole-crossing labels.  In outcome 1 put the two
remaining labels in the third block; it contains a pole-crossing label.
In outcome 2 put the two noncrossing labels in the third block; their
combined mask meets both poles by hypothesis.

Replace every block by the union of its old clique bags.  Each union is
connected, and the three far carriers are pairwise adjacent.  By
construction each is adjacent to both \(D_a,D_z\).  Every far carrier is
also adjacent to \(W\), because \(W\) contains the old clique bag
\(B_h\).  Finally the three sets in (7.1), and hence
\(D_a,D_z,W\), are pairwise adjacent.  Thus

\[
                 D_a,D_z,W,\text{ the three far carriers} \tag{7.4}
\]

form a \(K_6\)-model. \(\square\)

### Theorem 7.2 (contact count and the sole helper exception)

In the contact-maximal setup:

1. outcome 1 of Theorem 7.1 always gives a strict contact augmentation;
2. outcome 2 gives a strict contact augmentation unless both labels in
   its forced doubleton block are contacted;
3. in that sole exception, (7.4) preserves the contact count and rotates
   the double root into the union of those two contacted exclusive bags.

#### Proof

Originally \(B\) and \(B_h\) contribute two contacted bags.  In (7.4),
the sets \(D_a,D_z,W\) contribute three, a gain of one.  Grouping the four
remaining labels into three carriers loses a contact exactly when the
doubleton block contains two contacted bags.

In outcome 1, choose an uncontacted label \(u\in J\); such a label exists
because \(h\) is contacted and the original model is not fully meeting.
Put \(u\) in the doubleton block while leaving two pole-crossing singleton
blocks.  This is possible with at least three crossing labels, whether or
not \(u\) itself crosses.  The doubleton then contains at most one
contacted bag, so the gain survives.

In outcome 2 the two crossing labels must be the singleton blocks, so the
other two labels form the unique doubleton.  The contact gain is cancelled
exactly when both are contacted.  Their union then contains their two old
distinct roots, proving the rotation assertion. \(\square\)

### Corollary 7.3 (the strict two-pole owner lock)

At contact maximum, every rooted triangle (7.1) based at a contacted
helper label has one of the following forms.

1. At most one of the remaining four labels is pole-crossing.
2. Exactly two are pole-crossing, while the other two masks fail to cover
   both poles (one pole is dark to both, or one mask is empty and the
   other is one-sided).
3. Exactly two are pole-crossing; the other two cover opposite poles, are
   both contacted, and give the same-contact double-root rotation of
   Theorem 7.2(3).

No rooted helper triangle has three or four pole-crossing labels.

When \(B\) is 2-connected and \(a,z,w\) are three distinct vertices, a
rooted triangle (7.1) exists by the fan/cycle rooted-triangle lemma.  Thus
any contacted portal vertex \(w\notin\{a,z\}\) can be tested by
Corollary 7.3.  Failure is now a two-pole owner lock on four labels, not
the original simultaneous four-row split problem.

## 8. Exact next dynamic object

The two-piece theorem leaves a width-two interval web.  The helper upgrade
adds a transverse test at every contacted portal \(w\): after spending its
label as a helper, at most one of the four remaining rows may cross both
pole pieces, except for a named two-crossing rotation state.

Accordingly the operation-sensitive target can be stated without Moser
labels:

> In a seven-contraction-critical host, a 2-connected double-root carrier
> with the two-piece width-two property and the three-piece helper lock at
> every contacted portal either has a common dark pole row behind an
> actual separation of order at most six, or two internal operations
> induce the same faithful equality state on opposite sides.

Theorems 7.1--7.2 are the explicit branch-set part of that target.  They
do not assert the final separator/state alternative.
