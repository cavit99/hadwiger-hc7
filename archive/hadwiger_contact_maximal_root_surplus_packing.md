# Root-surplus block packing at a contact-maximal \(K_6\)-model

## 1. Spanning terminal setup

Use the spanning normalization in
\`hadwiger_contact_maximal_spanning_normalization.md\`.  Let

\[
             (D,U,B_1,B_2,B_3,B_4)                       \tag{1.1}
\]

be a spanning \(K_6\)-model in \(H=G-v\), where \(U\) is the unique
uncontacted bag and the other five bags are contacted.  Every union of
old bags used below is connected because the six old bags are pairwise
adjacent.

For disjoint connected pieces \(C_1,\ldots,C_s\subseteq D\) and an old
bag \(Q\in\{U,B_1,\ldots,B_4\}\), define its support mask

\[
        \mu(Q)=\{i\in[s]:E(C_i,Q)\ne\varnothing\}.       \tag{1.2}
\]

It is important that masks record actual edges to the selected pieces,
not merely the old adjacency \(D\sim Q\).

### Theorem 1.1 (uniform rooted-piece/group packing)

Let a labelled (K_r)-model have old bags (D,Q_1,ldots,Q_{r-1}).
Suppose (D) contains (s) disjoint, pairwise adjacent connected rooted
pieces (C_1,ldots,C_s), and the old bags (Q_j) can be partitioned
into (r-s) nonempty groups (J_1,ldots,J_{r-s}) such that

1. every group contains an old contacted bag; and
2. for every (i,k), the piece (C_i) is adjacent to at least one bag
   in (J_k).

Then the host contains an (N(v))-meeting (K_r)-model, and adjoining
({v}) gives a (K_{r+1})-minor.

#### Proof

For each (k), merge all old clique bags in (J_k).  The resulting
sets are disjoint, connected, pairwise adjacent and contacted.  Condition
2 makes them adjacent to all (C_i), and the (C_i)'s form a clique
model among themselves.  These are (s+(r-s)=r) rooted clique bags.
(square)

This is the uniform principle behind all allocations below.  The special
feature of (HC_7) is that two surplus roots reduce the allocation to
five masks on three pieces, or four masks on a cross-frame.

## 2. One bag containing three roots

### Theorem 2.1 (three-piece helper packing)

Suppose \(D\) contains three distinct roots \(a_1,a_2,a_3\in N(v)\)
and contains disjoint, pairwise adjacent connected sets

\[
                         C_1,C_2,C_3,                    \tag{2.1}
\]

with \(a_i\in C_i\).  Put

\[
                         \mathcal Q=\{U,B_1,B_2,B_3,B_4\}.
\]

If \(\mathcal Q\) has a partition into three nonempty blocks

\[
                         \mathcal Q=J_1\dot\cup J_2\dot\cup J_3 \tag{2.2}
\]

such that

1. every \(J_k\) contains at least one contacted bag \(B_j\); and
2. for every \(i,k\in[3]\), some \(Q\in J_k\) satisfies
   \(i\in\mu(Q)\),

then \(G\) contains a \(K_7\)-minor.

#### Proof

For \(k\in[3]\), put

\[
                         F_k=\bigcup_{Q\in J_k}Q.        \tag{2.3}
\]

The sets \(F_k\) are connected, disjoint, and pairwise adjacent, because
the old bags form a clique model.  Each \(F_k\) is contacted by condition
1.  Condition 2 makes every \(C_i\) adjacent to every \(F_k\), while the
three \(C_i\)'s are pairwise adjacent by (2.1).  Hence

\[
                         C_1,C_2,C_3,F_1,F_2,F_3         \tag{2.4}
\]

are six disjoint, connected, pairwise adjacent branch sets, each meeting
\(N(v)\).  Adding \(\{v\}\) gives a \(K_7\)-model. \(\square\)

### Corollary 2.2 (rooted triangle versus a cut root)

If \(D\) is 2-connected, then (2.1) exists for any three prescribed
roots.  Thus the only internal geometric obstruction preceding the mask
test is a cutvertex/root-set separation in \(D\).

#### Proof

The standard rooted-triangle lemma says that any three vertices of a
2-connected graph lie in three disjoint pairwise adjacent connected
sets.  Apply it to \(a_1,a_2,a_3\). \(\square\)

### Lemma 2.2A (cut-root adhesion or a repeated foreign carrier)

Let the ambient graph be seven-connected and retain the spanning model
(1.1). Suppose \(q\) is a cutvertex of \(D\), and let \(L\) be a
component of \(D-q\) which contains at least one root. For
\(Q\in\{U,B_1,B_2,B_3,B_4\}\), put

\[
                         P_Q=N_Q(L).
\]

Then

\[
                         \sum_Q|P_Q|\ge5.                 \tag{2.5a}
\]

If equality holds, then

\[
                         \Gamma=\{v,q\}\cup\bigcup_QP_Q. \tag{2.5b}
\]

is an actual exact seven-vertex separator.  If the inequality is strict,
some old bag \(Q\) contains at least two distinct neighbours of \(L\).

#### Proof

Because the model is spanning, every neighbour of \(L\) outside \(D\)
lies in one of the five old bags. Different components of \(D-q\) have
no edge, and \(L\) contains a root, so

\[
                         N_G(L)\subseteq
                         \{v,q\}\cup\bigcup_QP_Q.
\]

Another component of \(D-q\) survives outside this set. Thus the right
side is a genuine separator.  Seven-connectivity gives (2.5a).  Equality
makes its order seven and forces equality in the displayed containment.
With more than five portal vertices distributed among five old bags, one
bag is repeated. \(\square\)

At equality, boundary-faithful proper-minor operations in \(L\) and in
the opposite open shore have disjoint equality-state spectra on the
actual adhesion \(\Gamma\). This is the crossed-splicing theorem applied
to (2.5b), not a quotient-state assertion.  In the strict case, the
repeated old bag is the precise carrier on which a detachable-arm or
second split must be attempted.

### Proposition 2.3 (exact maximal mask residue)

Identify a nonempty support mask with a nonempty subset of
\(\{1,2,3\}\).  Up to permuting the three pieces and the four contacted
labels, every support system which is maximal under adding incidences but
does **not** satisfy Theorem 2.1 is one of the following five rows.  The
first entry is the mask of the uncontacted helper \(U\).

\[
\begin{array}{c|cccc}
 \mu(U)&\mu(B_1)&\mu(B_2)&\mu(B_3)&\mu(B_4)\\ \hline
 12&12&12&123&123\\
 123&1&2&3&123\\
 123&12&12&12&123\\
 123&12&12&13&13\\
 123&12&12&13&23
\end{array}                                             \tag{2.5}
\]

Every bad support system is obtained from one of these rows by deleting
incidences.

#### Verification

There are \(7^5\) ordered nonempty mask systems.  Enumerate the 25 set
partitions of five labels into three blocks.  Accept a partition exactly
when each block contains a contacted label and its bitwise mask union is
\(123\).  Keep a rejected system only when adding any missing incidence
makes it accepted, then quotient by \(S_3\times S_4\).  The five orbits
are exactly (2.5).  The independent exhaustive verifier is
\`contact_root_surplus_mask_verify.py\`.

The table is a finite support certificate, not a claim that all five rows
occur in a contraction-critical graph.  For example the second row is a
sharp static obstruction: the uncontacted bag and one contacted bag are
universal, while the other three contacted bags see only one rooted piece
each.  No three rooted far groups can be formed.

### Theorem 2.4 (two-helper compression)

Retain the rooted triangle \(C_1,C_2,C_3\). Suppose there are distinct
indices \(p,q,k\in[3]\) and a contacted label \(h\in[4]\) such that

\[
 p\in\mu(U),\qquad q\in\mu(B_h),\qquad
 k\in\bigcap_{j\in[4]-\{h\}}\mu(B_j).                    \tag{2.6}
\]

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Absorb the uncontacted helper \(U\) into \(C_p\), and absorb the contacted
helper \(B_h\) into \(C_q\). The two enlarged pieces are connected and
remain disjoint.  Each is adjacent to every remaining old bag through the
old clique edge from its helper. The third piece \(C_k\) is adjacent to
all three remaining contacted bags by (2.6).

Use those three remaining contacted bags as singleton far carriers.  The
three rooted triangle pieces are pairwise adjacent, the far carriers are
pairwise adjacent, and the preceding paragraph gives every cross
adjacency.  All six branch sets are contacted: the triangle pieces contain
the three roots of \(D\), and the far carriers retain their old roots.
Adding \(\{v\}\) gives \(K_7\). \(\square\)

### Corollary 2.5 (combined two-helper mask residue)

Theorem 2.4 closes four of the five *old* maximal bad rows in (2.5), but
submasks of those rows create new maximal systems for the combined test.
Up to permuting the three pieces and contacted labels, the systems maximal
subject to failure of both Theorems 2.1 and 2.4 are

\[
\begin{array}{c|c}
\mu(U)&(\mu(B_1),\mu(B_2),\mu(B_3),\mu(B_4))\\ \hline
1&(1,3,123,123)\\
1&(1,23,23,23)\\
1&(3,3,13,13)\\
12&(1,2,123,123)\\
12&(1,12,23,23)\\
12&(12,12,12,12)\\
123&(1,1,1,1)\\
123&(1,1,23,23)\\
123&(1,2,3,123)\\
123&(1,2,13,23)
\end{array}                                             \tag{2.7}
\]

#### Proof

For the five rows of (2.5), choose respectively

\[
\begin{array}{c|ccc}
\text{row}&p&q&k\text{ and helper }h\\ \hline
1&1&3&2,\ h=4,\\
3&1&3&2,\ h=4,\\
4&2&3&1,\ h=3,\\
5&1&3&2,\ h=3.
\end{array}                                             \tag{2.8}
\]

The displayed helper mask contains \(q\), the uncontacted mask contains
\(p\), and every other contacted mask contains \(k\), so Theorem 2.4
applies. In row 2, deleting any one contacted helper leaves three masks
with empty intersection, so (2.6) fails for every choice.

For completeness, the combined monotone predicate was exhaustively
checked on all \(7^5\) ordered nonempty mask systems. There are 5,778
systems failing both the three-group and two-helper tests and 330 which are
inclusion-maximal under adding an incidence. Quotienting those 330 by
\(S_3\times S_4\) gives the ten rows in (2.7). The independent assertions
are in `contact_root_surplus_mask_verify.py`. \(\square\)

The row \((123;1,2,3,123)\) is the sharp three-pole owner frame, but it is
not the only maximal residue once helper incidences themselves may be
deleted.  The ten-row table is a finite support audit, not a structural
closure; its purpose is to prevent the valid two-helper theorem from being
overstated.

## 3. Two distinct double-root bags

Now write the six old bags as

\[
                         (A,B,U,R_1,R_2,R_3),             \tag{3.1}
\]

where \(A,B\) each contain two distinct roots, the \(R_j\)'s are
contacted, and \(U\) is uncontacted.

Choose connected adjacent rooted splits

\[
 A=A_1\dot\cup A_2,\qquad B=B_1\dot\cup B_2.             \tag{3.2}
\]

All four pieces contain roots.  For \(Q\in\{U,R_1,R_2,R_3\}\), let
\(\sigma(Q)\subseteq[4]\) be its support mask on
\((A_1,A_2,B_1,B_2)\).

### Theorem 3.1 (four-piece/two-group packing)

Suppose every \(A_i\) is adjacent to every \(B_j\).  If

\[
 \{U,R_1,R_2,R_3\}=J_1\dot\cup J_2                    \tag{3.3}
\]

so that each block contains a contacted \(R_j\) and

\[
                         \bigcup_{Q\in J_k}\sigma(Q)=[4]
                         \quad(k=1,2),                  \tag{3.4}
\]

then \(G\) contains a \(K_7\)-minor.

#### Proof

Merge the old bags in each \(J_k\) into a connected far carrier \(F_k\).
The cross-completeness hypothesis and the two split edges make
\(A_1,A_2,B_1,B_2\) a \(K_4\)-model.  Equations (3.3)--(3.4) make both
far carriers contacted and adjacent to all four pieces.  Thus the four
pieces and \(F_1,F_2\) are an \(N(v)\)-meeting \(K_6\)-model; add
\(\{v\}\). \(\square\)

The cross-completeness cannot be inferred from the old edge \(AB\): it
requires all four actual piece adjacencies.

### Theorem 3.2 (matched cross-frame/three-group packing)

Suppose, after possibly exchanging indices,

\[
                         E(A_1,B_1)\ne\varnothing,\qquad
                         E(A_2,B_2)\ne\varnothing.       \tag{3.5}
\]

Put

\[
                         C_1=A_1,\quad C_2=B_1,\quad
                         C_3=A_2\cup B_2.                \tag{3.6}
\]

Then \(C_1,C_2,C_3\) are connected, pairwise adjacent rooted sets.  If
\(\{U,R_1,R_2,R_3\}\) can be partitioned into three blocks, each
containing a contacted \(R_j\) and each covering all three masks on
\((C_1,C_2,C_3)\), then \(G\) contains a \(K_7\)-minor.

Equivalently, because there are exactly three contacted old bags, two of
the \(R_j\)'s must individually see all three \(C_i\)'s, and the mask of
the third \(R_j\), together with the support mask of \(U\), must cover
all three.

#### Proof

The edge \(A_2B_2\) makes \(C_3\) connected.  The old split edges
\(A_1A_2\) and \(B_1B_2\) make \(C_3\) adjacent to \(C_1,C_2\), and the
edge \(A_1B_1\) gives the remaining adjacency.  Apply the same far-group
construction as Theorem 2.1. \(\square\)

### Audit of a tempting shortcut

The hypotheses

\[
 A\text{ is 2-connected},\qquad |N_A(B)|\ge2             \tag{3.7}
\]

do let one split \(A\) into two rooted pieces which both meet \(B\): use
two disjoint paths from the two roots to two distinct \(B\)-portals and
extend them to a connected bipartition.  They do **not** prove contact
augmentation.  The two pieces must also both meet each of
\(R_1,R_2,R_3\).  Those three portal classes may be concentrated on one
side.  Thus (3.7) alone cannot justify the six proposed bags

\[
                         A_1,A_2,B\cup U,R_1,R_2,R_3.
\]

The exact sufficient condition for that simpler construction is that the
rooted split of \(A\) meets all four portal classes
\(B,R_1,R_2,R_3\) on both sides.

### Proposition 3.3 (matched-frame maximal mask residue)

For the three pieces in Theorem 3.2, the edge-maximal bad support systems
have, up to permuting the pieces and the three contacted labels, exactly
the following three forms.  Again the first entry is the uncontacted
helper.

\[
\begin{array}{c|ccc}
 U&R_1&R_2&R_3\\ \hline
 12&12&123&123\\
 123&12&12&123\\
 123&12&13&123
\end{array}                                             \tag{3.8}
\]

Every other failed mask system is a submask of a row in (3.8).  The same
verifier enumerates the \(7^4\) systems, applies the exact condition after
Theorem 3.2, and obtains 36 labelled maximal systems in these three
orbits.

### Lemma 3.4 (mutual portal multiplicity creates a matched frame)

Assume \(A\) and \(B\) are 2-connected and

\[
                         |N_A(B)|\ge2,\qquad |N_B(A)|\ge2. \tag{3.9}
\]

Then rooted splits (3.2) can be chosen so that the two matching edges in
(3.5) exist.  Consequently the only obstruction after (3.9) is one of
the three support rows in (3.8).

#### Proof

The bipartite graph of \(AB\)-edges has a matching of order two. Indeed,
a bipartite graph with matching number one has a one-vertex cover, so all
its edges share one endpoint; that would make one of the two sets in
(3.9) a singleton.  Choose disjoint edges

\[
                         u_1v_1,\quad u_2v_2,\qquad
                         u_i\in A,\ v_i\in B.             \tag{3.10}
\]

In the 2-connected graph \(A\), vertex Menger gives two disjoint paths
from its two distinct roots to the two distinct vertices \(u_1,u_2\), in
some pairing.  There is no one-vertex source--target separator: deleting
one vertex leaves (A) connected and leaves at least one source and one
target.  Extend the two disjoint path carriers to a connected bipartition
of \(A\), by contracting them in a spanning tree and deleting an edge of
the path between the two contracted vertices.  Relabel the two pieces so
that \(u_i\in A_i\). Repeat in \(B\), obtaining rooted pieces with
\(v_i\in B_i\). The two edges in (3.10) now give (3.5). \(\square\)

If roots and cross portals coincide, use a length-zero path at the common
vertex in the Menger linkage; the same extension proof applies.  Thus no
hidden distinctness assumption is needed beyond the two roots and the two
portal vertices on each side.

## 4. Sharp static residual

The support and cross-frame hypotheses above are genuine.  A smallest
labelled counterarchitecture takes

* \(A=a_1-x-a_2\) and \(B=b_1-y-b_2\), with the displayed ends as roots;
* the sole \(AB\)-edge \(xy\);
* the four old bags \(U,R_1,R_2,R_3\) pairwise adjacent; and
* every edge from \(A\) or \(B\) to one of those four bags incident with
  \(x\) or \(y\), respectively.

Every rooted split of \(A\) concentrates all four old-bag supports on the
\(x\)-side, and symmetrically for \(B\).  The cross graph of any two such
splits has only the single edge between the two pieces containing
\(x,y\), and hence has no two-edge matching.  The support masks also fail
the far-group tests.  Thus none of Theorems 3.1--3.2 applies.

This is a labelled branch-bag architecture, not a seven-connected
contraction-critical graph.  The spanning seven-connected graph
\(K_2\vee I\) in \`hadwiger_rooted_k24_clean_capture.md\` realizes the
same portal-concentration phenomenon and has no \(K_7\)-minor, but it is
six-colourable.  Therefore no theorem based only on spanning, root
surplus, 2-connectivity, and support masks can eliminate the residual.
The missing axiom is precisely all-operation minor-critical state novelty
inside the concentrated owner cores.

## 5. Outcome

Theorems 2.1 and 3.1--3.2 close unbounded families: the branch bags and
old clique bags may have arbitrary order.  The exact remaining terminals
are finite support types plus one internal geometry:

1. in the triple-root case, one of the five maximal mask rows (2.5), or a
   root-separating cutvertex before the rooted triangle is formed;
2. in the two-double case, failure of every matched cross-frame, or a
   far-support system with no rooted cover partition.

Those are the locations at which a faithful minor-operation state must be
used; root multiplicity by itself is exhausted.
