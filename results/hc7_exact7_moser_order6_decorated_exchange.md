# Exact-order-six decorated Moser exchange

**Status:** proved and independently audited.  This theorem is conditional
on the literal order-six connector adhesion below; no reduction of an
arbitrary rooted-model separator to this cell is claimed.

## 1. Exact cell

Let `G` be seven-connected, `K_7`-minor-free, not six-colourable, and assume
every proper minor is six-colourable.  Let `v` have the pure-Moser
neighbourhood

\[
 S=\{0,1,2,3,4,5,6\},\qquad
 E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Put

\[
 a=1,\quad b=3,\quad U=\{0,2,4,5,6\},
 \quad T=U\mathbin{\dot\cup}\{w\}.
\]

Assume `H=G-v` has a literal separation with adhesion `T`, with `a` and
`b` on opposite open sides.  In the exact cell, each terminal side has one
connected open shore `D_t`, where

\[
 N_G(D_a)=T\cup\{a\},\qquad
 N_G(D_b)=T\cup\{b\}.                              \tag{1.1}
\]

The two shores are anticomplete.  This is the exact-order-six specialization
of the connector separator; it is a hypothesis here.

## 2. Supported frames and admissible decoration

The nonedges of `G[U]` form a five-cycle.  A frame `(e,f;r)` consists of
two disjoint edges `e,f` of that missing cycle and the remaining root `r`.
A supported frame core on one closed terminal side consists of three
disjoint connected pairwise adjacent sets

\[
                         E,F,R,                      \tag{2.1}
\]

avoiding the side terminal and having literal adhesion traces `e,f,{r}`.
A crossed frame supplies such a core: its two portal paths realize `e,f`,
while the present complementary cycle supplies the three required block
adjacencies.

Let `W` be connected, disjoint from the core and the side terminal, with
`W cap T={w}`.  A root-block decoration `w->K`, for
`K in {E,F,R}`, is **supported** when

1. `W` is adjacent to `K`; and
2. `{w} union (K cap T)` is independent.

The second condition is essential: geometric contact alone does not make a
legal equality block.  The singleton decoration `w->*` is supported when
`W` is adjacent to all three core blocks and to the side terminal.

### Theorem 2.1 (bilateral decorated overlap)

Suppose the same labelled frame has supported cores on both terminal sides.
Then `G` is six-colourable in each of the following cases.

1. Both sides support the same root-block decoration.
2. One side supports `w->*` and the other supports any root-block
   decoration.
3. Both sides support `w->*`.

### Proof

In case 1, both sides realize the same partition of `T` into the three
independent blocks `e,f,{r}`, with `w` adjoined to the common decorated
block.  Their connected realizations are pairwise adjacent.  The audited
bilateral portal-transfer theorem therefore contracts them on opposite
sides, returns the same exact equality state, aligns the two palettes, and
six-colours `G`.

In case 2, the singleton side can merge `W` into the requested admissible
core block.  Connectivity and all other block adjacencies survive, reducing
to case 1.

In case 3, each side realizes the four independent traces
`e,f,{r},{w}`.  The portal-only block is adjacent to all core blocks and to
the side terminal, so the portal-only form of bilateral transfer applies.
Again the exact states align and six-colour `G`. `square`

## 3. Literal portal restrictions

### Lemma 3.1

In the exact cell,

\[
                             wa,wb\notin E(G).         \tag{3.1}
\]

### Proof

If `wa` were an edge, the following seven sets would be disjoint connected
pairwise adjacent branch sets:

\[
 \{0\},\ \{a\},\ \{2\},\ \{b,5,6\},\ \{v,4\},
 \ D_a,\ D_b\cup\{w\}.                              \tag{3.2}
\]

The first three form triangle `012`.  The Moser edges give every adjacency
among the first five bags.  Fullness in (1.1) supplies all incidences with
`D_a,D_b`, and `wa` makes the last bag see `{a}`.  Thus (3.2) is a literal
`K_7`, a contradiction.  The Moser automorphism interchanging
`a,b`, `2,4`, and `6,5` proves the `wb` case. `square`

## 4. Admissible rank and its exact failure certificate

Fix a supported core on one terminal shore `D`.  Delete its open-shore
vertices.  Let `K_w` be the union of the remaining components having a
neighbour at `w`, and put `W_w={w} union K_w`.  Define

\[
 \begin{aligned}
 \tau_D(w)&=\{K\in\{E,F,R\}:E(W_w,K)\ne\varnothing\},\\
 \sigma_D(w)&=\{K\in\tau_D(w):
                 \{w\}\cup(K\cap T)\text{ is independent}\}.
 \end{aligned}                                      \tag{4.1}
\]

Thus `sigma` records supported **admissible** decorations, not merely raw
bridge contacts.

### Corollary 4.1 (rank two on both sides closes)

If the same frame is supported on both shores and

\[
             |\sigma_{D_a}(w)|\ge2,
             \qquad |\sigma_{D_b}(w)|\ge2,           \tag{4.2}
\]

then `G` is six-colourable.

### Proof

Two subsets of the three named blocks, each of order at least two, meet.
Their common member is the same supported admissible decoration on both
sides, so Theorem 2.1(1) applies. `square`

### Lemma 4.2 (rank-one portal exhaustion)

If `|sigma_D(w)|<=1`, at least one of the following literal certificates
occurs.

1. **Boundary incompatibility:** `|tau_D(w)|>=2`, and every raw contact but
   at most one is inadmissible because `w` is adjacent to a root in that
   named trace.
2. **Direct-core lock:** `K_w` is empty, and every edge from `w` into the
   open shore lands in one named core block.
3. **Five-attachment lock:** `K_w` is nonempty and, for one named block
   `K`,

   \[
      N_G(K_w)\subseteq K\cup\{w,t\},
      \qquad |N_G(K_w)\cap K|\ge5,                  \tag{4.3}
   \]

   where `t` is the side terminal.  Moreover, in the closed terminal shore
   `J=D union T union {t}`, putting `Q=N_J(K_w)` gives a literal separation

   \[
      (K_w\cup Q,\ J-K_w),\qquad Q\subseteq K\cup\{w,t\}. \tag{4.4}
   \]

### Proof

If `|tau_D(w)|>=2`, each member outside `sigma_D(w)` is geometrically
contacted but inadmissible.  Since its original trace is independent,
inadmissibility is exactly a literal `w`--root edge.  This gives outcome 1.

Suppose `|tau_D(w)|<=1`.  If `K_w` is empty, fullness at `w` and the
definition of `tau` put every open-shore `w`-edge in the unique contacted
core block, giving outcome 2.

Now let `K_w` be nonempty.  Components left after deleting the open-shore
vertices of the core have no mutual edges.  Every neighbour of `K_w` in
`D-K_w` therefore lies in the unique raw-contact block `K`.  Every root of
`U` belongs to one of the three core blocks; a root neighbour in another
block would be a second raw contact.  The terminal separation excludes the
opposite shore and `v`.  Hence

\[
                         N_G(K_w)\subseteq K\cup\{w,t\}.
\]

This neighbourhood separates nonempty `K_w` from `v`.  Seven-connectivity
gives it order at least seven, and at most `w,t` lie outside `K`, proving
the five-attachment bound.  Finally `Q=N_J(K_w)` is by definition the
adhesion in (4.4). `square`

## 5. Degree surplus and a label-faithful lobe surgery

The following statements continue to assume the exact cell (1.1): the two
open shores `D_a,D_b` exhaust all vertices outside
`T union {a,b,v}`.  Put `k=|N_U(w)|`.

### Lemma 5.1 (palette obstruction versus shore surplus)

In the exact cell,

\[
 |N_{D_a}(w)|+|N_{D_b}(w)|=d_G(w)-k\ge 7-k.       \tag{5.1}
\]

For a frame `e|f|{r}`, the number of blocks to which `w` may legally be
adjoined is the number of those three blocks disjoint from `N_U(w)`.
Consequently:

1. if `k=0`, all three decorations are admissible;
2. if `k=1`, exactly two are admissible;
3. if `k=2`, two are admissible exactly when the two neighbours form one
   of the two two-vertex frame blocks, and otherwise exactly one is; and
4. if `k>=3`, at most one is admissible.

### Proof

The vertex `w` misses `v` because `w` is not in `N(v)`, and it misses
`a,b` by Lemma 3.1.  Exact exhaustion therefore accounts for every
neighbour of `w` in `U,D_a,D_b`, proving the equality in (5.1); the frozen
minimum-degree bound gives the inequality.  The remaining assertions count
the blocks of the partition `e|f|{r}` which meet `N_U(w)`. `square`

Use the missing-edge cyclic order

\[
                              0,5,2,4,6,0.          \tag{5.2}
\]

### Lemma 5.2 (dense extra-portal contacts close)

If `N_U(w)` contains three consecutive vertices of (5.2) whose middle
vertex is not `0`, then `G` has a `K_7` minor.  Hence every
`K_7`-minor-free exact cell satisfies

\[
 |N_U(w)|\le3.                                      \tag{5.3}
\]

If equality holds, then

\[
 N_U(w)\in\{024,045,026,056,256,456\}.             \tag{5.4}
\]

### Proof

For the four possible three-vertex arcs, the following rows are literal
`K_7` models.  A term such as `{4} union D_a` denotes one branch set.

\[
\begin{array}{c|lllllll}
N_U(w)&\multicolumn{7}{c}{\text{branch sets}}\\ \hline
025&\{0\}&\{2\}&\{1,6\}&\{v\}&\{5,w\}&\{4\}\cup D_a&\{3\}\cup D_b\\
245&\{0\}&\{4\}&\{3,5\}&\{v\}&\{2,w\}&\{1\}\cup D_a&\{6\}\cup D_b\\
046&\{0\}&\{4\}&\{3,5\}&\{v\}&\{6,w\}&\{1\}\cup D_a&\{2\}\cup D_b\\
246&\{0\}&\{2\}&\{1,6\}&\{v\}&\{4,w\}&\{5\}\cup D_a&\{3\}\cup D_b.
\end{array}                                         \tag{5.5}
\]

The fixed Moser edges make the four nonshore, non-`v` bags in each row a
clique.  Every such bag contains a boundary vertex and hence sees `{v}`.
Fullness in (1.1) supplies all contacts with the two shore bags; their
mutual contacts in the four rows are respectively the boundary edges
`34,16,12,35`.  Thus all seven displayed bags are disjoint, connected, and
pairwise adjacent.

Every four-subset of a five-cycle contains a three-vertex arc whose middle
is not `0`, proving (5.3).  Removing the four positive triples
`025,245,046,246` from the ten triples of `U` leaves exactly (5.4).
`square`

Combining Lemmas 5.1 and 5.2, `w` has at least four literal edges into the
two shores, and at least five unless its root neighbourhood is one of the
six triples in (5.4).

The five-attachment lock of Lemma 4.2 admits the following first
label-faithful surgery.  This statement is independent of the Moser labels.

### Lemma 5.3 (pendant-lobe decoration promotion)

Let `K,L,M` be disjoint connected pairwise adjacent blocks with prescribed
literal traces in an adhesion `T`.  Let `W` be connected, disjoint from
those blocks and from the side terminal, with trace `{w}`, and suppose `W`
is adjacent to `K`.  Assume that adjoining `w` to the trace of `M` is
independent.

Choose an endpoint `q_L in K` of a `K-L` edge, and let `Q_L` be an
inclusion-minimal tree in `G[K]` containing

\[
                         (K\cap T)\cup\{q_L\}.       \tag{5.6}
\]

If a component `C` of `G[K]-V(Q_L)` contains both an endpoint of a `W-K`
edge and an endpoint of a `K-M` edge, then the replacements

\[
 K\longmapsto K-C,\qquad M\longmapsto M\cup C\cup W \tag{5.7}
\]

give three disjoint connected pairwise adjacent blocks with the old traces,
except that `w` is adjoined to the trace of `M`.

### Proof

Every component of `G[K]-V(Q_L)` has a neighbour in the connected tree
`Q_L`.  Hence `K-C` is connected: it consists of `Q_L` and all the other
components, each attached to `Q_L`.  It retains the complete trace of `K`
and the protected `K-L` edge at `q_L`.

The two endpoint hypotheses make `M union C union W` connected.  This new
block sees `K-C` through a `C-Q_L` edge and sees `L` through the old `M-L`
edge.  The other two blocks retain their old adjacency.  Finally `C`
contains no adhesion vertex, since all of `K cap T` lies in `Q_L`.
Therefore the only trace change is the stipulated legal addition of `w` to
`M`. `square`

Lemma 5.3 eliminates every five-attachment lock in which a `W`-attachment
and a portal to an admissible foreign block occur in the same pendant lobe
of a protected witness tree.  If promotion fails, then for every admissible
target `M` and every protected choice, all such foreign portals lie in the
minimal central path or subdivided `Y`, or in pendant lobes containing no
`W`-attachment.  This is a structural central-core lock, not another
boundary-state enumeration.

## 6. Exact scope

This theorem closes every exact-order-six cell with a common frame and
bilateral admissible rank at least two, converts rank at most one into one
of three literal geometric certificates, excludes all but six dense
three-root contact patterns, and label-faithfully promotes every
pendant-lobe instance of the five-attachment lock.  It does **not** prove
that the general separator from the rooted `K_5` theorem has order six,
that the two shores possess a common crossed frame, or that the remaining
central-core locks can be rerouted.  Those are the remaining bridge/Tutte
composition tasks.
