# The singleton-shore lock in the \(C_6\dot\cup K_1\) boundary

## 1. Exact boundary states

Use the boundary notation of hadwiger_c6_two_piece_locks.md.  Suppose
one full shore is the singleton \(D_1=\{h\}\), and write \(D=D_2\) for
the opposite shore.

### Lemma 1.1

No six-colouring of \(G[S\cup D]\) induces a boundary partition with at
most five blocks.

### Proof

The singleton \(h\) has no neighbours outside \(S\) and is adjacent to
every vertex of \(S\).  If a side colouring used at most five colours on
\(S\), give \(h\) a sixth colour absent from \(S\).  This would
six-colour \(G\).

### Lemma 1.2 (all six exact one-edge states)

For every edge \(e=ab\) of the missing cycle \(F=C_6\), the graph
\(G[S\cup D]\) has a six-colouring whose exact boundary state is

\[
 \{a,b\}\mid\{s\}\quad(s\in S-\{a,b\}).              \tag{1.1}
\]

### Proof

Contract the connected set \(\{h,a,b\}\) to a vertex and colour the
resulting proper minor with six colours.  Expanding \(a,b\) with the
colour of the contracted image gives a side colouring in which
\(\{a,b\}\) is an exact block: every other boundary vertex was adjacent
to \(h\), hence to the contracted image.

If any second boundary equality occurred, the state would have at most
five blocks, contrary to Lemma 1.1.  Thus all other boundary vertices
are singleton blocks and (1.1) follows.

## 2. Forced Kempe paths

Fix \(e=ab\), a colouring from Lemma 1.2, and put
\(U=S-\{a,b\}\).  The missing-edge graph \(F[U]\) is \(P_4\dot\cup K_1\),
where the isolated vertex is the universal boundary vertex \(c\).

### Lemma 2.1

For every edge \(pq\in E(F[U])\), the \(p\)-\(q\) bichromatic component
contains both \(p\) and \(q\).  Consequently it contains a \(p\)-\(q\)
path whose internal vertices lie in \(D\).

### Proof

If \(p,q\) belonged to different bichromatic components, interchange
their two colours on the component containing \(p\).  The colouring
would remain proper.  On the boundary, \(p\) would now have the colour
of \(q\), while the original exact block \(\{a,b\}\) would be unchanged.
Thus at most five colours would occur on \(S\), contrary to Lemma 1.1.

No boundary vertex other than \(p,q\) has either of their colours in
the exact state (1.1).  Hence a shortest path in their common
bichromatic component has all internal vertices in \(D\).

Paths belonging to vertex-disjoint edges of \(F[U]\) are automatically
vertex-disjoint, because their colour pairs are disjoint.

### Corollary 2.2

The five vertices of \(U\) admit a rooted \(K_5\)-model in
\(G[D\cup U]\).

### Proof

The three forced connections in Lemma 2.1 realize the path \(P_4\).
Every connected graph with at most one cycle has the Kempe
rooted-minor property (Kriesell--Mohr, Theorem 5); in the tree case this
also follows directly by inductively absorbing the three paths.  The
complementary pairs of roots are already boundary edges, so the
resulting five rooted bags form a rooted \(K_5\)-model.

### Lemma 2.3 (edge-deletion rooted path)

For every rim vertex \(b\), there is a proper six-colouring of
\(G-hb\) with the following structure:

1. \(h,b\) have one colour \(\alpha\);
2. the unique repeated boundary block is a missing edge
   \(e\in E(F)\) not incident with \(b\);
3. for at least one missing-cycle neighbour \(d\) of \(b\), the vertex
   \(d\) is singleton-coloured on \(S\), and the \(\alpha,c(d)\) Kempe
   component contains a \(b\)-\(d\) path whose internal vertices lie
   in \(D\).

### Proof

Colour the proper minor \(G-hb\).  The ends \(h,b\) must have one colour,
or the deleted edge could be restored.  No other boundary vertex has
that colour because it remains adjacent to \(h\).  If at most five
colours occurred on \(S\), recolour \(h\) with a sixth colour absent
from \(S\), again restoring \(hb\).  Hence exactly six colours occur on
the seven boundary vertices.  Their unique repeated block is a nonedge
of \(G[S]\), hence an edge \(e\) of \(F\), and it does not contain \(b\).

The two neighbours of \(b\) on \(F=C_6\) are nonadjacent in \(F\), so
the edge \(e\) contains at most one of them.  Choose the other one,
called \(d\); its boundary colour is a singleton.

Let \(K\) be the bichromatic component containing \(b\), using colours
\(\alpha,c(d)\).  The vertices \(h,d\) lie in one such component through
the edge \(hd\).  If \(d\notin K\), interchange the two colours on
\(K\).  Then \(b\) no longer has colour \(\alpha\), while \(h\) retains
it, so the deleted edge \(hb\) can be restored and \(G\) is
six-coloured.  Therefore \(b,d\in K\).

In \(G-hb\), the vertices \(b,d\) are the only boundary vertices of
these two colours, and \(bd\) is a missing boundary edge.  Moreover
\(h\) has no neighbour in \(D\).  A shortest \(b\)-\(d\) path in \(K\)
therefore has every internal vertex in \(D\).

## 3. Exact remaining reserved-contact problem

Let \(d\) be the other neighbour of \(b\) on the missing cycle, so
\(d\in U\).  The singleton \(b\) is adjacent in the boundary to every
root of \(U\) except \(d\).  Therefore Corollary 2.2 yields a \(K_7\)
model as soon as the bag rooted at \(d\) can be chosen to contain a
neighbour of \(b\): use the five rooted bags, the singleton bag
\(\{b\}\), and the connected bag \(\{h,a\}\).  The last bag sees every
rooted bag through \(h\), and \(b\) sees the \(d\)-bag by the reserved
contact and every other bag through boundary edges or \(bh\).

Thus the singleton-shore case is reduced to the following finite-label
strengthening of a tree-rooted model, not to arbitrary rooted \(K_5\):

> For some missing edge \(ab\), the forced \(P_4\)-packaging on
> \(U=S-\{a,b\}\) can be chosen so that the bag at the other missing
> neighbour \(d\) of \(b\) meets \(N_D(b)\).

Failure for every orientation of every cycle edge is a sixfold
reserved-contact lock.  The full-shore condition guarantees
\(N_D(b)\ne\varnothing\), while the minimum-degree inequality gives
\(|N_D(b)|\ge2\) because \(b\) has four boundary neighbours and the
singleton shore contributes only one.  This two-portal multiplicity is
the additional input available for the reserved-contact rerouting.

Lemma 2.3 supplies more than abstract Kempe connectivity: one edge of
the induced \(P_4\) has a path explicitly rooted through a shore
neighbour of its boundary endpoint.  Since that edge is itself part of
the \(P_4\) used in Corollary 2.2, one still needs a label-preserving
version of the constructive tree packaging; the path is not a seventh
branch bag by itself.
