# Audit: four-response exclusive-trace barrier

**Verdict:** GREEN for the stated abstract claim, after the named-endpoint
repair incorporated in the adjacent certificate.  The certificate also
satisfies all four demand lower bounds required by a simultaneous
`(1,1)/(1,1)` twin.  It does not realize an `HC_7` host or the universal
proper-minor response language.

## 1. Named separating swap

Name `u=b1`.  Extend the displayed boundary colourings by

\[
 \phi(z)=\phi(u)=0,\qquad \phi(d)=1,
\]

where `f=dt`.  Let the `z`-side `X` of the deleted bridge `f` have literal
boundary trace

\[
                         X\cap(K\cup A_0\cup B_0)
                         =\{t,a_1,a_2\}.
\]

Swapping colours `0,1` on `X` changes `z,t,a1,a2` from colour zero to
colour one.  It leaves `d` at colour one and `u=b1` at colour zero.  Thus
the resulting colouring is proper on `e=zu`, has the two ends of the
deleted edge `f` in the common colour `gamma=1`, and agrees exactly with
the displayed response `psi` on all nine boundary labels.  In particular
the certificate respects the facts that the `z`-side contains `z,t` but
not `u,d`.

For each `epsilon in {2,3,4,5}`, a `gamma-epsilon` component containing
`d,t` may have literal boundary trace `{t}`.  Swapping it changes only the
displayed colour of `t`.  The persistent block

\[
                         \{a_1,a_2,k_1\}
\]

witnesses mismatch on `Omega_D`, while the broken fixed equality
`t=b1` witnesses mismatch on `Omega_E`.  Hence all eight crossed-state
inequalities hold without an exclusive trace in any of the four new lock
components.

The sentence that the *other literal lock side* contains all of `B_0`
would be too strong: `b2` has colour five and is not in the `0-1` lock.
What is proved, and all the barrier needs, is that the swapped trace
contains all of `A_0` and no member of `B_0`; its complement in the
nine-label set contains `B_0`.  No geometric membership of that complement
in the other lock component follows.

## 2. Packet-demand check

Take no gate--old-boundary edges and put on the old seven labels the path

```text
a1-k2-a2-b2-b1-k3-k4.
```

It is connected and bipartite, and both `phi` and `psi` are proper on it.
Using

\[
 d_H(\Pi)=|\Pi|-\omega(H[\operatorname{sing}(\Pi)]),
\]

the exact demands on `(Omega_D,Omega_E)` are

| response | `Omega_D` | `Omega_E` |
|---|---:|---:|
| `phi` | 3 | 4 |
| `psi` | 2 | 4 |
| swap `epsilon=2` | 2 | 4 |
| swap `epsilon=3` | 3 | 4 |
| swap `epsilon=4` | 3 | 4 |
| swap `epsilon=5` | 3 | 4 |

Every number is strictly greater than one.  Therefore the four strict
demand inequalities from the crossed-state theorem, specialized to packet
vectors `(1,1)/(1,1)`, do not eliminate the certificate.  Packet number
one is geometric data and is not asserted by this abstract state pattern.

## 3. What double-contraction saturation does not add abstractly

The saturation fork concerns a colouring `c` of the different minor
`G/e/f`.  It does not identify `c` with `psi` or require either exact
boundary partition to be preserved.  Even compatibility with one saturated
double response imposes no new nine-label restriction: keep the `psi`
colours on the nine labels, set

\[
 c(z)=c(u)=0,\qquad c(d)=c(t)=1,
\]

and give `d` five internal neighbours of colours `0,2,3,4,5`.  The four
neighbours of colours `2,3,4,5` may be internal vertices on the literal
paths `d-x_epsilon-t`; those paths have boundary trace `{t}`.  Thus `d`
sees all five alternate colours outside `t`, while the four-response
boundary certificate is unchanged.

This is only a compatibility extension, not a realization of the universal
statement for every colouring of `G/e/f`.  It pinpoints the missing input:
one must couple a saturated double response to the selected bridge response
by a boundary-state-preserving operation, or localize its five witnesses in
literal twin duties/model rows.  Saturation as a palette statement alone
cannot do that.

## 4. Exact consequence for the decoder

The state-only promotion is false even after imposing every numerical
condition visible in the simultaneous packet-one cell.  A viable next
operation must spend at least one genuinely geometric datum:

1. a literal localization of one lock/bypass relative to `D,E,A_0,B_0`;
2. a boundary-preserving transfer from a colouring of `G/e/f` to the
   selected `G/f` response; or
3. a labelled first-hit/same-row split in the regenerated `K_6` model.

Another comparison of the eight exact partitions cannot distinguish the
certificate above.
