# A pentagon boundary-state lemma for the pure-Moser cell

## 1. Scope

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(d(v)=7\), and suppose

\[
G-N[v]=C_1\mathbin{\dot\cup}C_2,
\qquad G[N]\cong M,
\]

where \(M\) is the pure Moser spindle.  Use the numerical labelling

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Contracting the star \(\{v,1,3\}\) gives a six-colouring of \(G-v\) in
which \(1,3\) are the repeated pair.  The other five boundary vertices
have pairwise distinct colours: any further equality on \(N\) would leave
a sixth colour absent from \(N\), which could be assigned to \(v\).  Thus
this is an exact singleton-state trace.  Put

\[
U=\{0,2,4,5,6\}.
\]

The missing edges on \(U\), in cyclic order, are

\[
e_0=05,\quad e_1=25,\quad e_2=24,\quad e_3=46,\quad e_4=06. \tag{1.1}
\]

For this fixed colouring, say that \(C_s\) **supports** \(e_i=xy\) if
the \(x,y\) bichromatic component in the side
\(G[N\cup C_s]\) contains both roots.  Every \(e_i\) is supported by at
least one side.  Encode its support by \(1,2,B\), where \(B\) means both.

This note proves that five of the fourteen genuinely mixed support orbits
are impossible.  It is a rigorous elimination of whole support families,
not a resolution of the remaining pure-Moser cell.

## 2. The specialized state system

Let \(\mathcal E_s\) be the boundary-state family of side \(s\), as in
`hadwiger_boundary_state_round.md`.  Define

\[
D_i=\{13,e_i\}.
\]

Two of the cycle edges \(e_i,e_j\) are vertex-disjoint exactly when

\[
ij\in E(P):=\{02,03,13,14,24\}. \tag{2.1}
\]

Thus their disjointness graph \(P\) is itself a pentagon.  For
\(ij\in E(P)\), put

\[
T_{ij}=\{13,e_i,e_j\}.
\]

Three elementary facts give a complete finite set of necessary axioms.

### (S1) State exclusivity

No \(D_i\) or \(T_{ij}\) belongs to both \(\mathcal E_1\) and
\(\mathcal E_2\).  Otherwise the two side colourings can be aligned and
glued, and their boundary uses at most five colours, so the colouring
extends to \(v\).

### (S2) Two-anchor coverage

For every \(i\) and every side \(s\), at least one of

\[
D_i,\qquad T_{ij}\ (ij\in E(P)) \tag{2.2}
\]

belongs to \(\mathcal E_s\).  Indeed, apply the two-anchor contraction to
the disjoint nonedges \(13,e_i\).  The only possible third equality pair
is one of the two \(e_j\)'s disjoint from \(e_i\), so the resulting state
is exactly one of (2.2).

### (S3) Unsupported-edge swaps

If the support symbol of \(e_i\) is \(1\), then
\(D_i\in\mathcal E_2\); if it is \(2\), then
\(D_i\in\mathcal E_1\).  This is the usual Kempe swap on the side which
does not support \(e_i\).

Moreover, if \(e_i,e_j\) are disjoint and both are unsupported by side
\(s\), then

\[
T_{ij}\in\mathcal E_s. \tag{2.3}
\]

The two swaps use four distinct unique colours, hence have disjoint vertex
sets and commute.  The repeated pair \(13\) is untouched.

All three facts concern the one fixed exact-trace colouring.  No Kempe
switch involving the repeated colour is being assumed.

## 3. The forbidden support orbits

### Lemma 3.1 (pentagon boundary-state elimination)

Up to a dihedral symmetry of (1.1) and interchange of the two exterior
components, none of the following support words can occur:

\[
\boxed{11112,\quad11122,\quad11212,\quad1121B,\quad1212B.} \tag{3.1}
\]

#### Proof

We repeatedly use the following immediate propagation rule.  If one side
contains \(D_i\) and both triples incident with \(i\) in \(P\), then (S1)
leaves the other side none of the three states in (2.2), contradicting
(S2).

For \(11112\), side 2 is unsupported on \(e_0,e_2,e_3\).  By (S3) it
contains \(D_0,T_{02},T_{03}\), so the propagation rule at \(0\) gives a
contradiction.

The same rule disposes of \(11212\): side 2 is unsupported on
\(e_3,e_0,e_1\), and hence contains \(D_3,T_{03},T_{13}\).  It also
disposes of \(1121B\), using exactly the same three positions.

For \(11122\), (S3) puts

\[
D_0,D_1,D_2,T_{02}\in\mathcal E_2,
\qquad D_3,D_4\in\mathcal E_1. \tag{3.2}
\]

At vertex \(0\) of \(P\), side 1 cannot use \(D_0\) or \(T_{02}\), so
(S2) forces \(T_{03}\in\mathcal E_1\).  Similarly, at vertex \(2\), it
forces \(T_{24}\in\mathcal E_1\).  Now side 2 cannot use those two
triples.  Coverage at \(3\) forces \(T_{13}\in\mathcal E_2\), and
coverage at \(4\) forces \(T_{14}\in\mathcal E_2\).  Finally side 1 can
use none of \(D_1,T_{13},T_{14}\), violating (S2) at \(1\).

For \(1212B\), (S3) gives

\[
D_0,D_2,T_{02}\in\mathcal E_2,
\qquad D_1,D_3,T_{13}\in\mathcal E_1. \tag{3.3}
\]

Coverage of \(0\) on side 1 forces \(T_{03}\in\mathcal E_1\).  But side
2 can then use none of \(D_3,T_{03},T_{13}\), contrary to its coverage at
\(3\).  This proves (3.1). \(\square\)

## 4. Exact residual

A genuinely unconfined word contains both a \(1\) and a \(2\).  The
fourteen orbits under the dihedral group and side interchange were listed
in `hadwiger_moser_c5_audit.md`.  Removing (3.1) leaves exactly

\[
\boxed{
1112B,1122B,112B2,112BB,11B2B,121BB,12B1B,12BBB,1B2BB.
} \tag{4.1}
\]

In particular, every purely binary mixed support pattern is impossible:
the three binary orbits \(11112,11122,11212\) all occur in (3.1).  Hence
every surviving pure-Moser configuration has at least one cycle edge
whose bichromatic connection is supported in **both** exterior components.

The dependency-free verifier `moser_pentagon_state_verify.py` independently
enumerates all ternary words and all assignments of the ten specialized
states to the two disjoint extension families.  It reproduces (3.1) and
(4.1).  The displayed propagation proof, rather than the computation, is
the proof of the lemma.

## 5. Binary supports for all ten exact traces

The preceding argument has a useful formulation which is not tied to the
choice \(13\).

Fix any repeated nonedge \(r\in E(\overline M)\), let \(F_r\) be the
missing-edge graph on the five unique roots, and let \(P_r\) be the graph
whose vertices are the edges of \(F_r\), two being adjacent when they are
vertex-disjoint.  Suppose for the moment that every edge of \(F_r\) is
supported by exactly one exterior component.  Colour the corresponding
vertex of \(P_r\) by that component, and let \(K_r\) be the spanning
subgraph of \(P_r\) consisting of the edges with differently coloured
ends.

### Lemma 5.1 (general binary-support cut criterion)

The specialized axioms (S1)--(S3) admit such a binary support pattern if
and only if every connected component of \(K_r\), including isolated
vertices, contains a cycle.

This statement does not use the Moser graph.  It holds for any
two-exterior-component degree-seven cell, any accessible repeated pair
\(r\), and its missing-edge graph \(F_r\) on the five uniquely coloured
roots.  Here (S2) is simply the two-anchor contraction for \(r,e\), and
the vertices adjacent to \(e\) in \(P_r\) index all possible third pairs.

#### Proof

At a vertex \(e\) labelled \(1\), the side-2 state \(D_e=\{r,e\}\) is
forced.  Every triple corresponding to a same-label edge incident with
\(e\) is forced on side 2 as well.  By exclusivity, none of those states
can cover \(D_e\) on side 1.  Thus two-anchor coverage on side 1 requires
at least one differently labelled incident edge, and its triple state must
be assigned to side 1.  Symmetrically, a vertex labelled \(2\) needs an
incident cut edge whose triple is assigned to side 2.

Orient a cut edge toward the endpoint whose side receives its triple.
The requirement is exactly an orientation of \(K_r\) in which every
vertex has indegree at least one.  A finite graph has such an orientation
if and only if every component contains a cycle: necessity follows by
counting edges, while sufficiency follows by orienting one cycle in each
component cyclically and all trees hanging from it away from the cycle.
Assigning the cut triples according to this orientation, and assigning
the forced vertex and same-label-edge states as above, also proves the
converse at the level of (S1)--(S3). \(\square\)

Since every cut graph is bipartite, Lemma 5.1 has the following convenient
general consequence: if \(P_r\) has no even cycle, then a mixed binary
support pattern is impossible.  Thus either one side confines all of
\(F_r\), or at least one edge of \(F_r\) is supported on both sides.  This
criterion can be applied to other degree-seven neighbourhood types without
repeating the pentagon propagation.

For the pure Moser spindle the ten cases are as follows:

\[
\begin{array}{c|c}
r & P_r\\ \hline
05,06 & C_6\\
13,14,23,24 & C_5\\
15,25,36,46 & P_5.
\end{array} \tag{5.1}
\]

If \(P_r=C_5\), a cut subgraph is bipartite and therefore cannot contain
the whole odd cycle; every such cut subgraph is a forest.  If
\(P_r=P_5\), it is a forest from the outset.  Lemma 5.1 consequently gives:

### Corollary 5.2 (eight forced bi-support traces)

For each

\[
r\in\{13,14,15,23,24,25,36,46\}, \tag{5.2}
\]

either one exterior component supports every edge of \(F_r\), which
already gives the confined rooted \(K_5\)-model and a \(K_7\)-minor, or
some edge of \(F_r\) is supported by **both** exterior components.

For \(r=05\) or \(06\), \(P_r=C_6\).  The only mixed binary patterns not
excluded by these axioms are the two alternating colourings of this
\(C_6\) (one up to interchange of the sides).  Indeed, a cut subgraph of
\(C_6\) contains a cycle only when it is the whole cycle.

The table (5.1) is obtained by directly listing the missing edges disjoint
from \(r\); it is also checked in the verifier described below.

## 6. Remaining gap

The new conclusion is a useful geometric input: a residual mixed
configuration necessarily contains a two-sided connection for at least one
edge of the rooted \(C_5\).  What is still missing is a bridge/linkage
argument using that two-sided path to either

1. confine all five certificate edges to one exterior component; or
2. repair the missing fifth bag adjacency while reserving a connected
   sixth branch set.

Abstract boundary states alone do not yet supply that rerouting.  The
remaining geometric target can now assume a two-sided bichromatic
connection in each of the eight exact traces (5.2), rather than only in
the single \(13\)-trace.
