# Elimination of the order-five one-component pure-Moser cell

## 1. The finite theorem

### Theorem 1.1 (computer-assisted)

Let \(G\) be a finite simple graph with a vertex \(v\) such that

\[
d(v)=7,\qquad
E(G[N(v)])=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Suppose \(G-N[v]=C\) is connected, \(|C|=5\),
\(\delta(G)\ge7\), and \(\kappa(G)\ge7\).  Then \(G\) contains a
\(K_7\)-minor.

This theorem assumes only the displayed local graph, minimum degree, and
connectivity.  It is therefore stronger than the corresponding
minor-critical-counterexample statement.

Together with the independently certified order-four theorem in
`hadwiger_moser_one_component_c4.md`, it gives the new residual bound

\[
\boxed{|C|\ge6} \tag{1.1}
\]

for a sole exterior component behind a pure-Moser neighbourhood in a
hypothetical \(\mathrm{HC}_7\) counterexample.

## 2. Exhaustive encoding

There are exactly 21 connected unlabelled graphs on five vertices.  For
each type of \(C\), all 35 possible edges between \(C\) and the seven
vertices of \(N(v)\) are Boolean variables.  All other edges are fixed:
the Moser edges inside \(N(v)\), the seven edges from \(v\) to its
neighbourhood, the chosen edges inside \(C\), and no edges from \(v\) to
\(C\).

The base system imposes the necessary conditions

* \(\delta(G)\ge7\); and
* every boundary vertex has a neighbour in \(C\).

The second condition follows from \(\kappa(G)\ge7\), but is included
explicitly.  The lazy certificate generator then adds only clauses which
are necessary for a seven-connected, \(K_7\)-minor-free graph:

1. a cut clause records a cut of order at most six and requires some
   optional edge between two components left by that cut; or
2. a minor clause records seven explicit disjoint connected pairwise
   adjacent bags and requires at least one optional witness edge of that
   model to be absent.

The resulting Boolean system is unsatisfiable for every graph type.

## 3. Shards and independent verification

The 21 certificates are archived in four shards:

* `moser_c5_certificate_0-1-2-3-4-5.json`;
* `moser_c5_certificate_6-7-8-9-10.json`;
* `moser_c5_certificate_11-12-13-14-15.json`; and
* `moser_c5_certificate_16-17-18-19-20.json`.

Their clause counts, in graph-atlas order, are

\[
\begin{split}
&(82,163,383,240,433,538,562,1031,673,641,987,\\
&\qquad1462,1589,890,873,1337,2235,1956,2584,2746,4069).
\end{split} \tag{3.1}
\]

`moser_c5_verify.py` is independent of the model-search routine.  It:

1. independently enumerates the 21 connected order-five graph-atlas
   types;
2. checks that every type occurs exactly once, with the exact archived
   case ID and edge set;
3. verifies every recorded cut clause from its partition and every minor
   clause from its seven branch sets;
4. reconstructs each final Boolean system and checks that it is
   unsatisfiable.

Thus the computation is checkable from explicit local certificates; it is
not merely a report that a graph generator found no example.

## 4. Remaining gap

The finite theorem completely eliminates \(|C|=5\), but it does not
address \(|C|\ge6\).  At larger orders one can still use the
one-component part of the proper-minor transition argument: an internal
deletion or contraction produces a higher boundary state extending the
modified exterior.  The opposite-side membership conclusion of
`hadwiger_two_side_minor_transition.md` is, of course, unavailable when
there is only one exterior component.  Bridge-switch geometry remains the
intended non-enumerative route.
