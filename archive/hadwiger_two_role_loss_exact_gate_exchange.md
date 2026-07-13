# Two-role loss at exact seven/eight gates: what can and cannot disappear

## 1. Result and scope

This note proves two operation-stable pieces of the bilateral
two-coordinate exchange.  They do not identify palette colours with model
labels.  They do show that two of the apparent ways in which two active
roles could disappear are not genuine:

1. in a minimum exact-seven fragment, contracting one internal edge cannot
   destroy distinct representatives for any proper subfamily of the
   literal boundary rows; and
2. at an exact-eight gate, either there is an immediate exact-seven descent,
   or every opposite component is full to the gate.  In the latter case a
   row which is private to one of the two lost roles gives two adjacent
   private carriers directly.

Consequently a bilateral loss which survives these lemmas must lose a
**common** carrier row (or a reserve row), rather than merely identify two
literal portal roots.  This is a smaller gate than the two-coordinate
axiom in `hadwiger_near_k7_active_root_face_exchange.md`.

## 2. Exact-eight shores are full or descend to exact seven

### Lemma 2.1 (full-shore normalization at order eight)

Let `G` be seven-connected, let `X` be an eight-vertex cut, and let `K` be
a component of `G-X` with

\[
                             N_G(K)=X.                 \tag{2.1}
\]

For every other component `C` of `G-X`, exactly one of the following
holds.

1. `N_X(C)=X`.
2. `|N_X(C)|=7`, and `N_X(C)` is an actual exact seven-cut separating
   `C` from `K`.

In particular, if the current descent has excluded a nested exact-seven
fragment, then every component of `G-X` is full to `X`.

#### Proof

The set `N_X(C)` separates `C` from `K`, because different components of
`G-X` are anticomplete and `K` is nonempty.  Seven-connectivity gives

\[
                             |N_X(C)|\ge7.             \tag{2.2}
\]

As `N_X(C)\subseteq X` and `|X|=8`, its order is seven or eight.  In the
first case every displayed vertex is an actual neighbour of `C`, so it is
an exact seven-cut.  In the second case `C` is full to `X`.  QED.

The point is that the old label omitted by the order-eight lobe is not
lost from the graph.  It lies in one of the opposite components of
`G-X`; absent exact-seven descent, that whole opposite component is full
to all eight gate vertices.

### Lemma 2.2 (private-row restoration across a full order-eight gate)

Retain Lemma 2.1 and assume there is no exact-seven outcome.  Let `R` be
an opposite component of `G-X`.  Suppose two extension roles have the
following form.

* Role `A` may be rooted in `R` at an old label `t\in R` and otherwise
  requires only contacts represented by vertices of `X`.
* Role `B` does not require `t` and all of its required contacts are
  represented by vertices of `X`.

Then the order-eight lobe supplies two disjoint adjacent private carriers
for the roles.  More explicitly, for any `x\in X`,

\[
                         R,\qquad K\cup\{x\}           \tag{2.3}
\]

are disjoint connected adjacent sets; the first carries role `A` rooted
at `t`, and the second carries role `B` rooted at `x`.

#### Proof

Both `K` and `R` are full to `X` by Lemma 2.1.  Hence `K\cup\{x\}` is
connected.  It is adjacent to `R`, since `R` has an edge to `x`.  The two
sets are disjoint because `K,R` are different components of `G-X` and
only the first displayed set contains no vertex of `X`.  Fullness gives
every required `X`-contact on both carriers, while `t\in R` supplies the
private root of role `A`.  QED.

This lemma deliberately says **private** row.  If `t` is a common
pool/reserve row needed by both roles, putting `t` into `R` does not make
`K\cup\{x\}` meet that row.  That common-row case is the true surviving
order-eight capacity-state web.

## 3. Strict Hall slack survives one contraction

Let `G` be `k`-connected, let `S` be a `k`-cut, and let `D` be a
minimum-order component behind all `k`-cuts.  Assume in addition that
`|D|\ge k`; this is already proved for the minimum
`C_6\dot\cup K_1` exact-seven cell (Corollary 4.5 of
`hadwiger_full_deletion_propagation.md`), but is not automatic for an
arbitrary minimum fragment.  Put

\[
                            P_s=N_D(s)\quad(s\in S).    \tag{3.1}
\]

The minimum-fragment surplus gives, for every nonempty proper
`A\subset S`,

\[
               \left|\bigcup_{s\in A}P_s\right|
                         \ge |A|+1.                    \tag{3.2}
\]

For reference, this is the proof of Lemma 5.4 of
`hadwiger_full_deletion_propagation.md`: if the union is not all of `D`,
take a component outside it and apply strict atomic surplus; if it is all
of `D`, the displayed size hypothesis gives (3.2).  The size hypothesis
must not be suppressed outside the audited minimum `C_6\dot\cup K_1`
cell.

### Theorem 3.1 (proper-subfamily contraction stability)

Let `uv` be an edge of `D`, let `q:D\to D/uv` be the contraction map,
and put

\[
                            P'_s=q(P_s).              \tag{3.3}
\]

For every proper subfamily indexed by `I\subsetneq S`, the sets

\[
                            (P'_s:s\in I)             \tag{3.4}
\]

have a system of distinct representatives.  Thus contraction of one
internal edge cannot destroy two (or even one) literal root roles inside
any proper collection of the boundary roles.

#### Proof

For `A\subseteq I`, contraction identifies only `u,v`, so

\[
 \left|\bigcup_{s\in A}P'_s\right|
 \ge
 \left|\bigcup_{s\in A}P_s\right|-1.                \tag{3.5}
\]

If `A` is nonempty, it is a proper subset of `S`, and (3.2)--(3.5) give

\[
 \left|\bigcup_{s\in A}P'_s\right|\ge |A|.          \tag{3.6}
\]

The empty set is harmless.  Hall's theorem applied to (3.4) proves the
claim.  QED.

### Corollary 3.2 (four literal active roots are operation-stable)

In the audited minimum `C_6\dot\cup K_1` exact-seven cell, any four active roles whose roots are
chosen from four distinct literal boundary portal classes still have
four distinct roots after contraction of an arbitrary internal edge.
Deletion of an internal edge does not change the portal classes at all.

Hence an internal edge operation cannot be said to destroy two active
coordinates merely because its ends carried two of the selected literal
roots.  If the contraction identifies those two selected occurrences,
Theorem 3.1 supplies another full transversal.

#### Proof

Take `|I|=4<7` in Theorem 3.1.  The deletion assertion is immediate from
the definition (3.1).  QED.

There is a sharper prescribed-root form already available.  Theorem 5.5
of `hadwiger_full_deletion_propagation.md` says that any two prescribed
distinct literal occurrences extend to a full seven-row SDR, or their
failure exposes an actual exact order-eight gate.  Thus Corollary 3.2 does
not merely replace two contracted roots by an unrelated transversal: the
two selected choices can be held fixed modulo precisely the next separator
layer treated in Lemma 2.1.

This is a rank statement, not yet a carrier-splitting theorem.  It does
not say that two roles forced into the same connected off-boundary lobe
can be separated, and it does not create a reserve disjoint from four
protected extensions.

### Theorem 3.3 (duplicating one common literal row)

Retain the audited minimum exact-seven hypotheses and let `t\in S`.  Take
two distinct occurrences

\[
                         x,y\in P_t.                   \tag{3.7}
\]

Then at least one of the following holds.

1. The multiset of demands consisting of two copies of `t` and one copy
   of every label in `S-\{t\}` has an SDR assigning the two copies of `t`
   to `x,y`.
2. There are a nonempty `A\subseteq S-\{t\}` and a component `C` outside
   
   \[
                         U=\bigcup_{a\in A}P_a          \tag{3.8}
   \]

   such that

   \[
    |U|=|A|+1,\qquad \{x,y\}\subseteq U,\qquad
    N_G(C)=U\mathbin{\dot\cup}(S-A),                    \tag{3.9}
   \]

   an actual exact order-eight gate.
3. `|D|=7`, `A=S-\{t\}`, and

   \[
                         D=\bigcup_{a\ne t}P_a.         \tag{3.10}
   \]

   Thus the only non-gate exception is one seven-vertex saturated atom.

#### Proof

Assign the two copies of `t` to `x,y` and apply Hall to the remaining six
sets `(P_s-\{x,y\}:s\ne t)`.  If Hall holds, outcome 1 follows.  Otherwise
some nonempty `A\subseteq S-\{t\}` has

\[
                  |U-\{x,y\}|<|A|.                    \tag{3.11}
\]

Strict Hall surplus (3.2) gives `|U|\ge|A|+1`.  Since deleting two
vertices leaves at most `|A|-1` vertices by (3.11), equality is forced:

\[
                  |U|=|A|+1,\qquad \{x,y\}\subseteq U. \tag{3.12}
\]

If `U\ne D`, take a component `C` of `D-U`.  It misses every label in
`A` and has no internal neighbour outside `U`, whence

\[
                         N_G(C)\subseteq U\cup(S-A).
\]

The right side has order eight.  Strict atomic surplus gives the reverse
lower bound eight, proving equality and outcome 2.

If `U=D`, then `|D|=|A|+1`.  Here `|D|\ge7` while `|A|\le6`, so equality
forces `|D|=7` and `A=S-\{t\}`.  This is outcome 3.  QED.

The theorem is the literal-root part of the common-row exchange.  Even a
row required twice can be duplicated, unless the failure has already
become an exact-eight separator or the whole minimum fragment has order
seven.  It still does not assert that the two root occurrences lie in
disjoint connected carriers meeting all the other rows of their respective
roles.

### Corollary 3.4 (no finite residue for a proper role support)

Let `I\subseteq S-\{t\}` and assume `\{t\}\cup I\subsetneq S`.  With
`x,y` fixed as in (3.7), the demand family consisting of two copies of
`t` and one copy of every member of `I` has an SDR, or an exact
order-eight gate occurs.  The seven-vertex saturated exception of Theorem
3.3 is impossible.

#### Proof

Repeat the proof of Theorem 3.3 with Hall witnesses `A\subseteq I`.  If
the tight union `U` is proper in `D`, the same atomic-surplus argument
gives the exact order-eight gate.  If `U=D`, then

\[
                         |D|=|A|+1\le |I|+1\le6,
\]

contrary to `|D|\ge7`.  QED.

Thus a two-role exchange using fewer than all seven distinct literal
boundary labels has no bounded order-seven root-capacity residue.  Only a
carrier-connectivity failure or the exact-eight separator can remain.

## 4. The exact reduced bilateral gate

Combine the preceding statements with the shared-lobe and active-face
reductions.

### Corollary 4.1 (two-role loss has a common-row witness)

In a retained minimum exact-seven near-`K_7` cell satisfying the strict
portal surplus (3.2)—in particular, in the audited minimum
`C_6\dot\cup K_1` cell—suppose a faithful
internal edge operation is alleged to destroy two active extension roles.
Assume the four roles before the operation use distinct literal boundary
classes and that every order-eight descendant with a private missed row
is retained in the descent.  Then one of the following holds.

1. The four literal root roles survive the operation; any rural rotation
   issue is therefore in the active-family/three-overlap branch, not a
   rank loss.
2. A nested exact-seven fragment occurs.
3. The two lost roles share one indispensable connected carrier or one
   common pool/reserve row.  For a common *literal* row, its two root
   occurrences are nevertheless distinct by Theorem 3.3, except at an
   exact-eight gate or the seven-vertex saturated atom.  Thus the live
   obstruction is connectivity of the two full role carriers, not literal
   portal multiplicity.

#### Proof

At an exact-seven minimum fragment, Corollary 3.2 and Theorem 5.5 of the
full-deletion note exclude loss of the four literal root coordinates,
modulo an exact-eight gate.  Theorem 3.3 does the same for two copies of
one common literal row, modulo that gate and the order-seven saturated
atom.  At an exact-eight descendant, Lemma 2.1
gives outcome 2 unless the opposite side is full.  With a full opposite
side, Lemma 2.2 restores the two roles whenever the missed row is private
to one role.  Negating these conclusions leaves only a row required on
both sides or a single connected carrier which both roles must consume.
QED.

The last outcome is narrower than the former bilateral exact-seven
axiom.  Its operation-sensitive form is now:

> **Common-row bilateral exchange.**  Two role families have distinct
> literal roots after every faithful internal operation, but both require
> one common carrier row which cannot be duplicated.  Either split that
> common carrier, match a full equality state across the two exact shores,
> or show that all occurrences of the common row lie in one compatible
> rural disk and hence in the coherent two-apex branch.

This remaining statement genuinely needs carrier geometry and the full
proper-minor state relation.  Portal rank, contraction of two selected
roots, and a private missed row no longer account for the failure.

## 5. Finite check on arbitrary four-lobe portal rows

The companion script `near_k7_contraction_role_loss_probe.py` records a
separate warning and guide.  If one drops the minimum-fragment Hall slack
and keeps only four exact-two portal sets, contraction-induced rank loss
has seven incidence types after the existing bouquet and unusable-
occurrence closures.  Six types have a literal `K_7` certificate with
branch bags of order at most three for all `6^4` missed-row profiles.  The
only type with profiles not closed by that small certificate is

\[
                       uv,uv,ab,cd,                    \tag{5.1}
\]

where the three pole pairs are mutually disjoint except for the repeated
contracted pair.  Thus even outside the minimum fragment the computational
residue is the same conceptual object: two roles consume one common
two-pole carrier, while the other roles do not provide an exchange path.
The script is exploratory evidence only; Corollary 4.1 is the hand-proved
result of this note.
