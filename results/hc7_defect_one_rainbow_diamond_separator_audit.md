# Audit of the rainbow-diamond separation theorem

**Verdict:** GREEN for the exact source revision identified below.

This is an independent internal mathematical audit.  It verifies the
conditional structural theorem in the source note; it is not external peer
review and does not promote the conditional defect-one branch to a proof of
`HC_7`.

## Audited revision

The audited file is
`results/hc7_defect_one_rainbow_diamond_separator.md`.

**Source SHA-256:**
`2af6cd527cb3ca13cb624a2f0e452c84debf1acbebe2997ce2f826693133b246`.

The line-by-line mathematical audit was performed on source SHA-256
`797fbf8190776a974df670ee3f495c4af624d3edd4c3a10196dc4f3beb545616`.
After that audit, the source status line alone was changed from
"written proof draft awaiting a separate exact-file audit" to "written
proof with a separate internal audit returning GREEN."  Replacing the
current status line by the former text reproduces the initially audited
SHA-256 exactly.  No theorem statement, hypothesis, proof, dependency, or
trust-boundary text changed, so the GREEN verdict applies to the current
source revision above.

The mathematical source was read line by line at the initial audited hash.
In particular, the fixed setup explicitly requires the represented
subgraphs to be pairwise
disjoint and disjoint from all three anchor branch sets.  This condition is
essential for the contractions and the labelled minor-model lifts below.

## 1. Fixed setup and quotient

The three anchor sets are disjoint, connected, and pairwise adjacent.  The
represented subgraphs are disjoint from one another and from the anchors,
and every represented subgraph is adjacent to every anchor.  Contracting
these sets therefore gives exactly the join

\[
                              H=K_3\vee J.
\]

No branch-set disjointness is inferred merely from quotient labels; it is an
explicit hypothesis of the audited revision.

The attachment-clique property is also stated explicitly in the setup.  In
the intended defect-one application it is supplied by Proposition 4.2 of the
audited simplicial-normalization theorem: any connected subgraph disjoint
from all represented sets has a clique of represented attachment indices in
`H`.  Applying it to a component of the complement of the model union is
therefore legitimate.

## 2. Rainbow diamond

The initial triangle in any two-tree construction has three distinct labels,
because adjacent vertices cannot share a protected label.  Since every one
of the four labels occurs, there is a first added vertex `l` carrying the
fourth label.  If `l` is stacked on the edge `mn`, that edge already belongs
to a triangle `mnr` in the partial two-tree immediately before `l` is added:
this is true for every edge of every partial two-tree, including initial and
subsequently created edges.

The triangle `mnr` has three pairwise distinct old labels, and none is the
fourth label by the choice of `l`.  Thus `l,r,m,n` have all four labels.
When `l` is added its only old neighbours are `m,n`, and later construction
steps add no edge between two existing vertices.  Hence `lr` remains absent,
whereas the other five edges are present.  The induced subgraph is exactly
`K_4-lr`, not merely a non-induced diamond.

Because the seven represented sets in Corollary 2.2 are disjoint and
connected, the three anchors meet all four selected component subgraphs, and
the component-contact graph records literal host adjacency exactly, they
form the stated label-faithful `K_7^-` minor model.  The sole missing model
adjacency is between `V_l` and `V_r`.

## 3. Separation by the shared edge

If `J-{m,n}` contained an `l-r` path, contracting that path down to an
`l-r` edge while leaving `m,n` untouched would complete the five diamond
edges to a `K_4` minor.  A two-tree is `K_4`-minor-free.  Thus `l` and `r`
lie in different components of `J-{m,n}`.

For the component `C` containing `l`, the lifted union

\[
                         X_0=\bigcup_{x\in V(C)}V_x
\]

is connected: every quotient edge on a path in `C` is a literal edge between
the corresponding connected host subgraphs.  There is no quotient edge from
`C` to a vertex of `J-(C\cup\{m,n\})` by the definition of a component after
deleting `m,n`.

## 4. Attachment-clique localization

Let `W` be a component of the complement of the complete model union which
touches `X_0`.  At least one represented attachment index of `W` lies in
`C`.  If another represented `J`-attachment lay outside
`C\cup\{m,n\}`, the two attachment indices would be nonadjacent in `H`,
contrary to the attachment-clique hypothesis.  The only remaining represented
attachments are therefore:

- vertices of `C`, whose subgraphs already lie in `X_0`;
- `m` and `n`; and
- the three vertices of the joined `K_3`, represented by the anchors.

This proves the claimed five-branch-set support for the boundary after
absorption.  It is a containment in five whole named branch sets, not a
five-vertex bound.

## 5. Simultaneous absorption and the far shore

The source fixes the model union before absorption and absorbs every
component of its complement touching `X_0`.  Every absorbed component is
connected and has an edge to `X_0`, so their union with `X_0` is connected.
Distinct components of the complement of the fixed model union are
anticomplete.  Consequently an omitted outside component cannot acquire a
new edge to the absorbed union through another outside component.  The
localization in Section 4 therefore proves

\[
 N_G(X)\subseteq A_1\cup A_2\cup A_3\cup V_m\cup V_n.
\]

The vertex `r` lies outside `C\cup\{m,n\}`.  Its represented subgraph is
disjoint from the five boundary-supporting branch sets and anticomplete to
`X_0`.  It is also anticomplete to every absorbed component: otherwise that
component's attachment clique would contain `r` and an attachment index in
`C`, which are nonadjacent in `J`.  Hence

\[
                   V_r\subseteq V(G)-(X\cup N_G(X)).
\]

Thus both open sides of the displayed separation are nonempty.  Its two
vertex sets cover `V(G)`, their intersection is exactly the external
neighbourhood `N_G(X)`, and by definition no edge joins the two open sides.
Seven-connectivity therefore gives only the asserted lower bound
`|N_G(X)|>=7`.

## 6. Dependency check

The source revisions used directly by this theorem were checked as follows.

- `results/hc7_defect_one_simplicial_normalization.md` has SHA-256
  `a6c954234ec2121b0150959f4ce9cff18e78045932a4d331343094db2bf88b05`,
  exactly the revision with a GREEN adjacent audit.  Proposition 4.2 is the
  attachment-clique input used here.
- `results/hc7_component_contact_defect_theorem.md` has SHA-256
  `247de0124f0fadf2000aa2984e77c709fece88d2daf9515fae9cd8ed4e1b44a5`,
  exactly the revision with a GREEN adjacent audit.  Its equality theorem is
  the source of the two-tree structure in the defect-one application.

The abstract theorem in the audited source assumes the two-tree and
attachment-clique conclusions directly, so it does not circularly use the
rainbow-diamond conclusion to obtain either dependency.

## 7. Trust boundary

The theorem proves a reusable structural consequence of a proper
four-labelled two-tree with the stated host realization.  It does not prove:

1. that every adjacent-pair configuration reaches the conditional
   defect-one setup;
2. an upper bound of seven on the returned separator;
3. compatible six-colour boundary partitions on the two closed shores;
4. preservation of the protected labels, path, cut, or selected components
   under a proper-minor colouring;
5. a host-measured strict descent; or
6. a `K_7` minor from the displayed `K_7^-` model.

These are excluded expressly by the source note.  In particular, the result
compresses an unbounded two-tree to a five-branch-set-supported actual
separation, but does not close the exchange-or-gluing theorem or prove
`HC_7`.

## Unresolved assumptions or gaps

None within Lemma 2.1, Corollary 2.2, Lemma 3.1, or Theorem 3.2 at the
audited source hash.  The six programme-level obligations in the trust
boundary are deliberately outside the theorem's conclusion.
