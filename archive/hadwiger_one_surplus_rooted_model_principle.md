# The one-surplus rooted-model principle

## 1. Statement

Let \(r\ge 2\), let \(H\) be a graph, and let

\[
                    \mathcal D=(D_1,\ldots,D_{r+1})
\]

be pairwise disjoint nonempty connected subgraphs of \(H\).  Let \(N\)
be a terminal set and assume that every \(D_i\) meets \(N\).  The support
graph \(Q=Q(\mathcal D)\) has vertex set \([r+1]\), with \(ij\in E(Q)\)
exactly when \(D_i\) and \(D_j\) are adjacent in \(H\).  Put
\(F=\overline Q\).

Throughout this note, **grouping the pieces** means taking every new
branch set to be the union of a selected collection of whole \(D_i\)'s;
pieces are not split and no vertex outside their union is introduced.
The exact converses below are converses only for this whole-piece
construction.  Other vertices of \(H\) can of course create clique models
which the support quotient does not see.

### Theorem 1.1 (exact one-surplus rooted packing)

The pieces \(D_i\) can be grouped into \(r\) pairwise adjacent connected
branch sets, every one meeting \(N\), if and only if \(F\) contains none
of

\[
                         K_3,\qquad P_4,\qquad 3K_2       \tag{1.1}
\]

as a (not necessarily induced) subgraph, with isolated vertices ignored.

Equivalently, the grouping exists if and only if either

1. some vertex \(x\) covers every edge of \(F\); or
2. some two vertices \(x,y\) cover every edge of \(F\), while

   \[
             xy\notin E(F),\qquad
             N_F(x)\cap N_F(y)=\varnothing.              \tag{1.2}
   \]

In outcome 1, discard \(D_x\).  In outcome 2, merge \(D_x\) and
\(D_y\), retaining every other piece as a singleton branch set.

This is a rooted statement: no terminal assignment or rerouting is lost
in the grouping, because every retained group contains at least one of
the original rooted pieces.

## 2. Proof of the exact criterion

An \(r\)-branch-set model supported on a graph with \(r+1\) vertices has
only two possible size patterns.  It either omits one support vertex and
uses \(r\) singleton branch sets, or it uses all support vertices and has
one branch set of size two and \(r-1\) singleton branch sets.  In the
second pattern the two merged vertices must be adjacent.

The first pattern exists exactly when \(Q-x\cong K_r\) for some \(x\),
which says that \(x\) covers every edge of \(F\).  The second exists
exactly when adjacent \(x,y\) satisfy

\[
 Q-\{x,y\}\cong K_{r-1}
 \quad\text{and}\quad
 N_Q(x)\cup N_Q(y)\supseteq V(Q)-\{x,y\}.
\]

In the complement this is precisely (1.2), with \(\{x,y\}\) a vertex
cover of \(F\).  This proves the cover formulation.

It remains to characterize failure of the two cover alternatives.  Each
graph in (1.1) is plainly a certificate of failure:

* \(3K_2\) has vertex-cover number three;
* every two-cover of \(K_3\) uses an edge of \(F\);
* every two-cover of \(P_4\) either uses its middle edge or has a common
  neighbour in \(F\).

Conversely, suppose \(F\) has no admissible cover and choose an
edge-minimal subgraph \(F_0\subseteq F\) with the same property.  If
\(F_0\) has a matching of size three, those three edges already certify
failure, so minimality gives \(F_0=3K_2\).  If it has a three-edge path,
that path already certifies failure, so \(F_0=P_4\).

Assume neither occurs.  Every nontrivial component of \(F_0\) is then a
star or a triangle.  A single star has a one-cover.  Two star components
have an admissible two-cover at their centres.  Three nontrivial
components contain a three-edge matching.  Hence failure forces a
triangle component; the triangle alone is already a certificate, and
minimality gives \(F_0=K_3\).  This proves Theorem 1.1. \(\square\)

## 3. Spanning partitions turn motifs into full-shore separators

Assume now that the \(D_i\) partition \(V(H)\), and that \(H\) is
\(k\)-connected.  If Theorem 1.1 fails, choose one motif in \(F\).

### Theorem 3.1 (rooted packing or concentrated adhesion)

Either the \(r+1\) pieces group to an \(N\)-meeting \(K_r\)-model, or
there are two connected shores \(R_1,R_2\) and an inclusion-minimal
separator \(Z\) with

\[
                    N_H(R_1)=Z=N_H(R_2),
                    \qquad |Z|\ge k,                    \tag{3.1}
\]

such that one of the following holds.

1. A \(K_3\) or \(P_4\) certificate is present, and \(Z\) is contained
   in the union of \(r-2\) named pieces.
2. A \(3K_2\) certificate is present, and \(Z\) is contained in the
   union of \(r-1\) named pieces.

Consequently, when \(k>r-2\) in the first outcome, or \(k>r-1\) in the
second, some named separator piece contains at least two vertices of
\(Z\).  More quantitatively, the total portal surplus beyond one vertex
per named separator piece is at least \(k-r+2\) or \(k-r+1\),
respectively.

#### Proof

For a missing triangle on support vertices \(a,b,c\), delete the other
\(r-2\) support vertices; the three displayed pieces are pairwise
nonadjacent.  For a missing path \(v_1v_2v_3v_4\), delete every support
vertex outside \(\{v_1,v_2,v_3\}\); the piece \(D_{v_2}\) is separated
from \(D_{v_1}\).  For a missing matching, choose either matched pair
and delete the other \(r-1\) support vertices.

Because the partition is spanning, the indicated union of deleted
pieces is an actual vertex separator in \(H\).  Choose an
inclusion-minimal subset \(Z\) which still separates the two selected
piece-unions.  Connectivity gives \(|Z|\ge k\).  Minimality implies
that every \(z\in Z\) has a neighbour in each of the two reachable
components of \(H-Z\), yielding (3.1).  The concentration bounds are
then pigeonhole. \(\square\)

## 4. The \(HC_7\) specialization

In the simultaneous-split cell, \(r=6\) and the seven rooted pieces
partition \(H=G-v\).  The known reduction \(\kappa(G)\ge7\) gives
\(\kappa(H)\ge6\).  Theorem 3.1 therefore says:

* a missing \(K_3\) or \(P_4\) concentrates a separator of order at
  least six inside four named pieces, giving portal surplus at least two;
* a missing \(3K_2\) concentrates such a separator inside five named
  pieces, giving portal surplus at least one.

In either case a named piece is multiply hit.  If equality \(|Z|=6\)
holds, then \(Z\cup\{v\}\) is an exact seven-vertex adhesion in \(G\):
each chosen shore contains a terminal from \(N(v)\), and hence sees
\(v\).  Thus the one-surplus rooted-model obstruction has only two
structural outputs: a grouped rooted clique model, or a concentrated
full-shore adhesion with a named multiply hit piece.

The theorem is uniform in \(r\); the labels and the Moser-spindle
geometry play no role.  What remains outside its scope is the dynamic
step that converts portal multiplicity in a named piece into a new split,
or converts the exact adhesion into compatible minor-critical boundary
states.

## 5. Exact two-surplus packing after one named piece splits

The first dynamic move replaces one support piece by two connected
adjacent rooted pieces.  There are then \(r+2\) support vertices for an
\(r\)-clique target.  The possible grouping patterns are still uniform.

### Theorem 5.1 (exact two-surplus rooted packing)

Let \(D_1,\ldots,D_{r+2}\) be disjoint connected rooted pieces and let
\(Q\) be their support graph.  They group to an \(N\)-meeting
\(K_r\)-model if and only if at least one of the following occurs.

1. **Two omissions.**  For some \(x,y\),
   \(Q-\{x,y\}\cong K_r\).
2. **One omission and one pair.**  For distinct \(z,x,y\), the edge
   \(xy\) is present, \(Q-\{z,x,y\}\cong K_{r-1}\), and every vertex
   outside \(\{z,x,y\}\) is adjacent to at least one of \(x,y\).
3. **One triple.**  Some three-vertex set \(T\) induces a connected
   subgraph, \(Q-T\cong K_{r-1}\), and every vertex outside \(T\) has
   a neighbour in \(T\).
4. **Two pairs.**  There are two disjoint edges \(xy,uw\) such that
   \(Q-\{x,y,u,w\}\cong K_{r-2}\); every remaining vertex sees both
   \(\{x,y\}\) and \(\{u,w\}\); and at least one edge joins those two
   pairs.

#### Proof

If \(d\) support vertices are omitted, then the total reduction obtained
by grouping the retained vertices is \(2-d\), so \(d\in\{0,1,2\}\).
For \(d=2\) all groups are singletons.  For \(d=1\) there is exactly one
two-vertex group.  For \(d=0\), either one group has order three or two
groups have order two.  Connectivity of each nonsingleton group and
pairwise adjacency of all groups give exactly conditions 1--4.
Conversely, each displayed condition explicitly supplies the indicated
grouping.  Every group remains rooted. \(\square\)

This theorem gives exact portal tests for splitting a separator piece in
each atomic one-surplus obstruction.  Two particularly clean tests are
as follows.

### Corollary 5.2 (triangle bisection)

Suppose the old support graph is exactly
\(K_{r+1}-K_3\), with missing triangle \(abc\), and split an old
universal rooted support piece into adjacent connected pieces \(x,y\).
The two new pieces need not separately contain roots.  If both
\(x\) and \(y\) see at least two of \(a,b,c\), then the new support
groups to a rooted \(K_r\).

#### Proof

The old universal piece saw all three triangle vertices, so the two
support sets on \(\{a,b,c\}\) have union three.  Two subsets of size at
least two with union three have a common vertex, say \(a\), while the
other two vertices can be labelled so that \(x\sim b\) and \(y\sim c\).
Use the two paired groups \(x\cup b\) and \(y\cup c\), retaining \(a\)
and every other old piece as singleton groups.  The two paired groups
see \(a\) through \(x,y\), see one another through \(xy\), and see all
old universal singletons through \(b,c\).  This is the support pattern in
Theorem 5.1(4).  Both paired groups are rooted through \(b,c\), so no
root is required in \(x\) or \(y\). \(\square\)

### Corollary 5.3 (path-end bisection)

Suppose the old support graph is exactly
\(K_{r+1}-P_4\), where the missing path is
\(v_1v_2v_3v_4\), and split an old universal rooted support piece into
adjacent connected pieces \(x,y\), not necessarily separately rooted.
If, after possibly exchanging the halves,

\[
                 x\sim v_1,v_2,\qquad y\sim v_3,v_4,   \tag{5.1}
\]

then the new support groups to a rooted \(K_r\).

#### Proof

Use the paired groups \(x\cup v_2\) and \(y\cup v_3\), and retain
\(v_1,v_4\) and all other old pieces as singletons.  The singleton set is
a clique.  The first pair sees \(v_1\) through \(x\) and \(v_4\) through
\(v_2\); the second sees \(v_4\) through \(y\) and \(v_1\) through
\(v_3\).  The pairs see one another through \(xy\), and the unsplit
universal pieces through their path vertices.  This is Theorem 5.1(4)'s
support pattern, and each paired group is rooted through \(v_2,v_3\).
\(\square\)

The hypotheses “exactly” in Corollaries 5.2--5.3 can be weakened to the
specific adjacencies used in their proofs.  They are kept here to isolate
the structural message: in two of the three atomic webs, a multiply hit
universal piece opens as soon as its two rooted halves distribute the
motif portals on both sides.  Persistent failure therefore forces a
one-sided portal order, rather than merely a shortage of contacts.
