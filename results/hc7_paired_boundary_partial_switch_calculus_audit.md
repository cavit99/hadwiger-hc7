# Audit of partial Kempe switches at a paired exact-seven boundary

**Verdict:** GREEN.  The common-equality setup, the two-subgraph obstruction
law, every switch formula and demand calculation, the `x`--`y` lock, the
absent-colour analysis, and the abstract parity example are correct.

**Audited source:**
[`hc7_paired_boundary_partial_switch_calculus.md`](hc7_paired_boundary_partial_switch_calculus.md)

**Source SHA-256:**
`bdbb02aa94b413a2ed68fd448f29385669a89f2cd4e1bde49da31aec592085b4`

The only change from the audited `a41befdb...` revision is the source's
status line and link to this audit; no mathematical content changed.

This is a separate internal mathematical audit, not external peer review.

## 1. Exact-seven setup and obstruction law

The separation is literal, both open shores are nonempty by
seven-connectivity, and the two connected subgraphs in `A` are disjoint and
adjacent to every boundary vertex.  If a proper boundary partition `Omega`
extends through `A` and has `d_H(Omega)<=2`, the two boundary-full subgraphs
support every nonsingleton/nonclique block required by exact packet
reflection.  Since `G` is `K_7`-minor-free, the exceptional seven-block
minor outcome cannot occur.  Reflection gives a colouring of the opposite
closed shore with exactly `Omega`; alignment on the boundary then
six-colours `G`.  This contradicts the hypotheses, so (1.5) is valid.

For the displayed partition `Pi`, the number of blocks is `|K|+3`, while
the clique `K` lies among its singleton blocks.  Hence

\[
 d_H(\Pi)=|K|+3-\omega(H[Q])\le3.
\]

The obstruction law makes this integer greater than two, proving both
`d_H(Pi)=3` and `omega(H[Q])=|K|`.

The repaired common-equality hypotheses are sufficient for every later
selected move.  A selected endpoint-component switch gives a proper
one-edge response, and its restriction to `G[A union S]` is therefore a
proper colouring whose boundary partition obeys (1.5).  For disjoint
`e,f`, the fixed-trace exposure theorem supplies such a partition-changing
move for every unlocked alternate colour.  The source restricts its lock
conclusions to that disjoint-edge case; it does not make the same inference
for arbitrary incident edges.

## 2. General switch formula

Switching one full two-colour component exchanges precisely its boundary
footprints `B_0,C_0`.  The vertices retaining the first colour are
`(B-B_0) union C_0`, and those retaining the second are
`(C-C_0) union B_0`, with empty classes discarded.  Properness of the
switched colouring makes both new classes independent.

An edge of `H[B union C]` from the footprint to its complement would join
the corresponding boundary vertices in the full bichromatic graph, contrary
to the definition of one component.  Conversely every component switch has
exactly this footprint form.  The equality partition changes exactly when
the resulting unordered pair of nonempty classes differs from the original
pair.

## 3. Singleton pairs and the exceptional `x`--`y` nonedge

If singleton vertices `u,v` are adjacent, their boundary vertices lie in the
same full bichromatic component.  A switch therefore meets neither or both;
neither footprint changes the equality partition.  No selected response can
use this palette.  For disjoint selected edges, unlockedness would provide
such a selected move, so the relevant edge is locked.

If `uv` is absent, the only partition-changing footprint contains exactly
one of `u,v`, and the switch merges the two singleton blocks.  In the
`(2,3)` case this gives five blocks and singleton set
`Q-{u,v}`; (1.5) is equivalent to the clique number of that three-set being
at most two.  In the `(3,2)` case it gives four blocks and two remaining
singleton vertices; (1.5) is equivalent to their being nonadjacent.

For `{u,v}={x,y}`, the complementary singleton set is respectively the
triangle or edge `K`.  It violates the corresponding condition, so no
selected `x`--`y` move exists.  The source correctly concludes an
`x`--`y` lock only for vertex-disjoint critical edges, where every unlocked
palette produces a selected move.

## 4. Singleton--`M` switches

For a switch between singleton `{u}` and `M`, the class not containing `u`
is a uniquely determined proper subset `W` of `M`; `W=M` would merely
reproduce the original two blocks.  The other class is
`(M-W) union {u}`.  Both are independent because they are colour classes
after the switch.

The three demand formulas follow from exact block and singleton counts:

* `W=emptyset`: two old blocks merge, giving `|Pi|-1` blocks and deleting
  `u` from the singleton set;
* `|W|=1`: the block count is unchanged, `u` ceases to be a singleton and
  the member of `W` becomes one; and
* `2<=|W|<|M|`: possible only for `|M|=3`, both new blocks are
  nonsingletons, and only `u` leaves the singleton set.

Every selected response must have the displayed demand greater than two.
For the full merge with `x` or `y`, identity (1.6) makes the remaining
singleton clique number exactly `3` in the `(2,3)` form and exactly `2` in
the `(3,2)` form.  Both demands equal two, so both merges are excluded.

## 5. The absent colour

In the `(3,2)` form exactly five boundary blocks use five of the six palette
colours.  A switch between the absent colour and a singleton can only move
that whole singleton to a new colour name, leaving the equality partition
unchanged.  Thus no selected move exists, and the lock conclusion is again
correctly limited to disjoint critical edges.

Switching the absent colour with the colour of the three-vertex block `M`
changes the partition only by a nontrivial `1+2` split.  It creates six
blocks with singleton set `Q union {m}`.  Since `omega(H[Q])=2`, adjoining
one vertex raises the clique number by at most one, so the new demand is at
least three.  The two-subgraph test alone therefore cannot exclude this
response.

## 6. Boundary-level parity example

The graph in Section 6 has exactly the independent-block-compatible edges
`k_1k_2` and `xm_1`.  Its displayed partition has five blocks and singleton
clique number two, hence demand three.  The vertices
`k_1,k_2,x,m_1` induce `2K_2`, so the graph is nonsplit.

For each listed cross-pair, both it and the complementary pair in
`{x,y,k_1,k_2}` are nonedges.  Each merge therefore passes the exact
singleton criterion, has four blocks, two nonadjacent singleton vertices,
and demand three.

The graph is nonempty, nonsplit, and two-colourable, so the hypotheses of
the split-boundary synchronization theorem with `r=6` hold.  Its even- and
odd-block languages are disjoint and each meets every exact-block cylinder.
The five-block original partition and four-block merges fall into opposite
parity classes.  The source correctly labels this as abstract boundary
sharpness only; it does not assert realization by two shores of a
seven-connected contraction-critical host.

## 7. Trust boundary

The note classifies the equality partitions and demand values of selected
two-colour switches.  It does not infer any of the following:

* a palette colour identifies a minor-model branch set;
* every demand-three partition is actually attained;
* the abstract parity languages are host-realizable; or
* one of the surviving footprints constructs a `K_7` minor or synchronizes
  the two shores.

The final statement that surviving footprints require literal host-path and
first-hit information is therefore within the proved scope.

## Final audit conclusion

The repaired setup supplies exactly the proper one-sided response needed by
the obstruction law, and every subsequent formula follows from literal
boundary footprints and exact block counts.  No unresolved mathematical
assumption remains.  The source is GREEN at the pinned hash above.
