# Independent audit: leaf blocks outside a fixed six-path linkage

**Verdict:** GREEN for the exact theorem revision identified below.

**Audited source:**
`results/hc7_linkage_bridge_leaf_block_separation.md`

**SHA-256:**
`2e953a0924f4e3cff0966cb3f6d48c073bdbd6681b3e0839cb71b31fa1b60205`

The first audit pass found that pairwise distinctness of the twelve path
ends was used but not assumed.  The audited revision makes that condition
an explicit standing hypothesis.  This audit checks the corrected
revision, not the earlier one.

After the substantive audit, only the source status line and repository
location were changed for promotion from `active/` to `results/`; the hash
above is the promoted revision.

## 1. Setup and block structure

The six paths are pairwise vertex-disjoint and their twelve ends are
pairwise distinct.  Hence every vertex of a component `C` of
`G-V(Sigma)` is outside every named path.

If `B` is a leaf block of a component whose block--cutvertex tree has more
than one block, it contains exactly one cutvertex `c` of `C`.  The set
`L=V(B)-{c}` is nonempty and connected, including when `B` is a bridge
block of order two.  An edge from `L` to `C-V(B)` would put a vertex of
`L` in a second block, making it a second cutvertex of `B`; therefore

\[
                         N_C(L)\subseteq\{c\}.
\]

Because `C` is a component outside the six-path linkage, every other
neighbour of `L` lies on that linkage.  Thus

\[
             N_G(L)\subseteq \{c\}\cup N_\Sigma(L).
\]

This verifies the block--cutvertex claim and the asserted neighbourhood
containment.

## 2. Connectivity count

If `|N_Sigma(L)|<=5`, deleting
`{c} union N_Sigma(L)` removes at most six vertices.  It leaves the
nonempty set `L`.  Since `c` is outside the linkage and the deleted
linkage part has at most five vertices, at least one of the twelve
distinct path ends also remains.  The neighbourhood containment above
precludes a path from `L` to that remaining end.  This contradicts
seven-connectivity.  Hence `|N_Sigma(L)|>=6`.

The endpoint count is conservative and valid: all twelve ends are
distinct vertices of `Sigma`, while `c` is not a vertex of `Sigma`.

## 3. Equality and preservation of labels

When `|N_Sigma(L)|=6`, the set

\[
                         X=\{c\}\cup N_\Sigma(L)
\]

has exactly seven vertices: `c` lies outside `Sigma`.  There is no edge
from `L` to `V(G)-(L union X)`.  Therefore the vertex sets
`L union X` and `V(G)-L` form an order-seven separation with boundary
exactly `X`.  The first open shore `L` is nonempty.  The second is
nonempty because at most six of the twelve distinct path ends lie in
`X`.

Moreover `L` is disjoint from `Sigma`.  Every path `P_i`, with all of its
vertices and its original label, lies in the closed opposite shore.  No
contraction, truncation, or relabelling is hidden in the construction.

## 4. One-block corollary

If `C` has no cutvertex, then its entire external neighbourhood is
`N_Sigma(C)`.  A set of at most six such neighbours would separate the
nonempty component `C` from at least one of the twelve distinct path ends,
contradicting seven-connectivity.  Thus `|N_Sigma(C)|>=7`.  At equality,
the same vertex-set construction gives an order-seven separation; at
most seven of the twelve ends lie on its boundary, so its opposite open
shore is nonempty and contains all six named paths in its closure.

The corollary really needs the explicit size/distinct-end hypothesis.  For
example, without it, six singleton paths in `K_8` leave a cutvertex-free
`K_2` component with only six linkage neighbours.  The corrected source
excludes that example.

## 5. Exact scope

The audited result is solely a seven-connectivity consequence for a fixed
six-path linkage with twelve distinct ends.  It proves:

- every leaf-block interior of an off-linkage component has at least six
  neighbours on the linkage;
- equality yields an actual order-seven separation preserving all six
  named paths; and
- a cutvertex-free off-linkage component has at least seven linkage
  neighbours, with the analogous separation at equality.

It does **not** settle the case of more than six linkage neighbours on a
leaf-block interior, impose any order on those attachments, construct a
`K_7` minor, or prove `HC_7`.
