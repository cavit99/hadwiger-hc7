# Independent audit: adaptive rich cut-packet exchange

**Status:** GREEN.

## Verdict

**GREEN after one required carrier-connectivity correction.**

The first draft incorrectly allowed a carrier missing `a` to fund a
nonsingleton independent block containing `a`.  That literal vertex would be
isolated in the carrier--block union.  The theorem and verifier now use the
correct condition

```text
a notin B,
```

not merely `B != {a}`.  With this repair, all ten hard boundary orbits and
all 42 ordered pairs of distinct defects pass.  The adaptive quantifiers,
minor contractions, exact pullbacks, and the rich-shore cutvertex geometry
are valid.

## 1. General labelled-carrier reflection

Let `C` be a maximum clique among the singleton blocks of `Pi`.  From
`d_H(Pi)=3`, exactly three blocks remain outside the singleton blocks
represented by `C`.  Assign these blocks bijectively to the three carriers.

The contracted sets `T_i union B(T_i)` are pairwise disjoint because the
carriers are disjoint outside `S` and the boundary blocks partition `S`.
Condition 1 makes each set connected.  Since both the carrier and its
assigned block are nonempty, such connectedness includes a carrier--block
edge, so at least one edge is contracted and the resulting minor is proper.

Condition 2 makes the three contracted representatives pairwise adjacent.
Condition 3 makes each representative adjacent to every retained literal
vertex in `C`; `C` itself is a clique.  Thus the representatives together
with `C` form a clique with exactly one vertex for every block of `Pi`.

The six-colouring is pulled back only to the untouched opposite closed
shore.  Each expanded block is independent, every edge from it to the
untouched shore became an edge at its representative, and distinct blocks
receive distinct colours because their representatives form a clique.  The
boundary equality partition is therefore exactly `Pi`.  It aligns by a
palette permutation with the colouring that returned `Pi`, and the two
colourings glue because there is no open-shore cross-edge.

## 2. Near-full carrier tests

For a carrier `X` with `D(X) subseteq {a}`, the worst case is that `X`
really misses `a`.

* `X union B` is connected whenever `a notin B`, since `X` contacts every
  vertex of `B`.
* If `a in B`, the literal vertex `a` has no edge to `X` and no edge to
  another vertex of `B`, because equality blocks are independent.  The union
  is disconnected.  This is why the corrected test is necessary.
* For a retained singleton `c != a`, `X` contacts `c`.  If `a in C`, the
  only missing representative--singleton adjacency can instead be supplied
  by an edge from `a` to a vertex of the assigned block `B`.

The same tests apply to `Y,b`.  The full carrier `Q` funds any remaining
block.  The `XY` edge supplies adjacency between their representative sets,
while fullness of `Q` at the nonempty boundary blocks assigned to `X,Y`
supplies both `Q` adjacencies.  These are exactly the hypotheses of the
general reflection lemma.

If an actual carrier is full while its selected pseudo-defect is `a`, these
tests are conservative: the extra contact cannot invalidate the certified
assignment.

## 3. Quantifier order and finite certificate

The required order is

```text
boundary H and geometric defects (a,b)
    -> choose independent block I(H,a,b)
    -> contract the thin full packet with I
    -> receive an arbitrary proper equality state Pi containing exact I
    -> choose C and assign its three remaining blocks to Q,X,Y.
```

The verifier implements this order.  It first computes every independent
block whose every exact state has demand three.  For each ordered pair of
distinct defects, it asks whether at least one such block closes **all** of
its possible returned states.  It then checks the compact graph6 certificate:

* one fixed block works for every ordered defect pair in each of the first
  nine orbits;
* in the standard Moser labelling, `I={1,5}` works except for the unordered
  pair `{3,4}`, for which `I={0,5}` works.

The printed two failures for the single global Moser choice `{1,5}` are
expected and are exactly the ordered pairs `(3,4)` and `(4,3)` repaired by
the adaptive choice `{0,5}`.  They are not theorem failures.

After the connectivity patch, a fresh run gives no adaptive-defect failures
in any orbit and terminates with

```text
CERTIFIED adaptive three-carrier exchange
```

The enumeration covers all 876 proper boundary partitions, every maximum
singleton clique, all six assignments of the three unrepresented blocks,
and all 42 ordered pairs of distinct defects for each of the ten hard atlas
graphs.

## 4. Two-component rich-shore geometry

Assume `G[R]` has components `Q,K`, with a cutvertex `w` in `K`.  Every
open-shore component is `S`-full: its neighbourhood lies in the literal
seven-set `S`, and deleting fewer than seven such neighbours would separate
it from the nonempty opposite shore.  Hence both `Q` and `K` are connected
full carriers.

Choose a component `D` of `K-w` and put

```text
X = D,
Y = K-D.
```

Because `K` is connected, every component of `K-w` has a neighbour at `w`.
Thus `X` is connected; `Y`, which contains `w` and at least one other
component of `K-w`, is connected; and an edge from `D` to `w` is an `XY`
edge.  The three carriers `Q,X,Y` are nonempty and pairwise disjoint.

For `X`, its graph neighbourhood is contained in `S union {w}`.  The other
rich component and the thin shore remain beyond that neighbourhood, so
seven-connectivity gives `|N_S(X)|>=6`.  Applying the same argument to any
other component of `K-w`, which lies inside `Y`, gives
`|N_S(Y)|>=6`.  Therefore each split carrier has defect empty or a singleton.

Since `X union Y=K` is `S`-full, the two actual singleton defects cannot be
equal.  If one carrier is full, select for it any pseudo-defect distinct from
the other's defect; if both are full, select any two distinct pseudo-defects.
This choice is made before `I` and only strengthens the near-full hypotheses.

The thin packet is then contracted with the certified `I(H,a,b)`.  Fullness
makes `I` an exact boundary block, and strong contraction-criticality gives
an arbitrary six-colouring of that proper minor.  The finite theorem handles
every state it can return.  Reflection through `Q,X,Y` and palette alignment
therefore six-colour `G`, contradicting the counterexample assumptions.

Singleton rich components cause no hidden problem: they are cutvertex-free
and are not claimed to be closed by this corollary.  A component possessing a
cutvertex has at least two components after deletion, exactly what is needed
to make both `X` and `Y` nonempty.

## 5. Exact scope

This is a genuine infinite-family closure: in the ten absolute-demand-three
boundary orbits, if the rich shore has two components, both must be
cutvertex-free.  It does not imply that those components are 2-connected,
does not close singleton components, and does not treat the connected-rich
shore or the other 119 adaptive boundary states.
