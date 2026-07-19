# Two crossed critical edges at a one-vertex series separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_series_incident_edge_fork_audit.md`](hc7_order8_series_incident_edge_fork_audit.md).  This is a
conditional theorem inside the connected order-eight opposite-response
branch.  It identifies exactly what the incident-edge colouring calculus
adds at the surviving one-cutvertex configuration.  It does not produce a
label-preserving `K_7`-minor model or prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le 6\quad\hbox{for every proper minor }M\hbox{ of }G.
 \tag{1.1}
\]

Use the exact one-cutvertex series configuration.  Thus

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \tag{1.2}
\]

where `|S|=8`, and there is a vertex `z in L` for which `G[L]-z`
has exactly two components `C_d,C_e` with

\[
 \begin{split}
 N_G(C_d)&=\{z\}\mathbin{\dot\cup}(S-\{e\}),\\
 N_G(C_e)&=\{z\}\mathbin{\dot\cup}(S-\{d\}).
 \end{split}
 \tag{1.3}
\]

The vertices `d,e` are nonadjacent to `z`.  Retain the named connected
subgraphs `P_0,P_1 subseteq R`, which are disjoint and boundary-full, and
the disjoint adjacent connected subgraphs `A_d,A_e subseteq L` satisfying

\[
 S-\{d\}\subseteq N_G(A_d),
 \qquad
 S-\{e\}\subseteq N_G(A_e).
 \tag{1.4}
\]

The crossed-colouring theorem supplies nonempty sets

\[
 Z_d\subseteq N_G(z)\cap C_e,
 \qquad
 Z_e\subseteq N_G(z)\cap C_d.
 \tag{1.5}
\]

Choose `u in Z_d` and `v in Z_e`, and put

\[
                    H=G-\{zu,zv\}.
 \tag{1.6}
\]

The braces in (1.6) denote deletion of the two edges.  Since `C_d,C_e`
are distinct components of `G[L]-z`, one has

\[
                         uv\notin E(G).
 \tag{1.7}
\]

## 2. Placement of the two named deficient subgraphs

### Lemma 2.1

Exactly one of `A_d,A_e` contains `z`.  More precisely,

* if `z in A_e`, then `A_d subseteq C_e`; and
* if `z in A_d`, then `A_e subseteq C_d`.

### Proof

The subgraph `A_e` has a neighbour at `d`.  Equation (1.3) and the nonedge
`dz` show that every neighbour of `d` in `L` belongs to `C_d`.  Hence
`A_e` meets `C_d`.  Symmetrically, `A_d` meets `C_e`.

If `A_e` omits `z`, its connectedness puts it wholly in the component
`C_d` of `G[L]-z`.  If `A_d` omits `z`, it lies wholly in `C_e`.  The two
subgraphs cannot both omit `z`, since then the assumed `A_d`--`A_e` edge
would join the distinct components `C_d,C_e`.  They cannot both contain
`z` because they are disjoint.  The two displayed alternatives follow.
\(\square\)

Thus the series decomposition does retain one literal fact about the old
labels.  It does not determine whether either selected crossed neighbour
`u,v` belongs to one of those named subgraphs.

## 3. Chromatic and connectivity fork for the common deletion

### Theorem 3.1

The graph `H` satisfies

\[
                         \chi(H)=6,
                 \qquad  \kappa(H)\ge5.
 \tag{3.1}
\]

Six-colouring the proper minor obtained by contracting both `zu,zv` and
expanding the contracted three-vertex class gives a proper colouring
`kappa` of `H` and a colour `alpha` such that

\[
 \kappa(z)=\kappa(u)=\kappa(v)=\alpha,
 \qquad
 N_G(z)\cap\kappa^{-1}(\alpha)=\{u,v\}.
 \tag{3.2}
\]

Moreover exactly one of the following connectivity alternatives applies.

In both alternatives, `H` is two-linked.  Consequently, for every fourth
vertex `r notin {z,u,v}`, the graph `H` has a `K_4`-minor model rooted at
`z,u,v,r`.

1. If `kappa(H)=5`, then

   \[
                            d_G(z)=7,
   \tag{3.3}
   \]

   and `N_G(z)` is the boundary of an actual order-seven separation whose
   one open side is the singleton `{z}`.  The two closed shores of this
   separation have no common equality partition induced by proper
   six-colourings.

2. `kappa(H)>=6`.

### Proof

The graph `H` is a proper subgraph of `G`, so it is six-colourable.  A
five-colouring of `H` could be extended to a six-colouring of `G` by giving
`z` one fresh colour and restoring both incident edges.  Hence
`chi(H)=6`.

Let `(A,T,B)` be a separation of `H` with both open sides nonempty.  Seven
internally vertex-disjoint paths in `G` between a fixed vertex of `A` and a
fixed vertex of `B` either meet `T` or use one of the two deleted edges.
The paths meeting `T` use distinct vertices of `T`, and each deleted edge
can occur on at most one of the remaining paths.  Therefore

\[
                             |T|+2\ge7,
\]

which proves `kappa(H)>=5`.

The contraction of the connected star on `z,u,v` is a proper minor.  The
nonedge (1.7) permits its colouring to be expanded to `H`.  Every other
neighbour of `z` is adjacent to the contraction image, proving the exact
trace (3.2).

The equality `chi(H)=6` and the Four Colour Theorem make `H` nonplanar.
Since `kappa(H)>=5`, Jung's theorem makes `H` two-linked.  All three
pairings of any four nominated vertices therefore have disjoint linkages.
The rooted-`K_4` characterization for a three-connected graph gives the
asserted rooted model.

Suppose first that `(A,T,B)` has order five.  Equality in the preceding
path budget forces both deleted edges to cross its open sides.  Since they
share `z`, orient the separation so that

\[
                       z\in A,
                 \qquad u,v\in B.
 \tag{3.4}
\]

If `A-{z}` were nonempty, the six-set `T union {z}` would separate it from
`B` in `G`, contrary to seven-connectivity.  Hence `A={z}`.  In `G`, all
neighbours of `z` therefore belong to `T union {u,v}`.  Minimum degree
seven gives equality, proving (3.3) and

\[
                         N_G(z)=T\mathbin{\dot\cup}\{u,v\}.
 \tag{3.5}
\]

The set `B-{u,v}` is nonempty.  Otherwise `B={u,v}`, and either of its
vertices would have at most the five neighbours in `T` together with `z`
(the edge `uv` is absent), contradicting minimum degree seven.  Thus
`N_G(z)` is an actual order-seven separator with singleton open side.

The incompatibility assertion is stronger than a statement about the
particular colouring `kappa`.  In every proper six-colouring of `G-z`, all
six colours occur on `N_G(z)`, or a missing colour could be assigned to
`z`.  Hence its equality partition on the seven-set `N_G(z)` has six
blocks.  In every proper six-colouring of the singleton closed shore
`G[N_G[z]]`, the colour of `z` is absent from `N_G(z)`, so the boundary
partition has at most five blocks.  No complete equality partition is
therefore induced on both closed shores.  In particular, (3.2) induces
exactly the six blocks

\[
                      \{u,v\}\mid\hbox{five singletons}.
 \tag{3.6}
\]

If no separation of order five exists, then `kappa(H)>=6`, which is the
second alternative.  \(\square\)

### Corollary 3.2 (the degree-seven neighbourhood in the low-connectivity branch)

Retain also the six distinct neighbours of `z` supplied by the three
merged-root Kempe paths:

\[
 a_1,a_2,a_3\in C_d,
 \qquad
 b_1,b_2,b_3\in C_e.
 \tag{3.7}
\]

In outcome 1 of Theorem 3.1, each of the triples in (3.7) induces a
triangle.  If `w` is the seventh neighbour of `z`, then `w` is complete to
at least one of those two triangles.  In particular, `G[N_G(z)]` contains
a `K_4`.

### Proof

Dirac's neighbourhood-independence inequality for a seven-contraction-
critical graph gives

\[
                         \alpha(G[N_G(z)])\le2.
\]

There is no edge between an `a_i` and a `b_j`, because `C_d,C_e` are
distinct components of `G[L]-z`.  If two members of the `a`-triple were
nonadjacent, those two vertices together with any `b_j` would be an
independent set of order three.  Hence the `a`-triple is a clique, and the
same argument applies to the `b`-triple.

If `w` failed to be complete to both triples, choose a nonneighbour of `w`
in each.  Those two vertices are nonadjacent to each other and would form
an independent triple with `w`.  Thus `w` is complete to one of the two
triangles, proving the assertion. \(\square\)

## 4. Exact output of the incident-edge colouring theorem

Apply the audited incident-edge saturation-or-bypass theorem to the two
edges `zu,zv` and to the colouring `kappa` in (3.2).  For every alternate
colour at least one of the two pairs is bichromatically linked.  Moreover,
one of the following holds.

1. One of `zu,zv` is linked in `H` for all five alternate colours.
2. There are distinct alternate colours `i,j`, an
   `{alpha,i}`-component `K_u` containing `u`, and an
   `{alpha,j}`-component `K_v` containing `v`, such that

   \[
       z,v\notin K_u,
       \qquad z,u\notin K_v,                         \tag{4.1}
   \]

   and the two components intersect or have one edge between them.  Their
   union therefore contains a three-colour `u`--`v` path avoiding `z`.
   Switching `K_u` gives a six-colouring of `G-zv`, while switching `K_v`
   gives a six-colouring of `G-zu`.

### Proposition 4.1 (literal first exit in the bypass outcome)

In outcome 2, at least one of the following occurs:

* `K_u` has a path from `u` whose first vertex outside `C_e` is a literal
  member of `S-{d}`; or
* `K_v` has a path from `v` whose first vertex outside `C_d` is a literal
  member of `S-{e}`.

### Proof

If `K_u subseteq C_e` and `K_v subseteq C_d`, the two components are
disjoint and there is no edge between them, because `C_e,C_d` are distinct
components of `G[L]-z`.  This contradicts the intersection-or-edge
conclusion above.  Thus at least one component leaves its native lobe.

Suppose it is `K_u`.  Take a path in `K_u` from `u` to a vertex outside
`C_e` and stop at its first such vertex.  Equation (1.3) says that this
vertex belongs to `{z} union(S-{d})`.  It is not `z` by (4.1), so it lies
in `S-{d}`.  The proof for `K_v` is symmetric.  \(\square\)

## 5. Exact gain and obstruction

The common deletion has now been exhausted at the purely chromatic and
connectivity levels.

* Its order-five-separator branch does return a literal order-seven
  boundary, but Theorem 3.1 proves that this singleton boundary is
  intrinsically incompatible: it cannot carry one complete equality
  partition induced on both closed shores.
* In both connectivity branches it gives an endpoint-rooted `K_4`, but the
  branch sets are not guaranteed to avoid or preserve `P_0,P_1,A_d,A_e`.
* The bypass branch gives an operation-specific literal first boundary
  hit.  The uncoloured existence of a `u`--`v` path avoiding `z` is not new:
  the connected lobes are both adjacent to every vertex of
  `S-{d,e}`, so such a path already exists through any one of those common
  boundary vertices.
* The two Kempe switches need not preserve the monochromatic blocks `X,Y`
  of the selected opposite response.  The simultaneous-contraction
  colouring `kappa` is not a selected boundary-response colouring, and the
  first hit in Proposition 4.1 need not belong to either named deficient
  subgraph.  Hence the singleton-response theorem cannot be applied to
  these switches, and a palette colour cannot be read as one of the labels
  `P_0,P_1,A_d,A_e`.

Thus the incident-edge theorem supplies a genuine literal first hit but no
terminal conclusion.  Closing this branch still requires a theorem which
either assigns that first hit to the named connected subgraphs while
preserving the selected boundary partition, or converts its failure into a
strict response-preserving separation.  Saturation alone supplies five
palette-indexed paths, not five label-distinct branch-set contacts.

## 6. Dependencies

- [response propagation across the two cutvertex lobes](hc7_order8_cutvertex_lobe_response_propagation.md);
- [ordered crossings of the two deficient connected
  subgraphs](../results/hc7_order8_ordered_defect_crossing.md);
- [incident-edge bichromatic saturation or bypass](../results/hc7_shared_interface_bichromatic_bypass.md);
- Dirac's neighbourhood-independence inequality for contraction-critical
  graphs;
- Jung's theorem that every four-connected nonplanar graph is two-linked;
  and
- the rooted-`K_4` characterization for three-connected graphs.
