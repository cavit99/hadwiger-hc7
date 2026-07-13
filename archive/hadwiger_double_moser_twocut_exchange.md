# A two-separator in the double-Moser body: exact residual and portal-rank endpoint

## 1. Setting

Use the cut-irreducible double-Moser endpoint.  Thus (G) is
seven-connected and (K_7)-minor-free, the fixed interface is

\[
 I=\{x_1,x_2,x_3,x_4,a,b,p,q\},
\]

and the mandatory edges are those in (1.1) of
`hadwiger_double_moser_cutvertex_exchange.md`.  The remaining body
(R) is connected.  In this note let

\[
 Z=\{z_1,z_2\}\subseteq V(R)
\]

be a two-separator of (R), and let (D_1,\ldots,D_m) be the
components of (R-Z).  Because (R) has no cutvertex, every (D_i)
has a neighbour in each of (z_1,z_2).

For a lobe (D), put

\[
 \Delta(D)=I-N_I(D).
\]

No vertex of a lobe is adjacent to (u) or (v), and distinct lobes
are anticomplete.  Consequently

\[
 N_G(D)=Z\cup (I-\Delta(D)).                       \tag{1.1}
\]

Seven-connectivity gives

\[
 |\Delta(D)|\le 3.                                \tag{1.2}
\]

If equality holds, (1.1) is immediately a proper exact seven-cut.

## 2. Audit of the preceding cutvertex theorem

Theorem 4.1 of `hadwiger_double_moser_cutvertex_exchange.md` is sound.
Two points which are easy to miss were checked directly.

1. The residual-relation triangle test in
   `double_moser_cutvertex_lobe_probe.cpp` allows the three defect rows
   to repeat.  Thus its zero count excludes loops as well as ordinary
   triangles, and the proof remains valid when several lobes have the
   same defect.
2. If an actual defect has order at most one, enlarging it to a
   two-defect really is conservative.  Either the enlarged pair is
   positive or it is one of the exceptional pairs, in which case the
   actual row restores at least one omitted contact and the
   single-contact test is positive.

Every quotient model lifts because a component of (R-z) is connected
and is adjacent to (z).  The only qualification is terminological:
using an arbitrary exact seven-cut to replace the graph still requires
the separate exact-adhesion descent or colouring-gluing lemma.  The
minor-or-cut conclusion itself is unaffected.

## 3. Exact two-separator quotient

Contract two lobes to (d_1,d_2), retain (z_1,z_2), join both
separator vertices to both lobe vertices, and optionally retain the
edge (z_1z_2).  Delete all other separator-interface edges and all
surplus lobe contacts.

### Lemma 3.1 (the second separator vertex does not change the defect relation)

For two defects of order at most two, this conservative quotient is
(K_7)-minor-free for exactly the same twenty-two ordered pairs as the
cutvertex quotient.  Up to the double-Moser automorphism group and
interchange of the lobes, they have representatives

\[
\begin{aligned}
 &\{x_1,x_3\}\mid\{x_2,x_4\},\\
 &\{x_1,a\}\mid\{x_3,p\},\\
 &\{a,b\}\mid\{p,q\}.                         \tag{3.1}
\end{aligned}
\]

This is true whether or not (z_1z_2) is present.  The residual
relation is triangle-free, including repeated vertices, and restoring
one omitted lobe-interface contact is positive.

#### Verification

`double_moser_twocut_lobe_probe.cpp` exhausts all

\[
 (1+8+\tbinom82)^2=1369
\]

ordered pairs of defects of order at most two, for both states of
(z_1z_2).  Its exact connected-branch-set search reports

```text
separator_edge=0 profiles=1369 negative=22
separator_edge=1 profiles=1369 negative=22
```

and prints precisely the twenty-two rows already printed by the
cutvertex verifier.  One direction also has a conceptual proof: delete
(z_2) and the quotient is the old one-hub quotient.  The computation
certifies the nontrivial converse, namely that the additional common
neighbour (z_2), even together with (z_1z_2), repairs none of the
twenty-two rows.

### Theorem 3.2 (complete coarse two-cut trichotomy)

If (R) has a two-separator (Z), then at least one of the following
holds.

1. (G) has a (K_7)-minor.
2. Some lobe of (R-Z) lies behind the proper exact seven-cut
   (Z\cup(I-\Delta(D))).
3. (R-Z) has exactly two components (D,E), both defects have order
   two, and the ordered pair (Delta(D)\mid\Delta(E)) is one of the
   twenty-two exceptional pairs in Lemma 3.1.

#### Proof

A defect of order three gives outcome 2 by (1.1).  Suppose all defects
have order at most two.  If one has order at most one, choose any other
lobe and enlarge both rows to two-defects.  Lemma 3.1 and its
single-contact repair property give a (K_7)-minor.  Hence in a
minor-free residue every defect has order two.

If there are at least three lobes, every pair of their defects must lie
in the residual relation.  Three defects, with repetitions allowed,
would be a triangle in that relation, contrary to Lemma 3.1.  Thus
there are exactly two lobes.  A nonexceptional pair is positive, leaving
exactly outcome 3.  \(\square\)

The fourteen-vertex quotient consisting of the ten fixed core vertices,
(z_1,z_2,d,e), for any row in (3.1), is the smallest conservative
counterarchitecture to the false two-outcome assertion

\[
 \text{two-cut}\quad\Longrightarrow\quad K_7
       \text{ or an immediately visible exact seven-cut}.       \tag{3.2}
\]

It is only a quotient obstruction, not a seven-connected graph.

## 4. The structural invariant hidden in the twenty-two rows

For every exceptional pair the two defects are disjoint.  Put

\[
 M=\Delta(D)\mathbin{\dot\cup}\Delta(E),\qquad K=I-M.           \tag{4.1}
\]

Then (|M|=|K|=4), and (G[K]\cong 2K_2).  Thus the exceptional
two-cut has a four-label missing side and a common four-label literal
core.  More importantly, the separator vertices are locked to that
core.

### Lemma 4.1 (separator-contact repair)

In outcome 3 of Theorem 3.2, if

\[
 z_i y\in E(G)\quad\text{for some }y\in M,
\]

then (G) has a (K_7)-minor.  Consequently, in a (K_7)-minor-free
residue,

\[
                         N_I(z_1)\cup N_I(z_2)\subseteq K.       \tag{4.2}
\]

#### Proof

Suppose, for example, (y\in\Delta(D)) and (z_1y\in E(G)).  Use
(z_2) as the hub in the one-hub quotient and absorb (z_1) into the
connected lobe (D).  The bag (D\cup\{z_1\}) now has the restored
contact to (y); all other extra adjacencies are harmless.  The
single-contact restoration part of Lemma 3.1 supplies the (K_7)-model.
The other cases are symmetric.  \(\square\)

For reference, one explicit restored-contact model for each orbit in
(3.1) is listed below.  Here (d,e) are the two contracted lobes and
the restored edge is from (z_1) to the first displayed missing label.

\[
\begin{array}{c|l}
\{x_1,x_3\}\mid\{x_2,x_4\}&
 u\mid x_1\mid x_2\mid vx_3\mid qe\mid x_4ab\mid pz_1d\\
\{x_1,a\}\mid\{x_3,p\}&
 u\mid x_1\mid x_2\mid vx_4\mid qe\mid x_3ab\mid pz_1d\\
\{a,b\}\mid\{p,q\}&
 v\mid x_1\mid x_2\mid ux_3\mid be\mid x_4pq\mid az_1d.
\end{array}                                                     \tag{4.3}
\]

The verifier checks connectedness, disjointness and every pairwise bag
adjacency.  The absorption proof, rather than orbit symmetry, covers
all four missing labels in every one of the twenty-two ordered rows.

### Corollary 4.2 (surplus portal or degree-seven re-root)

Fix (z_i\in Z).  Unless (z_i) has two distinct neighbours in one
of (D,E), all of the following hold:

\[
 z_1z_2\in E(G),\qquad N_I(z_i)=K,\qquad d_G(z_i)=7,             \tag{4.4}
\]

and (z_i) has exactly one neighbour in each lobe.

#### Proof

Both lobes meet (z_i), because (R) is two-connected.  If neither
supplies two neighbours, these contribute exactly two neighbours.
By (4.2), (z_i) has at most four interface neighbours, and its only
other possible neighbour is the other member of (Z).  Minimum degree
seven forces all seven possible neighbours to occur, proving (4.4).
\(\square\)

Thus failure of portal multiplicity does not create a new arbitrary
case: it creates another adjacent degree-seven re-root over the common
(2K_2) core.

## 5. A label-free low-rank collapse

The C6 closure suggests measuring portal incidence rather than merely
which labels occur.  The following part of that transfer is completely
elementary and does not use Moser labels.

Let

\[
 O=\{a,b,p,q\},\qquad X=\{x_1,x_2,x_3,x_4\}.
\]

For a lobe (D), form the bipartite incidence graph between (D) and
(X), putting (d x) in the incidence graph exactly when (dx\in
E(G)).  Call its matching number the (X)-portal rank of (D).

### Lemma 5.1 (rank-one lobe collapse)

If a lobe (D) of a two-separator has (X)-portal rank at most one,
then either

1. a nonempty part of (D) lies behind a proper exact seven-cut; or
2. (D=\{t\}) is a singleton.

In outcome 2, if (D) belongs to the exceptional residue of Theorem
3.2, then

\[
 N_G(t)=Z\cup(I-\Delta(D)),\qquad d_G(t)=8.                    \tag{5.1}
\]

#### Proof

By König's theorem, one vertex covers every edge of the (D)-(X)
incidence graph.

If the cover is a boundary label (x\in X), then

\[
 N_G(D)\subseteq Z\cup O\cup\{x\},
\]

a set of order seven.  Seven-connectivity makes it an exact seven-cut.

Otherwise the cover is a shore vertex (t\in D).  If (D-t) is
nonempty, let (Y) be any component of (D-t).  It has no direct
neighbour in (X), no edge to another component of (D-t), and no
neighbour outside (I\cup Z\cup D).  Hence

\[
 N_G(Y)\subseteq Z\cup O\cup\{t\},
\]

again a set of order seven.  Seven-connectivity makes (N_G(Y)) an
exact seven-cut.  The only alternative is (D=\{t\}).  In the
exceptional residue, (1.1) and (|\Delta(D)|=2) give (5.1).  \(\square\)

This is the exact analogue of the orientation-free low-rank leaf step
in the audited (C_6\dot\cup K_1) proof.  The numerical shift is
instructive: there the surviving singleton had degree seven and Dirac's
bound closed it; here it has degree eight, so it feeds directly into the
degree-eight programme.

## 6. The remaining structural statement

For a connected split (C=C_a\dot\cup C_b) rooted at (a,b), define
the favourable cross-label set

\[
 F(C_a,C_b)=
 (N_X(C_a)\cap\{x_3,x_4\})\cup
 (N_X(C_b)\cap\{x_1,x_2\}).                    \tag{6.1}
\]

The explicit three-cross certificate in
`hadwiger_double_moser_edge_exchange.md` says that, once both carriers
meet (P),

\[
 |F(C_a,C_b)|\ge3\quad\Longrightarrow\quad K_7.                \tag{6.2}
\]

Thus the maximal bad cross states live in the six two-subsets of the
four cross labels, the bases of (U_{2,4}).  The finite defect atlas has
now been exhausted; the next missing theorem is the following genuinely
structural leaf exchange.

> **Rank-two SPQR leaf exchange.**  In a two-connected exceptional
> two-lobe residue, either a leaf flip produces a connected split with
> three favourable cross labels, or one leaf interior has (X)-portal
> rank at most one.

The second outcome is already closed by Lemma 5.1 up to the explicit
degree-eight singleton (5.1); the first is closed by (6.2).  Proving
this exchange requires the same orientation-free ingredient as in the
(C_6) closure: apply the Two Paths web to four portal representatives,
use the basis-intersection interval property of their transversal
matroid, and treat the crossed four-cycle as the direct-minor outcome
rather than as a counterexample.  This note does **not** claim that
exchange without proving the missing synchronization of the four portal
sets.

The exact residue is therefore no longer “an arbitrary 2-connected
body”.  It is either

* a (U_{2,4}) rank-two leaf whose web orientations still need to be
  synchronized; or
* a singleton degree-eight lobe with the exact neighbourhood (5.1); or
* the adjacent degree-seven re-root in (4.4).

