# A boundary-labelled near-`K_7` model at a degree-seven vertex

**Status:** written proof; separate internal audit GREEN.  This theorem is
conditional on the existence of a degree-seven vertex in a hypothetical
minor-minimal counterexample to `HC_7`.  It does not prove `HC_7`.

## Theorem

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad K_7\not\preccurlyeq G,
\]

and every proper minor of `G` is six-colourable.  Let `u` be a vertex of
degree seven and put

\[
 S=N_G(u),\qquad H=G[S].
\]

Then `G` has seven pairwise disjoint connected branch sets, one equal to
`{u}` and another equal to a singleton `{c}` with `c in S`, such that all
but at most two of the pairwise branch-set adjacencies are present.  Every
possibly missing adjacency is incident with `{c}`.

Since `G` has no `K_7` minor, at least one of those adjacencies is absent.
Thus the branch sets form a boundary-labelled model of either `K_7^-` or
the graph obtained from `K_7` by deleting two adjacent edges.

## Proof

By the separately audited degree-seven anti-neighbourhood theorem,

\[
                    C=G-N_G[u]
\]

is nonempty and connected.  Seven-connectivity makes `C` adjacent to every
vertex of `S`: if it missed `s in S`, its neighbourhood would have order at
most six.  Contracting `C` to one vertex and retaining `u` therefore gives

\[
                 \overline K_2\vee H\preccurlyeq G,       \tag{2.1}
\]

where the two independent universal vertices are `u` and the contracted
image of `C`.  In particular, `\overline K_2\vee H` has no `K_7` minor.

Put `F=\overline H`.  Dirac's neighbourhood inequality gives
`alpha(H)<=2`, so `F` is triangle-free.

We also have `chi(H)<=4`.  Indeed, apply the exact-seven boundary
classification to the actual separation with open shores `C` and `{u}`.
If `chi(H)=5`, that classification gives `H\cong K_2\vee C_5` and says
that the two open shores are connected and full.  If `p,q` are the two
universal vertices of this boundary, then
`chi(G-\{p,q\})>=5`; the established case `HC_5` supplies a `K_5` minor
in `G-\{p,q\}`.  The cycle-boundary completion theorem would then give a
`K_7` minor in `G`, a contradiction.

A proper four-colouring of the seven-vertex
graph `H` has at least three colour classes of size two, because every
colour class has size at most two.  Hence `F` has a matching of size three.

The exact matching and rooted-model theorem supplies the following input:
for every `ab in E(F)`, writing `U=S-{a,b}`, the graph `G-u-{a,b}` contains
a `U`-rooted `K_5` model

\[
                         (B_x:x\in U),                 \tag{2.2}
\]

with `x in B_x`.

### The nonisolated complement is two-connected

Every nonisolated vertex of `F` has degree at least two.  Indeed, suppose
that `a` has unique neighbour `b` in `F`.  In the rooted model (2.2), `a`
is adjacent in `H` to every root `x in U`.  Consequently

\[
                 \{u\},\quad \{a\},\quad (B_x:x\in U)
\]

are seven pairwise adjacent branch sets, contrary to
`K_7\not\preccurlyeq G`.

Let `K` be the subgraph of `F` induced by its nonisolated vertices.  Each
component of `K` has minimum degree at least two and therefore contains a
cycle.  As `F` is triangle-free, each such component has at least four
vertices.  The matching found above shows that `|V(K)|>=6`; hence `K` is
one connected component on six or seven vertices, with at most one
isolated vertex of `F` outside it.

The graph `K` is two-connected.  Otherwise its block-cutvertex tree has at
least two leaf blocks.  A leaf block cannot be a bridge, since its noncut
endpoint would have degree one in `K`.  Every leaf block is therefore a
triangle-free two-connected graph on at least four vertices.  Since
`|V(K)|<=7`, equality is forced: `K` consists of two four-cycles sharing
one cutvertex.  Write them as

\[
 v a b c v,\qquad v d e f v.
\]

Let `p,q` be the two independent universal vertices of
`\overline K_2\vee H`.  Then

\[
 \{p,v\},\ \{b,e\},\ \{a\},\ \{c\},\ \{d\},\ \{f\},\ \{q\}
\]

are seven pairwise adjacent branch sets.  The four singleton vertices are
pairwise adjacent in `H`; `{b,e}` meets each singleton; and `p,q` supply
all remaining adjacencies.  This contradicts (2.1).  Thus `K` is
two-connected.

### A degree-two vertex gives one missing edge

Suppose `a in V(K)` has degree two in `F`, with

\[
                         N_F(a)=\{b,x\}.
\]

Triangle-freeness gives `bx in E(H)`.  Apply (2.2) to `ab`.  If `a` has a
neighbour in `B_x`, then

\[
 \{u\},\quad \{a\},\quad \{b\}\cup B_x,
 \quad (B_t:t\in S-\{a,b,x\})                         \tag{2.3}
\]

are seven branch sets of a `K_7` model: `{b}\cup B_x` is connected through
the edge `bx`, the rooted bags supply their mutual adjacencies, and `a` is
adjacent in `H` to every `t in S-\{a,b,x\}`.  Therefore `a` is
anticomplete to `B_x`.  The branch sets in (2.3) then have exactly one
absent adjacency,

\[
                  \{a\}\;--\;(\{b\}\cup B_x),         \tag{2.4}
\]

and give the required boundary-labelled `K_7^-` model with singleton
centre `{a}`.

### The two exceptional complement graphs

It remains to assume `delta(K)>=3`.  If `|V(K)|=6`, then Mantel's bound
and the minimum-degree bound both give `|E(K)|=9`; equality in Mantel's
theorem yields

\[
                         K\cong K_{3,3}.
\]

The seventh vertex of `F` is isolated.

If `|V(K)|=7`, every vertex has degree at most four.  Indeed, if a vertex
`v` had degree at least five, its independent neighbourhood would leave at
most one vertex outside `N[v]`, so a neighbour of `v` would have degree at
most two.  Since a graph of odd order cannot be three-regular, some vertex
`v` has degree four.  Put `A=N_K(v)` and
`R=V(K)-N_K[v]`.  The set `A` is independent and `|R|=2`.  Every vertex of
`A` needs two neighbours besides `v`, so it is adjacent to both vertices
of `R`.  The two vertices of `R` are nonadjacent, or they would form a
triangle with any vertex of `A`.  Hence

\[
                         K\cong K_{3,4}.               \tag{2.5}
\]

For `F=K_{3,4}`, write its bipartition as

\[
 P=\{a,p_1,p_2\},\qquad Q=\{b,q_1,q_2,q_3\}.
\]

Use the rooted `K_5` model for the edge `ab` of `F`.  The seven connected
branch sets

\[
 \{u\},\ \{b\},\ \{a\}\cup B_{p_1},\ B_{p_2},
 B_{q_1},\ B_{q_2},\ B_{q_3}                          \tag{2.6}
\]

have every pairwise adjacency except possibly the two pairs joining
`{b}` to `{a}\cup B_{p_1}` and to `B_{p_2}`.  Here
`ap_1 in E(H)`, so the enlarged bag is connected; the rooted bags are
pairwise adjacent; and `b` is adjacent in `H` to all three `q_i`.

For `F=K_{3,3}\mathbin{\dot\cup}K_1`, write the bipartite component with
parts

\[
 P=\{a,p_1,p_2\},\qquad Q=\{b,q_1,q_2\},
\]

and let `r` be the isolated vertex.  Again use the rooted model for `ab`.
The seven branch sets

\[
 \{u\},\ \{b\},\ \{a\}\cup B_{p_1},\ B_{p_2},
 B_{q_1},\ B_{q_2},\ B_r                            \tag{2.7}
\]

have every pairwise adjacency except possibly the analogous two pairs
incident with `{b}`.  The vertex `r` is universal in `H`, so the contact
between `{b}` and `B_r` is present.

In (2.6) and (2.7), if both possible adjacencies were present the branch
sets would form a `K_7` model.  Thus at least one is absent, and the model
is `K_7^-` or `K_7` with two adjacent edges deleted.  This completes the
proof.  \(\square\)

## Trust boundary

The theorem aligns the deficient edges with a singleton vertex of the
literal degree-seven boundary.  It does not create either missing
adjacency while preserving the other five named bags, and it does not by
itself produce an order-seven separation whose two shore colourings agree.
Those are the remaining composition tasks.

## Dependencies

- [connected degree-seven anti-neighbourhood](hc7_degree7_anti_neighbourhood_connectivity.md)
- [exact matching languages and rooted `K_5` models](hc7_degree7_matching_bridge_bundle.md)
- [exact-seven boundary classification](hc7_exact7_no_rigid_trace.md)
- [cycle-boundary completion](hc7_cycle_boundary_completion.md)
