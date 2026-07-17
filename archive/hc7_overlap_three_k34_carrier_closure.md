# `K_{3,4}` carrier closure at overlap three

## Status and exact scope

**Status:** computer-assisted theorem; independent audit pending.

This theorem closes the normalized irredundant arm-order-six,
overlap-three rigid cell whenever its seven exterior terminals root a
`K_{3,4}`.  It does not show that this carrier, rather than the alternative
`C_7`, must occur.

The independent checker is
[`hc7_seven_terminal_carrier_live_crosscheck.py`](hc7_seven_terminal_carrier_live_crosscheck.py).
It shares only the joined nine-support relation with the earlier decoder;
it independently reconstructs the symmetry group, common-outcome filter,
minor search, and branch-set verification.

## Theorem

Let `G` be seven-connected and use the normalized labels

```text
A={0,1,2,3,4,5},       I=A cap X={0,1,2},
X=I union {6,7},        p=8, q=9,
T={3,4,5,6,7,8,9}.
```

Assume that each of

```text
A, X union {p}, X union {q},
(A-{i}) union {p}, (A-{i}) union {q}  for i in I
```

is an irredundant six-vertex support of a spanning `K_5` model.  If `T`
roots a `K_{3,4}` model in `G-I`, then `G` contains a `K_7` minor.

The `3+4` bipartition of the seven rooted bags is arbitrary.

## Finite certificate

Joining the nine irredundant support relations gives `60,162` partial
states, each with the same seven unresolved literal terminal pairs.  The
exact automorphism group of the normalized support family is

```text
Sym(I) x Sym(A-I) x Sym(X-I) x Sym({p,q}),
```

of order `144`.  The categories are intrinsic: `X-I` and `{p,q}` have
support-degrees two and four; among the support-degree-seven vertices,
co-incidence with an `(X-I)` support distinguishes `I` from `A-I`.

After independently removing the forced common rooted-`K_4` outcome there
are `140` orbits.  Thirty already contain a `K_7` using forced original
edges, leaving `110` live orbits.  For every live representative and every
one of the `35` labelled `3+4` bipartitions, the forced original edges plus
the twelve carrier adjacencies contain an explicit `K_7` model:

```text
110 x 35 = 3850 successful labelled compositions.
```

The checker searches independently by at most three edge contractions on
the ten quotient objects.  It then expands the contraction recipe and
verifies that the seven returned bags are nonempty, connected, disjoint,
and pairwise adjacent.  A deterministic digest of the `3,850` verified
certificates is

```text
3e83bbcf1b2e63519c3e8a3b1bc8ae5d758580b4d66a055111b418265d85a089
```

## Label-faithful lift

Carrier edges are added only after all original six-support relations and
the common-outcome test have been fixed.  Replace each terminal quotient
vertex by its rooted `K_{3,4}` bag in `G-I`, while the three members of `I`
remain singleton objects.  Original root-incident edges remain literal
through the roots, and each virtual biclique edge is an actual adjacency
between two rooted bags.  The rooted bags are pairwise disjoint and avoid
`I`, so every finite branch-set certificate lifts exactly.

No carrier edge is treated as a literal edge between its terminal roots or
fed back into an irredundancy constraint.
