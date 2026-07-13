# Multi-component seven-cuts: five shores are impossible

## 1. Setting

Let \(G\) be a seven-connected \(K_7\)-minor-free graph with
\(\delta(G)\ge7\), and let \(S\) be a vertex cut of order seven.  Write

\[
 G-S=D_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}D_m
\]

for its components.  Every \(D_i\) is full to \(S\): if some
\(s\in S\) had no neighbour in \(D_i\), then
\(N(D_i)\subseteq S-\{s\}\) would be a cut of order at most six.

The following closes the multi-component alternative left open by the
atomic-fragment normalization.

## 2. Elementary packing observations

### Lemma 2.1

If \(m\ge7\), then \(G\) contains a \(K_7\)-minor.  If \(m=6\), the
same conclusion holds.

#### Proof

For \(m\ge7\), choose seven components and distinct vertices
\(s_1,\ldots,s_7\in S\).  The sets
\(D_i\cup\{s_i\}\) are connected and pairwise adjacent: for
\(i\ne j\), fullness gives an edge from \(D_i\) to \(s_j\).

For \(m=6\), choose \(s_0\in S\), assign the other six boundary
vertices bijectively to the six components, and use the six bags
\(D_i\cup\{s_i\}\) together with the singleton \(\{s_0\}\).  Fullness
makes every required adjacency. \(\square\)

### Lemma 2.2

If \(m=5\) and \(G[S]\) has an edge, then \(G\) contains a
\(K_7\)-minor.

#### Proof

Let \(uv\in E(G[S])\).  Use \(\{u\},\{v\}\) as two bags and assign the
five vertices of \(S-\{u,v\}\) bijectively to the five components.
The five resulting component bags are pairwise adjacent and see both
singletons by fullness. \(\square\)

Thus a surviving five-component cut has \(G[S]\) edgeless.

## 3. The five-component closure

For \(s\in S\) and a component \(D_i\), call \((s,D_i)\) repeated if
\(|N_{D_i}(s)|\ge2\).

### Lemma 3.1 (two repeated portal classes)

If \(m=5\) and \(G[S]\) is edgeless, some component \(D_i\) contains
two distinct repeated boundary classes.

#### Proof

Fix \(s\in S\).  Fullness gives at least one neighbour of \(s\) in
each of the five components.  Since \(S\) is independent and
\(d_G(s)\ge7\),

\[
 \sum_{i=1}^5 |N_{D_i}(s)|=d_G(s)\ge7.
\]

Hence \((s,D_i)\) is repeated for at least one \(i\).  There are seven
boundary vertices and only five components, so one component repeats
two distinct classes. \(\square\)

### Theorem 3.2 (no five-component seven-cut)

The case \(m=5\) is impossible.

#### Proof

By Lemma 2.2, assume \(S\) is independent.  Choose a component \(R\)
and distinct \(a,b\in S\) for which

\[
 |N_R(a)|\ge2,\qquad |N_R(b)|\ge2.
\]

Apply the double-root split-or-cutvertex theorem
(`hadwiger_root_multiplicity_split.md`, Theorem 1.1).

First suppose \(R=R_1\dot\cup R_2\) is a connected adjacent split and
both rows contain \(a,b\).  Use the singleton \(\{a\}\).  Assign the
six vertices of \(S-\{a\}\) bijectively to the six pieces consisting
of \(R_1,R_2\) and the other four components as follows.  Since the two
contact rows cover \(S\), at least one split piece, say \(R_1\), contacts
a vertex \(c\in S-\{a,b\}\).  Give \(R_1\) the anchor \(c\), give
\(R_2\) the anchor \(b\) (both pieces contact \(b\)), and assign the
remaining four vertices of \(S-\{a,b,c\}\) as anchors for the four full
components.

Each piece plus its anchor is connected.  Bags coming from different
original components are adjacent because the unsplit component is full
to the other bag's anchor.  The two \(R\)-bags are adjacent by the split.
Every one of the six bags sees \(\{a\}\): the four unsplit components
are full to \(a\), and both split pieces contact \(a\).  These are seven
pairwise adjacent bags.

Now suppose a cutvertex \(q\in R\) meets every
\(N_R(a)\)-to-\(N_R(b)\) path.  At least two components
\(C_1,C_2\) of \(R-q\) contain the separated portal classes.  For every
component \(C\) of \(R-q\),

\[
 N_G(C)\subseteq S\cup\{q\}.
\]

Seven-connectivity therefore gives \(|N_S(C)|\ge6\).  In particular,
each of \(C_1,C_2\) misses at most one boundary vertex.

Choose \(s_0\in S\) contacted by both \(C_1,C_2\); at least five choices
exist.  The intersection

\[
 (N_S(C_1)\cap N_S(C_2))-\{s_0\}
\]

has at least four vertices.  Choose distinct \(x_1,x_2\) in this
intersection and use them as anchors for \(C_1,C_2\), respectively.
Assign the remaining four anchors to the other four full components.
The six anchored component bags are pairwise adjacent: the only
nonautomatic pair is \(C_1,C_2\), and each component contacts the other
bag's anchor.  All six bags see the singleton \(\{s_0\}\).
Again they form a \(K_7\)-model, a contradiction. \(\square\)

## 4. Exact surviving multi-component forms

### Corollary 4.1

Every seven-cut in \(G\) has at most four components.  Moreover:

* if it has four components, \(G[S]\) is triangle-free;
* if it has three components, \(G[S]\) has no \(K_4\).

#### Proof

The component bound is Lemma 2.1 and Theorem 3.2.  If four components
and a boundary triangle exist, use the three triangle vertices as
singletons and anchor the four components at the other four boundary
vertices.  If three components and a boundary \(K_4\) exist, use its
four vertices as singletons and anchor the three components at the
remaining boundary vertices.  Fullness verifies all adjacencies.
\(\square\)

### Lemma 4.2 (three-shore triangle split packing)

Suppose \(G-S\) has three full components, one of which has a connected
adjacent split \(R=R_1\dot\cup R_2\).  If there is a triangle \(T\) in
\(G[S]\) such that

\[
 T\subseteq N_S(R_1)\cap N_S(R_2)
\]

and both split rows meet \(S-T\), then \(G\) contains a \(K_7\) minor.

#### Proof

The two contact rows cover \(S\), because \(R\) is full.  Their
restrictions to the four-element set \(S-T\) therefore have union
\(S-T\); since both are nonempty, they admit distinct representatives
\(x_1,x_2\).  Anchor \(R_1,R_2\) at \(x_1,x_2\), anchor the other two
full components at the remaining two vertices of \(S-T\), and use the
three vertices of \(T\) as singleton bags.  The two split bags are
adjacent internally.  Every pair involving an unsplit component bag is
adjacent by fullness, and all four component-derived bags see every
singleton in \(T\). \(\square\)

Thus the exact split obstruction for a fixed common triangle is that one
split row has boundary contact set exactly \(T\).  If the split occurs
inside a minimum fragment, atomic surplus then forces that three-contact
row to have at least five distinct neighbours across the split.

### Lemma 4.3 (three-shore cutvertex triangle packing)

Suppose \(G-S\) has three full components and \(q\) is a cutvertex of one
component \(R\).  Let \(C_1,C_2\) be two components of \(R-q\).  If

\[
 |N_S(C_1)|,|N_S(C_2)|\ge6
\]

and \(G[N_S(C_1)\cap N_S(C_2)]\) contains a triangle, then \(G\)
contains a \(K_7\) minor.

#### Proof

Put \(I=N_S(C_1)\cap N_S(C_2)\), so \(|I|\ge5\), and choose a
triangle \(T\subseteq I\).  There remain two distinct vertices
\(x_1,x_2\in I-T\); use them as anchors for \(C_1,C_2\).  Anchor the
other two full components at the remaining two vertices of
\(S-T-\{x_1,x_2\}\), and use \(T\) as three singleton bags.  The two
cutvertex pieces see each other's anchors, all pairs involving a full
component are adjacent by fullness, and all four component-derived bags
see \(T\). \(\square\)

For a Moser-spindle boundary, the cutvertex outcome can therefore survive
only if the at most two labels missed collectively by \(C_1,C_2\) form a
triangle transversal.  In the standard Moser labelling these pairs are

\[
 \{1,3\},\{1,4\},\{2,3\},\{2,4\};
\]

for the one-edge extension \(M+13\), the list is

\[
 \{1,3\},\{1,4\},\{2,3\}.
\]

These are exact portal-placement residues, rather than further failures
of the coarse full-shore quotient.

## 5. Consequence for atomic normalization

The minimum-fragment theorem in
`hadwiger_exact_cut_atomic_kernel.md` applies to a component of a cut
with two, three, or four full shores.  The cyclic-hull theorem applies
directly only in the two-shore case.  Corollary 4.1 supplies the exact
remaining atomic branches rather than silently assuming them away:

\[
 \begin{array}{c|c}
 \text{number of shores}&\text{necessary boundary condition}\\
 \hline
 2&\text{cyclic-hull / covering-split geometry},\\
 3&\omega(G[S])\le3,\\
 4&G[S]\text{ triangle-free}.
 \end{array}
\]

Under only the hypotheses of this note, the theorem eliminates every
atomic cut with five or more shores.  In the six-minor-critical HC7
setting, the full-shore block-gluing theorem in
`hadwiger_full_shore_block_gluing.md` also eliminates the four-shore row:
it forces \(\chi(G[S])\ge4\), whereas every triangle-free graph on seven
vertices is three-colourable.  The exact multi-component residue is
therefore the three-shore row, constrained further by Lemmas 4.2--4.3
and the block-state conditions.
