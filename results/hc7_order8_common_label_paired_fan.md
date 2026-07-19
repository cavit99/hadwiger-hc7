# Common-label paired paths at a boundary-full order-eight separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_common_label_paired_fan_audit.md`](hc7_order8_common_label_paired_fan_audit.md).
The first
theorem forces two vertex-disjoint boundary edges with different inherited
common-branch-set labels in every non-singleton boundary-full component.
The second theorem turns those edges into either five paths with prescribed
literal first-hit labels or a strictly smaller component behind an actual
order-seven separation carrying both edge-deletion responses.  The fan
outcome is still an input to the open label-preserving branch-set exchange;
this note does not by itself produce a `K_7` minor or prove `HC_7`.

## 1. Labelled order-eight setting

Let `G` be seven-connected.  Let `S` be an eight-vertex set such that
`G-S` has at least two components, and let `C` be one of those components.
Assume that `C` is adjacent to every literal vertex of `S`.

The boundary carries the inherited labels of a spanning labelled
`K_7`-minus-one-edge model:

\[
 S=\{k_1,k_2\}\mathbin{\dot\cup}
   \{s_X,s_Y,s_D,s_{F_1},s_{F_2},s_{F_3}\}.             \tag{1.1}
\]

The vertices `k_1,k_2` have the same label `U`.  Every other displayed
vertex has its displayed label.  The five labels

\[
                         U,D,F_1,F_2,F_3                \tag{1.2}
\]

will be called the **common model labels**: their branch sets are pairwise
adjacent in the inherited near-complete model.  This terminology describes
ordinary branch-set labels, not colours in a six-colouring.

## 2. Two differently labelled boundary edges

### Theorem 2.1 (common-label contact matching)

If `|C|>1`, then there are vertex-disjoint edges

\[
                    e=a_1s_i,\qquad f=a_2s_j,           \tag{2.1}
\]

where `a_1,a_2` are distinct vertices of `C` and `s_i,s_j` are distinct
members of

\[
                         R=\{s_D,s_{F_1},s_{F_2},s_{F_3}\}. \tag{2.2}
\]

In particular, the two boundary ends have different inherited common-model
labels.  The only possible failure of (2.1) is the singleton component
`C={a}`.

#### Proof

Consider the bipartite graph formed by the edges of `G` between `C` and
`R`.  Every member of `R` has a neighbour in `C`, by boundary-fullness.
Suppose this bipartite graph has no matching of order two.

Choose one incident edge for each of the four vertices in `R`.  The four
chosen ends in `C` must all be one vertex, say `a`: edges to two distinct
vertices of `R` with different ends in `C` would be a matching.  Moreover,
every further edge between `C` and `R` is incident with `a`, since such an
edge with an end different from `a` can be paired with an edge from `a` to
one of the other three vertices of `R`.  Thus

\[
                         E_G(C-a,R)=\varnothing.        \tag{2.3}
\]

If `|C|>1`, let `W` be a component of `G[C-a]`.  Since `C` is a component
of `G-S`, componenthood and (2.3) give

\[
             N_G(W)\subseteq\{a,k_1,k_2,s_X,s_Y\}.     \tag{2.4}
\]

Another component of `G-S` lies outside `W\cup N_G(W)`, so (2.4) is a
nontrivial separation of order at most five.  This contradicts
seven-connectivity.  Hence the bipartite contact graph has a matching of
order two, which is precisely (2.1). \(\square\)

### Corollary 2.2 (the edges are operation-critical)

Assume additionally that

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\quad\hbox{for every proper minor }M\hbox{ of }G.
                                                               \tag{2.5}
\]

Every proper six-colouring of `G-e` gives `a_1,s_i` one colour, and every
proper six-colouring of `G-f` gives `a_2,s_j` one colour.  Contracting both
edges and expanding a six-colouring gives a colouring of
`G-\{e,f\}` in which both endpoint pairs are monochromatic.  Thus the two
labelled crossing edges carry the standard one-edge and common-contraction
responses.

#### Proof

The required six-colourings exist by (2.5).  If the ends of a deleted edge
had different colours, restoring that edge would give a proper
six-colouring of `G`.  The simultaneous assertion follows by colouring the
proper minor `G/e/f` and expanding its two distinct contraction vertices.
\(\square\)

## 3. Paired-source fan or strict order-seven descent

Choose the edges in Theorem 2.1.  Select one of `k_1,k_2`, say `k_1`, and
put

\[
                  T=\{k_1,s_D,s_{F_1},s_{F_2},s_{F_3}\}. \tag{3.1}
\]

Thus `T` contains exactly one representative of each common model label,
and it contains `s_i,s_j`.  Let `P` be an `a_1`--`a_2` path in `G[C]`.

### Theorem 3.1 (paired-source alternative)

At least one of the following holds.

1. There are five paths from `P` to the five literal vertices of `T`, one
   ending at each member of `T`, which are pairwise vertex-disjoint outside
   `P`, meet `S` only at their terminal vertices, and include `e` and `f`
   as the paths ending at `s_i,s_j`.
2. There is a nonempty connected proper subset `A` of `C` such that

   \[
                           |N_G(A)|=7,                 \tag{3.2}
   \]

   both `e` and `f` cross between `A` and `N_G(A)`, and

   \[
       \{k_2,s_X,s_Y,s_i,s_j\}\subseteq N_G(A).       \tag{3.3}
   \]

   In particular, this is a strict full-neighbourhood-separator descent
   `|A|<|C|` retaining two differently labelled crossing-edge responses
   and five literal inherited boundary labels.

#### Proof

Contract the connected path `P` to one vertex `r` in

\[
                          H=G[C\cup T]/P.              \tag{3.4}
\]

Apply the fan form of Menger's theorem from `r` to the five-set `T`.

Suppose first that a five-fan exists.  Since its five terminal vertices are
exactly `T`, replace the path ending at `s_i` by the direct edge `rs_i`,
and similarly replace the path ending at `s_j` by `rs_j`.  These
replacements cannot create an intersection away from `r`.  Lift the
contraction of `P` and stop every path at its first boundary vertex.  The
five lifted paths are pairwise disjoint outside `P`, have the five distinct
ends in `T`, have no other vertex of `S`, and the two designated paths are
the original edges `e,f`.  This is outcome 1.

Suppose instead that no five-fan exists.  There is a set

\[
                    Z\subseteq V(H)-\{r\},\qquad |Z|\le4, \tag{3.5}
\]

separating `r` from `T-Z`.  The two direct edges `rs_i,rs_j` force

\[
                              s_i,s_j\in Z.             \tag{3.6}
\]

Let `A` be the literal lift in `C` of the component of `H-Z` containing
`r`.  In particular `P\subseteq A`, so `a_1,a_2\in A`.  Componenthood in
the induced graph (3.4), together with the fact that `C` is a component of
`G-S`, gives

\[
                  N_G(A)\subseteq(S-T)\mathbin{\dot\cup}Z. \tag{3.7}
\]

The right side has order at most `3+4=7`.  Since `|T|>|Z|`, a vertex of
`T-Z` survives outside `A\cup N_G(A)`.  Another component of `G-S` also
lies outside.  Hence (3.7) is a nontrivial separation.  Seven-connectivity
forces equality throughout:

\[
        |Z|=4,qquad N_G(A)=(S-T)\mathbin{\dot\cup}Z,
        \qquad |N_G(A)|=7.                             \tag{3.8}
\]

Boundary-fullness of `C` at a vertex of `T-Z` also shows that `A` is a
proper subset of `C`: that vertex has a neighbour in `C`, and no such
neighbour lies in the `r`-component of `H-Z`.

Now `S-T=\{k_2,s_X,s_Y\}` and (3.6) holds, proving (3.3).  Finally
`a_1,a_2\in A` and `s_i,s_j\in Z\subseteq N_G(A)`, so both displayed
edges cross the new boundary.  This proves outcome 2. \(\square\)

### Corollary 3.2 (proper-minor responses survive the descent)

Under (2.5), in outcome 2 of Theorem 3.1 every one-edge or simultaneous
contraction response associated with `e,f` restricts to the corresponding
edge-deleted closed `A`-shore.  Its equality partition on `N_G(A)` is also
realized by the same colouring on the unchanged opposite closed shore.

Thus the descent retains the paired traces literally.  It does **not** say
that this partition colours the intact `A`-shore, because the crossing edge
whose ends are equal is present there in `G`.

#### Proof

Both operated edges have one end in `A` and one in `N_G(A)`.  Restrict the
global colouring of the corresponding edge-deleted graph to each closed
shore.  The only monochromatic operated edge is absent on the edge-deleted
`A`-shore and has no end in the opposite open shore.  The restrictions are
therefore proper and agree literally on their common boundary. \(\square\)

### Corollary 3.3 (minimum generic shore forces the five common labels)

Assume that `C` is a proper subset of the selected connected shore `C_0`
of a minimum-order generic exact-seven response interface.  Then outcome 1
of Theorem 3.1 holds.

#### Proof

In outcome 2, delete either crossing edge `e` or `f` and use its
six-colouring from Corollary 2.2.  The connected set `A`, its full
neighbourhood `N_G(A)` of order seven, and the unchanged nonempty opposite
side form a generic exact-seven response interface.  But

\[
                             |A|<|C|<|C_0|,
\]

contrary to the minimum choice of `C_0`.  Hence the five paths in outcome 1
exist.  Their first boundary hits are one literal representative from each
of `U,D,F_1,F_2,F_3`, so this conclusion removes endpoint repetition and
palette-to-label ambiguity for this paired-edge path system. \(\square\)

## 4. What the opposite boundary-full component does and does not force

The other component of `G-S` is used twice: it makes every separator in the
proof a genuine host separation, and it remains wholly on the opposite side
of the strict descent.  It does not by itself convert the five paths in
outcome 1 into seven branch sets.  Such a conversion still has to preserve
the inherited branch sets when pieces of `C` are reassigned.

This limitation is necessary.  The audited
[selected-fan barrier](../barriers/hc7_order_eight_selected_kempe_fan_barrier.md)
and
[static first-hit barrier](../barriers/hc7_multi_owner_static_first_hit_barrier.md)
show that a boundary-full opposite component, a labelled near-complete model
and one selected system of five paths do not alone force a `K_7` minor.
What is new here is the forced pair of literal common-label edges and the
well-founded order-seven response descent when their joint five-label fan
fails.

The singleton case `|C|=1` is not covered by Theorem 2.1.  It is a genuine
separate terminal mode: all common-label contacts may be incident with the
one vertex, so no two vertex-disjoint crossing edges exist.

## 5. Dependencies

- Menger's theorem in its fan form;
- the inherited order-eight label pattern from the reserved-component
  normal form;
- the standard edge-deletion and edge-contraction colouring responses of a
  minor-minimal seven-chromatic graph.
