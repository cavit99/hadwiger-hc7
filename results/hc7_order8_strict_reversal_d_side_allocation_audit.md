# Independent audit: symmetric allocation in the three-vertex reversal case

**Verdict: GREEN.**  This is a separate internal mathematical audit, not
external peer review.  It checks the complete source
[`hc7_order8_strict_reversal_d_side_allocation.md`](hc7_order8_strict_reversal_d_side_allocation.md)
at SHA-256

```text
c873b80894ac72e9afec44c023d4ad4245d15df84160d8ec68eee08b2545ed88
```

After the audit, the source status was changed only to record this verdict
and link to this file.  No hypothesis, conclusion, proof step, or trust
boundary changed.  The resulting source SHA-256 is

```text
5a506ab80f1a32a0d0e7097c248c626369a16a28cad044e19f4bd220ca8a4335
```

## 1. Minimum-degree portal counts

The source now states explicitly that `G[E]` is the induced path `a b c`.
Together with the exact endpoint-reversal contacts and the absence of
`L`--`R` edges, the neighbours of `a` outside `D` are exactly
`b,d,x_d,y_d`, while those of `b` outside `D` are exactly `a,c,d`.
Minimum degree seven therefore gives

\[
                              |Q_a|\ge3,
                    \qquad   |Q_b|\ge4.
\]

The remaining three portal sets are nonempty because `D` is adjacent to
every boundary vertex except `d`.

## 2. Five-terminal allocation and the branch sets

The source invokes Xie's theorem with five distinct literal terminals:
the pair lies in `Q_a,Q_e` and the triple lies in
`Q_b,Q_{x_d},Q_{y_d}`.  The theorem returns two disjoint connected
subgraphs in the original graph `G[D]`; none of the virtual completion
edges is used as a host edge.

The two augmented branch sets are connected:

- `T union {a,e}` uses the literal contacts from `a,e` to the pair
  subgraph;
- `B union {b,c,x_e}` uses the contact from `b` to the triple subgraph and
  the literal path `b-c-x_e`.

They are adjacent through `ab`.  Together with `P_0,P_1` and the singleton
triangle `d,x_d,y_d`, the seven displayed branch sets are pairwise
disjoint.  Every adjacency is literal: `a` supplies the first augmented
set's three triangle contacts, `b,p_x,p_y` supply the second's, and
`e,x_e` supply the contacts to the two boundary-full subgraphs.  The
positive conclusion is therefore an explicit `K_7`-minor model.

## 3. Hall failure

For a deficient subfamily `I`, its union `Z` has order at most `|I|-1`.
If `D=Z`, then `|D|<=4`.  Otherwise a component `C` of `D-Z` has all its
internal neighbours in `Z`.  Its possible neighbours outside `D` lie in
the ten-set

\[
                             E\cup(S-\{d\}).
\]

It misses the distinct outside vertex corresponding to every portal set in
`I`.  Hence

\[
 |N_G(C)|\le (|I|-1)+(10-|I|)=9.
\]

The nonempty opposite shore `R` remains outside `C union N_G(C)`, so this
is an actual separator rather than only a neighbourhood estimate.
Seven-connectivity supplies the lower bound seven.

## 4. Failure of six-connectivity and the retained response

When the completion has at least seven vertices and is not six-connected,
its separator has order at most five.  Since the completion only adds
edges, a component `C` of an open side in the original `G[D]` satisfies
`N_D(C) subseteq K`.  The other open side is nonempty, so `C` is a strict
connected proper subset of `D`.  The full-neighbourhood decomposition in
the source follows from `L=E dotcup D`, the absence of `L`--`R` edges, and
the fact that `D` misses `d`.

For a crossing edge `uv`, every six-colouring of `G-uv` makes its endpoints
equal; otherwise the edge can be restored.  If its outside restriction
induced the fixed inner equality partition on the full separator, colour
names could be aligned and the two colourings glued.  This would
six-colour `G`.  Proposition 5.2 is therefore valid.

## 5. Trust boundary

The theorem does not eliminate `|D|<=6`, make an order-seven-to-nine
separator colour-compatible, or show that the strict subset reproduces the
labelled order-eight configuration.  It is a conditional unbounded
reduction, not a proof of `HC_7`.
