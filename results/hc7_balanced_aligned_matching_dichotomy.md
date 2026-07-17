# Aligning the balanced matching with a prescribed missing clique contact

**Status:** written proof with a separate GREEN internal audit in
[`hc7_balanced_aligned_matching_dichotomy_audit.md`](hc7_balanced_aligned_matching_dichotomy_audit.md).
This note refines the cross-pair matching normalization and, under the support-at-most-six
proper-deletion response, eliminates the exact Hall obstruction to forcing
the matching edge incident with `x` to use a prescribed clique vertex.  It
leaves the matching-aligned colouring/linkage branch and does not prove
`HC_7`.

## 1. An exact colourful-matching dichotomy

### Theorem 1.1

Let

\[
 S=R\mathbin{\dot\cup}A\mathbin{\dot\cup}B
       \mathbin{\dot\cup}\{x\},
 \qquad |R|=3,\quad |A|=|B|=2,
\]

and let `F` be a graph on `S`.  Assume that

1. `R` is independent in `F`;
2. `F[A]` and `F[B]` have no edges, while `F` contains every edge between
   `A` and `B`; and
3. for each of `A` and `B`, the two endpoint neighbourhoods in `R` are
   nonempty and disjoint.

Fix `r in R` with `xr in E(F)`.  Then exactly one of the following holds.

1. `F` has a perfect matching containing `xr` and an `A`--`B` edge.
2. Some vertex `p in R-{r}` has

   \[
                    N_F(p)\cap(A\cup B)=\varnothing.   \tag{1.1}
   \]

If `F` has at least one perfect matching, outcome 2 has the additional
consequences

\[
                    N_F(p)=\{x\},                     \tag{1.2}
\]

relative to the boundary `S`, and every perfect matching of `F` contains
the edge `px`.

### Proof

Write `R-{r}={p,q}`.  After fixing the edge `xr`, a perfect matching of
`F` must match `p,q` to two endpoints, one in `A` and one in `B`; the two
remaining endpoints then form the required `A`--`B` edge.  Conversely,
any such choice gives a perfect matching because all `A`--`B` edges are
present.  Thus outcome 1 holds exactly when

\[
\begin{split}
 &\bigl(N_F(p)\cap A\ne\varnothing
       \text{ and }N_F(q)\cap B\ne\varnothing\bigr),\quad\text{or}\\
 &\bigl(N_F(p)\cap B\ne\varnothing
       \text{ and }N_F(q)\cap A\ne\varnothing\bigr).  \tag{1.3}
\end{split}
\]

Suppose (1.3) fails and neither `p` nor `q` satisfies (1.1).  If, say,
`p` had neighbours in both `A` and `B`, failure of the first line of
(1.3) would make `q` have no neighbour in `B`, while failure of the second
would make it have no neighbour in `A`, contrary to the supposition.
Hence each of `p,q` has endpoint neighbours in exactly one of the two
sets `A,B`.  If these two sets were different, one line of (1.3) would
hold.  They are therefore the same; after interchanging `A,B`, both
`p,q` have no neighbour in `B`.

But the two endpoint neighbourhoods of `B` in `R` are nonempty and
disjoint.  If neither endpoint sees `p` or `q`, both nonempty
neighbourhoods would be subsets of the singleton `{r}`, which is
impossible.  This proves that failure of outcome 1 forces outcome 2.  The
two outcomes are mutually exclusive because, after deleting `x,r`, the
vertex `p` in (1.1) is isolated.

Finally assume that `F` has a perfect matching and (1.1) holds.  The
vertex `p` has no neighbour in `R` because `R` is independent and no
neighbour among the four endpoints by (1.1).  It must therefore be
adjacent to `x`, and that is its only boundary neighbour.  Every perfect
matching consequently contains `px`, proving (1.2). \(\square\)

## 2. The forced theta remainder

Let `J=overline F`.  In outcome 2 of Theorem 1.1, write

\[
                    R=\{p,r,q\}.
\]

### Corollary 2.1

Assume that `F` has a perfect matching.  Then `p` is adjacent in `J` to
every vertex of `S-{p,x}` and nonadjacent to `x`.  Moreover the six-vertex
graph

\[
                     J[S-\{p,x\}]                     \tag{2.1}
\]

is the union of the edge `rq` and two internally vertex-disjoint paths of
length three from `r` to `q`, one with internal vertices `A` and the other
with internal vertices `B`.  In particular, it is triangle-free.

### Proof

Equation (1.2) says that `px` is the only `F`-edge incident with `p`, which
gives the first assertion after taking complements.

Neither endpoint neighbourhood in `R` contains `p`.  For either of the
two sets `A,B`, its endpoint neighbourhoods are nonempty disjoint subsets
of the two-element set `{r,q}`.  They are therefore the complementary
singletons `{r}` and `{q}`.  In `J`, its two endpoints form an edge and,
after orienting them, give a path of length three from `r` to `q`.  There
is no edge of `J` between `A` and `B`, while `rq` is an edge because `R`
is independent in `F`.  These are exactly the edges in (2.1), proving the
theta description. \(\square\)

## 3. A uniform two-reserved-vertex anchoring theorem

### Theorem 3.1

Let `k>=3`, let `G` be a `k`-connected graph, and let `S` be a vertex set
of order `k+1` such that `G-S` has exactly two connected components `U,V`,
both adjacent to every vertex of `S`.  Let `p,x` be distinct vertices of `S`,
and suppose

\[
                    p\text{ is adjacent to every vertex of }
                    S-\{p,x\}.                        \tag{3.1}
\]

If `G-{p,x}` contains a `K_{k-2}`-minor model of support order at most
`k-1` which is disjoint from `V`, then `G` contains a `K_k` minor or has
an actual order-`k` separation.

### Proof

Write the `k-2` branch sets as `M_1,...,M_{k-2}`, put

\[
                       m=\left|\bigcup_iV(M_i)\right|\le k-1,
                       \qquad B=S-\{p,x\},
\]

and let `I` index the branch sets disjoint from `B`; put `h=|I|`.

If `h>0`, choose one vertex `a_i in M_i` for every `i in I`, and define

\[
 A_0=\{a_i:i\in I\},\qquad
 Z=\left(\bigcup_iV(M_i)-A_0\right)\cup\{p,x\},\qquad
 T=B-\bigcup_iV(M_i).                                \tag{3.2}
\]

The sets are pairwise disjoint and

\[
                       |Z|=m-h+2.                     \tag{3.3}
\]

At most `m-h` vertices of `B` belong to the old support, because every
branch set indexed by `I` avoids `B`.  Hence

\[
                       |T|\ge(k-1)-m+h\ge h.          \tag{3.4}
\]

If `G-Z` has no `h` pairwise vertex-disjoint `A_0`--`T` paths, set-Menger
gives an `A_0`--`T` separator `X` of order at most `h-1`.  Both terminal
sets retain a vertex after deleting `X`, and

\[
                       |Z\cup X|\le m+1\le k.         \tag{3.5}
\]

An order below `k` contradicts `k`-connectivity; equality `k` gives an
actual order-`k` separation, one of the conclusions.  This really is an
actual separation: after deleting `Z union X`, a vertex of `A_0-X` and a
vertex of `T-X` remain in different components.

Otherwise choose the `h` disjoint paths and stop them on their first visits
to `B`.  Their first boundary vertices lie in `T`, because `p,x` and every
old model vertex outside `A_0` belong to `Z`.  Before that first visit the
paths stay in `U`: their selected starts lie in boundary-disjoint branch
sets, the model avoids `V`, and passage from `U` to `V` meets `S`, where
`p,x` are deleted and every other vertex belongs to `B`.  Enlarge each
branch set indexed by `I` along its stopped path.  The `k-2` branch sets
remain disjoint, preserve their labels and old adjacencies, avoid `V`, and
now each contains a distinct vertex of `B`.

When `h=0`, no linkage is needed and the original `k-2` branch sets already
have this property.  In either case the `k` sets

\[
                       M_1,\ldots,M_{k-2},\qquad
                       V(V)\cup\{x\},qquad \{p\}      \tag{3.6}
\]

(using the enlarged `M_i` where necessary) form a `K_k`-minor model.  The
set `V union {x}` is connected by boundary fullness.  It is adjacent to
each `M_i` through that row's vertex of `B`, while `{p}` is adjacent to
each `M_i` by (3.1).  Finally `V` has a neighbour at `p`, so the last two
sets are adjacent.  This proves the theorem. \(\square\)

### Corollary 3.2 (the forced branch is genuinely mixed-shore)

Continue with outcome 2 of Theorem 1.1 and Corollary 2.1.  Suppose `G` has
the full order-eight separation on `S`, has neither a `K_7` minor nor an
actual order-seven separation, and every two-vertex deletion contains a
`K_5`-minor model of support order at most six.  Then every minimum
support model in `G-{p,x}` meets both open components, and at least one
open component meets two distinct branch sets.

Consequently its support has order six.  After orienting the two open
components, its branch sets have the form

\[
 \{u_1\},\ldots,\{u_h\},\quad
 \{w_1\},\ldots,\{w_{4-h}\},\quad \{v,t\},           \tag{3.7}
\]

where `2<=h<=3`, the `u_i` lie in one open component, `v` lies in the
other, and `t,w_j` lie in `S-{p,x}`.  Moreover `t` is nonadjacent to at
least one of the vertices `w_j`.

### Proof

Theorem 3.1, applied in either orientation, excludes a model avoiding one
open component.  If each open component met at most one branch set, each
could be enlarged inside that branch set and contracted without merging
two labels.  This would give a support-at-most-six `K_5` model in the
quotient obtained by contracting the two open components and deleting
`p,x`.  Corollary 2.1 identifies its six-vertex boundary as the theta
graph.  The audited quotient-support theorem in
[`../results/hc7_endpoint_rigid_gallai_exchange.md`](../results/hc7_endpoint_rigid_gallai_exchange.md),
Theorem 4.2, excludes such a model.  Thus one open component meets at least
two branch sets.

A support-five model has only singleton branch sets and cannot meet both
anticomplete open components, so the support order is six.  There is one
two-vertex branch set and four singleton branch sets.  Orient the
components so that the first contains at least two branch sets.  At least
one of them is a singleton.  The only branch set which can meet the other
component and remain adjacent to that singleton is the two-vertex branch
set; connectivity forces it to have the form `{v,t}` with `v` in the
opposite component and `t in S-{p,x}`.  All branch sets in the first open
component are singletons; the remaining singleton branch sets lie on the
boundary.  This gives (3.7) with `2<=h<=4`.

If `h=4`, adjacency of `{v,t}` to the four open-side singletons is supplied
entirely by `t`, because the two open components are anticomplete.  Those
five vertices form a support-five `K_5` in `G-{p,x}`, contradicting
minimality of the chosen support-six model.  Hence `h<=3`.

Finally `t` is adjacent to every `u_i`, again because the opposite open
components are anticomplete.  If it were also adjacent to every `w_j`,
then `t` together with the four singleton branch-set vertices would be a
support-five `K_5` model, the same contradiction. \(\square\)

## 4. Elimination of the forced-theta alternative

The extra reserved vertex in Theorem 3.1 allows the mixed-shore completion
chain to be run with one unit less connectivity slack.  Every failed
linkage then returns an actual order-seven separation.

### Lemma 4.1 (common-neighbour completion)

Let $G$ be a $k$-connected graph, let $a,b$ be adjacent vertices, and let
$W$ be a set of at least $k-1$ common neighbours of $a,b$.  If
$G-\{a,b\}$ contains a $K_{k-2}$-minor model of support order at most
$k-1$, then $G$ contains a $K_k$ minor or has an actual order-$k$
separation.

### Proof

Let the model support have order $m\le k-1$, and let $h$ branch sets miss
$W$.  Retain one root in each such branch set, delete the other $m-h$
support vertices together with $a,b$, and link the $h$ roots to the
unused vertices of $W$.  There are at least

\[
                    (k-1)-(m-h)\ge h
\]

available targets.  If the linkage fails, Menger gives a separator of
order at most

\[
                    (m-h)+2+(h-1)=m+1\le k.
\]

Both terminal sets retain a vertex.  Thus order below $k$ contradicts
$k$-connectivity and equality gives an actual order-$k$ separation.
If the linkage exists, stop the paths at their first visits to $W$ and
enlarge the corresponding branch sets.  All $k-2$ branch sets now meet
distinct vertices of $W$, so adjoining the singleton branch sets
$\{a\},\{b\}$ gives a $K_k$-minor model.  The case $h=0$ starts at this
last sentence. \(\square\)

### Theorem 4.2 (forced-theta completion)

Let $G$ be seven-connected and let $S$ be an eight-vertex set such that
$G-S$ has exactly two connected components $U,V$, each adjacent to every
vertex of $S$.  Let $p,x\in S$, put

\[
                         B=S-\{p,x\},
\]

and suppose that $p$ is adjacent to every vertex of $B$.  Assume also:

1. every two-vertex deletion of $G$ contains a $K_5$-minor model of
   support order at most six;
2. $G-\{p,x\}$ has a minimum-support model with branch sets

   \[
     \{u_1\},\ldots,\{u_h\},
     \quad\{w_1\},\ldots,\{w_{4-h}\},
     \quad\{v,t\},                                   \tag{4.1}
   \]

   where $2\le h\le3$, all $u_i$ lie in $U$, $v$ lies in $V$, and
   $t,w_j$ lie in $B$; and
3. $t$ is nonadjacent to at least one $w_j$.

Then $G$ contains a $K_7$ minor or has an actual order-seven separation.

### Proof

Write $M$ for the six support vertices in (4.1).

#### Step 1: the opposite open component is not a singleton

Suppose $V=\{v\}$.  Boundary fullness makes $v$ adjacent to every vertex
of $S$, so $p,v$ are adjacent and have the six common neighbours $B$.
By hypothesis, $G-\{p,v\}$ has a support-at-most-six $K_5$ model.
Lemma 4.1 with $k=7$ gives the conclusion.  We may therefore assume
$V-v$ is nonempty.

#### Step 2: exact contacts of components of $V-v$

Fix a component $C$ of $V-v$.  Connectedness of $V$ and the absence of
edges to $U$ or to another component of $V-v$ give

\[
                         N_G(C)=\{v\}\cup N_S(C).
                                                               \tag{4.2}
\]

Hence $|N_S(C)|\ge6$.  Equality makes $N_G(C)$ an actual order-seven
separator, with $C$ and $U$ on nonempty opposite sides.  Assume therefore
$|N_S(C)|\ge7$.

Put

\[
 F_0=\{p,t,w_1,\ldots,w_{4-h}\},\qquad
 A_0=\{u_1,\ldots,u_h\}.                              \tag{4.3}
\]

We claim that $F_0\subseteq N_S(C)$ gives one of the two conclusions.
Delete

\[
                  Z=(M-A_0)\cup\{p,x\},
\]

so $|Z|=8-h$, and use as targets

\[
                  T=(N_S(C)\cap B)-\{t,w_1,\ldots,w_{4-h}\}.
                                                               \tag{4.4}
\]

The set $F_0$ has order $6-h$.  At least $h+1$ contacts of $C$ lie
outside $F_0$, and at most one of them is the unsafe vertex $x$.
Thus $|T|\ge h$.  If there are no $h$ disjoint $A_0$--$T$ paths in
$G-Z$, a Menger separator of order at most $h-1$, together with $Z$,
is an actual order-seven separator (or has smaller order, contradicting
seven-connectivity).

Otherwise stop such paths at their first visits to $T$.  They do not
enter $C$ first: by (4.2), all entrances other than $T$ belong to $Z$.
Enlarge the $u_i$ branch sets along the stopped paths.  The five model
branch sets, $C$, and $\{p\}$ form a $K_7$-minor model.  Each old row
meets $B$, hence is adjacent to $p$; it is adjacent to $C$ through its
new terminal or through $t,w_j$; and $C$ is adjacent to $p$.

It follows that, in the absence of either conclusion, every component of
$V-v$ sees exactly seven boundary vertices and its unique missed vertex
lies in $F_0$.

#### Step 3: no component misses $t$

Suppose $N_S(C)=S-\{t\}$.  Delete

\[
                  Z=\{w_1,\ldots,w_{4-h},v,t,p,x\},
\]

of order $8-h$, and use

\[
                  T=B-\{t,w_1,\ldots,w_{4-h}\},
\]

which has order $h+1$.  The same Menger count gives either an actual
order-seven separation or $h$ disjoint paths from the $u_i$ to distinct
vertices of $T$.  Stop them on their first visits to $T$.  All other
entrances to $C$ are in $Z$, so the stopped paths avoid $C$.

After enlarging the $u_i$ rows, let $R_1,\ldots,R_4$ denote them together
with the unchanged singleton rows $\{w_j\}$.  Then

\[
             R_1,R_2,R_3,R_4,\quad \{v,t\},\quad C,\quad\{p\}
                                                               \tag{4.5}
\]

is a $K_7$-minor model.  The first five sets retain the old model
adjacencies; $C$ sees every row through its boundary vertex and meets
$\{v,t\}$ through $v$; while $p$ sees every row through $B$, sees
$\{v,t\}$ through $t$, and sees $C$.  Thus every surviving component
misses one of

\[
                         \{p,w_1,\ldots,w_{4-h}\}.     \tag{4.6}
\]

#### Step 4: the missed boundary vertex is common

First let $h=3$ and write $w=w_1$.  If components $C_p,C_w$ miss $p,w$,
respectively, delete

\[
                       Z=\{w,v,t,p,x\},\qquad
                       T=B-\{w,t\}.
\]

Here $|Z|=5$ and $|T|=4$.  Failure of three disjoint paths from
$\{u_1,u_2,u_3\}$ to $T$ gives an actual order-seven separation.
Otherwise stop the paths on their first visits to $T$ and enlarge the
three singleton rows to $R_1,R_2,R_3$.  The seven sets

\[
 R_1,R_2,R_3,\quad
 C_p\cup\{w\},\quad\{t\},\quad C_w\cup\{v\},\quad\{p\} \tag{4.7}
\]

form a $K_7$-minor model.  The six pairs among the last four sets use,
respectively, a $C_p$--$t$ edge, a $C_p$--$v$ edge, $wp$, $tv$, $tp$,
and a $C_w$--$p$ edge.  Each $R_i$ meets the other four sets through the
old edges to $w,t$, its terminal contact with $C_w$, and its terminal
edge to $p$.  Therefore all components have one common missed vertex
when $h=3$.

For $h=2$, suppose distinct components $C,D$ miss distinct vertices
$y,z\in\{p,w_1,w_2\}$.  Delete

\[
              Z=\{p,x,t,w_1,w_2,v\},\qquad
              T=B-\{t,w_1,w_2\}.
                                                               \tag{4.8}
\]

Now $|Z|=6$ and $|T|=3$.  Failure of two disjoint paths from
$\{u_1,u_2\}$ to $T$ gives an actual order-seven separation.  Otherwise
stop the paths at distinct terminals $\alpha,\beta\in T$, enlarge the
two rows to $R_1,R_2$, and choose

\[
                           r\in T-\{\alpha,\beta\}.    \tag{4.9}
\]

For $b\in\{p,w_1,w_2\}$ define

\[
                     L(b)=\{e\in\{v,t\}:eb\in E(G)\}. \tag{4.10}
\]

Every $L(b)$ is nonempty: $pt$ is an edge, and the old edge row is
adjacent to each $w_j$.  If $L(y),L(z)$ have distinct representatives
$e_C,e_D$, then

\[
 R_1,R_2,\ C\cup\{e_C\},\ D\cup\{e_D\},\
 \{p\},\{w_1\},\{w_2\}                                \tag{4.11}
\]

are seven clique branch sets.  Each component supplies the two boundary
contacts it does not miss, its assigned endpoint supplies the missed one,
and the two enlarged component sets meet through $v$ and $t$.

If no distinct representatives exist, then
$L(y)=L(z)=\{e\}$.  When $e=v$, the edge $pt$ forces
$\{y,z\}=\{w_1,w_2\}$; orienting $C,D$ by their missed vertices, use

\[
 R_1,R_2,\ C,\ \{t\},\ \{p\},\ D\cup\{r\},\ \{v,w_2\}.
                                                               \tag{4.12}
\]

When $e=t$, hypothesis 3 rules out $\{y,z\}=\{w_1,w_2\}$.
After relabelling, let $C$ miss $p$, let $D$ miss $w_2$, and let $t$
miss $w_1$.  Then use

\[
 R_1,R_2,\ C,\ \{w_1\},\ \{w_2\},\
 D\cup\{t\},\ \{p,r\}.                                \tag{4.13}
\]

For completeness, here are the ten pairs among the last five sets in
each Hall obstruction.  In (4.12) they are witnessed by

\[
 Ct,\ Cp,\ Cr,\ Dt,\ Dp,\ Cv,\ tv,\ tp,\ pw_2,\ Dv .
\]

In (4.13) they are witnessed by

\[
 Cw_1,\ Cw_2,\ Ct,\ Cr,\ w_1w_2,\ Dw_1,\ tw_2,\
 pw_1,\ pw_2,\ tp .
\]

The two rows $R_1,R_2$ remain adjacent to one another.  Their old edges
to $t,w_1,w_2$, their distinct terminal contacts with both components,
and the edges from their terminals to $p$ give the other eleven pairs.
Thus all 21 adjacencies hold in both displays.  This is the audited
two-defect exchange with the universal vertex there replaced by $p$ and
the extra vertex $x$ included in $Z$.  Every former use of universality is
an edge from $p$ to a vertex of $B$, which is available here; no edge
$px$ is used.  Thus different missed vertices also give a conclusion
when $h=2$.

We have proved that every component of $V-v$ misses one common vertex

\[
                       y\in\{p,w_1,\ldots,w_{4-h}\}.   \tag{4.14}
\]

#### Step 5: the shifted side is connected

If $V-v$ has two components, set

\[
                           S'=\{v\}\cup(S-\{y\}).
\]

Both components are adjacent to every vertex of the order-eight set $S'$,
and the support-six model (4.1) avoids both.  The uniform two-full-component
completion theorem, Theorem 1.1 of
[the shifted-boundary completion note](../results/hc7_shifted_boundary_completion.md),
gives a $K_7$ minor.  Hence, absent the conclusions, $X=V-v$ is connected.

#### Step 6: final boundary anchoring

Suppose first that $y\ne p$.  Then $y=w_j$ for some $j$.  Put

\[
                  W=B-\{y\},\qquad
                  A_0=\{u_1,\ldots,u_h,y\}.
\]

The $h+1$ entries of $A_0$ represent exactly the branch sets of (4.1)
which miss $W$.  Delete

\[
                  Z=(M-A_0)\cup\{p,x\},
\]

of order $7-h$, and use the $h+1$ vertices of $W-M$ as targets.  If the
corresponding linkage fails, a separator of order at most $h$, together
with $Z$, gives an actual order-seven separation.  If it exists, stop it
on first visiting $W$.  The stopped paths avoid $X$: the vertex $v$ and
the boundary vertices $p,x$ are deleted, $X$ misses $y$, and every other
boundary entrance is a deleted model vertex or a target in $W$.

Enlarge the represented branch sets.  All five model rows now meet
distinct vertices of $W$.  These five rows, $X$, and $\{p\}$ form a
$K_7$ model: both $X$ and $p$ are adjacent to every row through $W$, and
$X$ is adjacent to $p$ because it misses only $y$.

Finally suppose $y=p$.  Delete

\[
            Z=(M-\{u_1,\ldots,u_h\})\cup\{p,x\},
\]

of order $8-h$, and link the $h$ vertices $u_i$ to unused vertices of
$B$.  There are exactly $h+1$ targets.  Linkage failure again gives an
actual order-seven separation; otherwise stop and enlarge the $u_i$
rows.  The five model rows now use five distinct vertices of $B$.  Choose
the unused vertex $z\in B$.  The five rows,

\[
                         X\cup\{z\},\qquad\{p\}
\]

are seven clique branch sets: $X$ sees all of $B$, $p$ is complete to
$B$, and $pz$ joins the last two sets.  This exhausts (4.14) and proves
the theorem. \(\square\)

### Corollary 4.3 (the Hall obstruction is eliminated)

Under the full hypotheses of Corollary 3.2, outcome 2 of Theorem 1.1 is
impossible in a graph with neither a $K_7$ minor nor an actual order-seven
separation.  Consequently the cross-pair perfect matching can be chosen
to contain $xr$, where $r$ is the prescribed vertex missed by both $x$
and the connected leaf-side interior.

### Proof

Corollary 3.2 supplies the model (4.1) and its missing $t$--$w_j$ edge.
Theorem 4.2 then gives a $K_7$ minor or an actual order-seven separation,
contrary to the hypotheses.  Theorem 1.1 therefore has outcome 1.
\(\square\)

## 5. Exact consequence and remaining host-level gap

The audited cross-pair normalization supplies a perfect matching with an
$A$--$B$ edge.  Its independently audited shared-contact corollary
supplies a vertex $r in R$ missed by both $x$ and the connected leaf-side
interior; in complement notation, $xr in E(F)$.  Corollary 4.3 proves that,
under the compact-model response and in the absence of the two terminal
outcomes, the perfect matching can be chosen to contain both $xr$ and an
$A$--$B$ edge.

This eliminates the Hall obstruction as an unbounded host family.  It is
not a proof of the balanced order-eight branch.  The exact surviving
problem is now the aligned branch: convert this particular four-pair
independent partition of $S$ into one of the following host-level objects:

1. compatible closed-shore colourings with that same literal boundary
   partition, which glue to a six-colouring of $G$;
2. the two disjoint connected subgraphs required by the promoted
   split-edge completion, giving a $K_7$ minor; or
3. an actual order-seven separation preserving the two defect edges and
   the named clique vertices.

The perfect matching alone gives none of these.  In the edge-critical
formulation, one must still show that a nontrivial Kempe component yields
the split-edge linkage, or that a proper-minor operation in the opposite
shore returns the matching-aligned boundary partition.  This is the exact
remaining palette-to-labelled-model gap; the forced-theta mixed-shore
alternative is no longer part of it.
