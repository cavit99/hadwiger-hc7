# Four common owners: rooted completion or an exact zero row

## 1. The reserve test after a rooted core has been selected

The following is the exact interface between the four-common-owner lock
and the uniform biportal rooted-core theorem.  It is stated without Moser
labels.

### Lemma 1.1 (free reserve or a literal zero row)

Let `P_0,P_1,F_1,F_2,F_3,F_4` be pairwise disjoint nonempty connected
sets in a graph `G`.  Assume

1. `P_0` and `P_1` are adjacent;
2. `F_1,...,F_4` are pairwise adjacent; and
3. every `F_i` is adjacent to both `P_0` and `P_1`.

Put

\[
 Z=G-\left(P_0\cup P_1\cup F_1\cup\cdots\cup F_4\right). \tag{1.1}
\]

Then either `G` contains a `K_7` minor, or every component `C` of `Z`
has a zero in the incidence row

\[
 \bigl(C\sim P_0,\ C\sim P_1,\ C\sim F_1,\ldots,C\sim F_4\bigr). \tag{1.2}
\]

#### Proof

If one component `C` has all six incidences in (1.2), use

\[
                    F_1,F_2,F_3,F_4,C,P_0,P_1.       \tag{1.3}
\]

These sets are disjoint and connected.  The first four are pairwise
adjacent, `C` sees all six other bags, both pools see every `F_i`, and the
pools see one another.  Thus (1.3) is a `K_7` model.  The contrapositive
is exactly the zero-row conclusion.  \(\square\)

There is a parameter-uniform version: replace the four protected bags by
a protected `r`-frame.  A free component with all `r+2` incidences gives
`K_{r+3}`.  The rooted-core theorem in
`hadwiger_biportal_rooted_k4_web_exchange.md` manufactures the protected
frame as

\[
                         F_i=L_i\cup E_i,            \tag{1.4}
\]

where `L_i` are rooted clique bags in a torso and the extensions `E_i`
are disjoint and biportal.  Consequently, after a rooted core and its
extensions have been selected, reserve failure is not vague “bad portal
placement”: it is precisely (1.2).

### Corollary 1.2 (zero row or shared protected material)

Suppose the required reserve contacts exist in several pieces but no
single component of the free graph (1.1) has all of them.  Any connected
set combining those pieces must meet

\[
                    P_0\cup P_1\cup F_1\cup\cdots\cup F_4. \tag{1.5}
\]

Hence it cannot be used as a seventh branch bag disjoint from (1.3).
Equivalently, every attempted completion either has a literal zero row on
one free component or consumes a pool/protected extension already used by
the rooted model.  In the torso language the latter is exactly the
shared-lobe (or shared-adhesion) state; it is not a new third obstruction.

#### Proof

Distinct components of `Z` have no edge between them.  A path joining two
therefore leaves `Z` and meets its deleted set, which is (1.5).  \(\square\)

## 2. What the homogeneous cross already forces

Let a distinct-class society cross split one exceptional piece into
adjacent connected sides `P_0,P_1`.  In an inclusion-maximal negative
homogeneous row of `near_k7_exceptional_cross_split_atlas.py`, the two
sides have exactly four common external owner classes.

Those four classes are:

* pairwise disjoint actual model pieces or singleton labels;
* connected; and
* adjacent to both `P_0` and `P_1` by the definition of common ownership.

Thus the disjointness and both pool columns required by the biportal
completion are already forced at class level.  Two assertions are **not**
forced by common ownership:

1. the four extensions have a rooted `K_4` after their torso paths are
   expanded without overlap; and
2. a fifth connected reserve is disjoint from them and has a positive row
   against the four rooted bags and both pools.

The torso--Helly and rooted-`K_4` web theorems address item 1.  Once item 1
has succeeded, Lemma 1.1 says that item 2 has the exact zero-row/shared-
lobe negation above.

## 3. A sharp quotient witness: rooted core present, reserve row zero

The first maximal row for the homogeneous profile `(c,c,a)`, with the
first piece split, is

\[
\begin{aligned}
 P_0&\sim\{a,b,q_1,q_2,q_3,X_2\},\\
 P_1&\sim\{q_1,q_2,q_3,X_2\}.                       \tag{3.1}
\end{aligned}
\]

The four common owners

\[
                         q_1,q_2,q_3,X_2             \tag{3.2}
\]

induce a literal `K_4`: the `q_i` form the neutral triangle and `X_2` is
adjacent to all of them.  Hence this row already has the rooted core and
four disjoint biportal extensions in their strongest singleton form.

Delete the six protected vertices in (3.1)--(3.2).  The remaining owner
classes have two components,

\[
                              \{a\},\qquad\{b,c,X_3\}. \tag{3.3}
\]

Both are anticomplete to `P_1`.  They see the four core vertices and the
other pool, but have a literal zero in the `P_1` column.  Thus no free
reserve exists.  The exhaustive quotient verifier finds no `K_7` minor.
The replay in `near_k7_four_common_zero_row_verify.py` checks all of these
claims independently.

This witness proves that four common owners, even when they already form
a rooted `K_4`, do not statically force closure.  The minimum missing
capacity is one fifth biportal reserve row.

## 4. Reserve-tree interpretation

The reserve-tree analysis reaches the same state before contraction.  In
the target-free owner branch, every off-core lobe hit by the opposite
side is dark to one common label `s^*` (Corollary 10.2 of
`hadwiger_near_k7_tree_society_split_2apex.md`).  Each such lobe is a
candidate free reserve component and its `s^*` entry is literally zero.
The strict attachment surplus increases the number of its attachments to
the reserve core but does not change that zero.

Combining several dark lobes requires a path through the reserve core or
through a protected extension.  If that core has already been allocated
to the rooted `K_4` bags, this is precisely the shared-lobe alternative of
Corollary 1.2.  The explicit strict-surplus tree society in Section 11 of
that note shows that all static cut inequalities can coexist with this
common zero row.  It is an interface counterarchitecture rather than a
seven-connected host, so proper-minor state exchange may still exclude
it; connectivity and portal counts alone do not.

## 5. Exact remaining condition

The four-common-owner homogeneous lock is therefore reduced to the
following literal selection problem.

> Select a rooted `K_4` with four pairwise disjoint biportal extensions.
> In the remaining free graph, either find one component with a positive
> incidence to the four rooted bags and both pools, or use a
> deletion/contraction state transition to fill the named zero without
> consuming a protected extension.

The first outcome is `K_7` by Lemma 1.1.  Failure is exactly a zero row or
shared protected lobe.  No broader phrase such as “unresolved portal
placement” is needed.
