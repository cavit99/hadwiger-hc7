# Exact-seven nonsplit exchange: closure through five defects

## Status

This round closes an infinite exact-adhesion family. It does not prove
\(HC_7\), but it replaces the induced-\(2K_2/C_4/C_5\) case split through
five defects by one structural theorem.

### Theorem 1 (five-defect full-adhesion closure)

Let \(G\) be seven-connected and let \(S\) be a seven-vertex cut such
that \(G-S\) has at least two components. Put

\[
                         F=\overline{G[S]}.
\]

If \(|E(F)|\le5\), then \(G\) contains a \(K_7\) minor or \(G\) is
six-colourable.

Consequently, if \(G\) is both non-six-colourable and
\(K_7\)-minor-free, every full exact seven-adhesion satisfies

\[
                         |E(F)|\ge6.                 \tag{1.1}
\]

### Proof

Seven-connectivity makes every component of \(G-S\) full to \(S\).
For at most four missing edges, Theorems 3.1 and 3.4 of
`hadwiger_exact_seven_two_gate_boundary_threshold.md` give an explicit
\(K_7\) model from two full shores.

For five missing edges, the exact labelled branch-set classification
`contact_order7_five_edge_verify.py` leaves precisely

\[
                  C_5\dot\cup2K_1,\qquad K_3\dot\cup2K_2.       \tag{1.2}
\]

Every other type has a \(K_7\) model after contracting two full shores.
If a third shore exists, Lemma 9.2 of
`hadwiger_contact_order7_threeedge_closure.md` gives explicit
\(K_7\) models for both graphs in (1.2).

It remains to consider exactly two shores. For the first graph in
(1.2), `hadwiger_c5_full_web_closure.md` proves that a crossing in
one shore gives a \(K_7\) model, while two crossless shore societies
glue to a planar graph after deleting the two universal boundary
vertices and hence give a six-colouring. For the second graph,
`hadwiger_k322_full_web_closure.md` proves the analogous statement:
a same-shore crossing gives a \(K_7\) model, while two crossless
four-webs glue to a planar graph after deleting three boundary vertices;
four colours on the planar part and two reusable new colours give a
six-colouring.

These alternatives exhaust (1.2), proving the theorem. \(\square\)

## 2. What happened to the induced nonsplit branches

Corollary 2.3 of the threshold note says that the missing graph of a
minor-critical full adhesion is nonsplit, and hence contains an induced
\(2K_2\), \(C_4\), or \(C_5\).

At the first two defect levels where this matters, the branches now have
a complete structural resolution:

* every four-edge missing graph, including all induced-\(C_4\) cells,
  closes by a static two-shore \(K_7\) model;
* at five edges, the only noncyclic survivor is
  \(K_3\dot\cup2K_2\), and its induced \(2K_2\) is exactly the
  four-terminal crossing frame;
* the cyclic survivor \(C_5\dot\cup2K_1\) is the coherent rural frame.

The web theorem is the reusable principle. A shore either contains a
labelled crossing, which repairs the missing boundary adjacencies and
lifts to \(K_7\), or all its portal routes admit one coherent disk order.
Seven-connectivity deletes every facial inserted clique, because its
neighbourhood has order at most six. Two coherent disks then glue, and
the few omitted boundary vertices form the apex colour budget.

Thus dirty or nested individual Kempe chains do not require separate
enumeration in these two cells: the simultaneous crossless state is
globally packaged as a web.

## 3. Exact limit of the Kempe-chain shortcut

The clean/dirty incidence theorem in
`hadwiger_exact7_kempe_trace_exchange.md` remains useful, but a pair
of clean connectors is not by itself a rooted-model theorem.

For the \(K_3\dot\cup2K_2\) boundary, add two nonadjacent full singleton
helpers. The paths

\[
                         1-h_1-2,\qquad3-h_2-4
\]

are disjoint and boundary-clean, but the resulting nine-vertex graph
has no \(K_7\) minor. Its connectivity is exactly six. The verifier
`exact7_split_clean_crossing_counterexample_verify.py` checks all
three assertions.

The missing condition is not path cleanliness; it is *capacity
coherence*. Both paths must form a crossing in one shore, or failure of
every such crossing must impose a common web order on the whole shore.
That is why the web argument succeeds where chain-by-chain Kempe
exchange stalls.

## 4. General rooted-model principle extracted

The proof uses the following label-free pattern.

### Crossing-or-coherent-apex principle

Let an exact adhesion have a cyclic terminal frame in each of two
anticomplete full shores.

1. If one auxiliary shore society has a crossing whose two routed
   demands admit the displayed boundary completion, the crossing and
   the opposite full shore form the target clique model.
2. If both societies are crossless, complete them on the same vertex
   sets to webs.
3. If every inserted facial clique would expose a cut smaller than the
   ambient connectivity, both webs are bare ribs.
4. If the two ribs have the same labelled frame, glue them. The graph
   becomes planar after deleting the fixed apex set.

This is a genuine uniform rooted-model dichotomy for the adhesion; it is
not specific to the internal order of a shore or to a chosen Kempe
colouring. The two sharp five-defect cores are its first complete
instances.

## 5. Remaining gap

The theorem advances the exact boundary threshold from five to six
missing edges. It does not say that every hypothetical \(HC_7\)
counterexample exposes an exact seven-cut, and it does not close all
six-edge or denser missing graphs. The next scalable task is therefore:

> classify which six-defect nonsplit frames admit a crossing completion
> and which crossless frames glue to a bounded-apex planar graph, while
> using the proper-minor state transition to eliminate any frame that
> is neither.

Any claim that the five-defect result alone proves \(HC_7\) would be
incorrect.
