# Elimination of every two-cut in the pure-Moser four-plus-one cell

## Statement

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(d(v)=7\), and suppose

\[
G-N[v]=C_1\mathbin{\dot\cup}C_2,
\qquad G[N(v)]\cong M,
\]

where \(M\) is the pure Moser spindle with the fixed numerical labelling

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Use the exact trace with repeated pair \(13\), and suppose that \(C_1\)
supports four edges of the missing pentagon while \(C_2\) is the selected
minority component.  Then

\[
\boxed{C_2\text{ has no two-vertex cut}.}
\]

Together with the support-independent global cutvertex theorem, this says
that every surviving minority component has no vertex separator of order
one or two.  In particular, if it has at least four vertices, it is
3-connected.

## Proof

The four-plus-one closures first reduce the physical minority edge to

\[
f\in\{25,24,46\}.
\]

Suppose that \(C_2\) has a two-cut.  Split it in the standard way into
two disjoint, connected, adjacent shores.  Seven-connectivity gives each
shore boundary defect of order at most two, and the two defects are
disjoint.

The exact quotient-model calculation in Lemma 5.2 of
`hadwiger_moser_4plus1_closures.md` says that, unless \(G\) already has a
\(K_7\)-minor, the unordered defect pair belongs to the following table:

\[
\begin{array}{c|l}
25&
[2|35],[5|12],[02|35],[05|12],[12|35],[12|45],
[12|56],[16|34],[24|35],[24|56],[26|35]\\[1mm]
24&
[2|34],[4|12],[02|34],[04|12],[12|34],[12|45],
[12|46],[16|35],[25|34],[25|46],[26|34]\\[1mm]
46&
[4|16],[6|34],[04|16],[06|34],[12|35],[16|24],
[16|34],[16|45],[24|56],[26|34],[34|56].
\end{array}
\]

On the other hand, the support-independent global two-cut theorem in
`hadwiger_moser_global_2cut_closure.md` applies to either exterior
component.  Its ten-vertex quotient uses the two split shores together
with the other, full-attachment exterior component.  It says that a
\(K_7\)-minor exists unless the same unordered defect pair is

\[
\{13,24\}\quad\text{or}\quad\{14,23\}.
\]

Neither exceptional pair occurs in any row of the displayed 33-pair
table.  Thus the assumed two-cut gives a \(K_7\)-minor in all cases, a
contradiction.  Hence \(C_2\) has no two-cut. \(\square\)

## Audit boundary

The conclusion is not a heuristic comparison of independently chosen
separations.  Both quotient lemmas apply to the same standard split of
an arbitrary selected two-cut, and both record the exact aggregate
boundary defects of those two shores.  Therefore their residual tables
may legitimately be intersected.

The global quotient lift has also been checked directly: replacing each
shore vertex by its connected shore preserves bag connectivity and every
bag adjacency, every quotient bag meets \(N\), and adding \(\{v\}\)
supplies the seventh branch set.

The two global quotient exceptions are themselves eliminated by the
complementary-defect colour-gluing lemma in
`hadwiger_moser_global_2cut_exceptions_closed.md`.  Thus the absence of a
two-cut is now support-independent; the table intersection above remains
a shorter independent proof for the selected four-plus-one cell.

## Remaining two-component obstruction

This closes the entire 33-case two-cut family.  It does **not** close the
pure-Moser two-component cell.  What remains includes:

* four-plus-one minority components with no cut of order at most two;
* the balanced support families \(1122B\) and \(112B2\); and
* the support-independent case in which both exterior components are
  internally 3-connected (when they have at least four vertices).
