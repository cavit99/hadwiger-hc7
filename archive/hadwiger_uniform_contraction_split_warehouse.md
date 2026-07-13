# A uniform contraction--split warehouse theorem

## Status

This note proves a label-preserving theorem for the branch bag created by
expanding one contracted edge.  It does not assert that the bag always
splits.  Instead it proves that, after minimizing the contracted-vertex bag,
every detachable off-root piece is a genuine **multi-label warehouse**.
The minimal warehouse branches have disjoint label charges, and each one is
either incident directly with an endpoint of the contracted edge or is
separated from that edge by a full ambient adhesion.  Across the latter
adhesion, the colouring state of the original edge contraction is disjoint
from every boundary-faithful opposite warehouse operation state.

The result is uniform in the target order.  For `HC_7` it leaves at most two
minimal warehouse branches in the expanded `K_6` model.  It is a structural
advance, not a proof of `HC_7` or of the full conjecture.

## 1. Rooting a clique model at a contraction vertex

Let `H` be a connected graph, let `z in V(H)`, and suppose that `H`
contains a `K_m`-model.  A **z-rooted model** is written

\[
                         (T,C_1,\ldots,C_{m-1}),          \tag{1.1}
\]

where `z in T`.  The labels of the external bags are
`L=[m-1]`.

### Lemma 1.1 (a model can always be rooted at `z`)

If a connected graph `H` contains a `K_m`-model, then it contains one
whose union contains `z`, and hence one of the form (1.1).

#### Proof

If `z` is outside the model union, take a shortest path from `z` to that
union.  Its internal vertices avoid all old bags.  Adjoin the path, except
its endpoint already in the union, to the bag containing that endpoint.
This preserves disjointness, connectivity, and every old model adjacency.
The enlarged bag contains `z`.  Relabel it as `T`.  QED.

Among all z-rooted `K_m`-models, choose one minimizing `|T|`.  No spanning
assumption is made, and the other bags and the model union are allowed to
change during this minimization.

For a nonempty set `X subseteq T-{z}`, suppose that both `H[X]` and
`H[T-X]` are connected.  (It is automatically a proper subset of `T`
because it avoids `z`.)  Since `H[T]` is connected, the two sets are
adjacent.  Call such an `X` **z-detachable**.  Define its monopoly set by

\[
 \Lambda_T(X)=
 \{i\in L:E_H(T-X,C_i)=\varnothing\}.                   \tag{1.2}
\]

Thus a label is monopolized precisely when all old `T-C_i` contacts have
their `T` endpoint in `X`.

## 2. The minimal-bag warehouse theorem

### Theorem 2.1 (zero-delete, one-rotate, or multi-label warehouse)

In a z-rooted model minimizing `|T|`, every z-detachable set satisfies

\[
                         |\Lambda_T(X)|\ge2.             \tag{2.1}
\]

#### Proof

If `Lambda_T(X)` is empty, then

\[
                         (T-X,C_1,\ldots,C_{m-1})        \tag{2.2}
\]

is still a z-rooted `K_m`-model: the new root bag is connected, contains
`z`, and retains every labelled adjacency.  This contradicts minimality.

Suppose `Lambda_T(X)={j}`.  Every old `T-C_j` edge has its `T` endpoint in
`X`, so `C_j union X` is connected.  Replace

\[
       T\longmapsto T-X,\qquad C_j\longmapsto C_j\cup X. \tag{2.3}
\]

The two new bags are adjacent through an `X-(T-X)` edge.  The new root bag
retains its adjacency to every `C_i`, `i ne j`; the enlarged `j`-bag sees
every other external bag through the old clique model.  All other pairs are
unchanged.  Thus (2.3) is a z-rooted `K_m`-model with a smaller root bag,
again a contradiction.  QED.

The theorem is stronger than the apex-arm monopoly statement: no demand
condition saying that `X` itself meets a prescribed list of bags is needed.
Zero monopolies permit deletion, while a unique monopoly supplies exactly
the bag into which `X` rotates.

Define the direct root-defect set

\[
              \Delta_z=\{i\in L:E_H(\{z\},C_i)=\varnothing\}. \tag{2.4}
\]

### Corollary 2.2 (only root defects can be warehoused)

For every z-detachable `X`,

\[
                       \Lambda_T(X)\subseteq\Delta_z.    \tag{2.5}
\]

Consequently, if a z-detachable set exists, then `|Delta_z|>=2`.

#### Proof

The vertex `z` belongs to `T-X`.  Hence a direct edge `z-C_i` is a retained
`(T-X)-C_i` contact, so `i` cannot be in the monopoly set.  Combine this
with Theorem 2.1.  QED.

## 3. Block-level form and its exact count

If `|T|=1`, there are no rooted lobes and every assertion in this section
is vacuous.  Otherwise root the block--cutvertex tree of `H[T]` at the
cutvertex node `z` when `z` is a cutvertex and at the unique block node
containing `z` otherwise.  (As usual, a bridge is a block.)  If `q` is a
cutvertex and `K` is a component of `T-q` not containing `z`, call `K` a
**rooted lobe**.  Then `K` is z-detachable: `T-K` is connected and contains
`z`.

### Theorem 3.1 (bounded minimal warehouse branches)

Every rooted lobe `K` satisfies

\[
       |\Lambda_T(K)|\ge2,
       \qquad \Lambda_T(K)\subseteq\Delta_z.             \tag{3.1}
\]

The inclusion-minimal rooted lobes have pairwise disjoint monopoly sets.
In particular, their number is at most

\[
                      \left\lfloor {|\Delta_z|\over2}\right\rfloor.
                                                               \tag{3.2}
\]

Every rooted lobe contains an inclusion-minimal one.  If
`|Delta_z|<=1`, the root bag has no non-root block lobe at all.

#### Proof

Equation (3.1) is Theorem 2.1 and Corollary 2.2.  Rooted lobes are the
descendant vertex sets in the rooted block--cutvertex tree, so they form a
laminar family.  Distinct inclusion-minimal lobes are therefore disjoint.

For a label `i`, let `P_i` be the nonempty set of all `T` endpoints of old
`T-C_i` edges.  If `i in Lambda_T(K)`, then `P_i subseteq K`.  Two disjoint
lobes cannot both contain the same nonempty `P_i`; hence their monopoly
sets are disjoint.  Each has size at least two and lies in `Delta_z`, which
proves (3.2).  Finite descent proves the containment assertion.  QED.

The statement controls every hanging block, not merely lobes satisfying a
separate portal-demand condition.  It does not control a two-connected
root torso; that is where a genuine two-path or SPQR exchange is still
needed.

## 4. Expansion over one edge

Let `G` be a graph, let `e=xy`, let `H=G/e`, and write `z` for the
contracted vertex.  Let (1.1) be a z-rooted model in `H`, and put

\[
 B=\bigl(T-\{z\}\bigr)\cup\{x,y\}.                     \tag{4.1}
\]

The set `B` is connected in `G`: lift a spanning tree of `H[T]` and use
the edge `xy` to reconnect the two possible preimages of incidences at
`z`.  Together with the unchanged bags `C_i`, it is the standard lifted
`K_m`-model.

### Proposition 4.1 (the exact label-preserving split)

Suppose

\[
                         B=X\mathbin{\dot\cup}Y,         \tag{4.2}
\]

where `G[X]` and `G[Y]` are connected, `x in X`, and `y in Y`.  If both
`X` and `Y` are adjacent to every `C_i`, then

\[
                         X,Y,C_1,\ldots,C_{m-1}          \tag{4.3}
\]

is a `K_{m+1}`-model in `G`.

#### Proof

The sets are connected and pairwise disjoint.  The edge `xy` supplies the
`X-Y` adjacency.  Every `X-C_i` and `Y-C_i` adjacency is assumed, and all
`C_i-C_j` adjacencies come from the old clique model.  QED.

Such a connected rooted split always exists geometrically: take a spanning
tree of `G[B]` containing `xy` and delete `xy`.  Therefore, in a
`K_{m+1}`-minor-free graph the obstruction is entirely labelled.  For a
split (4.2), put

\[
 D_X=\{i:E_G(X,C_i)=\varnothing\},\qquad
 D_Y=\{i:E_G(Y,C_i)=\varnothing\}.                       \tag{4.4}
\]

Then `D_X intersect D_Y=emptyset`, because the unsplit bag `B` meets every
`C_i`, and `D_X union D_Y` is nonempty by Proposition 4.1.  Theorem 3.1
adds the nontrivial information that every off-root block branch capable of
carrying the lost contacts is charged to at least two named root defects,
and that the minimal such branches have disjoint charges.

### Theorem 4.2 (root-torso `st`-order dichotomy)

Let `R` be the block of `G[B]` containing the edge `xy`; a bridge block
`R=G[\{x,y\}]` is allowed.  For `q in V(R)`, let `A_q` consist of `q`
together with all components of `G[B-V(R)]` attached to `R` at `q`.
Then the sets `A_q`, `q in V(R)`, partition `B`, each is connected, and
edges between distinct cells project to edges of `R`.

For each model label define its effective torso portal set

\[
 Q_i=\{q\in V(R):E_G(A_q,C_i)\ne\varnothing\}.          \tag{4.5}
\]

Choose an `st`-ordering

\[
                      q_1=x,q_2,\ldots,q_n=y            \tag{4.6}
\]

of the block `R`: every intermediate vertex has an earlier and a later
neighbour.  At least one of the following conclusions holds; the proof
returns the first applicable outcome in the displayed order.

1. **Full ordered split.**  For some `t in [n-1]`, every `Q_i` meets both
   `{q_1,...,q_t}` and `{q_{t+1},...,q_n}`.  The corresponding unions of
   cells give the split in Proposition 4.1.
2. **Pinned label.**  Some effective portal set `Q_i` is a singleton.
3. **Ordered two-label lock.**  There are distinct labels `i,j` and an
   index `p` such that

   \[
     \operatorname{pos}(Q_j)\subseteq[1,p],\qquad
     \operatorname{pos}(Q_i)\subseteq[p,n].              \tag{4.7}
   \]

   The two sets may meet only at `q_p`.

#### Proof

A component of `G[B-V(R)]` has exactly one attachment vertex in `R`;
two distinct attachments together with a path through the component would
place them in a common block with that path, contrary to maximality of
`R`.  This proves the asserted cell decomposition.

The classical `st`-numbering theorem supplies (4.6) when `R` is
2-connected; for the bridge block use the order `x,y`.  Every prefix and
suffix of (4.6) is connected, because each intermediate vertex has an
earlier and a later neighbour.  Adjoining its attached cells preserves
connectivity.

If a `Q_i` is a singleton, outcome 2 holds.  Otherwise put

\[
 I_i=[\min\operatorname{pos}(Q_i),
      \max\operatorname{pos}(Q_i)-1].                    \tag{4.8}
\]

Every `I_i` is a nonempty integer interval.  A cut after position `t`
places a portal of label `i` on both sides exactly when `t in I_i`.
Hence a common point of all the intervals gives outcome 1.

If their intersection is empty, choose `i` with maximum left endpoint and
`j` with minimum right endpoint.  The interval property gives

\[
 \min\operatorname{pos}(Q_i)
   >\max\operatorname{pos}(Q_j)-1,
\]

which is (4.7) with `p=min pos(Q_i)` (or the common boundary position in
the equality case).  The labels are distinct, since one nonempty interval
cannot have its left endpoint larger than its own right endpoint.  QED.

Every component of `B-V(R)` is detachable from `B` while leaving a
connected set containing `x,y`; after contracting `xy`, it is a
z-detachable set in `T`.  Theorem 2.1 therefore says that each such hanging
component is itself a multi-label warehouse.  Theorem
4.2 reduces the remaining root-torso obstruction, without enumerating its
order, to a pinned label or an ordered pair of label classes.  Turning that
ordered pair into two disjoint repair paths is the precise SPQR/web step
still missing.

### Corollary 4.3 (an internal pin is automatically a multi-label pin)

Suppose outcome 2 of Theorem 4.2 holds, say `Q_i={q}`.  Then either
`q in {x,y}`, or at least two labels are pinned at the same torso vertex:

\[
                 |\{h:Q_h=\{q\}\}|\ge2.                 \tag{4.9}
\]

#### Proof

If `q` is not an endpoint, the cell `A_q` avoids `x,y`.  Since `R` is a
block containing the edge `xy`, deleting the internal vertex `q` leaves
`R-q` connected; after adjoining all other cells, `B-A_q` is connected.
Thus `A_q` maps after contracting `xy` to a z-detachable set in `T`.

A label `h` is monopolized by this set exactly when no cell other than
`A_q` meets `C_h`, which is exactly the condition `Q_h={q}`.  Theorem 2.1
therefore gives (4.9).  If `q` is `x` or `y`, the pin is instead an actual
endpoint charge and Theorem 2.1 does not apply.  QED.

### Theorem 4.4 (the ordered lock carries two owner corridors)

In outcome 3 of Theorem 4.2, assume the pinned-label outcome was excluded,
as in the proof there.  Let `U=Q_j` and `V=Q_i` be the two ordered owner
sets.  Then one of the following holds.

1. If `U intersect V=emptyset`, the root block contains two
   vertex-disjoint `U-V` paths with distinct endpoints in each owner set.
2. If `U intersect V={q_p}`, then `R-q_p` contains a path from
   `U-{q_p}` to `V-{q_p}`; together with the common owner vertex `q_p`
   this is a degenerate two-corridor certificate.

The nontrivial paths may be chosen with interiors disjoint from `U union V`.

#### Proof

Both owner sets have order at least two because singleton portal sets were
excluded.  In the disjoint case, no single vertex separates `U` from `V`:
after deleting any vertex, at least one vertex of each owner set remains,
and the 2-connected block remains connected.  The vertex form of Menger's
theorem gives two disjoint paths with distinct endpoints.  Truncate them at
their first and last owner vertices to clear their interiors.

In the intersecting case, (4.7) implies that the only common vertex is
`q_p`.  Each owner set has another vertex.  The graph `R-q_p` is connected,
so it contains the required path; choose a shortest one between the two
reduced owner sets to clear its interior.  QED.

Thus the cutvertex-free obstruction is not an amorphous large torso.  It is
either an endpoint pin, an internal multi-label pin, or an ordered pair of
owner classes equipped with two concrete corridors.  What remains dynamic
is to reroute those corridors while preserving all other model labels, or
to turn the failure into a boundary-faithful operation-state adhesion.

The hypotheses cannot be weakened to a static assertion that
2-connectivity alone forces the full split.  On the cycle

\[
                         x-a-b-y-x,
\]

put one portal class on `{x,a}` and another on `{b,y}`.  No connected
`x-y` partition meets both classes on both sides; the two owner corridors
are precisely the edges `xy` and `ab`.  Adding mutually adjacent external
label bags realizes this as a fixed-model example.  It is not asserted to
be z-bag-minimal, minor-critical, or target-minor-free; it shows why the
corridor must be combined with the warehouse/operation-state hypotheses.

## 5. Endpoint charge or a full adhesion

The next statement uses ambient connectivity and applies to every warehouse
lobe individually.  It does not require the clique-model bags to span `G`.

### Theorem 5.1 (endpoint charge or full separator)

Let `G` be `s`-connected and use the expansion setup of Section 4.  Let
`K` be a rooted lobe of the minimized bag `T` (viewed as the same vertex
set in `G`, since it avoids `z`).  Then one of the following holds.

1. **Endpoint charge:** `K` is adjacent in `G` to at least one of `x,y`.
2. **Full adhesion:** there is an inclusion-minimal separator `Z`, disjoint
   from `K union {x,y}`, separating the connected set `K` from the edge
   `xy`, such that

   \[
                              |Z|\ge s.                  \tag{5.1}
   \]

   If `R_K,R_e` are the components of `G-Z` containing `K` and
   `{x,y}`, respectively, then

   \[
                         N_G(R_K)=Z=N_G(R_e).             \tag{5.2}
   \]

#### Proof

If outcome 1 fails, there is no edge from `K` to `{x,y}`.  The open
neighbourhood of `K` separates it from the connected edge `xy`, so a
separator disjoint from both distinguished sets exists.  Choose an
inclusion-minimal such separator `Z`.  It is a vertex cut, so
`s`-connectivity gives (5.1).

For every `zeta in Z`, minimality supplies a path from `K` to `{x,y}` in
`G-(Z-{zeta})`.  That path passes through `zeta`, proving that `zeta` has a
neighbour in both distinguished components.  Conversely, every neighbour
outside either component lies in the separator.  This proves (5.2).  QED.

Thus connectivity cannot by itself split a warehouse.  It either places an
actual endpoint portal in that warehouse or produces a genuine full
adhesion, with no spanning-model assumption.

## 6. The contraction reference state and opposite operation states

Let `r>=1`, and suppose that `G` is proper-minor-minimal subject to not
being `r`-colourable.  Every proper minor of `G` is then `r`-colourable.
For a separation `(P,Q)` with boundary `Z=P intersect Q`, write
`Pi_Z(c)` for the equality partition induced on `Z` by a colouring `c`.

Assume that the full-adhesion outcome of Theorem 5.1 holds, and choose the
associated separation by taking `P=R_K union Z` and
`Q=V(G)-R_K`, so that

\[
             K\subseteq P-Z,qquad \{x,y\}\subseteq Q-Z. \tag{6.1}
\]

Let `Sigma_e(Z)` be the set of partitions induced on `Z` by all
`r`-colourings of `G/e`.  Let `Sigma_K(Z)` be the union of the partitions
induced by all proper minors whose nontrivial deletions and contractions
are supported entirely in `P-Z` and which retain the closed `Q`-shore
literally.

### Theorem 6.1 (warehouse/reference-state disjointness)

Under (6.1),

\[
                         \Sigma_K(Z)\cap\Sigma_e(Z)=\varnothing. \tag{6.2}
\]

#### Proof

The contraction `e=xy` is supported entirely in `Q-Z` and leaves the
closed `P`-shore unchanged.  Every warehouse-side minor in the definition
of `Sigma_K` leaves the closed `Q`-shore unchanged.  If two colourings
induced the same equality partition on `Z`, permute one palette so that the
two restrictions agree literally on `Z`.  Use the `G/e` colouring on `P`
and the warehouse-minor colouring on `Q-Z`.  Both closed shores are
represented faithfully, and there is no edge between the two open shores.
This gives an `r`-colouring of `G`, a contradiction.  QED.

In particular, deleting any vertex of `K`, deleting an internal edge of
`K`, or contracting an internal edge of `K` produces only boundary states
outside the entire reference-state set of the original contraction `e`.
This is an operation-state invariant, not merely a numerical separator.

There is also an endpoint saturation attached to the reference operation.

### Lemma 6.2 (same-colour endpoint saturation)

Let `G` be `(r+1)`-critical and let `e=xy`.  Every `r`-colouring of `G/e`,
pulled back to `G-e`, gives `x,y` one common colour `alpha`; each of `x`
and `y` has a neighbour of every colour different from `alpha`.

#### Proof

The colouring--contraction dictionary gives the common colour.  If, say,
`x` had no neighbour of a colour `beta ne alpha`, recolour `x` with
`beta`.  All edges at `x` would be proper, including `xy`, whose other end
keeps colour `alpha`.  This would be an `r`-colouring of `G`, contrary to
criticality.  The proof for `y` is symmetric.  QED.

The state theorem and endpoint saturation coexist in one contraction
reference colouring.  What is not yet proved is a colour-to-model-label
alignment forcing one of the disjoint state sets to contain the other.

### Theorem 6.3 (exact boundary trace rank of a connected bag)

Let `B` be a connected vertex set in a graph and let `Z` be any vertex
set.  Put `S=B intersect Z` and assume `|S|=p>=1`.  There is a connected
trace on terminal set `S` of total rank exactly `p-1`, whose pieces are of
the following two types:

1. an actual edge of `G[B intersect Z]`, of rank one; or
2. a connected carrier contained in one component of `G[B-Z]`, incident
   with `d>=2` vertices of `S`, of rank `d-1`.

The nontrivial carriers are pairwise vertex-disjoint.  In particular, they
are each wholly contained in a component of `G-Z`.

#### Proof

For every component `R` of `G[B-S]`, introduce an auxiliary node `rho_R`.
Form an incidence graph `Gamma_B` on

\[
              S\cup\{\rho_R:R\text{ a component of }G[B-S]\}.
\]

Join two terminals when they are adjacent in `G[B]`, and join `s in S` to
`rho_R` when `s` has a neighbour in `R`.  Contracting each component of
`G[B-S]` shows that `Gamma_B` is connected.  Choose a spanning tree `F`.

Retain every terminal--terminal edge of `F`.  For a component node
`rho_R` of degree `d`, retain a minimal connected subtree of `G[B]` inside
`R` together with its incident edges which joins the `d` boundary
terminals.  Nodes of degree zero do not occur, and nodes of degree one
carry rank zero and may be discarded.  Distinct carriers lie in distinct
components of `G[B-S]`, so they are disjoint and each lies within one
component of `G-Z`.

If `q` is the number of component nodes of `F`, `e_Z` the number of its
terminal--terminal edges, and `e_I` its incidence edges, then

\[
 e_Z+\sum_R(d_F(\rho_R)-1)
   =e_Z+e_I-q
   =(p+q-1)-q=p-1.                                      \tag{6.3}
\]

The spanning tree also shows that the resulting terminal trace is
connected.  QED.

### Corollary 6.4 (two trace units in a four-bag six-adhesion)

Suppose `Z` has order at least six and is contained in the union of four
pairwise disjoint connected named bags.  Summing the trace ranks of the
bags which meet `Z` gives at least

\[
                   |Z|-4\ge2                            \tag{6.4}
\]

units, realized by actual boundary edges or by pairwise bag-disjoint
connected carriers off `Z`.

#### Proof

If the nonempty intersections have orders `p_1,...,p_q`, where `q<=4`,
Theorem 6.3 gives total rank

\[
                         \sum_{i=1}^q(p_i-1)=|Z|-q
                         \ge |Z|-4.                       \tag{6.5}
\]

The original bags are disjoint, so carriers chosen in different bags are
also disjoint.  QED.

This converts numerical separator surplus into actual internal connection
packets.  It does **not** by itself show that the two units in (6.4) repair
the two labels monopolized by a warehouse; that requires an additional
label-ownership or operation-state alignment.  The distinction is
essential.

## 7. Application to a least-parameter Hadwiger counterexample

Assume `k` is the least parameter for which Hadwiger fails, and choose a
proper-minor-minimal counterexample `G`.  Then

\[
             \chi(G)=k,qquad
             \chi(G/e)=\eta(G/e)=k-1                  \tag{7.1}
\]

for every edge `e`.  Put `m=k-1`.  Lemma 1.1 supplies a z-rooted
`K_{k-1}`-model in `G/e`; choose it with minimum z-bag and expand it over
`e`.

Here are the dependencies in (7.1).  The graph `G` is connected, since
otherwise its proper components could be coloured separately, and hence
`G/e` is connected.  Proper-minor minimality gives
`chi(G/e)<=k-1`.  If `G/e` were `(k-2)`-colourable, lifting that colouring
to `G-e` and assigning one endpoint of `e` a new colour would
`(k-1)`-colour `G`; therefore `chi(G/e)=k-1`.  Since `G` has no `K_k`
minor, `eta(G/e)<=k-1`, while the already valid parameter `HC_{k-1}` and
`chi(G/e)=k-1` force `eta(G/e)>=k-1`.  Finally `chi(G)=k`: deletion of any
vertex is `(k-1)`-colourable and its colour can be restored with one new
colour.

The proved uniform output is:

1. a label-preserving split of the expanded bag gives a `K_k` minor;
2. every off-z block lobe of a minimized bag monopolizes at least two of
   the `k-2` external clique labels;
3. the minimal warehouse lobes have disjoint label charges, so there are
   at most

   \[
                         \left\lfloor{k-2\over2}\right\rfloor; \tag{7.2}
   \]

4. after compressing the hanging warehouses, every cutvertex-free root
   torso either splits, has an endpoint pin or internal multi-label pin, or
   has two ordered owner classes carrying a two-corridor certificate;
5. every warehouse lobe is endpoint-charged or lies behind a full adhesion
   of order at least `kappa(G)`; and
6. at a full adhesion, every boundary-faithful warehouse-side proper-minor
   state is disjoint from every state of the original edge contraction.

For `k=7`, there are five external labels and hence at most two minimal
warehouse branches.  The known seven-connectivity of a noncomplete
7-contraction-critical graph makes every non-endpoint warehouse adhesion
have order at least seven.  This is the same quantitative scale as the
double-root `P4` gate, now obtained directly and uniformly from an arbitrary
edge contraction.

For general `k`, (7.2) is linear with coefficient `1/2`, whereas the
currently available general connectivity is only linear with a much smaller
coefficient (in particular the `ceil(k/8)` bound).  The two inequalities do
not contradict one another.  The remaining uniform theorem must therefore
use the disjoint operation states or a label-preserving two-path exchange,
not connectivity alone.

## 8. Sharpness and exact remaining gap

The multi-label conclusion cannot be strengthened to a bounded number of
labels in one warehouse.  For `r>=2`, let `C_1,...,C_r` be singleton vertices inducing
a clique, let `q` be adjacent to all of them, and add the path `z-s-q`,
with no further edges at `z` or `s`.  Then

\[
                         T=\{z,s,q\},C_1,\ldots,C_r
\]

is a z-rooted `K_{r+1}`-model with minimum possible root-bag order.  Its
rooted lobe `{q}` (attached at the cutvertex `s`) monopolizes all `r`
labels.  Variants with several length-two branches at the root, each
serving a disjoint label set of order at least two, realize disjoint
monopoly sets and show that the packing count (3.2) has the right form.
These examples have low connectivity and make no claim about
minor-criticality.

For completeness, partition the `r` labels into `h` groups, each of order
at least two, replace the single path by internally disjoint paths
`z-s_j-q_j`, and join `q_j` precisely to the clique vertices in group `j`.
The displayed root bag becomes the union of all these paths.  It is
minimum.  To see this, consider any z-rooted `K_{r+1}`-model and call its
other `r` bags external.  External bags containing no clique vertex must
all lie in the same two-vertex branch (otherwise two of them are
anticomplete).  There can be at most one: two would be the separate
vertices `s_j,q_j`, and the `s_j` bag has no edge to any clique-containing
external bag (when `r=2`, they exhaust the external bags but leave the
root unable to reach the clique through their occupied branch).  If there
is one, it contains `q_j`, so all other `r-1`
external bags must contain distinct clique vertices from group `j`.  This
is impossible when there is another group.  With only one group it is
also impossible, because any clique vertex in the root could be connected
to `z` only through the already external `q_j`, while without such a
vertex the root has no edge to the clique-containing external bags.
Consequently all `r` external bags contain a clique vertex.  There are
exactly `r` such vertices, so they occur one per external bag and none is
in the root.  Since group `j` has at least two vertices, the root must
contain both `s_j` and `q_j` in order to meet all of their bags: if
`q_j` is outside, the single branch can be placed in at most one of those
external bags and hence can make at most one of them adjacent to the root.
Thus the root has at least
`1+2h` vertices, with equality in the construction.  Its `h` minimal
lobes `{q_j}` have the prescribed disjoint monopoly sets.  Taking groups
of order two, with one group of order three when necessary, realizes
`h=floor(r/2)`.

There is also a sharp `K_7`-minor-free example showing that target-minor
exclusion and z-bag minimality still do not force a static split.  Let

\[
                         C=\{c_1,c_2,c_3,c_4,c_5\}
\]

induce `K_5`, let `x,a,b,y` induce the cycle

\[
                         x-a-b-y-x,                      \tag{8.1}
\]

and add exactly the cross edges

\[
   ac_1,ac_2,\qquad bc_3,bc_4,\qquad xc_5,yc_5.          \tag{8.2}
\]

Contract `xy` to `z`.  In the resulting graph the six bags

\[
       T=\{z,c_5\},\quad D=\{a,b\},\quad
       \{c_1\},\{c_2\},\{c_3\},\{c_4\}                 \tag{8.3}
\]

form a z-rooted `K_6`-model.  The z-bag is minimum: a singleton z-bag
would have to be adjacent to five distinct other branch sets, but `z` has
only the three neighbours `a,b,c_5`.

Expanding (8.3) gives the triangle `B={x,y,c_5}`.  Each of the four
singleton external labels has `c_5` as its unique portal in `B`; hence no
`x-y` split of `B` retains even one of those labels on both sides.

Nevertheless the graph has no `K_7` minor.  The elimination order

\[
                         x,y,a,b,c_1,c_2,c_3,c_4,c_5
\]

has induced width at most five after the usual fill edges: the successive
later-neighbour counts are at most `3,3,4,5,4,3,2,1,0`.  Thus the graph has
treewidth at most five, whereas a `K_7` minor would force treewidth at least
six.

This example is not highly connected (the vertex `x` has degree three), is
5-colourable (colour `c_1,...,c_5` distinctly and take, for example,
`a,b,x,y` in the colours of `c_5,c_1,c_1,c_2`), and is not
contraction-critical at level seven.  It proves
that the dynamic full-adhesion and operation-state hypotheses in Sections
5--6 are essential; they cannot be replaced merely by z-bag minimality and
`K_7`-minor-freeness.

The exact unresolved object is now narrower than an arbitrary expanded
bag.  It is one of:

1. an endpoint pin, an internal multi-label pin, or an ordered two-owner
   corridor in the cutvertex-free root torso;
2. one of at most `floor((k-2)/2)` multi-label warehouse branches charged
   directly by `x` or `y`; or
3. a full adhesion across which the reference contraction state and every
   warehouse operation state are disjoint.

A completion requires a dynamic exchange proving that one of these three
objects either yields the label-preserving split of Proposition 4.1 or
forces two opposite proper-minor states to agree.  The present theorem does
not assume that conclusion and does not repackage it as an equivalence.
