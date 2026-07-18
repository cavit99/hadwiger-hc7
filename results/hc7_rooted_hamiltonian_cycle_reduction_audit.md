# Audit: Hamiltonian-cycle reduction for the four-root degree-eight disk

**Audited source:** `results/hc7_rooted_hamiltonian_cycle_reduction.md`

**Audited SHA-256:** `8c3f9eb12e4e04716a590d9a98eb4b7716cffbd9874eee6a149fa4c19bfe7c32`
**Verdict:** **GREEN** — the written proof is valid for its stated
hypotheses and conclusion.

## Checks

1. **Four-connected augmentation.** Adding the new outer-face vertex `r`
   preserves planarity. A cut of order at most three containing `r`
   contradicts three-connectivity of `H`; a cut omitting `r` produces a
   nonempty component disjoint from `U` and hence a separation of `H` of
   order at most three whose opposite closed side contains all four roots,
   contradicting rooted internal four-connectivity.
2. **Published Hamiltonicity input.** Thomas--Yu, *Journal of Combinatorial
   Theory, Series B* **62** (1994), statement (3.4), says that deleting at
   most two vertices from a four-connected planar graph leaves a
   Hamiltonian graph. Applying it to `J-{r,v}=H-v` is exact. Their statement
   (3.3) permits one prescribed edge on either chosen exposed facial circuit
   after relabelling the two deleted vertices; no simultaneous two-edge
   prescription is used.
3. **Cyclic interval allocation.** The repaired hypothesis requires a joint
   injective assignment of all four roots, including roots already in `C`.
   Cutting each open `C`-interval between the left- and right-assigned root
   blocks yields five pairwise disjoint connected path sets with cyclic
   adjacency and four distinct root-containing sets.
4. **Exceptional orders.** When `U` and `C` are disjoint, Hall failure is
   exhausted by three roots in one interval, or by two roots in each of two
   adjacent intervals. After excluding the first pattern, any feasible
   matching can be made monotone within each interval.
5. **Omitted low-separator case.** If neither open side of an
   order-at-most-two separation of `H` meets `L`, then `L` lies in the
   separator. The original anticomplete decomposition with boundary `T` is
   already a nontrivial order-seven separation.

## Trust boundary

The result does not solve either remaining root-clustering pattern,
synchronize shore colourings, or construct a `K_7` minor. It does not use
the failed orthogonal-fan lemma. These are stated limitations, not gaps in
the proved reduction.
