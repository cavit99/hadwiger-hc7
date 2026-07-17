# Barrier: an arbitrary seven-root three-connected kernel does not compose

## Status

**Exact finite counterexample.**  The checker is
[`hc7_order_six_rooted_kernel_universality_falsifier.py`](hc7_order_six_rooted_kernel_universality_falsifier.py).
It uses the same joined support relation and exact branch-set enumerator as
the positive overlap-three decoders.

This barrier refutes only an overstrong carrier principle.  It is not a
counterexample to `HC_7` and does not include the geometry lost when a
four-connected host is contracted to a three-connected terminal kernel.

## Refuted statement

The following proposed composition claim is false:

> Every labelled three-connected graph on the seven terminal roots, when
> added as a rooted carrier to every surviving arm-order-six,
> overlap-three relation, produces a `K_7` minor.

Use the normalized labels

```text
I={0,1,2},   T={3,4,5,6,7,8,9}.
```

One legal joined partial relation has forced original edges

```text
01 02 04 05 06 08 09 12 14 15 17 18 19
23 24 25 26 27 28 29 34 35 38 39 49 58
67 68 69 79.
```

On the seven literal terminal roots add the carrier edges

```text
34 35 36 45 49 58 67 68 69 78 79.
```

The carrier is edge-minimal three-connected (it is a labelled copy of the
seven-vertex graph with graph6 code `FBjN_`).  Nevertheless the exact
branch-set enumerator finds no `K_7` model in the ten-object union.

The obstruction is not repaired by any one of the three missing carrier
edges

```text
37, 38, 39.
```

Every other single missing carrier edge does repair the quotient.  Thus the
counterexample is structured but not merely one arbitrary edge short of
closure.

## Consequence for the proof spine

The universal rooted `C_7`-or-`K_{3,4}` theorem remains valid and useful,
and every labelled `K_{3,4}` carrier closes this cell.  What fails is the
attempt to replace the carrier returned by a four-connected host with an
arbitrary bare three-connected terminal kernel.

A viable repair must retain additional information forced by the original
four-connectivity.  Two concrete possibilities are:

1. preserve four-connectivity under terminal-legal contractions and use the
   Fontet--Martinov structure of four-contraction-critical graphs; or
2. prove a label-preserving branch-bag split across a three-separator of the
   displayed minimal kernel.

Neither repair is proved here.
