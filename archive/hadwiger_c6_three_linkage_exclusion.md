# The \(C_6\) contact core permits only the identity prism linkage

## 1. Setting

Let

\[
 \overline{G[S]}=C_6\mathbin{\dot\cup}K_1,qquad
 C_6=0,4,2,3,1,5,0,qquad S=\{0,\ldots,6\}, \tag{1.1}
\]

and let (D,D') be the two connected full shores.  Contract (D') to
a helper (H) complete to (S).

The six edges of the missing cycle have two alternating perfect matchings:

\[
 \mathcal M_0=\{04,23,15\},qquad
 \mathcal M_1=\{42,31,50\}.                         \tag{1.2}
\]

An \(\mathcal M_i\)-linkage in \(D\) means three pairwise
vertex-disjoint paths whose interiors lie in \(D\), one joining the ends
of each pair in \(\mathcal M_i\).

## 2. A three-linkage immediately gives (K_7)

### Theorem 2.1

Neither full shore contains an \(\mathcal M_0\)-linkage or an
\(\mathcal M_1\)-linkage.

#### Proof

Suppose first that (D) contains three disjoint path interiors
(A,B,C) for (04,23,15), respectively.  Since (D) is connected, join
these three connected sets by a minimal connector.  Split and absorb the
connector so that (A,B,C) remain disjoint and connected and their
adjacency graph is a tree.  Up to the three possible centres, this tree is
one of

\[
 AB+BC,qquad AB+AC,qquad AC+BC.                   \tag{2.1}
\]

If (BC) is an edge of the tree (the first or third case), use

\[
 \{0\},\ \{1\},\ \{2\},\ \{6\},\ H,
 \quad A\cup\{4,5\},\quad B\cup C\cup\{3\}.       \tag{2.2}
\]

If the tree is (AB+AC), use

\[
 \{0\},\ \{1\},\ \{2\},\ \{6\},\ H,
 \quad B\cup\{3,4\},\quad A\cup C\cup\{5\}.    \tag{2.3}
\]

All bags are connected by the indicated path contacts, connector-tree
edges, and the present boundary edges (45,34).  The two nonsingleton
bags are adjacent through the remaining connector-tree edge.  The helper
(H) sees every boundary-containing bag, and comparison with (1.1)
verifies all other adjacencies.  Thus (2.2) or (2.3) is a (K_7)-model.

Now let (A,B,C) be the path interiors for (42,31,50).  If (BC) is a
connector-tree edge, use

\[
 \{0\},\ \{1\},\ \{2\},\ \{6\},\ H,
 \quad A\cup\{3,4\},\quad B\cup C\cup\{5\}.       \tag{2.4}
\]

In the remaining tree (AB+AC), use

\[
 \{0\},\ \{1\},\ \{2\},\ \{6\},\ H,
 \quad B\cup\{3,5\},\quad A\cup C\cup\{4\}.    \tag{2.5}
\]

Connectivity uses (34,35), respectively, and the same direct check gives
a (K_7)-model.  This contradiction proves the theorem. \(\square\)

The finite quotient check is especially small: contract \(A,B,C,H\), add
each of the three possible trees on \(A,B,C\), and replay the seven bags
in (2.2)--(2.5).  No assumptions about the orders or internal structures
of the shores are used.

## 3. All nonidentity prism matchings are excluded

The present graph on \(W=\{0,\ldots,5\}\) is the triangular prism, with
triangles

\[
 P=\{0,1,2\},\qquad Q=\{3,4,5\},
\]

and identity matching

\[
 I=\{03,14,25\}.                                      \tag{3.1}
\]

For a bijection \(\pi:P\to Q\), call three mutually vertex-disjoint
\(P\)-to-\(Q\) paths, one for each pair \(x\pi(x)\), a
\(\pi\)-linkage.  Its non-boundary vertices are required to lie in a
single shore, but an identity edge may of course itself be used as a
one-edge path.

### Theorem 3.1 (nonidentity three-linkage exclusion)

No full shore supports a \(\pi\)-linkage for any \(\pi\ne I\).

### Proof

Simultaneously permuting the three columns of the triangular prism is a
boundary automorphism.  Hence a nonidentity \(\pi\) has one of two
types.

If \(\pi\) is a transposition, it fixes one column and its other two
pairs are two opposite edges of the missing cycle.  In the canonical
case these are \(15\) and \(24\).  Discard the fixed-column path.  The
remaining two disjoint paths are one of

\[
 04\mid13,\qquad 42\mid15,\qquad 23\mid50.           \tag{3.2}
\]

The ordinary crossing quotient for each pair in (3.2), together with
the opposite full shore, is a \(K_7\)-model.

If \(\pi\) is a three-cycle, its three pairs are, up to the same boundary
automorphism, exactly \(\mathcal M_0\) or \(\mathcal M_1\).  This is
excluded by Theorem 2.1. \(\square\)

For audit, `c6_nonidentity_three_linkage_verify.py` independently checks
all six bijections and all three possible connector trees.  In its
transparent certificate family the identity matching is the unique
negative row; every one of the other fifteen instances has seven
explicit bags.

## 4. Structural interpretation

The three opposite pairs of missing-cycle edges are

\[
 04\mid13,qquad 42\mid15,qquad 23\mid50.          \tag{3.1}
\]

A two-linkage for any pair in (3.2) already gives a \(K_7\)-minor by the
ordinary crossing quotient.  Hence each shore simultaneously has:

1. no linkage for any of the three opposite pairs (three crossless
   four-terminal societies); and
2. no linkage for either alternating perfect matching (Theorem 2.1);
3. equivalently, no nonidentity \(P\)-to-\(Q\) three-linkage
   (Theorem 3.1).

These five nonidentity matching exclusions are the natural infinite-order
description of the sole six-edge residual.  A missing-cycle-rooted \(C_6\)-model in a
shore would in particular supply one of the alternating three-linkages,
so it too is excluded.

Conversely, any theorem that classifies a two-connected six-terminal graph
with the five exclusions above into a prism/rope web plus pieces behind
three-vertex adhesions is exactly suited to the contact problem: the
two-piece atlas and seven-connectivity already control two-cuts and would
eliminate any nontrivial piece whose boundary contacts have order at most
three.
