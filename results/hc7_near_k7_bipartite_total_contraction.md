# Total-contraction states on a constant corridor

## Status

This note proves a new uniform state lemma for the induced bridge corridors
in `../archive/hc7_near_k7_constant_owner_corridor.md`.  It does not prove
`HC_7`.

The previous edge-by-edge argument gives at least three externally started
Kempe layers at each internal edge, but the colourings may be unrelated from
one edge to the next.  The result below instead contracts a whole corridor
path and uses one colouring of that proper minor.  In that one colouring
there is an edge of the original path whose two connected shores both see
all five colours different from the contracted colour.

Thus the remaining gap is no longer palette synchronization across the
corridor.  It is exactly the conversion of five already synchronized
palette witnesses into five literal, pairwise adjacent model carriers.

## 1. A list lemma for paths

Let `Q` be a finite colour set.  If

\[
                 P=v_0v_1\cdots v_{n-1}
\]

is a path and `L_i` is a nonempty subset of `Q`, an `L`-colouring is a
proper colouring `f` of `P` with `f(v_i) in L_i`.

### Lemma 1.1 (two-block contraction witness)

Suppose

\[
                    a\in\bigcap_{i=0}^{n-1}L_i              \tag{1.1}
\]

and `P` has no `L`-colouring.  Then `n>=2`,

\[
                    \bigcap_{i=0}^{n-1}L_i=\{a\},            \tag{1.2}
\]

and for some `k in {0,...,n-2}`,

\[
 \bigcap_{i=0}^{k}L_i=\{a\}
       =\bigcap_{i=k+1}^{n-1}L_i.                            \tag{1.3}
\]

Equivalently, after contracting the two intervals
`v_0...v_k` and `v_{k+1}...v_{n-1}` separately, the two adjacent
contracted vertices are both forced to the same colour `a` by the fixed
outside state.

#### Proof

If the total intersection contained distinct colours `a,b`, alternating
`a,b` along the path would be an `L`-colouring.  This proves (1.2); it
also rules out `n=1`.

Put

\[
 A_i=\bigcap_{j=0}^{i}L_j,qquad
 B_i=\bigcap_{j=i}^{n-1}L_j.
\]

Let `p` be the least index with `A_p={a}`, and let `q` be the greatest
index with `B_q={a}`.  If `p<q`, choose any `k` with
`p<=k<q`.  Then `A_k=B_{k+1}={a}`, which is (1.3).

It remains to show that `p>=q` would colour the path.  When `p>0`, choose

\[
                   b\in A_{p-1}-\{a\};                       \tag{1.4}
\]

when `q<n-1`, choose

\[
                   c\in B_{q+1}-\{a\}.                       \tag{1.5}
\]

Every vertex before `p` admits both `a,b`, and every vertex after `q`
admits both `a,c`.

If `p=q`, colour `v_p` with `a`; colour the left interval backwards,
alternating `a,b` and ending at `v_{p-1}` with `b`, and colour the right
interval forwards, alternating `a,c` and starting at `v_{p+1}` with
`c`.  Empty end intervals require no colour.  This is proper.

Suppose `p>q`.  The left interval through `v_q` can be coloured with
`a,b` with either prescribed colour at `v_q`, and the right interval
from `v_p` can be coloured with `a,c` with either prescribed colour at
`v_p`.  Every vertex strictly between them admits `a,b,c` when
`b!=c`, so that middle path can be coloured after choosing its two end
neighbours; three colours always suffice for a path with two forbidden
end colours.  If `b=c`, every vertex from `v_q` through `v_p` admits
`a,b`; choose the two freely adjustable end phases so that this whole
interval alternates `a,b`.  In both cases the three colourings splice to
an `L`-colouring of `P`, a contradiction.  Therefore `p<q`, and (1.3)
follows.  QED.

The lemma is palette-uniform: no bound on `|Q|` is used.

The path order is in fact unnecessary.

### Lemma 1.2 (poor-edge lemma for bipartite graphs)

Let `X` be a connected bipartite graph, let `T` be any spanning tree of
`X`, and give each vertex `x` a nonempty list `L(x) subseteq Q`.  Suppose

\[
                             a\in L(x)\quad(x\in X),          \tag{1.6}
\]

but `X` has no list-colouring.  Then some edge `uv` of `T` has the following
property.  If `X_u,X_v` are the vertex sets of the two components of
`T-uv`, then

\[
              \bigcap_{x\in X_u}L(x)=\{a\}
                  =\bigcap_{x\in X_v}L(x).                   \tag{1.7}
\]

The two returned sets are connected and adjacent in `X`.  Extra edges of
`X` do not need to respect the tree components.

#### Proof

For an oriented tree edge `vu`, call the `u`-side of `T-vu` **poor** if
the intersection of its lists is `{a}`, and **rich** otherwise.  Orient
`v -> u` when the `u`-side is poor.  We claim that every vertex has an
outgoing edge.

Suppose instead that a vertex `v` has none.  Every component `C` of
`T-v` is then rich, so choose

\[
                       b_C\in\bigcap_{x\in C}L(x)-\{a\}.      \tag{1.8}
\]

Fix the global bipartition `(A,B)` of `X`; assume first that `v in A`.
Give `v` colour `a`.  In each tree branch `C`, give its vertices in `A`
colour `a` and its vertices in `B` colour `b_C`.  All assigned colours
belong to the lists.  Every edge inside one branch is proper because it
crosses `(A,B)`.  An extra edge joining two different tree branches also
crosses `(A,B)`: its `A`-end has colour `a` and its `B`-end has the
secondary colour belonging to its own branch.  Extra edges from `v` are
proper for the same reason.  This list-colours `X`, a contradiction.  The
case `v in B` is symmetric, interchanging the bipartition classes.

Thus every vertex has an outgoing tree edge.  Following outgoing arcs in
the finite tree eventually repeats a vertex.  Since the underlying graph
has no cycle of length at least three, the resulting directed cycle is a
two-cycle on one edge `uv`.  Both the `u`-side and the `v`-side are poor,
which is (1.7).  QED.

For `X=P`, Lemma 1.2 implies Lemma 1.1.  The direct prefix-intersection
proof was retained because it identifies the same edge without choosing a
spanning tree and makes the two-block state interpretation transparent.

## 2. The graph-theoretic corridor theorem

For a connected vertex set `X`, write `G/X` for the minor obtained by
contracting a spanning tree of `G[X]` to one vertex and deleting the
resulting loops.  Throughout, `N_G(X)` denotes the open external
neighbourhood, and is therefore disjoint from `X`.

### Lemma 2.1 (low-chromatic contractions stay chromatically high)

Let `G` be proper-minor-minimal non-`q`-colourable, so that
`chi(G)=q+1` and every proper minor is `q`-colourable.  If `X` is a
connected vertex set with at least two vertices and `G[X]` is
`s`-colourable, where `2<=s<=q+1`, then

\[
                         \chi(G/X)\ge q-s+2.                  \tag{2.1}
\]

In particular, if `G[X]` is bipartite, then

\[
                            \chi(G/X)=q.                      \tag{2.2}
\]

#### Proof

The contraction is proper, so `chi(G/X)<=q`.  Suppose `G/X` had a
`(q-s+1)`-colouring, and let `a` be the colour of the contraction vertex
`z`.  No external neighbour of `X` has colour `a`.  Take a proper
`s`-colouring of `G[X]`.  Assign colour `a` to one of its colour classes,
and assign `s-1` fresh colours, not used on `G/X`, to its other classes.
Internal edges of `X` are proper.  External edges at the `a`-class are
proper because all external neighbours avoid `a`; external edges at the
other classes are proper because their colours are fresh.  The total
number of colours is at most

\[
                         (q-s+1)+(s-1)=q,
\]

contradicting the choice of `G`.  This proves (2.1).  At `s=2`, the lower
bound is `q`, matching the proper-minor upper bound.  QED.

More generally, if `HC_q` is known and the host is
`K_{q+1}`-minor-free, the tight bipartite contraction has a `K_q` minor
and no `K_{q+1}` minor.  Hence

\[
                         \chi(G/X)=\eta(G/X)=q.               \tag{2.3}
\]

In the `HC_7` application `q=6`, this uses the known theorem `HC_6`.
Thus contracting a whole corridor path preserves both sides of the
equality cell

\[
                         \chi(G/X)=\eta(G/X)=6,               \tag{2.4}
\]

not merely six-colourability.

### Theorem 2.2 (bipartite bilateral full-palette cut)

Let `G` be a graph which is not `q`-colourable, and let `X` be a connected
vertex set with at least two vertices such that `G[X]` is bipartite.
Suppose the proper minor `G/X` has a `q`-colouring `c`.  Let `z` be the
contraction image of `X` and put `a=c(z)`.

For every spanning tree `T` of `G[X]`, some edge of `T` splits its vertex
set into two nonempty sets

\[
                              X=X^-\mathbin{\dot\cup}X^+      \tag{2.3}
\]

which are connected and adjacent in `G[X]`, and for which both shores have
an outside neighbour of every colour different from `a`:

\[
 c\bigl(N_G(X^-)-X\bigr)
   =c\bigl(N_G(X^+)-X\bigr)=Q-\{a\}.                         \tag{2.4}
\]

Here `c` on `G-X` is the restriction of the one fixed colouring of
`G/X`.  In particular the five layers in the case `q=6` are simultaneous.
Neither a path order nor a separate colouring at each edge is required.

#### Proof

For each `x in X`, define

\[
                 L(x)=Q-c\bigl(N_G(x)-X\bigr).               \tag{2.5}
\]

Every outside neighbour of every `x` is adjacent to `z` in `G/X`, so
none has colour `a`; hence `a in L(x)` for every `x`.  If `G[X]` had an
`L`-colouring, adjoining it to `c|_{G-X}` would properly colour `G`,
contrary to the hypothesis.

Apply Lemma 1.2 to `G[X]` and the selected spanning tree `T`.  For the
two returned tree sides,

\[
 \bigcap_{x\in X^-}L(x)
   =Q-c\bigl(N_G(X^-)-X\bigr)=\{a\},                         \tag{2.6}
\]

and the same equality holds for `X^+`.  Taking complements in `Q` gives
(2.4).  Each side is connected in `T`, and the deleted tree edge joins
them.  QED.

### Corollary 2.3 (minor-minimal corridor form)

If `G` is proper-minor-minimal non-`q`-colourable, Theorem 2.2 applies to
every connected induced bipartite subgraph with at least two vertices.
Thus every constant-owner bridge corridor has a cut whose two shores carry
one common full `(q-1)`-colour exposure in a single proper-minor state.
The same conclusion holds for an arbitrary induced bipartite transit tree
or for a bipartite ear closure with extra edges: choose any spanning tree
inside it and apply the theorem.

Moreover Lemma 2.1 says that **every** colouring of this total contraction
uses the full `q`-colour palette.  Applying Theorem 2.2 to any one of them
gives the bilateral cut; no favourable choice of a lower-palette state is
being assumed.

For an interval consisting of strictly internal vertices in the ordered
`K_7^vee` source, Theorem 2.1 of
`../archive/hc7_near_k7_constant_owner_corridor.md` says that none of these direct
outside contacts lies in an owner bag.  Consequently all five synchronized
layers are forced through the nonowner bags or through unused exterior
material.  This is a sharper collision input than the three per-edge
Kempe layers of that note.

No connectivity is used in Theorem 2.2.  Seven-connectivity is to be spent
after (2.4), on separating or splitting the common carriers of the ten
literal shore-colour incidences.

### Corollary 2.4 (a forced two-block state jump)

Retain the minor-minimal setting and the cut returned by Theorem 2.2, and
assume `|X|>=3`.
Let `G_2` be the proper minor obtained by contracting `X^-` and `X^+`
separately to two adjacent vertices.  The colouring `c|_{G-X}` does
not extend to `G_2`, although `G_2` has some `q`-colouring.

Consequently no `q`-colouring of `G_2` restricts on the exterior
`G-X` to a global colour permutation of the total-contraction state
`c`.  The corridor therefore supplies a literal
pair of incompatible proper-minor states:

\[
 \begin{array}{c|c}
 G/X & \text{one contracted vertex of colour }a,\\
 G_2 & \text{two adjacent contracted shores, with no extension of the
              same exterior state.}
 \end{array}                                                  \tag{2.8}
\]

#### Proof

Under the fixed exterior colouring `c`, the available colours of the two
contracted vertices of `G_2` are respectively

\[
       \bigcap_{x\in X^-}L(x)=\{a\},\qquad
       \bigcap_{x\in X^+}L(x)=\{a\}.
\]

They are adjacent, so no extension exists.  Minor-minimality colours the
proper minor `G_2`; such a colouring cannot agree with `c` on the whole
exterior.  If it agreed up to a global colour permutation, applying the
inverse permutation would give exact agreement and the same contradiction.
QED.

At an actual small adhesion, Corollary 2.4 is exactly the kind of state
jump on which crossed-splicing can act.  At a gate-rich corridor it says
precisely what a new transport theorem must preserve; it is stronger than
repeating a one-edge equality state.

### Corollary 2.5 (the jump localizes on the actual adhesion)

Let

\[
                              S=N_G(X).                       \tag{2.9}
\]

Regard `c|_S` as a marked boundary state, modulo a global permutation of
the palette.  No `q`-colouring of the two-block contraction `G_2` has the
same marked state on `S`.

#### Proof

Suppose a colouring `d` of `G_2` had the same state on `S`.  Permute its
colour names so that `d|_S=c|_S`.  Use `d` on the side consisting of the
two contracted shores together with `S`, and use `c` on
`G-X`.  The two colourings agree on their overlap `S`, and every edge
between the two sides has an end in `S` by (2.9).  They therefore splice
to a `q`-colouring of `G_2` which agrees with `c` on the entire exterior
`G-X`.  This contradicts Corollary 2.4.  QED.

For a constant-owner interval, `S` is an actual separator and has order at
least seven.  At order seven or eight, Corollary 2.5 produces a fully
localized, faithful state incompatibility on exactly the adhesions already
isolated by the near-clique descent.  It uses the total contraction and the
two-block contraction on the **same** original bipartite subgraph; no
quotient boundary vertex is mistaken for an original vertex.

### Corollary 2.6 (uniform rooted split principle)

Let `G` be a `k`-contraction-critical graph in the strong minor-minimal
sense: `chi(G)=k` and every proper minor is `(k-1)`-colourable.  Let
`x,y` be nonadjacent vertices in a connected vertex set `D`.  Choose a
shortest `x-y` path `P` in the induced graph `G[D]` and contract all of
`P` to `z`.  Then:

1. `P` is induced in `G`;
2. `chi(G/P)=k-1`;
3. in every `(k-1)`-colouring `c` of `G/P`, with `a=c(z)`, some edge
   of `P` splits it into connected adjacent shores `P_x,P_y` containing
   `x,y`, respectively, such that
   
   \[
      c\bigl(N_G(P_x)-V(P)\bigr)
        =c\bigl(N_G(P_y)-V(P)\bigr)
        =Q-\{a\}.                                           \tag{2.10}
   \]

Thus a prescribed nonadjacent root pair can always be separated by a
connected two-shore split carrying one simultaneous double exposure of
all `k-2` secondary colours.  If `HC_{k-1}` is known and `G` has no
`K_k` minor, the total contraction also satisfies

\[
                         \chi(G/P)=\eta(G/P)=k-1.             \tag{2.11}
\]

#### Proof

A chord of the shortest path would give a shorter `x-y` path inside
`G[D]`, proving item 1.  The path is connected and bipartite, so Lemma
2.1 gives item 2.  Apply Theorem 2.2 with `q=k-1` and take the path itself
as the spanning tree.  Deleting any one of its edges separates its two
ends, so the returned shores contain `x` and `y` on opposite sides; (2.10)
is (2.4).  The equality in (2.11) is (2.3).  QED.

This is the direct bridge between the equality-carrier and near-clique
programmes.  Every last-pair carrier contains a label-separating rooted
split with a double full-palette interface.  What still requires geometry
is turning those palette exposures into the prescribed old branch-set
labels without overlapping carriers.

## 3. Exact label-aligned closure

The following records precisely what remains between the palette theorem
and a clique model.

### Theorem 3.1 (balanced palette-carrier completion)

Retain Theorem 2.2.  Suppose there are pairwise disjoint connected
subgraphs

\[
                         D_\beta\quad(\beta\in Q-\{a\})       \tag{3.1}
\]

which are pairwise adjacent and such that both `X^-` and `X^+` are
adjacent to every `D_beta`.  Then

\[
               X^-,\quad X^+,\quad
               D_\beta\ (\beta\in Q-\{a\})                  \tag{3.2}
\]

are a `K_{q+1}` minor model in `G`.

#### Proof

The two shores are nonempty, connected, disjoint, and adjacent through
the selected spanning-tree edge.  By hypothesis they are adjacent to all the
`D_beta`; the latter are connected, disjoint, and pairwise adjacent.
Thus the `2+(q-1)=q+1` displayed branch sets are pairwise adjacent.  QED.

For `q=6`, five literal clique carriers close the corridor to `K_7`.
In a spanning one-complex near-`K_7` shell the five singleton clique rows
are exactly such carriers whenever the witnesses in (2.4) are literal
row contacts.  More generally the `D_beta` may be old connected branch
bags or private extensions of them.

## 4. Exact remaining exchange

The total-contraction theorem changes the constant-owner frontier as
follows.

```text
old input:
    for each corridor edge, three external Kempe layers
    in a colouring depending on that edge;

new input:
    at one corridor edge, both connected shores see all five
    secondary colours in one colouring of the total contraction.
```

Therefore finite-state repetition along the path is unnecessary.  The
unproved operation-sensitive statement can be narrowed to:

> **Bilateral palette-to-label exchange.**  At the cut returned by
> Theorem 2.2 in a seven-connected, 7-contraction-critical,
> `K_7`-minor-free near-clique host, either the ten synchronized
> shore-colour incidences can be connected into five pairwise adjacent
> literal carriers as in Theorem 3.1, or their first carrier collision
> lies behind an actual colour-gluable order-seven/eight adhesion, or all
> carrier occurrences have one compatible rural expansion after deleting
> the same two vertices.

Theorem 3.1 proves the first outcome once carriers are aligned.  The
active-face, shared-lobe and literal triangle-adhesion theorems already
handle the geometric consequences of four fixed private carriers.  What
is not proved here is that vertices with the same palette colour lie in a
prescribed old branch bag, or even in one connected carrier.  Colour
classes are independent sets, so asserting that step without an exchange
or adhesion argument would repeat the colour-label noncommutation error.

The substantive gain is that the missing exchange now starts from one
bilateral five-colour state, rather than attempting to synchronize an
arbitrary sequence of local edge states.
