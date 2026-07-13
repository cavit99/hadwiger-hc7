# A portal-SDR lemma for six-root `K_{3,3}` Kempe systems

## 1. Normalized setting

Let

\[
L=\{1,2,3\},\qquad R=\{\bar1,\bar2,\bar3\}.
\]

Let a graph `X` be properly colored by the six independent color classes
`A_i` (`i in L`) and `B_j` (`j in R`), with prescribed roots

\[
x_i\in A_i,\qquad y_j\in B_j.
\]

Assume the usual minimal-witness normalization for a `K_{3,3}` routing
system:

1. for each `i,j`, `X[A_i union B_j]` has exactly one nontrivial
   component, and this component is an `x_i`--`y_j` path `P_{ij}`;
2. every other vertex in that two-color graph is isolated;
3. every edge of `X` lies on at least one of the nine paths `P_{ij}`; and
4. every non-root vertex of `X` has degree at least four.

These are precisely the reductions obtained by choosing a counterexample to
property (*) with minimum `|V(X)|+|E(X)|` and suppressing a degree-two
non-root in the standard Kriesell--Mohr way.  The lemma below only uses the
four displayed hypotheses, so it is independent of that provenance.

For each `i,j`, let `p_{ij}` be the neighbor of `x_i` on `P_{ij}`.  Thus
`p_{ij}` lies in `B_j`.  Define its column support

\[
S_{ij}:=\{h\in L:p_{ij}\in V(P_{hj})\}
\]

and define the common portal support in column `j` by

\[
I_j:=S_{1j}\cap S_{2j}\cap S_{3j}.
\]

## 2. Portal-SDR theorem

**Theorem (portal SDR).**  If the family `(I_j:j in R)` has a system of
distinct representatives, then `X` contains a `K_{3,3}`-certificate rooted
at the six prescribed roots.

### Proof

Choose distinct indices `sigma(j) in I_j`.  For `i in L`, set

\[
C_i:=\{x_i\},
\]

and for `j in R`, set

\[
D_j:=V(P_{\sigma(j),j})\setminus\{x_{\sigma(j)}\}.
\]

Each `D_j` is connected and contains `y_j`.  If `j` and `j'` are distinct,
then the two color pairs

\[
\{A_{\sigma(j)},B_j\},\qquad
\{A_{\sigma(j')},B_{j'}\}
\]

are disjoint, because both `j != j'` and `sigma(j) != sigma(j')`.
Consequently `D_j` and `D_{j'}` are disjoint.  They are also disjoint from
all singleton bags `C_i`.

For every `i,j`, the vertex `p_{ij}` is adjacent to `x_i`.  Since
`sigma(j) in I_j subseteq S_{ij}`, the vertex `p_{ij}` lies on
`P_{sigma(j),j}`, and it is not the deleted vertex
`x_{sigma(j)}` because it belongs to `B_j`.  Hence `p_{ij} in D_j`, so
`C_i` is adjacent to `D_j`.  Thus

\[
(C_1,C_2,C_3,D_{\bar1},D_{\bar2},D_{\bar3})
\]

is the required rooted `K_{3,3}`-certificate.  QED.

## 3. Exact form of a column with no common portal

**Lemma (cyclic portal lock).**  For every `i,j`, either `p_{ij}=y_j`, in
which case `S_{ij}=L`, or `|S_{ij}|>=2`.  Consequently, if `I_j` is empty,
then all three supports `S_{1j},S_{2j},S_{3j}` have order exactly two and
their three omitted indices form a fixed-point-free permutation of `L`.
Equivalently, up to reversing the 3-cycle,

\[
S_{1j}=\{1,2\},\qquad
S_{2j}=\{2,3\},\qquad
S_{3j}=\{1,3\}.
\]

### Proof

The root `y_j` lies on every `P_{hj}`, giving the first assertion when
`p_{ij}=y_j`.  Otherwise `p_{ij}` is a non-root vertex.  It lies on
`P_{ij}`.  In the normalized graph, its contribution to each path containing
it consists of two incident edges, and paths with different `A`-colors use
neighbors in different color classes.  The degree lower bound four therefore
forces `p_{ij}` to lie on at least one further `P_{hj}`.  Hence
`|S_{ij}|>=2`.

If one support had order three while the intersection were empty, the other
two supports, each of order at least two in a three-element ground set, would
still have nonempty intersection, a contradiction.  Thus all three supports
have order two.  Each contains its row index `i`, so its omitted index is not
`i`.  Empty total intersection says that every index is omitted at least
once.  There are exactly three omissions, hence every index is omitted once;
the omission map is a derangement of a three-element set and therefore a
3-cycle.  QED.

## 4. What remains for `K_{3,3}`

The theorem reduces a normalized counterexample to two finite *types* of
portal obstruction, without bounding the sizes of the color classes:

1. at least one column has the cyclic portal lock above; or
2. all `I_j` are nonempty, but Hall's condition fails for the three sets
   `I_j`.

The same dichotomy holds after interchanging rows and columns.  A proof that
the row and column locks cannot coexist, or a branch-set exchange resolving
one of them, would prove that `K_{3,3}` has property (*).

This is a genuine uniform reduction: it covers color classes of arbitrary
order and replaces arbitrary path geometry at the roots by a three-state
portal obstruction.  It is not by itself a proof of property (*).

## 5. Exact falsification checks

`trianglefree_six_property_search.py` exhaustively checks minimal alternating
path unions and every rooted branch-set assignment.  No `K_{3,3}` failure was
found for:

- six classes of order two (512 path systems);
- class sizes `3,2,2,2,2,2` (1,728 systems);
- all three distribution types of total order 14 (4,096, 5,832, and 11,664
  systems);
- the distribution `5,2,2,2,2,2` (8,000 systems).

These checks are falsification evidence only.  They do not prove the theorem
for unbounded class sizes.
