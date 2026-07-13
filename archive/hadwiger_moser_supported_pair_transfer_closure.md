# Closing every mixed support pattern in the pure-Moser two-component cell

## 1. Setup and boundary states

Let $G$ be a proper-minor-minimal counterexample to
$\mathrm{HC}_7$, let $d(v)=7$, and suppose

\[
G-N[v]=C_1\mathbin{\dot\cup}C_2,
\qquad G[N(v)]\cong M,
\]

where

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Use the exact six-colouring obtained from the independent repeated pair
$r=13$.  The five uniquely coloured roots are

\[
U=\{0,2,4,5,6\},
\]

and their missing edges, in cyclic order, are

\[
e_0=05,\quad e_1=25,\quad e_2=24,\quad
e_3=46,\quad e_4=06.                                  \tag{1}
\]

Let $P$ be the disjointness graph of these five edges.  Thus

\[
E(P)=\{02,03,13,14,24\},                              \tag{2}
\]

and $P\cong C_5$.  Put

\[
D_i=\{r,e_i\},\qquad T_{ij}=\{r,e_i,e_j\}
\quad(ij\in E(P)).                                    \tag{3}
\]

Here a displayed set denotes the exact equality partition on $N$:
each listed pair is one colour class and every unlisted boundary vertex
is a singleton.  Let $\mathcal E_s$ be the family of exact boundary
states extending to $G[N\cup C_s]$.

We use three already proved boundary-state facts.

1. **Exclusivity.**  No $D_i$ or $T_{ij}$ lies in both
   $\mathcal E_1$ and $\mathcal E_2$, because equal states glue to a
   six-colouring of $G$.
2. **Two-anchor coverage.**  For every $s\in\{1,2\}$ and every $i$,
   at least one of $D_i$ and the two triples $T_{ij}$ incident with
   $i$ in $P$ lies in $\mathcal E_s$.
3. **One-swap state.**  If $e_i$ is supported only by $C_1$, then
   $D_i\in\mathcal E_2$, and symmetrically with the sides exchanged.

The missing ingredient is the following transfer fact.  It is stronger
than the earlier double-swap rule when a bi-supported edge is present.

## 2. Supported-pair transfer

### Lemma 2.1

Let $ij\in E(P)$.  If $C_s$ supports both $e_i$ and $e_j$, then

\[
T_{ij}\in\mathcal E_{3-s}.                            \tag{4}
\]

### Proof

Write $e_i=ab$ and $e_j=cd$.  In the fixed exact colouring, choose
the $a,b$-bichromatic path $Q_i$ and the $c,d$-bichromatic path
$Q_j$ whose interiors lie in $C_s$.  The four terminal colours are
distinct because $e_i,e_j$ are vertex-disjoint.  Hence $Q_i,Q_j$
are vertex-disjoint.  Their interiors are nonempty because $ab,cd$
are nonedges.

Join their interior vertex sets by a shortest path in the connected
graph $C_s$.  Its internal vertices avoid both $Q_i,Q_j$.  Split the
connector at one edge and assign its two parts to the corresponding
paths.  We obtain disjoint connected sets $H_i,H_j\subseteq C_s$,
adjacent to one another, such that

\[
H_i\cup\{a,b\},\qquad H_j\cup\{c,d\}
\]

are connected.

In a proper minor of $G$, contract the three disjoint connected sets

\[
\{v,1,3\},\qquad H_i\cup\{a,b\},\qquad
H_j\cup\{c,d\},                                      \tag{5}
\]

and delete all remaining vertices of $C_s$.  Let $w$ be the unique
vertex of $U-(e_i\cup e_j)$.  The three contracted images and the
singleton $w$ form a $K_4$: the star image is adjacent to the other
three through $v$; the two path images are adjacent through the split
connector edge; and in the complement of a five-cycle the vertex left
outside two disjoint cycle edges has a neighbour in each edge.

The proper minor is six-colourable.  Restrict that colouring to the
retained copy of $G[N\cup C_{3-s}]$, assigning each boundary vertex the
colour of the contracted image containing it, and discard the contracted
$C_s$-interiors and $v$.  This gives a six-colouring of
$G[N\cup C_{3-s}]$ in which $r,e_i,e_j$ are the three pair classes.
The $K_4$ just exhibited makes these three colours and the colour of $w$
pairwise distinct.  Since those four blocks
partition all seven boundary vertices, there can be no further boundary
equality.  The exact state is $T_{ij}$, proving (4). $\square$

Every contraction in (5) is of a connected set, all three sets are
disjoint, and the proof never uses a boundary root internally on a path.
Thus the transfer has no hidden branch-set overlap.

## 3. Elimination of the five former residual words

Encode support of $e_0,\ldots,e_4$ by $1,2,B$, where $B$ means
support on both sides.  The earlier state and disjoint-bi-support lemmas
left

\[
1112B,\quad1122B,\quad112B2,\quad112BB,\quad121BB.    \tag{6}
\]

We now eliminate them.  Every contradiction below is simply failure of
two-anchor coverage after exclusivity removes all three possible states.

### $1112B$

The edge $e_2$ is supported only by $C_1$, so
$D_2\in\mathcal E_2$.  Its two neighbours in $P$ are $e_0,e_4$,
and both are supported by $C_1$.  Lemma 2.1 gives

\[
T_{02},T_{24}\in\mathcal E_2.
\]

Exclusivity leaves $C_1$ none of $D_2,T_{02},T_{24}$, contrary to
coverage at $e_2$.

### $112BB$

Here $D_1\in\mathcal E_2$.  Both neighbours $e_3,e_4$ of $e_1$
in $P$ are supported by $C_1$, so

\[
T_{13},T_{14}\in\mathcal E_2.
\]

Coverage of $e_1$ on side $1$ is impossible.

### $121BB$

Now $e_1$ is supported only by $C_2$, whence
$D_1\in\mathcal E_1$.  The same two neighbours $e_3,e_4$ are
supported by $C_2$, and Lemma 2.1 gives

\[
T_{13},T_{14}\in\mathcal E_1.
\]

Coverage of $e_1$ on side $2$ is impossible.

### $1122B$

The forced double states are

\[
D_0,D_1\in\mathcal E_2,\qquad
D_2,D_3\in\mathcal E_1.                              \tag{7}
\]

Since $C_1$ supports $e_1,e_4$, transfer gives
$T_{14}\in\mathcal E_2$.  Since $C_2$ supports $e_2,e_4$, it gives
$T_{24}\in\mathcal E_1$.

Coverage of $e_1$ on side $1$, using (7), forces
$T_{13}\in\mathcal E_1$.  Coverage of $e_2$ on side $2$ forces
$T_{02}\in\mathcal E_2$.  Coverage of $e_0$ on side $1$ then
forces $T_{03}\in\mathcal E_1$.  But side $2$ now has none of

\[
D_3,T_{03},T_{13},
\]

contrary to coverage at $e_3$.

### $112B2$

We have

\[
D_0,D_1\in\mathcal E_2,\qquad D_2,D_4\in\mathcal E_1.
\]

The component $C_1$ supports $e_0,e_3$, so
$T_{03}\in\mathcal E_2$.  Coverage of $e_0$ on side $1$ therefore
forces $T_{02}\in\mathcal E_1$.  Also $C_2$ supports $e_2,e_4$,
so $T_{24}\in\mathcal E_1$.  Side $2$ is consequently left none of

\[
D_2,T_{02},T_{24},
\]

contrary to coverage at $e_2$.

This proves that all five words in (6) are impossible.

## 4. Closure of the full two-component pure-Moser cell

The pentagon boundary-state lemma already eliminates

\[
11112,\ 11122,\ 11212,\ 1121B,\ 1212B,
\]

and the disjoint-bi-support lemma eliminates

\[
11B2B,\ 12B1B,\ 12BBB,\ 1B2BB.
\]

Section 3 eliminates the remaining five orbit representatives.  Hence
no genuinely mixed support word exists.  If a support word is not
genuinely mixed, one exterior component supports all five edges of the
missing $C_5$.  Kriesell--Mohr's pseudoforest construction then gives
a rooted $K_5$-model on $U$ contained in that side: the five
certificate edges supply the missing-cycle adjacencies and $M[U]$
supplies their complement.  The other full-attachment exterior component
together with $\{1,3\}$ is a connected sixth bag adjacent to every
rooted bag.  Adding $\{v\}$ gives a $K_7$-minor.

We have therefore proved:

### Theorem 4.1

In a proper-minor-minimal counterexample to $\mathrm{HC}_7$, a
degree-seven vertex whose neighbourhood is the pure Moser spindle cannot
have two exterior components.

The dependency-free script
`moser_supported_pair_transfer_verify.py` assigns every specialized
state to side $1$, side $2$, or neither, enforces exclusivity,
two-anchor coverage, one-swap states, and Lemma 2.1, and independently
checks that all fourteen genuinely mixed support orbits are infeasible.
The displayed propagation arguments, not the script, prove the five new
cases.

### Remark 4.2 (the transfer is not assumed on every side)

Some mixed words have a side with no two vertex-disjoint supported
pentagon edges.  In the displayed orbit convention, side $2$ has this
property in $11112$, $11122$, and $1112B$: its support indices are,
respectively, $\{4\}$, $\{3,4\}$, and $\{3,4\}$, while $e_3,e_4$
share a root.  Thus the proof does not assume a paired linkage on both
sides.  Lemma 2.1 is applied only where a disjoint supported pair really
exists; coverage and exclusivity propagate the resulting state to the
side with no such pair.

## 5. Consolidated degree-seven two-exterior corollary

The audited seven-vertex atlas classification can be stated in the exact
form needed here: among the $107$ seven-vertex graphs $J$ with
$\alpha(J)\le2$, all but the pure Moser spindle and its relevant
one-edge extension contain a $K_4$-model using at most five vertices
such that two unused vertices are adjacent.  For such a model, anchor the
two full-attachment exterior components at those adjacent unused roots.
The four old bags and the two anchored exterior bags form an
$N(v)$-meeting $K_6$-model, and $\{v\}$ completes a $K_7$-model.

The one-edge Moser extension is excluded by the earlier two-anchor
colour-gluing lemma.  Theorem 4.1 excludes the pure Moser spindle.
Consequently, subject to the installed finite neighbourhood
classification, we obtain:

### Corollary 5.1

In a proper-minor-minimal counterexample to $\mathrm{HC}_7$, if
$d(v)=7$, then $G-N[v]$ cannot have exactly two components.

The dependency-free script `degree7_neighborhood_labeled_verify.py`
exhausts all $2^{21}$ labelled graphs on seven vertices.  It finds
$133{,}501$ labelled graphs with independence number at most two, and
checks that the exact failures of the usable "two adjacent unused
anchors" certificate are the two complete isomorphism orbits of the
Moser spindle and $M+13$: respectively $630$ labelled graphs with
$11$ edges and $2{,}520$ with $12$ edges.  The independent NetworkX-atlas
cross-check `degree7_neighborhood_classification_audit.py` gives the same
two unlabelled exceptions.
