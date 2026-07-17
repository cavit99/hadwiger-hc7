# Audit of the component-contact defect theorem

**Verdict:** GREEN for the exact theorem revision identified below.

## Audited revision

The audited file is `results/hc7_component_contact_defect_theorem.md`.

**Source SHA-256:**
`247de0124f0fadf2000aa2984e77c709fece88d2daf9515fae9cd8ed4e1b44a5`.

The revision also received an independent second audit.  That audit checked
the mixed-label lift, defect and equality identities, both move formulae,
the four-nonempty-part scope, and the small-order exceptions.  Its verdict
for the exact source hash above was GREEN.

## 1. Seven-set component count

After contracting each internal component of each of the seven disjoint
sets, there are `n=sum c_i` quotient vertices.  For a fixed unordered pair
`i,j`, the induced quotient on those two component classes has `c_i+c_j`
vertices and `r_ij` components, so it has at least
`c_i+c_j-r_ij` distinct simple edges.  Different unordered index pairs use
disjoint edge sets.  Summing gives

\[
          |E(J)|\ge6n-\sum_{i<j}r_{ij}.
\]

The assumed bound makes this at least `5n-14`, one more than the exact
`5n-15` extremal bound for a `K_7`-minor-free simple graph.  The contraction
and deletion operations are legitimate even though the original seven sets
need not be connected.

## 2. Lift from the component-contact graph

At a valid cut, `C_q`, `U_q`, and `{z}` are disjoint connected pairwise
adjacent sets.  Every selected quotient vertex represents a connected
subgraph disjoint from those anchors and adjacent to all three.  Therefore a
`K_4` model in the component-contact graph lifts branch set by branch set and
combines with the three anchors to give seven disjoint connected pairwise
adjacent branch sets.  A quotient branch set is allowed to contain different
protected labels; no step of the lift requires label purity.

For the alternative component-count proof, the three anchor pairs and the
twelve anchor--protected pairs contribute fifteen component counts equal to
one.  Lemma 1.1 consequently reduces to

\[
        15+\sum_{K<K'}r_{KK'}
           \le (3+C)+14,
\]

or `sum r_KK'<=C+2`, exactly `Delta<=0`.

## 3. Rank identity and equality case

For each bichromatic graph, `rho_KK'=c_K+c_K'-r_KK'` is the number of
edges in a spanning forest.  Every part occurs in exactly three pairs, so

\[
 \sum\rho_{KK'}=3C-\sum r_{KK'}=2C-2-\Delta.
\]

The six forests have disjoint edge sets.  Thus `Delta<=0` produces a
spanning subgraph with at least `2C-2` edges, above the `2C-3` extremal
bound for `K_4`-minor-free graphs.

When `Delta=1`, the forest union has exactly `2C-3` edges.  In a
`K_4`-minor-free host it is edge-maximal and hence a two-tree.  The full
component-contact graph cannot have an additional edge, because that would
exceed the same extremal bound.  Conversely, a two-tree is chordal.  A
shortest cycle in a bichromatic induced subgraph would be an induced cycle
of length at least four in the two-tree, impossible.  Hence every
bichromatic graph is a forest, its ranks sum to all `2C-3` edges, and the
displayed identity gives `Delta=1`.  The four nonempty parts ensure `C>=4`,
so none of the small-order exceptions to the standard extremal formulation
is relevant.

## 4. Move formulae

When one vertex is added to part `K`, in pair `K,K'` it merges exactly the
`t_K'` old components it meets, with the formula `r'-r=1-t_K'` also valid
for zero contacts.  The total selected component count increases by one.
Thus

\[
                 \Delta'-\Delta=2-\sum t_{K'}.
\]

For a split into `s` vertices, all unchanged bichromatic components remain
unchanged.  The old component containing the split vertex is replaced by
`kappa_K'` components, giving `r'-r=kappa_K'-1` for each of the three
other parts, while the total selected component count increases by `s-1`.
This gives

\[
                 \Delta'-\Delta=\sum\kappa_{K'}-s-2.
\]

The no-new-contact hypothesis in Proposition 4.2 is stated explicitly and
is exactly what is needed for the incidence graph to account for the whole
change.

## 5. Sharp labelled obstruction

The graph on `a,b,c,d1,d2` has seven edges and is obtained from triangle
`abc` by stacking `d1` on `ac` and `d2` on `ab`; it is a two-tree and has
no `K_4` minor.  All six label pairs occur.  Because the `A`, `B`, and `C`
parts are singletons, they must be selected.  Connectivity of the selected
`B`--`D` union requires selecting `d2` and not `d1`; connectivity of the
selected `C`--`D` union requires selecting `d1` and not `d2`.  Hence no
part-respecting pairwise-connected selection exists.  Direct substitution
also gives `Delta=1`.

For the recorded 44-vertex quotient, `K_4` minus one edge has five connected
bichromatic pairs and one pair with two components.  Thus `sum r=7`,
`C=4`, and `Delta=1`, confirming the theorem's stated interpretation.

## 6. Scope

The theorem proves a `K_7` model when the component-contact graph has a
`K_4` minor and classifies the minimum-defect obstruction.  It does not show
that a simplicial lifted component of the resulting two-tree can be split,
does not bound its literal neighbourhood above, and does not derive the
fixed-pair outcome.  Those are correctly retained as the next
contraction-critical step.

## Unresolved assumptions or gaps

None for the stated theorem and move formulae.  The label-preserving
contact-distribution statement in Section 6 of the theorem remains open.
