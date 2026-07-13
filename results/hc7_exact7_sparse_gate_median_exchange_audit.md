# Independent audit: exact-seven sparse-gate median exchange

## Verdict

**GREEN after one scope correction and terminology clarification.**  The
three-terminal connector normal form, its lift through the arm
contractions, both versions of the missing leaf--leaf repair, and the
seven literal branch sets in Theorem 3.1 are valid.  The universal
quantifiers in Corollaries 4.1 and 4.2 are also valid when a *minimal
connector* means an inclusion-minimal and then edge-minimal connected
subgraph after contracting the three chosen arm sets.

The original closing paragraph said that all `Y` connectors had been
eliminated also in the edgeless-gate case.  That was too strong: a `Y`
whose three chosen boundary labels are independent can remain.  The
theorem file now states the exact weaker residue.  It also distinguishes
a rooted `K_3` model in the contracted lobe from a minimal connector,
which itself is a tree.

This audit does **not** regard the common-median residue as closed and
does not infer a common colouring state from it.

## 1. Dependencies used

The note invokes only already audited facts from the exact `(1,3)`
two-lobe setting:

1. a lobe of order at least three has three distinct portal vertices
   with three distinct literal labels in `S`;
2. those vertices have three vertex-disjoint paths to the three distinct
   gate vertices, truncated at their first gate hits;
3. every lobe meets each literal gate vertex and has at least four
   literal boundary labels;
4. a surviving thin shore has order at least eight; and
5. three disjoint `S`-full packets exist in the opposite shore.

Items 1--4 are proved and audited in
`hc7_exact7_two_lobe_gate_exchange.md`; item 5 is part of the literal
exact `(1,3)` hypothesis.  No contraction-critical colouring assertion,
virtual web edge, or extra connectivity is used here.

## 2. Connector normal form and contraction lift

Let `A_1,A_2,A_3` be the entire `K`-parts of the three linkage paths.
They are nonempty, connected, and pairwise disjoint.  Contracting each
`A_i` to a named vertex `a_i` is legitimate and preserves all edges from
that arm to the rest of the lobe.

If the contracted lobe has an `{a_1,a_2,a_3}`-rooted `K_3` model, its
three branch sets lift to disjoint connected sets containing the whole
respective `A_i`; every model edge also lifts to a literal original
edge.  This proves outcome 1.

Otherwise choose an inclusion-minimal, then edge-minimal, connected
subgraph containing the three named roots.  After pruning irrelevant
parts it is a tree whose minimal root-spanning subtree has exactly one
of two forms:

* one named root lies on the path between the other two; or
* a unique non-root degree-three vertex has three internally disjoint
  arms to the roots.

The first form partitions into three connected bags whose adjacency
tree is a path centred at the internal named root.  In the second form,
placing the Steiner vertex and its chosen root arm in any prescribed
root bag makes that root bag the median.  The other two arms are
disjoint leaf bags.  Lifting the named contractions restores the entire
`A_i` inside its assigned bag.  Thus the `W_i` in Lemma 2.1 really do
contain the complete linkage arms; no path segment is lost during the
contraction or lift.

If an additional literal leaf--leaf edge exists, the lifted bags are
already a rooted triangle, which is harmless and only strengthens
outcome 1.  The proof never relies on a contraction-created edge without
lifting it.

## 3. Literal carrier construction

For `B_i=W_i union {t_i}`:

* the `B_i` are pairwise disjoint because the `W_i` and `t_i` are;
* each `B_i` is connected because `W_i` contains `A_i=Q_i-t_i`, including
  the vertex incident with `t_i`;
* each `B_i` contains the portal `x_i` and therefore can be enlarged by
  its distinct representative `s_i`.

In connector outcome 1 all three `B_i` adjacencies already occur in the
lobe.  In path outcome 2, the connector supplies the two median--leaf
adjacencies.  The missing leaf--leaf adjacency is supplied in either of
the two asserted literal ways:

1. an edge between the two leaf gate vertices joins the two unanchored
   carrier bags; or
2. an edge between the two leaf representatives joins those bags after
   the representatives are adjoined.

The other lobe `J` is disjoint from all `B_i`, connected, and adjacent
to each of them through its contact with the corresponding literal
`t_i`.  Since `|N_S(J)|>=4`, it has a representative `s_0` outside the
three distinct `s_i`.  Consequently the four anchored `L`-side carriers
are connected, disjoint, and pairwise adjacent.

Anchor the three disjoint full packets at the remaining three literal
vertices of `S`.  Two packet bags are adjacent because either packet is
full to the anchor of the other; a packet bag is adjacent to every
`L`-carrier bag because it is full to that carrier's anchor.  These are
seven literal, pairwise adjacent branch sets.  Thus Theorem 3.1 produces
an actual `K_7` minor, not only a quotient model.

## 4. Audit of the universal residual statements

Fix arbitrarily:

* an order-at-least-three lobe;
* a legal three-label portal matching;
* a legal three-arm linkage, indexed by its distinct gate endpoints;
  and
* any minimal connector of the three contracted arms.

Theorem 3.1 applies to this arbitrary choice.  Therefore its
contrapositive may be taken universally over all such choices in a
surviving graph.

### 4.1 One literal gate edge

If the unique gate edge is `t_1t_2`, a Steiner `Y` can be represented
with median `t_3`; its leaf bags are then repaired by `t_1t_2`.  A path
whose median is `t_3` is repaired in the same way.  Hence, once a rooted
`K_3` model is excluded, **every** minimal connector is a path with
median `t_1` or `t_2`.  Its two leaf representatives must be nonadjacent,
or the boundary-edge version of Theorem 3.1 closes it.

### 4.2 Two-edge gate path

If the gate edges are `t_1t_2,t_2t_3`, a Steiner `Y` may be assigned
median `t_1` (or `t_3`) and repaired by the opposite literal gate edge.
A path with median `t_1` has leaf gate edge `t_2t_3`; a path with median
`t_3` has leaf gate edge `t_1t_2`.  Therefore every minimal connector in
a survivor is a path with median exactly `t_2`, and its `t_1`- and
`t_3`-arm representatives are nonadjacent.  This universal conclusion
does not depend on choosing one preferred connector.

### 4.3 Edgeless gate

A rooted `K_3` model closes.  For a Steiner `Y`, if two of the three
chosen labels are adjacent, choosing the opposite arm as the median
makes those two labels the leaves and closes by the boundary edge.  A
path connector closes whenever its two leaf labels are adjacent.

What remains is genuinely weaker than a common-median statement: a
Steiner `Y` with three independent chosen labels is not eliminated, and
different path connectors may have different medians provided their
respective leaf labels are nonadjacent.  The corrected theorem file now
records exactly this trust boundary.

## 5. Exact remaining gap

For a one-edge gate, the residue has only the two endpoint medians; for
an unlabelled-middle two-edge gate, every minimal connector has the same
literal middle.  To close those cells one still needs a portal exchange
that breaks the orientation or a separately justified proper-minor
state.  In the edgeless-gate cell even that common orientation has not
been proved.  None of these missing conclusions follows from the present
literal model construction alone.
