# Audit of the four-component centre-deletion closure

**Audited file:** `hc7_order8_four_centre_components_closure.md`
**Mathematical revision SHA-256:**
`fa5cbf12c8bd6fa382175e261ebc7911db91abce41b6fb2edd40eedbef723961`
**Promoted revision SHA-256:**
`ab00e80d7a36d10b18ce16c343f2289a2b92281ca49917ea4b04bea5514f0eb8`
**Audit date:** 2026-07-20
**Verdict:** **GREEN.**  The relative Menger split, connected bipartition,
representative allocations, both explicit `K_7` models and the
three-component corollary are correct at the audited revision.

The promoted revision differs only in its status line and link to this
audit.

## 1. Repeated-neighbour case

If the two-path packing from `{a,b}` to `Y` fails, set-Menger gives a
separator of order at most one.  A surviving source component `R` then
satisfies

\[
 N_G(R)\subseteq\{v\}\cup M\cup\{p_0\}\cup Z,
 \qquad |N_G(R)|\le1+3+1+1=6.
\]

The opposite component is a far side, contradicting seven-connectivity.
The successful paths, truncated at their first boundary hits, leave two
disjoint connected source pieces.  Contracting them in a spanning tree and
cutting the tree path between them proves the connected-bipartition lemma.

For the last three components, at most four of the five available
representatives are forbidden at any greedy step: previous choices, one
current missed vertex and at most one reciprocal missed vertex.  Direct
enumeration of all one-defect patterns corroborated the written argument.
Every pair among the seven displayed bags has the edge specified in the
proof; no boundary--boundary edge is used implicitly.

## 2. Unique-neighbour case

The four unique centre neighbours lie in distinct components of `C-v` and
are independent.  Dirac's contraction-critical inequality

\[
                \alpha(G[N(v)])\le d(v)-5
\]

and `d(v)=|N(v) intersect S|+4` force at least five boundary neighbours.
At most four boundary vertices are missed collectively, so one boundary
neighbour `q` meets every component and another `p_0` remains.  The final
representative choice forbids at most five of six available vertices.
The displayed seven sets are disjoint, connected and pairwise adjacent.

## 3. Corollary and trust boundary

The corollary states all host hypotheses explicitly.  The centre decoder
closes five or more components or exposes `|N_G(A)|=7`; absent that output,
four components satisfy the theorem and give `K_7`.  Therefore at most
three components remain after deleting the centre.

The argument does not close one, two or three components and does not make
an order-seven response colour-compatible across both shores.  Removing
seven-connectivity breaks the Menger cut; removing contraction-criticality
breaks the unique-neighbour case.  The theorem does not prove `HC_7`.
