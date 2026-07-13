# A planar-web counterexample to a portal-block trichotomy

## 1. Purpose

The portal-transversal theorem is correct, but an SDR cannot be promoted
to disjoint connected block witnesses using only

* a minimum cut;
* full attachment of every boundary vertex;
* ambient \(t\)-connectivity and minimum degree at least \(t\);
* exclusion of a \(K_t\)-minor; and
* exact independent-set traces on both shores.

This note gives an explicit counterexample for \(t=7\). It also identifies
the additional counterexample-derived axiom which the example violates:
**boundary minor-switching**.

The dependency-free executable certificate is
portal_block_web_counterexample_verify.py. Run it with

    uv run --script portal_block_web_counterexample_verify.py

In a restricted environment, pass a writable cache:

    uv --cache-dir /tmp/codex-uv-cache run --script portal_block_web_counterexample_verify.py

## 2. The pentagonal disk

All subscripts below are modulo five. Let \(Q\) be the plane graph with
outer boundary

\[
 A=a_0a_1a_2a_3a_4a_0,
\]

two inner pentagons \(X=(x_0,\ldots,x_4)\) and
\(Y=(y_0,\ldots,y_4)\), and a hub \(h\). Its edges, in addition to the
three pentagon cycles, are

\[
 a_ix_i,\ a_ix_{i-1},\qquad
 x_iy_i,\ x_iy_{i-1},\qquad
 hy_i
 \quad(0\le i<5).
\tag{2.1}
\]

Thus \(Q\) is a triangulated disk. Its interior

\[
 D=X\cup Y\cup\{h\}
\]

has eleven vertices.

Take two copies \(Q^+,Q^-\) and identify their boundary \(A\), one disk
on each side of \(A\). Call the resulting plane graph \(H\).

### Lemma 2.1

\[
 |H|=27,\qquad \delta(H)=5,\qquad \kappa(H)=5.
\]

Moreover, \(A\) is a minimum cut and \(H-A\) has exactly the two
eleven-vertex components \(D^+,D^-\).

#### Proof

The degree calculation follows directly from (2.1):

* every \(a_i\) has degree six;
* every outer-ring vertex \(x_i^\pm\) has degree six;
* every inner-ring vertex \(y_i^\pm\) has degree five; and
* each hub has degree five.

The graph \(H\) is a maximal plane graph. Direct inspection of the
layered construction shows that every triangle is facial and every
4-cycle has a chord; hence there is no separating cycle of order three
or four. In a maximal plane graph every minimal vertex separator is the
vertex set of a chordless separating cycle. Therefore \(H\) is
5-connected. Deleting \(A\) separates the two disk interiors, so its
connectivity is exactly five. \(\square\)

The inspection in the proof is finite: the only triangles are the two
triangles in each annular cell and the five hub triangles on each side.
A 4-cycle either lies in two adjacent annular cells and has their shared
diagonal, or uses vertices from nonadjacent layers and cannot close.

## 3. The seven-connected \(K_7\)-minor-free graph

Let \(R=\{r_0,r_1\}\) induce \(K_2\), and form

\[
 G=K_2\vee H,
\]

the join in which both vertices of \(R\) are adjacent to every vertex
of \(H\). Put

\[
 S=R\cup A.
\]

### Theorem 3.1

The graph \(G\) has all of the following properties.

1. \(\kappa(G)=7\).
2. \(\delta(G)=7\).
3. \(G\) has no \(K_7\)-minor.
4. \(S\) is a minimum cut of order seven, and both components
   \(D^+,D^-\) of \(G-S\) are full to \(S\) and have order eleven.
5. The portal family \((N_{D^+}(s):s\in S)\) has an SDR.
6. \(\chi(G)=\eta(G)=6\).

#### Proof

If at most six vertices are deleted and one of \(r_0,r_1\) remains, that
universal vertex connects the remainder. If both are deleted, at most
four vertices of \(H\) were deleted, and Lemma 2.1 leaves \(H\)
connected. Thus \(G\) is 7-connected. The set \(S\) separates the two
disk interiors, so \(\kappa(G)=7\).

Joining \(K_2\) raises every degree in \(H\) by two, so
\(\delta(G)=7\).

In any clique-minor model of \(G\), at most two branch sets meet \(R\).
After deleting those branch sets, all remaining branch sets lie in
\(H\). A \(K_7\)-model would therefore leave a \(K_5\)-model in the
planar graph \(H\), impossible.

The hub together with its inner pentagon induces a 4-chromatic odd
wheel, while the colourings displayed later in (5.1) colour both
isomorphic disks compatibly with four colours. Hence \(\chi(H)=4\).
Also \(\eta(H)=4\): planarity gives the upper bound and the odd wheel
has a \(K_4\)-minor. Chromatic number and Hadwiger number are additive
under joining with a clique, so \(\chi(G)=\eta(G)=6\).

Fullness is immediate from (2.1) and the universality of \(R\). An
explicit SDR in \(D^+\) is

\[
 a_i\longmapsto x_i^+\quad(0\le i<5),\qquad
 r_0\longmapsto y_0^+,\qquad r_1\longmapsto y_1^+.
\]

All seven representatives are distinct. \(\square\)

## 4. A complete-quotient block system with no witnesses

Partition \(S\) into

\[
 P=\{a_0,a_2\},\qquad Q=\{a_1,a_3\},\qquad
 \{a_4\},\qquad\{r_0\},\qquad\{r_1\}.
\tag{4.1}
\]

Every block is independent. The block-adjacency quotient is complete:
the \(A\)-cycle supplies all adjacencies among \(P,Q,\{a_4\}\), and
\(r_0,r_1\) are adjacent universal singleton blocks.

### Theorem 4.1

There are no pairwise vertex-disjoint connected subgraphs in
\(G[D^+\cup S]\), one containing each block in (4.1).

#### Proof

The witnesses of the singleton blocks occupy \(a_4,r_0,r_1\).
Consequently the witnesses containing \(P\) and \(Q\) cannot use those
vertices. If the two witnesses existed, connectedness would give
vertex-disjoint paths

\[
 a_0\longleftrightarrow a_2,\qquad
 a_1\longleftrightarrow a_3
\]

inside the plane disk \(Q^+\). The four ends occur on its outer boundary
in the cyclic order \(a_0,a_1,a_2,a_3\). Two paths joining alternating
boundary pairs in a disk must meet, by the Jordan curve theorem. This is
a contradiction. \(\square\)

Thus this graph has no low-degree vertex, no cut smaller than \(S\), and
no Hall deficiency (indeed it has the explicit SDR), yet it has no block
witnesses at all. The obstruction is a genuine two-paths web, not a
gammoid rank defect.

## 5. Exact independent-set traces still hold

The example even satisfies the conclusion of the full-shore exact-trace
lemma on both shores.

### Lemma 5.1

For every nonempty independent set \(I\subseteq S\), the graph
\(G-D^+\) has a proper six-colouring with a colour whose trace on \(S\)
is exactly \(I\). The same holds with the two shores interchanged.

#### Proof

The only independent sets meeting \(R\) are the singleton sets
\(\{r_0\},\{r_1\}\). Give \(r_0,r_1\) two fresh colours; either one is
then an exact singleton trace.

The nonempty independent subsets of \(A=C_5\) are singletons and
nonadjacent pairs. Dihedral symmetry reduces them to \(\{a_0\}\) and
\(\{a_0,a_2\}\). The following are proper four-colourings of one copy
of \(Q\); entries in each row are indexed \(0,\ldots,4\).

\[
\begin{array}{c|ccccc}
 &0&1&2&3&4\\ \hline
 A\ (\{a_0\})     &0&2&1&3&2\\
 X                &1&0&2&1&3\\
 Y                &2&1&0&2&0\\ \hline
 A\ (\{a_0,a_2\}) &0&3&0&1&2\\
 X                &1&2&3&0&3\\
 Y                &0&1&2&1&2
\end{array}
\tag{5.1}
\]

In the first colouring, colour zero has boundary trace \(\{a_0\}\);
in the second it has trace \(\{a_0,a_2\}\). Rotation and reflection give
all other cases. In both rows of (5.1), give the hub colour \(3\).
Add the two fresh colours on \(R\). This proves the
claim, and symmetry proves it for either shore. \(\square\)

## 6. The axiom which fails: boundary minor-switching

For an \(S\)-boundaried graph \(L\), let

\[
 {\cal E}_6(L,S)
\]

be the set of labelled six-colourings of \(S\) which extend to \(L\).
The two shore graphs in the example are isomorphic by an isomorphism
fixing \(S\). Hence

\[
 {\cal E}_6(G[D^+\cup S],S)
 =
 {\cal E}_6(G[D^-\cup S],S).                       \tag{6.1}
\]

In particular their extension sets intersect, and \(G\) itself is
six-colourable. This is exactly where the construction falls short of a
minor-minimal counterexample.

In fact the disk is much more flexible than exact traces reveal.

### Lemma 6.1 (boundary universality of the pentagonal disk)

Every proper four-colouring of the outer \(C_5=A\) extends to \(Q\).
Consequently

\[
 {\cal E}_6(G[D^+\cup S],S)
 =
 \{\hbox{all proper labelled six-colourings of }G[S]\}. \tag{6.2}
\]

#### Proof

Up to a permutation of the palette, a proper colouring of \(C_5\) with
at most four colours has one of the ten boundary words in the first
column below. The other columns give extending colour words on \(X,Y\)
and the colour of \(h\).

\[
\begin{array}{c|c|c|c}
A&X&Y&h\\ \hline
01012&23201&10120&3\\
01021&23103&10210&3\\
01023&23101&02323&1\\
01201&20123&12010&3\\
01202&20131&12020&3\\
01203&20121&13030&2\\
01212&20301&12120&3\\
01213&20301&12120&3\\
01231&20103&32320&1\\
01232&20101&12323&0
\end{array}
\]

Direct inspection against (2.1) verifies every row. These are all
normalized proper \(C_5\)-words: after fixing the first colour as zero,
introduce each new colour by its first occurrence, which gives exactly
the displayed list.

In a proper six-colouring of \(S=K_2\vee C_5\), the two vertices of
\(K_2\) use distinct colours and \(A\) uses only the other four.
The first assertion extends the boundary colouring over the disk.
\(\square\)

Thus if \(M\) is *any* six-colourable graph on the opposite side of the
same boundary, first colour \(M\) and then extend its boundary state over
the disk. The union is six-colourable. This particular web side is
therefore excluded from a hypothetical contraction-critical graph even
without examining its individual internal edges. General webs need not
be boundary-universal, which is why the switching formulation below is
still required.

The following elementary lemma records the missing axiom.

### Lemma 6.2 (critical boundary minor-switching)

Let \(G=L\cup_S M\) be a proper separation of a graph which is not
\(r\)-colourable but every proper minor of \(G\) is \(r\)-colourable.
If \(\mu\) is any deletion or contraction wholly internal to \(L-S\),
then

\[
 \bigl({\cal E}_r(L^\mu,S)\setminus{\cal E}_r(L,S)\bigr)
 \cap {\cal E}_r(M,S)\ne\varnothing.               \tag{6.3}
\]

The symmetric statement holds for operations internal to \(M-S\).

#### Proof

Colour the proper minor \(G^\mu=L^\mu\cup_S M\) with \(r\) colours and
let \(\varphi\) be its boundary restriction. Then
\(\varphi\in{\cal E}_r(L^\mu,S)\cap{\cal E}_r(M,S)\). If
\(\varphi\in{\cal E}_r(L,S)\), its two extensions glue to an
\(r\)-colouring of \(G\), a contradiction. \(\square\)

Equation (6.1) shows that the symmetric planar web cannot satisfy the
incompatibility and switching forced by Lemma 6.2. Exact traces are only
one-colour projections of the extension relation and do not detect this
failure.

## 7. Corrected structural target

A viable uniform portal theorem must have a fourth, web-like outcome.
One precise research target is:

> **Block witnesses, lift, low degree, or critical web.** Let \(S\) be a
> minimum cut of a \(t\)-contraction-critical \(K_t\)-minor-free graph,
> let \(D\) be a full component, and prescribe a complete-quotient
> independent partition of \(S\). Then at least one of the following
> occurs:
>
> 1. the blocks have disjoint connected witnesses with deletion loss
>    below the exposure-weighted knitting threshold;
> 2. a Hall/gammoid or residual relative deficiency lifts to a cut
>    smaller than \(S\);
> 3. some vertex has degree at most \(t-1\); or
> 4. after deleting inessential bridges, the unsatisfied blocks occur in
>    alternating order in a two-paths web (more generally, a bounded-
>    adhesion society), and every internal minor operation satisfies
>    the critical switching condition (6.3) against the opposite shore.

Outcomes 1--3 are the previously proposed portal-peeling trichotomy.
Theorem 4.1 proves that outcome 4 cannot be omitted, even with
\(t\)-connectivity, minimum degree \(t\), \(K_t\)-minor exclusion, an
SDR, and all exact independent traces.

The remaining genuinely counterexample-specific lemma is now:

> **Critical-web exclusion.** No web side and opposite side in a
> \(t\)-contraction-critical \(K_t\)-minor-free graph can satisfy (6.3)
> for every internal deletion and contraction while also satisfying all
> full-shore exact traces.

The symmetric construction above fails this lemma maximally because its
two extension sets are identical. Proving critical-web exclusion, rather
than another Hall theorem, is the necessary next step.

### Lemma 7.1 (planar-web curvature bound)

There is nevertheless a uniform restriction on outcome 4. Let
\(S=A\mathbin{\dot\cup}B\), let \(B\) induce a cycle of order \(b\),
and suppose that

\[
 H=G[D\cup B]
\]

has a plane embedding with \(B\) bounding the outer face and all vertices
of \(D\) inside it. Assume \(N_G(D)\subseteq D\cup S\),
\(\delta(G)\ge t\), and

\[
 |N_G(x)\cap A|\le e\qquad(x\in D).
\]

If \(t-e>6\), then

\[
 |D|\le\frac{2b-6}{t-e-6}.                         \tag{7.1}
\]

#### Proof

Put \(n=|D|\). Since the outer face has length \(b\),

\[
 |E(H)|\le 3(n+b)-3-b=3n+2b-3.
\]

The boundary cycle contributes at least \(2b\) to the sum of the degrees
of its vertices. Every \(x\in D\) loses at most \(e\) neighbours when
\(A\) is omitted, so \(d_H(x)\ge t-e\). Consequently

\[
\begin{aligned}
 (t-e)n
 &\le\sum_{x\in D}d_H(x)\\
 &=2|E(H)|-\sum_{v\in B}d_H(v)\\
 &\le 6n+2b-6.
\end{aligned}
\]

Rearranging proves (7.1). \(\square\)

If the \(B\)-portal family has an SDR, then \(|D|\ge b\). Lemma 7.1
therefore eliminates every planar web with \(t-e\ge8\). When \(b\le5\),
it also eliminates \(t-e=7\), since (7.1) gives
\(|D|\le2b-6<b\). Thus a surviving planar web with a portal transversal
must have

\[
 e\ge t-7,
\]

and for a five-vertex society it must have \(e\ge t-6\). In words: a
large critical web is possible only when almost the entire degree budget
of its interior vertices is supplied by the protected boundary
\(A\). This is the quantitative bridge from the web outcome back to the
exposure-weighted knitting theorem.

## 8. The obstruction is uniform in \(t\)

The construction is not a peculiarity of seven colours.

For \(L\ge2\), define \(Q_L\) by placing \(L\) concentric pentagonal
rings between the boundary \(A=C_5\) and the hub. Consecutive rings are
joined by the same triangulated annulus as in (2.1). Glue two copies
along \(A\), obtaining \(H_L\), and put

\[
 G_{t,L}=K_{t-5}\vee H_L.
\]

### Theorem 8.1 (uniform structural counterexample)

For every \(t\ge7\), choose

\[
 L\ge \left\lceil\frac{t-1}{5}\right\rceil.
\]

Then \(G_{t,L}\) satisfies

\[
 \kappa(G_{t,L})=\delta(G_{t,L})=t,\qquad
 \chi(G_{t,L})=\eta(G_{t,L})=t-1.
\tag{8.1}
\]

It has a minimum cut

\[
 S=V(K_{t-5})\cup A
\]

of order \(t\), and each full shore has \(5L+1\ge t\) vertices and an
\(S\)-portal SDR. Nevertheless the complete-quotient partition

\[
 \{a_0,a_2\}\mid\{a_1,a_3\}\mid\{a_4\}\mid
 \{\{r\}:r\in V(K_{t-5})\}
\tag{8.2}
\]

has no disjoint connected witnesses in either shore. Every independent
set of \(S\) is still an exact trace from either side.

#### Proof

The same face inspection as in Lemma 2.1 shows that \(H_L\) is a
5-connected planar triangulation of minimum degree five, with \(A\) a
minimum 5-cut. Joining \(K_{t-5}\) raises connectivity and minimum
degree to \(t\). A \(K_t\)-model would leave a \(K_5\)-model in the
planar graph \(H_L\) after discarding the at most \(t-5\) branch sets
meeting the joined clique. Thus \(G_{t,L}\) is \(K_t\)-minor-free.

The innermost pentagon and hub form a 4-chromatic odd wheel, and the
four-colour extension below gives \(\chi(H_L)=4\). Hence the chromatic
number of the join is \(t-1\). The same join argument and planarity give
\(\eta(G_{t,L})=t-1\).

Map each \(a_i\) to the corresponding vertex of the outermost ring.
After these five representatives are used, the shore has \(5L-4\)
vertices left. The displayed bound on \(L\) gives

\[
 5L-4\ge t-5,
\]

so the joined-clique vertices also receive distinct representatives.

The alternating-path proof of Theorem 4.1 is unchanged. Finally,
boundary universality propagates through additional annuli: use the
first two layers of the table in Lemma 6.1 to colour a new outer ring,
then extend its proper colouring through the already universal inner
disk. Induction from \(Q_2\) proves that every proper four-colouring of
\(A\) extends through \(Q_L\). Assign distinct fresh colours to the
joined clique. This proves boundary universality and all exact traces.
\(\square\)

Thus even a uniform theorem for every \(t\) cannot be based only on
connectivity, degree, minor exclusion, portal transversals, or exact
independent traces. The one hypothesis distinguishing a hypothetical
counterexample is precisely the jump from \(\chi=t-1\) to \(\chi=t\),
encoded locally by the extension-set incompatibility and minor-switching
condition (6.3).
