# Corrected two-cut quotient for the (C_6) shore

## 1. Retraction and exact counterstate

The former assertion that a two-cut quotient cannot visibly support an
opposite pair of frames is false.  Let the two components of
(D-\{p,q\}) be contracted to (a,b).  The state

\[
 (N_S(a),N_S(b),N_S(p),N_S(q))=(109,118,0,0)         \tag{1.1}
\]

in seven-bit notation passes every connected allocation through the
exact negative two-piece atlas.  It visibly supports frames 0 and 3:
both use the singleton quotient pieces (b,a).  Thus the two frame
crossings exist separately but are incompatible, because both reuse the
same two component vertices.

The corrected program `c6_twocut_support_probe.py` includes zero contact
rows, checks all singleton cut-vertex splits, and now asserts the actual
output.  There are 21 visible support words.  Besides the six maximal
three-consecutive words, the maximal family contains

\[
 001001,qquad010010,qquad100100,                    \tag{1.2}
\]

the three opposite pairs.

## 2. Exact maximal opposite-visible states

Among the 384 opposite-visible states, there are six inclusion-maximal
contact tuples:

\[
\begin{array}{c|c|c}
(N_S(a),N_S(b),N_S(p),N_S(q))&
(d_a,d_b,d_p,d_q)&\text{support}\\
\hline
(91,109,73,73)&(36,18,54,54)&010010\\
(91,118,82,82)&(36,9,45,45)&100100\\
(109,91,73,73)&(18,36,54,54)&010010\\
(109,118,100,100)&(18,9,27,27)&001001\\
(118,91,82,82)&(9,36,45,45)&100100\\
(118,109,100,100)&(9,18,27,27)&001001.
\end{array}                                         \tag{2.1}
\]

Write the three identity matching pairs as

\[
 M_0=\{c_0,c_3\},\quad M_1=\{c_1,c_4\},\quad
 M_2=\{c_2,c_5\}.
\]

Table (2.1) has a uniform interpretation.  After permuting the indices,

\[
 d_a=M_i,qquad d_b=M_j,qquad
 N_S(p),N_S(q)\subseteq M_k\cup\{z\},               \tag{2.2}
\]

where ({i,j,k}=\{0,1,2\}).  Since each component has at least five
boundary contacts, its row is exactly (S-M_i) or (S-M_j); only the
cut-vertex rows may shrink from the displayed maxima.

The two separately visible opposite frames assign one missing-edge path
to (a) and one to (b) in each frame.  For the canonical state
(d_a=M_1,d_b=M_0), component (A) separately supports the antipodal
demands (e_2,e_5), while (B) separately supports (e_4,e_1).
Neither component can support its two demands disjointly, since that
would be an antipodal two-linkage in the whole shore and hence an
explicit (K_7)-model.

Thus a genuine opposite-visible two-cut is not arbitrary: both
(A\cup\{p,q\}) and (B\cup\{p,q\}) are crossless four-terminal
societies.  This is the correct rope/web conclusion replacing the false
visibility lemma.

## 3. Structural next step

Apply the generalized Two Paths Theorem separately to those two
societies, retaining (p,q) as real vertices.  Any inserted clique
behind a facial triangle, together with the three omitted boundary
vertices, gives a cut of order at most six, so each completion is a bare
web.  The remaining issue is the relative flip of the two web disks
across the virtual (pq) edge.  Aligning the flips gives the common-face
circular closure; failure to align must be converted into an exact
colour-gluable two-separation or a degree-six portal bottleneck.
