# Two reserved terminals plus a rooted triangle do not close overlap three

**Status:** exhaustive falsification of the stated bounded-carrier
mechanism.  This is not a graph-theoretic counterexample to `HC_7`.

The checker is
[`hc7_overlap_three_order_six_two_reserved_triangle_verify.py`](hc7_overlap_three_order_six_two_reserved_triangle_verify.py).

## Proposed mechanism

In the normalized arm-order-six, overlap-three cell put

```text
I={0,1,2},  T={3,4,5,6,7,8,9},  H=G-I.
```

The host `H` is four-connected.  For two reserved terminals `r,s`, the
graph `H-{r,s}` is two-connected, so any selected three of the other five
terminals root a `K_3` model there.  The proposed composition retains the
three singleton vertices of `I`, the two reserved singleton terminals, and
the three rooted-triangle bags.  It asks whether some choice produces a
`K_7` minor in this eight-object quotient.

The lift is label-faithful.  The three rooted bags avoid `r,s`; original
quotient edges are literal root incidences; and the only virtual edges are
the three actual adjacencies of the rooted triangle.  Omitted terminals may
be absorbed by its bags without affecting the certificate.

## Exhaustive result

After the common three-rooted small-`K_4` and already-forced literal `K_7`
outcomes are removed, there are 110 category-automorphism orbits of live
partial states, of total weight 6,636.  The checker tests, for each orbit,
all

```text
21 choices of {r,s} times 10 choices of the rooted triple.
```

Exactly 55 orbits, of total weight 3,141, admit no successful choice.  All
failures have path core `G[I]=P_3`; their weighted profile is

```text
(good terminals, I-edges) : weight
(4,2):1071, (5,2):1260, (6,2):810.
```

Across all live states, the number of successful reserved-pair/triple
choices has weighted distribution

```text
0:3141, 1:81, 3:468, 4:2592, 6:354.
```

The separate reserved-five-root fan experiment has 13 failure orbits.
Every one of those 13 also fails the two-reserved triangle mechanism.
Thus the two mechanisms do not patch one another at the exact residue for
which the triangle was proposed.

## Consequence

Deleting two terminals and retaining only the universal rooted-`K_3`
guarantee loses too much labelled carrier information.  Any viable repair
must use the repair-terminal/path-core incidence, retain a larger rooted
model, or decode the web/preimage structure forced by four-connectivity.
