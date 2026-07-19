# Three opposite-shore edge probes eliminate simultaneous five-chromatic saturation

**Status:** written proof; separate internal audit GREEN in
[`hc7_three_edge_owner_saturation_elimination_audit.md`](hc7_three_edge_owner_saturation_elimination_audit.md).  This theorem
uses the three owner pairs in the concentrated three-owner configuration.
It proves that their three opposite-shore deletion hosts cannot all be
five-chromatic: otherwise the endpoint `K_4` conclusions give a strict
label-preserving reduction of the donor branch set.  Consequently at least
one probe is six-chromatic and has a spanning `K_6`-minor model.  The theorem
does not align that model with the five inherited branch-set labels, reflect
a complete boundary partition, or prove `HC_7`.

## 1. Setting

Use the notation and all hypotheses of the audited
[three-owner concentration theorem](hc7_three_owner_reserved_component_concentration.md).
Thus `G` is seven-connected, seven-chromatic, `K_7`-minor-free, every proper
minor of `G` is six-colourable, and

\[
                 X,Y,D,U,F_1,F_2,F_3
\tag{1.1}
\]

is a spanning labelled `K_7`-minus-one-edge model, with the only possible
missing branch-set adjacency `X-Y`.  Write

\[
                         U=U_0\mathbin{\dot\cup}C,       \tag{1.2}
\]

where `U_0` and `C` are nonempty and connected, they are adjacent, the
prescribed root of `U` lies in `U_0`, and the fixed connected response
subgraph lies in `D` and has a fixed edge to `U_0`.  The three owner branch
sets are

\[
       I=\{R_1,R_2,R_3\}\subseteq\{X,Y,F_1,F_2,F_3\}. \tag{1.3}
\]

All old `U-R_i` contacts lie in `C`.  Put

\[
 B=N_G(U_0)\cap C,
 \qquad A_i=N_G(R_i)\cap C\quad(i=1,2,3).              \tag{1.4}
\]

The sets in (1.4) are nonempty.  Every branch set outside `I` retains an
edge to `U_0` (with the fixed `D-U_0` edge used for `D`).  The labelled
model was selected by first maximizing the relaxed literal first-hit rank
and then minimizing `|U|`, with the selected boundary partition, response
subgraph, prescribed roots and labels fixed.

Assume additionally that there is an edge `h` in the open shore opposite
`C` and the owner contact edges, so that both ends of `h` are anticomplete
to every vertex of `C` and every `R_i` endpoint used below.  For each
unordered pair `i,j`, the proper-two-owner linkage supplies vertex-disjoint
contact edges

\[
 e_{ij}=a_i r_i,
 \qquad f_{ij}=a_j r_j,                               \tag{1.5}
\]

where `a_i,a_j` are distinct vertices of `C` and `r_i in R_i`,
`r_j in R_j`.  The choices in (1.5) may depend on the pair.  Define

\[
                  J_{ij}=G-\{h,e_{ij},f_{ij}\}.        \tag{1.6}
\]

The braces in (1.6) mean edge deletion.

## 2. A connected-transversal lemma

### Lemma 2.1

Let `C` be a finite connected graph, let `B` be a nonempty subset of
`V(C)`, and let `A_1,A_2,A_3` be subsets satisfying

\[
                         |A_i\cap A_j|\ge2
                         \quad(i\ne j).                \tag{2.1}
\]

There is a nonempty connected set `L proper subset C` such that

1. `C-L` is connected;
2. `C-L` meets `B` and each `A_i`; and
3. `L` meets at least one `A_i`.

#### Proof

Choose an inclusion-minimal vertex set `T subseteq V(C)` such that `C[T]`
is connected and `T` meets each of `B,A_1,A_2,A_3`.  We first show that
some vertex of `A_1 union A_2 union A_3` lies outside `T`.

Suppose to the contrary that all three `A_i` are contained in `T`.  The
set `T` has at least two vertices, because (2.1) makes every `A_i` have at
least two vertices.  Take a spanning tree of `C[T]`.  Removing a leaf from
that tree leaves a connected vertex set.  By the minimality of `T`, each
leaf must therefore be the unique member in `T` of one of the four target
sets.  No leaf can be the unique member of an `A_i`, since every `A_i` is
contained in `T` and has order at least two.  Hence every leaf would have
to be the unique member of `B cap T`.  A tree has at least two distinct
leaves, and they cannot both be the unique member of the same nonempty
set.  This is a contradiction.

Choose

\[
 x\in(A_1\cup A_2\cup A_3)-T
\]

and let `L` be the vertex set of the component of `C-T` containing `x`.
Then `L` is nonempty, connected and meets some `A_i`.  Every component of
`C-T` has a neighbour in connected `T`, because `C` is connected.  Thus
the union of `T` with all components other than `L` is connected; this is
exactly `C-L`.  It contains `T`, so it meets `B` and every `A_i`.  All
three conclusions follow. \(\square\)

## 3. Elimination of the simultaneous five-chromatic branch

### Theorem 3.1

For at least one owner pair `i,j`, the four endpoints of
`e_{ij},f_{ij}` do not induce a `K_4` in `G`, and the corresponding graph

\[
                         J_{ij}=G-\{h,e_{ij},f_{ij}\}
\tag{3.1}
\]

is six-chromatic.  Hence it contains a `K_6` minor; since deleting
three edges cannot disconnect the seven-edge-connected graph `G`, that
model can be enlarged to a spanning `K_6`-minor model of the corresponding
common deletion host.

More precisely, if all three owner-pair deletion hosts were five-chromatic,
there
would be another spanning labelled `K_7`-minus-one-edge model in the same
host, preserving the selected boundary partition, response subgraph,
prescribed roots, five inherited labels and maximum relaxed first-hit rank,
but with a strictly smaller branch set labelled `U`.

#### Proof

Suppose first that for all three owner pairs the four endpoints of
`e_{ij},f_{ij}` induce a `K_4` in `G`.  In particular, both `C`-endpoints
`a_i,a_j` are adjacent to both owner branch sets `R_i,R_j`.  Therefore

\[
                    \{a_i,a_j\}\subseteq A_i\cap A_j,
\]

and the two endpoints are distinct.  Running this for the three owner
pairs gives

\[
                         |A_i\cap A_j|\ge2
                         \quad(i\ne j).                \tag{3.2}
\]

Apply Lemma 2.1 to `C,B,A_1,A_2,A_3`, and let `L` be its connected set.
Put

\[
                         U^*=U-L=U_0\cup(C-L).         \tag{3.3}
\]

The set `U^*` is connected: `C-L` is connected and meets `B`, while every
vertex of `B` has an edge to connected `U_0`.  It contains the prescribed
root of `U`.  It remains adjacent to every owner `R_i`, because `C-L`
meets every `A_i`.  It remains adjacent to every nonowner through `U_0`,
and the fixed edge preserves its adjacency to `D`.

Choose `i` such that `L cap A_i` is nonempty and replace

\[
                      U\longmapsto U^*,
              \qquad R_i\longmapsto R_i\cup L.        \tag{3.4}
\]

The enlarged owner is connected, since `L` contains a neighbour of
`R_i`.  All seven new branch sets are connected, disjoint and spanning.
Every old adjacency not incident with `U` is retained by enlargement, and
the preceding paragraph verifies every adjacency incident with `U^*`.
Thus either (3.4) repairs the possible missing `X-Y` adjacency and gives an
explicit `K_7`-minor model, or it gives another compatible spanning
labelled `K_7`-minus-one-edge model.  The first outcome is excluded by
the hypothesis on `G`.

The second model preserves the selected response data.  Every ranked
first-hit path ending at a label other than `U` avoided the old branch set
`U`, so it also avoids `L` and remains valid after (3.4).  A ranked path
ending in `U^*` remains valid.  If the old `U`-path ended in `L`, reroute
it inside the fixed connected response subgraph to the fixed edge entering
`U_0`, exactly as in the audited rank-preserving transfer theorem.  Paths
may overlap inside that response subgraph by the definition of the relaxed
rank, and the new one-vertex tail in `U_0` is avoided by every other ranked
path.  Hence the relaxed first-hit rank does not decrease.

The rank was maximal, so it remains maximal, while

\[
                           |U^*|=|U|-|L|<|U|.
\]

This contradicts the secondary minimality of `U`.  Therefore some owner
pair has endpoints which do not induce a `K_4`.

The joint three-edge fork gives chromatic number in `{5,6}` for every
pair and says that its five-chromatic branch forces precisely such an
endpoint `K_4`.  The selected non-`K_4` pair is consequently
six-chromatic.  The established `t=6` case of
Hadwiger's conjecture gives a `K_6` minor.  Seven-connectivity implies
seven-edge-connectivity, and deleting three edges leaves the host
connected.  Absorbing every component outside the model into an adjacent
branch set makes the model spanning. \(\square\)

## 4. Exact gain and remaining obstruction

The theorem spends endpoint saturation globally across the three owner
pairs.  In particular it eliminates the simultaneous five-chromatic
branch, but its stronger conclusion is a six-chromatic probe with one
literal missing cross-edge between its two labelled endpoint pairs.  It
does not identify a colour with an owner label:
the labels in (3.2) come from literal endpoint adjacencies in the three
endpoint `K_4` subgraphs.  The strict decrease in (3.3)--(3.4) is measured
on the literal donor branch set and preserves the selected response data.

What remains is the six-chromatic branch for at least one owner pair.  Its
spanning `K_6` model is not automatically aligned with the selected
boundary partition or with the inherited labels.  In particular, this
theorem does not prove that:

- the selected fixed boundary trace is attained by that particular owner
  pair;
- any branch set of the regenerated `K_6` model contains two prescribed
  endpoints;
- a complete boundary equality partition extends through both closed
  shores; or
- the spanning `K_6` model can be combined with one of the three deleted
  edges to form a `K_7`-minor model.

Thus the all-five-chromatic branch is a genuine strict-descent branch, while
the label-preserving absorption of the surviving six-chromatic probe is the
remaining theorem.

## 5. Dependencies

- [three-owner concentration and pairwise owner-contact edges](hc7_three_owner_reserved_component_concentration.md)
- [opposite-shore joint three-edge chromatic fork](hc7_cross_shore_critical_edge_linkage.md)
- [rank preservation under a donor branch-set transfer](hc7_first_hit_rank_preserving_branch_set_transfer.md)
- the established parameter-six case of Hadwiger's conjecture
