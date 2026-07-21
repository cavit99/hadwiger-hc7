# A common connector/provenance vertex does not orient atomic collision descent

**Status:** explicit barrier/counterexample to an intermediate claim;
computer-assisted finite result; separate internal audit GREEN.

This note tests a sparse obstruction in which an `e`--`x` connector
passes through the unique internal vertex of the provenance route from `f`
to `g`.  Moving that common vertex into the `x`-bag produces the exact
eight-bag quotient

\[
                     K_8-\{ab,cd,fg\}.
\]

That quotient change is not a collision descent.  In the graph below the
original atomic strong `K_7` immersion is globally minimal for the
bookkeeping potential `(M,T,H,L)`, and it is the unique atomic strong
immersion at the minimum score.  The rotated quotient has no
label-preserving strong-immersion lift.

The host is only three-connected and is three-colourable.  Thus it is not a
counterexample to a theorem which genuinely uses seven-connectivity or the
proper-minor colouring responses of a hypothetical minor-minimal
counterexample to `HC_7`.  It refutes the local inference that the quotient
rotation itself supplies progress.

The
[`deterministic checker`](hc7_atomic_shared_hub_defect_rotation_verify.py)
is retained beside this note.

## 1. The local claim refuted

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}
\]

with core branch vertices `a,b,c,d,e,f,g` and collision vertex `x`.
Consider the following proposed implication.

> **False shared-vertex descent claim.**  Suppose `T` is a labelled
> subdivision of `H_0`, `h` is internal on `T_fg`, and there are edges
> `eh,hx`.  If assigning `h` to the `x`-bag gives a spanning quotient
> `K_8-{ab,cd,fg}`, then a collision-minimal atomic immersion supported by
> `T` can be replaced by a weak `K_7` immersion with smaller
> `(M,T,H,L)`, or at least by an equal-score atomic strong immersion which
> realizes the rotated labels.

Here `T` in the potential is the branch-transit coordinate, not the
subdivision.  The example below satisfies all the local graph and quotient
hypotheses of this claim and falsifies both conclusions.

## 2. Construction

Start with the literal graph `H_0`.  Subdivide the four edges

\[
                         ac,\quad bd,\quad ad,\quad bc
\]

once, using new vertices

\[
                    p_{ac},\quad p_{bd},\quad p_{ad},\quad p_{bc},
\]

respectively.  Add the four edges

\[
             fp_{ac},\quad fp_{bd},\quad gp_{ad},\quad gp_{bc}.
\]

Subdivide `fg` once as `f-h-g`, and add `eh,hx`.  Call the resulting
graph `G_*`.  It has thirteen vertices and thirty-four edges.

The original labelled routes use `a-x-b` for the `ab` demand,
`c-x-d` for the `cd` demand, the five displayed subdivided routes for
their corresponding core edges, and the literal edge for every other
demand.  They form an atomic strong `K_7` immersion with

\[
                         (M,T,H,L)=(1,0,0,28).             \tag{2.1}
\]

The unique collision is `x`, on the disjoint demands `ab` and `cd`.
There are seven internal transit roles: two at `x`, one at each of the
four `p`-vertices, and one at `h`.

The graph is far outside the full `HC_7` hypotheses.  Its connectivity is
three, and the following are the colour classes of a proper
three-colouring:

\[
 \{f,g,x\},\qquad
 \{e,p_{ac},p_{bd},p_{ad},p_{bc}\},\qquad
 \{a,b,c,d,h\}.                                          \tag{2.2}
\]

The triangle `aef` shows that its chromatic number is exactly three.

## 3. Exact rotated quotient

Define eight connected bags

\[
\begin{array}{c|c}
\text{label}&\text{bag}\\ \hline
X&\{x,h\}\\
e&\{e\}\\
a&\{a,p_{ac},p_{ad}\}\\
b&\{b,p_{bd},p_{bc}\}\\
c&\{c\}\\
d&\{d\}\\
f&\{f\}\\
g&\{g\}.
\end{array}                                                \tag{3.1}
\]

They partition `V(G_*)`.  The only nonadjacent pairs of bags are

\[
                            ab,\qquad cd,\qquad fg.        \tag{3.2}
\]

In particular, `eh` gives the `eX` adjacency, `fh,gh` give the `fX,gX`
adjacencies, and the four `x`-edges give all contacts from `X` to
`a,b,c,d`.  Thus (3.1) is exactly a labelled model of
`K_8-{ab,cd,fg}`.

The operation has consumed the only `f`--`g` provenance route.  It has not
constructed new edge-disjoint demand paths.

## 4. The original immersion is globally collision-minimal

### Theorem 4.1 (finite classification)

The graph `G_*` has no `K_7` minor.  Among all weak `K_7` immersions in
`G_*`, the immersion in Section 2 is lexicographically minimum for
`(M,T,H,L)`.  More precisely:

1. there is no atomic strong immersion of length at most twenty-seven;
2. there is exactly one atomic strong immersion of length twenty-eight;
3. its branch set is `\{a,b,c,d,e,f,g\}`, and its unique collision is
   `x` on `ab,cd`; and
4. its complete route family is the one displayed in Section 2.

#### Finite proof

The checker first exhausts all spanning partitions of `V(G_*)` into seven
nonempty blocks.  It tests connectedness of every block and all twenty-one
pairwise block adjacencies.  This is an exact `K_7`-minor oracle: in a
connected graph, every clique-minor model can be made spanning by absorbing
each component outside the model into an adjacent branch set.  The oracle
finds no model.

Consequently a weak immersion with `M=0` is impossible, because such an
immersion is a subdivision of `K_7` and hence gives a `K_7` minor.  The
displayed immersion has `M=1` and `T=0`, so a lexicographically better
immersion must also have `M=1,T=0`.  Then it is an atomic strong immersion,
and `H=0` automatically.

For each of the

\[
                              \binom{13}{7}=1716
\]

possible branch sets, the checker generates every simple path for each of
the twenty-one demands whose internal vertices avoid the other branches.
It backtracks over these paths using a 34-bit edge-usage mask.  Every
nonbranch vertex may have one transit role, except that exactly one vertex
may have two.  These are precisely the atomic strong-immersion conditions.

There are six nonbranch vertices for every branch choice.  An atomic strong
immersion therefore has at most seven internal transit roles: two at its
collision and at most one at each of the other five vertices.  Hence its
length is at most `21+7=28`.  The enumeration through length twenty-eight
is exhaustive, not a search-bound assumption.  It gives the four claims
above.

This proves global lexicographic minimality: later coordinates cannot
improve until `M=1,T=0,H=0` have been matched, and the exhaustive search
then minimizes `L`.

## 5. Why the rotated quotient has no labelled strong lift

To decode (3.2) while retaining `ab,cd` as the two collision demands, the
new collision would have to be `f` or `g`.  Consider collision `f`.  A
literal lift using `x` as the root of the `X`-bag would have branch set

\[
                          \{a,b,c,d,e,g,x\}.              \tag{5.1}
\]

In a strong immersion, the `xe` and `xg` demand paths must avoid the other
six branch vertices internally.  But

\[
                            N_{G_*}(x)=\{a,b,c,d,h\}.
\]

Both paths must therefore begin with the same edge `xh`, contradicting
edge-disjointness.  Choosing `h` as the literal root does not help: a
branch vertex of a weak `K_7` immersion needs six distinct incident first
edges, while `d_{G_*}(h)=4`.  The argument with `f,g` interchanged is
identical.

The exact enumeration is stronger: no choice of seven literal branch
vertices supports another atomic strong immersion at all.  Thus the
failure is not repaired by choosing a different vertex from one of the
other bags.

This is the ownership gap.  A connected minor bag can carry six quotient
adjacencies without containing one vertex from which six edge-disjoint
immersion demands can be routed.  Relabelling the three absent quotient
pairs does not supply that routing.

## 6. Verification

Run from the repository root:

```text
.venv/bin/python -B barriers/hc7_atomic_shared_hub_defect_rotation_verify.py
```

The exact output is

```text
GREEN atomic shared-hub defect-rotation barrier
host: vertices=13 edges=34 connectivity=3 K7_minor=no
original: potential=(1,0,0,28) collision=x demands=ab,cd
rotated_partition: defects=ab,cd,fg bag_X={x,h}
atomic_search: branch_sets=1716 L<=27=0 L=28=1
minimum_witness: branches=abcdefg collision=x demands=ab,cd
rotated_strong_lifts: collision_f=no collision_g=no
```

The clique-minor oracle and the immersion-routing search are separate
exhaustive calculations.  NetworkX is used only for the graph data
structure and the supplementary exact connectivity value.

## 7. Correct host-level gate

The barrier does not rule out a theorem which spends seven-connectivity.
It identifies what that theorem must produce before claiming progress.

### Lemma 7.1 (clean replacement or an exact seven-separator)

Let `G` be seven-connected and contain a subdivision `T` of `H_0`.  Let
`h` be internal on `T_fg`, and suppose `eh,hx` are edges.  Put

\[
                           Z=\{a,b,c,d,e,x\}.
\]

Then either

1. `Z union {h}` is an actual order-seven separator between `f` and `g`;
   or
2. `G-Z-h` contains an `f`--`g` path `R`.

If outcome 2 has a choice of `R` satisfying

\[
                         V(R)\cap V(T)=\{f,g\},           \tag{7.1}
\]

then `G` contains an explicit `K_7` minor.

#### Proof

The graph `G-Z` is connected because `|Z|=6`.  If deleting `h` separates
`f` from `g`, outcome 1 holds.  Otherwise it contains the path in outcome
2.

Under (7.1), assign `h` to a connected bag containing `x`.  The edge `eh`
supplies the missing `xe` quotient adjacency, and the two sides of `T_fg-h`
supply the contacts from this bag to the `f`- and `g`-bags.  Split the
internal vertices of `R` between those two bags; one edge of `R` supplies
their adjacency.  Allocate every other route interior of `T` to an endpoint
bag.  This gives eight disjoint connected bags whose only absent pairs are
`ab,cd`.  The seven bags

\[
                 X,\quad E,\quad A\cup C,\quad B,\quad D,
                 \quad F,\quad G
\]

are pairwise adjacent and form a `K_7` model.  \(\square\)

The unresolved shared-vertex case is now precise: outcome 2 exists, but
every such path meets another provenance-route interior.  Those attachment
intervals must be decoded into a clean replacement, an `ab`/`cd` crossing,
an exact order-seven separator, or a response-preserving reduction.  Calling
the dirty path a rotated defect does none of these things.

There is also a safe contraction test which must be applied in the original
host, before any large provenance forest is contracted.  If `uv` is an edge
of a seven-connected graph and `G/uv` is not seven-connected, then `G` has
an actual order-seven separator containing `u,v`.  Indeed, a cut of order at
most six in `G/uv` must contain the contracted vertex; replacing it by
`u,v` gives a cut of order at most seven in `G`, and seven-connectivity makes
the order exactly seven.  If `G/uv` remains seven-connected, however, that
fact supplies no colouring or immersion lift by itself.  After earlier
forest contractions, expanding the cut can have unbounded order, so the
same inference cannot be made at quotient level without host-level control.

## 8. Trust boundary

The example proves only a local barrier.  In particular:

* `G_*` is three-connected, not seven-connected;
* `G_*` is three-colourable and is not contraction-critical;
* its degree-four common vertex cannot occur unchanged in a
  seven-connected host;
* the original atomic frame does not have two separately owned contacts
  from `x` to both clean support bags `f,g`; both attempted contacts use
  the one vertex `h`; and
* the result neither refutes the exact minimal-forest landing theorem nor
  supplies a counterexample to the single-collision terminal disjunction.

A valid positive theorem may use the extra neighbours forced at `h`, the
proper-minor colouring responses, or the dirty replacement path's bridge
attachments.  What it may not use is the bare isomorphism between the two
eight-bag quotient matchings as a well-founded step.
