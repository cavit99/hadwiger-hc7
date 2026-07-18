# Independent audit: two full connected subgraphs and Kempe compression

**Verdict:** **GREEN.**  The adaptive packet-reflection step, the complete
classification of high-demand boundary partitions, both Kempe-switch cases,
and the two exact contraction arguments are valid under the stated
hypotheses.  The strengthened theorem removes the former exact-four-block
normalization gap in its intended Kempe-fan application.  It remains
conditional on the existence of two disjoint boundary-full connected
subgraphs on the relevant shore; they need not be adjacent to one another.

**Audited source:**
`results/hc7_exact7_two_full_subgraph_kempe_compression.md`.

**Source SHA-256:**
`996f6e4cb7c1d00a90c6e2b57bd2f3f441fc09aa1553b490a60154d77a3692dd`.

## 1. Exact hypotheses

The theorem assumes:

1. `G` is not six-colourable and every proper minor of `G` is
   six-colourable;
2. `V(G)=A dotcup S dotcup B`, where `A,B` are nonempty and there is no
   edge between them;
3. the literal seven-vertex boundary is

   \[
     S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
     \qquad |D|=3,\quad |E|=2;
   \]

4. `G[A union S]` has a proper six-colouring `c` in which `D` and `E`
   are monochromatic in two distinct colours; and
5. `G[A]` contains disjoint connected subgraphs `C_D,C_E`, each adjacent
   to every literal vertex of `S`.

The setup does not initially prescribe the colours of `r,z`, nor require
the complete boundary equality partition to have four blocks.  Since `D`
and `E` are monochromatic in a proper colouring, each is independent.  Let
`Pi` denote the complete equality partition induced by `c` on `S`; it is a
partition into independent blocks.

## 2. Exact use of adaptive packet reflection

The cited exact packet-reflection lemma applies to a partition `Omega` of a
literal seven-vertex boundary and `q` disjoint boundary-full connected
subgraphs on one open shore.  If

\[
 d_H(\Omega)
   =|\Omega|-
      \omega\bigl(H[\operatorname{sing}(\Omega)]\bigr)
 \le q,
\]

it constructs either a `K_7`-minor model or a proper-minor colouring of the
opposite closed shore whose boundary equality partition is exactly
`Omega`.

Here `C_D,C_E` are precisely two such connected subgraphs, so `q=2` and the
lemma applies to `Pi` whenever `d_H(Pi)<=2`.  The contractions used by the
reflection lemma are supported in `A union S`; its colouring is expanded
only on the untouched closed side `G[B union S]`.

The source correctly excludes the lemma's `K_7` alternative in this
application.  Since `D,E` already account for five boundary vertices and
`r,z` add at most two further blocks, `|Pi|<=4`.  In the proof of the
reflection lemma, the first `K_7` case is the zero-contraction case in which
all seven boundary blocks are singleton vertices forming `K_7`, and the
other is the explicit `|Pi|=7` branch-set construction.  Neither can occur
when `|Pi|<=4`.  Exact reflection is therefore the only possible outcome.

If `d_H(Pi)<=2`, the reflected colouring and `c` induce the same complete
partition.  The injection matching their block colours extends to a
permutation of the six colour names.  After applying it on one side, the
closed-side colourings agree on every boundary vertex and glue because
there is no `A-B` edge.

## 3. Exhaustive high-demand classification

The blocks containing `D` and `E` are distinct.  Consider how `r,z` can
occur in `Pi`.

If either `r` or `z` joins the `D`- or `E`-block, then `Pi` has at most
three blocks.  With at most two blocks, demand is automatically at most
two.  If it has exactly three blocks, the other one of `r,z` is a singleton,
so the singleton graph has clique number at least one and

\[
                         d_H(Pi)\le3-1=2.
\]

Thus high demand is impossible in this branch.

If neither `r` nor `z` joins the `D`- or `E`-block, there are exactly two
possible complete equality partitions:

\[
 \begin{aligned}
   \Pi_A&=D\mid E\mid\{r\}\mid\{z\},\\
   \Pi_B&=D\mid E\mid\{r,z\}.
 \end{aligned}
\]

For `Pi_A`, the singleton graph is `H[{r,z}]`.  If `rz` is an edge, its
clique number is two and the demand is `4-2=2`; if `rz` is absent, its
clique number is one and the demand is `4-1=3`.  The partition `Pi_B` has
three blocks and no singleton blocks, so its demand is three.  Consequently

\[
 d_H(Pi)>2
 \quad\Longleftrightarrow\quad
 \bigl(Pi=\Pi_A\text{ and }rz\notin E(G)\bigr)
 \text{ or }Pi=\Pi_B.
\]

This exhausts every placement of `r,z`; there is no omitted boundary
partition.

## 4. The two connected block representatives

Put

\[
                   K_D=C_D\cup D,\qquad K_E=C_E\cup E.
\]

Both unions are connected because their named connected subgraphs are
adjacent to every vertex of the corresponding boundary block.  They are
disjoint.  No edge between `C_D` and `C_E` is needed: fullness of `C_D`
supplies a literal edge from `C_D` to every vertex of `E subseteq K_E`
(and symmetrically fullness of `C_E` supplies edges into
`D subseteq K_D`).  Hence `K_D,K_E` are adjacent.  Contracting a spanning
tree in each union is a proper-minor operation: both unions contain boundary
vertices and a nonempty connected subgraph in `A`, so literal
subgraph--boundary edges are contracted.

In any six-colouring of the minor, the two representatives have distinct
colours because they are adjacent.  Each is adjacent to both `r,z` through
the full boundary contact of `C_D,C_E`, so neither `r` nor `z` uses either
representative colour.  Expanding on `G[B union S]` is proper: `D,E` are
independent, and every edge from one of their vertices to an untouched
vertex became an edge incident with its representative.

Therefore the returned complete boundary equality partition is exactly one
of `Pi_A,Pi_B`.  The contraction does not return a hidden third case.

## 5. Case A: the original partition is `Pi_A`

If the returned partition is also `Pi_A`, exact-partition colour alignment
and gluing give a six-colouring of `G`.  Otherwise the returned partition is
`Pi_B`.

Let

\[
                         \gamma=c(r),\qquad\eta=c(z).
\]

These colours are distinct.  Because the original partition is exact,
`r,z` are the only boundary vertices using either colour.  If their
`gamma,eta` Kempe components in `G[A union S]` are different, swapping the
two colours on the component containing `r` changes only `r` on the
boundary, produces exactly `Pi_B`, and glues to the returned colouring.

Otherwise the component contains an `r-z` path.  Every internal vertex of
every such path lies in `A`, because no other boundary vertex has either
colour.  Suppose one such path `P` avoids `C_D union C_E`.  Split its vertex
sequence at any edge into nonempty connected sets `P_r,P_z` containing
`r,z`, respectively.  The four sets

\[
                         K_D,\quad K_E,\quad P_r,\quad P_z
\]

are pairwise disjoint: the path avoids the two named connected subgraphs,
its internal vertices lie in `A`, and no vertex of `D,E` has either path
colour.  They are pairwise adjacent: `K_D-K_E` follows from the automatic
fullness adjacency above, `P_r-P_z` is the split edge, and each `K`-set has
literal edges to the boundary vertices `r,z` lying in the two path parts.

After contracting spanning trees in all four sets, the four representatives
form a clique.  Expanding only on `G[B union S]` assigns four distinct
colours to the blocks `D,E,{r},{z}` and therefore forces exactly `Pi_A`, not
a coarsening.  It glues to `c`.  Thus in the non-six-colourable setup every
such bichromatic `r-z` path meets `C_D union C_E`.

## 6. Case B: the original partition is `Pi_B`

Write

\[
                         \kappa=c(r)=c(z).
\]

If the returned partition is `Pi_B`, it aligns and glues immediately.
Suppose the returned partition is `Pi_A`.  Its four blocks have four
distinct colours.  The original colouring uses exactly the three colours
of `D`, `E`, and `{r,z}` on the boundary, leaving three palette colours
absent there.

Choose one such absent colour `theta`.  A permutation of the returned
colour names can simultaneously:

- match its `D`-colour to the original `D`-colour;
- match its `E`-colour to the original `E`-colour;
- give `z` the colour `kappa`; and
- give `r` the colour `theta`.

The four target colours are distinct, so this partial bijection extends to
a permutation of all six colours.

In the original colouring, `theta` is absent from `S`, while `kappa` occurs
there exactly at `r,z`.  If the `kappa,theta` Kempe component containing
`r` does not contain `z`, swapping its colours changes only `r` on the
boundary.  The boundary colours then agree vertex-by-vertex with the
aligned returned `Pi_A` colouring, so the two sides glue.

Otherwise the component contains an `r-z` path, every internal vertex of
which lies in `A`.  Suppose such a path `P` avoids `C_D union C_E`.  Retain
the whole vertex set of the path as one connected set.  The three sets

\[
                             K_D,\quad K_E,\quad V(P)
\]

are disjoint for the same literal reasons as in Case A and pairwise
adjacent: each full connected subgraph contacts `r` and `z` on `P`, and the
two `K`-sets are adjacent to one another.

Contracting spanning trees in the three sets is a proper minor.  Its three
representatives form a clique and correspond exactly to the boundary
blocks `D,E,{r,z}`.  Hence every six-colouring gives these blocks three
distinct colours, and expansion on `G[B union S]` induces exactly `Pi_B`.
It glues to `c`.  Thus every `kappa,theta` path joining `r` to `z` meets
`C_D union C_E` in the surviving branch.

## 7. Application to the Kempe-fan separator

For the boundary returned by the Kempe-fan theorem, the intended
substitution is

\[
          D=J\cup\{q\},\qquad E=\{b,z_1\},\qquad z=z_2,
\]

where `z_1` is chosen as a separator vertex sharing the colour of `b`.
That theorem gives `J union {q}` one monochromatic colour and `b,z_1` a
second, distinct monochromatic colour.  The strengthened setup therefore
does not require any further exact-partition normalization: every possible
colour collision involving `r,z_2` is either reflected because its demand
is at most two or is one of the two Kempe cases audited above.

What the Kempe-fan theorem does **not** provide by itself is the pair
`C_D,C_E` of disjoint connected subgraphs on the relevant open shore, each
adjacent to all seven literal boundary vertices.  Establishing
those two subgraphs, or obtaining a terminal outcome when they do not exist,
is the remaining input needed to apply this theorem in the active proof
spine.

## 8. Trust boundary

The GREEN verdict proves only the conditional synchronization-or-first-entry
theorem stated in the source.  It does not:

- produce the two boundary-full connected subgraphs;
- determine which of them is first met in a model-improving way;
- turn the forced first entry into a smaller labelled minor model or a
  strictly smaller host separation;
- construct a `K_7`-minor model from the path outcome; or
- prove `HC_7`.

Those are explicit remaining obligations, not hidden conclusions of the
packet-reflection or Kempe arguments.
