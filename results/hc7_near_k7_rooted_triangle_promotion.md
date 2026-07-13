# Rooted row promotion through connected carriers

## Status

This is a label-preserving carrier exchange for the path-cut capacity
state.  It removes all one-row portal geometry: one portal, a cutvertex
arm and a two-connected support are identical for this operation.  The
construction is uniform in the clique-model order.

## Theorem 1 (uniform clique-root row promotion)

Let

\[
 R_1,\ldots,R_p,F_1,\ldots,F_s
\]

be pairwise disjoint connected sets.  Assume that the `R_j` are pairwise
adjacent and that the `F_i` are pairwise adjacent.  Let
`K_1,...,K_s` be pairwise disjoint connected sets, disjoint from all
these roots, such that `K_i` has an edge to `F_i` and to every `R_j`.

Then the graph contains a `K_{p+s}` model rooted at the displayed sets.
Explicitly, keep every `R_j` unchanged and replace

\[
                         F_i\longmapsto F_i'=F_i\cup K_i.
\]

### Proof

Each `F_i'` is connected because `F_i` and `K_i` are connected and
adjacent.  The displayed branch sets are pairwise disjoint.  Old edges
give every `R_jR_k` and every `F_i'F_h'` adjacency, while an edge from
`K_i` to `R_j` gives `F_i'R_j`.  Hence all `p+s` branch sets are
pairwise adjacent.  \(\square\)

The operation is protected outside the selected carriers: all old
vertices and adjacencies of the rooted sets survive, and no vertex of a
different carrier is used.

## Corollary 2 (one-carrier rooted triangle)

Let `X,Y,Z,K` be pairwise disjoint connected sets.  If `X,Y` are
adjacent and `K` has an edge to each of `X,Y,Z`, then

\[
                         X,\quad Y,\quad Z\cup K
\]

are three pairwise disjoint connected pairwise adjacent branch sets.

This is Theorem 1 with `p=2,s=1`.  In particular, neither portal
multiplicity nor internal connectivity beyond connectedness of `K` is
needed.

## Corollary 3 (one-portal row duplication at a path cut)

Use the path-cut notation `L|R` and a connected crossing old exterior
piece `K` from
`../results/hc7_near_k7_literal_shore_completion.md`.  Let `Q` be a
foreign row with at least one edge to `K`.  Replacing `Q` by `Q union K`
makes the row adjacent to both `L` and `R`; the two path sides remain
connected, disjoint and adjacent.

Consequently, if all other row requirements of the two shores are
already supplied by mutually disjoint helper families outside `K`, with
every helper piece attached to its assigned path side, adjoining those families
preserves connectedness and every literal contact.  Both shores may use
the enlarged row in the literal shore-completion model.  A single portal
in an arbitrarily cut-up carrier is enough.

## Corollary 4 (Hall promotion certificate)

In the root setting of Theorem 1, let `mathcal K` be a family of pairwise
disjoint connected pieces, disjoint from all `R_j,F_i`, every member of
which has an edge to each of the pairwise adjacent roots
`R_1,...,R_p`.  Form the bipartite incidence graph between the pairwise
adjacent foreign rows `{F_1,...,F_s}` and `mathcal K`, putting `F_iK` in the incidence graph
exactly when `K` has an edge to `F_i`.

If this incidence graph has a matching saturating the foreign rows,
then the host contains a `K_{p+s}` minor.  If it has no such matching,
Hall's theorem gives a nonempty set `S` of foreign rows with

\[
                  |N_{\mathcal K}(S)|<|S|.               \tag{4.1}
\]

### Proof

Use the matched carrier for each row in Theorem 1.  The alternative is
exactly Hall's marriage theorem.  \(\square\)

For the one-missing `HC_7` path state, take `p=2,s=5` with roots the two
path sides and rows the five retained foreign bags.  Thus a target-free
carrier has a Hall-deficient set of literal foreign rows whose entire
crossing support lies in fewer pieces than rows.  This counts pieces,
not vertices, and is not by itself an ambient separator.

### Corollary 5 (minimal deficiency is one two-row duty)

Let `S` be an inclusion-minimal nonempty Hall-deficient set of rows.  If
`|S|>=2`, then

\[
                       |N(S)|=|S|-1.                    \tag{4.2}
\]

For every chosen row `Q in S`, the rows `S-{Q}` can be matched
bijectively to `N(S)`.  Choose any `K in N(Q)`.  In such a bijective
matching some edge `HK` uses that same carrier.  Thus all rows of `S`
other than the unmatched `Q` have distinct assigned carriers; relative
to this assignment, `K` is assigned to `H` and also supports `Q`.  This
is a two-row assignment collision.  It does not assert that `K` has
degree two in the incidence graph or that either row has unique support.

If `|S|=1`, its sole row has no crossing carrier at the selected cut.

### Proof

Every proper subset `T` of `S` satisfies `|N(T)|>=|T|` by minimality.
For `Q in S`, Hall's theorem therefore matches `S-{Q}` into `N(S)`.
It follows that `|N(S)|>=|S|-1`; deficiency gives equality.  The matching
is consequently a bijection onto `N(S)`.  When `|S|>=2`, the proper
singleton `{Q}` is not deficient, so choose `K in N(Q)`.  The bijection
matches every such chosen `K` to some `H in S-{Q}`, proving the claim.  The singleton case
is immediate.  \(\square\)

## Exact limitation: multi-duty carriers

A selected carrier can be absorbed into only one foreign row.  If one
carrier is simultaneously the unique left helper for a row `H` and the
only right helper for a distinct row `Q`, promoting it into either row
can destroy the other literal duty.  The path whose terminal order is

\[
        L\text{-attachment},\ Q\text{-portal},\
        R\text{-attachment},\ H\text{-portal}
\]

is the sharp four-terminal obstruction.  It has no disjoint paths
joining the left side to `H` and the right side to `Q`.

Thus the exact next principle is a fixed two-path linkage or coherent
web alternative for a Hall-deficient multi-duty carrier.  One-row portal
multiplicity and block-cut peeling are no longer part of the gap.
