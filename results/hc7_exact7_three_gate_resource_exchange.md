# Exact-seven three-gate resource exchange

## 1. Scope

Let `G` be a seven-connected graph with a literal separation

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                                  \tag{1.1}
\]

where `L,R` are nonempty, there are no `LR` edges, and `R` contains
three pairwise vertex-disjoint connected `S`-full packets
`P_1,P_2,P_3`.  Assume that `G[L]` is three-connected.  This is the
three-connected branch of the oriented exact-seven packet cell
`(nu_L,nu_R)=(1,3)`.

Let `T={t_1,t_2,t_3}` be an actual three-cut of `G[L]`, and call the
components of `G[L]-T` the **`T`-lobes**.  Three-connectivity implies
that every lobe has a neighbour at every literal member of `T`.

The main theorem repairs the virtual web triangle without assuming that
any edge of that triangle is literal:

> **Every three-gate with at least three lobes gives a literal `K_7`.**

Thus a surviving nonplanar web cell has exactly two `T`-lobes.  This is
a reusable gate/resource theorem, not a classification by Moser labels.

## 2. Two elementary literal inputs

For a connected set `C subseteq L`, write

\[
                         A(C)=N_S(C).                       \tag{2.1}
\]

### Lemma 2.1 (four labelled clique carriers lift)

Suppose `B_1,B_2,B_3,B_4 subseteq L` are pairwise disjoint nonempty
connected sets and are pairwise adjacent.  If the four sets

\[
                         A(B_1),\ldots,A(B_4)               \tag{2.2}
\]

have a system of distinct representatives in `S`, then `G` has a
literal `K_7` minor.

#### Proof

Choose distinct `s_i in A(B_i)` and write

\[
                    S-\{s_1,s_2,s_3,s_4\}
                         =\{r_1,r_2,r_3\}.                 \tag{2.3}
\]

The seven branch sets are

\[
 B_i\cup\{s_i\}\quad(1\le i\le4),\qquad
 P_j\cup\{r_j\}\quad(1\le j\le3).                       \tag{2.4}
\]

They are disjoint and connected.  The first four are pairwise adjacent
by the carrier hypothesis.  The last three are pairwise adjacent because
each full packet contacts the other packet bag's literal anchor.  Every
last bag is adjacent to every first bag because it contacts the literal
vertex `s_i`.  Hence (2.4) is a literal `K_7` model. `square`

### Lemma 2.2 (a lobe has four labels and localized portal rank four)

For every `T`-lobe `C`,

\[
                         |A(C)|\ge4.                        \tag{2.5}
\]

Moreover the bipartite incidence graph between `S` and `V(C)` has a
matching of order

\[
                         \min\{4,|C|\}.                    \tag{2.6}
\]

#### Proof

All neighbours of `C` outside `C` lie in `T union A(C)`.  Another lobe
and the nonempty opposite shore lie outside this set, so seven-connectivity
gives

\[
                         3+|A(C)|\ge7,
\]

which is (2.5).

Let `m` be the maximum portal-matching order and suppose
`m<min{4,|C|}`.  Hall's deficiency identity gives `U subseteq S` with

\[
                 m=7-|U|+|N_C(U)|.                         \tag{2.7}
\]

Delete

\[
                 T\cup(S-U)\cup N_C(U).                    \tag{2.8}
\]

Its order is `3+m<7`.  The set `C-N_C(U)` is nonempty: otherwise (2.7)
would give `m>=|C|`.  It has no neighbour in `U`, by definition, and all
of its other exits in (2.8) have been deleted.  The opposite shore remains
outside (2.8).  Thus (2.8) is a separator of order below seven, a
contradiction. `square`

### Lemma 2.3 (two rooted pieces inside a nontrivial lobe)

Let `C` be a `T`-lobe of order at least two.  There are distinct labels
`a,b in S`, distinct vertices `x,y in C` with `xa,yb in E(G)`, distinct
gate vertices `u,v in T`, and a partition

\[
                         C=X\mathbin{\dot\cup}Y             \tag{2.9}
\]

such that:

1. `X,Y` are nonempty and connected;
2. there is an `XY` edge;
3. `X` has a neighbour at `u` and contains `x`;
4. `Y` has a neighbour at `v` and contains `y`.

#### Proof

Lemma 2.2 supplies the two matched incidences `ax,by`.  Since `G[L]` is
three-connected, the set version of Menger's theorem supplies two
vertex-disjoint paths from `{x,y}` to two distinct members `u,v` of
`T`.  Stop each path at its first vertex of `T`.  Its remaining vertices
lie in `C`, because `C` is a component of `L-T`.  Let `Q_x,Q_y` be the
two disjoint connected initial path segments in `C`; they contain `x,y`
and have neighbours at `u,v`, respectively.

Choose a spanning tree of `G[C]` which contains spanning trees of
`Q_x,Q_y` and a path joining them.  Delete one tree edge on the unique
`Q_x-Q_y` path.  The two resulting tree components have vertex sets
`X,Y`; after assigning the names so that `Q_x subseteq X` and
`Q_y subseteq Y`, they satisfy all four conclusions. `square`

The use of Menger is literal.  A one-vertex separator between
`{x,y}` and `T` would contradict three-connectivity (even if the deleted
vertex were one of `x,y`), so the required linkage has order two.

## 3. The multi-lobe exchange

### Theorem 3.1 (three-gate resource theorem)

If `G[L]-T` has at least three components, then `G` contains a literal
`K_7` minor.

#### Proof: at least four lobes

Choose four distinct lobes `C_0,C_1,C_2,C_3`.  The four sets

\[
                   B_0=C_0,\qquad
                   B_i=C_i\cup\{t_i\}\quad(1\le i\le3)   \tag{3.1}
\]

are disjoint and connected.  They are pairwise adjacent: `C_0` has a
neighbour at every `t_i`, while for `i ne j`, `C_i` has a neighbour at
`t_j`.  Each `A(B_i)` has order at least four by Lemma 2.2.  Any family
of four subsets of a seven-set, each of order at least four, has an SDR:
every subfamily of order `r<=4` has union of order at least four, hence at
least `r`.  Lemma 2.1 now gives `K_7`.

#### Proof: exactly three lobes, one nontrivial

Let the lobes be `C_1,C_2,C_3`, with `|C_1|>=2`.  Apply Lemma 2.3 in
`C_1`; after renaming `T`, write its output as

\[
             C_1=X\dot\cup Y,qquad
             X-t_1,quad Y-t_2,quad XY,                   \tag{3.2}
\]

where `X` contacts the literal label `a`, `Y` contacts the distinct label
`b`, and the displayed dashes denote literal adjacencies.  Put

\[
 B_1=X\cup\{t_1\},\quad
 B_2=Y\cup\{t_2\},\quad
 B_3=C_2\cup\{t_3\},\quad
 B_4=C_3.                                                 \tag{3.3}
\]

These sets are disjoint and connected.  Here is the complete adjacency
check.

* `B_1B_2` is the edge between `X` and `Y`.
* `B_1B_3` and `B_2B_3` are supplied by the contacts of `C_2` to
  `t_1,t_2`.
* `B_4B_i` for `i=1,2,3` is supplied by the contacts of `C_3` to
  `t_1,t_2,t_3`, respectively.

Thus they are four clique carriers.  The first two already have distinct
representatives `a,b`.  Since `|A(C_2)|,|A(C_3)|>=4`, choose

\[
 c\in A(C_2)-\{a,b\},\qquad
 d\in A(C_3)-\{a,b,c\}.                                  \tag{3.4}
\]

Both choices exist.  The labels `a,b,c,d` represent the four carriers,
so Lemma 2.1 gives `K_7`.

#### Proof: exactly three singleton lobes

Now `L` has the six vertices consisting of `T` and the three singleton
lobes `c_0,c_1,c_2`.  The portal-matching theorem for an actual
seven-separation (equivalently, the Hall-separator proof of Lemma 2.2
applied to the whole connected shore) gives a portal matching saturating
all six vertices of `L`.  In particular some gate vertex, say `t_3`,
contacts a literal label `a in S`.

Use the four carriers

\[
 B_0=\{c_0\},\qquad
 B_1=\{c_1,t_1\},\qquad
 B_2=\{c_2,t_2\},\qquad
 B_3=\{t_3\}.                                             \tag{3.5}
\]

They are connected and pairwise adjacent.  Indeed `c_0` sees all three
gate vertices; `c_1` sees `t_2,t_3`; and `c_2` sees `t_1,t_3`.  The last
carrier is represented by `a`.  Each singleton lobe contacts at least
four labels, so, successively, choose three distinct representatives for
`B_0,B_1,B_2` outside `a`: after excluding at most one, two, and three
previous labels, respectively, a set of order at least four remains
nonempty at every step.  Lemma 2.1 again gives `K_7`. `square`

### Corollary 3.2 (the exact residual is a two-lobe gate)

In a `K_7`-minor-free graph satisfying (1.1), every three-cut `T` of the
three-connected thin shore has exactly two `T`-lobes.

This conclusion repairs the virtual web triangle by using whole other
bridges, without ever treating a virtual gate edge as literal.

## 4. What literal gate edges additionally force in the two-lobe residue

Let the two lobes be `C,D`, let `uv` be a literal edge of `G[T]`, and let
`w` be the third gate vertex.

### Proposition 4.1 (edge plus two gate anchors closes)

If the two portal sets `N_S(u),N_S(v)` have an SDR, then `G` contains a
literal `K_7` minor.

#### Proof

The four carriers

\[
                         C,\qquad D\cup\{w\},qquad
                         \{u\},\qquad\{v\}                \tag{4.1}
\]

are connected and pairwise adjacent.  The two lobes see every gate
vertex, and the last pair is adjacent through the literal edge `uv`.
Use the two distinct gate labels supplied by the SDR.  Each lobe has at
least four labels, so two further distinct representatives can be chosen
outside those gate labels.  Lemma 2.1 gives `K_7`. `square`

Consequently, in a survivor, for every literal gate edge `uv`,

\[
             \operatorname{rank}\{N_S(u),N_S(v)\}\le1.    \tag{4.2}
\]

Equivalently, one endpoint has no boundary portal, or both nonempty
portal sets are the same singleton.  This is the exact literal-edge
barrier left after the multi-lobe exchange.

## 5. Guardrail: deleting one lobe need not root a gate triangle

It is false that three-connectivity alone makes `L-K` contain a
`T`-rooted `K_3` after deleting an arbitrary `T`-lobe `K`.

Let

\[
 T=\{0,1,4\},\qquad K=\{2,3\},\qquad D=\{5\},              \tag{5.1}
\]

and take all nine edges between `T` and `K union D`, together with the
edge `23`.  This is `K_{3,3}` plus one edge, hence is three-connected and
nonplanar.  The set `K` is a component behind the three-cut `T`.  But
`L-K` is the star with centre `5` and leaves `0,1,4`.

That star has no `T`-rooted `K_3`: at most one of three disjoint root bags
can contain the centre, and the other two root bags are nonadjacent.
The independent exhaustive verifier

```text
PYTHONPATH=active/runtime/deps python3 \
    active/hc7_gate_rooted_triangle_search.py
```

finds this as the smallest graph-atlas counterexample.  It is only a
guardrail against the connectivity-only inference; Theorem 3.1 instead
uses the other lobes as literal resources and is unaffected by it.

## 6. Exact remaining gate barrier

After this exchange, the nonplanar three-connected branch has one actual
three-gate `T` and exactly two lobes `C,D`.  Each lobe:

* contacts at least four literal boundary labels;
* has localized portal-matching order `min{4,|C|}`; and
* meets all three gate vertices.

Every literal gate edge satisfies the rank-one restriction (4.2).  The
remaining theorem must either distribute three labelled carriers through
one lobe while the other serves as the fourth carrier, or obtain a common
proper-minor boundary state.  It may not assume that deleting either lobe
leaves a rooted gate triangle.
