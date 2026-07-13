# Hand-checkable terminal certificate for the Moser owner descent

## 1. The finite lemma

Let \(G\) be seven-connected with \(\delta(G)\ge7\), let \(S\) be a
seven-cut, and let \(D\) be a full component of \(G-S\).  Fix a
partition

\[
 S=A_1\dot\cup A_2\dot\cup A_3\dot\cup\{s\},
 \qquad |A_i|=2.
\]

### Lemma 1.1

If \(4\le |D|\le6\) and \(D\) is three-connected, then \(D\) contains
disjoint connected carriers for two of \(A_1,A_2,A_3\).

In particular, such a shore owns every Moser partition and cannot be a
low-owner shore.

## 2. Reduction to three facial cycles

Suppose the conclusion fails.  For each two pair blocks, attach four
artificial terminals to their complete portal sets.  The corresponding
tuple is crossless.  The same-vertex Two Paths Theorem embeds it in a
web.  A nonempty clique inserted behind a facial triangle, together
with the three omitted boundary roots, would give a cut of order at
most six separating an original shore vertex from another full shore.
Thus all three webs are bare.

The first web proves \(D\) planar.  Whitney uniqueness gives one fixed
embedding of \(D\).  There are faces

\[
F_{12},F_{13},F_{23}
\]

containing the complete portal sets for the indicated two blocks.  In
particular,

\[
\begin{aligned}
 P(A_1)&\subseteq F_{12}\cap F_{13},\\
 P(A_2)&\subseteq F_{12}\cap F_{23},\\
 P(A_3)&\subseteq F_{13}\cap F_{23}.
\end{aligned}                                      \tag{2.1}
\]

All three intersections in (2.1) are nonempty by fullness.

For \(v\in D\), let \(m(v)\) be the number of these three pairwise face
intersections which contain \(v\).  Equation (2.1) gives the elementary
upper bound

\[
 |N_S(v)|\le 1+2m(v):                              \tag{2.2}
\]

the \(1\) is the omitted root \(s\), and each intersection accounts for
at most the two roots of one pair block.  Minimum degree therefore
requires

\[
             d_D(v)+1+2m(v)\ge7
             \qquad(v\in D).                       \tag{2.3}
\]

Thus the problem is reduced from \(2^{7|D|}\) contact matrices to a
list of triples of ordinary facial cycles.

## 3. Complete facial table

There are ten planar three-connected unlabelled graphs on four to six
vertices.  The complete atlas gives the following table.  The middle
column counts unordered face triples, with repetition allowed, whose
three pairwise intersections are nonempty.  The last column counts
those which also satisfy (2.3) at every vertex.

\[
\begin{array}{c|c|c|c}
\text{order}&\text{graph6}&
 \text{nonempty-intersection triples}&
 \text{degree-compatible triples}\\ \hline
4&C{\sim}&20&0\\
5&Dl\{&35&0\\
5&Dn\{&56&0\\
6&EtTg&30&0\\
6&Ehfw&56&0\\
6&EzNG&50&0\\
6&ER{\sim}g&77&0\\
6&Ep{\sim}o&70&0\\
6&Ep{\sim}w&104&0\\
6&EznW&88&0
\end{array}
\]

Every nonplanar three-connected graph is already excluded by the first
bare web.  The last column proves Lemma 1.1.

The short verifier
moser_three_shore_small_face_verify.py reconstructs this table directly
from the NetworkX graph atlas.  It uses no SAT solver, no minor-model
search, and no variable portal incidences.  Its sole test is the
inequality (2.3), so each row can also be checked by hand from the
facial cycles of the indicated graph.

## 4. Orders one to three

The remaining orders have elementary proofs.

* If \(|D|=1\), fullness makes its vertex adjacent to all seven roots.
  This is the unique terminal survivor.
* If \(|D|=2\), connectedness gives one internal edge.  Minimum degree
  makes each vertex contact at least six boundary roots.  For every
  partition, each vertex fully contacts at least two of the three pair
  blocks; the two adjacent singleton carriers can be assigned distinct
  blocks.  Thus \(D\) owns every partition.
* A three-vertex path has a cutvertex and owns every partition by the
  cutvertex ownership lemma.  If \(D=K_3\), every vertex contacts at
  least five roots.  For a fixed partition, every vertex fully contacts
  at least one pair block.  If two vertices admit distinct blocks, they
  themselves are the required carriers.  Otherwise all three fully
  contact the same block \(A_i\), and each contacts exactly one root
  from each other block.  Fullness supplies two vertices which differ
  on one of those blocks.  Their edge is a carrier for that block, and
  the third vertex is a disjoint carrier for \(A_i\).

Consequently, among connected shores of order at most six satisfying
the counterexample-derived hypotheses and having no exact-cut descent,
the sole low-owner possibility is a single vertex complete to \(S\).

## 5. Certification scope

This is a transparent replacement for the opaque order-four-to-six
Z3 result in moser_three_shore_terminal_cegis.py.  The larger script
remains a useful independent cross-check and now asserts the exact
twenty-five-record digest

\[
\texttt{d74287d353e0f3d49b1f24c90f42938b08ba40e3543cad5070348a908d75576b}.
\]

The certificate closes only the finite endpoint.  A strict nested
seven-fragment exported by the owner-descent theorem has a new boundary
which need not be Moser and does not automatically inherit the
ownership invariant.

