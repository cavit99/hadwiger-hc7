# Independent audit: atomic three-packet core completion

## Verdict

**GREEN.**  Both dependency-free verifiers pass, and the displayed branch
sets lift correctly.  The updated theorem closes exactly the stated
order-two, order-four, order-five and order-six atomic circuits.  Its
rooted Hall completion is valid for arbitrary target order, but assumes
the pairwise-adjacent core pieces and a full opposite shore; it does not
claim the full capture--capture or web--web branch and does not create the
core from colouring saturation alone.

## 1. Proposition 2.1

For a singleton shore subset, the three other `K_4` vertices and five
boundary contacts give eight external neighbours.  For a two-vertex
subset, the two remaining core vertices and at least six boundary labels
give eight; every three rows cover all seven labels and have one remaining
core neighbour.  Thus the strict-surplus inequality is correct.

An `A`-carrier and a `B`-carrier each require at least two vertices, so
two disjoint such carriers exhaust the four-vertex shore and leave no
nonempty `C`-carrier.  The three displayed pairwise packets are valid:
the diagonal edges carry `A|B`, and the indicated edge/singleton pairs
carry `A|C` and `B|C`.

## 2. Boundary orientation and the order-four bags

The orientation dichotomy in Lemma 3.1 is replayed over all 336 oriented
matching rows by the verifier.  In the ordinary case, the four core bags
in (4.1) are connected through their portal pieces and pairwise adjacent
through the core clique; their four distinct `A union B` roots contact the
full shore.  The `c_0,s` singleton bags see every core piece, see one
another, and see the full shore.

In the exceptional case, `a_1s` is an edge, `X_10 union X_01` is
connected, and `R union {c_0}` is connected by fullness.  Direct replay of
the seven missing boundary edges and the three displayed portal rows
verifies all 21 bag adjacencies.  In particular every missing incidence
with `c_0` is repaired through `R`; no branch set overlaps another.

## 3. Theorem 5.1: parameter-uniform rooted Hall completion

Theorem 5.1 is sound for every `t`.  Hall's condition gives an injection
from the `t-2` core pieces into the `t-2` labels in `S-{s,r}` and hence a
bijection.  The bags `U_i union {t_i}` are connected, disjoint and
pairwise adjacent through the `U_i`.  Their distinct roots contact `R`;
their `s`-portals contact the connected boundary bag `{s,r}`; and
fullness supplies the adjacency between `R` and every other bag.  The bag
count is `(t-2)+1+1=t`, so these are a literal `K_t` model.

The exact scope matters.  This is a completion theorem, not a general
rooted-clique packaging theorem: it requires `t-2` already disjoint,
pairwise adjacent connected core pieces, all with an `s`-portal, plus a
connected shore adjacent to every boundary label.  Subject to those
hypotheses, no boundary clique assumption beyond the edge `sr` is used.

## 4. Order-two closure

The two-vertex circuit is a valid strict-surplus, pairwise-but-not-triple
example: either singleton has one internal and seven boundary neighbours,
and two vertices cannot carry three disjoint nonempty demands.

For each of the seven fully-positive boundary rows, the table in (6.2)
gives a vertex `r` and four disjoint connected pairwise adjacent bags in
`J-r`.  With the two adjacent full circuit pieces and `R union {r}`, the
four boundary bags see both circuit pieces by fullness and see the last
bag through `R`; the two circuit pieces see the last bag through `r`.
Thus (6.1) has all 21 adjacencies.  The verifier checks these certificates
for all 48 orientations of each row, even though the order-two certificate
itself is orientation-independent.

For order five, every core vertex is a `6`-portal and every row of (6.4)
is a distinct representative system after omitting `r`.  For order six,
`{0,1}|{2}|{3}|{4}|{5}` is a literal `K_5` model in
`K_6-{03,14}`, every bag has a `6`-portal, and (6.7) gives the required
SDRs.  A seven-edge boundary containing the three matching edges cannot
make `6` nonadjacent to all six endpoints, so an adjacent omitted root
`r` always exists.

## 5. Executable replay

The commands

```text
.venv/bin/python atomic_three_packet_circuit_verify.py
.venv/bin/python atomic_three_packet_core_completion_verify.py
```

return, respectively,

```text
strict-surplus packet circuits verified (2, 4, 5, 6)
explicit core-completion certificates {2: 336, 4: 336, 5: 336, 6: 336}
```

The order-two boundary `K_4` table, the order-four case split, and every
order-five/six SDR are replayed as explicit branch-set certificates rather
than accepted from a generic minor-search result.

No scope overclaim was found: the remaining atomic obstruction may have
order at least seven or fail the rooted Hall condition, exactly as Section
7 says.
