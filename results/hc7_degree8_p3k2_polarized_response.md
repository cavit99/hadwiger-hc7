# Polarized responses in the degree-eight `P_3`-plus-edge reserve

**Status:** written proof; [separately audited **GREEN**](hc7_degree8_p3k2_polarized_response_audit.md).
This theorem does not prove `HC_7`.

## 1. Setup

Let `G` be a finite simple graph such that

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le 6\quad\hbox{for every proper minor }M\hbox{ of }G. \tag{1.1}
\]

Let `u` have degree eight, put `X=N_G(u)`, and suppose that `G-N_G[u]`
has exactly two nonempty components `E,F`, with

\[
                         N_G(E)=N_G(F)=X.                       \tag{1.2}
\]

Suppose

\[
 X=I\mathbin{\dot\cup}R,
 \qquad |I|=3,
 \qquad R=\{a,b,c,d,e\},                                      \tag{1.3}
\]

where `I` is independent and the only edges of `G[R]` are

\[
                              ab,\ bc,\ de.                    \tag{1.4}
\]

Fix a proper six-colouring `c` of `G-u` whose equality partition on `X`
is

\[
                   I\mid\{a\}\mid\{b\}\mid\{c\}
                    \mid\{d\}\mid\{e\}.                      \tag{1.5}
\]

Assume that every nonedge of `G[R]` has a `c`-bichromatic path whose open
interior lies in `E`.  In the concentrated seven-demand application these
are exactly the seven `E`-exclusive reserve demands; the absence of the
corresponding fixed-colouring paths in `F` is not needed in the proof
below.

For `z\in\{d,e\}`, let `\bar z` denote the other member of `\{d,e\}` and
put

\[
                 T_z=\{a,c,z\},
       \qquad    P_z=\{b,\bar z\}.                              \tag{1.6}
\]

Both sets in (1.6) are independent.  They partition `R`.

## 2. The opposite shore realizes the coarse partition

### Theorem 2.1 (two disjoint fixed-colouring carriers)

For each `z\in\{d,e\}`, the closed shore `G[F\cup X]` has a proper
six-colouring whose exact boundary equality partition is

\[
                              I\mid T_z\mid P_z.                 \tag{2.1}
\]

### Proof

Choose the fixed-colouring paths in `E` for the three nonedges

\[
                              ac,\ az,\ b\bar z.                 \tag{2.2}
\]

The union of the `a`--`c` and `a`--`z` paths is a connected subgraph
`L_z` containing every vertex of `T_z`.  It uses only the three colour
classes represented by `T_z`.  The `b`--`\bar z` path, denoted `Q_z`, uses
only the two colour classes represented by `P_z`.  Hence `L_z` and `Q_z`
are vertex-disjoint.  Their open interiors lie in `E`.

The three sets

\[
                     \{u\}\cup I,\qquad V(L_z),\qquad V(Q_z)    \tag{2.3}
\]

are therefore pairwise disjoint and connected.  Contract a spanning tree
in each set.  The result is a proper minor, so it has a proper
six-colouring by (1.1).  Restrict that colouring to the unchanged vertices
of `F`, discard the contracted copies of `u` and the path interiors in
`E`, and expand the three contraction vertices over `I,T_z,P_z`,
respectively.

The expansion is proper.  Each of `I,T_z,P_z` is independent, and every
edge from one of those boundary sets to a retained vertex was represented
at its contraction vertex.  The three contraction vertices have distinct
colours: the first is adjacent to the other two through the edges from `u`
to `R`, while the latter two are adjacent through literal boundary edges.
Indeed, `ab,bc` join `\{a,c\}` to `b`, and `de` joins `z` to `\bar z`.
Thus the induced boundary partition is exactly (2.1). \(\square\)

## 3. The pole-side response is forced to split the complementary pair

### Theorem 3.1 (exact polarization)

For each `z\in\{d,e\}`, the other closed shore `G[E\cup X]` has a proper
six-colouring whose exact boundary equality partition is

\[
                       I\mid T_z\mid\{b\}\mid\{\bar z\}.        \tag{3.1}
\]

Consequently the two shores realize the following two polarized response
pairs:

\[
\begin{array}{c|c|c}
 &G[E\cup X]&G[F\cup X]\\ \hline
 z=d&I\mid\{a,c,d\}\mid\{b\}\mid\{e\}
     &I\mid\{a,c,d\}\mid\{b,e\}\\
 z=e&I\mid\{a,c,e\}\mid\{b\}\mid\{d\}
     &I\mid\{a,c,e\}\mid\{b,d\}.
\end{array}                                                     \tag{3.2}
\]

### Proof

Fix `z`.  The sets

\[
                        A=\{u\}\cup I,
                 \qquad B=F\cup T_z                             \tag{3.3}
\]

are disjoint and connected.  Contract a spanning tree in each and
six-colour the resulting proper minor.  Restrict to the unchanged vertices
of `E`, discard `u` and `F`, and expand the two contraction vertices over
`I` and `T_z`.

This gives a proper colouring of `G[E\cup X]` in which `I` and `T_z` are
exact boundary blocks.  The two remaining boundary vertices `b,\bar z`
receive neither block colour: each is adjacent to the contraction of `A`
through `u`, and to the contraction of `B` through the full component
`F`.  They are nonadjacent, so they may a priori have either equal or
different colours.

If they had equal colours, this colouring and the colouring from Theorem
2.1 would induce the same exact partition `I\mid T_z\mid P_z` on `X`.
After a permutation of colour names, the two closed-shore colourings would
glue to a proper six-colouring of `G-u`.  Only three colours occur on `X`,
so a colour absent from `X` could be assigned to `u`.  This would
six-colour `G`, contrary to (1.1).  Hence `b` and `\bar z` have different
colours, proving (3.1)--(3.2). \(\square\)

## 4. Each polarized pair forces response-coloured paths in both shores

### Theorem 4.1 (two-sided complementary-pair paths)

For each `z\in\{d,e\}`, choose the two shore colourings from Theorems 2.1
and 3.1.  Then there is a `b`--`\bar z` path with open interior in `E`
which is bichromatic in the fine colouring (3.1), and a `b`--`\bar z`
path with open interior in `F` which is bichromatic in the coarse
colouring (2.1).

Thus proper-minor responses force `b`--`e` paths in both open shores for
the `z=d` response pair, and `b`--`d` paths in both open shores for the
`z=e` response pair.  The two response pairs use separately chosen
colourings; no disjointness between paths belonging to different rows of
(3.2) is asserted.

### Proof

Fix `z` and permute colour names so that the two shore colourings agree on
the blocks `I,T_z` and on the colour `beta` of `\bar z`.  In the fine
`E`-shore colouring let `b` have colour `alpha`.  In the coarse `F`-shore
colouring let `b` instead have colour `beta`, and choose `alpha` to be a
colour absent from the boundary.  The two boundary colourings then differ
by the `alpha`--`beta` interchange on the singleton component `\{b\}`.
This really is a boundary Kempe component in both directions: the only
other boundary vertex using either colour is `\bar z`, and
`b\bar z\notin E(G)`.

Consider first the full `alpha`--`beta` component of `G[E\cup X]` which
contains `b` in the fine colouring.  If it did not contain `\bar z`, its
only boundary vertex would be `b`.  Interchanging the two colours on that
full component would therefore change the fine boundary partition to the
coarse one.  It would then glue to the selected coarse colouring of
`G[F\cup X]`; since at most three colours occur on `X`, an absent colour
could be assigned to `u`.  This contradicts (1.1).  The component must
therefore contain `\bar z`.  A shortest `b`--`\bar z` path in it has all
internal vertices in `E`.

Now use the coarse colouring on `G[F\cup X]`.  Here `alpha` is absent from
`X`, while `b,\bar z` both have colour `beta`.  They are nevertheless two
different singleton components of the boundary `alpha`--`beta` graph,
because they are nonadjacent.  If the full component containing `b` did
not contain `\bar z`, swapping it would give `b` colour `alpha` and would
produce exactly the fine boundary partition.  That colouring would glue
to the selected fine colouring of `G[E\cup X]`; now four colours occur on
`X`, so again at least one of the six colours is available for `u`.  This
is the same contradiction.  Hence the full component contains `\bar z`,
and a shortest joining path has open interior in `F`. \(\square\)

## 5. The seventh demand completes a rooted `K_5`

### Theorem 5.1 (bilateral-path completion)

The graph `G-u` contains an `R`-rooted `K_5`-minor model.  More precisely,
for either choice

\[
                              f\in\{bd,be\},                    \tag{5.1}
\]

six fixed-colouring demands give an `E`-confined rooted model with at most
the adjacency `f` missing, and the response-coloured `f`-path in `F` from
Theorem 4.1 repairs that last adjacency.

### Proof

Let `Gamma` be the whole colour class of `c` which contains `I`, and put

\[
                              Q=(G-u)-\Gamma.                    \tag{5.2}
\]

As in the five-reserve Kempe-packet theorem, `Q` is five-colourable, `R`
is rainbow in every proper five-colouring of `Q`, and every selected
reserve demand has its two roots in one component induced by their two
fixed colours.  For the present application this can also be read directly
from the setup: a reserve bichromatic path uses two of the five colours on
`R`, not the colour of `I`, so each of the paths selected below lies in
`Q[E\cup R]`.

Fix `f\in\{bd,be\}` and let `D_0` be the other six nonedges of `G[R]`.
Kriesell--Mohr, Theorem 7, applied inside `Q[E\cup R]` to the six-edge
demand graph `(R,D_0)`, gives five pairwise disjoint connected rooted bags

\[
                              B_r\quad(r\in R)                    \tag{5.3}
\]

which are adjacent for every pair in `D_0`.  The literal root edges
`ab,bc,de` supply three more bag adjacencies.  Hence these five bags are
pairwise adjacent except possibly for `B_b,B_x`, where `f=bx`.

Theorem 4.1 gives a literal `b`--`x` path `P` whose open interior lies in
`F`.  Its response colouring is irrelevant after the path has been found.
The path meets `X` only at its ends.  Split `P` at any one of its edges
into disjoint connected subpaths `P_b,P_x`, containing `b,x`, respectively.
The split edge joins the two subpaths.  Replace

\[
                         B_b\ \hbox{ by }\ B_b\cup P_b,
              \qquad    B_x\ \hbox{ by }\ B_x\cup P_x.          \tag{5.4}
\]

The original bags lie in `E\cup R`, whereas the new open path vertices lie
in `F`.  Thus the five enlarged bags remain pairwise disjoint and
connected.  All old adjacencies survive, and the split edge supplies the
only possibly missing adjacency.  They form the claimed `R`-rooted `K_5`
model. \(\square\)

Theorem 5.1 is not a terminal `K_7` construction.  The repaired rooted
model uses both exterior components, and deleting the thin path from `F`
need not leave a connected set which can be joined to `I` and used as the
seventh branch set.

## 6. The exact response square and the remaining gap

After suitable palette alignment, the four attained boundary partitions
in (3.2) are the vertices of the boundary Kempe square

\[
\begin{array}{ccc}
 I\mid\{a,c,d\}\mid\{b\}\mid\{e\}
   &\longleftrightarrow&I\mid\{a,c,d\}\mid\{b,e\}\\
 \updownarrow&&\updownarrow\\
 I\mid\{a,c,e\}\mid\{b\}\mid\{d\}
   &\longleftrightarrow&I\mid\{a,c,e\}\mid\{b,d\}.
\end{array}                                                     \tag{6.1}
\]

The horizontal moves interchange a singleton `b` with an absent boundary
colour and are the cross-shore moves analysed in Theorem 4.1.  Each
vertical move is the boundary interchange on the component induced by the
literal edge `de`; on the coarse side the other component is the path
`a-b-c`, while on the fine side `a,c` are isolated from `de` in the two
selected colours.  Formula (6.1) is a statement about attained boundary
partitions.  It does not claim that either selected pair of same-shore
extensions is joined by one full-shore Kempe interchange.

This closes the static response ambiguity and the existence of a rooted
`K_5` in the surviving
`P_3\mathbin{\dot\cup}K_2` reserve: the two complementary nonedges `be`
and `bd` have named opposite-shore response transitions and literal paths
in both shores, and either bilateral path completes the six-demand rooted
certificate.  It is not terminal.  The two rows use different colourings,
their paths may intersect, and the opposite-shore path used in Theorem 5.1
can consume the connected seventh bag.  A terminal continuation must
either choose the rooted bags and one response path while reserving a
connected subgraph adjacent to all five bags, or show that failure to
reserve the remainder of that shore gives a bounded response-preserving
separation or a strict smaller literal component.

## Inputs

- [concentrated exclusive reserve responses](hc7_common_root_exclusive_reserve_response.md)
- [five-reserve Kempe packet](hc7_common_root_five_reserve_kempe_packet.md)
- [two independent boundary triples](hc7_degree8_two_independent_triples.md)
- the elementary lift-or-interior-path argument used in the
  [opposite-shore single-transition theorem](hc7_opposite_shore_single_kempe_transition.md)
- Matthias Kriesell and Samuel Mohr,
  [*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
  Theorem 7
