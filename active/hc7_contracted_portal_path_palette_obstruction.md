# A common-contraction palette obstruction on a portal path

**Status:** written proof; unaudited active result.  The two-leaf Kempe
case overlaps the audited incident-edge saturation-or-bypass theorem.  The
new uniform content is Theorem 4.3: a Hall-type saturation-or-bypass
dichotomy for three or more incident named edges, allowing arbitrary edges
among their noncentral endpoints.  The note does not align colours with all
five fixed branch sets and does not prove `HC_7`.

## 1. A general list obstruction

### Lemma 1.1

Let `G` be a graph which is not `q`-colourable, let `D` be a connected
vertex set of order at least two, and let `c` be a `q`-colouring of the
proper minor `G/D`.  Write `d` for the contracted vertex and
`alpha=c(d)`.  For `x in D`, put

\[
  L_c(x)=[q]-c(N_G(x)-D).                              \tag{1.1}
\]

Then `alpha` belongs to every list `L_c(x)`, and `G[D]` is not
`L_c`-colourable.

#### Proof

Every outside neighbour of every vertex of `D` becomes a neighbour of
`d`, and hence has colour different from `alpha`.  Thus `alpha` belongs to
all the lists.  An `L_c`-colouring of `G[D]` would combine with `c` on
`G-D` to give a proper `q`-colouring of `G`, contrary to the hypothesis.
\(\square\)

## 2. Exact classification on an induced three-vertex path

### Theorem 2.1 (portal-path palette obstruction)

Suppose `D={w,s,f}` induces the path

\[
                              w-s-f.                    \tag{2.1}
\]

In every `q`-colouring `c` of `G/D`, the centre `s` and at least one of
the two leaves `w,f` have an outside neighbour of every colour different
from `alpha=c(D)`.  Equivalently,

\[
  L_c(s)=\{\alpha\},
  \qquad
  L_c(w)=\{\alpha\}\quad\text{or}\quad
  L_c(f)=\{\alpha\}.                                  \tag{2.2}
\]

#### Proof

All three lists contain `alpha` by Lemma 1.1.  If `s` had an available
colour `beta!=alpha`, colour `s` with `beta` and both nonadjacent leaves
with `alpha`; this would be an `L_c`-colouring of the path.  Hence
`L_c(s)={alpha}`.

If both leaves had alternate available colours, assign one such colour to
each leaf and retain colour `alpha` at `s`.  The leaves are nonadjacent, so
their two chosen colours need not be distinct.  This would again
`L_c`-colour the path.  Lemma 1.1 excludes it, proving that one leaf also
has singleton list `{alpha}`.  The list definition translates singleton
lists exactly into the asserted full outside palettes.  \(\square\)

This is stronger than applying endpoint saturation separately after
contracting `sw` and `sf`: both saturated vertices in (2.2) occur in one
colouring of the common contraction of the whole labelled path.

### Corollary 2.2 (induced portal star)

Suppose instead that `D` induces a star with centre `s` and at least one
leaf.  In every `q`-colouring of `G/D`, the centre `s` and at least one
leaf have an outside neighbour of every colour different from
`alpha=c(D)`.

#### Proof

If `s` had an alternate available colour, give it that colour and give
every leaf colour `alpha`.  If every leaf had an alternate available
colour, give `s` colour `alpha` and choose an alternate colour separately
at each leaf.  The leaves are independent, so both assignments are proper
list-colourings of the star.  Lemma 1.1 excludes both assignments.  Thus
`L_c(s)={alpha}` and `L_c(f)={alpha}` for at least one leaf `f`.  \(\square\)

The conclusion deliberately says *one* leaf.  Even with arbitrarily many
named leaves, nonextendability alone does not select one saturated leaf in
each named branch set.  This is the exact limitation of replacing the
three-vertex path by a larger portal star.

## 3. Application to a reversible branch-set rotation

Use the notation of the audited opposite-boundary-response theorem.  Thus
`W` is the transferred connected subgraph, `s` is its unique attachment to
the residual donor subgraph, and `sw` is a donor-interface edge with
`w in W`.  Let `H` be one newly missed fixed branch set.  If its selected
contact edge can be chosen as

\[
                              sf,
  \qquad f\in H,                                       \tag{3.1}
\]

then `w-s-f` is induced: `W` is anticomplete to every newly missed branch
set.  Contracting this path is a proper minor.  Theorem 2.1 therefore gives
one common six-colouring in which

* the literal donor portal `s` sees all five alternate colours outside the
  path; and
* either the literal transferred-side vertex `w` or the precise lost-label
  vertex `f in H` sees all five alternate colours outside the path.

This is a label-faithful allocation: the second possible saturated leaf is
in the named branch set whose adjacency the rotation lost.  It also fails
in a six-colourable shadow at the premise—if the displayed lists coloured
the path, they would simply reconstruct a six-colouring of the host.

If contacts to several newly missed branch sets form an induced star at
`s`, Corollary 2.2 applies to their common contraction.  It still certifies
only one saturated named leaf.  Applying Theorem 2.1 separately to several
portal paths uses different proper-minor colourings and therefore cannot be
combined without a further response-collision theorem.

### Proposition 3.1 (the common contraction orients the response)

Retain the three-vertex path `w-s-f` and suppose that `s` is the only
boundary vertex on the path.  Let `Pi` be the equality partition induced
on that boundary by a colouring `c` of `G/{w,s,f}`.

* If `f` has an available colour different from `alpha`, then the same
  exterior colouring extends, without changing `Pi`, to a colouring of
  `G-sw`.
* If `w` has an available colour different from `alpha`, then it extends,
  without changing `Pi`, to a colouring of `G-sf`.
* These two direct extensions cannot both exist.

Thus the common-contraction colouring has exactly three possible local
types: it lifts toward the donor-edge response only, it lifts toward the
lost-label-edge response only, or both leaves are palette-saturated and it
lifts toward neither.  The last type is a genuinely stronger lock than two
unrelated one-edge response colourings.

#### Proof

If `beta in L_c(f)-{alpha}`, keep `w,s` at colour `alpha` and colour `f`
with `beta`.  All external edges at `f` are proper by the definition of
the list.  The edge `sf` is proper, and `sw` is the sole remaining
monochromatic edge.  Deleting it therefore gives a proper colouring of
  `G-sw`.  The recoloured leaf lies off the boundary, so its equality
partition remains `Pi`.  The argument with `w` and `f` interchanged gives
the second assertion.

If both direct extensions existed, their unchanged boundary partition
would belong to the two opposite response languages in the rotation
setup, contradicting the audited response-collision theorem.  Equivalently,
colouring both leaves with their alternate colours and retaining colour
`alpha` at `s` would directly six-colour `G`.  \(\square\)

### Proposition 3.2 (incident-edge lock allocation)

More generally, let `D` be an induced star with centre `s`, leaves
`f_1,...,f_m`, and edges `e_i=sf_i`; assume again that only `s` lies on
the labelled boundary.  In a colouring `c` of `G/D`, define

\[
  F(c)=\{i:L_c(f_i)=\{\alpha\}\}.                       \tag{3.2}
\]

Then `F(c)` is nonempty.  Here a **direct lift** means a colouring which
keeps `c` on `G-D`, keeps `s,f_k` at colour `alpha`, and recolours the
other leaves independently from their lists.  For a fixed `k`, such a
direct lift to `G-e_k`, with the same boundary partition, exists if and
only if

\[
                              F(c)=\{k\}.                \tag{3.3}
\]

Thus a common contraction of all incident portal edges either allocates
its boundary response to one uniquely locked named edge, or produces a
multi-lock involving at least two named leaves.  This is the incident-edge
analogue of lock allocation for two vertex-disjoint edges, but it uses one
common contraction colouring and preserves the literal boundary vertex
`s`.

#### Proof

Corollary 2.2 gives `F(c)\ne\varnothing`.  To lift directly to `G-e_k`, keep
`s` and `f_k` at colour `alpha`.  Every other leaf must receive an
alternate colour from its list; because the leaves are independent, those
choices can be made separately and create no leaf--leaf conflict.  Such a
choice exists exactly when no index other than `k` belongs to `F(c)`.
Together with nonemptiness of `F(c)`, this is equivalent to (3.3).  The
boundary colour is unchanged throughout.  \(\square\)

## 4. A common-colouring Kempe allocation

The list obstruction has a version which produces literal
colour-restricted connections rather than only palette neighbours.

### Theorem 4.1 (incident-star Kempe allocation)

Let `D` induce the star with centre `s`, leaves `f_1,...,f_m`, and let `c`
be a `q`-colouring of `G/D`, with contraction colour `alpha`.  Expand `c`
to the graph

\[
                    H=G-\{sf_i:1\le i\le m\}             \tag{4.1}
\]

by assigning colour `alpha` to every vertex of `D`.  For each
`beta!=alpha`, put

\[
 K_\beta=\{i:s\text{ and }f_i\text{ lie in the same component of }
                 H[c^{-1}(\{\alpha,\beta\})]\}.           \tag{4.2}
\]

Then `K_beta` is nonempty for every `beta!=alpha`.  Consequently the
`q-1` alternate colours are allocated, in one common colouring, to
literal bichromatic paths from `s` to named leaves.  Some leaf receives at
least

\[
                         \left\lceil\frac{q-1}{m}\right\rceil
                                                               \tag{4.3}
\]
such paths.  For a three-vertex portal path in the `HC_7` application,
one of its two labelled leaves therefore receives at least three of the
five colour-restricted paths.

If `K_beta={k}`, a single `alpha`--`beta` component switch gives a
`q`-colouring of `G-sf_k`.  Thus a singleton allocation is already a
proper-minor response of the named edge; a nonsingleton allocation is a
common-colouring collision between named portal edges.

#### Proof

The expanded assignment is a proper colouring of `H`: the only edges of
`G[D]` are the deleted star edges, and every outside neighbour of `D`
avoids colour `alpha` in `G/D`.

Fix `beta!=alpha`.  If `K_beta` were empty, interchange `alpha` and
`beta` on every bichromatic component containing a leaf.  None of those
components contains `s`.  After the switches every leaf has colour
`beta`, while `s` retains colour `alpha`; restoring all star edges would
therefore give a proper `q`-colouring of `G`, a contradiction.  Hence
`K_beta` is nonempty.  Counting the incidences `(i,beta)` gives (4.3), and
membership in `K_beta` supplies the stated literal bichromatic path.

If `K_beta={k}`, switch the component containing `s`.  The centre and
`f_k` both change to `beta`, while every other leaf remains `alpha`.
Hence exactly the edge `sf_k` is monochromatic when all star edges are
restored, producing a proper colouring of `G-sf_k`.  \(\square\)

The switch in the last paragraph can change colours on other boundary
vertices in its bichromatic component.  It therefore supplies a named
edge response, but it need not preserve the original boundary equality
partition.  This is why Theorem 4.1 does not by itself contradict the
opposite orientation of two response languages.

### Corollary 4.2 (response collision or a boundary-changing component)

Return to the portal path `w-s-f`, where `sw` and `sf` have oppositely
oriented response languages on the same boundary.  Let `Pi` be the
boundary partition of the common-contraction colouring.  For an alternate
colour `beta`, call the centre's `alpha`--`beta` component
**boundary-preserving** when switching it leaves `Pi` unchanged.

There cannot be two alternate colours `beta,gamma` such that

\[
                  K_\beta=\{w\},\qquad K_\gamma=\{f\},    \tag{4.4}
\]

and both corresponding centre components are boundary-preserving.
Consequently every common-contraction colouring has at least one of the
following features:

1. some centre bichromatic component contains both labelled leaves;
2. all boundary-preserving singleton allocations are oriented toward the
   same edge; or
3. a centre bichromatic component changes the literal equality partition
   by splitting or merging boundary colour blocks.

#### Proof

Under the first equality in (4.4), Theorem 4.1 switches the centre
component to give a colouring of `G-sw`; boundary preservation puts `Pi`
in `Resp(sw,S)`.  The second equality similarly puts the same `Pi` in
`Resp(sf,S)`.  This contradicts the opposite-response collision theorem.

If no allocation set contains both leaves, every `K_beta` is a singleton.
Unless all boundary-preserving singleton allocations choose the same leaf,
the forbidden pair (4.4) occurs.  Every remaining singleton allocation
uses a component whose switch changes `Pi`.  This is the
boundary-changing outcome.  \(\square\)

The third outcome is not yet an order-seven separation: a bichromatic
component may have an arbitrarily large full neighbourhood.  Its value is
that the residual obstruction is now a literal component crossing a
specified boundary colour block, rather than an unlabelled failure of
palette-to-branch-set alignment.

### Theorem 4.3 (Hall saturation or a leaf-to-leaf bypass)

Let

\[
                         D=\{s,f_1,\ldots,f_m\}
\]

be a connected vertex set in a graph `G` which is not `q`-colourable,
with `s` adjacent to every `f_i`; edges among the named
leaves are allowed.  Colour `G/D`, call the contraction colour `alpha`,
and expand the colouring to

\[
                         \widehat H=G-E(G[D])            \tag{4.5}
\]

by giving all of `D` colour `alpha`.  Define `K_beta` as in (4.2), using
the bichromatic components of `widehat H`.  For each leaf put

\[
 U_i=\{\beta\ne\alpha:i\notin K_\beta\}.                \tag{4.6}
\]

these are the colours for which `f_i` is *not* bichromatically connected
to the centre.  Then at least one of the following holds.

1. The graph `widehat H-s` contains a path between two distinct named
   leaves.
2. There is a nonempty set `I` of leaves such that

   \[
                     \left|\bigcup_{i\in I}U_i\right|<|I|. \tag{4.7}
   \]

In particular, for `q=6` and three leaves, absence of every leaf-to-leaf
bypass forces one of the following common-colouring saturation patterns:

* one named leaf is linked to `s` in all five alternate colours;
* two named leaves are both linked to `s` in at least four alternate
  colours; or
* all three named leaves are linked to `s` in at least three alternate
  colours.

#### Proof

If (4.7) fails, Hall's theorem gives distinct representatives
`beta_i in U_i`, one for each leaf.  Let `A_i` be the
`alpha`--`beta_i` component of `widehat H` containing `f_i`.  By the definition of
`U_i`, none of the `A_i` contains `s`.

If two of the `A_i` intersect or are joined by an edge, their connected
union contains a path between the corresponding leaves which avoids `s`.
This is outcome 1.  Otherwise the `A_i` are pairwise disjoint and
pairwise anticomplete.  Interchange `alpha,beta_i` on every `A_i`.
The interchanges are independent and preserve properness.  Every leaf
changes from `alpha` to its distinct representative colour, while `s`
stays `alpha`.  The distinct representatives make every edge among the
leaves proper, and their difference from `alpha` makes every centre--leaf
edge proper.  Thus all deleted edges of `G[D]` can be restored.  This
would `q`-colour `G`, a contradiction.  Thus outcome 1 or 2 holds.

For three leaves, apply (4.7).  If `|I|=1`, its unique leaf has empty
`U_i` and is linked for all five colours.  If `|I|=2`, the union of the
two `U_i` has order at most one, so both leaves are linked for the other
at least four colours.  If `|I|=3`, their union has order at most two, so
all three are linked for the other at least three colours.  \(\square\)

For two nonadjacent leaves, Theorem 4.3 reduces to the already audited
incident-edge saturation-or-bypass theorem.  Its new content begins with
three or more incident named edges, or when the leaves have additional
edges: a failed system of distinct Kempe switches yields a quantitative
common-colouring saturation certificate without assuming an induced star.

## 5. Exact remaining gap

The theorems give simultaneous palette saturation and five
colour-distinguished paths, but do not identify the five colours with the
five fixed branch sets.  All five witnesses may
be concentrated in one connected outside region, and different lost
branch sets may select different colourings of their respective contracted
portal paths.  Thus (2.2) alone yields neither a quasi-`K_7` model nor a
bounded full neighbourhood.

A terminal continuation needs one additional statement: in the
`K_7`-minor-free rotation geometry, a fully saturated centre--leaf pair
must either have five label-distinct connected witnesses, or all its
witnesses meet a connected region whose full neighbourhood has order
seven and carries the opposite response partition.  Proving that assertion
is exactly the unresolved palette-to-labelled-branch-set step; ordinary
Kempe saturation does not supply it.  Corollary 4.2 narrows the first
necessary host-level input further: control a centre bichromatic component
which either contains both labelled leaves or changes one of the at most
seven literal boundary colour blocks.  A theorem converting that component
to pairwise disjoint named branch-set contacts, or to its full
order-seven neighbourhood, would close this local exchange.

## 6. Dependency

- [oppositely oriented boundary responses at a connected-subgraph rotation](../results/hc7_rotation_opposite_boundary_responses.md)
- [the two-incident-edge saturation-or-bypass theorem](../results/hc7_shared_interface_bichromatic_bypass.md)
