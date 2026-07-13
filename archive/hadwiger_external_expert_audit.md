# Audit of the external-expert directions

This note audits only the progress-relevant assertions in the external
expert response.  The standing hypothesis is that (G) is a
minor-minimal counterexample at parameter (t); for the degree-seven
claims, (t=7), (d(v)=7), (N=N_G(v)), and (H=G-v).

## 1. Valid coloring witnesses

### 1.1 Independent-set trace

If (S\subseteq N) is a nonempty independent set, contract the connected
set 
\[
        \{v\}\cup S
\]
to (z).  Every ((t-1))-coloring of the resulting proper minor expands
to a proper coloring (c) of (H) such that
\[
 \{x\in N:c(x)=c(z)\}=S.                    \tag{1.1}
\]
Indeed, (S) can be expanded monochromatically because it is independent,
and every vertex of (N-S) is adjacent to (z) through its original edge
to (v).

This lemma is valid in the asserted generality.  One qualification is
important: (1.1) alone does **not** say that the vertices of (N-S) have
distinct colors.  That conclusion also uses neighborhood saturation
(every ((t-1))-coloring of (H) uses all (t-1) colors on (N)) and the
count
\[
        |N-S|=t-2.
\]
Thus it applies in the equality cell
(d(v)=t+s, |S|=s+2), and in particular to every nonedge of a
degree-seven neighborhood.  In the present degree-seven program this
recovers the already audited every-nonedge accessibility lemma; the
arbitrary-(S) formulation is a useful general-(t) extension, not a new
degree-seven reduction.

### 1.2 Edge deletion

For every edge (xy\in E(G)), every ((t-1))-coloring of (G-xy) gives
(x,y) the same color.  Otherwise it colors (G).  Moreover, each of
(x,y) has a neighbor of every other color: if, say, (x) has no
neighbor of color (j\ne c(x)), recoloring (x) with (j) makes the
restored edge (xy) proper and colors (G).

This is valid for a minor-minimal counterexample (which makes every edge
deletion colorable).  It should not be attributed merely to a definition
of contraction-criticality that assumes only colorability after edge
contractions.

## 2. Exterior components and the seven-vertex classification

The following assertions are valid.

1. For every component (C) of (G-N[v]), seven-connectivity gives
   (N_G(C)=N).  Otherwise at most six boundary vertices separate (C)
   from (v).
2. There is at least one exterior component: if not, (V(G)=N[v]) has
   eight vertices, and δ(G)≥7 forces (G=K_8).
3. There are at most two exterior components.  If (C_1,C_2,C_3) exist,
   choose a triangle (r_1r_2r_3) in (G[N]) (it exists because
   α(G[N])≤2) and distinct (x_i\in N-\{r_1,r_2,r_3\}).  The six
   bags
   \[
      \{r_1\},\{r_2\},\{r_3\},
      C_1\cup\{x_1\},C_2\cup\{x_2\},C_3\cup\{x_3\}
   \]
   form an (N)-meeting (K_6)-model.
4. With two exterior components, a (K_4)-model in (G[N]) supported on
   at most five vertices gives an (N)-meeting (K_6): append the two
   bags (C_1\cup\{x_1\}) and (C_2\cup\{x_2\}), using two boundary
   vertices outside the support.

The claimed finite classification was independently checked over all
1,044 unlabeled graphs on seven vertices.  Among the 107 graphs with
α≤2, exactly two have no (K_4)-model supported on at most five
vertices.  They have 11 and 12 edges, respectively, and are the Moser
spindle and its unique relevant one-edge extension.  This validates the
classification as a computer-assisted lemma.  A formal write-up still
needs an archived graph/certificate enumeration or a hand proof.

## 3. The new two-anchor lemma is valid

Suppose (G-N[v]) has two components (C_1,C_2).  Let (ab) and (cd)
be disjoint nonedges of (G[N]), and suppose the remaining vertices
(x,y,z) induce a triangle.

To color (Q_1=G[N\cup C_1]), simultaneously contract
\[
       \{v,a,b\}\quad\hbox{and}\quad C_2\cup\{c,d\}
\]
to adjacent vertices (p,q).  The second set is connected because
(N_G(C_2)=N).  Each of (x,y,z) is adjacent to both (p,q), and the
three form a triangle.  A six-coloring of this proper minor therefore
expands on (Q_1) with the exact boundary partition
\[
       ab\mid cd\mid x\mid y\mid z.          \tag{3.1}
\]
The symmetric contraction colors (Q_2) with the same partition.  Align
the five boundary colors by a permutation, glue the two side colorings,
and color (v) with the sixth color absent from (N).  This contradiction
proves the lemma.

For the numerical Moser labeling
\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\},
\]
the extension (M+13) has disjoint nonedges (25,46), while the remaining
vertices (0,1,3) form a triangle.  Hence the one-edge Moser extension is
indeed eliminated in the two-component case.  This is the one genuine
new local reduction in the expert response: only the pure Moser spindle
remains in this cell.

## 4. Corrections to the proposed pure-Moser (C_5) program

For the pure Moser spindle, (13) is a nonedge and
\[
 U=\{0,2,4,5,6\},\qquad
 \overline{G[U]}=05,52,24,46,60\cong C_5.
\]
The exact-trace coloring and the exterior bichromatic paths are valid.
Every such path has its interior in one exterior component.  If one
component supports **all five** edges of this (C_5), Kriesell--Mohr
property ((*)), applied to the whole unicyclic graph in that side, gives
the required rooted (K_5), and the other component together with (1,3)
is the sixth bag.  Thus full component confinement is a correct
sufficient target.

The expert's proposed spanning-tree shortcut is false.  If one side
supports only four cycle edges, property ((*)) for the resulting spanning
tree supplies those four bag adjacencies.  The direct edges of

\[
       G[U]=\overline{C_5}
\]

supply five more, but the omitted fifth cycle pair is also a nonedge of
(G[U]).  The result is only a rooted

\[
       \overline{C_5}\cup(C_5-e)=K_5-e,
\]

not a rooted (K_5).  Using the fifth path through the other exterior
component may consume the component needed for the sixth bag.  A (4+1)
argument therefore needs a new reserved-connector lemma; it is not a
consequence of Kriesell--Mohr Theorem 5.

Two corrections are required in setting up its finite obstruction.

* A cycle edge may have exterior paths in **both** components.  The correct
  datum is a nonempty support set
  \(σ(e)\subseteq\{1,2\}\), not an arbitrary binary label obtained by
  choosing one path.  An arbitrary choice can hide the fact that all five
  cycle edges are actually supported on one side.
* It is false that, after the monochromatic outcome is
  excluded, both color classes of the edge-colored (C_5) must be
  disconnected.  For example, three consecutive red edges followed by
  two consecutive blue edges give connected edge sets on both of their
  vertex supports.

For one selected path per cycle edge, the binary labelings have four
orbits up to the dihedral group and exchange of the two sides:

\[
 11111,\qquad11112,\qquad11122,\qquad11212.          \tag{4.1}
\]

Only the first is closed by the established argument.  In particular,
the (4+1) pattern `11112` remains open.

For the correct support-set record, write `1`, `2`, or `B` according as
an edge is supported only by the first side, only by the second, or by
both.  A configuration fails full confinement exactly when it has at
least one `1`-only and one `2`-only edge.  There are fourteen such orbits:

\[
\begin{gathered}
11112,11122,1112B,11212,1121B,1122B,112B2,\\
112BB,11B2B,1212B,121BB,12B1B,12BBB,1B2BB.
\end{gathered}                                      \tag{4.2}
\]

Thus the earlier five-pattern list was an artifact of the false
spanning-tree shortcut and must not be used.

Full (C_5) confinement remains narrower than arbitrary nonseparating
rooted (K_5), but it substantially overlaps the already audited
Moser-pseudoforest and support-switch reductions.  The alternative
(4+1) target is legitimate only when stated with an additional
reserved-connector conclusion.  Neither is a proved advance.  The proved
advance is the removal of the one-edge extension.

## 5. Near-(K_7) terminology

The expert's terminology correction is valid: a spanning minor model has
no outside component.  One must use either

* a nonspanning model plus a component of the unused graph, or
* a spanning model and surgery inside a current bag.

Any connected clique-minor model in connected (G) may be made spanning
by absorbing each unused component into a bag to which it attaches.  In a
spanning (K_7^\vee)-model with deficient bag (A), if no
(K_7^-)-minor exists, the two deficient pairs (AB,AC) are genuinely
anticomplete.  Thus all external neighbors of (A) lie in the four
unaffected bags.  They form an (A)-to-(B) separator, so
seven-connectivity gives at least seven such attachment vertices and some
unaffected bag is hit at least twice.  This counting statement is valid;
the proposed label-preserving peel-or-six-separator theorem remains
unproved.
