# Barrier: four response swaps need not expose an exclusive trace

**Status:** exact nine-label partition certificate with a dependency-free
verifier.  This is not an `HC_7` counterexample and contains no assertion
about realization by a seven-connected host.

## Claim refuted

In the separating twin seam, let `psi` be the response colouring of
`G/f`, with common endpoint colour `gamma`, and let the four
`gamma-epsilon` components containing `d,t` be swapped one at a time.
The facts that every resulting response still mismatches the fixed
`G/e` state on both twin boundaries do **not** imply that one component
has a boundary trace outside the common five-set `K`.  They do not even
force the original bridge side to contain one literal from each exclusive
pair.

Thus the four crossed-state inequalities alone do not label one bypass
with an `A_0`- or `B_0`-duty.  Actual path or portal geometry is required.

## Certificate

Use colours `0,1,2,3,4,5`, with

\[
 \gamma=1,\qquad\delta=0,
\]

and literal labels

\[
 K=\{t,k_1,k_2,k_3,k_4\},\qquad
 A_0=\{a_1,a_2\},\qquad B_0=\{b_1,b_2\}.
\]

The twin boundaries are

\[
                    \Omega_D=K\cup A_0,
       \qquad       \Omega_E=K\cup B_0.
\]

Give the fixed `G/e` state `phi` and the bridge-swapped `G/f` state `psi`
the following colours:

| label | `t` | `k1` | `k2` | `k3` | `k4` | `a1` | `a2` | `b1` | `b2` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `phi` | 0 | 1 | 2 | 3 | 4 | 0 | 0 | 0 | 5 |
| `psi` | 1 | 1 | 2 | 3 | 4 | 1 | 1 | 0 | 5 |

This is exactly the boundary effect of swapping colours `0,1` on a bridge
side whose trace is `{t,a1,a2}`.  In particular the swapped trace contains
all of `A_0` and none of `B_0`; its complement in the nine-label set
contains `B_0`.  This does **not** put all of `B_0` in the other literal
lock component (`b2` has colour five).  Notice also that the
unswapped state `psi` already differs from `phi` on both twin boundaries:
on `Omega_D` the block `{t,a1,a2}` is replaced by a block containing
`t,a1,a2,k1`, while on `Omega_E` the `phi`-block `{t,b1}` is broken and
`t` instead joins `k1`.  For each

\[
                         \epsilon\in\{2,3,4,5\},
\]

let the trace of the central `1-epsilon` component be only `{t}`.  Swapping
that component changes `t` from `1` to `epsilon` and no other boundary
label.

Every one of the four resulting states still differs from `phi` on both
twin boundaries:

* on `Omega_D`, the response retains the new equality
  `a1=a2=k1`, absent in `phi`;
* on `Omega_E`, the response breaks the `phi`-equality `t=b1` (and for
  `epsilon=2,3,4` merges `t` with a `k_i`, while for `epsilon=5` it merges
  `t` with `b2`).

Thus none of the four *new swaps* needs an exclusive trace: the crossed
inequalities are maintained by a persistent bridge mismatch together with
changes whose traces lie inside `K`.  All four component traces are
contained in `K`, and the original bridge trace contains only one of the
two exclusive duties.

The old seven labels can simultaneously carry a connected bipartite
boundary on which both displayed colourings are proper.  For example take
the path

```text
a1-k2-a2-b2-b1-k3-k4.
```

This verifies that connected bipartiteness of the old boundary does not
remove the abstract certificate.

## Exact implication

The next decoder cannot infer a duty-labelled channel merely by comparing
the four exact response partitions with `phi`.  It must additionally use
one of:

1. literal localization of a bypass in a twin shore;
2. row-duty geometry in the regenerated `K_6` model; or
3. another named proper-minor operation whose response controls the
   common-five-set mergers.

The certificate says nothing against such a geometric or dynamically
coupled theorem.
