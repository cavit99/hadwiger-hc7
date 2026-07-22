# Low degree compresses the common-root alternating trace

**Status:** written proof; separately audited GREEN.  This theorem does not
prove `HC_7`.

## Theorem 1 (short-trace classification)

Assume the exact two-full-component common-root setup of the
[synchronized flip-cube theorem](hc7_common_root_flip_cube_fork.md).  Thus
`u` has degree eight or nine, `X=N_G(u)`, `H=G[X]`, and `G-N[u]` has exactly
two components.  At the synchronized cube vertex let `theta` be the fixed
boundary colouring, let `E` be its unique rejecting component, and let `F`
be the other component.

Fix one rejector-changing coordinate `k`.  Let

\[
                         W_0,\ldots,W_{n-1}             \tag{1.1}
\]

be the components of `H[alpha,beta]`.  Fix one extension of `theta` through
`F` and one extension of `theta^{\{k\}}` through `E`, and form the bipartite
full-component multigraph `Gamma` from their two partitions as in the
[alternating-cycle theorem](hc7_common_root_alternating_trace_cycle.md).
Then:

1. The sharper packing bound

   \[
      \sum_{r=0}^{n-1}\alpha(H[W_r])\le d_G(u)-5       \tag{1.2}
   \]

   holds.  In particular, `n<=3` in degree eight and `n<=4` in degree
   nine.
2. A shortest cycle of `Gamma` containing edge `k` is either a parallel
   two-edge cycle, or `d_G(u)=9`, `n=4`, and the cycle has length four and
   uses all four edges of `Gamma`.
3. In the latter case, after relabelling the other three coordinates as
   `a,b,c`, the two full-component partitions are exactly

   \[
      \mathcal P_F=\{\{k,a\},\{b,c\}\},\qquad
      \mathcal P_E=\{\{k,b\},\{a,c\}\}.               \tag{1.3}
   \]

   Moreover, each `W_r` is either one vertex or one edge.

Thus a longer alternating trace cycle cannot occur in the actual low-degree
host.

### Proof

Choose a maximum independent set inside each `W_r`.  Their union is
independent in `H`: an edge between two different `W_r` would be an edge of
`H[alpha,beta]` and would join their two alleged components.  The audited
low-degree neighbourhood bound gives

\[
                         \alpha(H)\le d_G(u)-5,
\]

which proves (1.2).  Every nonempty `W_r` contributes at least one vertex,
so `n<=d_G(u)-5`.

The alternating-cycle theorem says that edge `k` is a nonbridge of
`Gamma`.  A shortest cycle through it is either a parallel pair or a simple
bipartite cycle of length at least four.  Since `Gamma` has exactly `n`
edges, the latter possibility requires `n=4`, and hence degree nine; the
cycle then uses every edge.

Every vertex of that four-cycle has degree two on the cycle, so its
partition block contains the two incident edge labels.  The four labels are
all used, and blocks of one partition are disjoint.  Each of the two
partitions therefore consists of two two-element blocks.  Consecutive
cycle vertices belong to opposite partitions, which gives the two crossing
pairings in (1.3), up to relabelling.  Finally, each `W_r` is bipartite and
there are four of them.  Equality in (1.2) forces
`alpha(H[W_r])=1` for every `r`.  A nonempty bipartite graph with
independence number one is `K_1` or `K_2`.  \(\square\)

## Theorem 2 (the two-coordinate fork)

Let `i,j` be the two rejector-changing coordinates at the synchronized cube
vertex, and fix one `theta`-extension through `F`.  Exactly one of the
following holds.

1. One full `alpha`--`beta` component of that fixed `F`-extension contains
   both `W_i` and `W_j`.
2. The degree is nine, there are exactly four boundary two-colour
   components, and the fixed `F`-partition is

   \[
                         \{\{i,a\},\{j,b\}\}.          \tag{2.1}
   \]

   For each `k in {i,j}`, and for any separately chosen extension of
   `theta^{\{k\}}` through `E`, either its full component containing `W_k`
   also contains the fixed mate of `W_k` in (2.1), giving a parallel
   two-cycle, or its full-component partition is one of the two perfect
   matchings transverse to (2.1), giving the exact four-cycle of
   Theorem 1.

In particular, outcome 2 is impossible in degree eight.
More precisely, at degree eight outcome 1 has one of two forms:

- its fixed `F`-block is exactly `{i,j}`, and every separately chosen
  `E`-extension for either switch also puts `i,j` in one full component, so
  the pair is bilateral; or
- there are exactly three boundary traces, the fixed `F`-component contains
  all three, and every trace is `K_1` or `K_2`.

### Proof

In the fixed `F`-extension, switching `W_i` alone does not lift, and the
same is true for `W_j`.  Consequently the full component containing either
one must contain at least one further boundary component: otherwise that
full component itself could be switched.

If the two operated components lie in the same full component, outcome 1
holds.  Otherwise their two distinct partition blocks each have size at
least two.  Hence `n>=4`.  Theorem 1 gives degree nine and `n=4`, and the
two blocks exhaust the four labels, giving (2.1).

For either coordinate `k`, apply Theorem 1 to the fixed `F`-extension and
the chosen `E`-extension.  A parallel partner for `k` must be the unique
other label in its fixed `F`-block.  If there is no such parallel edge, the
exact four-cycle conclusion gives a two-by-two partition sharing no block
with (2.1), namely one of its two transverse perfect matchings.

For the degree-eight refinement, Theorem 1 leaves at most three traces.  If
the common fixed block contains only `i,j`, every cycle through either edge
is a parallel two-cycle and its parallel partner must be the other one.
Thus every corresponding `E`-extension also puts `i,j` together.  Otherwise
the fixed block contains a third trace, so there are exactly three.  The
summed bound (1.2) then makes each trace `K_1` or `K_2`, exactly as in the
four-trace equality case.  \(\square\)

## Theorem 3 (literal geometry of the four-cycle)

In the four-cycle case of Theorem 1, the four selected full components can
be written cyclically as

\[
                 K_0^F,K_1^E,K_2^F,K_3^E,             \tag{3.1}
\]

and the four edge labels as `W_0,W_1,W_2,W_3`, so that

\[
                 K_r\cap X=W_r\cup W_{r+1}            \tag{3.2}
\]

with subscripts modulo four.  They have all of the following literal
consequences.

1. Each `K_r` contains a `W_r`--`W_{r+1}` path `P_r` whose open interior
   lies wholly in its named open shore.  The four open interiors are
   pairwise vertex-disjoint; the two on either one shore are anticomplete.
2. Paths inside the four connected sets `W_r` join the consecutive
   endpoints of the `P_r` to form a simple odd cycle `Z`.  Its four
   nonempty open-shore sectors alternate between `F` and `E`.
3. There is a `Z`-path with interior in `F` joining the two `F`-sectors and
   a vertex-disjoint `Z`-path with interior in `E` joining the two
   `E`-sectors.  Their four ends alternate on `Z`.
4. Consequently `G-u` contains an `X`-meeting `K_4`-minor model, and adding
   the singleton branch set `{u}` gives an explicit `K_5`-minor model in
   `G`.

### Proof

Equation (3.2) follows from (1.3): every selected partition block consists
of exactly its two incident labels.  In `K_r`, choose a shortest path
between its two boundary traces.  Truncating at the first and last boundary
visits shows that only its ends lie in `X`; its open interior therefore lies
in the corresponding open shore.  Distinct selected full components in one
fixed shore colouring are disjoint and anticomplete.  The two shores are
disjoint and anticomplete, proving item 1.

At `W_r`, join the end of `P_{r-1}` to the end of `P_r` by a path inside the
connected graph `W_r`.  Different `W_r` are disjoint, every `P_r` meets its
two boundary traces only at its ends, and all four open interiors are
disjoint.  The eight paths therefore form a simple cycle `Z`.

To determine its parity, compare the two fixed shore colourings on the four
boundary traces.  They agree on three of them and differ by the
`alpha,beta` interchange on precisely the operated trace.  Following the
proper two-colour alternation along the four carrier paths and the four
boundary paths therefore returns with the colour phase reversed exactly
once.  Hence `Z` is odd.  This proves item 2.

The literal component `F` is connected and contains the open interiors of
`P_0` and `P_2`.  A shortest path in `G[F]` between those two sets, truncated
at its first and last contacts, is a `Z`-path whose interior avoids `Z`.
The same construction in `E` joins the interiors of `P_1` and `P_3`.  The
two paths are vertex-disjoint because the exterior components are disjoint,
and their ends alternate on `Z` because the four shore sectors alternate.
This proves item 3.

A cycle together with two internally disjoint paths joining alternating
pairs of points on it is a subdivision of `K_4`.  Each of its four rim
arcs contains one of the boundary paths in a distinct `W_r`.  Split each
rim arc at an edge after a chosen boundary vertex and contract the remaining
subdivision paths toward their incident branch vertices.  This gives four
disjoint connected branch sets, each meeting `X`.  They form a `K_4` model
in `G-u`; `{u}` is adjacent to all four and completes the claimed `K_5`
model.  \(\square\)

## Theorem 4 (the degree-eight fork retains the literal root)

Assume `d_G(u)=8`, and retain the original notation of the synchronized
flip-cube theorem, in which `W_0={x}` and the edge from `emptyset` to
`{0}` changes the unique rejector.  One endpoint `S` of that edge is
incident with a second rejector-changing edge in some coordinate `j!=0`.
Consequently Theorem 2 may be applied with `i=0`: in one fixed accepted-
shore extension, a full `alpha`--`beta` component contains the literal root
`x` and `W_j`.  More precisely, either

1. `{0,j}` is the exact fixed block and every separately chosen
   opposite-shore extension for either switch also contains `W_0` and
   `W_j` in one full component; or
2. there are exactly three boundary traces, the fixed full component
   contains all three, and every trace is `K_1` or `K_2`.

### Proof

The flip-cube theorem excludes `n=1`, while Theorem 1 gives `n<=3`.
Suppose first that `n=2`, with coordinates `0,h`, and suppose neither
endpoint of the cut edge `emptyset`--`{0}` has another incident cut edge.
Then

\[
 r(\{h\})=r(\varnothing),\qquad
 r(\{0,h\})=r(\{0\}).                                 \tag{4.1}
\]

The sets `{h}` and `{0}` are antipodal, so antipodal invariance makes the
two sides of the original cut equal, a contradiction.

Now let `n=3`, with other coordinates `h,l`, and make the same supposition.
The noncut edges at the two endpoints give

\[
 r(\{h\})=r(\varnothing),\qquad
 r(\{0,l\})=r(\{0\}).                                 \tag{4.2}
\]

But `{h}` and `{0,l}` are antipodal.  Again (4.2) contradicts the original
cut.  Thus one of `emptyset,{0}` has changing incident edges in coordinates
`0` and some `j!=0`.

Switching coordinate zero changes only the colour names on `W_0`; its
literal vertex set remains `{x}`.  Apply the degree-eight conclusion of
Theorem 2 at the selected endpoint.  It gives exactly the two displayed
alternatives.  \(\square\)

## Theorem 5 (tight traces force a five-singleton reserve)

Assume either the atomic three-trace degree-eight outcome or the exact
four-trace degree-nine outcome.  Choose one vertex from each `W_r`, and let
`I` be the resulting set.  Put `R=X-I`.  Then:

1. `I` is a maximum independent set of `H`, with

   \[
                         |I|=d_G(u)-5,
         \qquad |R|=5.                                \tag{5.1}
   \]

2. Contracting the star on `{u} union I` and six-colouring the resulting
   proper minor gives, after expansion, a proper colouring of
   `G-\{ui:i in I\}` whose boundary equality partition is exactly

   \[
                  I\mid\{r\}\quad(r in R).             \tag{5.2}
   \]

3. The restriction to `G-u` is one colouring which induces (5.2) through
   both literal exterior components simultaneously.
4. No proper six-colouring of a closed shore containing `u` can induce
   (5.2).  In every such colouring in which `I` is an exact boundary colour
   class, at least two vertices of `R` have the same colour and hence form
   a boundary nonedge.
5. In the degree-nine four-cycle case, the representatives forming `I` may
   be chosen so that the four branch sets of the `X`-meeting `K_4` model in
   Theorem 3 contain one distinct member of `I` each.

### Proof

Distinct boundary two-colour components are anticomplete, so `I` is
independent.  Its order is three in degree eight and four in degree nine.
The neighbourhood bound `alpha(H)<=d_G(u)-5` proves maximality and (5.1).

Contract the connected star on `{u} union I` to one vertex `w`.  This is a
proper minor.  In any proper six-colouring of it, let `gamma` be the colour
of `w`.  Expand `w` by assigning `gamma` to `u` and every vertex of `I`,
leaving precisely the edges `ui` with `i in I` deleted.  Every vertex of
`R` avoids `gamma`, because it is adjacent to `w` through the contracted
copy of `u`.

If the five vertices of `R` used at most four of the other colours, some
one of the six colours would be absent from all of `X`.  Recolour `u` with
that absent colour and restore the edges from `u` to `I`.  Since
`N_G(u)=X`, this would be a proper six-colouring of `G`, a contradiction.
Thus the five vertices of `R` use all five remaining colours, one each.
This proves (5.2).

Deleting `u` removes every edge omitted during expansion, so the colouring
restricts to the original graph `G-u`.  That graph contains both exterior
components and their common boundary `X`, proving item 3.

Finally, in a closed shore which contains `u` and all of `X`, the colour of
`u` is absent from `X`.  If `I` is one exact boundary colour class, the five
vertices of `R` therefore use at most four further colours.  Two of them
share a colour; properness makes them nonadjacent.  In particular the
six-block partition (5.2) cannot occur on that shore.


For item 5, choose the representative of `W_r` on the boundary subpath of
the corresponding rim arc in Theorem 3.  In the cyclic branch-set
allocation, split that rim arc after this representative and assign its
initial segment to the preceding branch vertex.  The four choices lie in
distinct traces, and the four resulting branch sets are disjoint, so each
retains its named representative.  \(\square\)

## Exact trust boundary

The independence bound eliminates arbitrary-length alternating cycles.
At degree eight only bilateral two-cycles remain.  At degree nine the only
additional case is one exact four-trace crossing, and that case has clean
literal shore paths and a crossed odd-cycle frame.
The degree-eight fork can furthermore be chosen to retain the original
singleton root `x`.
In both tight atomic cases, the proper-minor response supplies one common
five-singleton reserve on `G-u`, while the pole-containing shore must merge
at least one reserve pair.

None of these conclusions is terminal.  A common full two-colour component
is not a complete common boundary partition.  A bilateral component may
still pass through boundary traces not named by its chosen parallel pair.
The `X`-meeting `K_4` model above gives only `K_5` after adding `u`, not the
required `K_7`.  The audited boundary-only barrier also rules out promoting
the contracted crossing pattern itself to a terminal clique-minor claim.
The five-singleton reserve is not yet aligned with six named clique-minor
bags, and the compulsory merge is not yet retained in the crossed frame.

The remaining common-root work is therefore finite in shape: couple the
proper-minor colouring response either to a bilateral two-cycle, or, only in
degree nine, to the exact crossed four-cycle while preserving its literal
branch-set contacts.

## Inputs

- [common-root synchronized flip-cube fork](hc7_common_root_flip_cube_fork.md)
- [alternating full-component cycle](hc7_common_root_alternating_trace_cycle.md)
- [low-degree neighbourhood independence bound](hc7_low_degree_exterior_component_bounds.md#1-attachment-and-independence-bounds)
- [boundary-only fork barrier](../barriers/hc7_common_root_boundary_only_fork_barrier.md)
