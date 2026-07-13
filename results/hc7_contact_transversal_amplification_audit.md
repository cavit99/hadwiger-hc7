# Independent audit: contact-transversal amplification

> Repository scope notice: this audit covers Sections 1--5 of the theorem
> note.  The later packet-witness Lemmas 4--5 in Section 6 are covered by
> `hc7_contact_transversal_amplification_section6_audit.md`.

## Verdict

**GREEN.**  All local scope repairs in Section 6 have been applied and
rechecked.  Lemma 1's separator arithmetic, Theorem 2's two-owner
rotation, Corollary 3, and the barrier's stated inference are correct.
The note now installs the residual `A-(F-L)` contact, permits every
needed comparison transfer, handles a sole owner `D` by a literal
`K_7`, and defines ownership using all actual interbag edges.

## 1. Owner-rule scope

For the deletion argument, replacing `F` by `F-L` preserves all
`F-Q` duties precisely when no foreign row is owned.  It preserves the
separate required `A-F` duty only if

\[
                         E(A,F-L)\ne\varnothing.          \tag{A.1}
\]

For the one-owner transfer into `Q`, condition (A.1) is again needed.
An old `L-Q` edge connects the enlarged row, and an edge across the
connected split `L|(F-L)` restores `F-Q`; every nonowned row retains an
actual contact from `F-L`.  This comparison is legitimate only when the
model-minimization class allows `Q` to be enlarged.  The phrase “all
earlier bags fixed” does not guarantee this for an arbitrary
`Q in {D,R_1,...,R_4}`.  The clean formulation is either:

* minimize `|F|` over a comparison class in which all five foreign rows
  may be enlarged; or
* explicitly assume transfer-minimality of `F` under deletion and every
  admissible single-owner transfer.

If the sole owner is `D`, moving `L` into `D` repairs `AD` through the
nonempty set `T`.  This is harmless if the comparison class allows the
pair `AD` to become present (the result is a literal `K_7` model), or if
the ambient argument is already in the no-`K_7` branch.  It should be
said explicitly if the comparison class instead insists that `AD`
remain absent.

Finally, define

\[
 \Omega(L)=\{Q:E_G(F,Q)\ne\varnothing\text{ and every edge in }
 E_G(F,Q)\text{ has its }F\text{-end in }L\}.
\]

All five `F-Q` pairs are required, so the nonemptiness clause is
automatic.  “Every model edge” is ambiguous if it means only a chosen
model witness.  Theorem 2 needs every actual edge: otherwise an owned
row may still have an unrecorded `F'-Q` edge, and the asserted exact list
of missing pairs is false.

With (A.1), the allowed-transfer condition, and actual-edge ownership,
the detachable-part proof of `|Omega(L)|>=2` is correct.

## 2. Actual-neighbour separator count

Lemma 1 is correct exactly as stated.  The spanning hypothesis gives the
disjoint equality

\[
             N_G(L)=T\mathbin{\dot\cup}Z\mathbin{\dot\cup}W.
\]

Since `|T|=3`, seven-connectivity and the assumed nonempty far side give

\[
             3+|Z|+|W|=|N_G(L)|\ge7,
             \qquad |W|\ge4-|Z|.
\]

If `|Z|+|W|<=3`, the actual neighbourhood has order at most six and
separates nonempty `L` from the far side.  The lemma correctly counts
vertices, not row labels.  Both the spanning and far-side hypotheses are
essential and are present.

## 3. Two-owner rotation

Under Theorem 2's hypotheses, put `D'=D\cup L` and `F'=F-L`.

* `D'` is connected through the assumed `D-L` edge.
* `F'` is connected by detachability.
* An edge across `L|F'` gives `D'F'`.
* `T=N_A(L)` has order three, so it is nonempty and gives `AD'`.
* The explicit residual hypothesis gives `AF'`.

All pairs not incident with old `F` survive.  Enlarging `D` cannot lose
one of its old contacts.  For a foreign row `Q`, actual-edge ownership
gives

\[
 E(F',Q)=\varnothing\quad\Longleftrightarrow\quad Q\in\Omega(L).
\]

The sole exception is `Q=D`: even if `D` is owned, the split edge gives
the new `D'F'` contact.  Therefore the only missing pairs are exactly

\[
                     F'Q\quad(Q\in\Omega(L)-\{D\}).
\]

When `D` is one of two owners this is one exact missing pair; otherwise
the two exact missing pairs share centre `F'`.  The old hole `AD` is
indeed repaired.  No adjacency after the transfer is being inferred
merely from colors or contractions.

## 4. Corollary 3

The corollary is correct after the owner rule is scoped as above.  An
owned row must actually meet `L`, because its nonempty `F-Q` edge has
its `F`-end in `L`.  Thus

\[
        \Omega(L)\subseteq\{\text{row bags containing foreign
        neighbours of }L\}.
\]

If the latter set has order at most two while the residual `A-F'`
contact makes (1.4) applicable, both sets have order exactly two.  If one
met row is `D`, then `L-D` supplies Theorem 2's transfer edge.  All three
hypotheses of Theorem 2 follow.

Section 5 must not drop the residual `A-F'` condition.  If neither its
small-gate branch nor Theorem 2 applies, the alternatives include:

1. `L` avoids `D`;
2. `L` owns more than two foreign rows; or
3. `F-L` has lost the last `A` portal.

The present text lists only the first two.  The third is a genuine live
case unless `A-F'` was already installed globally.

## 5. Barrier scope

The family in Section 4 does exactly what is claimed.  For `L={l}`,

\[
 T=\{t_1,t_2,t_3\},\qquad Z=\{f\},\qquad
 \Omega(L)=\{Q_1,Q_2\},
\]

while joining `l` to every vertex of the two order-`M` row bags makes
`|N_G(L)|` unbounded.  Moving `L` into one owner repairs that owner via
the `lf` split edge but loses the other `F-Q` adjacency.  Hence ownership
labels neither bound the actual neighbourhood nor choose a faithful
single transfer.

The construction is not claimed to be seven-connected,
contraction-critical, or `K_7`-minor-free, and it does not claim that no
other small cut exists.  It refutes only the proposed inference from two
owner labels to a bounded actual separator.  The note's final disclaimer
correctly states this boundary.

## 6. Repairs applied and verified

1. Add `E(A,F-L) ne empty` to the owner-rule paragraph preceding (1.4),
   or state (1.4) only conditionally for detachable lobes retaining that
   contact.
2. Specify that the comparison class permits enlargement of every
   possible owner row.  If exact absence of `AD` is protected, treat a
   sole owner `D` as an immediate `K_7` outcome rather than an ordinary
   comparison move.
3. Replace “every `F-Q` model edge” by “every actual edge of `G` between
   `F` and `Q`” in the definition of ownership and its later uses.
4. In Section 5, item 2 add the residual `A-(F-L)` contact and exact
   two-owner hypotheses.  In item 3 include loss of that residual contact
   among the alternatives, unless it is made a standing assumption.

All four changes now appear in the source note.  The note is ready for
promotion as an audited result.
