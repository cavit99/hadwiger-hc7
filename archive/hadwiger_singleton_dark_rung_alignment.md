# The dark singleton rung: aligned detours close, contaminated detours remain

## 1. Setting

Retain the potential-maximal spanning rooted model

\[
                         K_0,K_j,L,M                         \tag{1.1}
\]

from `hadwiger_rooted_core_dark_bag_split.md`.  Put

\[
                         A=\{a,c\},\qquad C=\{1,2\}.         \tag{1.2}
\]

Assume, after symmetry, that (K_0) is anticomplete to (A), while
(K_j) meets (A).  The potential is the number of incidences between
the four rooted bags and the two groups (A,C), and has been maximized
over all spanning rooted models with the same four prescribed
(b)-roots.

Suppose an edge (xy\in E(K_j)) gives a connected split

\[
                         K_j=X\mathbin{\dot\cup}Y,qquad
                         x\in X, y\in Y,                      \tag{1.3}
\]

where \(X\) contains an \(A\)-portal and \(Y\) retains

* the prescribed (b)-root of (K_j);
* an edge to each of (K_0,L,M); and
* every (A,C)-incidence originally charged to (K_j).

The only missing condition for the standard peel is an \(XK_0\)-edge.
Delete \(xy\).  Minor-criticality supplies a six-colouring in which
\(x,y\) have one colour \(\alpha\), and for every other colour
\(\beta\) an \(\alpha/\beta\)-path joins \(x\) to \(y\).

## 2. A bag-aligned Kempe detour is the missing peel

### Theorem 2.1 (aligned-detour peel)

If one of the five edge-Kempe paths (P) satisfies

\[
 V(P)-\{y\}\subseteq X\cup K_0
 \quad\hbox{and}\quad V(P)\cap K_0\ne\varnothing,              \tag{2.1}
\]

then the rooted model can be changed so that (K_0) gains an
(A)-incidence and (K_j) loses none of its protected incidences.
Consequently (2.1) is impossible in a potential-maximal model.  If
(K_0) was the sole bag missing a group, already met (C), and the
other three bags met both groups, then (2.1) directly gives a
(K_7)-minor.

#### Proof

Put

\[
 K'_0=K_0\cup X,qquad K'_j=Y.                              \tag{2.2}
\]

The first set is connected.  Indeed, follow (P) from (x\in X) to
its first vertex in (K_0); its preceding vertices lie in (X) by
(2.1), and then the connected bag (K_0) is reached.  The set (Y) is
connected by (1.3).  The two new bags are adjacent both through the old
edge (xy) and through the last (K_0)-to-(y) transition on (P)
(if the latter is used).

The bag (K'_0) retains every old adjacency and its old (b)-root, and
gains the (A)-contact in (X).  The bag (K'_j) retains its root,
its edges to (K_0,L,M), and all group incidences by hypothesis.
Thus (2.2), together with (L,M), is again a spanning rooted
(K_4)-model, and its potential is strictly larger.  This contradicts
maximality.

Under the stated direct-completion hypotheses, all four new bags meet
both (A,C).
The seven explicit bags are

\[
 K'_0\mid K'_j\mid L\mid M\mid\{b\}\mid A
                    \mid(\{d\}\cup C).                       \tag{2.3}
\]

The first four form the rooted clique model; (b) sees their prescribed
roots and both final bags; (A=ac) and ({d}\cup C) are connected;
and both final bags see all four rooted bags.  Hence (2.3) is a
(K_7)-model. \(\square\)

### Corollary 2.2 (five contaminated detours)

At a potential-maximal critical rung, all five bichromatic detours are
**contaminated**: each either avoids (K_0), or between its first visit
to (K_0) and its arrival at (y), or before that first visit, it uses
an internal vertex of

\[
             Y\cup L\cup M\cup\bigl(B\cup\{d\}\bigr).         \tag{2.4}
\]

Thus the transition atlas does act on the rooted model whenever one
colour is bag-aligned.  The exact remaining obstruction is simultaneous
contamination of all five colours by the protected bags or boundary.

#### Proof

If a path meets (K_0) and has no contaminating vertex, truncate loops
if necessary.  Every internal vertex then belongs to (X\cup K_0), so
(2.1) holds.  Apply Theorem 2.1.
\(\square\)

The conclusion is genuinely colour-sensitive: detours for distinct
\(\beta\)'s may meet only in \(\alpha\)-coloured vertices, but they may
all use the same \(\alpha\)-coloured contaminating portal.  No
disjointness of the five paths is asserted.

### Lemma 2.3 (distinct exits or a doubled alpha portal)

Put (R=X\cup K_0).  For each of the five colours
(\beta\ne\alpha), choose an (\alpha/\beta) detour and let
(z_\beta) be its first vertex outside (R).  Then either

1. the five vertices (z_\beta) are distinct; or
2. some (\alpha)-coloured vertex (z\notin R) has two distinct
   neighbours in (R), of two distinct colours
   (\beta,\gamma\ne\alpha).

More generally, if one exit vertex is used by (s) detours, it is
(\alpha)-coloured and has (s) distinct predecessors in (R), one
in each of the (s) other colours.

#### Proof

The first exit on an (\alpha/\beta)-path has colour (\alpha) or
(\beta).  If (z_\beta=z_\gamma) for distinct
(\beta,\gamma), the common vertex belongs to both two-colour palettes,
so it has colour (\alpha).  Its predecessor on the
(\alpha/\beta)-path has colour (\beta), and its predecessor on the
(\alpha/\gamma)-path has colour (\gamma).  Those predecessors are
distinct and lie in (R) by the definition of first exit.  The same
argument proves the (s)-fold statement. \(\square\)

Thus simultaneous contamination has a second exact form: it exports
five distinct coloured portals from (R), or creates a multiply-hit
external (\alpha)-hub.  A future splitter may act on this hub, but it
cannot call the five Kempe paths disjoint.

### Theorem 2.4 (clean multi-bag contamination is absorbable)

For each rooted bag (H\in\{L,M\}), choose a connected protected core
(W_H\subseteq H) containing its prescribed (b)-root, the endpoint of
one fixed retained edge to each other rooted bag, one retained portal
for every one of the groups (A,C) seen by (H), and
(h,r) when present.  Thus deleting any union of components of
(H-W_H) leaves a connected bag with all protected data.

The fixed edges are chosen coherently: the selected \(LM\)-edge has
both endpoints in \(W_L,W_M\); for an \(HK_j\)-edge its \(K_j\)-end
lies in the protected residual \(Y\); and for an \(HK_0\)-edge its
\(K_0\)-end remains in the unchanged core \(K_0\).  Such a choice is
possible because \(Y\) retains an edge to each of \(L,M\) by (1.3).

Let (P) be one of the five (x)-(y) detours and suppose it meets
(K_0).  Let (P_0) be the segment from (x) through its first vertex
of (K_0).  Assume

1. (P_0) avoids (B\cup\{d\});
2. before reaching (K_0), its vertices in (K_j) all lie in (X);
   and
3. for (H=L,M), every vertex of (P_0\cap H) lies in components of
   (H-W_H) disjoint from (W_H).

Then the rooted model can be reallocated so that (K_0) gains the
(A)-incidence of (X) and no other bag loses protected data.
Consequently no such detour exists at maximum potential.

#### Proof

For (H=L,M), let (mathcal C_H) be the set of components of
(H-W_H) met by (P_0), and put

\[
 S=X\cup V(P_0)\cup
       \bigcup_{H=L,M}\bigcup_{C\in\mathcal C_H}V(C).          \tag{2.5}
\]

Move (S-K_0) into (K_0), replace (K_j) by (Y), and replace
each intermediate bag (H) by

\[
                         H'=H-\bigcup_{C\in\mathcal C_H}V(C). \tag{2.6}
\]

The enlarged (K'_0=K_0\cup S) is connected along (P_0), and every
whole off-core component added to it is connected to a vertex of that
path.  The bag (Y) is connected.  Each (H') is connected because it
contains (W_H), and every unremoved component of (H-W_H) has an edge
to (W_H).

All rooted bags remain disjoint and spanning.  Every required model
adjacency, root and group incidence has a representative in the
coordinated protected cores; (Y) retains the donor data by (1.3).  The old edge
(xy) supplies the new (K'_0Y)-adjacency.  Finally (K'_0) gains the
(A)-portal in (X).  Hence the potential strictly increases, contrary
to maximality. \(\square\)

This closes every detour contaminated only by removable off-core lobes,
even when it visits both other rooted bags many times.  The surviving
contamination is forced to hit an actual protected core or boundary
vertex before its first (K_0)-visit, or to avoid (K_0) altogether.

## 3. The equality data alone do not align a root bag

The degree-(b=9) equality case gives four rainbow (b)-portals,
complete pairwise bichromatic connectivity among them, and a rooted
(K_4).  The following exact quotient shows that those facts, together
with a unique dark root, still do not determine the needed peel.

Let (Q_\star) have vertices

\[
 q_0,q_1,q_2,q_3,b,d,a,c,1,2.                         \tag{3.1}
\]

Make (q_0q_1q_2q_3) a (K_4), make (b) adjacent to every other
vertex, add

\[
 d\sim a,c,1,2,q_0,q_1,qquad ac,12,                  \tag{3.2}
\]

and give the four boundary-contact rows

\[
\begin{array}{c|c}
a&q_0,q_1,q_2\\
c&q_0,q_1\\
1&q_0,q_1,q_2,q_3\\
2&q_0,q_1.
\end{array}                                           \tag{3.3}
\]

Here (q_0,q_1) are the two bags containing the contracted (h,r)
roles.  The vertex (q_3) is the unique (A)-dark root, while every
other root meets both (A) and (C).  Also

\[
                         d_{Q_\star}(b)=9,qquad
                         d_{Q_\star}(d)=7.             \tag{3.4}
\]

### Proposition 3.1 (sharp quotient counterarchitecture)

The graph (Q_\star) has no (K_7)-minor.

Nevertheless its four roots induce (K_4).  They can therefore be
coloured with four distinct colours, and every two roots lie in the same
bichromatic component (their edge).  Thus “four rainbow roots + complete
Kempe connectivity + exactly one dark root” does not, at branch-quotient
level, imply the rooted-core completion.

#### Verification

`singleton_hub_k4_contact_atlas.cpp` exhausts every partition of every
subset of the ten vertices into seven nonempty connected branch sets.
For the rows (3.3) it returns negative.  The same program enumerates all
root-contact supergraphs: in the case where the (h,r) roles lie in
different bags, 691 of 1024 patterns are positive and 333 are negative;
the pattern (3.3) is one of the 52 maximal negative patterns.  Adding any
contact which dominates a maximal row is checked against an explicit
branch-set search.

The proposition is a finite graph statement and can also be checked
directly by the following elementary exhaustive criterion: a (K_7)
model on ten vertices has total branch-set excess at most three, so its
possible bag-size types are

\[
 1^7,\quad 2\,1^6,\quad 2^2 1^5,\quad3\,1^6,\quad
 2^3 1^4,\quad3\,2\,1^5,\quad4\,1^6,          \tag{3.5}
\]

with arbitrary unused vertices.  The verifier tests exactly these
types. \(\square\)

This does not purport to be a seven-connected counterexample: (Q_\star)
is the exact contracted branch interface.  Its role is adversarial.  It
proves that any successful equality-case theorem must use uncontracted
bag geometry or a detour satisfying Theorem 2.1; static rainbow/Kempe
root data cannot supply the missing adjacency.

## 4. Exact theorem-strength blocker

The combination of the transition atlas and Theorem 2.1 leaves one
specific joint statement, rather than a further state list:

> In the degree-(b=9) singleton endpoint, a potential-maximal dark
> rooted model cannot have all five detours at its specified critical
> rung contaminated as in (2.4).

Proving this requires a *joint* colour/model lemma.  The transition
colouring and the Strong-(HC_4) rooted model arise from different minor
colourings, and no current argument identifies a colour class with a
fixed branch bag.  Proposition 3.1 shows that such an identification
cannot be inferred after contracting the bags.  A valid next step must
either uncross the five detours in the uncontracted model or turn their
common contaminating \(\alpha\)-portal into a separator of order at most
six.
