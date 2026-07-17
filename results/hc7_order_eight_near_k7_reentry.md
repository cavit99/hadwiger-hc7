# Near-`K_7` re-entry at the exceptional order-eight separation

**Status:** written proofs with a separate GREEN internal audit in
[`hc7_order_eight_near_k7_reentry_audit.md`](hc7_order_eight_near_k7_reentry_audit.md).
This note does not close the order-eight case or prove `HC_7`.

## 1. Exact setup

Let `G` be a seven-connected graph with chromatic number seven such that
every proper minor is six-colourable.  Assume that `G` has no `K_7` minor
and that

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},\qquad |R|=3,                 \tag{1.1}
\]

is an eight-vertex separator with the following properties.

1. `R` is a clique.
2. `e` and `f` are vertex-disjoint edges and are anticomplete to one
   another.
3. Each of `e,f` is collectively adjacent to every vertex of `R`.
4. `G-S` has exactly two components `C,D`, and each component is adjacent
   to every literal vertex of `S`.

In a hypothetical critical counterexample, this is the exceptional
two-component output of Lemma 6.1 in
[`../results/hc7_star_kernel_rooted_four_contraction.md`](../results/hc7_star_kernel_rooted_four_contraction.md).

Write

\[
                         H=G-\{e,f\},                         \tag{1.2}
\]

where the braces in (1.2) mean deletion of the two edges, not deletion of
their endpoints.

## 2. An explicit branch-set split which repairs the missing adjacency

For a component `U in {C,D}` and an ordered pair `(g,h)` equal to `(e,f)`
or `(f,e)`, call disjoint connected nonempty subgraphs `X,Y subseteq U` a
**repair split oriented from `g` to `h`** when

\[
\begin{array}{ll}
\text{(i)}&X\text{ is adjacent to both }g\text{ and }h,\\
\text{(ii)}&Y\text{ is adjacent to }x,h,
                  \text{ and every vertex of }R,\\
\text{(iii)}&X\cup V(g)\text{ is adjacent to }Y\cup\{x\}.
\end{array}                                                \tag{2.1}
\]

Adjacency to an edge means adjacency to at least one of its two endpoints.

### Lemma 2.1 (repair-split completion)

If either component admits a repair split in either orientation, then `G`
contains a `K_7` minor.

### Proof

Suppose `X,Y subseteq C` satisfy (2.1), oriented from `g` to `h`, and let
`D` be the opposite component.  The following seven sets are branch sets:

\[
        g\cup X,\quad h,\quad Y\cup\{x\},\quad D,
        \quad \{r\}\ (r\in R).                              \tag{2.2}
\]

They are pairwise disjoint and connected.  The first two are adjacent
through an `X-h` edge; the first and third by condition (iii); and the
second and third through a `Y-h` edge.  The third and fourth are adjacent
through an `x-D` edge.  Full adjacency of `D` supplies all of its remaining
edges to the boundary-derived branch sets.  Finally, collective adjacency
of `g,h` to `R`, condition (ii), and the fact that `R` is a clique supply
every adjacency involving its three singleton branch sets.  Thus (2.2) is
a `K_7`-minor model.  The other component and orientation are symmetric.
\(\square\)

This criterion is label-preserving: it repairs the unique absent adjacency
between the two specified edge branch sets and retains the three specified
singleton branch sets.  Condition (iii) deliberately includes both an
internal `X-Y` edge and the alternative in which `x` is adjacent to `X`;
these are two different valid ways to join the first and third bags.

### Corollary 2.2 (attachment-tree test)

Let `T` be a tree in one component `U` which contains a selected neighbour
in `U` of every vertex of `S`.  If an edge of `T` has components `T_1,T_2`
such that, in one of the two orientations,

\[
\begin{array}{c|c}
T_1&\text{has neighbours in both }g\text{ and }h\\
T_2&\text{has neighbours at }x,h\text{ and every }r\in R,
\end{array}                                                \tag{2.3}
\]

then `G` contains a `K_7` minor.

### Proof

The two components of `T` are connected and adjacent through the deleted
tree edge.  They satisfy Lemma 2.1 with `X=T_1` and `Y=T_2`.  \(\square\)

Thus failure of the labelled repair has an exact representation on every
attachment-spanning tree: every oriented tree edge fails at least one of
the six named boundary requirements in (2.3).  This is the appropriate
finite label set for a tree-separator or point--tree argument; no claim is
made that the failed requirements have a common vertex transversal.

The following elementary subtree lemma gives exactly the transversal which
is valid.

### Lemma 2.3 (two-family subtree alternative)

Let `T` be a tree and let `mathcal A,mathcal B` be two nonempty families of
subtrees of `T`.  If no member of `mathcal A` is vertex-disjoint from a
member of `mathcal B`, then either

\[
       \bigcap_{A\in\mathcal A}V(A)\ne\varnothing
       \qquad\hbox{or}\qquad
       \bigcap_{B\in\mathcal B}V(B)\ne\varnothing.          \tag{2.4}
\]

### Proof

If the members of `mathcal A` pairwise intersect, the Helly property for
subtrees of a tree gives the first conclusion.  Otherwise choose disjoint
`A_1,A_2 in mathcal A`.  Every `B in mathcal B` meets both.  Since `B` is
connected, it contains the unique fixed path in `T` with one end in
`A_1`, one end in `A_2`, and no internal vertex in either subtree.
Consequently every member of `mathcal B` contains every vertex of that
nonempty path.  This gives the second conclusion.
\(\square\)

### Corollary 2.4 (exact obstruction on an attachment tree)

Fix a component `U`, a tree `T subseteq U` which meets every boundary
neighbourhood, and an orientation `(g,h)`.  For a boundary subgraph or
vertex `q`, put

\[
                         P_q=N_U(q)\cap V(T),                 \tag{2.5}
\]

where `N_U(g)` and `N_U(h)` mean the union of the neighbourhoods of their
two endpoints.  Let `mathcal A_{g,h}` be all subtrees of `T` meeting both
`P_g,P_h`, and let `mathcal B_h` be all subtrees meeting each of

\[
                         P_x,P_h,P_{r_1},P_{r_2},P_{r_3}.     \tag{2.6}
\]

If `G` has no `K_7` minor, then at least one of the following holds.

1. One vertex of `T` belongs to every `P_g`--`P_h` connector subtree.
2. One vertex of `T` belongs to every subtree meeting all five sets in
   (2.6).

### Proof

If some `A in mathcal A_{g,h}` and `B in mathcal B_h` are disjoint, enlarge
`A` along the unique `A-B` path in `T` until the two subtrees are adjacent.
The enlarged `A` and `B` satisfy (2.1), so Lemma 2.1 gives a `K_7` minor.
Thus the two subtree families are cross-intersecting, and Lemma 2.3 gives
exactly the two conclusions above.  \(\square\)

The first outcome is an ordinary one-vertex separator for the two portal
sets inside `T`: after deleting that vertex, no component of the tree meets
both sets.  In the second outcome, after deleting the transversal vertex,
no component of the tree meets all five portal sets in (2.6).  It is a
one-vertex transversal for the specified five-terminal Steiner subtrees.
It does not imply that the same vertex
works for a different attachment tree, the opposite orientation, or the
other component.  Aligning these tree transversals with the colour-forced
separators in Lemma 3.3 is the remaining global step.

### Lemma 2.5 (minimal attachment-tree normal form)

Fix one component `U`.  For each vertex `s in S`, choose a neighbour
`p_s in U`, and let `P` be the set of distinct chosen vertices.  Among all
such choices and all trees in `U` containing `P`, choose `P,T`
lexicographically to minimize

\[
                         (|V(T)|,|P|).                       \tag{2.7}
\]

Then every vertex `w in U-V(T)` satisfies

\[
                         |N_U(w)\cap V(T)|\leq |P|+1\leq9.   \tag{2.8}
\]

### Proof

By minimality, every leaf of `T` belongs to `P`.  If `|P|=1`, then `T`
has one vertex, so (2.8) is immediate.  Assume `|P|>=2`, and suppose that
`w` has a set `N` of at least `|P|+2` neighbours in `T`.  For each
`p in P`, take a shortest path `Q_p` in `T` from `p` to `N`, and denote
its last vertex by `y_p`.  The path contains no other vertex of `N`.
Consequently

\[
 T' = \bigcup_{p\in P} Q_p
      \;\cup\;\{w y_p:p\in P\}                              \tag{2.9}
\]

is connected, contains `P union {w}`, and avoids every vertex of
`N-{y_p:p in P}`.  At least two vertices of `T` are therefore omitted
and only `w` is added.  A spanning tree of `T'` containing `P` has fewer
vertices than `T`, contradicting (2.7).  This proves the first inequality;
the second follows from `|P|<=|S|=8`.  \(\square\)

The strict-threshold argument is the one-component case of the forest
reduction in [Kawarabayashi--Yu, arXiv:2606.01586, Theorem
4](https://arxiv.org/abs/2606.01586).  Lemma 2.5 supplies a well-founded
attachment-tree parameter.  It does not classify the tight value
`|N_T(w)|=|P|+1`, and seven-connectivity does not itself force a vertex to
reach the strict threshold.  The extremal forest theorem cannot be applied
from connected-tree minimality alone: a counterexample to that proposed
connected-tree subdivided-star corollary is recorded in
[`../barriers/kawarabayashi_yu_forest_extremal_structure_counterexample.md`](../barriers/kawarabayashi_yu_forest_extremal_structure_counterexample.md).

## 3. The common host has two opposite colouring witnesses

### Lemma 3.1 (common-host structure)

The graph `H` is five-connected and has chromatic number six.  It contains a
spanning `K_6`-minor model.  Moreover there are six-colourings `c_f,c_e`
of `H` with the following properties:

\[
\begin{array}{c|cc}
 &e&f\\ \hline
c_f&\text{ends different}&\text{ends equal}\\
c_e&\text{ends equal}&\text{ends different}.
\end{array}                                                \tag{3.1}
\]

There is also a six-colouring of `H` in which both endpoint pairs are
monochromatic, and no six-colouring of `H` makes both pairs bichromatic.

### Proof

For any two vertices `s,t`, seven-connectivity supplies seven internally
vertex-disjoint `s-t` paths in `G`.  Each of the two deleted edges occurs
on at most one path in such a family, so at least five paths remain in
`H`.  Menger's theorem gives `kappa(H)>=5`.

The cross-edges between `e` and `f` are absent, so Theorem 2.1 and
Corollary 3.1 of
[`../results/hc7_common_edge_deletion_k6_fork.md`](../results/hc7_common_edge_deletion_k6_fork.md)
give `chi(H)=6`, the two colourings in (3.1), and the impossibility of the
fourth pattern.  Hadwiger's conjecture for parameter six gives a `K_6`
minor in `H`; connectedness lets one absorb every vertex outside its model
union into an adjacent branch set, making the model spanning.

Contracting both disjoint edges gives a proper minor of `G`.  A
six-colouring of that minor expands to a six-colouring of `H` in which both
endpoint pairs are monochromatic.  \(\square\)

The next lemma extracts geometric information from the two opposite
colourings.  It is the new criticality input of this note.

### Lemma 3.2 (three colour-protected Kempe connectors)

Write `f=uv`.  In the colouring `c_f`, put

\[
 c_f(u)=c_f(v)=\alpha,qquad
 \{c_f(a),c_f(b)\}=\{\rho,\sigma\},\quad e=ab,
                                                                  \tag{3.2}
\]

where `rho != sigma`.  For every colour

\[
                  \beta\notin\{\alpha,\rho,\sigma\},             \tag{3.3}
\]

the vertices `u,v` lie in one component of the subgraph of `H` induced by
colours `alpha,beta`.  Consequently `H` contains at least three
`u-v` paths, one for each of at least three different choices of `beta`,
whose vertices use only `alpha` and that path's second colour.
Every such path avoids each endpoint of `e` whose colour is not `alpha`;
in particular it avoids both endpoints of `e` when `alpha` is different
from `rho,sigma`, and it always avoids at least one endpoint of `e`.

The symmetric assertion holds for the endpoints of `e` in `c_e`, with
the two endpoint colours of `f` excluded.

### Proof

Fix a colour `beta` satisfying (3.3).  Suppose that `u` and `v` lie in
different `alpha-beta` components of `H`.  Interchange `alpha` and `beta`
on the component containing `u`.  The edge `f` becomes proper when it is
restored.

The edge `e` remains proper.  If `alpha` is different from `rho,sigma`,
neither endpoint of `e` changes colour.  If, say, `alpha=rho`, then the
endpoint of `e` of colour `alpha` may change to `beta`, but the other
endpoint still has colour `sigma`, and `beta != sigma` by (3.3).  The
case `alpha=sigma` is symmetric.  Every other edge remains proper under a
Kempe interchange.  Restoring both `e` and `f` would therefore give a
six-colouring of `G`, a contradiction.

Thus `u,v` lie in the same `alpha-beta` component.  A path between them in
that component lies in `H`: the only edge present in `G-f` but absent from
`H` is `e`, and its endpoint colours are `rho,sigma`; by (3.3) it is not
an `alpha-beta` edge.  A vertex whose colour is outside `\{alpha,beta\}`
does not lie on the path, which gives the endpoint-avoidance assertion.
Finally, the set in (3.3) has order at least three:
`rho,sigma` are distinct, and `alpha` either is one of them or adds only
one further excluded colour.  This proves the assertion for `f`; the
other assertion is symmetric.  \(\square\)

The same proof is uniform.  If `q>=3`, `G` is not `q`-colourable, and a
`q`-colouring of `G-{e,f}` makes `e` bichromatic and `f` monochromatic,
then the ends of `f` have a bichromatic path in the common deletion graph
for every second colour outside the common colour and the two endpoint
colours of `e`.  Hence there are at least `q-3` protected second colours.
No connectivity or minor hypothesis is needed for this uniform statement;
the exact endpoint pattern is the essential input.

The paths in Lemma 3.2 need not be mutually vertex-disjoint.  Paths with
different second colours can meet internally only at vertices of the
common colour, which is the precise remaining concentration phenomenon.

### Lemma 3.3 (protected cycle or a common-colour separator)

In the notation of Lemma 3.2, for every colour `beta` satisfying (3.3),
let `K_beta` be the `alpha-beta` component of `H` containing `u,v`, and put

\[
                         K_f=\bigcup_\beta K_\beta.              \tag{3.4}
\]

Exactly one of the following alternatives holds.

1. `K_f` contains two internally vertex-disjoint `u-v` paths; their union
   contains a cycle through `u,v` and uses only the protected colour
   components from Lemma 3.2.
2. There is a vertex `z_f notin {u,v}` which separates `u` from `v` in
   `K_f`.  Every such one-vertex separator has colour `alpha` and belongs
   to every `K_beta`.

The symmetric dichotomy gives either two protected paths for `e` or a
common-colour separator `z_e` in the union defined from `c_e`.

### Proof

The graph `K_f` is connected and contains `u,v`.  If it has two internally
vertex-disjoint `u-v` paths, item 1 holds.  Otherwise the vertex form of
Menger's theorem gives a one-vertex `u-v` separator `z_f` in `K_f`; the
edge `uv=f` is absent from `H`, so the separator is different from the
ends.

For each protected colour `beta`, the connected graph `K_beta` contains a
`u-v` path.  Since `z_f` separates `u,v` in their union, it belongs to
every `K_beta`.  There are at least three distinct protected colours.  A
vertex common to an `alpha-beta` component and an `alpha-gamma` component,
where `beta != gamma`, must have colour `alpha`.  Hence `c_f(z_f)=alpha`.
The symmetric assertion is identical.  \(\square\)

### Lemma 3.4 (three neighbours on each side of a protected separator)

Assume the second outcome of Lemma 3.3, and let `U_f,V_f` be the
components of `K_f-z_f` containing `u,v`, respectively.  For every
protected colour `beta`, the vertex `z_f` has a neighbour of colour
`beta` in `U_f` and a neighbour of colour `beta` in `V_f`.  In particular,

\[
 |N_H(z_f)\cap U_f|\geq 3,
 \qquad |N_H(z_f)\cap V_f|\geq 3.                         \tag{3.5}
\]

The corresponding assertion holds for `z_e` in the symmetric colouring.

### Proof

Fix a protected colour `beta` and take a `u-v` path in `K_beta`.  Since
`z_f` separates `u` and `v` in `K_f`, the path contains `z_f`.  Its two
edges incident with `z_f` lead, on the two subpaths, to vertices in
`U_f` and `V_f`.  Lemma 3.3 says that `z_f` has colour `alpha`; properness
of the colouring therefore makes both neighbours have colour `beta`.
Neighbours obtained for different protected colours are distinct.  There
are at least three such colours by Lemma 3.2, proving (3.5).  \(\square\)

After fixing the two colourings and choosing one separator in each
separator outcome, they nominate a set `{z_e,z_f}` of order at most two.
Lemma 3.3 does **not** assert that this
pair meets every `K_5` model; proving that completeness property, or using
one of the protected cycles to obtain a repair split, is the remaining
composition problem.

## 4. Exact near-clique re-entry theorem

### Theorem 4.1

Under the hypotheses of Section 1, all of the following hold
simultaneously.

1. The seven branch sets

   \[
       C\cup\{x\},\quad D,\quad e,\quad f,
       \quad\{r\}\ (r\in R)                              \tag{4.1}
   \]

   form a spanning `K_7`-minus-one-edge model, whose unique missing
   branch-set adjacency is `e-f`.
2. The common edge-deletion graph `H` is five-connected and has the
   spanning `K_6` model and the three attainable endpoint-equality patterns
   of Lemma 3.1.
3. Each opposite one-edge-deletion colouring supplies at least three
   colour-protected endpoint connectors in `H`, as in Lemma 3.2.
4. For each specified edge, those connectors either contain two internally
   disjoint endpoint paths or nominate one common-colour separator vertex
   having at least three neighbours on each endpoint side, as in Lemmas
   3.3 and 3.4.
5. Neither `C` nor `D` admits a repair split in either orientation.

### Proof

For item 1, the displayed sets are disjoint, connected, and cover `V(G)`.
The component `D` is adjacent to `C union {x}` through an `x-D` edge.
Fullness supplies every adjacency from the two component-derived sets to
`e,f,R`; collective adjacency of `e,f` supplies their edges to the three
singletons in `R`; and `R` is a clique.  The only missing pair is `e-f`.
Items 2--4 are Lemmas 3.1--3.4 above.  Item 5 follows from Lemma 2.1
and the assumption that `G` has no `K_7` minor.  \(\square\)

The theorem replaces the unstructured phrase "repair a spanning
near-`K_7` model" by two exact objects in one common host:

- a label-preserving connected-subgraph split whose occurrence gives the
  seven branch sets immediately; and
- two families of at least three colour-protected Kempe connectors forced
  by proper-minor criticality, each compressed to a protected cycle or one
  common-colour separator vertex.

## 5. Falsification boundary and sharpened target

Seven-connectivity and a spanning `K_7^-` model do not force `K_7`.  The
graph $K_2\vee I$, where `I` is the icosahedral graph, is seven-connected,
`K_7`-minor-free, and has explicit spanning `K_7^-` models; deleting the
two vertices of the `K_2` leaves the planar graph `I`.  The explicit models
and inverse branch-set pivots are verified in
[`../barriers/hc7_near_k7_rotation_involution_barrier.md`](../barriers/hc7_near_k7_rotation_involution_barrier.md).
Thus a connectivity-only repair theorem is false, while the correct
alternative in that construction is one coherent two-vertex planarizing
set.

The exact remaining local theorem suggested by Theorem 4.1 is therefore:

> **Protected-connector split-or-pair target.**  In the setup of Section 1,
> the two opposite colouring witnesses and their protected Kempe connectors
> force either a repair split in `C` or `D`, or a two-vertex set `Z` such
> that `G-Z` has no `K_5` minor.

Either conclusion closes this residue.  The first gives `K_7` by Lemma
2.1.  In the second, `G-Z` is five-connected.  The standard
four-connected consequence of Wagner's characterization makes every
four-connected `K_5`-minor-free graph planar; the Four Colour Theorem plus
two fresh colours then six-colours `G`.

This is strictly narrower than a connectivity-only near-`K_7` theorem.  It
uses an actual two-component order-eight separation, two specified
two-vertex branch sets, and the proper-minor colourings in their common
edge-deletion graph.  Lemma 3.3 gives the concrete candidate
`Z={z_e,z_f}` when both protected unions have packing number one.  The two
remaining obligations are now explicit: show that a protected cycle yields
a repair split, or show that the nominated pair meets every `K_5` model.
The icosahedral construction shows why the latter may be the correct
outcome rather than a branch-set split.
