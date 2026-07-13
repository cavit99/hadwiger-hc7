# Kempe certificates versus removable paths in the degree-seven cell

## 0. Outcome

The colour-preserving removable-path target cannot be proved from the
local degree-seven package alone, even when the five-root missing-edge
graph is a **single edge**.  Section 2 gives an explicit graph with

\[
\chi(G)=7,\quad \delta(G)=\kappa(G)=7,\quad
\kappa(G-v)=7,\quad d(v)=7,\quad \alpha(G[N(v)])=2,
\]

such that every nonedge of \(G[N(v)]\) is accessible by its genuine
triple-contraction colouring, every six-colouring of \(G-v\) saturates
\(N(v)\), and every accessible pair has a one-edge forest \(F\).
Nevertheless, no accessible colouring has a colour-preserving removable
path.

The example necessarily fails two global CE hypotheses: it already has a
\(K_7\)-minor, and it is not edge-critical.  Thus CP--RP must genuinely
use minor exclusion or proper-minor criticality.  Connectivity, saturation,
full accessibility, and the constructive pseudoforest proof do not suffice.

## 1. Audit of the constructive pseudoforest proof

Kriesell--Mohr prove property \((*)\) for a cycle by taking a minimal
counterexample and contracting three-vertex segments of two-coloured
paths.  They obtain unicyclic graphs with attached trees by repeatedly
using their pending-edge lemma, which performs the same kind of
contraction and later expands the bag containing the contracted vertex.

Those operations preserve the routing graph.  They do not preserve
avoidance of a separately prescribed path: expansion may force a bag to
absorb precisely the vertices of that path.  There is therefore no latent
invariance saying that a certificate can be chosen in \(H-P\).  The next
construction shows this is a real obstruction, not just a gap in that
proof.

## 2. A fully accessible one-edge-forest obstruction

Let

\[
C=p\,a\,q\,b\,c\,r\,d\,e\,p
\]

be an eight-cycle.  Put \(J=\overline C\), add two adjacent vertices
\(h_1,h_2\) complete to \(J\), and call the resulting graph

\[
H=K_2\vee\overline{C_8}.
\]

Set

\[
N=\{h_1,h_2,a,b,c,d,e\},                                   \tag{2.1}
\]

and obtain \(G\) from \(H\) by adding \(v\) adjacent precisely to \(N\).
Thus \(G-N[v]=\{p,q,r\}\).  The nonedges among the cycle vertices are

\[
pa,aq,qb,bc,cr,rd,de,ep.                                   \tag{2.2}
\]

### Lemma 2.1 (local D7 data)

\[
\chi(H)=6,\quad \chi(G)=7,\quad
\kappa(H)=7,\quad\kappa(G)=7,\quad\delta(G)=7,              \tag{2.3}
\]

and

\[
\overline{G[N]}=\{bc,de\},\qquad\alpha(G[N])=2.             \tag{2.4}
\]

#### Proof

Independent pairs of \(J=\overline{C_8}\) are precisely edges of \(C\).
A four-colouring of \(J\) is therefore a perfect matching of \(C\), and
there are exactly two:

\[
M_0=\{pa,qb,cr,de\},\qquad
M_1=\{ep,aq,bc,rd\}.                                       \tag{2.5}
\]

Thus \(\chi(J)=4\) and \(\chi(H)=6\).

The graph \(\overline{C_8}\) is five-connected.  Its minimum degree is
five.  If deletion of at most four vertices disconnected it, all pairs
between two remaining components would be cycle edges.  A singleton
component has at most two such neighbours; two components of size at
least two would force a \(K_{2,2}\) in the cycle.  Both contradict the
fact that at least four vertices remain.  Hence joining \(K_2\) gives
\(\kappa(H)=7\).

Delete at most six vertices from \(G\).  If \(v\) remains, then \(H\)
minus the deleted vertices is connected and at least one member of \(N\)
remains to join it to \(v\).  If \(v\) is deleted, at most five vertices
are deleted from \(H\).  Hence \(\kappa(G)=7\).  The cycle vertices have
degree seven in \(H\), \(p,q,r\) do not see \(v\), and \(d_G(v)=7\);
thus \(\delta(G)=7\).

Only \(bc,de\) from (2.2) lie wholly in \(N\), proving (2.4).  In each
matching in (2.5), exactly one pair lies wholly in \(N\), while every
other pair meets \(N\); \(h_1,h_2\) are singleton colour classes.
Every six-colouring of \(H\) therefore uses all six colours on \(N\).
It cannot be extended to \(v\), so \(\chi(G)=7\). \(\square\)

### Lemma 2.2 (full accessibility)

Both edges of \(\overline{G[N]}\) are accessible repeated pairs:
\(M_0\) repeats \(de\), and \(M_1\) repeats \(bc\).  If \(J_{xy}\) is
obtained by contracting \(\{v,x,y\}\), for \(xy\in\{bc,de\}\), then

\[
\chi(J_{xy})=6.                                            \tag{2.6}
\]

#### Proof

The corresponding colouring in (2.5) descends to the contraction, with
the contracted vertex receiving the common colour of \(x,y\).  If the
contraction were five-colourable, expand its vertex onto the nonadjacent
pair \(x,y\) and give \(v\) a fresh sixth colour.  That would six-colour
\(G\), contrary to Lemma 2.1. \(\square\)

This strengthens the fixed-colouring obstruction in Section 7 of
hadwiger_nonseparating_k5_round.md: here the entire nonedge graph is
realised by genuine triple contractions.

### Lemma 2.3 (CP--RP fails for both colourings)

For both accessible colourings, \(F\) is a one-edge forest and no
colour-preserving removable path exists.

#### Proof

Under \(M_0\), the repeated pair is \(d,e\), and

\[
U=\{h_1,h_2,a,b,c\},\qquad F=\{bc\}.                       \tag{2.7}
\]

The colour classes of \(b,c\) are \(\{q,b\}\), \(\{c,r\}\).
Their two-coloured graph has the unique \(b\)-\(c\) path

\[
b-r-q-c.                                                    \tag{2.8}
\]

Now \(H-U=H[\{p,q,r,d,e\}]\).  Deleting \(\{q,r\}\) separates
\(d\) from \(e\), because on \(\{p,d,e\}\) the only edge is \(pd\).
Every \(d\)-\(e\) path avoiding \(U\) therefore uses \(q\) or \(r\),
and deletion of either destroys (2.8).

Under \(M_1\), the repeated pair is \(b,c\), and

\[
U=\{h_1,h_2,a,d,e\},\qquad F=\{de\}.                       \tag{2.9}
\]

The two relevant colour classes are \(\{r,d\}\), \(\{e,p\}\), with
unique \(d\)-\(e\) path

\[
d-p-r-e.                                                    \tag{2.10}
\]

Here \(H-U=H[\{p,q,r,b,c\}]\).  Deleting \(\{p,r\}\) separates
\(b\) from \(c\), since on \(\{q,b,c\}\) the only edge is \(qc\).
Every \(b\)-\(c\) path destroys (2.10). \(\square\)

Du--Li--Xie--Yu feasibility is not enough here.  In the first colouring,
\(d-q-e\) avoids \(U\), and \(U\) remains connected after its deletion,
but the prescribed two-coloured connection (2.8) is destroyed.

## 3. The missing global hypotheses

### Lemma 3.1 (explicit \(K_7\)-minor)

The graph \(H\) already has a \(K_7\)-minor.

#### Proof

Inside \(J\), the five bags

\[
\{p\},\quad\{q\},\quad\{c\},\quad\{d\},\quad\{a,r\}         \tag{3.1}
\]

form a \(K_5\)-model.  The first four vertices are pairwise
nonconsecutive on \(C\).  The last bag is connected; use \(r\) for its
adjacency to \(p,q\), and \(a\) for its adjacency to \(c,d\).  Add the
singleton universal bags \(\{h_1\},\{h_2\}\). \(\square\)

### Lemma 3.2 (failure of edge-criticality)

The proper subgraph \(G-pb\) remains seven-chromatic.

#### Proof

Deleting \(pb\) from \(H\) adds the chord \(pb\) to its nonedge graph.
The graph \(R=C_8+pb\) is triangle-free, so every independent set of
\(\overline R\) has order at most two.  Its chromatic number remains four:
the lower bound is \(8/2\), and (2.5) gives the upper bound.  Hence every
four-colouring partitions the cycle vertices into four edges of \(R\).

The exterior set is \(\{p,q,r\}\), and \(R[\{p,q,r\}]\) is edgeless.
Every colour pair therefore meets \(N\).  The two singleton colours on
\(h_1,h_2\) also meet \(N\).  Every six-colouring of \(H-pb\) saturates
\(N\), so none extends to \(v\).  Thus \(\chi(G-pb)=7\). \(\square\)

The example is excluded precisely by two global inputs not used in the
local CP--RP proposal:

\[
\eta(G)=6,\qquad
\text{every proper minor of }G\text{ is six-colourable}.   \tag{3.2}
\]

In particular, an exchange using only the two triple-contraction
colourings cannot work; those colourings exist here exactly as in the
putative counterexample.

## 4. A weaker exact reduction for a one-edge forest

CP--RP is stronger than necessary.  The following uncoloured linkage
already gives the minor.

### Lemma 4.1 (two-pair linkage suffices)

In the genuine D7 setup, suppose an accessible colouring has repeated
pair \(x,y\), unique roots

\[
U=\{r,s,t_1,t_2,t_3\},\qquad
\overline{H[U]}=\{rs\}.
\]

Put \(L=H-\{t_1,t_2,t_3\}\).  If \(L\) has vertex-disjoint paths
joining \(x\) to \(y\) and \(r\) to \(s\), then \(G\) has a
\(K_7\)-minor.

#### Proof

Let \(P\) be the \(x\)-\(y\) path and \(R\) the \(r\)-\(s\) path.
Split \(R\) at an edge into adjacent connected bags \(B_r,B_s\)
containing \(r,s\).  Use \(V(P)\) as a third bag.  It is adjacent to
both: at least one of \(xr,yr\), and at least one of \(xs,ys\), exists
because \(\alpha(G[N(v)])=2\).

The singleton bags \(\{t_1\},\{t_2\},\{t_3\}\) form a clique.  As \(rs\)
is the only missing edge in \(H[U]\), each is adjacent to \(B_r,B_s\);
each is also adjacent to \(V(P)\) through \(x\) or \(y\).  These six
bags form an \(N(v)\)-meeting \(K_6\)-model in \(H\).  Add \(\{v\}\).
\(\square\)

Because \(H\) is six-connected, \(L\) is three-connected.  Thus a
\(K_7\)-minor-free graph in this one-edge cell must be a genuine
two-disjoint-paths obstruction for \((x,y),(r,s)\) in a three-connected
graph.  This is sharper than CP--RP: the second path need not be
bichromatic.  The next branch is therefore

\[
\boxed{\text{two-pair linkage}}
\quad\text{or}\quad
\boxed{\text{two-paths web obstruction plus edge-critical colouring}}.
\tag{4.1}
\]

## 5. Exact remaining target

The pseudoforest cell is not closed.  The concrete next statement is:

> **Edge-critical web elimination.**  In Lemma 4.1, the
> two-disjoint-paths web obstruction in
> \(H-\{t_1,t_2,t_3\}\) is incompatible with the six-colourings of every
> proper edge deletion of the seven-contraction-critical graph \(G\),
> unless \(G\) already has a \(K_7\)-minor.

This target explicitly uses the hypothesis absent from Section 2 and
would eliminate the smallest nontrivial forest cell without requiring a
colour-preserving removable path.

## References

* M. Kriesell and S. Mohr, *Kempe Chains and Rooted Minors*, Lemmas 1--2
  and Theorem 5, arXiv:1911.09998.
* X. Du, Y. Li, S. Xie and X. Yu, *Linkages and Removable Paths Avoiding
  Vertices*, J. Combin. Theory Ser. B 169 (2024), 211--232.

