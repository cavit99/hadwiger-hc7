# Audit of the paired all-tight odd-cycle closure

**Audited file:** `hc7_order8_all_tight_odd_cycle_closure.md`
**Mathematical revision SHA-256:**
`63907c2beaf52450d92280d2e8bce623eaa9f574772a3b04e52e814498717504`
**Archived revision SHA-256:**
`4ddc5d0cc0ae5cb450e2ef0ffa8b9bb8d0048366617ae2f4c5d97c7d92b6132b`
**Audit date:** 2026-07-20
**Verdict:** **GREEN as a conditional theorem.**  The constant-list
argument, lexicographic singleton exclusion, density calculation, equality
case and explicit `K_7` model are correct.  The two-connected extension
correctly leaves only the bounded `K_5,K_5` and `K_4,K_4` cases, and the
final density argument returns both bounded cases to a strict degree-seven
singleton response.

The archived revision differs from the audited mathematical revision only
in its status paragraph and supersession link.

## 1. Constant lists

Tightness on an odd cycle gives two-element lists.  If two consecutive
lists differ, orient the cycle across such an edge, choose at the first
vertex a colour absent from the last list, and colour greedily around the
cycle.  The closing edge is automatically proper.  Thus a non-colourable
assignment has one common two-element list.

Its complement is the four-colour set seen from every shore vertex.
Fullness of each component makes this exactly the set of colours used on
the boundary: every boundary colour is seen somewhere, and every seen
colour occurs there.  This verifies Lemma 2.1 for both shores.

## 2. Lexicographic and density reduction

A shore vertex of degree seven has a nontrivial singleton-side
order-seven boundary, with the opposite shore outside its closed
neighbourhood.  A shore vertex of degree eight would make its singleton an
eligible pair `(8,1)`, contradicting the selected `(8,|R|)` with
`|R|>=3`.  Hence, outside the degree-seven outcome, every shore vertex has
degree at least nine and at least seven boundary neighbours.

Writing `s=|A|+|D|`, `e_cross` for the shore--boundary edges and
`h=|E(G[S])|`, the strict host bound gives

\[
 e_{\rm cross}\ge7s,
 \qquad s+e_{\rm cross}+h\le5s+24,
 \qquad 3s+h\le24.
\]

Thus `s<=8`; two odd cycle orders leave `(3,3)` and `(3,5)`.  For `(3,3)`,
the boundary degree sum gives `e_cross+2h>=56`, while the edge bound gives
`e_cross+h<=48` and `e_cross>=42`.  These force both `h>=8` and `h<=6`.

For `(3,5)`, equality forces `h=0`, `e_cross=56`, and degree seven on both
sides of the eight-by-eight shore--boundary bipartite graph.  Its
complement is therefore a perfect matching.

## 3. Explicit equality-case model

The seven displayed branch sets are pairwise disjoint and use all sixteen
vertices.  The nonsingleton sets are connected by the triangle/five-cycle
edges and cross edges avoiding the unique forbidden matching pair.  The
witness table supplies all twenty-one pairwise adjacencies; every cross
witness avoids its sole nonedge and the remaining witnesses are cycle
edges.  An independent direct encoding confirmed disjointness,
connectivity and every displayed adjacency, but the written table is
already a complete human-checkable certificate.

## 4. Two-connected all-tight extension

The Borodin--Erdos--Rubin--Taylor characterization makes each
two-connected all-tight kernel a clique or an odd cycle.  An odd-cycle
shore forces four boundary colours; the other shore is then either another
odd cycle or `K_3`, which is itself an odd cycle, so the main theorem
applies.

For a clique `K_r`, the uncolourable `(r-1)`-list assignment has one common
list by Hall's theorem: a deficient proper subfamily is impossible, while
deficiency of all `r` lists forces their union, and hence every list, to
have order `r-1`.  Fullness gives `r=7-b`, where `b` is the number of
boundary colours.  The cases `b=4` and `b=1` are respectively the triangle
case and an immediate `K_7` model consisting of six singleton vertices in
one `K_6` shore plus the connected other shore together with the boundary.
Only `K_5,K_5` and `K_4,K_4` remain.

## 5. Trust boundary

This is an unbounded conditional closure: the odd cycles initially have
arbitrary order.  It assumes rather than proves a minimum boundary of order
eight, two full components, a common boundary colouring rejected by both,
and spanning vertex-minimal all-tight two-connected kernels.  It neither
forces every minimum order-eight response into those hypotheses nor closes
the two bounded clique-pair contact allocations.  A degree-seven output is
a fresh exact-seven response, not already a global six-colouring.  The
result does not prove `HC_7`.

## 6. Bounded clique-pair density

For the `K_5,K_5` and `K_4,K_4` residues, the host has respectively
eighteen or sixteen vertices.  A degree-eight singleton would beat the
selected `(8,4)` or `(8,5)` pair.  Absent a degree-seven vertex,
seven-connectivity therefore gives minimum degree at least nine.  The
handshake inequality and the strict Mader bound imply `n>=32`, a
contradiction.  Hence a degree-seven vertex supplies the strict
singleton-side exact-seven response claimed in the archived Theorem 5.3.
