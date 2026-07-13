# A circular obstruction theorem for complementary frames

> **Scope correction.** The common-face circular theorem in Sections
> 1--3 remains valid. The claim in Section 6 that one four-terminal web
> forces a rank-one side at every SPQR leaf is false: reflecting a leaf
> can destroy portal cofaciality. Do not cite Theorem 6.1 or Corollary
> 6.2. See `hadwiger_c6_closure_spotcheck_counteraudit.md`.

## 1. Label-free pattern

Let \(U\) be a six-element set and let \(\mathcal A,\mathcal B\) be two
perfect matchings of \(U\) whose union is one alternating six-cycle.
For \(a\in\mathcal A\), let \(\tau(a)\in\mathcal B\) be the unique edge
of \(\mathcal B\) disjoint from \(a\). Thus
\(\tau:\mathcal A\to\mathcal B\) is a bijection.

Let \(D\) be a plane graph with a facial cycle \(\Omega\), and assign a
nonempty portal set

\[
 P_u\subseteq V(\Omega)\qquad(u\in U).
\]

A **connector** for \(uv\) is a connected subgraph of \(D\) meeting
both \(P_u\) and \(P_v\).  A two-edge set
\(F\in\binom{\mathcal A}2\) is **packable** if its two edges have
vertex-disjoint connectors. Define packability in \(\mathcal B\) in the
same way.  The system is **cross-free** if no pair
\(a,\tau(a)\) has vertex-disjoint connectors.

This definition mentions neither a labelled \(C_6\) nor a clique-minor
quotient.  Its finite obstruction graph has six demand vertices:
\({\cal A}\) and \({\cal B}\) induce two triangles of possible frames,
and the three forbidden pairs form the perfect matching \(a\tau(a)\).

### Theorem 1.1 (complementary-frame rank one)

Assume that the six portal sets have a system of distinct
representatives on \(\Omega\), and that the portal system is cross-free.
Then exactly one set \(F\in\binom{\mathcal A}2\) has both \(F\) and
\(\tau(F)\) packable.

In particular, a common-face society cannot realize two different
complementary frame pairs.

The word *exactly* can be weakened to *at most* if \(\Omega\) is only a
topological boundary and its boundary arcs are not required to be edges
of the society.  In the facial-cycle setting the boundary arcs prove
existence of one pair.

## 2. The exact disk rule

Take an edge \(uv\in\mathcal A\), write
\(\tau(uv)=xy\), and select

\[
 p\in P_u,\quad q\in P_v,\quad r\in P_x,\quad s\in P_y.
\]

If \(\{p,q\}\cap\{r,s\}=\varnothing\), cross-freeness forces

\[
 p\ne q,\qquad r\ne s,
 \qquad p,q,r,s\text{ alternate on }\Omega.        \tag{2.1}
\]

For if all four points are distinct and do not alternate, two disjoint
facial arcs join the prescribed pairs.  If \(p=q=w\), use the singleton
\(\{w\}\) and an \(r\)-\(s\) facial arc avoiding \(w\); if \(r=s\),
use the singleton \(\{r\}\).  These are again disjoint connectors.
This proves (2.1), including all portal coincidences.

Conversely, if two connected subgraphs are disjoint and join two
prescribed portal pairs, any selected attachments on \(\Omega\) are
either collapsed within one pair or are four nonalternating points.
Four alternating attachments would force the two connected subgraphs
to cross in the disk.  Notice that no representatives chosen for
different connectors have been identified.

## 3. Proof of Theorem 1.1

Choose distinct representatives \(b_u\in P_u\).  Apply (2.1) to the
three pairs \(a,\tau(a)\).  To display the finite order calculation,
temporarily put

\[
 U=\{x_0,y_0,x_1,y_1,x_2,y_2\},\qquad
 A_i=x_iy_i,\qquad B_i=y_ix_{i+1}
\]

with subscripts modulo three.  Then
\(\mathcal A=\{A_0,A_1,A_2\}\),
\(\mathcal B=\{B_0,B_1,B_2\}\), and
\(\tau(A_i)=B_{i+1}\).

Number

\[
 x_0,y_0,x_1,y_1,x_2,y_2
       \quad\text{by}\quad 0,1,2,3,4,5.
\]

Fixing \(b_{x_0}\) first, the three required alternations leave exactly
the following six oriented cyclic orders:

\[
\begin{array}{c|c}
\text{order}&\text{two-edge set in }\mathcal A
                 \text{ having a facial packing together with its image}\
\hline
024153&\{A_1,A_2\}\\
035142&\{A_1,A_2\}\\
025314&\{A_0,A_1\}\\
041352&\{A_0,A_1\}\\
031524&\{A_0,A_2\}\\
042513&\{A_0,A_2\}
\end{array}                                         \tag{3.1}
\]

This is a \(5!=120\)-order check: place the other five representatives
successively and test the three alternations in (2.1).  The first part
of `c6_circular_witness_degenerate_smt.py` independently derives the
same list rather than trusting it as input.  In each row, disjoint
facial arcs pack the displayed pair and its \(\tau\)-image.  Thus at
least one complementary frame is packable.

It remains to exclude a second one.  The automorphism group of the two
matchings, together with reversal of \(\Omega\), is transitive on the
six rows of (3.1).  The reflection fixing the first row interchanges its
two alternative second frames.  It therefore suffices to use the order

\[
024153                                                   \tag{3.2}
\]

and ask for disjoint connectors for

\[
 A_0,A_1\qquad\text{and}\qquad
 \tau(A_0)=B_1,\ \tau(A_1)=B_2.                    \tag{3.3}
\]

Choose two portal attachments for each of these four connectors.  There
are six SDR occurrences and eight connector occurrences, hence at most
fourteen distinct points of \(\Omega\).  Replace the physical points by
their cyclic ranks.  For each of the four connectors its two
occurrences may coincide; connectors belonging to the same packing are
cross-disjoint.  If neither connector of a packing collapses, their four
attachments are nonalternating.  Finally impose (2.1) on every selected
occurrence choice for each of the three forbidden pairs.

These necessary conditions have no circular weak order.  For
transparency, splitting according to whether the connectors

\[
 B_2,\ B_1,\ A_1,\ A_0
\]

are noncollapsed (N) or collapsed (C) gives the complete table

\[
\begin{array}{cccc|c@{\qquad}cccc|c}
N&N&N&N&0&N&N&N&C&0\\
N&N&C&N&0&N&N&C&C&0\\
N&C&N&N&0&N&C&N&C&0\\
N&C&C&N&0&N&C&C&C&0\\
C&N&N&N&0&C&N&N&C&0\\
C&N&C&N&0&C&N&C&C&0\\
C&C&N&N&0&C&C&N&C&0\\
C&C&C&N&0&C&C&C&C&0
\end{array}                                         \tag{3.4}
\]

where the final entry is the number of feasible weak orders.  The
sixteen rows are generated and checked by
`c6_circular_witness_collapse_table.py`; the full twelve unnormalised
instances are checked by `c6_circular_witness_degenerate_smt.py`.
Both encodings allow coincidences between different witnesses and with
the SDR, and impose only genuine disjointness.  Thus a real second
packing would yield one of the weak orders counted in (3.4), a
contradiction.  The displayed frame in (3.1) is consequently unique.
\(\square\)

## 4. The invariant and an SPQR leaf flip

For a valid common-face SDR order \(\omega\), define

\[
 \sigma(\omega)=F\in\binom{{\cal A}}2
\]

to be the unique complementary frame in (3.1).  This is the
**circular frame index**.  It is independent of orientation of
\(\Omega\).

Consider a leaf of an SPQR decomposition attached through a separation
pair \(\{p,q\}\).  If all six selected representatives lie on the
current outer facial cycle and \(k\) of them lie internally on the
leaf's exposed \(p\)-\(q\) arc, flipping the leaf reverses one
contiguous block of length \(k\) in their cyclic order.

### Lemma 4.1 (leaf-flip rigidity)

If both the original and flipped orders satisfy the three forbidden
alternations, then

\[
 k\in\{0,1,5,6\},
 \qquad\text{and}\qquad
 \sigma(\omega')=\sigma(\omega).                  \tag{4.1}
\]

In particular, a leaf containing two, three, or four internal SDR
representatives cannot be flipped while retaining a common-face
realization of all three cross-free demands.

### Proof

Use the six rows in (3.1).  Reverse every cyclic interval of lengths
two, three, or four.  None of the resulting orders is another row of
(3.1).  Reversing zero or one entry changes nothing.  Reversing five or
six entries is, up to a cyclic shift, reversal of the whole circle; it
maps the two rows with each fixed value of \(\sigma\) to each other and
does not change \(\sigma\).  The dependency-free enumeration is
`c6_spqr_leaf_flip_probe.py`.  \(\square\)

This is a precise gain over a raw two-cut case list.  In a
two-connected common-face society, every SPQR leaf flip preserves the
frame index; a flip capable of changing it must expose a separation pair
with a nontrivial \(2\)-to-\(4\) distribution of the six roots.  Such a
distribution cannot remain common-face and cross-free on both sides.
It therefore localizes the failure of simultaneous web alignment at
that two-cut, where the exact two-piece defect atlas applies.

There is an important scope qualification.  The three separate
four-terminal web embeddings of an arbitrary two-connected shore have
not yet been proved to share one facial cycle.  Lemma 4.1 applies once a
common-face SPQR state exists; it does not by itself manufacture that
state.  The remaining synchronization target is therefore:

> At the first SPQR edge where two of the three web states disagree,
> either their leaf side contains two to four portal classes and the
> exact defect rows give a positive minor, or the flip is trivial on the
> circular frame index and can be propagated past the edge.

This converts the unbounded geometry into a three-state transfer
invariant plus a local two-cut obstruction.

## 5. From leaf flips to a rope path

The preceding finite transition combines cleanly with a standard
transversal-matroid fact.  Let \(M_P\) be the transversal matroid on
\(V(\Omega)\) defined by the six portal classes: an independent set is
the image of a partial system of distinct representatives.  It has rank
six, and its bases are exactly the six-vertex images of full SDRs.

For any vertex set \(X\subseteq V(\Omega)\), the values

\[
 |B\cap X|\qquad(B\text{ a basis of }M_P)           \tag{5.1}
\]

form an integer interval.  Indeed, basis exchange changes the
intersection size one step at a time; equivalently the minimum and
maximum are

\[
 6-r(V(\Omega)-X),qquad r(X).                       \tag{5.2}
\]

### Lemma 5.1 (rank-one leaf)

In the setting of Lemma 4.1, let \(X\) be the internal vertices on the
exposed arc of a genuine SPQR leaf.  Then

\[
 r(X)\le1\qquad\text{or}\qquad
 r(V(\Omega)-X)\le1.                               \tag{5.3}
\]

### Proof

Lemma 4.1 applies to every SDR, not just the initially selected one.
Thus (5.1) contains none of \(2,3,4\).  Since (5.1) is an interval, it
is contained in \(\{0,1\}\) or in \(\{5,6\}\).  Formula (5.2) gives
(5.3). \(\square\)

Now restore the ambient two-shore setting and seven-connectivity.  A
proper two-separation of the shore has separator \(\{p,q\}\), with
nonempty anticomplete interiors \(L,R\).  Apply Lemma 5.1 to a leaf
side.  After possibly exchanging the sides, the portal-incidence graph
between the six boundary labels and one interior, say \(L\), has
matching number at most one.

By the size-one case of Konig's theorem, all of its incidences are
covered either by one boundary label or by one shore vertex.

* In the first case,
  \(N_G(L)\subseteq\{p,q,z,c\}\) for one boundary vertex \(c\), a cut
  of order at most four.
* In the second case, let \(x\in L\) cover all boundary incidences.  If
  \(L-\{x\}\ne\varnothing\), a component of it has all its neighbours
  in \(\{p,q,x,z\}\), again a cut of order at most four.

The opposite shore lies beyond either cut, so seven-connectivity rules
out both alternatives.  Therefore \(L=\{x\}\).  Two-connectivity makes
\(p,q\) the two shore neighbours of \(x\).  The exact degree-two portal
lock then supplies a unique boundary label \(v_x\) such that

\[
 S-N_S(x)=N_{C}(v_x),\qquad
 S-N_S(D-x)=\{v_x\},                               \tag{5.4}
\]

where \(C\) is the alternating six-cycle underlying
\({\cal A}\cup{\cal B}\).

### Corollary 5.2 (locked sides cannot branch)

For every leaf edge of a residual common-face SPQR decomposition, at
least one of its two interiors is a single degree-two shore vertex with
the exact lock (5.4).  There are at most two distinct vertices obtained
in this way.

### Proof

It remains to prove the second assertion.  If \(x,y\) are distinct
degree-two locked vertices with unique labels \(v_x,v_y\), then
\(y\in D-x\) is not a portal of \(v_x\), while (5.4) says that the only
labels missed by \(y\) are the two cycle-neighbours of \(v_y\).
Hence \(v_x\in N_C(v_y)\).  Symmetrically
\(v_y\in N_C(v_x)\).  Thus the unique labels of any two leaves are
adjacent on \(C\).  Three leaves would give a triangle in a six-cycle,
which is impossible.  Hence there are at most two. \(\square\)

This is the reusable structural output of the flip analysis:

\[
 \text{incompatible circular states}
 \Longrightarrow
 \text{rank-one two-cut}
 \Longrightarrow
 \text{an exact locked side}.                      \tag{5.5}
\]

The orientation issue at a leaf edge is real: the low-rank singleton
may lie on the complement side. Section 6 retains only the
orientation-free conclusion and shows that any such singleton exposes
a canonical S-node leaf. The former SPQR-path and two-node analysis is
retracted.

## 6. Four terminals already force the rank-one leaf

The common-face qualification in Lemma 5.1 is unnecessary for the leaf
conclusion in the Hadwiger shore.  One of the three four-terminal web
embeddings suffices.

Let \(Q_0,Q_1,Q_2,Q_3\) be four full portal sets on one facial cycle,
with no linkage joining the prescribed pair \(Q_0,Q_2\) disjointly
from the prescribed pair \(Q_1,Q_3\).  The four portal sets have an SDR
by restriction of the six-portal SDR.  Their representatives alternate.
After a leaf flip, they must still alternate.  Reversing a contiguous
block of four alternating points preserves alternation only when the
block contains

\[
 0,1,3,\text{ or }4
\]

of them; a two-point reversal destroys alternation.

Apply the interval argument (5.1)--(5.2) to the rank-four transversal
matroid of these four portal sets.  Since no basis uses exactly two
vertices of the leaf side, one side has portal rank at most one for
these four labels.  The two unrepresented boundary labels now replace
the missing portal information in the cut calculation.  If all four
represented-label incidences on that side are covered by one label,
then its external neighbourhood is contained in

\[
 \{p,q,z\}\cup\{\text{the two omitted labels}\}
             \cup\{\text{one represented label}\},                 \tag{6.1}
\]

of order at most six.  If they are covered by one shore vertex \(x\),
then a component after deleting \(x\) has its neighbourhood in

\[
 \{p,q,z,x\}\cup\{\text{the two omitted labels}\},                 \tag{6.2}
\]

again of order at most six.  Seven-connectivity therefore forces the
low-rank side to be the singleton \(\{x\}\).

### Theorem 6.1 (orientation-free leaf singleton)

Let \(D\) be a nonsingleton high-owner shore satisfying the audited
six-portal Hall condition, the three forbidden antipodal linkages, and
the exact two-cut locks.  For every leaf edge of a nontrivial reduced
SPQR decomposition of \(D\), one of the two interiors displayed by that
edge is a singleton degree-two vertex with the exact lock (5.4).

### Proof

Each forbidden antipodal linkage supplies a bare four-web embedding in
which its four full portal sets lie on one face.  Apply the rank-four
argument above to either side of the selected leaf separation.  It gives
portal rank at most one on one of the two interiors.  The cut calculation
(6.1)--(6.2) then forces that interior to be a singleton \(\{x\}\).
Two-connectivity makes the separation vertices the two shore neighbours
of \(x\), and the exact degree-two portal lock gives (5.4).  The argument
does not choose which orientation of the leaf edge contains \(x\).
\(\square\)

The orientation qualification is essential.  In a canonical
three-node R--P--S decomposition, viewed from the R-leaf edge, the
complementary P--S side can have the sole internal vertex \(x\): the
real edge \(pq\) and the path \(pxq\) require both the P- and S-nodes.
Thus the former inference that a tree with at least three nodes has
singleton *actual leaf sides*, and hence is a path with two locked ends,
was false and is retracted.

### Corollary 6.2 (canonical S-leaf)

If \(D\) has a nontrivial SPQR tree, then it has an S-node leaf whose
real path is \(pxq\) for a singleton degree-two vertex \(x\).

### Proof

Choose any SPQR leaf edge and let \(\{x\}\) be the singleton side given
by Theorem 6.1, with separation pair \(\{p,q\}\).  The degree-two lock
gives \(d_G(x)=7\), and \(p,q\) both miss the unique boundary label of
\(x\).  Dirac's bound \(\alpha(N_G(x))\le2\) therefore forces
\(pq\in E(D)\).  The three \(p\)-\(q\) bridges are the path \(pxq\),
the real edge \(pq\), and the connected complementary side.  A reduced
SPQR decomposition represents them by a P-node, with a leaf S-node for
the triangle \(pxq\).  This conclusion is independent of the
orientation of the originally selected leaf edge. \(\square\)

The cycle-leaf theorem in `hadwiger_c6_spqr_cycle_leaf.md` eliminates
exactly this S-node leaf.  Hence no nontrivial SPQR tree occurs.  Together
with the three-connected closure of Theorem 1.1, this closes the
high-owner shore and therefore the \(C_6\dot\cup K_1\) boundary core.

## 7. Conditional monotone defect calculation (not used in the closure)

This section records a conditional calculation for a shore which is
*separately assumed* to have two locked end vertices and an
\(xy\)-numbering between them.  The retracted orientation claim above
does not produce those two ends, so nothing below is part of the proof
of Corollary 6.2 or of the \(C_6\) closure.

Assume the two end vertices have unique labels \(v,w\), where
\(vw\in E(C)\).  Orient the SPQR path from the \(v\)-end to the
\(w\)-end.  Choose the natural nested connected bipartitions
\(L_j\mid R_j\) across its successive virtual edges, allocating each
separation pair consistently so that

\[
 L_0=\{x_v\},\qquad R_m=\{x_w\}.
\]

Put

\[
 d_j=S-N_S(L_j),\qquad e_j=S-N_S(R_j).
\]

Then \(L_j\) increases and \(R_j\) decreases, so

\[
 d_{j+1}\subseteq d_j,qquad e_j\subseteq e_{j+1}.                  \tag{7.1}
\]

The endpoint locks give

\[
 (d_0,e_0)=(N_C(v),\{v\}),\qquad
 (d_m,e_m)=(\{w\},N_C(w)).                         \tag{7.2}
\]

Every pair in the chain has both coordinates of order at most two and
is negative in the exact split atlas.  The low-defect list and (7.1)
leave three states: the two endpoint states in (7.2) and their
coordinatewise union.  In particular the state changes at most twice
(allowing repetitions and a direct jump).

To see this directly, normalize \(v=0,w=1\) on the alternating cycle.
The first coordinate is trapped between \(\{1\}\) and
\(\{5,1\}\), while the second is trapped between \(\{0\}\) and
\(\{0,2\}\).  The singleton--singleton pair is positive, and no
antipodal-pair row of the atlas lies in these inclusion intervals.  The
remaining three possibilities are negative:

\[
 L=\{5,1\}\mid\{0\},\qquad
 M=\{5,1\}\mid\{0,2\},\qquad
 R=\{1\}\mid\{0,2\}.                             \tag{7.3}
\]

Here \(M\) dominates the singleton-neighbour row
\(\{1\}\mid N_C(1)\).  Monotonicity forces the word

\[
 L^{*}M^{*}R^{*},                                  \tag{7.4}
\]

with nonempty first and last runs; the middle run may be empty.  The
infinite rope has consequently been reduced to at most two local
state-switch torsos.  A detailed construction of the nested SPQR
prefixes and audit of the atlas direction are recorded in
`hadwiger_c6_rope_defect_transition.md`.  Closing the shore now requires
a local theorem at these transitions, not a case analysis growing with
the length of the rope.
