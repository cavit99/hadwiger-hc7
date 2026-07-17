# Compact-model completion at an almost-universal boundary vertex

**Status:** written proof with a separate GREEN internal audit in
[`hc_almost_universal_straddling_completion_audit.md`](hc_almost_universal_straddling_completion_audit.md).
This note gives an all-parameter branch-set completion theorem.  Its `k=7`
application removes the forced-theta Hall alternative in the balanced
order-eight configuration, subject to the compact-model hypothesis.  It does
not orient the order-seven separation outcome and does not prove `HC_7`.

## 1. The uniform theorem

### Theorem 1.1 (one-straddling-branch-set completion)

Let `k>=3`, let `G` be a `k`-connected graph, and let `S` be a set of
`k+1` vertices.  Suppose `G-S` has distinct connected components `U,V`,
each adjacent to every vertex of `S`.  Let `p,x` be distinct vertices of
`S`, put

\[
                         B=S-\{p,x\},
\]

and assume that `p` is adjacent to every vertex of `B`.

Suppose `G-{p,x}` contains a `K_{k-2}`-minor model `mathcal M` of support
order `m<=k-1` for which there are vertices `v in V` and `t in B` such
that

1. the model support meets `V` exactly in `v`; and
2. `v,t` belong to the same branch set of `mathcal M`.

If `V-v` is nonempty, then `G` contains a `K_k` minor or has an actual
order-`k` separation.

### Proof

Let `C` be a component of `V-v`.  Since `V` is connected, `v` has a
neighbour in `C`, and

\[
                         N_G(C)=\{v\}\cup N_S(C).       \tag{1.1}
\]

If `|N_S(C)|<=k-1`, then `|N_G(C)|<=k`.  An order below `k` contradicts
`k`-connectivity, while equality gives an actual order-`k` separation:
after deleting `N_G(C)`, the component `C` and the nonempty component `U`
lie on opposite sides.  We may therefore assume

\[
                         |N_S(C)|>=k.                  \tag{1.2}
\]

Thus `C` misses at most one vertex of `S`.  Denote that vertex by `y` if
it exists.

First suppose that `C` is adjacent to `p`.  Define

\[
 W=
 \begin{cases}
    B-\{y\},&y\in B,\\
    B,&y\notin B,
 \end{cases}                                           \tag{1.3}
\]

so `|W|>=k-2`, and both `C` and `p` are adjacent to every vertex of `W`.
Let `I` index the branch sets of `mathcal M` which avoid `W`, and put
`q=|I|`.  Select one vertex `a_i` from every such branch set.  If the
branch set containing `v` belongs to `I`, then necessarily `y=t`; in that
case select `a_i=t`, rather than `v`.  Put

\[
 A=\{a_i:i\in I\},\qquad
 Z=\left(V(\mathcal M)-A\right)\cup\{p,x\},\qquad
 T=W-V(\mathcal M).                                   \tag{1.4}
\]

The `q` unanchored branch sets supply `q` distinct support vertices outside
`W`.  In addition, `v` lies outside `W` and was deliberately not selected
into `A`.  Hence

\[
 |V(\mathcal M)\cap W|\le m-q-1,
 \qquad
 |T|\ge |W|-m+q+1\ge q.                               \tag{1.5}
\]

If `q>0` and `G-Z` has no `q` pairwise vertex-disjoint `A`--`T` paths,
set-Menger gives an `A`--`T` separator `X` in `G-Z` of order at most
`q-1`.  Both terminal sets retain a vertex, and

\[
                         |Z\cup X|\le m+1\le k.        \tag{1.6}
\]

An order below `k` contradicts connectivity, while equality is an actual
order-`k` separation.  Otherwise choose the linkage, and stop every path
on its first visit to `W`.  Its endpoint lies in `T`, because every old
model vertex in `W` belongs to `Z`.

The stopped paths avoid `C`.  Indeed, by (1.1), every entrance to `C`
uses `v` or a vertex of `S`.  The vertex `v` and the vertices `p,x` lie
in `Z`; a possible missed vertex `y` has no neighbour in `C`; and every
remaining boundary entrance lies in `W`, where the path has already
stopped.  The paths also meet the old model only in their own selected
starts.  Enlarge the corresponding branch sets along the stopped paths.
All `k-2` model branch sets now contain distinct vertices of `W`, retain
their labels and old adjacencies, and avoid `C`.

For `q=0`, no enlargement is needed and the same conclusion already
holds.  In either case the `k` sets

\[
             \mathcal M,\qquad V(C),\qquad\{p\}        \tag{1.7}
\]

are a `K_k`-minor model.  Both new sets meet every old row through its
vertex of `W`, and `C` is adjacent to `p` by the present case assumption.

It remains that `C` is not adjacent to `p`.  By (1.2), `p` is then the
unique boundary vertex missed by `C`, so `C` is adjacent to every vertex
of `B`.  Let `I` now index the model rows which avoid `B`, put `q=|I|`,
and select one vertex from each such row.  The row containing `v` is not
in `I`, because it also contains `t in B`; thus `v` again remains in

\[
 A=\{a_i:i\in I\},\qquad
 Z=\left(V(\mathcal M)-A\right)\cup\{p,x\},\qquad
 T=B-V(\mathcal M).                                   \tag{1.8}
\]

The `q` selected vertices and the additional vertex `v` are outside `B`,
so

\[
 |T|\ge(k-1)-m+q+1\ge q+1.                            \tag{1.9}
\]

The same Menger count (1.6) gives an actual order-`k` separation or lets
us enlarge every unanchored row to a distinct vertex of `B`, without
entering `C`.  After the enlargement, the model uses at most

\[
                         m-1\le k-2                    \tag{1.10}
\]

vertices of `B`: before enlargement at most `m-q-1` old support vertices
lie in `B`, and the `q` stopped paths add exactly `q` new vertices of `B`,
their terminals.  Thus the enlarged model uses at most `m-1` vertices of
`B`.  Choose an unused vertex `z in B`.  Then

\[
             \mathcal M,\qquad V(C)\cup\{z\},\qquad\{p\}            \tag{1.11}
\]

are `k` pairwise adjacent connected branch sets.  The component `C` and
the vertex `p` both meet every model row through its vertex of `B`; the
set `C union {z}` is connected; and `pz` supplies the last adjacency.
This proves the theorem. \(\square\)

## 2. The singleton-side case

### Lemma 2.1

Let `G` be `k`-connected, let `a,b` be adjacent vertices, and suppose
they have at least `k-1` common neighbours.  If `G-{a,b}` has a
`K_{k-2}`-minor model of support order at most `k-1`, then `G` contains a
`K_k` minor or has an actual order-`k` separation.

### Proof

Let `W` be a set of `k-1` common neighbours.  Retain one root in every
model row which avoids `W`, delete the remaining model vertices together
with `a,b`, and link the retained roots to unused vertices of `W`.  If
there are `q` retained roots and the model support has order `m`, at least

\[
                         (k-1)-(m-q)\ge q
\]

targets are available.  A failed linkage gives a separator of order at
most

\[
                         (m-q)+2+(q-1)=m+1\le k;
\]

orders below `k` contradict connectivity and equality is an actual
order-`k` separation.  A successful linkage anchors every old row at a
different common neighbour, after which the old `k-2` rows together with
`{a},{b}` form a `K_k`-minor model.  The case `q=0` needs no linkage.
\(\square\)

## 3. Consequence for the balanced order-eight Hall branch

### Corollary 3.1

In the forced-theta outcome of the balanced order-eight configuration,
assume every two-vertex deletion contains a support-at-most-six `K_5`
model.  Then the host contains a `K_7` minor or has an actual order-seven
separation.

### Proof

The mixed-shore normalization gives a support-six model in `G-{p,x}`
with exactly one support vertex `v` in one open component and with that
vertex sharing its branch set with a vertex `t in S-{p,x}`.  If that open
component has another vertex, Theorem 1.1 with `k=7` applies.  If it is
the singleton `{v}`, then boundary fullness makes `p,v` adjacent with the
six common neighbours `S-{p,x}`.  Apply Lemma 2.1 to a support-at-most-six
`K_5` model in `G-{p,v}`, supplied by the hypothesis. \(\square\)

## 4. Exact contribution

Theorem 1.1 is independent of the six-vertex theta graph and of the
detailed distribution of missed boundary contacts among components of
`V-v`.  It uses only one compact labelled model, one almost-universal
boundary vertex, and the fact that the unique model vertex on the opposite
open side shares its branch set with a safe boundary vertex.  Consequently
it replaces the component-by-component exchange in the current Hall
branch by one uniform Menger argument.

The theorem does **not** turn the order-`k` separation into a strict
inductive descent, and it does not address the remaining aligned perfect-
matching trace.  In the balanced branch the exact surviving problem is to
convert that aligned four-pair boundary partition into compatible shore
colourings, the promoted split-edge linkage, or a ranked order-seven
separation.
