# Portalized four-block transfer for the reserved-connector cell

## 1. Setup

Let $G$ be a proper-minor-minimal counterexample to $\mathrm{HC}_7$.
Let $v$ have degree seven, put $H=G-v$ and $N=N_G(v)$, and fix an
accessible repeated pair $a,b\in N$.  Write

$$
N=\{a,b\}\mathbin{\dot\cup}U,
\qquad |U|=5.
$$

The point of the next theorem is that an internal separation of $H$ is
not a separation of $G$: the path $a v b$ crosses it.  Thus the ordinary
two-side boundary-state lemma cannot simply be applied.  Contracting the
star $\{v,a,b\}$ on both sides repairs this issue and also prescribes the
common colour of $a,b$.

## 2. Portalized transfer

### Theorem 2.1 (bilateral four-block portal transfer)

Let $(A,B)$ be a separation of $H$, with adhesion $S=A\cap B$, such
that

$$
a\in A-S,\qquad b\in B-S,\qquad U\subseteq S.
$$

Let

$$
\Pi=\{P_1,\ldots,P_q\}
$$

be a partition of $S$ into nonempty independent sets, where $q\le4$ and
every block meets $U$.

Suppose that each side realizes $\Pi$ in the following strong sense.  On
the $A$-side there are pairwise disjoint connected sets

$$
X^A_1,\ldots,X^A_q\subseteq A-\{a\}
$$

such that $X^A_i\cap S=P_i$ and the $X^A_i$ are pairwise adjacent.  On
the $B$-side there are analogous pairwise disjoint connected sets

$$
X^B_1,\ldots,X^B_q\subseteq B-\{b\}
$$

with $X^B_i\cap S=P_i$, again pairwise adjacent.

Then $G$ is six-colourable, a contradiction.

#### Proof

Put $Z=\{v,a,b\}$.  This set is connected, since $va,vb\in E(G)$.
It is disjoint from every $X^A_i$.  Contract $Z$ and all the
$X^A_i$, and delete every unused vertex of $A-S$.  Denote their images
by $z,x_1,\ldots,x_q$.

These $q+1$ images form a clique.  The $x_i$ are pairwise adjacent by
hypothesis.  For each $i$, choose $u_i\in P_i\cap U$.  The old edge
$vu_i$ proves that $z$ is adjacent to $x_i$.  The resulting graph is a
proper minor of $G$, so it has a six-colouring.

Expand this colouring to $H[B]$ as follows.  Give every vertex of $P_i$
the colour of $x_i$, give $b$ the colour of $z$, and retain the colours
on $B-(S\cup\{b\})$.  This is proper.  Each $P_i$ is independent;
different blocks get different colours; every old edge from $S$ into
$B-S$ survived incident with the appropriate contracted image; and every
old edge incident with $b$ survived incident with $z$.  Since
$z,x_1,\ldots,x_q$ form a clique, the equality partition induced on
$S\cup\{b\}$ is exactly

$$
P_1\mid\cdots\mid P_q\mid\{b\}.                 \tag{2.1}
$$

Perform the symmetric contraction using the $X^B_i$.  Expanding on the
$A$-side gives a six-colouring of $H[A]$ whose exact equality partition
on $S\cup\{a\}$ is

$$
P_1\mid\cdots\mid P_q\mid\{a\}.                 \tag{2.2}
$$

Permute the palette on one side so that the colours of corresponding
blocks, and the colours of $a,b$, agree.  The colourings glue on $S$,
and there is no edge from $A-S$ to $B-S$.  We obtain a six-colouring of
$H$ in which $a,b$ share one colour and the five vertices of $U$ use at
most $q$ further colours.  Hence at most $q+1\le5$ colours occur on
$N$.  Give $v$ a sixth colour absent from $N$.  This six-colours $G$,
the required contradiction. $\square$

### Corollary 2.2 (the exact four-rooted-block target)

Under the hypotheses above, let $e=xy$ be a nonedge of $G[U]$.  There
cannot be a bilateral realization of a partition of $S$ into four
independent blocks whose traces on $U$ are

$$
\{x,y\},\qquad \{u\}\quad(u\in U-\{x,y\}).       \tag{2.3}
$$

Indeed every block in (2.3) meets $U$, so Theorem 2.1 applies.  Thus the
repeated pair $ab$ and one additional missing-root pair are precisely the
two equalities needed to leave a colour for $v$.

### Corollary 2.3 (one portal-only block is allowed)

The same proof remains valid with as many as five blocks, provided that

1. at most four blocks meet $U$; and
2. on each side every realized block is adjacent to the star
   $Z=\{v,a,b\}$.

Indeed the five block images form a clique and condition 2 makes their
images together with $z$ a clique of order at most six.  The exact
boundary states therefore align as before.  Only the blocks meeting $U$
contribute colours to $N$, so at most

$$
1+|\{i:P_i\cap U\ne\varnothing\}|\le5
$$

colours occur on $N$.  A block meeting $U$ is automatically adjacent to
$Z$ through an edge $vu$; the extra condition matters only for a
portal-only block.  Thus a fifth independent block may absorb otherwise
awkward adhesion vertices without spending a colour on $N$.

## 3. Application to a locked rooted certificate

Let $\mathcal B=(B_u:u\in U)$ be a rooted $K_5$-model supplied by the
Kriesell--Mohr construction, and put

$$
X=\bigcup_{u\in U}B_u.
$$

Assume that $a,b$ lie in different components of $H-X$.  Choose an
inclusion-minimal $a$--$b$ separator $S_0\subseteq X$ and put
$S=S_0\cup U$.  Let $R_a$ be the component of $H-S$ containing $a$,
set

$$
A=R_a\cup S,
\qquad B=V(H)-R_a,
$$

and note that $(A,B)$ is a separation with $a\in A-S$, $b\in B-S$,
and $U\subseteq S$.

Consequently, for every missing root edge $xy$ of $G[U]$, at least one
of the two open sides fails to realize the four-block trace (2.3) on the
full portal set $S$.  This is the exact remaining bridge obstruction:
it is not enough that both sides contain an $x$--$y$ path.  Every portal
of $S$ must be assigned to the same independent block on both sides, and
the four connected block realizations must be pairwise adjacent.

There are also two unconditional portal facts.  If $R$ is a component of
$H-X$ containing $a$ or $b$, then

1. $R$ is not adjacent to all five rooted bags, since otherwise $R$ and
   the five bags form an $N$-meeting $K_6$-model; and
2. $|N_H(R)|\ge6$ by six-connectivity of $H$.

Thus $N_H(R)$ consists of at least six distinct portals distributed over
at most four rooted bags, and some rooted bag is hit at least twice.  A
valid bridge switch must turn this locked double hit into one of the
bilateral realizations of Corollary 2.2 (or directly into the sixth bag).
Theorem 2.1 proves that such a realization closes the cell; it does not
assert that the realization is automatic.

## 4. Scope

This theorem is a genuine portalized extension of exact boundary-state
transfer for the degree-seven sole-exterior geometry.  It explicitly
handles the apex path $a v b$ and proves the missing-colour count.  It
does not prove the reserved-connector theorem: the remaining geometric
step is to assign a locked separator's portals to four independent rooted
blocks on both sides.

## 5. A sharp six-adhesion counterarchitecture

Even adhesion order six is not forced by six-connectivity of $H$ and
minimality of the separator.  The following explicit construction shows
why seven-connectivity of the full apex graph, or a proper-minor
transition, must enter the next step.

Use the pure-Moser trace with repeated pair $a=1,b=3$ and

$$
U=\{0,2,4,5,6\},\qquad
\overline{G[U]}=05,25,24,46,06.
$$

Add a portal $w$ anticomplete to $U$, and put $S=U\cup\{w\}$.  On the
$a$-side take a clique

$$
A_0=\{a,h_1,\ldots,h_6\}.
$$

Besides the Moser edges from $a$ to $U$, add $aw$, and give the six
helpers respectively the unique $S$-neighbour labels

$$
2,4,5,6,w,w.                                         \tag{5.1}
$$

On the $b$-side take a clique

$$
B_0=\{b,k_1,\ldots,k_6\},
$$

add $bw$, and make every $k_i$ complete to $S$.  There are no
$A_0$--$B_0$ edges.  Retain exactly the pure-Moser graph on
$\{a,b\}\cup U$.

### Proposition 5.1

The resulting graph $H_0$ is six-connected, $S$ is an inclusion-minimal
$a$--$b$ separator among sets containing $U$, but the $A_0$-side has no
four-block realization from Corollary 2.2 for any of the five missing
edges of $G[U]$.

#### Proof

Deleting $S$ separates the two open cliques, so
$\kappa(H_0)\le6$.  We show that deleting at most five vertices leaves
the graph connected.

For every nonempty $Y\subseteq A_0$,

$$
|A_0-Y|+|N_S(Y)|\ge6.                                \tag{5.2}
$$

If $a\notin Y$, the helper labels in (5.1) have only one repetition, so
$|N_S(Y)|\ge |Y|-1$ and (5.2) follows from $|A_0|=7$.  If $a\in Y$ and
$Y$ contains $k$ helpers, then

$$
N_S(a)=\{0,2,6,w\}.
$$

For $k\le4$ these four vertices suffice; for $k=5$ the union of the
helper labels with $N_S(a)$ has order at least five; and for $k=6$ it is
all of $S$.  Again (5.2) follows.  Thus after at most five deletions the
surviving part of $A_0$ has a neighbour in $S$.

The same conclusion is immediate for $B_0$.  At least one of the six
vertices $k_i$ survives, and it is complete to every surviving vertex of
$S$.  Since $|S|=6$, some vertex of $S$ also survives.  Hence the
surviving $A_0$, $S$, and $B_0$ all lie in one component.  This proves
$\kappa(H_0)=6$.

The set $S$ separates $a,b$.  The smaller compulsory set $U$ does not:
in $H_0-U$ the path $a w b$ remains.  Since $S-U=\{w\}$, $S$ is
inclusion-minimal subject to containing $U$.

It remains to exclude a four-block realization on the $A_0$-side.  No
$h_i$ is adjacent to root $0$.  If the merged missing pair is $05$ or
$06$, the block containing that pair (and possibly $w$) has $0$ as an
isolated vertex, so it is not connected.

For each of the other three missing pairs, root $0$ is a singleton trace.
Its realized bag must be the singleton $\{0\}$: it cannot contain a
helper, and assigning $w$ to it would make it disconnected.  Among the
other two singleton-root blocks there is a root $z\in\{5,6\}$ with
$0z\notin E(H_0)$.  The $z$-block has no edge to $0$, because its only
adhesion vertices are $z$ and possibly $w$, and no helper sees $0$.
Thus the four realized blocks cannot be pairwise adjacent.  This covers
all five edges of the missing cycle. $\square$

The script `portal_s6_counterexample_probe.py` independently checks
$\kappa(H_0)=6$ and exhausts every assignment of the six $A_0$-helpers
to the four candidate blocks.

If one adds an apex $v$ adjacent precisely to the seven Moser vertices,
then $G-N[v]$ is connected, but the resulting graph is only
six-connected: deleting $a,w$ and the four helpers labelled
$2,4,5,6$ isolates the two helpers labelled $w$.  Thus this is not a
counterexample-derived graph.  It proves the exact negative result that
six-connectivity of $H$, a minimal order-six portal separator, the Moser
trace, and a connected sole exterior do not by themselves force the
four-block realization.  The missing full hypothesis is visible: the
duplicate locked portal class creates a six-cut in $G$, which a valid
seven-connected counterexample must repair.

## 6. Full seven-connectivity classifies the order-six adhesion

The repair forced by $\kappa(G)\ge7$ has a sharp consequence.  Continue
with the pure-Moser labels above.  Suppose $(A,B)$ is a separation of
$H=G-v$ with

$$
S=A\cap B=U\mathbin{\dot\cup}\{w\},\qquad
a\in A-S,\qquad b\in B-S,
$$

and $S$ is inclusion-minimal subject to containing $U$ and separating
$a,b$.  Let $R_a$ and $R_b$ be the components of $H-S$ containing
$a,b$, respectively.  Write $\mathcal D_a$ for the components of
$R_a-a$, and define $\mathcal D_b$ symmetrically.

There is no third component of $H-S$.  Such a component contains no
vertex of $N(v)$, so it has no neighbour at $v$, and its entire external
neighbourhood is contained in the six-set $S$.  This would contradict
$\kappa(G)\ge7$.

### Lemma 6.1 (every terminal-side piece is a full seven-shore)

For every $D\in\mathcal D_a$,

$$
N_G(D)=S\cup\{a\},                                   \tag{6.1}
$$

and symmetrically $N_G(D)=S\cup\{b\}$ for
$D\in\mathcal D_b$.

#### Proof

A component $D$ of $R_a-a$ has no neighbour in another such component,
no neighbour in $B-S$, and no neighbour at $v$ because it contains no
vertex of $N(v)$.  Hence $N_G(D)\subseteq S\cup\{a\}$, a set of order
seven.  Its external neighbourhood separates $D$ from $b$ and $v$.
Seven-connectivity therefore gives $|N_G(D)|\ge7$, proving equality.
The other side is identical. $\square$

Both families are nonempty.  For example, if $R_a=\{a\}$, then all
neighbours of $a$ lie in $S\cup\{v\}$.  In the pure Moser boundary $a$
has only three neighbours in $U$, so even the possible edges $aw,av$
give degree at most five, contrary to $\delta(G)\ge7$.

### Lemma 6.2 (four full pieces give an $N$-meeting $K_6$)

If

$$
|\mathcal D_a|+|\mathcal D_b|\ge4,
$$

then $G$ has a $K_7$-minor.

#### Proof

Choose four pieces, including one $a$-side piece $D_0$.  Choose an edge
$pq$ of $G[U]$, and enumerate the other three roots of $U$ as
$u_1,u_2,u_3$.  Assign the three pieces other than $D_0$ bijectively to
these roots.  The six bags

$$
D_0\cup\{a\},\quad D_i\cup\{u_i\}\ (1\le i\le3),
\quad\{p\},\quad\{q\}                                \tag{6.2}
$$

are connected and disjoint.  Every piece sees all of $U$ by Lemma 6.1,
so every shore bag is adjacent to every other shore bag and to the two
singletons.  The last two bags are adjacent by the choice of $pq$.
Thus (6.2) is an $N$-meeting $K_6$-model in $H$; add $\{v\}$.
$\square$

### Lemma 6.3 (three full pieces also give the minor)

If

$$
|\mathcal D_a|+|\mathcal D_b|=3,
$$

then $G$ has a $K_7$-minor.

#### Proof

Suppose first that two pieces $D_1,D_2$ lie on the $a=1$ side and one
piece $E$ lies on the $b=3$ side.  Use the Moser triangle $012$.  The
six bags

$$
D_1\cup\{4\},\quad D_2\cup\{5\},\quad E\cup\{6\},
\quad\{0\},\quad\{1\},\quad\{2\}                    \tag{6.3}
$$

are pairwise adjacent.  The three singleton bags form a triangle.
Every piece sees $0,2$ and every anchored shore sees the other shores'
$U$-anchors.  The two $a$-side pieces see singleton $1$ directly, while
$E\cup\{6\}$ sees it through the Moser edge $16$.

If two pieces lie on the $b=3$ side, use the triangle $034$ and the
bags

$$
D_1\cup\{2\},\quad D_2\cup\{6\},\quad E\cup\{5\},
\quad\{0\},\quad\{3\},\quad\{4\},                   \tag{6.4}
$$

where now $E$ is the $a$-side piece.  The edge $35$ supplies the only
terminal-side check not already supplied by full $U$-attachment.  Thus
either display is an $N$-meeting $K_6$-model, and $\{v\}$ completes it.
$\square$

### Corollary 6.4 (exact order-six residual)

In a counterexample-derived order-six portal separation,

$$
|\mathcal D_a|=|\mathcal D_b|=1.                    \tag{6.5}
$$

Indeed each family is nonempty, while Lemmas 6.2 and 6.3 exclude total
size at least three.

Thus the sharp $|S|=6$ geometry is no longer an arbitrary portal system:
each open terminal side consists of its terminal together with one
connected component, and that component has neighbours at every portal
and at its terminal.  What remains is exactly a bilateral two-shore
splitting problem inside these two connected full shores.  Plain
connectedness cannot split either shore into the four or five disjoint
blocks of Section 2; one-step minor transitions are the next necessary
input.

## 7. The two-vertex shore is impossible

The exact residual can be sharpened from connectivity to an order bound.

### Lemma 7.1 (neither full shore is a singleton)

$$
|D_a|,|D_b|\ge2,
$$

where $D_a,D_b$ are the unique components in Corollary 6.4.

#### Proof

If $D_a$ were a singleton, then $a=1$ would have at most its three
Moser neighbours in $U$, the neighbour $v$, the possible neighbour $w$,
and the one vertex of $D_a$.  Thus $d_G(a)\le6$, contrary to
$\delta(G)\ge7$.  The argument at $b=3$ is symmetric. $\square$

### Lemma 7.2 (a two-vertex shore gives the minor)

Neither $D_a$ nor $D_b$ has order two.

#### Proof

Suppose $D_a=\{d_1,d_2\}$; the two vertices are adjacent because the
shore is connected.  Apart from $D_a$, the neighbours of $a=1$ are its
three Moser neighbours, $v$, and possibly $w$.  The inequality
$d_G(a)\ge7$ therefore forces

$$
aw,ad_1,ad_2\in E(G).                                \tag{7.1}
$$

Each $d_i$ has one neighbour inside $D_a$ and the neighbour $a$.
Its remaining neighbours lie in the six-set $S$.  Minimum degree seven
implies that $d_i$ sees at least five vertices of $S$, so it misses at
most one portal.

Contract the connected opposite shore $D_b$ to one helper vertex.  By
Lemma 6.1 this helper is adjacent to every vertex of $S\cup\{b\}$.
Delete no useful fixed edge, but ignore all optional edges inside $S$
incident with $w$.  We obtain the following finite quotient:

* the fixed pure Moser graph on $N$;
* the portal $w$ and the fixed edge $aw$;
* the edge $d_1d_2$, with each $d_i$ adjacent to $a$ and missing at
  most one of the six portals; and
* one opposite helper complete to $S\cup\{b\}$.

There are exactly

$$
(1+|S|)^2=7^2=49
$$

labelled defect pairs for $d_1,d_2$.  Every one of the 49 quotient
graphs has an explicit $N$-meeting $K_6$-model.  Replacing the opposite
helper by $D_b$ lifts its bag, so the original graph has the same model;
adding $\{v\}$ gives $K_7$.

The discovery file `portal_k2k1_discover.py` archives one model per
defect pair in `portal_k2k1_certificate.json`.  The independent,
dependency-free replay `portal_k2k1_verify.py` regenerates all 49
quotients and checks bag disjointness, boundary contact, connectedness,
and all fifteen bag adjacencies.  It prints

```text
verified 49 K2/K1 defect certificates
```

No SAT solver or graph-minor oracle occurs in the verifier.  This proves
the finite lemma.  The $b$-side case follows by the Moser automorphism
interchanging the two triangles, or by the identical 49-case argument.
$\square$

### Corollary 7.3 (new exact size bound)

Every order-six locked reserved-connector separation satisfies

$$
|D_a|\ge3,\qquad |D_b|\ge3.                          \tag{7.2}
$$

For redundancy, `portal_k2k2_certificate.json` and
`portal_k2k2_verify.py` independently check all $7^4=2401$ four-helper
defect systems when both shores have order two.  Lemma 7.2 is stronger,
because it contracts an arbitrary opposite shore and closes the cell as
soon as either distinguished shore has order two.

## 8. A three-vertex shore must be a triangle

### Lemma 8.1 (no three-vertex path shore)

Neither distinguished shore $D_a,D_b$ is a path on three vertices.

#### Proof

Suppose $D_a=d_1d_2d_3$ is a path.  Every neighbour of a shore vertex
outside the path lies in the seven-set $S\cup\{a\}$.  Hence minimum
degree seven gives

$$
|N_{S\cup\{a\}}(d_1)|,|N_{S\cup\{a\}}(d_3)|\ge6,
\qquad
|N_{S\cup\{a\}}(d_2)|\ge5.                         \tag{8.1}
$$

Lemma 6.1 says that the union of these three neighbourhoods is all of
$S\cup\{a\}$.  Also

$$
4+\mathbf 1_{aw\in E(G)}+|N_{D_a}(a)|\ge7,          \tag{8.2}
$$

because $a$ has exactly three Moser neighbours and the neighbour $v$
outside $D_a\cup\{w\}$.

Contract the arbitrary opposite shore $D_b$ to one helper complete to
$S\cup\{b\}$ and ignore all optional $w$--$U$ edges.  The possible
labelled quotients are exactly the incidence rows satisfying
(8.1), full attachment, and (8.2).  There are 2729 such quotients.  Every
one has an explicit $N$-meeting $K_6$-model.

The discovery program `portal_p3k1_discover.py` archives the models in
`portal_p3k1_certificate.json`.  The independent no-solver verifier
`portal_p3k1_verify.py` regenerates all admissible incidence rows and
checks all branch-set axioms.  Its output is

```text
verified 2729 P3/K1 certificates
```

Replacing the contracted helper by the connected shore $D_b$ lifts the
certificate to $H$, and $\{v\}$ completes a $K_7$-model.  This is a
contradiction.  The $b$-side is symmetric. $\square$

### Lemma 8.2 (no three-vertex triangle shore)

Neither distinguished shore is a triangle.

#### Proof

Suppose $D_a$ is a triangle.  Each of its vertices has two internal
neighbours, so minimum degree gives at least five neighbours in the
seven-set $S\cup\{a\}$.  The three attachment rows collectively cover
that seven-set by Lemma 6.1, and the terminal-degree inequality is again
(8.2).  Contract the arbitrary opposite shore to one full helper.

Up to permuting the three triangle vertices, there are 5051 labelled row
systems satisfying these constraints.  In 5047 cases the quotient has
an explicit $N$-meeting $K_6$-model.  The remaining four row systems are

$$
\begin{split}
&(93,115,115),\qquad(109,115,115),\\
&(115,115,124),\qquad(115,115,125),                 \tag{8.3}
\end{split}
$$

with $aw$ absent.  Here a row is the incidence bit mask on the ordered
labels

$$
(0,2,4,5,6,w,a).
$$

Every exceptional system has two triangle vertices with the identical
row

$$
115=\{0,2,6,w,a\}.                                  \tag{8.4}
$$

Those two adjacent vertices have no neighbour outside their pair except
the third triangle vertex and the five vertices in (8.4).  Their external
neighbourhood therefore has order six and separates the pair from $b,v$
and the opposite shore.  This contradicts $\kappa(G)\ge7$.

The discovery program `portal_k3k1_discover.py` archives the 5047 models
and the four explicit exceptions.  The dependency-free verifier
`portal_k3k1_verify.py` regenerates all 5051 canonical row systems,
checks every model, and checks the repeated five-neighbour row in each
exception.  It prints

```text
verified 5051 canonical K3/K1 cases; four end in a six-cut
```

Thus every triangle attachment system yields either the minor or a
forbidden cut. $\square$

### Corollary 8.3 (new exact size bound)

Every distinguished shore in the order-six reserved-connector residual
has order at least four:

$$
|D_a|\ge4,\qquad |D_b|\ge4.                          \tag{8.5}
$$

## 9. The four-vertex shore is impossible

The same arbitrary-opposite contraction closes the next order, but the
seven-connectivity hypothesis must now be imposed on every proper subset of
the shore rather than only on an exceptional twin pair.

### Lemma 9.1 (local cut inequality)

Let $D$ be either distinguished shore and let
$L=S\cup\{a\}$ on the $a$-side (or $L=S\cup\{b\}$ on the $b$-side).
For every nonempty proper subset $X\subsetneq D$,

$$
\left|N_D(X)-X\right|+
\left|\bigcup_{x\in X}N_L(x)\right|\ge7.             \tag{9.1}
$$

#### Proof

There are no neighbours of $X$ outside $D\cup L$: this is exactly the
one-shore conclusion of Corollary 6.4 and Lemma 6.1.  Thus the two sets
counted in (9.1) form $N_G(X)$.  If their total order were at most six,
$N_G(X)$ would separate the nonempty set $X$ from $v$, the opposite shore,
and the opposite terminal, contrary to $\kappa(G)\ge7$. $\square$

For $X=\{x\}$, (9.1) includes the minimum-degree restriction on a shore
vertex.  For $X=D$, which is deliberately excluded from the statement,
Lemma 6.1 gives the full seven-set $N_G(D)=L$.

### Lemma 9.2 (no four-vertex shore)

Neither $D_a$ nor $D_b$ has order four.

#### Proof

Suppose $|D_a|=4$.  There are six connected unlabelled graphs on four
vertices:

$$
P_4,\quad K_{1,3},\quad C_4,\quad
\text{the paw},\quad K_4-e,\quad K_4.               \tag{9.2}
$$

Fix one such internal graph $F=G[D_a]$.  Encode the neighbours of each
shore vertex in the ordered seven-set

$$
L=(0,2,4,5,6,w,a)                                  \tag{9.3}
$$

by a seven-bit row.  The complete list of necessary restrictions is:

1. a vertex of internal degree $d$ has row weight at least $7-d$;
2. the union of the four rows is all of $L$, by Lemma 6.1;
3. if $\epsilon$ records the optional edge $aw$, then
   $$
   \epsilon+|N_{D_a}(a)|\ge3,                       \tag{9.4}
   $$
   since $a$ has precisely its three Moser neighbours and $v$ outside
   $D_a\cup\{w\}$; and
4. every nonempty proper $X\subsetneq V(F)$ satisfies (9.1).

Contract the arbitrary connected opposite shore $D_b$ to one helper
complete to $S\cup\{b\}$.  Ignore optional edges from $w$ to the roots.
For every attachment system satisfying 1--4, the resulting quotient has an
explicit $N$-meeting $K_6$-model.

Here is the finite certification.  Attachment systems are canonicalized by
the automorphism group of $F$.  There are, in total, $2,820,640$ canonical
systems satisfying 1--4, distributed as follows:

$$
\begin{array}{c|r}
F&\text{canonical systems}\\ \hline
P_4&49,042\\
K_{1,3}&13,750\\
C_4&156,219\\
\text{paw}&360,088\\
K_4-e&1,330,956\\
K_4&910,585
\end{array}                                         \tag{9.5}
$$

The discovery program `portal_k4k1_cegis.py` found a finite family of
monotone model supports for each $F$.  A support consists only of required
shore--portal edges (and possibly $aw$), together with six explicit branch
sets.  Consequently the same branch sets work in every attachment system
containing that support.

The independent, dependency-free program `portal_k4k1_verify.py` performs
two checks without Z3 or a graph-minor oracle.  First, for every archived
support it reconstructs the graph using only the fixed edges and the listed
required edges, and checks disjointness, boundary contact, connectedness and
all fifteen bag adjacencies.  Second, it exhausts every automorphism-canonical
row system satisfying 1--4 and checks that it contains a verified support.
Its output is

```text
p4: verified 49042 canonical cut-free attachment systems
claw: verified 13750 canonical cut-free attachment systems
c4: verified 156219 canonical cut-free attachment systems
paw: verified 360088 canonical cut-free attachment systems
diamond: verified 1330956 canonical cut-free attachment systems
k4: verified 910585 canonical cut-free attachment systems
verified all six order-four shore types (2820640 canonical systems)
```

The archive is `portal_k4k1_cegis_result.json`.  Replacing the contracted
helper in any certified model by the original connected opposite shore lifts
the model to $H$, and adding $\{v\}$ gives a $K_7$-minor.  This contradiction
excludes the $a$-side order-four shore.  The $b$-side is symmetric. $\square$

### Corollary 9.3 (current exact size bound)

Every distinguished shore in the order-six reserved-connector residual has
order at least five:

$$
|D_a|\ge5,\qquad |D_b|\ge5.                          \tag{9.6}
$$

## 10. The five-vertex shore is impossible

The local cut inequality also closes the next order.  Unlike the order-four
case, the independent replay below checks coverage over every *labelled*
attachment system; it does not rely on the lexicographic representatives used
by the discovery search.

### Lemma 10.1 (no five-vertex shore)

Neither distinguished shore (D_a,D_b) has order five.

#### Proof

Suppose (|D_a|=5), and put (F=G[D_a]).  The graph (F) is connected,
so it is one of the 21 connected unlabelled graphs on five vertices.  As in
Section 9, encode the neighbours of every shore vertex in

$$
L=(0,2,4,5,6,w,a)
$$

by a seven-bit row.  If (d_F(x)) denotes its internal degree, every
attachment system obeys all of the following necessary conditions:

1. the row of (x) has weight at least (7-d_F(x));
2. the union of the five rows is all of (L);
3. if (epsilon) records the optional edge (aw), then
   $$
   epsilon+|N_{D_a}(a)|\ge3;
   $$
4. for every nonempty proper (X\subsetneq V(F)),
   $$
   |N_F(X)-X|+
   \left|\bigcup_{x\in X}N_L(x)\right|\ge7.          \tag{10.1}
   $$

The first and third conditions are the degree-seven inequalities, the second
is Lemma 6.1, and the last is Lemma 9.1.  Notice that (10.1) comprises all 30
nontrivial shore-subset inequalities, not only singleton or edge cuts.

Contract the arbitrary connected opposite shore (D_b) to a helper complete
to (S\cup\{b}).  Keep the pure Moser edges, every encoded
(D_a)--(L) edge and the internal edges of (F), but delete the optional
(w)--(U) and (bw) edges.  The resulting quotient has an
(N)-meeting (K_6)-model for every attachment system satisfying 1--4.

Here is an exact finite certificate for the preceding assertion.  The program
`portal_k5k1_cegis.py` regenerates the 21 internal types from their ten-bit
edge masks, imposing connectivity and quotienting by all (5!) relabellings.
For every type it asks symbolically for an attachment system satisfying 1--4
that avoids all model supports found so far.  A model support lists only
required incidence edges (and possibly (aw)) and six explicit branch sets;
it is therefore monotone.  All 21 residual formulas become unsatisfiable.
The archive `portal_k5k1_cegis_result.json` contains 8,928 explicit models,
distributed by the number of internal edges as follows:

$$
\begin{array}{c|rrrrrrr}
|E(F)|&4&5&6&7&8&9&10\\ \hline
\text{models}&358&1,386&2,227&2,496&1,506&647&308.
\end{array}                                         \tag{10.2}
$$

The independent replay `portal_k5k1_verify.py` does not import the discovery
program and uses no graph-minor oracle.  It independently regenerates the 21
types and checks directly, for every archived model, that the six branch sets
are nonempty, pairwise disjoint, connected, meet (N), and have all fifteen
pairwise adjacencies using only the listed support edges and fixed quotient
edges.  It then applies every automorphism of (F) to every verified support
and checks a fresh Boolean formula over *all labelled* row systems.  The base
formula is exactly conditions 1--4, and every support contributes the clause
that at least one of its required edges is absent.  After deleting clauses
subsumed by smaller verified supports there are 27,582 clauses.  For each of
the 21 types the formula is unsatisfiable.  The replay prints

```text
verified all 21 order-five shore types: 8928 models,
27582 irredundant labelled support clauses
```

Thus every possible attachment system contains a verified support.  If the
contracted helper occurs in its model, replace it by the original connected
shore (D_b).  Every helper incidence lifts because Lemma 6.1 makes (D_b)
adjacent to all of (S\cup\{b}); connectedness of (D_b) preserves the
branch set.  Hence (H) has an (N)-meeting (K_6)-model and adjoining
({v}) gives a (K_7)-minor, a contradiction.  The (b)-side follows by
the Moser automorphism interchanging (a) and (b). □

### Corollary 10.2 (strengthened exact size bound)

Every distinguished shore in the order-six reserved-connector residual has

$$
|D_a|\ge6,\qquad |D_b|\ge6.                         \tag{10.3}
$$
