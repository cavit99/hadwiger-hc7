# Independent audit of the compressed `HC_7` near-`K_7` spine

## Verdict

There is now one red link.

| link | verdict | exact scope |
|---|---|---|
| `P1` general-model normalization **with global coherence** | **RED / OPEN** | No theorem takes an arbitrary spanning labelled `K_7^\vee` model to the audited singleton/bipartite/two-portal shell, a literal `K_7`, or one fixed global two-apex pair. |
| `P2` bipartite total contraction | **GREEN** | Connected induced bipartite carrier; one fixed proper-minor colouring; actual adhesion `N(X)`. |
| `P3` singleton-shell palette alignment | **GREEN in scope** | Spanning one-complex induced-bipartite bag, five literal singleton clique labels. |
| `P4` singleton-shell exchange | **GREEN in scope** | `d=1` and both `d=2` low-portal outcomes are closed by independently audited literal models/rooted-face arguments. |
| endgame | **GREEN once `P1` holds** | `K_7`, a faithful common colouring state, or one literal global apex pair are all terminal contradictions. |

Thus the present programme has a complete audited **target shell**, but no
audited theorem which earns that shell from the arbitrary near-clique
minor.

## 1. The single red link `P1`

### Green normalization facts

1. An arbitrary `K_7^\vee` model can be made spanning.  Its labelled
   adjacency graph is connected, so its bag union is connected.  Each
   unused component can be absorbed into one incident bag without losing
   connectedness, disjointness, labels or any old model edge.
2. The lexicographically minimal **nonspanning** source theorem in
   `../results/hc7_near_k7_literal_rooting_bridge.md` is label-faithful.
   A detachable part with no monopoly may be deleted.  A uniquely
   monopolized part may be transferred into its owner: an old owner edge
   connects the enlarged owner, and an actual cut edge restores the
   residual source-owner adjacency.
3. The strengthened deficient-first continuation in
   `../results/hc7_near_k7_deficient_path_normalization.md` is GREEN.  In a
   deficient-first lexicographically minimal **nonspanning** model, every
   detachable side monopolizes at least two of the four ordinary labels.
   Applying this to every edge of every spanning tree forces the four
   portal classes to be singletons, every spanning tree of the deficient
   bag to be a path, and hence the bag itself to be an induced path.  Its
   two endpoints carry exactly two portal labels each, with the four
   labels partitioned `2+2`.
4. `../results/hc7_near_k7_coherent_spanning_transport.md` gives a faithful partial
   transport back to a spanning model.  Union the normalized deficient
   bag with every unused component meeting it.  This connected union
   must be anticomplete to one fixed deficient twin, since otherwise it
   and the six foreign bags are a `K_7` model.  All remaining components
   can be absorbed into foreign bags without changing that pair.  Under
   seven-connectivity every added lobe has an actual adhesion of order at
   least seven on the same five-label side.
5. Full exact seven-adhesions with at most five boundary defects are
   GREEN.  Up through four defects explicit two-shore models give
   `K_7`; the two sharp five-defect boundaries are closed for arbitrary
   shore order by a same-shore crossing or compatible planar webs.
   Sources: `../results/hc7_near_k7_exact7_boundary_threshold.md` and
   `../results/hc7_near_k7_exact7_web_closures_audit.md`.

### Why these facts do not prove `P1`

* The deficient bag is now induced bipartite, but its six foreign model
  bags remain arbitrary connected sets.  A palette colour in the total-
  contraction state may occur in several foreign bags, and a foreign bag
  need not be monochromatic.  Full palette exposure therefore does not
  produce literal model-label contacts.
* Colouring a quotient in which foreign bags have been contracted cannot
  be expanded merely by list-colouring the carrier.  The foreign bags may
  need several colours and their internal portal placements matter.
* Coherent transport preserves one fixed missing twin and the old induced
  path as a core, but absorbing all components which meet that core can
  create bypasses, odd cycles and new neutral portal occurrences.  It
  does not produce the induced-bipartite carrier required by `P2/P3`.
* The exact-seven theorem starts only after an actual full two-shore
  adhesion is present, and closes only boundary defect at most five.  It
  neither forces such an adhesion from an arbitrary near model nor
  handles the remaining defect layers.
* Existing rural/annular results are conditional on two **fixed** deleted
  singleton labels and on societies covering the whole remainder in
  compatible rotations.  They do not show that locally obtained rural
  pieces choose the same two original vertices.  This former `P5` issue is
  now correctly incorporated into `P1`: a valid normalization theorem
  must output one global pair, not a family of local pairs.

Accordingly `P1` remains RED against all required falsification gates:
non-bipartite deficient blocks, repeated palette colours, nonsingleton
foreign bags and incompatible local apex choices.

## 2. `P4` is GREEN in the earned shell

The following results and sibling audits close every written residue.

1. **Unique shadow (`d=1`).**
   `../results/hc7_near_k7_rainbow_cycle_completion.md` and its audit:
   deleting the ordinary singleton clique leaves a 3-connected graph.
   The two poles and one saturated vertex lie on one cycle.  Splitting the
   pole arcs gives three literal branch sets, each complete to the
   ordinary singleton clique, and hence `K_7`.
2. **Disconnected witness deletion (`d=2`).**
   `../results/hc7_near_k7_two_defect_cut_closure.md` and its audit:
   every component of `B-{x_s,x_t}` lies behind an actual seven-row cut.
   Two components give seven explicit branch bags, including when they
   miss different ordinary rows.
3. **Captured ordinary portal (`d=2`).**
   `../results/hc7_near_k7_two_defect_rooted_face.md` and its audit:
   the five literal common roots in a 4-connected remainder give a rooted
   `K_4`, hence `K_7`, or lie on one face.  Exact capture makes the
   concentrated singleton's whole remaining neighbourhood cofacial, so
   deleting the other two ordinary singleton labels is one global planar
   pair.

All branch sets in the minor outcomes are connected, disjoint and joined
by literal original edges.  No colour class is treated as connected, and
no contracted quotient vertex is mistaken for an original singleton.

## 3. End-to-end audit

The only missing arrow is now

```text
arbitrary spanning labelled K7^vee model
  -- P1 OPEN -->
spanning singleton / induced-bipartite / two-portal shell
  -- P2+P3+P4 GREEN -->
K7, six-colouring, or one fixed two-apex pair.
```

The Four Colour Theorem is invoked only after a literal pair of original
vertices has been shown to planarize the whole graph.  A contracted
carrier, a pair depending on the local society, or pairwise compatible
rural drawings is not sufficient.
