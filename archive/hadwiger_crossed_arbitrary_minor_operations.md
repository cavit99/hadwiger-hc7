# Crossed splicing for arbitrary shore-supported minor operations

## 1. Boundary-faithful minors

Let \(G\) be a graph which is not \(r\)-colourable, and let
\((A,B)\) be a separation of \(G\), with

\[
                         W=A\cap B.                         \tag{1.1}
\]

The formulation below includes the apex version: if \((A_0,B_0)\) is
a separation of \(G-v\), use

\[
                         A=A_0\cup\{v\},\qquad
                         B=B_0\cup\{v\},
\]

so that \(W=(A_0\cap B_0)\cup\{v\}\).  The old “marked state” is simply
the equality partition on \(W\).

Let \(Q_A\) be a minor of \(G\).  Say that it is **\(B\)-faithful** if
there is an injective labeling

\[
                         \lambda_A:B\longrightarrow V(Q_A)  \tag{1.2}
\]

such that

\[
 bb'\in E(G[B])
 \quad\Longrightarrow\quad
 \lambda_A(b)\lambda_A(b')\in E(Q_A).                       \tag{1.3}
\]

Thus a colouring of \(Q_A\), pulled back through \(\lambda_A\), is a
proper colouring of the untouched closed shore \(G[B]\).  Extra edges
among labeled images are allowed.

There are two useful sufficient minor-model descriptions.

1. **Strict open-shore support.**  Every deletion and every nontrivial
   contraction branch set lies in \(A-W\); every vertex and edge of
   \(G[B]\) is retained literally.
2. **Boundary-anchored support.**  A contraction branch set may meet
   \(W\), but it meets \(B\) in exactly one vertex \(w\in W\), is
   contained in \(\{w\}\cup(A-W)\), and distinct boundary labels use
   disjoint branch sets.  Label its contracted image by \(w\).  Every
   vertex of \(B-W\) remains a singleton branch set, and no edge of
   \(G[B]\) is deleted.

Both descriptions imply (1.2)--(1.3).  The second permits a rooted
branch set to be collapsed onto its one adhesion root.  It never
identifies two adhesion vertices.

If “no contraction of \(W\)” is interpreted literally as requiring
every \(w\in W\) to remain a singleton branch set, only description 1
is allowed.  The crossed theorem remains valid.  The Hall-circuit
rooted-clique application below needs description 2; its safety follows
from faithfulness, not from pretending that the rooted contraction is
strictly open-shore.

## 2. Arbitrary-operation crossed splice

### Theorem 2.1 (boundary-faithful crossed-minor theorem)

Let \(Q_A,Q_B\) be proper minors of \(G\), where \(Q_A\) is
\(B\)-faithful and \(Q_B\) is \(A\)-faithful.  Let
\(\phi_A,\phi_B\) be proper \(r\)-colourings of those minors.  If their
labeled restrictions induce the same equality partition on \(W\),

\[
 \Pi_W(\phi_A\circ\lambda_A)
 =
 \Pi_W(\phi_B\circ\lambda_B),                              \tag{2.1}
\]

then \(G\) is \(r\)-colourable, a contradiction.

#### Proof

Equality of the partitions gives a palette permutation \(\pi\) such
that

\[
 \pi\phi_A(\lambda_A(w))
 =
 \phi_B(\lambda_B(w))
 \qquad(w\in W).                                            \tag{2.2}
\]

Colour \(A\) by pulling \(\phi_B\) back through its \(A\)-faithful
labeling.  Colour \(B-A\) by pulling \(\pi\phi_A\) back through its
\(B\)-faithful labeling.  The restrictions agree on \(W\) by (2.2).
Every edge of \(G[A]\) is proper by \(A\)-faithfulness of \(Q_B\), and
every edge with a vertex in \(B-A\) is proper by \(B\)-faithfulness of
\(Q_A\).  No edge joins the two open shores.  This colours \(G\), a
contradiction.  \(\square\)

The proof uses only faithfulness, not the order or type of the
operations.  It applies simultaneously to edge/vertex deletions,
sequences of contractions, and contractions of disjoint rooted branch
sets.

### Corollary 2.2 (opposite operation-state sets are disjoint)

Let \({\cal M}_A\) be any family of \(B\)-faithful proper minors
supported from the \(A\)-shore, and define \({\cal M}_B\) symmetrically.
The sets of equality partitions on \(W\) induced by their
\(r\)-colourings are disjoint.

In a proper-minor-minimal non-\(r\)-colourable graph, every member of
the two families is \(r\)-colourable.  Thus every attempted pair of
opposite operations must expose a genuine boundary-state mismatch.

## 3. Audit of contraction subtleties

The following conditions cannot be dropped silently.

1. **No two boundary labels in one contraction branch set.**  Otherwise
   the minor assigns one colour to two original boundary vertices and
   the pullback need not colour an edge between them.
2. **No deletion of the untouched closed shore.**  If an original edge
   of \(G[B]\) is missing in \(Q_A\), its ends may receive one colour,
   invalidating the crossed restriction.
3. **No opposite-shore vertex inside a nontrivial branch set.**  Such a
   contraction can identify or delete a vertex whose original colour is
   needed in the crossed half.
4. **Extra boundary adjacencies are harmless.**  Contracting an
   \(A\)-side set onto \(w\in W\) may make its image adjacent to
   additional vertices of \(W\).  This only restricts
   \(\phi_A|_W\).  The crossed colouring uses \(\phi_A\) on the
   untouched \(B\)-side, where every original edge is still represented.
5. **A common protected vertex is just another boundary label.**  In the
   apex formulation, retaining \(v\) as a singleton in both minor
   models makes equality on \(X\cup\{v\}\) exactly the earlier marked
   state condition.

These conditions are sufficient, and (1.2)--(1.3) are the exact
abstract hypotheses used by the proof.

## 4. Application to an exact Hall-deficit circuit

Use the notation of
hadwiger_relative_deficit_circuit_promotion.md.  Thus \(I\) is a
minimal nonlinkable set of deficient bags,

\[
                         |X|=|I|-1=:q,                       \tag{4.1}
\]

\(U\) is the root-side union, and

\[
                         S=\{v\}\cup X\cup P                 \tag{4.2}
\]

is the promoted genuine adhesion.

Corollary 2.2 of that note supplies \(q\) disjoint root-to-\(X\)
prefixes in \(G[U\cup X]\).  Label them \(R_x\), \(x\in X\), and let
\(n_x\in N(v)\cap U\) be the root of \(R_x\).

For every omitted index \(i\in I\), Corollary 2.3 supplies on the far
side an \(X\)-rooted \(K_q\)-model

\[
                         (F_x^i:x\in X),                      \tag{4.3}
\]

whose branch sets meet \(S\) exactly in their labeled roots \(x\).
The latter assertion uses \(P_i=\varnothing\) and the fact that the
model uses only the deficient bags \(B_j\), \(j\in I-\{i\}\), while
\(P\) lies in accessible bags.

### Root operation

Contract every prefix \(R_x\) to its labeled endpoint \(x\).  The
prefixes are disjoint and meet \(S\) only at their distinct endpoints,
so this is a boundary-anchored root-shore operation.  Call the minor
\(Q_R\).  Since \(n_xv\) was an edge, \(Q_R\) contains every edge

\[
                              vx\qquad(x\in X).                \tag{4.4}
\]

Hence every \(r\)-colouring of \(Q_R\) puts \(v\) in a different block
from every \(x\), although different vertices of \(X\) may still share
a colour.

### Far operation

For fixed \(i\), contract every rooted branch set \(F_x^i\) to its
labeled root \(x\).  This is a boundary-anchored far-shore operation;
call the minor \(Q_F^i\).  Its images of \(X\) induce \(K_q\), so every
\(r\)-colouring of \(Q_F^i\) makes the vertices of \(X\) pairwise
different.  It need not separate the colour of \(v\) from every
\(x\).

### Theorem 4.1 (Hall circuit becomes an exact rainbow-state mismatch)

Let \({\cal T}_R\) be the equality partitions of \(S\) induced by
\(r\)-colourings of \(Q_R\), and let \({\cal T}_F^i\) be those induced
by \(Q_F^i\).  Then

\[
                         {\cal T}_R\cap{\cal T}_F^i
                         =\varnothing
                         \qquad(i\in I).                       \tag{4.5}
\]

Moreover, any hypothetical common partition would restrict on
\(\{v\}\cup X\) to the rainbow partition.

#### Proof

The root operation is far-side faithful and the far operation is
root-side faithful.  Equation (4.5) is Theorem 2.1.

By (4.4), a root-operation state separates \(v\) from every \(x\).
By (4.3), a far-operation state separates every two vertices of \(X\).
Both conditions together say that \(\{v\}\cup X\) is rainbow.
\(\square\)

Thus the Hall deficit has been promoted beyond a numerical capacity
cut:

\[
\boxed{\text{opposite rooted contractions have disjoint full-adhesion
state sets, and their only possible common core state is rainbow.}}
\tag{4.6}
\]

## 5. Can the contractions be forced to share the rainbow state?

Not from the Hall-circuit data proved so far.

The two operations impose complementary, not identical, constraints:

\[
\begin{array}{c|c}
Q_R & v\ne x\text{ for all }x\in X,\quad
      X\text{ may repeat colours},\\
Q_F^i & X\text{ is rainbow},\quad
      v\text{ may share a colour with one }x.
\end{array}                                                  \tag{5.1}
\]

There is a useful simultaneous reference operation.  For fixed
\(i\in I\), the union

\[
                         C_x^i=R_x\cup F_x^i                  \tag{5.2}
\]

is connected, and the sets \(C_x^i\), \(x\in X\), are pairwise
disjoint.  Contract all of them to their labels \(x\).  Call the
resulting proper minor \(Q_{RF}^i\).  Its labeled vertices
\(\{v\}\cup X\) induce \(K_{q+1}\): the root prefixes supply every
\(vx\), and the far rooted model supplies every \(xx'\).

Hence every \(r\)-colouring of \(Q_{RF}^i\) supplies a boundary state
\(\sigma\) on \(S\) which is rainbow on \(\{v\}\cup X\).  The crossed
theorem gives the exact repair lock

\[
                 \sigma\notin{\cal T}_R
                 \quad\hbox{or}\quad
                 \sigma\notin{\cal T}_F^i.                    \tag{5.3}
\]

Indeed, membership in both sets would contradict (4.5).  Thus the
simultaneous contraction automatically creates the desired rainbow
core state, but at least one shore refuses to realize that same state
when the other shore's contraction is undone.

In the earlier apex terminology, this is precisely an **unpinned
rainbow marked state on \(X\)**: the vertices of \(X\) are singleton
blocks and the apex block is disjoint from all of them.

Even if one finds colourings of both minors which are rainbow on
\(\{v\}\cup X\), their equality relations involving the additional
portal vertices \(P\) may differ.  The crossed theorem needs equality
on the full genuine adhesion \(S=\{v\}\cup X\cup P\), because paths
through \(P\) are actual root-to-far bypasses.

Consequently the present Hall circuit does **not** by itself close the
capacity defect.  It reduces the missing assertion to either of the
following exact statements.

1. **Rainbow repair.**  \(Q_R\) has an \(r\)-colouring making \(X\)
   pairwise distinct, and some \(Q_F^i\) has an \(r\)-colouring making
   \(v\) distinct from \(X\), with the same equality pattern on \(P\).
2. **Portal-state forcing.**  The circuit exchange over all
   \(i\in I\) and all root-prefix linkages forces
   \({\cal T}_R\cap{\cal T}_F^i\ne\varnothing\) for some \(i\).

Equivalently, starting from \(Q_{RF}^i\), prove that its rainbow state
can be repaired on both shores while \(S\) is fixed.  Equation (5.3)
says that a counterexample must lock at least one of those two repairs.

Either statement would contradict (4.5) and close the Hall circuit.
Neither follows merely from the star (4.4), the rooted clique (4.3), or
the numerical surplus bound on \(P\).  In particular, deleting \(P\)
from the state comparison is invalid.

This identifies the precise reusable target: synchronize a rainbow core
state **and** its portal equality pattern.  It is strictly narrower than
an arbitrary rooted-clique theorem, but it remains a genuine
colour-extension problem.
