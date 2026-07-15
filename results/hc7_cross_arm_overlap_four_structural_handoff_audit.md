# Cold audit of the overlap-four structural handoff

## Verdict

**GREEN.**  Lemma 1.1 preserves the given cyclic order of the five
terminals and produces a genuine extra adjacency between nonconsecutive
rooted bags.  The terminal-cycle input, crossed-residue `K_3` core, and
the final `K_4^-` composition are also valid under the eleven stated
irredundant support hypotheses.

The theorem ends at a labelled `K_7^-` model.  It does not repair its last
missing adjacency, select a global two-vertex transversal, or create a
ranked exact-seven descent.  The sentence that this feeds an existing
one-hole spine should therefore be read only as a handoff description,
not as a closed implication to `K_7`.

## 1. The nonlocal bridge exists

Let the five prescribed terminals occur on `C` in the order

```text
t_0,t_1,t_2,t_3,t_4.
```

The closed terminal arcs `C_i=t_iCt_{i+1}` overlap only at their terminal
ends.  Suppose every `C`-bridge were local to one such arc.  A nontrivial
component bridge in a three-connected graph has at least three distinct
attachments, so its local arc is unique.  A local chord can be assigned
to its containing arc.

For a fixed `i`, take the internal vertices of `C_i` and the interiors of
all bridges assigned to it.  No edge from this set leaves through a
vertex other than `t_i,t_{i+1}`.  If the set is nonempty, those two
terminals are a vertex cut separating it from the other three prescribed
terminals, contradicting three-connectivity.

If all five sets are empty, every terminal arc is a single edge and there
is no nontrivial component bridge.  A local chord would duplicate one of
the five cycle edges, which is impossible in the simple graph.  Hence the
whole graph would be `C_5`, which is not three-connected.  Therefore some
bridge has two attachments `x,y` not contained together in any one
terminal arc.  A path through that bridge has ends `x,y` and all internal
vertices outside `C`.

This also covers the case in which the nonlocal bridge is itself a chord,
when the path has one edge.

## 2. Terminal-order-preserving endpoint assignment

For a point `x` on `C`, let `L(x)` be the set of terminal bags to which it
can be assigned while the five bags remain in the prescribed cyclic
order:

```text
L(t_i)={i},
L(x)={i,i+1} if x is internal to C_i.
```

The required elementary fact is

> If `x,y` do not lie in one common `C_i`, some
> `a in L(x), b in L(y)` are nonconsecutive on the five-cycle.

Here is a complete verification without changing terminal names.

* If `x=t_i`, the exclusion of a common terminal arc says that `y` lies
  neither internally on `C_{i-1}` nor internally on `C_i`, and is not
  `t_{i-1}` or `t_{i+1}`.  A terminal `y` is therefore already
  nonconsecutive to `t_i`; if `y` is internal to another arc, at least one
  end of that arc is nonconsecutive to `i`.
* If both points are internal, say to distinct arcs `C_i,C_j`, then for
  consecutive arcs choose the two nonshared ends (`i` and `i+2`, after
  rotation).  For nonconsecutive arcs, at least one of the four choices
  is nonconsecutive.  Otherwise both ends of `C_j` would lie in the
  three-set `{i-1,i,i+1}` and `C_j` would be `C_{i-1}` or `C_i`, contrary
  to the preceding cases.

The symmetric terminal/internal case is included in the first bullet.
Thus the assignments can be made while retaining the original cyclic
order; no cyclic permutation depending on graph labels is hidden here.

The two assigned points lie in different terminal arcs unless one is a
terminal, so the cut edge in each relevant open arc can be chosen
independently.  Delete one edge from every open terminal arc, choosing it
so that `x` and `y` lie in their selected terminal pieces.  The resulting
five pieces are nonempty, connected, pairwise disjoint, contain
`t_0,...,t_4` in the original order, and the five deleted edges give the
five consecutive bag adjacencies.

Add the bridge path with `y` deleted to the bag containing `x`.  Its
internal vertices avoid `C`, so this preserves disjointness and
connectivity.  Its last edge supplies an adjacency to the bag containing
`y`; the selected bags are nonconsecutive.  This proves Lemma 1.1 with
the precise rooted order claimed.

## 3. Published cycle input

Lemma 4 of Groenland--Nederlof--Koana applies with its subdivision-edge
set empty and root set `R=T`.  It says that a three-connected graph with
no minor model of `K_4` whose four bags all contain terminals has a cycle
through every terminal.

For five literal terminals, this rooted condition is equivalent to a
`K_4` model rooted at some four of them.  Four pairwise disjoint bags
meeting `T` contain four distinct members of `T`; conversely a model
rooted at four terminals has all four bags meeting `T`.  The fifth
terminal may lie in one of the bags, and the audited rooted-`K_4` decoder
explicitly permits that.

## 4. Crossed-residue three-bag core

In each of the 27 crossed states, the complement on `I` is a perfect
matching

```text
u u', v v'.
```

The only possible terminal--`I` nonedge is `6w`.  Choose `u=w` if it is
present, otherwise choose either endpoint of one matching edge, and take
`v` on the other matching edge.  Then

```text
{u,v}, {u'}, {v'}
```

are connected, disjoint, and pairwise adjacent: `uv`, `vu'`, `uv'`, and
`u'v'` are all original edges because their ends belong to different
matching pairs where required.  Every terminal other than `6` is complete
to `I`; vertex `6` contacts `{u,v}` through `v` and contacts both
singletons.  Lemma 3.1 is therefore literal and does not use a virtual
cycle edge.

## 5. Final branch-set composition

Lemma 1.1 returns five bags `E_0,...,E_4` in the original terminal order,
with the cycle adjacencies and a chord.  Every chord of a five-cycle joins
vertices at cyclic distance two.  Rotate indices only for exposition so
that it is `E_0E_2`, and merge `E_3` with `E_4` across their cycle edge.
The four exterior bags

```text
E_0, E_1, E_2, E_3 union E_4
```

have edges

```text
01, 12, 02, 2(34), 0(34),
```

and hence form `K_4` with only the pair `E_1--(E_3 union E_4)` possibly
missing.

Each exterior bag contains at least one of the five original terminals.
Every such terminal contacts all three `I`-bags from Section 4.  Thus all
twelve cross adjacencies between the four exterior bags and three
interior bags are literal.  The interior bags form `K_3`, and the exterior
bags form `K_4^-`; together they are seven disjoint connected bags with
exactly one possible missing pair, a labelled `K_7^-` model.

No terminal order is changed in producing the rooted chord.  The later
cyclic relabelling only names the endpoints of the chord for the abstract
`K_4^-` composition and is independent of the crossed-frame labels.

## 6. Trust boundary

This audit relies on the already independently checked finite decoder
statements for:

1. the 27-state crossed complement form;
2. the lift from any exterior rooted `K_4`; and
3. closure of the ten noncrossed terminal orders.

It checked the new infinite part directly: existence of a nonlocal
bridge, preservation of the five terminal order, and the literal
seven-bag one-hole composition.  It does not assert that an arbitrary
`K_7^-` minor in a seven-connected contraction-critical graph can be
repaired to `K_7`.
