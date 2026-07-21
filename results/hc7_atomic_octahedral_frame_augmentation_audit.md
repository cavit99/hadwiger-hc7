# Independent audit of atomic octahedral-frame augmentation

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- theorem:
  [`hc7_atomic_octahedral_frame_augmentation.md`](hc7_atomic_octahedral_frame_augmentation.md)
- exact SHA-256:
  `a1b9992af5e7c18396583be0e183a71b62c3ff59cce5c5237b89ff7c640ae9b5`

## Verdict

GREEN.  Every stated minor model, route allocation, connectivity
reduction, and extremal calculation is correct under its displayed
hypotheses.  The note does not silently assume the unresolved
ownership-preserving augmentation theorem.

## Checks performed

1. The eight-vertex graph
   `J=K_8-\{xe,ab,cd\}=K_2\vee K_{2,2,2}` has clique number five and no
   `K_7` minor.  Each of the three displayed one-edge augmentations gives
   seven disjoint, connected, pairwise adjacent branch sets.
2. The atomic common-frame partition has exactly the three absent bag
   adjacencies stated in (2.2), with `D'_e=\{v_e\}`.  Thus any one
   ownership-preserving augmentation closes the model.
3. In Lemma 3.1, the clean `a`--`b` path repairs `ab`, while the branch set
   containing `c,x` and the internal vertices of `T_{xd}` repairs `cd`.
   Assigning every other route interior to one of its ends preserves
   disjointness, connectedness, and every remaining clique adjacency.
4. The sets `P_e,P_f,P_g` are disjoint and connected, pairwise adjacent,
   and each adjacent to all four literal roots.  Fabila-Monroy and Wood,
   Theorem 6, therefore lifts a rooted `K_4` minor in `L` to the displayed
   `K_7` model, leaving only the planar cofacial alternative.
5. In Corollary 3.3, a separator of order at most three in `L`—including
   the empty separator when `L` is disconnected—combined with eight
   internally disjoint paths in `G` leaves at least five avoiding the
   separator.  Taking the last `U` vertex and first `W` vertex on each
   path puts every internal vertex in `P_e\cup P_f\cup P_g`.
6. Both complete-substitution constructions are valid.  In the universal
   bag case the quotient sets in (4.1) form a `K_4` model; in an
   octahedral bag the sets in (4.2) form a `K_3` model.  Splitting an
   internal bag edge supplies the remaining two branch sets as claimed.
7. The monotone-augmentation count is correct:
   `|E(H)|\ge55+8r-\binom r2`, while the audited eight-connected extremal
   lemma gives `|E(H)|\le54+5r`.  Their difference is
   `1+3r-\binom r2>0` for every integer `1\le r\le7`.
8. Fabila-Monroy--Wood Theorem 6 and Hayashi Theorems 1.2(5), 1.3 were
   checked against the linked primary sources.  Their scope is reported
   accurately and does not preserve the pre-existing connected support
   sets.

## Trust boundary

The result does not prove that eight-connectivity forces a
model-compatible realization of one of `xe,ab,cd`.  The five paths of
Corollary 3.3 may all use the same support set, and the planar cofacial
alternative has not been converted into a strict bounded-interface
reduction.  The result also does not prove that a collision-minimal weak
`K_7` immersion is atomic, the single-collision terminal disjunction, or
`HC_7`.
