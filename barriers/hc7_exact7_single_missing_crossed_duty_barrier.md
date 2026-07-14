# Single-missing crossed-duty carrier barrier

**Status:** finite static and minimum-degree barriers verified.  They refute
the direct claim that two crossed duties plus one gate-supported duty must
contain two disjoint duty carriers.  They do not refute the full
seven-connected common-face/curvature closure.

The executable certificate is
`hc7_exact7_single_missing_crossed_duty_barrier_verify.py`.

## 1. Exact five-vertex cell

Let

```text
C=G[{k,j,x1,x2,x3}]=K5-kj,
X={x1,x2,x3}, K={k}, J={j}.
```

Give the two lobes the exact supports

```text
N_S(k)={c,a1,a2,a3},
N_S(j)={c,a1,t2,t3},
```

and put the sole missing-duty gate edge at `t1-x1`.  This is the isolated
alternative

```text
U1=W1={x1},
U2=U3=W2=W3=empty.
```

Adding `t2-x1` gives a literal concentrated alternative: every nonempty
set among the six gate-contact sets is the singleton `{x1}`.

All three duties have connected carriers.  Nevertheless no two distinct
duties have disjoint carriers.  In the isolated graph every `B2`- or
`B3`-carrier contains both `k` and `j`, while every `B1`-carrier contains
`x1` and at least one of `k,j`.  After adding `t2-x1`, a `B2`-carrier which
avoids `j` must contain both `k` and `x1`; the same intersection obstruction
remains.

Thus the following inference is false even in a three-connected literal
triangle-gate cell:

> two crossed duties exist, and the third duty is gate-supported;
> therefore two duty carriers can be selected disjointly.

The obstruction is shared portal rank, not absence of individual paths.
The four crossed terminal roles collapse to the two literal lobe anchors
`k,j`.

## 2. Minimum degree seven still does not repair the inference

The verifier expands the `K`-lobe to a literal icosahedron.  Each of its
twelve vertices gets one gate edge and a `c`-edge; only the named anchor
`north` sees `a1,a2,a3`.  The sibling remains the singleton `j`, with
support `{c,a1,t2,t3}`, and only `x1` sees `t1`.  Add two singleton
`S`-full packets `p,q` and the complete four-partite boundary graph with
parts

```text
{a1,t1}, {a2,t2}, {a3,t3}, {c}.
```

This expansion has all of the following properties, checked literally:

* minimum degree seven;
* a three-connected rich cell with the exact two lobe supports and isolated
  gate-contact pattern;
* an actual old seven-boundary with packet vector `(1,2)`;
* legal attainment of the paired state by contracting `p` with
  `{a1,t1}` and extending a proper six-colouring; and
* no two distinct duties with disjoint carriers inside the rich cell.

It is not seven-connected.  The verifier checks that its vertex
connectivity is exactly four, with minimum cut

```text
{c,j,north,t1}.
```

It also verifies an explicit `K7` model, so no `HC7` counterexample or
terminal-disjunctive falsifier is claimed.  Its purpose is narrower:
minimum degree, exact state attainment, and the packet vector do not replace
the global cell-cut use of seven-connectivity.

## 3. What survived the adversarial test

The full seven-connected closure does not need a distinct opposite-lobe
portal pair for the gate-supported first duty.  Under nonreflection, form
the three pairwise four-terminal instances using artificial terminals
attached to the complete literal portal stars.  For each pair:

1. a crossing decodes to two disjoint literal duty carriers;
2. a crossless web completion cannot retain an actual clique-cell vertex,
   because its exits lie in a set of order at most six; and
3. deleting completion edges and then the artificial terminals leaves a
   genuine face containing all four complete portal sets.

The two genuinely crossed duties provide the synchronization invariant.
For `r=2,3`, choose

```text
p_r in N_K(a_r), q_r in N_J(t_r).
```

The vertices `p_r,q_r` are nonadjacent.  Whitney uniqueness therefore
identifies the three pairwise faces: duty 2 identifies the `12` and `23`
faces, and duty 3 identifies the `13` and `23` faces.  The resulting one
face contains the complete `a1` and `t1` portal stars as well, even though
the first duty has no opposite-lobe witness pair.

The order-five cell cannot survive this conclusion.  Its common face has
length four or five.  Length five makes the three-connected five-vertex
cell outerplanar, contradicting the edge lower bound from minimum degree
three; at length four the fifth vertex has no non-`c` boundary neighbour
and hence host degree at most five.  Therefore the cell has at least six
vertices.  The standard exact-seven Hall cut then gives six distinct
portal representatives on the common face.  Pairwise nonreflection forces
their cyclic word to be

```text
A B D A B D.
```

The audited circle-incidence upper bound and planar curvature lower bound
then contradict minimum degree seven.

The sharply necessary invariant is therefore not the existence of three
individual duties.  It is:

```text
full pairwise carrier failure
+ complete-star four-terminal pages
+ two nonadjacent crossed-duty synchronizers
+ genuine seven-connectivity for clique-cell clearance and the six-label SDR.
```

Removing the last item gives the verified finite barriers above.  Treating
completion edges as host edges is neither needed nor permitted.
