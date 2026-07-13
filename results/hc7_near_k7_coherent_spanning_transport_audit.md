# Independent audit: coherent spanning transport

## Verdict

**GREEN.**  The proof in
`hc7_near_k7_coherent_spanning_transport.md` is valid as written.  It
uses only connectedness of the host, disjointness of components outside
the old model union, and `K_7`-minor-freeness.  It does not silently
assume that the starting model is spanning.

## Line-by-line checks

Let

\[
 M=A\cup B\cup C\cup U_1\cup\cdots\cup U_4
\]

and let `R` be the union of the components of `G-M` which have a
neighbour in `A`.

1. Each component used in `R` is connected and has an edge to the
   connected set `A`.  Distinct such components need not meet each
   other; nevertheless their union with `A` is connected.  Thus the
   first assertion about `A^+=A\cup R` is correct.
2. The six foreign bags `B,C,U_1,...,U_4` retain all their old mutual
   adjacencies.  If `A^+` met both `B` and `C`, these six bags together
   with `A^+` would be seven disjoint connected pairwise adjacent branch
   sets.  Hence one fixed member `D` of `{B,C}` is anticomplete to all
   of `A^+`, not merely to the old bag `A`.
3. A component `K` of `G-M` not used in `R` has no edge to `A` by
   definition.  It has no edge to a component used in `R`, because two
   different components of `G-M` have no edge.  Therefore `K` is
   anticomplete to `A^+`.
4. Connectedness of `G` guarantees that `K` has an edge to the old model
   union.  Since it has no edge to `A`, it has an edge to a foreign bag.
   Absorbing `K` into any such bag preserves connectedness, disjointness,
   and every required old model adjacency.
5. Repeating the absorption cannot create an `A^+D` edge: every absorbed
   component was already anticomplete to `A^+`.  The selected missed
   twin is therefore coherent through the whole spanning operation.

No assertion is made that `A^+` is bipartite, that its old path remains
an induced subgraph of the whole host after absorption, or that the
other twin is adjacent to `A^+`.  In particular the argument correctly
allows the branch in which `A^+` is anticomplete to both `B` and `C`.

## Exact bridge-boundary corollary

Assume in addition that `G` is seven-connected and that the old bag `A`
is the normalized induced path `P`.  Let `K` be any component of `G-M`
which is absorbed into `A^+`.  Then

\[
                  S_K=N_G(K)
\]

is an actual vertex boundary separating `K` from the same fixed missed
twin `D`, and

\[
                         |S_K|\ge 7.                 \tag{A.1}
\]

Indeed `K` is anticomplete to `D`, so the nonempty bag `D` lies outside
`K\cup N_G(K)`.  Every path from `K` to `D` meets `N_G(K)`; hence this
neighbourhood is a genuine separator.  Seven-connectivity gives (A.1).
Moreover different absorbed components have no edges between them, so
the expanded carrier is literally the path core together with a family
of mutually anticomplete bridge pieces, each behind its own actual
order-at-least-seven boundary and each anticomplete to the same `D`.

The boundary may contain vertices in several foreign bags as well as
vertices of `P`; (A.1) is a vertex-count statement, not a bound on the
number of model labels represented.  Treating those labels as seven
distinct boundary vertices would be invalid.

## Scope

The result resolves coherence of the missed **role**, not the global
two-apex conclusion.  A rural embedding obtained after deleting the
whole bag `D` is not terminal: `D` must still be reduced to literal apex
vertices, or a labelled split/common colour state must be produced.
