# Independent audit: cyclic gate-bypass falsifier

Audited file: `barriers/hc7_exact7_gate_bypass_falsifier.md`.

## Verdict

**GREEN as a local adversarial certificate.**  It refutes only the
unqualified local implication

> a bridge bypassing a selected Helly gate permits two attained duties to be
> rerouted onto disjoint connected carriers.

It is not an `HC_7` counterexample and does not refute a dichotomy whose
second outcome is a coherent web/adhesion structure.  In fact it is the
atomic coherent cyclic-web outcome that such a dichotomy must retain.

For Lemma 4.1 itself the verdict is split:

* the positive nonalternating-arc construction is **GREEN** for an actual
  cycle with six mutually distinct selected portals;
* uniqueness of the cyclic word `A B D A B D` is **GREEN** under the same
  hypothesis; and
* the stated infinite-family extension is **GREEN only for subdivisions
  and pendant, single-attachment portal-free trees**.  It would be false if
  "attached trees" were allowed two or more attachments on the cycle.

The phrase "two selected, pairwise distinct portal vertices for each of
three duties" should be read, or amended, to say that **all six** selected
portal vertices are pairwise distinct.  Pairwise distinctness merely within
each duty would not support the cyclic-word proof.

## 1. The boundary state is literal

For the displayed Moser graph, each of

\[
 A=\{2,3\},\qquad B=\{1,4\},\qquad D=\{0,5\}
\]

is independent.  Together with the singleton `{6}` these form a proper
partition with four blocks.  Taking `C={6}` gives demand three.  The Moser
edges `62,61,65` show that the retained singleton already sees every one of
the three nonsingleton blocks, so the duties are exactly `A,B,D`.

This check is partition-dependent; it does not appeal to carrier defect.

## 2. Duty-specific portal freedom does not remove the example

The packet is the six-cycle `u_0...u_5u_0`.  Each of the six literal duty
labels has exactly one neighbour in the packet:

\[
 2\mapsto u_0,\ 1\mapsto u_1,\ 0\mapsto u_2,\
 3\mapsto u_3,\ 4\mapsto u_4,\ 5\mapsto u_5.
\]

Thus the current duty-specific convention still forces precisely the
three terminal pairs

\[
 A:\{u_0,u_3\},\qquad
 B:\{u_1,u_4\},\qquad
 D:\{u_2,u_5\}.
\]

The extra edge from `6` to `u_0` makes the packet `S`-full but does not
alter any of these duties.  Hence this is not a false collision caused by
reusing a portal for a shared label.

## 3. Every selected packet tree has a bypassed gate

A tree in the six-cycle containing all six forced witnesses is a spanning
tree and therefore is obtained by deleting one cycle edge.  The terminal
pairs for every two duties alternate cyclically.  On the resulting path,
the three pair hulls are intervals which meet pairwise, hence have a common
vertex by interval Helly.

Neither endpoint of the path can be common to all three hulls: each endpoint
is the private terminal of only one pair, while the other two pair intervals
end before reaching it.  The omitted cycle edge is a literal tree bridge;
its attachment-to-attachment tree path is the whole spanning path.  It
therefore bypasses every possible common gate.

## 4. No label-compatible local rerouting exists

A connected carrier for a duty must contain both of its two forced portal
vertices.  For two alternating pairs on a cycle, every connected subgraph
containing one pair meets every connected subgraph containing the other:
each of the two arcs joining the first pair contains a terminal of the
second.  This applies to all three duty pairs.  Consequently changing the
spanning tree, using the omitted edge, or choosing larger connected
subgraphs of the packet never yields two disjoint duty-correct carriers.

The classification in Lemma 4.1 is also correct for six mutually distinct
portals on an actual cycle.  Three two-element portal pairs are mutually
alternating precisely when their cyclic word is, up to rotation, reversal,
and duty renaming,

\[
                            A\,B\,D\,A\,B\,D.
\]

If a pair is nonalternating, disjoint arcs for those two pairs can be
extended through a portal-free gap until adjacent, supplying the two
carriers used by the attained-duty split theorem.

Subdividing cycle edges does not affect either argument.  Attaching a
portal-free tree at one cycle vertex is also harmless: any excursion into
the tree returns through the same attachment and cannot link alternating
terminal pairs.  A tree with two cycle attachments is different; it is a
chord-like bypass and may permit disjoint carriers despite the alternating
cyclic order.  Thus the note's final infinite-family sentence needs the
single-attachment qualification and should not be read as a statement for
arbitrary multi-attachment bridges.

## Exact consequence

The positive gate theorem and this negative certificate fit exactly:

* disjoint duty hulls reflect the attained state;
* a mere topological bypass does not force such hulls; and
* the surviving obstruction is a labelled width-two cyclic web order.

Any valid strengthening must use the second packet and the ambient
seven-connected contraction-critical graph to turn that web order into a
common equality-state adhesion, a literal `K_7`, or the fixed-pair
`K_5`-minor-free endgame.  The local packet alone cannot do so.
