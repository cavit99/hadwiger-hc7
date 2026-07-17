# Bare-cycle and full-wheel barrier at overlap three

## Status

**Status:** explicit finite counterarchitecture, independently reproducible
by
[`hc7_seven_terminal_carrier_live_crosscheck.py`](hc7_seven_terminal_carrier_live_crosscheck.py).

This is not a counterexample to `HC_7`.  It shows that neither a bare
rooted `C_7` nor an arbitrary full seven-vertex three-connected terminal
kernel is sufficient, by itself, to compose the normalized arm-order-six,
overlap-three support relation.

## Exhaustive cycle result

There are `110` live support-relation orbits and `360` unoriented labelled
orders of `C_7`.  Of the `39,600` state/order pairs,

```text
2111 are not K7-forcing,
107 of the 110 states have at least one bad order,
3 states close for every order.
```

Thus the universal rooted-carrier theorem

```text
C7 or K3,4
```

does not alone close the cell.  Every `K_{3,4}` placement is sufficient,
but the theorem may return only a cycle.

## Explicit first cycle obstruction

For the first canonical live state, the forced original edges are

```text
02 03 04 05 06 07 08 09
12 13 14 15 16 17 18 19
24 25 26 27 28 29
34 35 38 39 45 67.
```

The forced original nonedges are

```text
01 23 48 49 58 59 68 69 78 79,
```

and the seven unresolved original pairs are

```text
36 37 46 47 56 57 89.
```

Choose every unresolved original pair absent and add only the rooted cycle

```text
3-4-5-6-7-8-9-3.
```

The resulting ten-object quotient has no `K_7` minor.  It nevertheless
satisfies the joined nine-support relation represented by the partial
state.

## Retaining the full kernel is still insufficient

The same canonical state remains `K_7`-minor-free after adding the full
wheel carrier with hub `3` and rim

```text
4-5-6-7-8-9-4.
```

This wheel is a minimally three-connected spanning terminal kernel.  Hence
the obstruction is not merely an artefact of discarding all kernel chords
except one Hamilton cycle.

The obstruction is edge-maximal on the terminal carrier.  Its nine absent
terminal pairs are

```text
46 47 48 57 58 59 68 69 79,
```

and adding any one of them produces a verified `K_7` model.  Thus a
composition-aware reversal of the last terminal-legal contraction need
only recover one genuine adjacency across this list; a bare quotient does
not record whether the two preimage sides provide it.

The exact implication is limited: a four-connected host which contracts
to this wheel may contain further preimage attachments capable of closing
the state.  A successful continuation must preserve and use such
attachments, obtain the `K_{3,4}` alternative, or invoke a separate
four-connected rooted carrier.  The terminal-irreducible kernel as an
unlabelled three-connected quotient is not enough.
