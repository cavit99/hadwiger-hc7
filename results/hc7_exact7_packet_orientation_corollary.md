# Exact-seven orientation by full connected subgraphs

**Status:** written proof; separate internal audit.  This note combines
the exact packet-reflection calculation with a host-level Two-Paths
reduction.  It is a conditional theorem for an actual seven-vertex
separator and does not prove `HC_7`.

## 1. Terminology

Let

\[
        V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
        \qquad E_G(A,B)=\varnothing,
        \qquad |S|=7,                                  \tag{1.1}
\]

where both open sides are nonempty.  A connected subgraph disjoint from
`S` is **`S`-full** when it has a neighbour at every literal vertex of
`S`.  The **full-subgraph packing number** of an open side is the maximum
number of pairwise vertex-disjoint `S`-full connected subgraphs in it.

For a proper equality partition `Pi` of `S`, put

\[
 d_{G[S]}(\Pi)=|\Pi|-
 \omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr).     \tag{1.2}
\]

The exact packet-reflection lemma says that `q` disjoint `S`-full
connected subgraphs reproduce every partition of demand at most `q` on
the opposite closed side, unless the same contractions already display a
`K_7`-minor model.

## 2. Two full connected subgraphs on the coloured side

### Corollary 2.1 (two disjoint full subgraphs suffice)

Assume that `G` is not six-colourable and every proper minor of `G` is
six-colourable.  Suppose `G[A]` contains two disjoint `S`-full connected
subgraphs.  Let `c` be a proper six-colouring of
`G[A\cup S]`.  Suppose there are disjoint sets

\[
                         D,E\subseteq S,
       \qquad |D|=3,\quad |E|=2,                       \tag{2.1}
\]

such that `c` is constant on each of `D,E` and uses distinct colours on
the two sets.  Write

\[
                         S=D\mathbin{\dot\cup}E
                              \mathbin{\dot\cup}\{r,z\}.             \tag{2.2}
\]

Then there are named disjoint `S`-full connected subgraphs `C_D,C_E` in
`A` such that one of the following holds.

1. The equality partition of `c` is

   \[
                         D\mid E\mid\{r\}\mid\{z\},                 \tag{2.3}
   \]

   the vertices `r,z` are nonadjacent, and their two-colour subgraph in
   `G[A\cup S]` contains an `r-z` path with interior in `A`.  Every such
   path meets `C_D\cup C_E`.

2. The equality partition of `c` is

   \[
                         D\mid E\mid\{r,z\},                           \tag{2.4}
   \]

   and, for some colour `theta` absent from `S` under `c`, the two-colour
   subgraph induced by `c(r),theta` contains an `r-z` path with interior
   in `A`.  Every such path meets `C_D\cup C_E`.

Every other equality partition is reflected through the two connected
subgraphs and would make `G` six-colourable.  Thus in every non-six-
colourable orientation a shortest displayed path has a literal first entry
into the named pair.

### Proof

Choose two disjoint `S`-full connected subgraphs `C_D,C_E` in `A`.  The
sets `C_D` and `C_E` need not be adjacent.  The two block unions used by
the Kempe-compression proof nevertheless are adjacent: `C_D` has a
literal edge to every member of `E`, and `E` lies in `C_E\cup E`.  Apply the
two-full-subgraph Kempe-compression theorem in this adjacency-free form.
Its demand calculation reflects every boundary partition except (2.3), with
`rz` absent, and (2.4).  In the first exceptional partition it gives the
`c(r),c(z)` path in outcome 1.  In the second it chooses a colour absent
from `S` under `c` and gives the path in outcome 2.  In both cases every
such path meets `C_D\cup C_E`, exactly as asserted. \(\square\)

## 3. A packet-thin side with a two-vertex contact transversal

Fix `b in S` and a two-set `I subseteq S-{b}`.  A **repair support** is a
connected subgraph of an open side adjacent to `b` and to at least one
member of `I`.  A **residual full subgraph** is a disjoint `S`-full
connected subgraph in the same open side.

### Theorem 3.1 (contact transversal without an internal-connectivity
assumption)

Assume now that `G` is seven-connected and that the full-subgraph packing
number of `A` is one.  Suppose `A` contains a set `W` of at most two
vertices meeting every portal set `N_A(s)`, `s in S`.  Then at least one
of the following holds.

1. Some nonempty connected `X subseteq A` has `|N_G(X)|=7`, and this
   neighbourhood is the boundary of an actual nontrivial separation.
2. `A` contains a repair support and a disjoint residual full subgraph.
3. The graph `G[A]` is two-connected, `W={p,q}` is a minimal
   two-vertex contact transversal, and, after possibly interchanging
   `p,q`,

   \[
       N_A(b)\cap W=\{p\},
       \qquad N_A(i)\cap W=\{q\}\quad(i\in I).          \tag{3.1}
   \]

   Put

   \[
       X_b=N_A(b)-W,
       \qquad X_I=\left(\bigcup_{i\in I}N_A(i)\right)-W.             \tag{3.2}
   \]

   These sets are nonempty and disjoint.  For every `x in X_b` and
   `y in X_I`, the literal graph `G[A]` has no pair of vertex-disjoint
   paths joining `x` to `y` and `p` to `q`; consequently it is a spanning
   subgraph of an `(x,p,y,q)`-web.

Thus the only case which returns neither an order-seven boundary nor a
repair/full-subgraph pair is a labelled alternating Two-Paths web.  No edge
belonging only to a web completion is asserted to be an edge of `G`.

### Proof

Every component of `G[A]` is `S`-full: its neighbourhood is contained in
the seven-set `S`, and it separates that component from the nonempty
opposite side.  Seven-connectivity forces equality.  Packing number one
therefore makes `G[A]` connected.

If `|A|<=2`, take `X=A`: its full neighbourhood is the original literal
seven-set `S`, so outcome 1 holds.  Assume henceforth that `|A|>=3`.

If it has a cutvertex, the audited boundary-full cutvertex theorem gives
outcome 1 or 2.  Hence assume `G[A]` is two-connected.

First suppose `W={p}`.  If `p` is the unique portal of some `s in S`,
then `G[A]-p` is connected and

\[
                         N_G(A-\{p\})=\{p\}\cup(S-\{s\}),            \tag{3.3}
\]

which is outcome 1.  Otherwise `G[A]-p` is connected and contains a
path from a neighbour of `b` outside `p` to a neighbour of `I` outside
`p`; a one-vertex path is allowed.  This is a repair support.  The
singleton `\{p\}` is disjoint, connected and `S`-full, giving outcome 2.

Suppose next that `W={p,q}` and no singleton subset of `W` is a contact
transversal.  If some boundary vertex has a unique portal `w`,
two-connectivity makes `G[A]-w` connected and seven-connectivity gives

\[
                         N_G(A-\{w\})=\{w\}\cup(S-\{s\}),            \tag{3.4}
\]

so outcome 1 holds.  If a vertex `w in A` is adjacent to `b` and to a
member of `I`, the singleton `\{w\}` is a repair support.  The graph
`G[A]-w` is connected, and the absence of a unique portal makes it
`S`-full, giving outcome 2.

We may exclude both events.  Since `W` meets every portal set, `b` is
adjacent to at least one of `p,q`; it cannot be adjacent to both, because
each member of `I` has a neighbour in `W`, which would give a common
repair vertex.  Orient `W` so that `b` meets `p`.  No member of `I` can
meet `p`, and hence every member of `I` meets `q`.  This proves (3.1).
The exclusion of unique portals makes both sets in (3.2) nonempty, and
the exclusion of a common repair vertex makes them disjoint.

Fix `x in X_b` and `y in X_I`.  If there are vertex-disjoint paths `P,Q`
joining `x` to `y` and `p` to `q`, respectively, then `P` is a repair
support.  The path `Q` contains both members of the contact transversal,
so it is `S`-full and is a disjoint residual full subgraph.  This is
outcome 2.  In its absence, the Two Paths theorem says that `G[A]` is a
spanning subgraph of an `(x,p,y,q)`-web.  The conclusion holds for every
choice of `x,y`, proving outcome 3. \(\square\)

## 4. Corollary for the Kempe-fan separator

### Corollary 4.1

Under (1.1), assume that `G` is not six-colourable, every proper minor of
`G` is six-colourable, `G` is seven-connected and `K_7`-minor-free.  Assume
that the separation is the one returned by the Kempe-fan
packing-or-separation theorem.  Orient it so that `A` is the side carrying
the restricted colouring.  Name the boundary as in that theorem, and put

\[
        D=J\cup\{q\},\qquad E=\{b,z_1\},\qquad z=z_2,                 \tag{4.1}
\]

where `z_1` is chosen to share the colour of `b`.  Then:

1. if the full-subgraph packing number of `A` is at least two, the
   colouring gives one of the two literal first-entry paths in
   Corollary 2.1; and
2. if that packing number is one and `A` has a boundary-contact
   transversal of order at most two, Theorem 3.1 gives an order-seven
   boundary, a repair support disjoint from a full connected subgraph, or
   a labelled alternating web.

### Proof

The Kempe-fan theorem gives `D` one monochromatic colour and `E` a second,
distinct colour, so all hypotheses concerning the one-sided colouring in
Corollary 2.1 hold.  Packing number at least two supplies its two disjoint
full connected subgraphs and proves item 1.  Packing number one and the
stated transversal are exactly the hypotheses of Theorem 3.1, proving item
2. \(\square\)

This is an orientation theorem, not a closure theorem.  The exact-seven
packet theorem ensures that at least one shore has packing number one, but
does not decide whether it is the shore carrying the Kempe-fan colouring.

## 5. Exact scope

Corollary 2.1 removes the boundary-orientation ambiguity: both high-demand
partitions give a first-entry path in the coloured open side and into the
same named full connected subgraphs.  It still does not act at that first
entry or produce the two full connected subgraphs when their packing number
is one.

Theorem 3.1 removes the earlier three-connectivity hypothesis from the
contact-transversal reduction.  Its repair/full-subgraph outcome is not by
itself a `K_7` model: it need not preserve the five already selected
far-side branch sets or the one-sided equality partition.  In the web
outcome, the remaining proof must use contraction-critical colouring data
to break the alternating web, rather than treating a completion edge as a
host edge.  Consequently neither residual is promoted here as terminal.

## 6. Dependencies

- [exact packet reflection](../results/hc7_exact7_adaptive_packet_reflection.md)
- [exact-seven full-subgraph packing](../results/hc7_exact_seven_packet_packing.md)
- [Kempe-fan packing or exact-seven boundary](../results/hc7_kempe_fan_or_exact_seven_boundary.md)
- [two-full-subgraph Kempe compression](hc7_exact7_two_full_subgraph_kempe_compression.md)
- [low-cut reduction in a boundary-full component](../results/hc7_boundary_full_component_low_cut_reduction.md)
- Fabila-Monroy and Wood, *Rooted K4-Minors*, Lemma 2 (Two Paths theorem)
