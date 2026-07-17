# Cold audit of the double-critical-edge rooted fan

## Verdict

**GREEN** for the exact mathematical revision described below.  This is a
separate internal mathematical audit, not external peer review.  It verifies
the common-neighbour colour saturation, set-valued Kempe lemma, rooted fan
minor, and private-label counts.  It does not verify or assert a `K_7` minor
or `HC_7`.

## Audited revision and provenance

The cold audit checked
[`hc7_double_critical_edge_rooted_fan.md`](hc7_double_critical_edge_rooted_fan.md)
at SHA-256

```text
d49a9dc7ed369a939e27c61e5f7c64e6476039ce1d1771d5a879a8af1b96b462
```

and returned GREEN for every mathematical theorem, proof, and numerical
count.  It requested one non-load-bearing wording correction in Section 4:
the four non-universal bags need not *induce* a path, but the theorem
guarantees only the path edges.  Applying exactly that correction produced
SHA-256

```text
3921eb3208e64d77ea9ddf73b3251c9343573438c166317fd333641dc7a163f6
```

The current source differs from the latter revision only in its status line,
which now links to this audit.  Its current SHA-256 is

```text
2d9d009b3a1eab4ee38c3b4f75eb4767328feb335ebcc439c1811b7e0e96a3c1
```

No theorem statement, hypothesis, proof step, or trust-boundary statement
changed in either edit.

## Checks

1. **Common-neighbour saturation.**  In Lemma 1.1 the vertices recoloured
   with the sixth colour were one colour class, hence are independent.  If
   one were adjacent to `y`, it would be a colour-`i` common neighbour of
   `x,y`, contrary to the supposition.  Giving `x` colour `i` and `y` the
   sixth colour is therefore proper.
2. **Kempe completeness.**  Swapping colours on the union of all
   `i,j`-components meeting `C_i` removes colour `i` from the fixed common-
   neighbour set `C` if no such component also meets `C_j`.  Lemma 1.1 may
   then be applied to the resulting proper five-colouring, giving the stated
   contradiction.
3. **Connectivity and rooted fan.**  Any separator of `G-{x,y}` of order at
   most four, together with `x,y`, would be a separator of `G` of order at
   most six.  Thus the audited universal five-root fan theorem applies.  Each
   rooted bag contains a common neighbour of `x,y`, so adjoining the two
   singleton branch sets gives exactly a `K_2 join F_5` minor.
4. **Private labels and counts.**  The common-neighbour set avoids `L`, `R`,
   and every branch set privately supported by the endpoint `x`.  Hence the
   five common neighbours, one neighbour for every private label, and `y`
   are distinct neighbours of `x`, proving `d(x)>=6+|P_L(x)|`.  When the
   reduced path is the edge `xy`, the two endpoint-private label sets are
   disjoint and each has size at least two, giving
   `|N_G({x,y})|>=5+2+2=9`.

## Exact trust boundary

The proved output is a common-neighbour-rooted `F_5=K_1 join P_4` model in
`G-{x,y}` and therefore a `K_2 join F_5` model in `G`.  Among the four
non-universal fan bags, only the three path edges are guaranteed; three
further adjacencies remain unsupported.  The Kempe lemma is set-valued and
does not select one rainbow transversal with all required pairwise
connections.  The private-label proposition explains a palette-to-model
misalignment but does not repair it.  Thus the note proves neither a
common-neighbour-meeting `K_5` model, a `K_7` model, a compatible order-seven
separation, nor a strict defect-one descent.
