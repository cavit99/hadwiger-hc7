# The double-overlap split in the unique-interface `C6` cell

## 1. The two quotient types

Put

\[
 S=\{z,c_1,\ldots,c_6\},\qquad G[S]=K_1\vee C_6,
\]

where the subscripts on the cycle are read modulo six.  Let `A,B` be
vertices complete to `S`, and let `P,Q` be adjacent vertices whose
contact rows cover `S`.  We use two helper geometries.

* In type **O** (the opposite shore was split), `AB` and `PQ` are
  edges and there are no other helper--helper edges.
* In type **A** (one unique-interface arm was split), `BP` and `PQ`
  are edges and there are no other helper--helper edges.  The label `P`
  is the split piece containing the old interface endpoint.  In
  particular, this convention does not silently forget which piece
  retains that endpoint.

Suppose two distinct cycle vertices `a,b` occur in both the `P`-row and
the `Q`-row.  The purpose of this note is to determine exactly what the
quotient calculation says.

## 2. A hand-checkable four-bag certificate

The following small lemma is the positive mechanism.  It is useful
independently of the two full helpers.

### Lemma 2.1 (anchored four-bag certificate)

Delete `z` and consider the graph consisting of the cycle and the edge
`PQ`, with the prescribed cycle contacts.  If one of the rows in the
following table occurs, up to a dihedral symmetry of the cycle and an
interchange of `P,Q`, the four displayed sets form a `K_4` model.  Here
`iP` denotes the two-vertex bag `\{c_i,P\}`, and similarly for `Q`.

| `N_C(P)` | `N_C(Q)` | four bags |
|---|---|---|
| 123 | 12456 | `1,2,3P,4Q` |
| 1234 | 1256 | `1,2,3P,5Q` |
| 1234 | 1356 | `1,2,4P,3Q` |
| 1234 | 2356 | `1,2,3P,6Q` |
| 12345 | 136 | `1,2,4P,3Q` |
| 12345 | 146 | `1,6,5P,4Q` |
| 12345 | 236 | `1,2,3P,6Q` |
| 12345 | 246 | `1,2,3P,6Q` |
| 123456 | 13 | `1,2,4P,3Q` |
| 1235 | 1246 | `1,2,3P,4Q` |
| 1235 | 1346 | `1,2,5P,3Q` |
| 1235 | 2456 | `1,2,3P,6Q` |
| 1245 | 1346 | `1,2,4P,3Q` |

Every bag contains exactly one cycle vertex, and two cycle vertices are
unused.  The verification is direct: consecutive singleton bags use a
cycle edge, the missing singleton-to-opposite-bag adjacencies are the
displayed portal contacts, and the two composite bags are adjacent
through `PQ` (or a cycle edge).  Thus the table is a branch-set
certificate rather than a mere numerical minor test.

### Lemma 2.2 (six-cycle word lemma)

Let the contact rows cover the cycle, and suppose their intersection
contains distinct vertices `a,b`.  Choose an allocation of all other
overlap vertices to one row, so that the allocated rows meet exactly in
`a,b`.  Then one of the following holds.

1. The allocated rows occur in Lemma 2.1.
2. The roots are antipodal and, after interchanging the rows,

   \[
   N_C(P)=\{a,b\},\qquad N_C(Q)=V(C_6).
   \tag{2.1}
   \]
3. The allocated rows are the two complementary closed `a-b` arcs of
   the cycle.

#### Proof

Rotate and reflect so the cyclic distance from `a` to `b` is
`d in {1,2,3}`.  Order the nonroots by first listing the open arc from
`a` to `b` and then the open arc from `b` to `a`, and record by a
four-bit word which row owns them.  The two arc words are, respectively,

\[
\begin{array}{c|c}
d&\text{arc words}\ \hline
1&0000,1111,\\
2&1000,0111,\\
3&1100,0011.
\end{array}
\tag{2.2}
\]

For `d=3`, the two additional constant words are exactly (2.1).
Putting each remaining word into its dihedral/complement orbit gives
the thirteen rows of Lemma 2.1.  This is a check of three lists of
sixteen four-bit words; the displayed table supplies an actual model
for every retained orbit. \(\square\)

## 3. Exact quotient dichotomy

### Theorem 3.1 (cyclic-arc lock)

In either quotient type O or A, if the `P,Q` rows cover `S` and contain
two common cycle roots, then either the quotient contains a `K_7`
minor, or

\[
 N_C(P),N_C(Q)
\tag{3.1}
\]

are exactly the two complementary closed arcs between some two common
roots.  There are no additional cycle contacts across the two arcs.
The vertex `z` may contact `P`, `Q`, or both.

#### Proof

Allocate every contact other than the two chosen common roots to one of
the rows.  If Lemma 2.1 applies, its four bags lift as follows.

* In type O, add the three bags `\{z\},\{A\},\{B\}`.  The last two are
  adjacent, and all three see each of the four anchored bags.
* In type A, let `c_r,c_s` be the two unused cycle vertices in
  Lemma 2.1 and add

  \[
  \{z\},\qquad \{A,c_r\},\qquad \{B,c_s\}.
  \tag{3.2}
  \]

  These bags are connected and pairwise adjacent; each sees all four
  anchored bags through the complete boundary contacts of `A,B`.

Both constructions are explicit `K_7` models and do not use a
`zP` or `zQ` edge.

It remains to treat (2.1).  Write `a=c_1,b=c_4`.  If `P` is the small
row and `Q` is the full row, the following seven bags work in both
types:

\[
 \{z\},\ \{c_4,c_5\},\ \{c_6\},\ \{A,c_2\},\
 \{B\},\ \{P,c_1\},\ \{Q,c_3\}.
\tag{3.3}
\]

For type A, the adjacency between `\{B\}` and `\{P,c_1\}` is the
retained old-interface edge `BP`; thus (3.3) explicitly audits the
identity of the interface-containing split piece.  If `Q` is small,
replace the last two bags in (3.3) by

\[
 \{P,c_3\},\qquad \{Q,c_1\}.
\tag{3.4}
\]

The other adjacencies follow from the cycle, the full contacts of
`A,B`, and `PQ`.

Consequently every allocated nonarc pattern is positive.  If an actual
row pair had an additional overlap at a nonroot cycle vertex, assigning
that overlap in the two different ways would give a nonarc allocation.
Hence a negative actual pair has no such overlap, and (3.1) consists
exactly of complementary closed arcs. \(\square\)

The converse (the arc rows really are quotient-negative) is checked by
the exact contraction verifier
`unique_interface_c6_surplus_split_fast_probe.py`.  On eleven vertices,
a `K_7` model uses at most four contractions.  The verifier enumerates
all adjacent-bag merges through depth four and at every state searches
for a seven-clique; unused vertices need not be deleted.  It reports

\[
 1344=2\cdot21\cdot32,\qquad
 1104\text{ positive},\qquad 240\text{ negative}.
\]

Restricting the repeated pair to two cycle roots gives 480 quotients of
each type.  In each type 420 are positive and 60 are negative.  The
negative counts by cyclic distance `1,2,3` are `24,24,12`, exactly the
arc words (2.2), with either placement of `z`.  The separate verifier
`unique_interface_c6_arc_rows_probe.py` also adds `z` to both rows and
confirms that all maximal arc-row quotients remain negative.

## 4. Portal placement and the exact-cut exit

Return to the actual graph.  Let `R=P dotcup Q` be the connected split,
and write

\[
 T_P=N_Q(P),\qquad T_Q=N_P(Q).
\tag{4.1}
\]

These are sets of actual interface vertices, not a count of parallel
edges in the contracted quotient.

### Proposition 4.1 (arc lock or nested seven-cut)

Assume the quotient is negative, so Theorem 3.1 gives complementary
closed arc rows.

1. In type O,

   \[
   N_G(P)=N_S(P)\mathbin{\dot\cup}T_P,
   \qquad
   N_G(Q)=N_S(Q)\mathbin{\dot\cup}T_Q.
   \tag{4.2}
   \]

   Hence `|N_S(P)|+|T_P|>=7`, and similarly for `Q`.  Equality exposes
   the nested exact seven-cut `N_S(P) union T_P` (or its `Q` analogue).
   If no exact cut occurs, the corresponding sum is at least eight.

2. In type A, label the pieces so that `P` contains the original
   interface endpoint `x`, whose unique neighbour in the other old arm
   is `y`.  Then

   \[
   \begin{aligned}
   N_G(P)&=N_S(P)\mathbin{\dot\cup}T_P\mathbin{\dot\cup}\{y\},\\
   N_G(Q)&=N_S(Q)\mathbin{\dot\cup}T_Q.
   \end{aligned}
   \tag{4.3}
   \]

   Equality at seven exposes respectively

   \[
   N_S(P)\cup T_P\cup\{y\},\qquad
   N_S(Q)\cup T_Q
   \tag{4.4}
   \]

   as a nested exact seven-cut.  With no such cut, both neighbourhoods
   have order at least eight.

#### Proof

The neighbourhood identities use anticompleteness of the two original
shores and, in type A, the fact that `xy` was the unique old-arm
interface edge.  Each displayed neighbourhood separates its nonempty
piece from the opposite full shore.  Seven-connectivity gives order at
least seven.  Equality is exactly a seven-vertex separator, nested
strictly inside the original shore. \(\square\)

If a closed arc contains `ell` cycle vertices and its row contains
`epsilon in {0,1}` copies of `z`, Proposition 4.1 gives the numerical
surplus bounds

\[
\begin{array}{c|c}
\text{piece type}&\text{no-exact-cut lower bound on }|T|\\ \hline
\text{type O}&8-(\ell+\epsilon),\\
\text{type A, contains }x&7-(\ell+\epsilon),\\
\text{type A, avoids }x&8-(\ell+\epsilon).
\end{array}
\tag{4.5}
\]

Thus the residual is no longer an arbitrary covering split.  It is a
**cyclic portal-order lock**: the boundary contacts occur in two closed
arcs, while either a nested minimum cut is exposed or the internal
`P-Q` interface has the explicit surplus (4.5).  For a six-minor-critical
ambient graph, every label-preserving deletion or contraction within
one side is additionally subject to the exact one-step boundary-state
transition theorem.  Converting that transition plus the surplus
interface into a cross-arc contact is the precise remaining local step;
the static quotient alone cannot do it, as the arc-row negatives show.
