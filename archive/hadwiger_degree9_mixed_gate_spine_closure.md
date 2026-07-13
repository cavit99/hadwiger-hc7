# The mixed degree-nine gate closes by a protected-target exchange

## 1. Setting

Use the globally lexicographically minimal balanced spanning rooted model

\[
                         L_6,L_0,R_5,R_0
\]

from `hadwiger_degree9_complementary_lobe_ownership.md`.  Thus the
potential is

\[
              (|L_0|+|R_0|,\ |R_0|,\ |R_5|),                 \tag{1.1}
\]

chosen over all balanced spanning models with the four prescribed roots
and with (6\in L_6), (5\in R_5).

Let (K) be the component of (L_6-6) containing the prescribed
left root and put (D=L_6-K).  Assume the left gate is in the
complementary cell

\[
 K\not\sim L_0,\qquad |N_{R_0}(K)|\leq1,\qquad
 |N_{R_5}(K)|\geq2.                                      \tag{1.2}
\]

Let (J) be the component of (R_5-5) containing the prescribed
right root (r_5).  This note closes the mixed alternative

\[
                  J\sim R_0,\qquad J\not\sim L_6,L_0.       \tag{1.3}
\]

The ordered-spine theorem gives much more information (including at
least four (J)-portals in strict surplus), but the closure below only
needs the first contact in (1.3).  It therefore applies to bags of
arbitrary order and to arbitrary portal placement.

Put

\[
 C=R_5-J,\qquad A=N_C(K),\qquad B=N_C(L_0).                 \tag{1.4}
\]

The set (C) is connected and contains (5): the components of
(R_5-5) other than (J) all attach to (5).  Moreover

\[
                         |A|\geq2,\qquad B\ne\varnothing.    \tag{1.5}
\]

Indeed, (J\not\sim L_6,L_0), so every (K)-portal and every old
(R_5L_0)-contact lies in (C).

The universal portal bound gives three portals in (R_5\cup R_0),
and Theorem 5.1 leaves at most one in (R_0), proving the displayed
bound even at exact equality.  In strict surplus it improves to three.

## 2. The split certificate

### Lemma 2.1 (a 5-preserving mixed split closes)

Suppose

\[
                         R_5=X\mathbin{\dot\cup}Y            \tag{2.1}
\]

is a connected adjacent bipartition satisfying

\[
 X\sim K,\qquad Y\sim K,\qquad X\sim L_0,\qquad 5\in Y.    \tag{2.2}
\]

Then (G) contains a (K_7)-minor.

#### Proof

If (r_5\in Y), this is Theorem 7.2 of
`hadwiger_degree9_complementary_lobe_ownership.md`: both protected
vertices (r_5,5) lie in (Y), both sides meet (K), and the
detachable side (X) meets (L_0).

It remains that (r_5\in X).  Use the seven branch sets

\[
 \{h\},\quad \{1\},\quad \{2\},\quad L_0,\quad K\cup X,
 \quad \{v,3\}\cup R_0,\quad \{4\}\cup D\cup Y.           \tag{2.3}
\]

They are disjoint.  The last three nontrivial connectivity checks use,
respectively, the (KX)-contact, the path (v-3-r_0), and the
path (4-5-6), where (r_0) is the prescribed root of (R_0),
(5\in Y), and (6\in D).

For completeness, among the four nonsingleton sets in (2.3), the six
adjacencies are witnessed by

\[
 XL_0,\quad L_0R_0,\quad DL_0,\quad r_5 3,\quad KD,\quad34. \tag{2.4}
\]

Here (D\sim L_0) because the old (L_6L_0)-adjacency cannot have
its (L_6)-endpoint in (K), by (1.2).  The four nonsingleton sets
see (h,1,2), respectively, through the left root of (L_0), the
left root in (K), the vertex (v), and the pair (4,6).  Finally
(h12) is a triangle.  Hence (2.3) is a (K_7)-model. \(\square\)

## 3. The protected-target exchange

We use the flexible-start lemma already proved as Lemma 4.4 of
`hadwiger_degree9_protected_portal_peel.md`.

> If (T) is connected, (|A|\geq2), and (B_0,B_1) are
> nonempty, then either two vertex-disjoint paths start at distinct
> members of (A), one ending in (B_0) and one in (B_1), or one
> vertex meets every (A)-to-((B_0\cup B_1)) path.

In the linkage outcome the two paths extend to a connected bipartition
with one path on each side.

### Theorem 3.1 (mixed complementary/same-bag gate closure)

Under (1.1)--(1.4), assuming only (|A|\geq2) and
(B\ne\varnothing), (G) contains a (K_7)-minor.

#### Proof

Apply the flexible-start lemma inside the connected graph (C), with
source set (A) and target classes

\[
                              B,\qquad \{5\}.                \tag{3.1}
\]

Suppose first that it gives disjoint paths.  Extend them to a connected
bipartition

\[
                              C=X\mathbin{\dot\cup}Y,         \tag{3.2}
\]

where (X) contains the (A)-to-(B) path and (Y) contains the
other (A)-to-(5) path.  In particular

\[
 X\sim K,L_0,\qquad Y\sim K,\qquad5\in Y.                   \tag{3.3}
\]

Add all of (J) to (Y).  The enlarged (Y) is connected because
(J) is a component of (R_5-5) and hence has an edge to (5).
Now (3.2) is a connected adjacent bipartition of (R_5), and Lemma
2.1 gives a (K_7)-minor.

It remains that there is one vertex (q\in C) meeting every path from
(A) to (B\cup\{5\}).  Since (|A|\geq2), choose a component
(U) of (C-q) meeting (A-\{q\}).  The bottleneck property gives

\[
                         U\cap B=\varnothing,\qquad5\notin U. \tag{3.4}
\]

Move (U) from (R_5) into (L_6):

\[
             L_6'=L_6\cup U,\qquad R_5'=R_5-U,              \tag{3.5}
\]

leaving (L_0,R_0) unchanged.  This is a valid rooted spanning
(K_4)-model, as the following audit shows.

* (L_6'\) is connected because (U) contains an (A)-vertex and
  hence meets (K\subseteq L_6).
* (R_5'\) is connected.  The graph (C-U) consists of (q) and
  all other components of (C-q), hence is connected; it contains
  (5), through which it is joined to (J).
* The two changed bags are adjacent because every component (U) of
  the connected graph (C-q) has an edge to (q\in R_5').
* The residue (R_5') retains its (L_0)-contact through the
  nonempty set (B), by (3.4), and retains its (R_0)-contact
  through (J\sim R_0).
* Enlarging (L_6) destroys no old adjacency.  No prescribed root is
  moved, (6\in L_6'), and (r_5,5\in R_5').

Thus (3.5) remains in the globally optimized family.  It preserves the
first two coordinates of (1.1) and strictly decreases the third one,
because (U\ne\varnothing):

\[
                |R_5'|=|R_5|-|U|<|R_5|.                    \tag{3.6}
\]

This contradicts the global lexicographic choice.  The bottleneck
outcome is therefore impossible, so the linkage outcome and hence the
(K_7)-minor are forced. \(\square\)

### Corollary 3.2 (no complementary gate survives)

In a globally potential-minimal balanced model, neither opposite gate
can be complementary in a (K_7)-minor-free graph, including at exact
portal equality.

#### Proof

Suppose the left gate is complementary.  The right gate is either
same-bag or complementary.  The same-bag alternative is Theorem 3.1
above.  The double-complementary alternative is Theorem 3.1 of
`hadwiger_degree9_opposite_gate_closure.md`, whose direct crossed model
also includes exact equality.  Both give (K_7), a contradiction.  The
left--right image excludes a complementary right gate. \(\square\)

Thus the sole surviving degree-nine attachment cell has both gates in
their same-bag states:

\[
             K\sim L_0,\qquad J\sim R_0.                    \tag{3.7}
\]


## 4. Significance and exact residue

This is an infinite-family closure, not a quotient enumeration.  The
ordered (R_0)-spine, the number and order of its (J)-portals, and
the internal block structure of (R_5) are immaterial.  The mechanism
is instead:

\[
 \text{two protected target paths}\Longrightarrow K_7,
 \qquad
 \text{one bottleneck}\Longrightarrow
 \text{a potential-decreasing rooted-model exchange}.      \tag{4.1}
\]

Together with the independently audited opposite-complementary closure,
this eliminates the entire complementary-gate family, at arbitrary bag
order and at both equality and strict surplus.  The exact remaining
degree-nine target is the bilateral same-bag cell.  In that cell both
root components have ordered portal spines in the ordinary bags; the
next operation must exchange the two prescribed ordinary roots or use
minor-critical boundary transitions.
