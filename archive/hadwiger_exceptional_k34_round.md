# The exceptional (K_3\dot\cup K_4) neighbourhood: rooted helpers and the remaining two-side lock

This note treats the exceptional degree-seven cell only.  It proves two
new eliminations:

1. the sole exterior component has at least eight vertices (the last
   two steps are computer-assisted); and
2. no cutvertex of the exterior component has three or more sides.

It also records a precise connected-partition formulation of what remains.
It does **not** eliminate the whole exceptional cell.

## 1. Standing hypotheses and the right target

Let (G) be a hypothetical proper-minor-minimal counterexample to
\(\mathrm{HC}_7\), let (v\) have degree seven, and suppose

\[
 N=N_G(v)=A\mathbin{\dot\cup}B,
 \qquad G[A]\cong K_3,\qquad G[B]\cong K_4,
\]

with no edge between (A) and (B).  Let

\[
 C=G-N[v].
\]

The preceding reduction shows that (C) is one nonempty connected
component.  We use

\[
 \delta(G)\geq7,\qquad \kappa(G)\geq7.                 \tag{1.1}
\]

Every (a\in A) has only its two neighbours in (A) and (v) outside
(C), while every (b\in B) has only its three neighbours in (B) and
(v) outside (C).  Hence

\[
 |N_C(a)|\geq4\quad(a\in A),\qquad
 |N_C(b)|\geq3\quad(b\in B).                         \tag{1.2}
\]

The following is the exact elementary construction sought in this cell.

### Lemma 1.1 (two-helper certificate)

Suppose (J_1,J_2\subseteq C\cup A) are disjoint connected sets such
that

* (J_1,J_2) each contain a vertex of (A); and
* every (b\in B) has a neighbour in each (J_i).

Then (G) has a (K_7)-minor.

#### Proof

The four singleton bags on (B), together with (J_1,J_2), form a
(K_6)-model.  The four singleton bags form a clique.  Each is adjacent
to each (J_i) by hypothesis.  Finally, the two helpers contain distinct
vertices of the clique (A), so they are adjacent to one another.  All
six bags meet (N), and hence the singleton bag \(\{v\}\) is adjacent to
all of them. \(\square\)

Thus it is not enough to find two unrooted helper bags adjacent to (B):
each helper must be rooted in (A), so that it is adjacent to (v).

### Lemma 1.2 (three-helper certificate)

Suppose (Y_1,Y_2,Y_3\subseteq C) are pairwise disjoint connected sets,
each adjacent to all three vertices of (A) and to at least three
vertices of (B).  Then (G) has a (K_7)-minor.

#### Proof

The three sets (L_i=N_B(Y_i)) have order at least three in the
four-set (B).  Hall's condition holds for (L_1,L_2,L_3), so choose
distinct (c_i\in L_i).  The bags (Y_i\cup\{c_i\}) are connected and
pairwise adjacent through the clique (B).  Together with the three
singleton bags on (A), they form an (N)-meeting (K_6)-model.  Add
\(\{v\}\). \(\square\)

This observation applies to disjoint sides even when they arise at
different cutvertices; it is not restricted to one block decomposition.

## 2. The cases \(\lvert C\rvert=4,5\) are impossible

Equation (1.2) first gives \(\lvert C\rvert\geq4\).

### Lemma 2.1

Under the standing hypotheses, \(\lvert C\rvert\neq4\).

#### Proof

If \(\lvert C\rvert=4\), every vertex of (A) is adjacent to every
vertex of (C).  Partition (C=R\dot\cup S) with
\(\lvert R\rvert=\lvert S\rvert=2\), and choose distinct
\(a_1,a_2\in A\).  Since every (b\in B) has at least three neighbours
in the four-set (C), it has a neighbour in each of (R,S).  The sets

\[
 J_1=R\cup\{a_1\},\qquad J_2=S\cup\{a_2\}
\]

are disjoint connected helpers satisfying Lemma 1.1. \(\square\)

### Lemma 2.2

Under the standing hypotheses, \(\lvert C\rvert\neq5\).

#### Proof

For (b\in B), call the two-set

\[
 P_b=C-N_C(b)
\]

*forbidden* when it has order two.  There are at most four forbidden
pairs.  Choose a two-set (R\subseteq C) which is not forbidden, and put
\(S=C-R\).  Then every (b\in B) has a neighbour in both (R) and (S).
Indeed, if (b) missed all of (R), then (1.2) would force
\(R=C-N_C(b)=P_b\); and (b) cannot miss the three-set (S), since it
has at least three neighbours in (C).

It remains to choose (R) and two roots so that the two helpers are
connected.  For (a\in A), put

\[
 M_a=C-N_C(a).
\]

By (1.2), \(\lvert M_a\rvert\leq1\).

If two vertices (a_1,a_2\in A) miss distinct vertices (p,q\in C),
consider the six pairs which contain exactly one of (p,q).  At most four
are forbidden.  After possibly interchanging (a_1,a_2), choose a
non-forbidden pair (R) with (q\in R), (p\notin R).  Then (a_1)
is complete to (R), while (a_2) is complete to (S).

If some (a_0\in A) is complete to (C), the same conclusion is even
easier.  If another vertex (a_1) misses (p), choose one of the six
pairs (R\subseteq C-\{p\}) which is not forbidden, use (a_1) on
(R), and use (a_0) on (S).  If two vertices of (A) are complete
to (C), any non-forbidden (R) works.

The only remaining case is

\[
 M_a=\{p\}\qquad\text{for all }a\in A                 \tag{2.1}
\]

for one common vertex (p\in C).  Choose a non-forbidden pair
\(R\subseteq C-\{p\}\); there are six candidate pairs and at most four
forbidden ones.  Put (S=C-R).  Every (a\in A) is complete to (R)
and to the two vertices of (S-\{p\}).  Moreover, (2.1) and
\(d_G(p)\geq7\) imply

\[
 d_C(p)+d_B(p)\geq7,
\]

so (d_C(p)\geq3).  Since (R) has only two vertices, (p) has a
neighbour in (S-\{p\}).  Consequently, for distinct
\(a_1,a_2\in A\), both

\[
 R\cup\{a_1\}\quad\text{and}\quad S\cup\{a_2\}
\]

are connected.  In every case these two sets are the helpers of
Lemma 1.1, a contradiction. \(\square\)

### Corollary 2.3

Every graph in the exceptional cell satisfies

\[
 |C|\geq6.                                             \tag{2.2}
\]

## 3. The three-side cutvertex cell closes

We use the already proved leaf-defect restrictions.  If (z) is a
cutvertex of (C) and (D) is a component of (C-z), then (D) is
adjacent to at least six vertices of (N).  There cannot be two such
sides both adjacent to all of (B), and two sides cannot have the same
unique defect in (B).  The preceding consolidation argument showed
that (C-z) has at most three components, and that if there are three,
then they have distinct one-vertex defects in (B).

The last three-side case also has a direct model.

### Lemma 3.1 (three distinct defects)

There is no cutvertex (z) for which (C-z) has three components.

#### Proof

Suppose the components are (D_1,D_2,D_3).  By the restrictions just
recalled, there are distinct (b_1,b_2,b_3\in B) such that (D_i) is
adjacent to every vertex of (N-\{b_i\}).  In particular, every (D_i)
is adjacent to all three vertices of (A).

Choose distinct (c_1,c_2,c_3\in B) with (c_i\neq b_i); for example,
cyclically permute (b_1,b_2,b_3).  The sets

\[
 X_i=D_i\cup\{c_i\}\qquad(i=1,2,3)
\]

are disjoint and connected.  They are pairwise adjacent through the
edges (c_ic_j) of the clique (B), and each is adjacent to each of the
three singleton bags on (A).  Thus

\[
 X_1,X_2,X_3,\{a_1\},\{a_2\},\{a_3\}
\]

is an (N)-meeting (K_6)-model in (G-v).  Add \(\{v\}\). \(\square\)

### Corollary 3.2 (two-side lock)

For every cutvertex (z) of (C), the graph (C-z) has exactly two
components.  At such a cutvertex, after interchanging the sides, the
only boundary patterns not already eliminated are:

1. one side is adjacent to all of (B), and the other has one defect
   in (B); or
2. both sides have one defect in (B), and the two defects are distinct.

In the second pattern both sides are adjacent to every vertex of (A).
The shared portal (z) is the exact obstruction to repairing both
distinct (B)-defects independently.

Here is one useful sufficient condition which makes the portal usable.

### Lemma 3.3 (an (A)-complete central portal closes)

Let (D_1,D_2) be the two components of (C-z).  Suppose each of
\(D_1,D_2,\{z\}\) is adjacent to every vertex of (A), and (z) has a
neighbour in (B).  Then (G) has a (K_7)-minor.

#### Proof

Each (D_i) misses at most one vertex of (B).  There are distinct
\(c_1,c_2,c_3\in B\) such that (c_i) is adjacent to (D_i) for
\(i=1,2\), and (zc_3\in E(G)).  To see this, first choose (c_3) from
\(N_B(z)\); each of the two remaining lists has order at least two in
\(B-\{c_3\}\), so they have distinct representatives.

Now use

\[
 D_1\cup\{c_1\},\quad D_2\cup\{c_2\},\quad
 \{z,c_3\},\quad \{a_1\},\{a_2\},\{a_3\}.
\]

The first three bags are connected and pairwise adjacent through the
clique (B); by hypothesis each is adjacent to all three singleton
bags on (A).  Add \(\{v\}\) to the resulting (N)-meeting
\(K_6\)-model. \(\square\)

Thus a remaining two-defect portal must either miss a vertex of (A) or
have no neighbour in (B).  In the good-side/defective-side pattern, a
good side may itself miss one vertex of (A), which is an additional
lock.

## 4. A connected-partition formulation using two-connectivity

Put

\[
 D=G-(B\cup\{v\})=G[C\cup A].
\]

### Lemma 4.1

The graph (D) is two-connected.

#### Proof

If (D) were disconnected, (B\cup\{v\}) would be a separator of
order five in (G).  If (x) were a cutvertex of (D), then
\(B\cup\{v,x\}) would be a separator of order six.  Both contradict
\(\kappa(G)\geq7\). \(\square\)

This gives a compact exact criterion.  Fix distinct (a_1,a_2\in A),
and take an (a_1a_2)-numbering

\[
 x_1=a_1,x_2,\ldots,x_m=a_2
\]

of the two-connected graph (D): every internal vertex has an earlier
and a later neighbour.  Every prefix and every suffix of this ordering
is connected.  For (b\in B), define

\[
 \ell_b=\min\{i:x_i\in N_D(b)\},\qquad
 r_b=\max\{i:x_i\in N_D(b)\}.
\]

### Lemma 4.2 (overlapping-neighbourhood criterion)

If

\[
 \max_{b\in B}\ell_b < \min_{b\in B} r_b,             \tag{4.1}
\]

then (G) has a (K_7)-minor.

#### Proof

Choose an integer (k) with

\[
 \max_b\ell_b\leq k<\min_b r_b.
\]

The prefix \(J_1=\{x_1,\ldots,x_k\}\) and suffix
\(J_2=\{x_{k+1},\ldots,x_m\}\) are disjoint and connected.  They
contain (a_1,a_2), respectively, and each contains a neighbour of every
vertex of (B).  Apply Lemma 1.1. \(\square\)

Consequently, in a counterexample, for **every** choice of two roots in
(A) and every corresponding numbering, the four intervals

\[
 [\ell_b,r_b)\qquad(b\in B)
\]

have empty common intersection.  Since intervals have the Helly
property, for each such numbering there is a pair of vertices
(b,c\in B), possibly depending on the numbering, for which
(r_b\leq\ell_c) or (r_c\leq\ell_b).  This is a sharper residual than
an unstructured request for two helper bags.

## 5. What the rooted \(K^*_{4,2}\) density theorem does and does not give

Let (H=G-v), (n=|C|),

\[
 p=e_G(C,N),\qquad q=e(G[C]).
\]

Then

\[
 p\geq24,\qquad p+2q\geq7n,                         \tag{5.1}
\]

and hence

\[
 p+q\geq\left\lceil\frac{7n+24}{2}\right\rceil.     \tag{5.2}
\]

The graph (H) is six-connected, so ((H,B)) is internally
four-connected.  The J\o rgensen--Norin--Totschnig rooted-minor bound says
that if (H) has no (B)-rooted (K^*_{4,2})-model, then

\[
 e(H)\leq4|H|-10.
\]

Since (e(H)=9+p+q) and \(|H|=n+7\), a rooted
\(K^*_{4,2}\)-model exists whenever

\[
 p+q\geq4n+10.                                      \tag{5.3}
\]

Such a model has four bags rooted at (B) and two mutually adjacent
helper bags, each adjacent to all four root bags.  The root bags are also
pairwise adjacent, using the edges of (G[B]), so this is a (K_6)-model
in (H).  It extends with (v) only if **both** unrooted helper bags meet
(A).  The theorem does not prescribe this, and treating its helpers as
though they were (A)-rooted is invalid.

For (n=6), (5.1)--(5.3) give a useful exact split:

* if (p+q\geq34), the rooted theorem supplies the (B)-rooted
  (K^*_{4,2})-model, but the (A)-rooting of its helpers remains to be
  proved;
* if (p+q\leq33), then necessarily

  \[
  p=24,\qquad q=9.                                   \tag{5.4}
  \]

  Equality holds in all degree sums: each (a\in A) has exactly four
  neighbours in (C), each (b\in B) has exactly three, and every
  vertex of (C) has degree exactly seven in (G).

The full six-vertex helper certificate in
`hadwiger_k34_c6_human.md`, Theorem 5.1, eliminates both branches.  It
is a finite **computer-assisted** proof: `k34_c6_full_search.py`
constructs all 112 unlabelled connected graphs on six vertices, checks
all 2024 multisets of three (A)-neighbourhoods of order at least four
for each graph, and uses the exact balanced-partition obstruction to
maximize the possible (B)-degree.  Of the 226,688 resulting
((C,A))-states, 63 have at most four compatible balanced partitions,
and none has a degree-feasible (B)-obstruction.  It follows that every
six-vertex (C) has the two rooted helpers of Lemma 1.1, and hence

\[
 |C|\geq7.                                             \tag{5.5}
\]

This strengthening from (2.2) to (5.5) depends on the reproducible
finite certificate; it is not asserted as a conceptual hand proof.

### The exact seven-vertex split

Suppose now that (n=|C|=7).  The rooted density threshold (5.3) is
(p+q\geq38).  If it fails, then (p+q\leq37); combining this with

\[
 p\geq24,\qquad p+2q\geq49
\]

leaves exactly

\[
 (p,q)=(24,13)\quad\hbox{or}\quad(25,12).           \tag{5.6}
\]

Indeed the inequalities force (p\leq25); for (p=24) they give
(13\leq q\leq13), and for (p=25) they give
(12\leq q\leq12).

These two cells have additional exact degree information.  In the
((25,12))-cell every vertex of (C) has degree seven in (G).  In the
((24,13))-cell six vertices of (C) have degree seven and one has degree
eight.  Consequently Dirac's contraction-critical neighbourhood bound
gives

\[
 \alpha(G[N_G(x)])\leq2                               \tag{5.7}
\]

at every degree-seven vertex (x\in C).  Seven-connectivity supplies a
second compact family of constraints: for every nonempty (X\subseteq C),
the external neighbourhood of (X) separates it from (v), and hence

\[
 |N_C(X)-X|+|N_N(X)|\geq7.                            \tag{5.8}
\]

In particular (|N_N(X)|\geq|X|), so the incidence graph between (C)
and (N) has a matching saturating (C).

The density split is superseded by the following stronger finite result.

### The full seven-vertex helper certificate

For each of the 853 connected unlabelled graphs (C) on seven vertices,
the fixed-(C) solver leaves all (A)- and (B)-incidences free and imposes
only:

1. the row bounds in (1.2);
2. all 127 necessary seven-connectivity inequalities (5.8); and
3. the negation of every pair of disjoint helpers, allowing either helper
   to use an arbitrary nonempty subset of (A).

The sparse incidence totals (5.6), the rooted density theorem, and the
Dirac constraints (5.7) are not imposed.  The helper predicate is exact:
for nonempty (P\subseteq C) and (R\subseteq A), the set (P\cup R) is
connected precisely when every component of (C[P]) has a neighbour in
(R), because (A) is a clique.  It is (B)-complete precisely when (P)
meets all four (B)-neighbourhoods.

The 853 instances were run in six shards and independently rerun with
machine-readable records.  Every instance returned UNSAT, with no SAT or
UNKNOWN result.  The merged records contain each atlas index
(0,\ldots,852) exactly once, match every graph6 identifier, and have
graph-ID/status digest

    fe854344e1c75336fa01d6bab426e1456e28a2f59ad46c9315dc82c11e72a946

The frozen solver and shard-runner hashes, per-shard records, and the full
encoding audit are recorded in hadwiger_k34_c7_kappa_audit.md; the merged
machine certificate is k34_c7_kappaonly_merged.json.

Therefore every seven-vertex exterior component satisfying the
counterexample-derived conditions has the two helpers of Lemma 1.1 and
would give a (K_7)-minor.  Together with (5.5), this proves the new
computer-assisted order bound

\[
 |C|\geq8.                                             \tag{5.9}
\]

## 6. Exact remaining gap in this cell

The exceptional neighbourhood is now constrained as follows (with the
order bound computer-assisted):

\[
 G[N]=K_3\dot\cup K_4,\qquad |C|\geq8,\qquad
 G[C\cup A]\text{ is two-connected},                \tag{6.1}
\]

and every cutvertex of (C) has precisely the two-side patterns in
Corollary 3.2.  Either of the following strictly local statements would
eliminate the whole remaining cell:

1. (G[C\cup A]) has two disjoint connected sets, each meeting (A)
   and each meeting all four neighbourhoods (N_C(b)), (b\in B);
2. some (A)-to-(A) numbering satisfies (4.1).

In the density branch (p+q\geq4|C|+10), there is a third sufficient
target: in a (B)-rooted (K^*_{4,2})-model supplied by (5.3), make both
helper bags meet distinct vertices of (A).  This third target does not
cover the sparser branch; the established inequalities (5.1) do not
imply the threshold once (|C|\geq8).

The remaining issue is exactly the simultaneous (A)-rooting of two
(B)-complete helpers.  An unrooted (K_6)-model, or two repairs which
both use the same cutvertex portal, does not suffice.

### Source for the rooted density statement

S. Norin and A. Totschnig, *Every graph with no
\(K_7^{\vee}\)-minor is 6-colorable* (2025), Lemma 2.5 on
rooted (K^*_{4,2})-models, extending J\o rgensen's rooted
(K_{4,2}) bound: <https://arxiv.org/abs/2507.03244>.
