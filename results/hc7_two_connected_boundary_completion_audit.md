# Audit of the two-connected-core completion theorem

**Verdict:** **GREEN.**

**Audited source:** theorem content before status-only promotion

**SHA-256:**
`f6a8974d10e940212e479f5e602b5103e522c4b36d7766d212f2f9352d7088fd`

Promotion changed only the status line.  The promoted source hash is
`8b12881cebb2df2bc17917367173aa047a64f990530da695a73e7fed68c31a2d`
for `results/hc7_two_connected_boundary_completion.md`.

This audit checked Theorem 1 and its stated consequence line by line.

## Checks

1. Removing `p,q` from a seven-connected graph leaves the graph `H`
   five-connected.  For either shore, deletion of at most two vertices
   cannot isolate an `A`-only or `B`-only component from the opposite
   shore.  The two-connectivity of `G[X]` then joins all remaining
   components.  Thus both `F_A` and `F_B` are three-connected.
2. If one closed side of an order-three separation of `F_A` contained all
   of `X`, the opposite open side would lie in `A` and have its entire
   neighbourhood in the three-vertex separator.  This contradicts the
   five-connectivity of `H`; the argument for `F_B` is symmetric.  Hence
   `X` is spread out in exactly the sense required by Martinsson--Steiner,
   Lemma 3.1.
3. An `X`-rooted `K_4` model in either shore lifts to the displayed
   `K_7` model: the opposite connected shore and the singletons `p,q`
   are disjoint connected branch sets, and fullness, universality to
   `X`, and the edge `pq` supply every required adjacency.
4. In the no-rooted-model case, Martinsson--Steiner applies to both
   shores.  Deleting each added apex makes `X` cofacial.  The standard
   uniqueness of the Hamiltonian boundary cycle in a two-connected
   outerplanar graph identifies the same cycle `C` on both sides.
   Connectedness and fullness place each open shore in the disc opposite
   its apex.  The revised proof also correctly accounts for every chord
   of `C`: wheel spokes exclude such a chord from the apex-side triangular
   faces.  Reflecting one disc, identifying `C`, and erasing only duplicate
   chord drawings therefore gives a planar embedding of `G-{p,q}`.
5. This contradicts the assumed `K_5` minor.  The `HC_5` consequence is
   also valid because deleting two vertices from a seven-chromatic graph
   leaves chromatic number at least five.

## Scope caveat

The theorem closes only interfaces having an adjacent pair `p,q` that is
complete to a two-connected boundary core `X`, with two connected open
shores full to the entire boundary and with a `K_5` minor after deleting
`p,q`.  It does **not** synchronize arbitrary four-colour boundary
extension relations, cover a nonadjacent universal pair, or prove
`HC_7`.
