# Audit of the simplicial defect-one normalization

**Verdict:** GREEN for the exact source revision identified below.

This is an internal mathematical audit.  It verifies the conditional
normalization proved in the source note; it is not external peer review and
does not promote the conditional branch to a proof of `HC_7`.

## Audited revision

The audited file is
`results/hc7_defect_one_simplicial_normalization.md`.

**Source SHA-256:**
`a6c954234ec2121b0150959f4ce9cff18e78045932a4d331343094db2bf88b05`.

After the mathematical audit, the source status was changed from
"written proof draft; not yet independently audited" to "written proof;
separate internal audit GREEN."  Replacing that one status line by its prior
text reproduces the initially audited SHA-256
`9d17c3e5dbf50811c57bdc0d9657e466980e73498a9881918f2445f82f59d266`
exactly.  No mathematical statement or proof text changed.

## 1. Fixed setup and equality structure

The selected residual components are disjoint from the three path-cut
anchors and from one another within each protected component decomposition.
Their contact graph is therefore the four-partite graph used by the audited
component-contact theorem.

Although the setup does not separately list `K_4`-minor-freeness of `J`, it
follows from the host assumption: a `K_4` model in `J`, together with the
three path-cut anchors, lifts to a `K_7` model in `G`.  Thus the assumptions
that all four parts are nonempty and `Delta(J)=1` satisfy the hypotheses of
the equality theorem, and `J` is a two-tree.  Since `J` has at least four
vertices, it has a simplicial degree-two vertex and also a vertex outside
that vertex and its two neighbours.

The use of seven-connectivity is legitimate.  The displayed hypotheses make
`G` a non-complete seven-contraction-critical graph; the standard Mader
connectivity theorem gives seven-connectivity.  The exclusion of a `K_7`
minor rules out the complete exceptional graph.

## 2. Inclusion-maximal component selection

For an omitted eligible component `W`, the adding-one-component identity is

\[
  \Delta(J+W)=3-\sum_{K'\ne K}t_{K'}.
\]

The augmented selection still represents all four labels and every selected
component remains adjacent to all three anchors.  If its defect were
nonpositive, the component-contact theorem would give a `K_7` model, so the
sum is at most two.  Equality would preserve defect one and strictly enlarge
the selection at the same fixed path and cut, contrary to the stated
inclusion-maximality.  Proposition 2.1 therefore correctly concludes that
the sum is at most one.

This counts bichromatic connected components, not selected quotient vertices
or literal attachment vertices.  Multiple contacts concentrated in one old
bichromatic component remain possible, as the source explicitly records.

## 3. Full-neighbourhood separation

For a simplicial selected component `L`, choose a selected quotient vertex
outside `v` and its two neighbours.  Its represented connected subgraph is
disjoint from and anticomplete to `L`, because contact is exactly adjacency
in `J`.  Consequently it survives outside
`L union N_G(L)`, while `L` is the other open side.  The pair in (3.1) has
union `V(G)`, intersection `N_G(L)`, and no edge between its open sides by
the definition of an open neighbourhood.  Proposition 3.1 and its lower
bounds from seven-connectivity are correct.

## 4. Saturated quotient and attachment cliques

The five sets in (4.1) are disjoint connected branch sets.  The three
anchors are pairwise adjacent, every eligible component meets every anchor,
and the two neighbours of a simplicial vertex in a two-tree are adjacent.
Thus they form a `K_5` model, and adjoining `L` gives the stated `K_6`
model.

Contracting all represented sets gives exactly

\[
                         H=K_3\vee J.
\]

Every nonedge of `H` lies in `J`.  A two-tree is edge-maximal
`K_4`-minor-free, so adding any such edge gives a `K_4` minor in the `J`
part and hence a `K_7` minor after adjoining the three vertices of the
`K_3`.  Since `H` itself is a minor of `G`, it is `K_7`-minor-free.  This
proves the exact edge-maximality assertion in Proposition 4.2.

For a connected subgraph `W` disjoint from the represented sets, contract
`W` to a new quotient vertex.  If it contacts two nonadjacent represented
vertices `a,b`, contracting the edge from its image to `a` retains all of
`H` and adds the edge `ab`; any additional edges are harmless.  This would
give the forbidden `K_7` minor.  Hence the attachment indices form a clique.
Six attachment indices together with the image of `W` would already form a
`K_7` subgraph, so their number is at most five.

For an omitted eligible component, its three anchor contacts leave room for
at most two selected-component contacts.  Two such contacts cannot share a
protected label, because distinct components of the same
`G[K-V(P)]` are anticomplete.  If they have different labels, they contribute
to two different summands in Proposition 2.1.  Both possibilities are
excluded, and the claimed at-most-one selected-component neighbour follows.

The proposition concerns branch-set labels.  It does not make the literal
attachment vertices a clique or bound their multiplicity.

## 5. Simultaneous absorption

Corollary 4.3 fixes the model union `mathcal U` before performing any
absorption.  Components of `G-mathcal U` are pairwise anticomplete.  Every
component absorbed into `L` has an attachment clique containing `v`, so all
its other represented attachments belong to the five-vertex clique
`N_H(v)`.  A component not initially adjacent to `L` cannot become adjacent
through an absorbed component, since two distinct components of
`G-mathcal U` have no edge.  Direct contacts from `L` itself are also exactly
to those five represented neighbours.  This proves

\[
 N_G(L^*)\subseteq C_q\cup U_q\cup\{z\}\cup M\cup N.
\]

A selected quotient vertex outside `v` and its two `J`-neighbours is
nonadjacent both to `L` and to every absorbed component; otherwise it would
be another member of an attachment clique containing `v`.  Its represented
subgraph remains in the far open side.  Thus (4.6) is a genuine separation,
and seven-connectivity gives only the asserted lower bound.

The source correctly warns that the right side of (4.5) consists of five
whole, potentially large branch sets.  It is not a five-vertex separator.
The absorbed set need not retain a protected label, residual-component
status, bipartiteness, or a boundary colouring.

## 6. The `X`-labelled bipartite split

When `L` has label `X`, it is a component of an induced subgraph of the
connected induced bipartite graph `X`, and hence `G[L]` is induced,
connected, and bipartite.  If it has at least two vertices, contracting it
is a proper minor and every such minor has a six-colouring.  The exact
hypotheses of the bilateral full-palette theorem therefore hold for any
chosen spanning tree and any chosen six-colouring of `G/L`.  That theorem
returns nonempty connected adjacent shores, each with external neighbours
in all five colours other than the contraction colour.

If both shores meet every one of the five branch sets in (4.1), those five
sets form a `K_5` model and the deleted tree edge joins the shores, so the
seven displayed sets are an explicit `K_7` model.  Otherwise a missed
branch set `F` is disjoint from and anticomplete to the corresponding shore
`Y`; hence all of `F` lies outside `Y union N_G(Y)`.  The pair (5.2) is a
genuine separation with two open sides, and seven-connectivity gives its
order at least seven.  The singleton case was already covered by
Proposition 3.1.

The palette witnesses are not aligned with the five model labels.  The
result supplies neither an upper bound on the separator order nor compatible
closed-shore colourings.  Applying the bipartite theorem to the original
`L`, rather than the absorbed `L^*`, is essential and is done correctly.

## 7. Dependency check

The source revisions used directly here were checked as follows.

- `results/hc7_component_contact_defect_theorem.md` has SHA-256
  `247de0124f0fadf2000aa2984e77c709fece88d2daf9515fae9cd8ed4e1b44a5`,
  exactly the revision given a GREEN audit.
- `results/hc7_colour_matched_path_all_cut_interval_exchange.md` has
  SHA-256
  `719e034ea81221c4fbddd77ea4cdd661ce1b04b1f84b007a69e73a89de4f2057`,
  exactly the revision given a GREEN audit.
- `results/hc7_colour_matched_path_component_exchange.md` has SHA-256
  `eb024c94213b993bccc3b7c116117831ee898cb8eaf94535e7dd1b7fe622257c`,
  exactly the revision given a GREEN audit.
- `results/hc7_near_k7_bipartite_total_contraction.md` has SHA-256
  `69044ccf85ccd3ec32ca118f11ddb1e673dade7fa7f7ac9d980b6b430ee5e228`,
  exactly the revision given a GREEN re-audit.  Relative to the revision
  initially checked here, only Theorem 3.1 was repaired, by adding the
  explicit condition that each carrier `D_beta` lies in `G-X`.  The
  simplicial normalization invokes only Theorem 2.2, whose statement and
  proof are unchanged.  Its use in Proposition 5.1 remains valid.

All four dependency paths exist.  No result is used to infer more than its
stated scope.

## 8. Trust boundary

The normalization is conditional on an already available four-labelled,
all-eligible, defect-one selection at one fixed path cut.  It does not prove
that every hypothetical counterexample reaches that branch.  It also does
not prove:

1. an order-seven upper bound for any returned separator;
2. compatible boundary equality partitions on the two closed shores;
3. preservation of the path, cut, protected labels, or selection under a
   proper-minor response;
4. a smaller valid defect-one configuration in the original host;
5. that the simplicial component has label `X`; or
6. that the infinite quotient family `K_3\vee J` is incompatible with
   contraction-criticality.

The result is therefore a sound host-level normalization and separator
alternative, not the open exchange-or-gluing theorem and not a proof of
`HC_7`.

## Unresolved assumptions or gaps

None within the exact statements of Propositions 2.1, 3.1, 4.1, 4.2 and
5.1 or Corollary 4.3 at the audited source hash.  The six items in the trust
boundary are programme-level obligations deliberately excluded from the
source theorem.
