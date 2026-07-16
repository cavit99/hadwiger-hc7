# Independent audit of the minimum-transversal graph theorem

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `hc7_exchange_core_transversal_graph.md`
- SHA-256: `6ee10c746300c94f1b7c129bf219eb5eb816ab2d250dc615aa28f75694621ae2`

After the mathematical audit, the source was moved from `active/` to
`results/` and only its status metadata was updated to link this audit.
The audited mathematical content is unchanged; the hash above binds the
final promoted revision.

This audit covers Theorem 2.1, Corollary 2.2, and the scope claims in
Section 3.  The result is a set-system and connectivity reduction; it is not
an audit of the still-open model-composition steps named at the end of the
note.

## Checks performed

### 1. Inherited hypotheses and support height

The reference to Theorem 2.1 of `hc7_one_vertex_support_exchange.md`
legitimately imports

\[
 \tau(\mathcal H)=2,
 \qquad \tau(\mathcal F_6(G))>2,
 \qquad \mathcal F_5(G)\subseteq\mathcal H,
\]

as well as a distinguished exact six-vertex support contained in
`Z_H`.  An edge of `B_H` is a two-vertex transversal of `H`; by the
definition of `Z_H` it is disjoint from every subset of `Z_H`.  Hence, for
each exact six-support `A' subseteq Z_H`, such an edge meets all support-five
models and avoids `A'`.  This proves `mu_G(R)=6`.  The contradictory
hypothesis `tau(F_6(G))>2` gives `mu_G(P)<=6` for every pair `P`, so the
global-maximality assertion is correct.

### 2. Classification of the transversal graph

The vertex set of `B_H` is exactly the union of its edges, so it has no
isolated vertices.  If it has no matching of order two, its edge family is
pairwise intersecting.  A nonempty pairwise-intersecting family of distinct
two-sets is either contained in a star or is exactly a triangle.  These two
possibilities are exclusive, and together with the matching case exhaust
all possibilities, including the one-edge case.

In the star case, `tau(H)=2` guarantees a member `E` avoiding the centre
`p`.  Every leaf is then forced into `E`, which gives `|L|<=|E|<=6`; the
same argument applies to every member avoiding `p`.  In the triangle case,
meeting all three transversal edges is equivalent to containing at least
two triangle vertices.  Thus (2.1)--(2.3) follow exactly as stated.

### 3. Connectivity corollary

For a separation of `G-U` with boundary `S` and two nonempty open sides,
`U union S` is a vertex cut of `G`.  Seven-connectivity therefore gives
`|S|>=7-|U|`.  If `|U|=7` and `C` is a component of `G-U`, then omitting
any `u in U` from `N_G(C)` would make the at-most-six-set `N_G(C)` separate
`C` from `u`.  Hence `N_G(C)=U`.  No stronger residual connectivity or
induction claim is made.

### 4. Scope

The fixed graph `B_H` is preserved only while the distinguished support is
replaced inside the same canonical core and `H` is held fixed, exactly as
used in Section 3.  The note correctly leaves both the disjoint-private-pair
composition and the bounded-locus linkage/separation problems open.

## Unresolved assumptions or gaps

None within the stated theorem and corollary.  Their cited input theorem is
separately audited elsewhere; this audit does not re-audit that source.
