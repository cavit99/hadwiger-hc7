# Independent audit of exact-seven critical-triangle full-subgraph demand

**Verdict:** GREEN for Theorem 2.1 and its exact trust boundary at the
source revision identified below.

**Audited source:** `hc7_exact7_critical_triangle_full_subgraph_demand.md`,
SHA-256

```text
5715ddbabac72efd27cfa6c5242c9026e64f6dcc7b1416707fea2842513931c6
```

The original GREEN audit was performed on source revision
`a46b2541cfd4428717663845aa62a01c2c7b21c72bc2939d5e209e898348998a`.
After promotion, the source revision was
`914bba1cbc947cbb2d37139cdfc1b61bb601ff2eeae1cfe45561a669ef67387d`.
The current revision renames the source from “packet demand” to
“full-subgraph demand” and replaces that project shorthand in its title and
expository prose by the defined standard-language object: pairwise disjoint
connected subgraphs adjacent to every literal boundary vertex.  It changes
no graph, hypothesis, formula, proof step, or trust-boundary conclusion.
Sections 1--7 below were replayed against the current source; the displayed
current hash is the governing audit pin.

This is a separate internal mathematical audit, not external peer review.
It reconstructed the two transition placements, the exact-seven
full-subgraph packing vector, the direction of reflection, palette alignment and gluing,
both boundary partition counts, and all four clique restrictions.
The strengthened revision's demand-critical singleton merge and the
location of its bichromatic path were audited separately in Section 6.

## 1. Transition placement and the actual separation

The cited critical-triangle theorem supplies one of two placements for the
single interchanged two-colour component `D`.

- In the centre placement, `v in D` and `a,b notin D`.  Both deleted
  edges `va,vb` join `D` to `S=N_G(D)` and therefore put `a,b in S`.
- In the outer-edge placement, `a,b in D` and `v notin D`.  Again both
  deleted edges join `D` to `S`, now putting `v in S`.

Thus neither edge is internal to the opposite open side `R` or to the
boundary.  The two Kempe-related colourings differ only on `D`, so their
restrictions to

\[
                             O=G-D
\]

agree vertexwise.  Since both deleted edges have their other endpoint in
`D`, neither belongs to the induced graph `O`; this common restriction is
a proper colouring of the original closed shore `O`.  On
`C=G[D\cup S]`, the response signatures show that `phi` fails only on
`va`, while `psi` fails only on `vb`.  This verifies item 1 without
treating either edge-deletion colouring as a colouring of the whole
original graph.

The additional hypotheses that `D` is nondominating and `|N_G(D)|=7`
make `(C,O)` an actual order-seven separation: `D` is one nonempty open
side and `R=V(G)-(D\cup S)` is the other.

## 2. Full components and the packing vector

Let `K` be a component of `G-S`.  Its neighbourhood is contained in `S`.
If it missed one literal boundary vertex, at most six vertices would
separate `K` from a component on the other open side.  Seven-connectivity
therefore gives

\[
                              N_G(K)=S.
\]

Every component is consequently an `S`-full connected subgraph, so both
packing numbers are positive.

The promoted exact-seven full-subgraph packing theorem applies to this literal actual
separation and gives

\[
             \nu_D+\nu_R\le4,
             \qquad\min\{\nu_D,\nu_R\}=1.
\]

The promoted adaptive full-subgraph reflection theorem excludes `(1,3)` in
either orientation.  The exhaustive remaining vectors are therefore

\[
                         (1,1),(1,2),(2,1).
\]

If a shore of packing number one had two components, those two components
would themselves be disjoint full connected subgraphs.  Hence that shore
is connected.  This proves every assertion in item 2.

## 3. Full-subgraph demand and the reflection direction

The equality blocks of `Pi` are independent because `Pi` comes from a
proper colouring of `F=G[S]`.  Choose a maximum clique among its singleton
blocks.  Every remaining block requires one distinct boundary-full connected
subgraph in the
reflection lemma, so the exact number required is

\[
 d_F(\Pi)=|\Pi|-\omega(F[\operatorname{sing}(\Pi)]).
\]

Assume `d_F(Pi)<=nu_R`.  Contract the required full connected subgraphs in the
`R`-closed shore, together with their assigned independent boundary
blocks.  The exact reflection lemma has two outcomes.

1. The corresponding connected sets and retained singleton clique already
   form an explicit `K_7`-minor model; or
2. a six-colouring of the resulting proper minor pulls back to a proper
   colouring `eta` of the **untouched** original closed shore `C`, with
   equality partition on literal `S` exactly `Pi`.

The direction is correct: full connected subgraphs in `R` are used precisely
because the colouring to be produced is on `C`.  None is expanded on the shore
where it was contracted.

Item 1 already supplies the proper colouring `phi|O` of the other closed
shore with the same exact partition.  Exactness makes the block-to-colour
maps injective.  A permutation of the six colours aligns them blockwise,
after which the two colourings agree at every boundary vertex and glue
because there is no `D-R` edge.  This would six-colour `G`.

Both reflection outcomes contradict the setup, proving the strict and
correctly oriented inequality

\[
                              d_F(\Pi)>\nu_R.
\]

This also verifies item 3's pre-contradiction terminal statement.

## 4. Centre-placement partition

In the centre placement, `a,b in S` have colours `alpha,beta`, which are
different because `ab` is an edge.  Every vertex in `S-{a,b}` has one of
the other four colours.  Saturation of the `alpha` side of `D` ensures
that all four occur among these five vertices.  Their multiplicities are
therefore `2,1,1,1`.

The repeated two-set `I` is independent.  All other boundary vertices are
singleton blocks, so with `Q=S-I` one has

\[
 |Q|=5,
 \qquad a,b\in Q,
 \qquad ab\in E(F),
 \qquad |\Pi|=6,
\]

and

\[
                  d_F(\Pi)=6-\omega(F[Q]).
\]

If `nu_R=2`, strict demand gives `omega(F[Q])<=3`, so `F[Q]` is
`K_4`-free.  If `nu_R=1`, it gives `omega(F[Q])<=4`, so `F[Q]` is
`K_5`-free.  These are exactly the restrictions in item 4.

## 5. Outer-edge-placement partition

In the outer-edge placement, `v in S` has colour `alpha`, while every
other boundary vertex avoids both `alpha,beta`.  Thus `v` is the unique
`alpha` singleton and `beta` is absent from `S`.  Saturation of both colour
sides of `D` ensures that all four untouched colours occur on the six-set
`S-{v}`.

The only positive multiplicity partitions of six into four parts are

\[
                    (3,1,1,1),\qquad(2,2,1,1).
\]

Adding the singleton `{v}` gives five blocks.  In the first case the
singleton set `Q` consists of `v` and three further vertices, so `|Q|=4`;
in the second it consists of `v` and two further vertices, so `|Q|=3`.
In both cases

\[
                  d_F(\Pi)=5-\omega(F[Q]).
\]

If `nu_R=2`, strict demand gives `omega(F[Q])<=2`, so `F[Q]` is
triangle-free.  If `nu_R=1`, it gives `omega(F[Q])<=3`, so `F[Q]` is
`K_4`-free.  This verifies item 5.

## 6. Demand-critical singleton merges when `nu_R=2`

Give the opposite closed shore `O=G[R\cup S]` its common proper colouring
`phi|O`.  If `{x}` and `{y}` are nonadjacent singleton blocks, their
colours are distinct and no other boundary vertex has either colour.  The
promoted singleton-block Kempe exchange therefore has two exhaustive
outcomes.

1. If `x,y` lie in one component of their two-colour graph, a shortest
   path between them has no internal boundary vertex.  Since the path is
   contained in `O`, all its internal vertices lie in
   `O-S=R`.
2. Otherwise, switching the component through one endpoint gives a proper
   colouring of `O` whose exact boundary partition `Pi'` is obtained by
   merging only `{x},{y}`.

The demand computations in the second outcome are exact.

- In the centre placement, the original partition consists of the
  repeated pair `I` and five singleton blocks `Q`.  After the merge it has
  five blocks and singleton set `Q-{x,y}`.  Under the stated triangle
  hypothesis,

  \[
              d_F(\Pi')=5-omega(F[Q-\{x,y\}])=5-3=2.
  \]

- In the outer-edge subcase with `|Q|=4`, the original partition has one
  non-singleton triple and four singleton blocks.  After the merge it has
  four blocks and the two singleton vertices in `Q-{x,y}`.  Their stated
  edge gives

  \[
              d_F(\Pi')=4-omega(F[Q-\{x,y\}])=4-2=2.
  \]

Because `nu_R=2`, exact full-subgraph reflection may use two disjoint full
connected subgraphs in `R`.  Its direction is the same as in Section 3:
the contractions occur in `R\cup S` and produce either a `K_7`-minor
model or a proper colouring of the untouched closed shore `C` inducing
exactly `Pi'`.  In the latter case, it glues to the newly Kempe-switched
colouring of `O`.  Thus the merge outcome contradicts the hypotheses, and
the path outcome is forced.

No disjointness between that path and the two full connected subgraphs is
proved or needed for this contradiction.  The source records this
limitation correctly.

## 7. Dependency eligibility and exact scope

The proof uses the following promoted dependencies.

1. `results/hc7_joint_persistent_incident_colour_fork.md`, source
   SHA-256

   ```text
   21b5fd5c523efb673ca11b0e604e0e81d173a5dbda677baa235efd8924d4b865
   ```

   has an adjacent GREEN audit pinned to that exact revision.
2. `results/hc7_exact_seven_packet_packing.md`, source SHA-256

   ```text
   501f581d764607ef9cd13b854150dae95ea251efde0fdd28c77bb9632415fc57
   ```

   has an adjacent GREEN audit pinned to that exact revision.
3. `results/hc7_exact7_adaptive_packet_reflection.md`, source SHA-256

   ```text
   14690180c44a9e5836591a54c4c7cdb7a26f1a2c78147470257072d5bc425e96
   ```

   now has an adjacent GREEN audit pinned to that exact revision.  Lemma
   2.1 and the `(1,3)` consequence were also independently reconstructed
   during the present audit.
4. `results/hc7_exact7_singleton_block_kempe_exchange.md`, source
   SHA-256

   ```text
   d0157bc10b6f588a7e7fd714b1e5be02faee3da35f2d35ce43cf03f5237c91e2
   ```

   now has an adjacent GREEN audit pinned to that exact revision.  The
   exact two-component proof was also independently reconstructed at this
   hash for Section 6.

The theorem applies only after a direct Kempe transition has produced a
nondominating component with an exact seven-vertex full neighbourhood.  It
does not handle Kempe-separated response families, larger neighbourhoods,
or the connected-dominating five-chromatic core.  The strict demand and
clique restrictions describe the residual configurations; they do not
eliminate them.  No palette colour is assigned to a near-clique branch-set
label.
