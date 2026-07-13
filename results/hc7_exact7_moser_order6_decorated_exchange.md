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

## 5. Exact scope

This theorem closes every exact-order-six cell with a common frame and
bilateral admissible rank at least two, and converts rank at most one into
one of three literal geometric certificates.  It does **not** prove that
the general separator from the rooted `K_5` theorem has order six, that the
two shores possess a common crossed frame, or that a five-attachment lock
can already be rerouted label-faithfully.  Those are the remaining
bridge/Tutte composition tasks.
