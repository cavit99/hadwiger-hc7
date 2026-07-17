# The one-vertex forest reduction does not lift through a contracted component

**Status:** written proof; independent audit pending.  The positive lemma
below is a label-preserving specialisation of the forest reduction of
Kawarabayashi--Yu.  The infinite family in Section 3 identifies why that
lemma cannot be applied after first contracting an arbitrary exterior
component.  This is a barrier to one proposed near-`K_7` simplification
mechanism, not a counterexample to `HC_7`.

## 1. Models reduced to attachment-spanning trees

Let `R` be a fixed graph on labels `1,...,r`, and let

\[
                         (X_1,\ldots,X_r)                 \tag{1.1}
\]

be a labelled `R`-minor model in a graph `G`.  For every edge `ij` of
`R`, select one literal model edge with one endpoint in `X_i` and the
other in `X_j`.  Let `S_i` be the set of selected endpoints in `X_i`.
Inside `G[X_i]`, choose an inclusion-minimal tree `T_i` containing
`S_i`.  Every leaf of `T_i` belongs to `S_i`.

Replacing `X_i` by `V(T_i)` for every `i` preserves all selected model
edges.  Thus the `T_i` themselves are branch sets of the same labelled
model.  Call this an **attachment-tree reduction** of (1.1).

For `R=K_7^\vee`, every set `S_i` has order at most six, and the branch
set at the common endpoint of the two missing edges has `|S_i|<=4`.

## 2. The valid atomic exchange

### Lemma 2.1 (label-preserving one-vertex insertion)

Let `(T_1,...,T_r)` be an attachment-tree reduction of a labelled
`R`-model.  Fix `i` with `|S_i|>=2`, and let

\[
               u\in V(G)-\bigcup_{j=1}^r V(T_j).
\]

If

\[
                     |N_G(u)\cap V(T_i)|\ge |S_i|+2,     \tag{2.1}
\]

then there is a tree `T_i'` in `G[V(T_i)\cup\{u\}]` such that

\[
 S_i\cup\{u\}\subseteq V(T_i'),\qquad
 |V(T_i')|<|V(T_i)|,
\]

and every leaf of `T_i'` belongs to `S_i`.  Consequently

\[
              (T_1,\ldots,T_{i-1},T_i',T_{i+1},\ldots,T_r)
                                                               \tag{2.2}
\]

is a labelled `R`-model with strictly smaller total branch-set order.
If the original model avoids a prescribed set `P` and `u\notin P`, the
new model also avoids `P`.

#### Proof

Apply Theorem 4 of Kawarabayashi--Yu to the one-component forest `T_i`,
the boundary set `S_i`, and the outside vertex `u`.  In the
one-component case its threshold is exactly (2.1), and its conclusion is
a strictly smaller tree containing `u` and spanning `S_i`, with every
leaf in `S_i`.

All selected model edges incident with label `i` have their `T_i`-end in
`S_i`, so all survive in `T_i'`.  Every other selected model edge is
unchanged.  The branch sets remain connected and pairwise disjoint because
`u` was outside their union.  This proves (2.2).  The final assertion is
immediate.  \(\square\)

The cited result is Theorem 4 of Ken-ichi Kawarabayashi and Gexin Yu,
*Connectivities for k-knitted graphs and for minimal counterexamples to
Hadwiger's Conjecture*, arXiv:2606.01586v2 (2026),
<https://arxiv.org/abs/2606.01586>.

Thus a model minimal under total attachment-tree order satisfies the
useful but purely local inequality

\[
                |N_G(u)\cap V(T_i)|\le |S_i|+1          \tag{2.3}
\]

for every vertex `u` outside the model.  The equality theorem in the same
paper classifies an irreducible one-tree instance at equality as a
subdivided star with a specified neighbourhood pattern.  That
classification is internal to `G[V(T_i)\cup\{u\}]`: it does not control
edges from the star arms to the other branch sets or to unused vertices.
Its centre is therefore not, without an additional attachment theorem, a
separator of the ambient graph.  This is the same quantifier boundary
exhibited by the existing
[single-attachment/block-cut barriers](hc7_near_k7_single_portal_block_cut_barrier.md).

## 3. Contracting an exterior component destroys the strict rank

The tempting next step is to contract a connected component outside the
model to one vertex and apply Lemma 2.1.  The following family shows that
strict order reduction in that quotient need not lift to strict order
reduction in the original graph.

For `m>=3`, let

\[
 T=s v_1v_2v_3v_4 t,
 \qquad
 C_m=c_1c_2\cdots c_m                                  \tag{3.1}
\]

be disjoint paths.  Add precisely the four edges

\[
          c_1v_1,\quad c_1v_2,\quad c_mv_3,\quad c_mv_4. \tag{3.2}
\]

Take the boundary set `S={s,t}`.  Contracting `C_m` to a vertex `u`
makes `u` adjacent to all four of `v_1,v_2,v_3,v_4`.  In the quotient,

\[
                         s v_1 u v_4 t                  \tag{3.3}
\]

is a five-vertex tree spanning `S` and containing `u`, strictly smaller
than the six-vertex tree `T`.

### Proposition 3.1 (unbounded lifting cost)

In the contracted graph, every tree `\overline T` which contains
`s,t,u`, has all its leaves in `{s,t}`, and satisfies

\[
                     |V(\overline T)|<|V(T)|=6
\]

is exactly the path (3.3).  Every lift of that path through a connected
subgraph of `C_m` has at least `m+4` vertices.  In particular its order
is greater than `|V(T)|` for `m>=3`.

#### Proof

A finite tree containing `s,t` and having no leaf outside `{s,t}` is an
`s`--`t` path.  In the quotient, a path using `u` enters it from some
`v_i` and leaves it through some `v_j`, where `1<=i<j<=4`.  Its order is

\[
                         (i+1)+1+(6-j)=8+i-j.
\]

This is less than six only when `(i,j)=(1,4)`.  Hence (3.3) is the
unique strict quotient reduction.

Any lift of its two edges `v_1u,uv_4` must meet `C_m` at both `c_1` and
`c_m`.  A connected subgraph of the path `C_m` containing those vertices
contains all `m` vertices.  Therefore the shortest lift is

\[
                         s v_1 C_m v_4 t,
\]

which has `m+4` vertices.  For `m>=3` this is at least seven.  \(\square\)

This example embeds verbatim into a labelled `K_7^\vee` model: add six
pairwise adjacent singleton branch sets `B,C,U_1,U_2,U_3,U_4`, join `s`
to `U_1,U_2`, join `t` to `U_3,U_4`, and use `T` as the branch set at the
common endpoint of the two missing edges.  The four selected attachment
vertices are still just `s,t`.  Contracting `C_m` creates the strict
quotient reduction (3.3), but every lift which actually uses the exterior
component increases the attachment-tree order.

The embedded family is not seven-connected or contraction-critical.  Its
role is narrower: it disproves the inference that the strict numerical
conclusion of the unweighted forest theorem survives contraction and
lifting of an arbitrary connected exterior piece.

## 4. Exact missing hypotheses

The obstruction leaves two genuinely different requirements.

1. **A weighted connector bound.**  If a contracted exterior component
   is represented by `u`, its weight must be the minimum order of a
   connected subgraph of that component meeting the attachment vertices
   used by the reduced tree.  A quotient reduction is useful only when
   the number of removed tree vertices exceeds that weight.  Ordinary
   seven-connectivity bounds the size of the component's neighbourhood;
   it does not bound this internal connector weight.
2. **Compatibility with the selected private pair.**  The support-six
   invariant concerns models in `G-P` for a prescribed two-vertex set
   `P`.  Lemma 2.1 preserves this information only when the starting model
   already avoids `P` and the inserted vertex is outside `P`.  The
   guaranteed `K_7^\vee` model is a model in `G`, whereas the present
   global input in `G-P` is only a `K_5` model.  No existing theorem in
   the repository aligns those two models.

There is a further issue with using the multi-component clause after a
designated deletion.  If `p\in V(T_i)` and `F=T_i-p`, a forest replacement
which is later to be rejoined through `p` must preserve the relevant
vertices of `N_{T_i}(p)` as well as the selected model-edge endpoints
`S_i`.  Otherwise adding `p` back need not connect the returned pieces.
Thus the boundary in the forest theorem is, without another reconnection
argument, at least

\[
                        S_i\cup N_{T_i}(p).              \tag{4.1}
\]

The multi-component threshold is one more than the order of this set.
Moreover its conclusion may reduce the number of components without making
the forest connected; a model avoiding `p` requires the latter.  Iterating
the reduction would require further actual high-contact vertices, all
avoiding the prescribed pair.  Neither seven-connectivity nor the present
dominating-model input supplies them.

Seven-connectivity also supplies only

\[
                           |N_G(C)|\ge7
\]

for an exterior component `C`.  It does not force one literal vertex of
`C` to have `|S_i|+2` neighbours in a specified attachment tree.  A
dominating `K_5` model similarly supplies one neighbour in each earlier
branch set for each later vertex, not the concentrated incidence (2.1).

Therefore the forest reduction is a sound **atomic** exchange, but it is
not yet a bridge from the guaranteed near-`K_7` model to the current
private-pair invariant.  Such a bridge needs either a literal high-contact
vertex outside a pair-avoiding model, or a new weighted forest theorem
whose connector cost and prescribed-pair avoidance are both part of the
hypotheses.  Without one of these additions, the proposed lexicographic
rank is not well founded under component absorption.
