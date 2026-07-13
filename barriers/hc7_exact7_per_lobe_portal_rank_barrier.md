# Barrier: portal rank three is not forced in each nontrivial lobe

## Exact negative statement

The following assertion is false, even with the complete literal
exact-seven `(1,3)` hypotheses:

> If a lobe `K` behind a three-cut has order at least three and satisfies
> the forbidden-label portal matching inequalities, then `K union T`
> has a `T`-rooted `K_3` model of literal portal rank three.

The verifier
`active/hc7_exact7_portal_rooted_triangle_probe.py` constructs an
18-vertex counterexample and checks every cut of order at most six.

## Construction

Let

```text
T = {t0,t1,t2},  C = {c0,c1,c2},  D = {d0,d1},
S = {s0,...,s6}, R = {p0,p1,p2}.
```

The gate is the path `t1-t0-t2`.  The lobe `C` is the path
`c0-c1-c2`, with `t0` adjacent to all of `C`, `t1` adjacent to `c0`,
and `t2` adjacent to `c2`.  The lobe `D` is the edge `d0d1`, and both
its vertices are adjacent to all of `T`.

Every vertex of `C` contacts `s0,...,s5`, and `c1` also contacts `s6`.
Every vertex of `D` contacts `s0,...,s5`.  Each of `t1,t2` contacts
`s0,s1,s2`, while `t0` has no boundary portal.  The boundary graph is
`K_{3,4}` with bipartition
`{s0,s1,s2}|{s3,s4,s5,s6}`.  Finally, each `p_i` is adjacent to every
literal vertex of `S`, and there are no `LR` edges.

The script prints the complete 86-edge list and verifies:

1. the ambient graph is seven-connected;
2. `L` is three-connected and nonplanar;
3. `T` is an actual three-cut with exactly the two lobes `C,D`;
4. the packet vector is `(nu_L,nu_R)=(1,3)`;
5. both lobes satisfy every forbidden-label rank inequality and the
   global portal rank is seven; and
6. exhaustive branch-set enumeration finds no portal-rank-three rooted
   triangle in `C union T`.

The obstruction is transparent.  In every `T`-rooted triangle model in
`C union T`, the `t0` bag is the singleton `{t0}`.  It has no literal
boundary portal, so the model has portal rank at most two.

## Exact trust boundary

This does **not** refute the target-free two-lobe route.  The other lobe
`D` has a rank-three rooted triangle, and the host contains the explicit
literal `K_7` model

```text
{t0,d0,s0}, {t1,s1}, {t2,d1,s2},
{c0,c1,c2,s6}, {p0,s3}, {p1,s4}, {p2,s5}.
```

Therefore the reusable target must be a disjunction over the two lobes
(or directly `rank-three model / literal K_7 / state splice`), not a
per-lobe assertion.  Any proof that insists on a prescribed lobe needs
an additional target-free or contraction-critical exchange mechanism.
