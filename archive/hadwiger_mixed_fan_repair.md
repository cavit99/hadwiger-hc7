# Repair of the mixed-fan gap: a fan-refined extremal model

## 1. Purpose and scope

The implication used in `hadwiger_hybrid_fan_absorption.md`, Theorem 5.2,

> no fan has an all-clean SPPA package \(\Longrightarrow\) every portal of every
> maximum fan is rigid,

is invalid.  A maximum fan may mix rigid portals with non-direct strongly
private non-cut portals.  The result below avoids that implication.  It changes
the extremal choice of the clique model and proves exactly the following:

> There is a contact-maximal spanning \(K_6\)-model and a length-minimum
> maximum \(v\)-to-noncontact-side fan for that model such that every portal of
> this one fan is rigid.

It does **not** prove that every old \(\Phi\)-maximal model is an RPC, nor that
every maximum fan of the selected model is all-rigid.

Throughout, paths in a \(v\)-to-\(C\) fan are truncated at their first vertex
in \(C\).  Their length is their number of edges.

## 2. Definitions

Let \(G\) be a finite graph, let \(v\in V(G)\), and suppose \(G-v\) contains a
\(K_6\)-model
\[
\mathcal B=(B_1,\ldots,B_6).
\]
Put
\[
S(\mathcal B)=\{i:N(v)\cap B_i\ne\varnothing\},\qquad
s(\mathcal B)=|S(\mathcal B)|,
\]
\[
J(\mathcal B)=[6]\setminus S(\mathcal B),\qquad
C(\mathcal B)=\bigcup_{j\in J(\mathcal B)}B_j,
\]
and
\[
Z(\mathcal B)=V(G-v)\setminus\bigcup_{i=1}^6B_i.
\]
Assume that no fully contacted \(K_6\)-model exists at \(v\); otherwise
\(\{v\},B_1,\ldots,B_6\) is already a \(K_7\)-model.  Thus
\(C(\mathcal B)\ne\varnothing\) for every model under consideration.

Let \(\mu(\mathcal B)\) be the maximum cardinality of a family of pairwise
internally vertex-disjoint \(v\)-to-\(C(\mathcal B)\) paths.  Common endpoints
in \(C(\mathcal B)\) are allowed; only their interiors must be disjoint.  Let
\(\ell(\mathcal B)\) be the minimum, over all such families of cardinality
\(\mu(\mathcal B)\), of the sum of their lengths.  These integers exist because
\(G\) is finite.

Define the fan-refined potential
\[
\Psi(\mathcal B)=
\left(
s(\mathcal B),
-|Z(\mathcal B)|,
\mu(\mathcal B),
-\ell(\mathcal B),
-\sum_{i=1}^6|B_i|^2
\right)
\]
with lexicographic order.  The last coordinate is inessential for the theorem;
it merely makes explicit that further tie-breaking is allowed.

A portal \(\alpha\in B_i\cap N(C)\) is **strongly private non-cut** if

1. \(B_i-\alpha\) is nonempty and connected;
2. \(N(v)\cap(B_i-\alpha)\ne\varnothing\); and
3. for every \(k\ne i\), there is a \(B_i-\alpha\)-to-\(B_k\) edge.

This is equivalent to the three operative conditions in the earlier
definition: non-cut removability, residual contact, and no unique cross-bag
attachment.  A portal is **rigid** if at least one of these conditions fails
(types (R1), (R2), and (R3), respectively).  A portal is **direct** if it lies
in \(N(v)\).

## 3. The one-portal move, including the non-direct case

### Lemma 3.1 (single clean-portal transfer)

Let \(\alpha\in B_i\cap N(C)\) be strongly private non-cut, and choose
\(j\in J\) and \(y\in B_j\) with \(\alpha y\in E(G)\).  Set
\[
B_i'=B_i\setminus\{\alpha\},\qquad
B_j'=B_j\cup\{\alpha\},\qquad
B_k'=B_k\quad(k\notin\{i,j\}).
\]
Then \(\mathcal B'=(B_1',\ldots,B_6')\) is a \(K_6\)-model.  Moreover:

* if \(\alpha\in N(v)\), then \(s(\mathcal B')=s(\mathcal B)+1\);
* if \(\alpha\notin N(v)\), then \(S(\mathcal B')=S(\mathcal B)\),
  \(J(\mathcal B')=J(\mathcal B)\), and
  \[
  C(\mathcal B')=C(\mathcal B)\cup\{\alpha\};
  \]
* in both cases \(Z(\mathcal B')=Z(\mathcal B)\).

#### Proof

The first condition makes \(B_i'\) nonempty and connected, and
\(\alpha y\) makes \(B_j'\) connected.  The branch sets remain disjoint.
Every old cross-edge not incident with \(B_i\) survives.  For every
\(k\ne i\), condition 3 gives an edge from \(B_i'\) to \(B_k\), including
\(k=j\).  All old cross-edges incident with \(B_j\) also survive because
\(B_j\subseteq B_j'\).  Hence the six new branch sets are again pairwise
adjacent.

Condition 2 retains contact at index \(i\).  If \(\alpha\in N(v)\), the
formerly noncontact index \(j\) gains contact, so \(s\) rises by one.  If
\(\alpha\notin N(v)\), then \(B_j'\) is still noncontact and the contact-index
sets do not change.  In that case the union of the noncontact bags gains
exactly \(\alpha\).  Finally, the union of all six bags is unchanged, so \(Z\)
is unchanged.  \(\square\)

## 4. Fan-refined extremality

### Lemma 4.1 (a \(\Psi\)-maximizer is spanning)

Assume \(G-v\) is connected.  Every \(\Psi\)-maximal \(K_6\)-model has
\(Z=\varnothing\).

#### Proof

Suppose \(Z\ne\varnothing\).  Since \(G-v\) is connected, some vertex
\(z\in Z\) has a neighbour in a branch set, say \(z x\in E(G)\) with
\(x\in B_i\).  Replacing \(B_i\) by \(B_i\cup\{z\}\) preserves the
\(K_6\)-model.  Its contact count does not decrease (and may increase), while
\(|Z|\) decreases by one.  Therefore the first changed coordinate of \(\Psi\)
is an improvement, contradicting maximality.  \(\square\)

### Theorem 4.2 (all-rigid fan at a fan-refined extremum)

Assume \(G-v\) is connected and no fully contacted \(K_6\)-model exists at
\(v\).  Choose a \(\Psi\)-maximal \(K_6\)-model \(\mathcal B\), and, for this
model, choose a maximum \(v\)-to-\(C(\mathcal B)\) fan \(\mathcal P\) whose
total length is \(\ell(\mathcal B)\).  Then every portal of \(\mathcal P\) is
rigid.

#### Proof

By Lemma 4.1 the model is spanning.  Let \(P\in\mathcal P\), let \(y\) be its
first vertex in \(C=C(\mathcal B)\), and let \(\alpha\) be the predecessor of
\(y\) on \(P\).  Suppose for a contradiction that \(\alpha\) is strongly
private non-cut.  Let \(y\in B_j\), and perform the transfer of Lemma 3.1.

If \(\alpha\in N(v)\), then the first coordinate \(s\) increases, immediately
contradicting \(\Psi\)-maximality.

It remains that \(\alpha\notin N(v)\).  Lemma 3.1 gives
\[
s(\mathcal B')=s(\mathcal B),\qquad
Z(\mathcal B')=Z(\mathcal B),\qquad
C(\mathcal B')=C\cup\{\alpha\}.
\]
Replace \(P\) by its initial subpath from \(v\) to \(\alpha\), and leave every
other member of \(\mathcal P\) unchanged.  This is a
\(v\)-to-\(C(\mathcal B')\) fan of the same cardinality.  Indeed,
\(\alpha\notin C\), and internal disjointness of the old fan implies that no
other member uses \(\alpha\).  Thus
\[
\mu(\mathcal B')\ge \mu(\mathcal B).
\]
If the inequality is strict, the third coordinate of \(\Psi\) improves.  If
equality holds, the displayed fan has total length
\(\ell(\mathcal B)-1\), since the old paths were truncated at their first
\(C\)-vertices and the deleted final edge is \(\alpha y\).  Consequently
\[
\ell(\mathcal B')\le \ell(\mathcal B)-1,
\]
so the fourth coordinate of \(\Psi\) improves.  Either conclusion contradicts
\(\Psi\)-maximality.  Hence \(\alpha\) is rigid.  Since \(P\) was arbitrary,
all portals of \(\mathcal P\) are rigid.  \(\square\)

### Corollary 4.3 (the minimal \(\mathrm{HC}_7\) setting)

Let \(G\) be a hypothetical minimal counterexample to \(\mathrm{HC}_7\).
For every \(v\), there is a spanning contact-deficient \(K_6\)-model and a
length-minimum maximum \(v\)-to-noncontact-side fan whose portal set \(L\)
consists entirely of rigid vertices.  Moreover \(|L|\ge7\).

#### Proof

The minimal-counterexample package gives a \(K_6\)-model in \(G-v\), no fully
contacted one, and \(G-v\) connected.  Apply Theorem 4.2.  Fix any \(y\in C\).
Since \(\kappa(G)\ge7\), Menger's theorem gives seven internally disjoint
\(v\)-to-\(y\) paths.  Truncating each at its first entry into \(C\) gives an
allowed common-end \(v\)-to-\(C\) family, so \(\mu=|L|\ge7\).  \(\square\)

## 5. Audit of the existing \(s=1\) and \(s=2\) work

The theorem supplies one all-rigid fan, which is enough for all statements
that only inspect a single portal set \(L\).  It does not supply the old RPC
quantifier "every portal of every maximum fan is rigid," and \(\Psi\)-maximality
does not imply maximality of the old
\(\Phi=(s,-|Z|,-\sum|B_i|^2)\).

### 5.1 Statements that survive for the selected model and fan

Under the minimal-\(\mathrm{HC}_7\) hypotheses, the following remain valid:

1. \(Z=\varnothing\), \(s\le5\), \(|L|\ge7\), and all vertices of \(L\) are
   rigid (Corollary 4.3).
2. Portal-load pigeonholes, including a multi-portal bag and the
   "one triple-portal bag or two double-portal bags" alternative.
3. The double-foot conclusion: \(\delta(G)\ge7\) and \(s\le5\) force some
   contact bag to contain at least two neighbours of \(v\).
4. At most one portal in a fixed bag can be of type (R2), and no portal in a
   multi-contact bag can use (R2).
5. Every unique-attachment target has at most one claiming vertex in a fixed
   source bag.  All elementary \(U(\alpha)\)-budget inequalities therefore
   survive.
6. In the \(s=1\) cell, all portals lie in the sole, necessarily
   multi-contact bag.  At most five of the at least seven portals can have
   nonempty \(U(\alpha)\).  Hence at least two selected-fan portals have
   \(U(\alpha)=\varnothing\), and their rigidity must be of type (R1): they are
   cutvertices of the sole contact bag.
7. Any explicitly verified reassignment whose final model has larger contact
   count is still forbidden: the first coordinate of \(\Psi\), just as of
   \(\Phi\), is \(s\).  Thus genuinely free component absorptions that raise
   contact remain valid sublemmas.

These conclusions use neither simultaneous SPPA nor the false dichotomy.

### Lemma 5.1 (what replaces the old \(s=1\) freeness assertion)

Assume \(s=1\), write the sole contact bag as \(B_1\), and let
\(\alpha\in L\) be a cutvertex portal with \(U(\alpha)=\varnothing\).  Let
\(K\) be a component of \(B_1-\alpha\) which contains the
\(N(v)\)-to-portal prefix of another member of the selected fan.  Suppose also
that \(N(v)\cap(B_1\setminus K)\ne\varnothing\).  Define the private-target
set of the whole component by
\[
T(K)=\{j\in J:\text{ every }B_1\text{-to-}B_j\text{ edge has its }B_1
\text{ endpoint in }K\}.
\]
Then \(|T(K)|\ge2\).

#### Proof

The fan prefix shows that \(K\) contains a neighbour of \(v\) and a vertex
adjacent to \(C\).  Suppose \(|T(K)|\le1\).  If \(T(K)=\varnothing\), choose
a noncontact bag \(B_j\) met by the portal edge from \(K\) to \(C\).  If
\(T(K)=\{j\}\), choose that \(B_j\); by its definition, \(K\) meets
\(B_j\).

Move all of \(K\) into \(B_j\).  The residual set \(B_1-K\) is connected:
it consists of \(\alpha\) together with the other components of
\(B_1-\alpha\).  The enlarged \(B_j\) is connected.  For every
\(k\ne j\), the fact that \(k\notin T(K)\) leaves a residual
\((B_1-K)\)-to-\(B_k\) edge.  If \(T(K)=\varnothing\), the same is true for
\(k=j\).  If \(T(K)=\{j\}\), an edge from \(\alpha\) to a vertex of the
component \(K\) becomes a \((B_1-K)\)-to-\(B_j\cup K\) edge.  All other
branch-set adjacencies survive unchanged.  Thus this is a \(K_6\)-model.

The hypothesis outside \(K\) retains contact at \(B_1\), while the neighbour
of \(v\) inside \(K\) gives contact to the formerly noncontact \(B_j\).
Hence \(s\) increases, contradicting the first coordinate of \(\Psi\).
Therefore \(|T(K)|\ge2\).  \(\square\)

Thus the valid \(s=1\) residual is sharper than merely "some private edge":
each fan-relevant component with residual contact outside it must monopolise
at least two of the five noncontact targets.  A component containing all of
\(N(v)\) is not covered by the lemma.

### 5.2 Statements that do not automatically transfer

The following parts of the old locked-core programme require new proofs:

1. The definition and reduction to a hard-core RPC.  Theorem 4.2 gives one
   all-rigid fan, not rigidity for every maximum or root fan.
2. Pure-(R2) size bounds, \(\Phi\)-neutral trades, and the assertion that a
   neutral maximizer remains hard-core.  A transfer that is neutral or
   improving in \(-\sum|B_i|^2\) may decrease \(\mu\) or increase \(\ell\), so
   it need not preserve \(\Psi\)-extremality.
3. The singleton-\(U\) descents in `hadwiger_G7lock_s2_s5.md`, Lemmas
   0.6--0.11 and Definition B.3.  Consequently the terminal bound in Theorem
   B.4, and hence the claimed elimination of \(s=2\), does not follow for the
   \(\Psi\)-selected model.
4. The \(s=2\) cutvertex ban (Theorem B.1) assumes the locked-core axiom that
   every relevant cut side has a private target of the asserted kind.  The
   existence of one all-rigid fan does not establish that axiom.
5. In the \(s=1\) cell, the budget argument still forces cutvertex portals,
   but the final contradiction does not yet follow.  The step called "no mixed
   \(N(v)\)-to-\(C\) component" (old Theorem 3.6) uses hard-core freeness.  Fan
   disjointness alone only shows that another fan path produces a component of
   \(B_1-\alpha\) meeting both \(N(v)\) and \(\partial C\); it does not show
   that this component has no irreplaceable private cross-edge.  Thus old
   Theorem 3.7 cannot be invoked without repairing Theorem 3.6.

The same warning applies a fortiori to the locked \(s=3,4,5\) reductions.

## 6. Exact new residual gap

The mixed-fan logical gap itself can be bypassed by Theorem 4.2.  The remaining
work on this route is:

> Starting from the \(\Psi\)-extremal spanning contact-deficient model and its
> one length-minimum maximum all-rigid fan, eliminate the resulting rigid
> configuration without using old \(\Phi\)-neutral trades unless those trades
> are also proved not to decrease \((\mu,-\ell)\).

Already at \(s=1\), the precise first unresolved cell is a selected-fan
cutvertex portal \(\alpha\) for which every fan-relevant
\(N(v)\)-to-\(\partial C\) component of \(B_1-\alpha\) either contains all
of \(N(v)\) or monopolises at least two noncontact targets (Lemma 5.1).  At
\(s=2\), the first unresolved step is the locked-side assertion preceding the
singleton-\(U\) descent.
