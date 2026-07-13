# Palette anchors give a label-preserving rooted star

## 1. The uniform lemma

### Theorem 1.1 (palette-anchor rooted star)

Let `c` be a proper colouring of a graph `H`, let `a` have colour
`alpha`, and let `B` be a set of colours different from `alpha`.  For each
`beta in B`, choose a vertex `t_beta` of colour `beta` in the
`alpha/beta` component containing `a`.  Then `H` contains a rooted
`K_{1,|B|}` minor whose centre bag contains `a` and whose leaf bag for
`beta` is the singleton `{t_beta}`.

Equivalently, there is a connected set

\[
 C\subseteq V(H)-\{t_\beta:\beta\in B\}
\]

which contains `a` and is adjacent to every `t_beta`.

#### Proof

For each `beta`, take an `a`--`t_beta` path in the corresponding
`alpha/beta` component and truncate it when it first reaches `t_beta`.
Its interior has colours only `alpha,beta`.  Hence it contains no
`t_gamma` with `gamma ne beta`; by truncation it contains no earlier copy
of `t_beta` either.

Delete all the vertices `t_beta` and let `C` be the component containing
`a` in the remaining graph.  The path just chosen, with its last vertex
deleted, lies in `C`, so its last edge joins `C` to `t_beta`.  Thus `C`
is adjacent to every displayed singleton.  The sets

\[
                         C,\quad \{t_\beta\}\ (\beta\in B)
\]

are disjoint and connected, and their required star adjacencies are
literal.  \(\square\)

The statement is parameter-uniform and uses no disjoint-path theorem.
The colour labels themselves enforce terminal avoidance: a path using
palette `alpha/beta` cannot pass through an anchor of a third colour.

### Corollary 1.2 (a full Kempe fan contains a two-apex frame)

Let `pa` be an edge of a graph `G`, let `H` be a subgraph of `G-pa`, and
let `p,a` have colour `alpha` in a proper colouring of `H`.  Suppose that,
for every one of the other `r` colours `beta`,
the `alpha/beta` component containing `a` also contains `p`.  Then `G`
has a minor

\[
                         K_2\vee\overline{K_r},                 \tag{1.1}
\]

in which one centre bag is `{p}`, the other contains `a`, and the `r`
independent-side bags are literal, distinctly coloured neighbours of
`p`.

#### Proof

For each `beta`, choose a simple `a`--`p` path in the corresponding
two-colour component and let `t_beta` be its neighbour of `p`.  The
vertices `t_beta` have their distinct colours `beta`.  Truncate each path
at `t_beta` and apply Theorem 1.1 to their union.  It gives a connected
bag `C` containing `a`, disjoint from all `t_beta`, and adjacent to each
of them.  The truncation also keeps `p` outside `C`.  The original edge
`pa` joins `{p}` to `C`, while every `pt_beta` is an edge.  Hence

\[
                    \{p\},\quad C,\quad
                    \{t_\beta\}\ (\beta\ne\alpha)
\]

is the claimed model.  No adjacency among the last bags is asserted or
needed.  \(\square\)

For a seven-critical graph the concentrated branch of the coupled-star
lemma therefore contains a literal `K_2`-apex frame over five labelled
leaves.  This is not a `K_7` by itself, but it explains why the sharp
static survivor is two-apex-shaped rather than an arbitrary fan.

## 2. Application to the coupled-star gate

In Lemma 5.5 of `hadwiger_c6_rank22_nested_cut_exchange.md`, let `B_0`
be the subfamily of exclusive colours having distinct beta-coloured gate
anchors.  Theorem 1.1 turns those anchors into a single connected
protected centre, containing the operated leaf, with one literal rooted
leaf at every anchor.  All remaining exclusive colours pass through the
at-most-three-vertex alpha warehouse.

Thus the exact residue is stronger than a partial transversal:

\[
 \boxed{\text{one rooted palette star}\quad\text{plus}\quad
        \text{an alpha warehouse of order at most three}.}
\]

This still does not give the colourful rooted `K_4` required for `K_7`.
The anchor labels are palette labels rather than boundary-portal labels,
and a rooted star can be the planar wheel obstruction.  Indeed, even four
anchors on the `C_4` induced by
`{c0,c2,c3,c5}` need not give a rooted `K_4` at those four rim vertices.
The next theorem must use the opposite exclusive family, the unique pole
orientation, or a common boundary state; Theorem 1.1 does not hide that
gap.
