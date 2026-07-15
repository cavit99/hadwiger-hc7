# Bad-hub wheel barrier at overlap three

**Status:** resolved quotient barrier, retained as a warning.  It is not a
graph counterexample to `HC_7`.

In the order-five-arm overlap-three cell, the finite decoder leaves one
planar quotient type after all common rooted-`K_4`, direct `K_7`,
five-good rooted-`K_4`, and all-six cofacial fan outcomes are removed.

Use

```text
I={0,1,2},
T=W dotunion {b},   |W|=5.
```

The set `I` is a clique and is complete to `W`; the terminal `b` misses two
or three vertices of `I`.  In facial order the literal graph on `W` is
`P_5`.  Contracting the connected side containing `b` gives the wheel

```text
b join C_5.
```

The resulting nine-object graph need not contain a `K_7` minor.  Every
nonconsecutive rim pair is nevertheless a repair edge: supplying any one
of the five chords gives `K_7`.  There are 48 labelled original states,
forming six symmetry types, and the checker in
[`../active/hc7_overlap_three_order_five_verify.py`](../active/hc7_overlap_three_order_five_verify.py)
verifies all 240 repairs.

This falsifies the unconditional inference

```text
five good cofacial terminals + one full connected bad-terminal side
    => K7.
```

The quotient erased the information that closes the cell.  In the actual
four-connected exterior, delete `b`.  The facial cycle remains peripheral
in the three-connected graph `H-b`, so the remainder `D` is a nonempty
connected bag universal to the five rim bags, while `b` remains a separate
adjacent singleton bag.  The expanded ten-object decoder closes all 864
state/order inputs (and hence all 48 facially feasible collapsed-wheel
states); see
[`../results/hc7_overlap_three_five_good_decoder.md`](../results/hc7_overlap_three_five_good_decoder.md).

The reusable warning is that contracting a full connected side together
with a named terminal can destroy the extra branch object needed for
composition.  Preserve the terminal and apply peripheral structure after
deleting it before declaring a wheel quotient terminal.
