# Closure of the three-connected high-owner (C_6) shore

## 1. Statement

Use cyclic missing-edge labels \(c_0,\ldots,c_5\), universal boundary
vertex \(z\), and the two full shores \(D_1,D_2\). A frame \(i\) asks
for disjoint realizations of

\[
 e_{i-2}=c_{i-2}c_{i-1},qquad
 e_{i+2}=c_{i+2}c_{i+3}.
\]

Opposite frames are (i,i+3).  The ownership theorem assigns every
opposite pair to one shore, so one shore owns at least two such pairs.

### Theorem 1.1

In a seven-connected, minimum-degree-seven, \(K_7\)-minor-free
realization, the high-owner shore is not three-connected.

Consequently every remaining (C_6\dot\cup K_1) realization has a
two-cut in its high-owner shore.

## 2. Reduction to one common face

Orders four and five are excluded by
`hadwiger_c6_portal_multiplicity_closure.md`.  Hence the high-owner shore
\(D\) has order at least six and its six portal sets

\[
 P_i=N_D(c_i)
\]

have a system of distinct representatives (b_i\in P_i).

Suppose \(D\) is three-connected. The three forbidden antipodal
two-linkages (e_i\mid e_{i+3}), (i=0,1,2), give three bare four-web
embeddings.  Whitney uniqueness puts their represented portal sets on
faces

\[
\begin{aligned}
F_0&\supseteq P_0\cup P_1\cup P_3\cup P_4,\\
F_1&\supseteq P_1\cup P_2\cup P_4\cup P_5,\\
F_2&\supseteq P_0\cup P_2\cup P_3\cup P_5.
\end{aligned}                                       \tag{2.1}
\]

The face-intersection argument in
`hadwiger_c6_simultaneous_prism_web.md` proves that these faces coincide.
For completeness, if exactly two coincide, four portal classes lie in
the intersection of two distinct faces, of order at most two; those two
vertices together with the other two boundary labels and (z) form a
cut of order at most five.  If all three faces are distinct, their
pairwise intersections contain the three opposite portal pairs.  Unless
(|D|\le5), seven-connectivity forces three disjoint intersection edges,
whose three facial cycles form a subdivided prism.  Any subdivision or
cap interior lies behind at most three rung endpoints plus (z), and is
therefore impossible.  The unsubdivided prism has internal degree three
and at most the two portal labels on its rung plus (z), giving total
degree at most six.  Thus (2.1) has one common face (F).

This argument uses the full portal sets.  It does not identify witnesses
chosen by different frames.

## 3. Circular order with collapsed occurrences

The absence of each antipodal linkage implies the following elementary
disk rule:

> whenever four distinct vertices of (F) are chosen from the four
> portal classes of (e_i,e_{i+3}), they alternate on (F).

Otherwise two disjoint arcs of the facial cycle give that forbidden
two-linkage.  Applying the rule to the six distinct (b_i), their
cyclic label order is, up to rotation, one of

\[
\begin{array}{lll}
024153,&025314,&031524,\\
035142,&041352,&042513.
\end{array}                                         \tag{3.1}
\]

For every order in (3.1), facial arcs realize exactly one opposite pair
of frames.  Since (D) is high-owner, it owns another opposite pair.
Choose its two frame witnesses.  A connected witness for one missing
edge may meet its two portal classes at one vertex, so four distinct
portal occurrences may **not** be assumed.

The exact disk rule, including this degenerate case, is as follows.  Let

\[
 a\in P_i,\quad b\in P_{i+1},\quad
 c\in P_{i+3},\quad d\in P_{i+4}.                  \tag{3.2}
\]

If the two supports \(\{a,b\}\) and \(\{c,d\}\) are disjoint, then
absence of an \(e_i\mid e_{i+3}\) linkage forces

\[
 a\ne b,\qquad c\ne d,
 \qquad a,b,c,d\text{ alternate on }F.            \tag{3.3}
\]

Indeed, if all four points are distinct and do not alternate, the two
appropriate arcs of the facial cycle are disjoint and give the
linkage.  If, say, \(a=b=x\), then \(\{x\}\) is one connected branch
piece.  Since \(c,d\ne x\), one of the two \(c\)-\(d\) arcs of the
facial cycle avoids \(x\) (and if \(c=d\), use the singleton
\(\{c\}\)).  This again gives the forbidden linkage.  The case
\(c=d\) is symmetric.  Thus (3.3), rather than a four-distinct-points
rule, is the exact necessary condition.

### Lemma 3.1 (exact circular-occurrence lemma)

No circular occurrence system can simultaneously satisfy:

1. one of the six SDR orders (3.1);
2. witnesses for a second opposite frame pair, allowing either path
   piece to have its two portal occurrences coincide;
3. the full disk rule (3.3) for every selected occurrence choice of
   each antipodal demand whose two pair-supports are disjoint.

### Certificate and audit

`c6_circular_witness_degenerate_smt.py` encodes exactly these finite
order types.  There are six orders and two choices of the additional
opposite pair, so it checks twelve instances.  All twelve are
unsatisfiable.

The encoding gives every one of the fourteen selected occurrences an
integer circular position.  It imposes inequalities only between the
two disjoint path pieces of a frame; occurrences within one piece may
coincide.  A frame witness is therefore allowed whenever one piece
collapses, or, with four distinct attachments, when its two pairs do
not alternate.  For each antipodal demand the program universally
checks all selected occurrence choices and imposes the full implication
(3.3), including its noncollapse conclusion.  Coincidences between
different frame witnesses and coincidences with SDR representatives are
left unrestricted unless disjointness or (3.3) forbids them.

For comparison, `c6_circular_witness_smt.py` also returns UNSAT in all
twelve cases after adding the stronger singleton-row consequences from
the exact two-piece atlas.  Its `--raw-overlap` mode is only the
deliberately weakened *four-distinct-occurrence* encoding; a SAT model in
that mode exploits a collapsed pair and violates the facial-arc argument
above.  It is not a geometric counterexample and is not used here.

## 4. Conclusion

The SDR facial arcs give one opposite frame pair, ownership gives a
second, and Lemma 3.1 says those data cannot coexist with the three
antipodal exclusions and the exact disk rule.  This
contradiction proves Theorem 1.1.

The result is deliberately limited to a three-connected high-owner
shore.  A merely two-connected shore can flip its three web embeddings
independently across its two-cuts.  The exact two-cut theorem says each
such cut has exactly two components; the remaining task is to align or
eliminate those Yu-ladder/rope flips.
