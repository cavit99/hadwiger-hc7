# Limits of the abstract pure-Moser boundary-state system

## Result

The explicit certificate in `moser_all_trace_state_certificate.py` proves
that the currently derived abstract state axioms are jointly consistent
across **all ten** accessible repeated-pair traces of the pure Moser
spindle.  This remains true under the strongest local conclusions proved
in `hadwiger_moser_pentagon_boundary_lemma.md`:

* the \(05\)- and \(06\)-rows are forced to the exceptional binary
  alternating patterns on their disjointness \(C_6\)'s; and
* every other repeated-pair row contains a bi-supported edge.

Thus the abstract extension/support layer is saturated: it cannot by
itself eliminate the pure-Moser cell.

## Axioms checked

The dependency-free verifier checks exactly the following.

1. The two side families of double and triple matching states are
   disjoint.
2. For every double matching \(\{r,e\}\), each side contains either that
   double state or a triple matching extending it.  This is the full
   two-anchor coverage condition, for all 26 double matchings.
3. In every exact singleton trace \(r\), each missing edge on the five
   unique roots is supported by at least one side.
4. Neither side supports every missing edge in any row; otherwise the
   confined Kriesell--Mohr model already gives \(K_7\).
5. If a side does not support \(e\), it contains the double state
   \(\{r,e\}\).
6. If two vertex-disjoint missing edges are both unsupported by a side,
   the commuting swaps force the corresponding triple state on that side.
7. Rows \(05,06\) are binary, while each of the other eight rows has a
   bi-supported edge.

The no-reversal consequence is implicit: if a double state belongs to one
side, state disjointness and item 5 force the reverse trace to support the
opposite direction on the other side.

## What the certificate does not assert

This is an abstract finite certificate, not a pair of boundaried graphs.
In particular, it does **not** encode or claim:

* simultaneous realizability of the extension families by actual
  six-colourings of graphs;
* consistency between the different chosen exact-trace colourings beyond
  the listed state implications;
* Kempe switches involving the repeated colour;
* the geometry or intersections of the bichromatic paths, except for the
  two disjoint swaps used in item 6;
* seven-connectivity, degree constraints, or exclusion of a \(K_7\)-minor;
* the new boundary state created after every internal vertex/edge deletion
  or contraction.

Therefore it does not refute the desired graph-theoretic lemma.  It proves
that any successful continuation must use at least one of the omitted
geometric or one-step-minor-critical inputs.
