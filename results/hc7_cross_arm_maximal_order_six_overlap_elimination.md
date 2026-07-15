# Maximal overlap in the order-six cross-arm outcome

## Status

Proved and independently cold-audited, using the audited full-seven-point
support lemma and its seven-connectivity lift.

This eliminates the maximal-overlap part of the remaining order-six rigid
cross-arm cell.  It does not treat `|A cap X|<=4`, nor the order-five arm
core `|X|=4`.

## Theorem

Let `G` be seven-connected and `K_7`-minor-free.  Suppose the rigid outcome
of the private-pair cross-arm theorem consists of a six-vertex support `A`,
a private pair `{p,q}` disjoint from `A union X`, and arms

```text
X union {p},   X union {q},
```

where `|X|=5`.  Suppose, as supplied by that theorem, that for every
`x in A cap X` both

```text
(A-{x}) union {p},   (A-{x}) union {q}
```

support `K_5` models.  Then

```text
|A cap X| <= 4.
```

## Proof

Assume instead that `|A cap X|=5`.  Since `|X|=5`, we have `X subset A`.
Let `r` be the unique vertex of `A-X` and put

```text
Y=A union {p}.
```

The set `Y` has seven vertices.  Every one of its six-subsets supports a
`K_5` model:

* `Y-{p}=A` is the original support;
* `Y-{r}=X union {p}` is the `p`-arm; and
* for every `x in X`,
  `Y-{x}=(A-{x}) union {p}` is one of the forced replacements.

These are all seven choices of the omitted vertex of `Y`.  The
full-seven-point support lemma therefore gives a `K_6` model whose support
is contained in `Y`.  Its support has order at most seven, so the audited
small-`K_6` lift in a seven-connected graph supplies a seventh branch set.
Thus `G` contains a `K_7` minor, a contradiction.  Hence
`|A cap X|<=4`.  \(\square\)

## Dependencies and exact contribution

The only external dependencies inside this repository are Lemmas 4.2 and
4.3 of
[`hc7_support_at_most_six_separated_triple_extraction.md`](hc7_support_at_most_six_separated_triple_extraction.md).
The proof uses only the `p`-arm; the symmetric `q`-arm is not needed.

Together with the literal-support overlap theorem, the positive-overlap
rigid cell now has the following precise form:

* if `|A|=5`, no overlap is possible;
* if `|A|=6` and the common arm core has order five, maximal overlap is
  impossible; and
* the live order-six overlap has `1<=|A cap X|<=4`, or has an order-four
  arm core.

No claim is made that the surviving overlaps compose automatically.
