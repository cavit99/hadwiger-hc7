# Audit of the weighted KLNZ terminal decoder

**Verdict:** **GREEN.**  Theorem 2.1 and Corollary 5.1 are correct as
conditional terminal-cell results.  The proved lemmas in the decorated
three-model note are also correct.  The audit corrections concerning KLNZ
provenance, the rooted shore, and the status of the live decoder have been
incorporated in the source notes.

## 1. Matrix and weights

Equations (1.1)--(1.2) make every row and column of the incidence matrix a
permutation of `(1,2,2)`.  For `a_ij=2`,

\[
 |(X_j\mathbin\triangle L_i)\cap\{z_1,z_2,z_3\}|
 =\mathbf 1_{z_i\notin X_j}
  +|(X_j\cap\{z_1,z_2,z_3\})-\{z_i\}|.
\]

The cases with zero or two distinguished vertices in a column give a
weight-seven cut.  A column with three forces another with zero.  If all
columns contain one distinguished vertex, placing it in a size-two cell
would give a forbidden weight-six separator.  Hence the size-one entries
are the diagonal distinguished vertices, and every off-diagonal standard
cut contains two distinguished vertices and has weight eight.  This proves
Theorem 2.1 exactly under assumption (1.3).

## 2. Exact KLNZ dependency

KLNZ 3.2.16 does **not** state unconditionally that
`X_j triangle L_i` is a cut.  In its notation the cut is

\[
       (X_j\mathbin\triangle L_i)\cup W\cup Z,
\]

and it separates `X_j cap L_i` from the other named cliques outside `W`.
Thus the bare cut in (1.3) follows in the terminal equality cell only after
stating `W=Z=emptyset`.  The source now states this explicitly and separately
retains the side conclusion needed in Section 3.

KLNZ 3.2.16 also does not imply that the whole distinguished open shore has
two vertices.  Its component may contain arbitrary vertices outside the
three named cliques.  What is proved is:

* the distinguished component contains the adjacent pair
  `L_i cap X_j`;
* no other named-terminal vertex lies in that open shore;
* `L_i-(L_i cap X_j)` is in the boundary; and
* the other two named cliques lie in the opposite closed shore.

Accordingly, the source now says **a shore rooted by a literal two-vertex
clique, whose intersection with the named terminal union off the boundary is
exactly that clique**.  Preservation of all three named models is valid, with
`L_i` retained on the distinguished closed shore and the other two cliques
retained on the opposite one.

## 3. Decorated three-model note

The following checks are green.

1. Expanding a quotient separator replaces each contained `z_i` by the two
   endpoints of its split edge, so its literal order is exactly its declared
   weight.
2. Seven disjoint good paths give seven disjoint connected bags.  Any two
   label pairs among three labels intersect, and their distinct endpoints in
   the common literal clique are adjacent.
3. The KLNZ/Mader obstruction uses the floor budget.  Moving a vertex of a
   positive even `X_j` to `W` preserves the certificate and its budget;
   after parity is established, moving a vertex of an odd `X_j` raises a
   strict budget by one.  A nonempty `X_j` exists because fifteen terminal
   vertices cannot all lie in `W`, whose order is at most six.
4. The terminal-coverage calculation gives
   `15 <= 12-|W|+o`, hence `o >= |W|+3`.
5. For a genuine cell with a vertex outside `W union Y_j`, the set
   `W union X_j` is a separator.  No named-clique vertex lies in its lobe,
   so all three models are retained in the opposite closed shore after
   literal expansion.

The source now correctly describes the boxed statement (4.1) as a
**sufficient stronger remaining statement**, not an equivalent
reformulation of every possible handoff.  Its direct-`K_7` contrapositive is
correctly restricted to maximal certificates.

## 4. Corollary 5.1 and the minimal-triple property

Corollary 5.1 is green.  In Theorem 2.1(1), a standard separator has ordinary
order six and weight seven, so it contains exactly one marked vertex.  In
Theorem 2.1(2), every standard separator has ordinary order six and contains
exactly two marked vertices.  Therefore either outcome contradicts the
additional hypothesis that every separator of order at most six contains all
three marked vertices.

The minimal-contraction justification is also correct.  Let all three split
edges be inclusion-minimal with a non-seven-connected quotient.  If a
separator of order at most six omits `z_i`, splitting `z_i` back preserves
that separator in the seven-connected proper predecessor.  Hence every
six-separator contains all three marks.  If a separator had order at most
five, it contains every mark; splitting any one mark back increases its
order by one, again producing a separator of order at most six in a proper
predecessor.  Thus the quotient is six-connected.  This second argument is
now written explicitly in the decorated note.

## 5. Promotion boundary

The conditional terminal decoder, Corollary 5.1, and Lemmas 2.1, 3.1 and 3.2
are green.  Corollary 5.1 excludes the canonical weight-eight terminal
pattern under the minimal-triple separator property.  Reaching the terminal
cell, proving the marked three-clique theorem, obtaining a small-weight
genuine cell in general, and proving the global support-six theorem remain
unproved.
