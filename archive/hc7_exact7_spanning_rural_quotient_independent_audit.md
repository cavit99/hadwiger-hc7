# Final independent audit: spanning rural quotient

Audited file: `active/hc7_exact7_spanning_rural_quotient.md`, after the
outcome, root-containment, exposure, and side-terminal repairs.

## Final verdict

**GREEN.**  The repaired Theorem 2.1, repaired Lemma 3.1, and the exact-six
specialization are correct.  The earlier hostile objections have all been
discharged:

* the bilateral cell outcome now names a proper web-cell component with a
  literal three-gate and connected retained carrier, so it is nonvacuous;
* exposure is a global property of the fixed allowed carrier set `Z`;
* the absorption lemma explicitly retains `x,y` in `K_0`;
* the exact Moser specialization gives the correct restricted `Z`; and
* the same-component and side-terminal branches are no longer called an
  automatic supported-core promotion.

The exact theorem ready for promotion is:

> Let `G` be seven-connected, let `J` be an induced connected subgraph,
> and let `Z` contain `x,y` and satisfy exposure `(E)`.  If an admissible
> spanning two-pole triple exists with both nonroot pole-contact sets of
> order at least three, then some such triple has either a carrier of
> connectivity at most two, a shared nonroot portal, a set-terminal cross,
> a proper bilateral three-gated cell with connected retained carrier, or
> a planar simple whole-`J` two-pole quotient contained in a four-web rib.

This is a whole-shore theorem: no vertex of `J` is omitted from the final
triple.

## 1. Exact exposure in the Moser shore

After deleting `v,w`, a closed terminal shore has vertex set

\[
                         V(J)=V(D_t)\mathbin{\dot\cup}U
                                  \mathbin{\dot\cup}\{t\}.
\]

The source now fixes

\[
 Z=V(J)-(U-\{x,y\})=V(D_t)\cup\{t,x,y\}.
\]

Hence a nonempty `C subseteq Z-{x,y}` contains only open-shore vertices
and possibly the side terminal `t`.  An open-shore vertex has no neighbour
in the opposite open side, no neighbour at `v`, and every boundary
neighbour other than `w` lies in `J`.  The side terminal has no
opposite-side neighbour; its only possible whole-graph neighbours outside
`J` lie among `v,w` (indeed the audited exact cell also has `wt` absent).
Therefore

\[
                         N_G(C)-V(J)\subseteq\{v,w\},
\]

uniformly for every such `C`.  This proves `(E)`, including when `C`
contains `t` or contains several components.

It is essential that the other three vertices of `U` are excluded from
`Z`: they may see the opposite shore.  The repaired source does exactly
this.

## 2. The far side before seven-connectivity

Let `D` be a component of actual carrier vertices in a nonempty web cell.
The block-terminal theorem gives

\[
                 N_{J[K]}(D)=V(\Delta),\qquad |V(\Delta)|=3,
                 \qquad J[K-D]\text{ connected}.       \tag{A1}
\]

Because `J` is induced in `G` and `J[K]` is induced in `J`, (A1) also says

\[
                         N_G(D)\cap K=V(\Delta).         \tag{A2}
\]

There is a vertex beyond this neighbourhood.  The disjoint sets `Q,P`
have orders at least three and all their vertices lie on the rib, not in a
cell.  At most three of their at least six vertices belong to `Delta`.
Thus some

\[
                  r\in(Q\cup P)-V(\Delta)

\]

lies in `K-(D union N_G(D))`.  Deleting `N_G(D)` genuinely separates the
nonempty set `D` from `r`.  Seven-connectivity may therefore be invoked,
and gives `|N_G(D)|>=7`.

Exactly three neighbours lie in `K` by (A2), so at least four lie outside
`K`.  The cell has no root and `K subseteq Z`, hence `(E)` applies to `D`
and at most two of those four lie outside `J`.  At least two neighbours
therefore lie in

\[
                         J-K=X\mathbin{\dot\cup}Y.
\]

This proves the pole exposure used in the cell move.  The proof needs only
one such neighbour; the stronger count of two is harmless.

## 3. Cell evacuation and protected invariants

If `D` sees both poles, it satisfies the repaired third bullet literally:
it is nonempty, proper, connected, disjoint from the roots and all marked
portals, has the three-neighbour gate (A1), and leaves a connected carrier.

Otherwise orient it toward the pole it sees, say `X`, and replace

\[
                         (K,X,Y)\quad\text{by}\quad
                         (K-D,X\cup D,Y).
\]

The retained carrier is connected by (A1), the enlarged pole is connected
through an actual `D-X` edge, and its anticompleteness to `Y` follows from
the chosen orientation.  The parts remain induced, disjoint, and spanning;
the roots remain in the carrier; the fixed sets remain in their poles; and
the carrier remains a subset of `Z`.

Every old member of `Q union P` is a rib vertex and hence lies outside
`D`.  Its old pole edge remains present, so both contact lower bounds are
preserved.  A newly shared portal or set-terminal cross is an explicit
outcome.  If neither appears, the new triple is a smaller crossless
competitor, irrespective of its new connectivity.  This is an exact
contradiction to the minimum choice.  No captured-path monotonicity or
three-connectivity preservation is assumed.

## 4. Planar quotient

After cell evacuation every actual carrier vertex and edge lies in the
plane rib.  The quotient edge list is exhaustive:

* nonroot `alpha-K` edges are exactly `alpha Q`;
* nonroot `beta-K` edges are exactly `beta P`;
* pole--root edges are among the four outer-frame edges;
* `alpha-beta` is absent by pole anticompleteness; and
* every vertex of `J` belongs to one of the three parts.

Thus the simple quotient is a literal subgraph of the same rib.  No
completion-only edge is treated as an original edge.

## 5. Repaired absorption and exact HC input

Lemma 3.1 now assumes `x,y in K_0`.  In its distinct-component case,
every other component of `J-V(K_0)` attaches to connected `K_0`; their
union with it is therefore a connected retained carrier containing both
roots.  The two selected pole components are connected, anticomplete, and
together with the carrier span `J`.

For the exact Moser application, `X_0=A union B` contains the other three
vertices of `U`, while `K_0` contains only the trace roots `x,y` from `U`.
No component absorbed into the carrier can contain another `U`-vertex, so
the carrier lies in the repaired set `Z`.  The three old foreign portals
retain their edges to the pole containing `A union B`, and the at least
three nonroot locked attachments retain their edges to the pole containing
`L`; hence the initial spanning triple has both required lower bounds.

The side terminal may land in any of the three topological parts because
it belongs to `Z` and not to the adhesion.  The source correctly warns
that this assignment need not preserve the earlier supported-core
normalization.  Likewise, in the same-component case Lemma 3.1 supplies
only a literal `K_0`-avoiding pole connector; it is not called a labelled
promotion if it uses the side terminal.

## Valid limitations

The promoted theorem does **not**:

* preserve three-connectivity or universal capture under component
  absorption;
* convert its shared portal, linkage, or bilateral gate into a labelled
  peel or a `K_7`;
* embed either induced pole graph; or
* retain parallel attachment occurrences in its simple quotient.

Those are explicit later exchange obligations, not gaps in the spanning
trichotomy itself.
