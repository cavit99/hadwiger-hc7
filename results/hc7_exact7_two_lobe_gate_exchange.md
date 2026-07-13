# Exact-seven two-lobe gate exchange

## 1. Scope and conclusion

Let `G` be a seven-connected graph with a literal separation

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where there are no `LR` edges, `R` contains three pairwise disjoint
connected `S`-full packets, and `G[L]` is three-connected.  Let
`T={t_1,t_2,t_3}` be an actual three-cut of `G[L]`, and suppose that
`G[L]-T` has exactly two components, called `C,D`.

The preceding audited three-gate exchange reduces the nonplanar
three-connected exact-`(1,3)` branch to this setup.  This note proves three
uniform closures.

1. Every surviving thin shore has `|L|>=8`.
2. A literal triangle on `T` always gives a literal `K_7`.
3. If `G[T]` is a path and its middle vertex has a neighbour in `S`, then
   `G` has a literal `K_7`.

Thus a surviving literal gate is not a triangle; if it is a two-edge
path, its middle vertex has no boundary portal.  The proof uses actual
branch sets and no edge of a web completion.

## 2. Portal rank after forbidden labels

For a lobe `K in {C,D}` put `A(K)=N_S(K)`.

### Lemma 2.1 (forbidden-label lobe matching)

For every `F subseteq S` with `|F|<=3`, the portal-incidence graph between
`S-F` and `V(K)` has a matching of order at least

\[
                  \min\{4-|F|,|K|\}.                    \tag{2.1}
\]

In particular `|A(K)|>=4`; three distinct portal vertices with three
distinct labels exist when `|K|>=3`; and after forbidding one prescribed
label, two such vertices still exist when `|K|>=2`.

#### Proof

Put `f=|F|`, and let `m` be the maximum matching order between `S-F` and
`K`.  Suppose

\[
                  m<\min\{4-f,|K|\}.                    \tag{2.2}
\]

The deficiency form of Hall's theorem gives `U subseteq S-F` such that

\[
             m=(7-f)-|U|+|N_K(U)|.                      \tag{2.3}
\]

Delete

\[
             X=T\cup F\cup((S-F)-U)\cup N_K(U).         \tag{2.4}
\]

By (2.3), `|X|=3+f+m<7`.  Also `K-N_K(U)` is nonempty; otherwise (2.3)
would give `m>=|K|`.  It has no neighbour in `U`, by definition, and all
of its other exits lie in the deleted set (2.4).  The other lobe and the
nonempty opposite shore remain outside `X`.  Hence `X` is a separator of
order below seven, a contradiction.  This proves (2.1).

For the first stated consequence, independently delete `T union A(K)`.
This separates the nonempty lobe `K` from the other lobe and the opposite
shore, so seven-connectivity gives `3+|A(K)|>=7`.  Thus
`|A(K)|>=4`, including when `|K|<4`, where (2.1) alone only saturates
the smaller vertex side. `square`

### Lemma 2.2 (a lobe-to-gate linkage)

Let `X={x_1,...,x_r} subseteq K` and `U subseteq T`, where
`|X|=|U|=r<=3`.  If `r=3`, there are `r` vertex-disjoint `X`--`U` paths
in `G[K union T]`.  If `r=2` and `T-U={w}`, there are two vertex-disjoint
`X`--`U` paths in `G[K union U]=G[K union T]-w`.

In either case the paths can be truncated at their first gate vertices;
their `K`-parts are disjoint and their gate endpoints are distinct.

#### Proof

For `r=3`, failure of the linkage gives by Menger a set `Z` of order at
most two meeting every `X`--`T` path in `G[K union T]`.  Since both
terminal sets have order three, some start and some gate vertex survive.
The component containing a surviving start in `G[L]-Z` lies in `K-Z`:
any exit from `K` first reaches `T`, and such a path would contradict the
choice of `Z`.  The other lobe still meets every surviving gate vertex,
so `G[L]-Z` is disconnected.  This contradicts three-connectivity.

For `r=2`, apply the same argument in `G[K union U]`.  A failed linkage
has an `X`--`U` separator `Z` of order at most one.  Then
`Z union {w}` has order at most two and separates a surviving start in
`K` from the other lobe in `G[L]`, again contradicting
three-connectivity.  Endpoint-inclusive versions of Menger cause no
exception: fewer than `r` deleted vertices cannot cover either terminal
set.  Truncating at first gate hits preserves disjointness and gives
distinct gate endpoints. `square`

## 3. Small shores close

### Lemma 3.1 (order at most seven)

If `|L|<=7`, then `G` contains a literal `K_7` minor.

#### Proof

The actual-adhesion portal-matching theorem supplies a matching between
`S` and `V(L)` saturating every vertex of `L`.  Every three-connected
graph contains a `K_4` minor.  Choose one vertex in each of four branch
sets of such a model.  Their matching partners are four distinct literal
vertices of `S`, so the rooted four-portal lift, together with the three
full packets in `R`, gives a literal `K_7`. `square`

## 4. Literal triangle gates close

### Theorem 4.1 (triangle-gate closure)

If `G[T]` is a triangle, then `G` contains a literal `K_7` minor.

#### Proof

By Lemma 3.1 assume `|L|>=8`.  Since

\[
                  |C|+|D|=|L|-3>=5,
\]

one lobe, say `D`, has order at least three.  Lemma 2.1 gives distinct
vertices `x_1,x_2,x_3 in D` with distinct boundary labels
`s_1,s_2,s_3`.  Lemma 2.2 gives three disjoint paths from those vertices
to the three distinct vertices of `T`.  Let `Q_i` be the path ending at
`t_i`, after a permutation of indices.

The four sets

\[
                        C,Q_1,Q_2,Q_3                   \tag{4.1}
\]

are disjoint and connected.  They are pairwise adjacent: `C` meets each
literal `t_i`, and `Q_i,Q_j` are adjacent through the literal edge
`t_it_j`.  The last three carriers have distinct representatives
`s_1,s_2,s_3`.  Since `|A(C)|>=4`, choose
`s_0 in A(C)-{s_1,s_2,s_3}`.  The rooted four-carrier lift through the
three opposite full packets gives a literal `K_7`. `square`

## 5. A path gate with a labelled middle closes

### Theorem 5.1 (middle-portal closure)

Suppose `G[T]` contains the two literal edges `t_1t_2,t_2t_3`.  If
`t_2` has a neighbour `q in S`, then `G` contains a literal `K_7` minor.

#### Proof

If both lobes are singletons then `|L|=5`, and Lemma 3.1 applies.  Thus
some lobe, say `D`, has order at least two.  Apply Lemma 2.1 with
`F={q}` to choose distinct portal vertices `x_1,x_3 in D` represented by
distinct labels `s_1,s_3 in S-{q}`.  Lemma 2.2, with
`U={t_1,t_3}` and `w=t_2`, gives disjoint path segments inside
`D union {t_1,t_3}` ending at the two leaves.  If necessary interchange
the subscripts `1,3` on the matched portals and their labels so that the
segment starting at `x_i` ends at `t_i`.

Join the two `D`-parts by a shortest connector in `D`, extend their union
to a spanning tree of `G[D]`, and delete one edge on the connector.  This
partitions `D=X_1 dotcup X_3` into two nonempty connected sets with a
literal `X_1X_3` edge, where `X_i` contains `x_i` and has a neighbour at
`t_i`.  Define

\[
 B_1=X_1\cup\{t_1\},\qquad
 B_3=X_3\cup\{t_3\},\qquad
 B_0=C,\qquad B_2=\{t_2\}.                              \tag{5.1}
\]

These are four disjoint connected clique carriers.  The complete list of
adjacencies is:

* `B_1B_3` from the deleted tree edge;
* `B_0B_i` from the fact that `C` meets every `t_i`, for `i=1,2,3`;
* `B_2B_1` from `t_2t_1`; and
* `B_2B_3` from `t_2t_3`.

Represent `B_1,B_3,B_2` by `s_1,s_3,q`.  Since `|A(C)|>=4`, choose a
fourth representative in `A(C)-{s_1,s_3,q}`.  The literal four-carrier
lift yields `K_7`. `square`

## 6. Exact residue

In the exact two-lobe gate cell, every survivor now satisfies:

1. `|L|>=8`;
2. `G[T]` is not a triangle;
3. if `G[T]` has two edges, their common endpoint has no neighbour in
   `S`; and
4. by the preceding audited gate-edge exchange, every literal gate edge
   has endpoint portal rank at most one.

The remaining constructive problem is therefore a sparse-gate carrier
exchange (zero or one literal gate edge, or a two-edge path with an
unlabelled middle), or a matching proper-minor state.  The theorem does
not assume a rooted gate triangle after deleting a lobe.
