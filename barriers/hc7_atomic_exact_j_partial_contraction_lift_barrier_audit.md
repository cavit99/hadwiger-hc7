# Internal audit of the partial-contraction lifting barrier

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- barrier:
  [`hc7_atomic_exact_j_partial_contraction_lift_barrier.md`](hc7_atomic_exact_j_partial_contraction_lift_barrier.md)
- exact SHA-256:
  `3c6d899bb9dc4225cad6b19e473aef59f86a9b88676b28d4bebdff26ac6ee6ec`

The hash was computed after the barrier status was changed to GREEN.

## Verdict

GREEN.  The path-join family has exactly the claimed connectivity,
contraction, colouring, and minor properties.  It proves an unbounded
connectivity-only lifting barrier while explicitly remaining outside the
`K_7`-minor-free and minor-critical hypotheses.

## Checks performed

1. The graph `B=K_7-{xe,ab,cd}` is complete multipartite with parts of
   orders `2,2,2,1`, so `kappa(B)=5` and `chi(B)=4`.  Contracting the path
   factor of `G_r=P_r` join `B` produces exactly
   `J=K_8-{xe,ab,cd}`.
2. A cut of a join must delete one whole factor.  Hence
   `kappa(P_s` join `B)=min(s+5,8)`, which is seven for `s=2` and eight for
   `s>=3`.  Every proper subset of the `r-1` path edges leaves `s>=2`, while
   the full contraction leaves the six-connected graph `J`.  Thus the
   all-subsets minimality and `kappa(G_r)=8` claims are exact.
3. In the two-vertex predecessor, replacing the quotient image `f` by its
   two path blocks in the antipodal six-cut gives the displayed order-seven
   separator.  Its full host expansion is
   `S_r={a,b,c,d,g}` union `V(R)`, and direct neighbourhood calculation gives
   `N(x)=N(e)=S_r` and `|S_r|=r+5=6+|F|`.  Since `kappa(G_r)=8`, no host
   separator of order seven exists.
4. Deleting any path edge gives two nonempty connected path bags `U,V`.
   Together with `{g}`, `{x,a}`, `{e,c}`, `{b}`, and `{d}`, they are seven
   disjoint connected pairwise adjacent bags.  This verifies the explicit
   terminal `K_7` model.  Join additivity gives
   `chi(G_r)=chi(P_r)+chi(B)=2+4=6`.
5. With the `H_0` branch labelled `f` represented by `p_1`, the literal
   frame uses the host edge `e-p_1` for its `ef` edge.  The outside component
   containing `p_2` supplies the paths
   `a-p_2-b` and `c-p_2-d`.  Its clean endpoint supports cross both missing
   pairs, consistently placing this family in the terminal rather than the
   quadrant-confined residue.
6. For a general inclusion-minimal first bad forest set `F_0`, splitting one
   edge gives a seven-connected predecessor.  Any cut of the quotient of
   order at most six must contain every nontrivial fibre image; replacing one
   such image by its split pair proves the cut has order six.  Full expansion
   adds one vertex per forest edge, giving `|T^+|=6+|F_0|`.  When `F_0` is a
   matching, each split predecessor has the exact seven-boundary
   `(T-{z_h})` union `{x_h,y_h}`, so seven-connectivity makes every expanded
   endpoint, as well as every ordinary cut vertex, full to every lifted
   component.

## Trust boundary

Every graph in the family is six-colourable and contains the displayed
`K_7` minor.  The family is not a counterexample to the atomic theorem or
`HC_7`; it only refutes lifting an immediate-predecessor cut by connectivity
and contraction minimality alone.  The bounded matching-interface number is
not a proved recursive rank, and the earlier partial-quotient ownership
problem remains open.
