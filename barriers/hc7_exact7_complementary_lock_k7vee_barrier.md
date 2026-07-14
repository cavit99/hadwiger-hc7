# Complementary-lock static `K_7^\vee` barrier

**Status:** exact finite counterexample quotient, with a dependency-free
verifier.  This note refutes only a boundary-independent static-minor
conclusion from the complementary-lock incidences; it is not asserted to be
a seven-connected host.

**Scope warning.**  This quotient deliberately contains only the rich-side
full packet `Q`; it omits the old thin-shore full packet `L` present in an
actual oriented `(1,2)` adhesion.  It therefore does **not** refute
`../results/hc7_exact7_complementary_lock_near_k7_handoff.md`.  That theorem
uses `L union B_1` as the missing fourth universal bag and proves that the
full actual lock does contain a spanning `K_7^vee` model.

Let

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad B_i=\{a_i,t_i\}.
\]

Take the boundary graph with exactly the six edges

\[
 ca_1,\ ca_2,\ ca_3,\ a_1a_2,\ a_1a_3,\ a_2t_3.       \tag{1}
\]

Thus each `B_i` is independent, `c` has a neighbour in every `B_i`, and
the last three edges in (1) witness all three inter-block adjacencies.

Add five quotient vertices `D,E,x,y,Q`.  Their exact neighbourhoods are

\[
\begin{aligned}
 N(D)&=\{x,y,c,t_1,t_2,a_3,t_3\},\\
 N(E)&=\{x,y,c,a_1,a_2,a_3,t_3\},\\
 N(Q)&=S.
\end{aligned}                                           \tag{2}
\]

There are no other edges.  In particular, `D,E` are the two raw lobes,
both attach to the two poles, `Q` is a disjoint full packet, and

\[
 \Delta(D)=\{a_1,a_2\},\qquad
 \Delta(E)=\{t_1,t_2\}.
\]

## Exact obstruction

This twelve-vertex graph has no `K_6` minor.  Consequently it has no
`K_7^\vee` minor, where `K_7^\vee` denotes `K_7` with two incident edges
deleted: the six vertices other than the common deficient vertex induce a
`K_6`.

The verifier `hc7_exact7_complementary_lock_k7vee_verify.py` checks the
claim exhaustively.  Completeness is short.  Any six connected branch bags
use some `u` of the twelve vertices.  Choose a spanning tree in every bag;
their union is a forest of

\[
                         m=u-6\in\{0,\ldots,6\}
\]

graph edges.  Exactly `6-m` vertices are unused, and none is incident with
the chosen forest.  Conversely, contracting any such forest and deleting
those `6-m` vertices gives exactly six connected bags.  The verifier
enumerates every choice and tests all fifteen bag adjacencies.  It checks,
for `m=0,\ldots,6`, respectively,

\[
 924,\ 6804,\ 31178,\ 102858,\ 240608,\ 358192,\ 252221
\]

forest/deletion candidates, and none contracts to a clique.

Hence the paired-triangle witnesses, the two complementary exact defects,
the two pole attachments, and one disjoint full packet do not by themselves
force a labelled or unlabelled `K_7^\vee` model.  This is only a reduced
one-packet obstruction.  In the actual `(1,2)` cell the second full packet
supplies exactly the missing resource, as the handoff theorem shows.
