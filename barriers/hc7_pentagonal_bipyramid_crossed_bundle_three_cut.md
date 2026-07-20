# A crossed two-column expansion can stop at a three-cut

**Status:** barrier/counterexample to an intermediate structural claim;
computer-checked by
[`hc7_pentagonal_bipyramid_crossed_bundle_three_cut_verify.py`](hc7_pentagonal_bipyramid_crossed_bundle_three_cut_verify.py).

This nine-vertex example shows that two individually nonalternating column
splits can be coupled across their common quotient edge to produce a
nonplanar, `K_5`-minor-free graph.  The obstruction is an exact three-cut.
It therefore supports, rather than refutes, the four-connectivity hypothesis
in the four-portal column theorem.

## Claim refuted

The following intermediate assertion is false.

> Replace two adjacent vertices of the pentagonal bipyramid by adjacent
> pairs.  Suppose neither replacement has a four-label alternating split.
> If the two pairs are joined crosswise, then the resulting graph is planar
> or contains a `K_5` minor.

The conclusion can fail even when every old quotient adjacency is retained.

## Construction

Write the pentagonal bipyramid as

\[
 P=C_5\vee\overline {K_2},
\]

with poles `p,q` and rim `c_0,c_1,c_2,c_3,c_4` in cyclic order.  Replace
the adjacent vertices `p,c_0` by the edges

\[
 p_0p_1,\qquad c_{00}c_{01}.
\]

Distribute the old neighbours as follows:

\[
\begin{array}{c|cc}
 &\text{first clone}&\text{second clone}\\ \hline
p&c_1,c_2,c_3&c_4\\
c_0&c_1,q&c_4.
\end{array}
\]

Join the two split columns crosswise by the edges

\[
                         p_0c_{01},\qquad p_1c_{00}.
\]

Keep every edge among the five unsplit old vertices.  Thus the complete
edge set is

\[
\begin{aligned}
\{&p_0p_1,c_{00}c_{01},p_0c_{01},p_1c_{00},\\
  &p_0c_1,p_0c_2,p_0c_3,p_1c_4,\\
  &c_{00}c_1,c_{00}q,c_{01}c_4,\\
  &c_1c_2,c_2c_3,c_3c_4,qc_1,qc_2,qc_3,qc_4\}.
\end{aligned}
\]

At `p`, the cyclic incidence word is

\[
                      (*,0,0,0,1),
\]

where `*` means that the old neighbour `c_0` is represented on both sides.
At `c_0` the word is

\[
                      (0,*,1,0).
\]

Neither word has four distinct old labels alternating between the two
clones.

The verifier checks that the resulting graph (graph6 string `H|do]CL`) is
nonplanar and has no `K_5` minor.  It has connectivity exactly three, and

\[
                         \{p_0,c_4,c_{00}\}
\]

is a three-cut.  Its deletion leaves the three components

\[
             \{c_1,c_2,c_3,q\},\qquad \{p_1\},\qquad\{c_{01}\}.
\]

## Trust boundary

This graph is not four-connected and is not claimed to occur as the full
core of a hypothetical `HC_7` counterexample.  It does not refute the
four-connected portal-rank dichotomy, a theorem with a cut outcome, or a
theorem using contraction-critical colourings.  It shows only that crossed
coupling of two locally nonalternating split columns is not by itself a
`K_5` certificate: a quotient three-separation is a genuine third outcome.
