# The cycle leaf of the locked \(C_6\) rope

## 1. Setting

Let

\[
 S=\{c_0,c_1,\ldots,c_5,z\},
\]

where the only missing boundary edges are
\(c_ic_{i+1}\), with indices modulo six.  Let \(D\) be the
high-owner full shore and let \(H\) denote the other full shore.  We use
the audited facts that

* \(G\) is seven-connected, \(\delta(G)\geq7\), and
  \(\alpha(G[N(u)])\leq d(u)-5\) for every vertex \(u\);
* \(D\) is two-connected;
* every two-cut of \(D\) has exactly two components; and
* a shore vertex of shore degree two has the exact portal lock

\[
 S-N_S(x)=N_{C_6}(v_x),\qquad
 S-N_S(D-x)=\{v_x\}.                              \tag{1.1}
\]

Consider a leaf S-torso of an SPQR decomposition of \(D\).  Its unique
virtual edge has ends \(p,q\), and its real part is a chordless path

\[
 p x_1x_2\cdots x_rq .                            \tag{1.2}
\]

The vertices \(x_i\) have shore degree two.

## 2. A cycle leaf is one vertex

### Lemma 2.1

In (1.2), \(r=1\).  Moreover \(pq\in E(D)\).

### Proof

Suppose first that \(r\geq2\), and consider the end vertex \(x_1\).
Its shore neighbours are \(p,x_2\), which are nonadjacent because
(1.2) is the real path of an S-torso.  By (1.1), \(x_1\) is the unique
shore neighbour of \(v_{x_1}\).  Thus neither \(p\) nor \(x_2\) is
adjacent to \(v_{x_1}\), whereas \(x_1v_{x_1}\) is an edge.  Hence

\[
 \{p,x_2,v_{x_1}\}
\]

is an independent triple in \(N_G(x_1)\).  But (1.1) gives five
boundary neighbours and two shore neighbours at \(x_1\), so
\(d_G(x_1)=7\); Dirac's bound gives
\(\alpha(N_G(x_1))\leq2\), a contradiction.

Therefore \(r=1\); write \(x=x_1\).  Normalize \(v_x=c_0\).  Then

\[
 N_S(x)=S-\{c_5,c_1\},\qquad
 N_S(D-x)=S-\{c_0\}.                              \tag{2.1}
\]

Both \(p,q\) lie in \(D-x\), so both miss \(c_0\).  If \(pq\) were
not an edge, then \(\{p,q,c_0\}\) would be an independent triple in
\(N_G(x)\), again contradicting Dirac's bound.  Thus \(pq\in E(D)\).
\(\square\)

This argument supersedes an earlier erroneous distance-two-label
enumeration.  No multi-vertex S-leaf certificate is needed.

## 3. Exact one-ear contact frontier

Let \(B\) be the component of \(D-\{p,q\}\) different from \(\{x\}\).
It is connected, and seven-connectivity gives \(|N_S(B)|\geq5\).  Put

\[
 A=\{c_2,c_4\},\qquad T=\{c_3\}.                 \tag{3.1}
\]

### Lemma 3.1

Every exact-atlas-negative one-ear state has

\[
\begin{aligned}
 N_S(B)&\supseteq\{c_1,c_2,c_4,c_5\},\\
 N_S(p),N_S(q)&\in
 \{A,A\cup\{z\},T,T\cup\{z\}\}.                \tag{3.2}
\end{aligned}
\]

The maximal states which remain negative even after testing the whole
one-ear quotient are

\[
\begin{array}{c|c|c}
N_S(B)&N_S(p)&N_S(q)\\ \hline
S-\{c_0\}&A&A\cup\{z\}\\
S-\{c_0\}&A\cup\{z\}&A\\
S-\{c_0\}&A\cup\{z\}&T\cup\{z\}\\
S-\{c_0\}&T\cup\{z\}&A\cup\{z\}\\
S-\{c_0\}&T\cup\{z\}&T\cup\{z\}.
\end{array}                                       \tag{3.3}
\]

Every negative state is coordinatewise contained in a row of (3.3).

### Certificate

Use the original atlas labels, whose missing cycle is
\(0,4,2,3,1,5,0\).  Then

\[
 N_S(x)=79,quad A=6,quad A\cup\{z\}=70,quad
 T=8,quad T\cup\{z\}=72 .                        \tag{3.4}
\]

The six connected allocations

\[
 x\mid Bpq,\ xp\mid Bq,\ xq\mid Bp,\ xpq\mid B,
 \quad p\mid xBq,\quad q\mid xBp                 \tag{3.5}
\]

are required to lie in the exact negative two-piece atlas.  The program
`c6_cycle_leaf_probe.py` enumerates all contact rows satisfying (2.1),
\(|N_S(B)|\geq5\), Dirac's neighbourhood bound at \(x\), and (3.5).
There are 64.  It then exhaustively enumerates all seven branch sets in
the quotient.  The complete maximal negative frontier is exactly

\[
 (126,6,70),(126,70,6),(126,70,72),
 (126,72,70),(126,72,72),                           \tag{3.6}
\]

which is (3.3).  In particular, the apparent broad--broad maximum
\((126,70,70)\) is positive.  The program prints an explicit model; in
cyclic notation its bags are

\[
 H\cup\{c_0,c_1,c_4,c_5\},\quad \{c_2\},\quad
 \{x,c_3\},\quad\{z\},\quad B,\quad\{p\},\quad\{q\}.
                                                               \tag{3.7}
\]

The three possible proper reductions of the \(B\)-row below this
positive maximum are checked separately, rather than inferred by
monotonicity in the wrong direction.

## 4. The seven-fan eliminates every broad cut vertex

### Lemma 4.1 (distributed fan arms)

There are two internally vertex-disjoint paths in \(D-x\), one starting
at \(p\), one at \(q\), and ending at \(c_1,c_5\) in some order.  Their
internal vertices avoid \(S\).

### Proof

By the Fan Lemma, seven-connectivity supplies a seven-fan from \(x\) to
the seven-set \(S\).  Shorten every arm at its first vertex of \(S\).
The seven arms start through distinct neighbours of \(x\).  Since
\(d_G(x)=7\), they use all five boundary neighbours of \(x\), together
with \(p,q\).  An arm starting with a boundary neighbour ends there.
Consequently the arms through \(p,q\) end at the two remaining boundary
vertices, namely \(c_1,c_5\).  Before first meeting \(S\), an arm which
starts in the component \(D\) cannot leave \(D\).  This proves the
claim. \(\square\)

### Theorem 4.2 (cycle-leaf fan closure)

If either \(p\) or \(q\) is broad, meaning that it is adjacent to both
\(c_2,c_4\), then \(G\) contains a \(K_7\)-minor.

### Proof

Assume first that \(p\) is broad.  Contract the internal vertices of
the two paths in Lemma 4.1 toward their starts, retaining their boundary
ends.  Delete all unused vertices of \(B\).  This is legitimate because
the two paths are internally disjoint and the model below uses no
branch set from the remaining body.

If the arms run \(p\) to \(c_1\) and \(q\) to \(c_5\), use

\[
 \{p,c_0,c_2\},\quad \{q,x,c_4\},\quad
 \{c_1\},\quad\{c_3\},\quad\{c_5\},\quad\{z\},\quad H.       \tag{4.1}
\]

If they run \(p\) to \(c_5\) and \(q\) to \(c_1\), use

\[
 \{p,c_0,c_4\},\quad \{q,x,c_2\},\quad
 \{c_1\},\quad\{c_3\},\quad\{c_5\},\quad\{z\},\quad H.       \tag{4.2}
\]

The first two bags in either line are connected: \(p\) touches the
displayed broad root, \(q x\) is an edge, and \(x\) touches the displayed
root.  They are adjacent through \(pq\).  The vertices
\(c_1,c_3,c_5\) form a triangle in the complement of the missing
six-cycle.  In (4.1), the two fan edges supply the adjacencies to
\(c_1,c_5\), while \(c_3c_0\) and \(xc_3\) supply the adjacencies to
\(c_3\); all remaining adjacencies follow from nonconsecutiveness on the
missing cycle.  The check for (4.2) is symmetric.  The vertex \(z\) is
complete to the six rim vertices, and the full shore \(H\) is connected
and adjacent to every boundary-rooted bag.  Thus (4.1) and (4.2) are
\(K_7\)-models.  Interchanging \(p,q\) proves the other case.
\(\square\)

The NetworkX-based exact replay `c6_cycle_leaf_fan_verify.py` tests
both fan orientations and all optional \(z\)-contacts.  It finds a
model exactly when at least one cut vertex is broad.  Because its body
vertex is deleted before the minor search, its certificates do not
silently assume that the complement of the two arms is connected.

## 5. Exact residual

Every surviving cycle leaf therefore has the following **double-thin
lock**:

\[
\begin{aligned}
N_S(p),N_S(q)&\in\{\{c_3\},\{c_3,z\}\},\\
N_S(B)&\supseteq\{c_1,c_2,c_4,c_5\},\\
N_S(B)\cap\{c_3,z\}&\ne\varnothing .              \tag{5.1}
\end{aligned}
\]

Moreover \(p,q\) have internally disjoint routed contacts to
\(c_1,c_5\), one each.  Since a thin cut vertex has at most two boundary
neighbours, minimum degree seven gives at least five shore neighbours;
besides \(x\) and the other cut vertex it has at least three neighbours
in \(B\) (at least four if it misses \(z\)).

The component \(B\) here is the entire component on the other side of
the leaf separation, not necessarily one SPQR torso.  Thus the result
applies to a leaf of an arbitrarily long SPQR path.  If the SPQR tree has
two nodes, \(B\cup\{p,q\}\) is the expansion of the other node; in a
longer rope it contains every later torso.  The fan proof is insensitive
to this distinction because it deletes every body vertex outside the two
selected arms.

## 6. The double-thin web is impossible

We use the following standard bare consequence of the Two Paths
Theorem.

> **Bare-web consequence.**  Let \(J\) have four distinct terminals
> \(a_1,b_1,a_2,b_2\).  Suppose every component of \(J-X\) contains a
> terminal whenever \(|X|\leq3\).  If \(J\) has no pair of disjoint
> paths joining \(a_1\) to \(b_1\) and \(a_2\) to \(b_2\), then \(J\)
> has a plane embedding in which the four terminals lie on one face.

Indeed, take an edge-maximal supergraph with no such linkage and apply
the web form of the Two Paths Theorem.  Every nonplanar insertion is
attached to a facial triangle.  Its interior is a terminal-free
component after deleting at most three vertices, contrary to the
hypothesis.  The remaining web is plane with the four terminals on its
outer face, and deleting the added edges gives the assertion for \(J\).

### Theorem 6.1 (cycle-leaf elimination)

The double-thin lock (5.1) cannot occur.  Consequently the high-owner
shore has no S-node leaf in its SPQR decomposition.

### Proof

Suppose (5.1) holds and put

\[
 J=G[D\cup\{c_0,c_1,c_3,c_4\}].                  \tag{6.1}
\]

There are no disjoint \(c_0\)-\(c_1\) and
\(c_3\)-\(c_4\) paths in \(J\).  Such paths cannot use either of the
other two terminals internally, so all their nonterminal vertices lie
in \(D\); they would be the forbidden antipodal two-linkage
\(e_0\mid e_3\), which has an explicit \(K_7\)-model.

The terminal-essentiality hypothesis of the bare-web consequence holds.
For if a component \(C\) of \(J-X\), \(|X|\leq3\), contained no
terminal, then \(C\subseteq D\) and

\[
 N_G(C)\subseteq X\cup\{c_2,c_5,z\}.              \tag{6.2}
\]

The right side has order at most six and separates \(C\) from the
opposite shore \(H\), contradicting seven-connectivity.  Hence \(J\)
has a plane embedding with \(c_0,c_1,c_3,c_4\) on one face.

Contract the connected body \(B\) to a vertex \(b\), and delete all
edges not listed below.  Two-connectivity makes \(B\) adjacent to both
\(p,q\).  Equation (5.1) makes it adjacent to both \(c_1,c_4\).  The
resulting terminal-preserving minor contains

\[
\begin{array}{c}
 xp,xq,pq,pb,qb,\\
 xc_0,xc_3,xc_4,\quad pc_3,qc_3,\quad bc_1,bc_4.
\end{array}                                       \tag{6.3}
\]

Add a new vertex \(r\) adjacent to the four terminals.  Cofaciality of
the terminals says that this augmented graph is planar, and contraction
away from the terminals preserves planarity.  But (6.3), together with
the two-edge path \(c_3rc_4\), is a subdivision of \(K_{3,3}\): its
bipartition is

\[
 \{x,b,c_3\}\quad\text{and}\quad\{p,q,c_4\}.       \tag{6.4}
\]

The nine cross-connections are

\[
\begin{array}{lll}
xp,&xq,&xc_4,\\
bp,&bq,&bc_4,\\
c_3p,&c_3q,&c_3rc_4.
\end{array}
\]

Their interiors are disjoint.  This contradicts planarity, proving the
theorem. \(\square\)

The tiny replay `c6_double_thin_web_verify.py` checks both the displayed
subdivision and nonplanarity after adding the cofacial apex.  Unlike the
ear quotient enumeration, the proof of Theorem 6.1 is unbounded in the
order and internal structure of \(B\).

Combining Lemma 2.1, Theorem 4.2, and Theorem 6.1 eliminates every
cycle-type SPQR leaf.  A remaining leaf of the high-owner rope, if any,
must therefore be an R-torso; that is the next portal-order case.

## 7. Canonical SPQR closure

The sound output of the rank-four leaf argument in
`hadwiger_circular_obstruction_frame_theorem.md` is orientation-free:
for a leaf edge of the SPQR tree, **one** of its two displayed interiors
is a singleton degree-two vertex with the exact lock (1.1).  It is not
necessary, and in a three-node R--P--S tree is not correct, to assert
that this singleton is always on the chosen leaf-node side.  The
following observation removes the orientation issue entirely.

### Lemma 7.1 (one-ear forces a P-node)

In a reduced SPQR decomposition of a simple two-connected graph, a
separation \(\{p,q\}\) whose one interior is the singleton \(\{x\}\),
with \(N_D(x)=\{p,q\}\) and \(pq\in E(D)\), is represented by at least
three SPQR nodes.

### Proof

The separation pair has three distinct \(p\)-\(q\) bridges:

1. the path \(pxq\);
2. the real edge \(pq\); and
3. the connected complementary side through \(D-\{p,q,x\}\).

Canonical SPQR reduction represents these three parallel bridges by a
P-node.  Its edge for \(pxq\) is virtual and is adjacent to the S-node
whose skeleton is the triangle \(pxq\); its edge for the complementary
bridge is another virtual edge adjacent to at least one further node;
the edge \(pq\) is real.  Thus the S-node, P-node, and complementary
node are three distinct nodes.  In the convention which retains Q-nodes
for real edges, an additional Q-node may appear, never fewer nodes.
\(\square\)

Now suppose the high-owner shore is not three-connected.  Its SPQR tree
has an edge; choose a leaf edge and apply the rank-four leaf argument.
One side is a singleton \(x\) with shore neighbours \(p,q\).  Lemma 2.1
gives \(pq\in E(D)\), and Lemma 7.1 says that the canonical decomposition
therefore contains an S-node leaf representing \(pxq\), regardless of
which orientation of the originally chosen leaf edge exposed \(x\).
But Theorem 6.1 eliminates every S-node leaf.  This contradiction rules
out every nontrivial SPQR tree.

The three-connected high-owner shore was already eliminated by the
common-face circular obstruction theorem.  Hence the combined
circular-rank and cycle-leaf argument closes the entire
\(C_6\dot\cup K_1\) boundary core: the high-owner shore is neither
three-connected nor capable of a nontrivial SPQR decomposition.
