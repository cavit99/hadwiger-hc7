# The central exact seven-adhesion has only two shores

## 1. Setting

Let (G) be a seven-connected, six-minor-critical,
(K_7)-minor-free graph.  Suppose

\[
 S=\{h,1,2,5,6,y,z\}
\]

is the exact seven-adhesion obtained in the central-edge outcome of
`hadwiger_four_connected_rooted_diamond.md`, and suppose that
(G-S) has three components.  Every component is full to (S).
In the old degree-seven Moser frame,

\[
 N_G(v)=\{h,1,2,3,4,5,6\}.
\]

When not both of the old literals (3,4) belong to (S), write the
three shores as

\[
                         C_v,\quad A,\quad B,
\]

where (C_v) contains (v) and every member of
({3,4}-S).  We use only the following part of the old geometry:

\[
 v3,v4,34\in E(G),\qquad
 vh,v1,v2,v5,v6\in E(G).                         \tag{1.1}
\]

### Theorem 1.1 (three-shore closure)

Under these hypotheses (G) contains a (K_7)-minor.  Consequently
the exact-adhesion outcome of the central-edge funnel has exactly two
shores.

The theorem is independent of the orders and internal structures of
the three shores.

## 2. The forced second triangle

The audited full-shore block theorem, its three-web closure, and the
seven-vertex support classification imply that the boundary of a
three-component seven-cut in a hypothetical (HC_7) counterexample is
the pure Moser spindle.  In the present labels it contains

\[
 h1,h2,12,16,26,56.                              \tag{2.1}
\]

We record the only consequence of that classification used below.

### Lemma 2.1

If a pure Moser spindle on
({h,1,2,5,6,y,z}) contains the six edges in (2.1), then

\[
                         5y,5z,yz\in E(G),        \tag{2.2}
\]

and at least one of (hy,hz) is an edge.

#### Proof

In the standard Moser spindle

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\},
\]

the four triangles are

\[
 012,\quad126,\quad034,\quad345.                 \tag{2.3}
\]

There are exactly two pairs of triangles sharing an edge.  The two
triangles (h12) and (612) in (2.1) must map to one such pair.
After possibly applying the symmetry interchanging the two halves of
the spindle, their distinct tips are (0) and (6), and the edge
from the second tip to (5) is the edge (56).  The three unused
vertices are therefore the other triangle (345).  This proves
(2.2).  The vertex corresponding to the first tip (0) is adjacent
to both vertices of the adjacent triangle (34); under a possible
automorphism interchanging the two tips, one of these two incidences
can instead be the edge from (6).  In every case at least one of
(hy,hz) remains.  Equivalently, the three possible labelled edge
rows beyond (2.1) are

\[
\begin{array}{c|c}
 &\text{additional incidences among }h,6,y,z\\ \hline
1&6y,hz,yz\\
2&6z,hy,yz\\
3&hy,hz,yz,
\end{array}
\]

and every row also contains (5y,5z). \(\square\)

## 3. A near-full piece in the distinguished shore

First observe that neither (y) nor (z) is (v).  Otherwise the
pure-Moser boundary (G[S]) would contain a vertex (v) adjacent
inside (S) to the five vertices (h,1,2,5,6).  The pure Moser
spindle has maximum degree four, a contradiction.

Assume for now that ({3,4}\nsubseteq S), and choose
(ell\in\{3,4}-S).  Let (R) be the component of (C_v-v)
containing (ell).  If both literals remain outside (S), they lie
in this same component through the edge (34).  In either case (R)
is nonempty and connected, and (R\sim v) through (v\ell).  Since (R)
is a component after deleting (v) from one shore and distinct shores
are anticomplete,

\[
                         N_G(R)\subseteq S\cup\{v\}.       \tag{3.1}
\]

The untouched shores (A,B) lie on the far side of this neighbourhood,
so (N_G(R)) is a genuine separator.  Seven-connectivity and
(v\in N(R)) give

\[
                  |N_G(R)\cap S|\ge6.             \tag{3.2}
\]

Thus (R) has at most one boundary defect.  Write that defect as
(d\in S), or put (d=\varnothing) if (R) is full to (S).

It remains to dispose of the exceptional placement
({y,z}={3,4}).  Then (S=N_G(v)), and the three components of
(G-S) are the singleton ({v}) and exactly two components of
(G-N[v]).  The three-shore boundary classification already says that
(G[N(v)]=G[S]) is the pure Moser spindle.  The supported-pair transfer theorem,
Theorem 4.1 of
`hadwiger_moser_supported_pair_transfer_closure.md`, applies exactly
to this situation and produces a (K_7)-minor.  Its hypotheses are:
(d(v)=7), pure-Moser neighbourhood, and exactly two exterior
components; all three have just been verified.  Hence the exceptional
placement is closed, and below we may use the near-full piece (R).

## 4. Explicit branch sets

In every row below, the first three bags are the singleton triangle

\[
                         \{h\},\quad\{1\},\quad\{2\}.      \tag{4.1}
\]

The last four bags are displayed in the table.  Let (qin\{y,z\})
be chosen with (hq\in E(G)), which is possible by Lemma 2.1.

\[
\begin{array}{c|c}
d&\text{last four bags}\\ \hline
\varnothing,y,z
  &\{v\},\ R,\ A\cup\{5\},\ B\cup\{6\}\\[1mm]
h
  &\{v\},\ R\cup\{q\},\ A\cup\{5\},\ B\cup\{6\}\\[1mm]
1\text{ or }2
  &A,\ \{v,5\},\ R\cup\{6\},\ B\cup\{y\}\\[1mm]
5
  &\{v\},\ R,\ A\cup\{6\},\ B\cup\{5,y\}\\[1mm]
6
  &\{v\},\ R,\ A\cup\{5\},\ B\cup\{6,y,z\}.
\end{array}                                                   \tag{4.2}
\]

All seven bags are disjoint and connected.  Connectivity of an
anchored shore bag follows from fullness; connectivity of the
(R)-bags follows from (3.2); and (v5,v6\in E(G)).

We verify pairwise adjacency.  Each of the four bags in every row sees
all three singleton bags in (4.1): full shores do so automatically;
(v) does so by (1.1); and a near-full (R)-bag uses its anchor only
when its unique defect lies in ({h,1,2}).  In the (d=1,2) row,
the bag (R\cup\{6\}) uses the edges (16,26) to repair the missing
one of (1,2), while (R) supplies the (h)-edge.

It remains to check the six pairs among the last four bags.

* In the first two rows, (vR,v5,v6) give the three incidences from
  the (v)-bag.  The (R)-bag sees both (5) and (6), and the two
  anchored opposite shores meet through (56).
* If (d\in\{1,2}), the whole shore (A) sees the three boundary
  anchors (5,6,y).  The other three bags meet through (vR,v6,56),
  and through the (R)-to-(y) contact.
* If (d=5), use (vR,v6,v5), the (R)-contacts to (6,y), and
  the edge (56).
* If (d=6), use (vR,v5,v6), the (R)-contacts to (5,y), and
  again (56).

These are all twenty-one adjacencies.  Hence (4.1)--(4.2) form a
(K_7)-model, proving Theorem 1.1. \(\square\)

## 5. Scope

The proof closes an infinite family: shore orders, cutvertices, portal
multiplicities, and internal treewidth are unrestricted.  It uses the
specific central-cut geometry only to identify the distinguished
shore and the vertex (v).  The sole placement in which the
distinguished near-full piece disappears is the old neighbourhood cut
itself; that placement is closed by the independent supported-pair
transfer theorem.  The critical-edge transition at (56)
is no longer needed in the three-shore branch; it remains concentrated
in the exact two-shore branch.

The dependency-free replay
`degree9_exact7_three_shore_split_verify.py` checks all three labelled
Moser rows, every possible unique defect of (R), connectivity,
disjointness, and all twenty-one bag adjacencies.
