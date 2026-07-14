# Independent audit: packet-donor rotation lock

**Verdict:** **GREEN.**  Under the declared exact complementary-lock setup,
every packet-donor rotation in the target-free one-/two-hole branch moves
exactly one of the two literal donor anchors.  The seven bags in Theorem 2.2
have all and only the two asserted missing cycle diagonals, so their quotient
is literally `K_3 join C_4`.  The Kempe swap in Theorem 3.1 produces the
stated exact boundary partition, and the four displayed representatives form
a literal `K_4`; the symmetric orientation is valid.

Audited theorem SHA-256:

```text
c1c77e21a5107927b075baadd0300bf7920eb5308b6ef7d6783fbcbe6963cc7e
```

After audit, the theorem's status line alone was changed from "awaiting
independent audit" to "proved and independently audited".  The resulting
SHA-256 is
`5fc5425bd2b0daa18c93885d917d8a59f9819b06dd6dcaea297dc4a81a4e9453`;
the mathematical text is unchanged.

## 1. Scope dependencies

Two inherited meanings are used and are essential.

1. A **legal single-gate rotation** is the one-/two-hole output of the
   audited near-model trichotomy.  Thus its new centre misses at most two of
   the five fixed rows.  Excluding `K_7` and `K_7^-` then gives
   `|mathcal E|=2`.  The exclusion alone would give only
   `|mathcal E|>=2`; the trichotomy's one-/two-hole conclusion supplies the
   reverse inequality.
2. The exact complementary-lock setup is the proper-minor-minimal
   non-six-colourable setting of the paired-state trichotomy.  This is what
   licenses the six-colouring of the proper minor in Theorem 3.1.

These hypotheses are present in the stated provenance (the complementary
lock followed by its audited near-model trichotomy), although restating them
in Section 1 would make the note more self-contained.

## 2. Exact portal and anchor classification

Different components of `G-S` are anticomplete.  The complementary defects
of `X,Y` on `B_1`, together with the retained literal lobe contacts, therefore
give the exact portal identities

```text
N_F1(X)={t1},    N_F1(Y)={a1}.
```

Consequently `W` misses `X` exactly when `t1` moved into `Z`, and it misses
`Y` exactly when `a1` moved into `Z`.

If both anchors move, the two missing rows are exactly `X,Y`, disjoint from
the old missing pair `c,r`; the overlap model (2.4) is then a `K_7^-`, a
contradiction.  If neither anchor moves, `W` contains all of `B_1`.  It sees
`c` through the required `c-B_1` edge, sees `F_2` because the `S`-full packet
`Q subseteq F_2` sees every vertex of `B_1`, and sees both `X,Y` through the
two retained exact portals.  It can then miss at most `r`, contradicting
`|mathcal E|=2`.  Thus exactly one anchor moves, and the missing set is
precisely its lobe row plus one member of `c,r`, as claimed.

The overlap model used above is also sound.  If the old and new two-row
missing sets were disjoint, `A={s} union W` meets every fixed row: `s` handles
the rows outside the old pair and `W` handles the rows outside the new pair.
The gate `Z` meets the old pair by legality and meets every newly missing row
because the old donor `F_1=Z union W` met that row while `W` does not.  Thus
`Z` can miss only the fifth fixed row.  Together with the fixed `K_5` this is
a literal `K_7^-` model.

## 3. Theorem 2.2: exact `K_3 join C_4` ledger

Put

```text
A={s} union W,
cycle = A-Z-{h}-K-A,
triangle = {bar h}, H, F2.
```

All seven sets are nonempty, pairwise disjoint, and connected.  In
particular, `A` is connected through the stipulated `s-W` edge.

### Cycle edges

- `A-Z`: the cut parts `W,Z` are adjacent.
- `Z-h`: a legal gate repairs both old missing rows `c,r`.
- `h-K`: every old neutral row meets both old singleton rows.
- `K-A`: the sole portal from `F_1` to `K` is the anchor retained in `W`.

### The two diagonals are genuinely absent

- `A-h` is absent, not merely unforced: `h in mathcal E` makes `W`
  anticomplete to `h`, while the old centre `s` is anticomplete to both
  `c,r`.
- `Z-K` is absent, not merely unforced: the exact portal identity says the
  only vertex of `F_1` seeing `K` is the retained anchor, and that anchor lies
  in `W`, not `Z`.

### Common triangle and all join edges

The rows `{bar h},H,F_2` are pairwise adjacent in the old near model.  Their
adjacencies to each cycle bag are literal:

| cycle bag | to `{bar h}` | to `H` | to `F_2` |
|---|---|---|---|
| `A={s} union W` | `W` sees every row outside `mathcal E={H,h}` | old `s-H` | old `s-F_2` |
| `Z` | gate repairs both `c,r` | moved anchor is the sole `F_1-H` portal | the moved boundary anchor sees the `S`-full packet `Q subseteq F_2` |
| `{h}` | old literal `c-r` edge | old singleton-neutral edge | old singleton-neutral edge |
| `K` | old neutral-singleton edge | old `K-H` neutral-clique edge | old `K-F_2` neutral-clique edge |

Hence every join edge exists, the triangle is complete, the four cycle
edges exist, and exactly the two cycle diagonals are absent.  The quotient
is literally `K_3 join C_4`, as asserted.

## 4. Theorem 3.1: exact state and literal `K_4`

Take the first orientation `t1 in Z`, `a1 in W`,
`mathcal E={X,c}`.  Since `W` contains `a1` and is anticomplete to `c`,
`ca1` is absent.  The required `c-B_1` contact is therefore `ct1`, so `c`
and `t1` lie in the same `alpha-delta` Kempe component.

If that component omitted `a1`, swapping it changes the boundary colours
exactly as follows:

```text
c: delta -> alpha,
t1: alpha -> delta,
a1: remains alpha,
B2 and B3: unchanged.
```

Thus the equality partition is exactly

```text
{c,a1} | {t1} | B2 | B3,
```

not a coarsening.  The four representatives

```text
R1=Y union {c,a1},  R2={t1},
R3=Q union B2,      R4=X union B3
```

are disjoint and connected.  Their six adjacencies are:

- `R1-R2` via `ct1`;
- `R1-R3` via fullness of `Q` at `c` or `a1`;
- `R1-R4` via the old literal `X-Y` edge;
- `R2-R3` via fullness of `Q` at `t1`;
- `R2-R4` via the exact `t1-X` portal;
- `R3-R4` via fullness of `Q` at either vertex of `B_3`.

They therefore form a literal `K_4` indexed by the four blocks.  Contracting
the three nonsingleton representatives is a proper operation: the nonempty
open thin shore remains untouched.  A six-colouring of this proper minor
returns exactly the same four-block state on the closed thin shore, while
the Kempe-swapped colouring realizes it on the closed rich shore.  Palette
alignment and gluing are valid.

For the symmetric orientation, interchange `a1,t1` and `X,Y`.  Then
`ct1` is absent, the required paired contact is `ca1`, the hypothetical
swap gives

```text
{c,t1} | {a1} | B2 | B3,
```

and the four representatives are

```text
X union {c,t1},  {a1},  Q union B2,  Y union B3.
```

The same six literal witnesses, with the indicated labels interchanged,
give the required `K_4`.  The second-packet statement follows by the
declared complete relabelling.

## 5. Exact scope

The theorem is a local lock on packet-donor rotations in the no-`K_7^-`
branch.  It does not show that a legal rotation exists, preserve a full
packet after splitting, supply a decreasing global potential, or terminate
the near-model rotation system.
