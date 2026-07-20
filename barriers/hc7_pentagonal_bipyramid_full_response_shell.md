# A full five-response shell on the pentagonal bipyramid

**Status:** barrier/counterexample to a labelled-shell response-coupling
claim; computer-checked by
[`hc7_pentagonal_bipyramid_full_response_shell_verify.py`](hc7_pentagonal_bipyramid_full_response_shell_verify.py).
The shell is only two-connected and four-colourable.  It is not a
counterexample to `HC_7` or to a theorem that uses seven-connectivity and
universal operation-specific nonextendability.

## 1. The claim refuted

The following static package does not force a `K_7` minor:

1. seven paired columns with adjacent roots and pentagonal-bipyramid contact
   graph;
2. five injectively labelled first-hit columns at each of two centres;
3. all five double-contraction response types, including opposite exclusive
   responses and one response joining both sides; and
4. a literal noncommutation edge for every oppositely exclusive pair.

Thus the five response colours, literal endpoint ownership and all pairwise
noncommutation witnesses still do not align four distinct column labels.

## 2. The canonical shell

Let the column labels be

\[
 {cal C}=\{A_0,A_1,R_0,R_1,R_2,R_3,R_4\},
\]

where `A_0,A_1` are the nonadjacent poles of the pentagonal bipyramid and
`R_0...R_4` form its rim cycle.  Take vertices `p,v,w`.  Join `p` to `v,w`.
For every `q in C`, take a three-vertex column

\[
                  v_q-h_q-w_q
\]

and add the edges `vv_q` and `w_qw`.  Join `h_q,h_r` precisely when `qr` is
an edge of the pentagonal bipyramid.

Let

\[
                         P=\{A_0,R_0,R_1\}.
\]

For every `q in P`, add `pv_q` and `pw_q`.  Finally, add all four edges

\[
             v_qw_r\qquad(q,r\in\{A_1,R_2\}).
\]

These four edges lie within one column or between two columns already
adjacent in the pentagonal bipyramid.  Hence the contact graph remains
exactly the pentagonal bipyramid.

## 3. Five exact response types

Delete `pv,pw`.  The verifier gives a proper six-colouring with

\[
                         c(p)=c(v)=c(w)=0.
\]

For colours `1,...,5`, use the first-hit maps

\[
\begin{aligned}
 f_v&=(A_1,R_2,A_0,R_0,R_1),\\
 f_w&=(A_0,R_0,A_1,R_2,R_1).
\end{aligned}
\]

Both maps are injective, and the chosen vertices `v_{f_v(i)}` and
`w_{f_w(i)}` have colour `i`.  In the `0,i` subgraph, the component of `v`
has the following exact incidence with `p,w`:

\[
\begin{array}{c|ccccc}
i&1&2&3&4&5\\ \hline
\text{type}&X&X&Y&Y&Z\\
p\text{ in the component?}&0&0&1&1&1\\
w\text{ in the component?}&0&0&0&0&1.
\end{array}
\]

For every `X`-colour and every `Y`-colour, the corresponding exclusive
components have the displayed literal edge `v_qw_r`.  All four
noncommutation requirements are therefore present simultaneously.

Nevertheless the graph has no `K_7` minor.  The verifier checks this by an
exact seven-branch-set flow formulation.

## 4. The balanced-face obstruction

All contacts from `p` to the columns are concentrated in the facial
triangle `P={A_0,R_0,R_1}`.  The two `X` first-hit labels and the two `Y`
opposite first-hit labels lie in the edge `{A_1,R_2}` of another facial
triangle.  The forced noncommutation edges therefore add internal portal
geometry but no new edge to the column-contact graph.

This concentration is sharp for the current proof mechanism.  Four clean
contacts from one additional connected branch set to four distinct
pentagonal-bipyramid columns would be terminal: every four column labels
root a `K_4` minor in the pentagonal bipyramid, so those four rooted bags,
the additional branch set and the two fixed roots would form a `K_7`
model.  The shell evades that closure with exactly three contact labels.

## 5. Trust boundary

The shell is a finite labelled obstruction, not a candidate host graph for
`HC_7`.  It is two-connected and four-colourable.  Its two deleted edges
and its six-colouring encode the local double-response calculation, but the
graph does not satisfy seven-chromaticity, seven-connectivity, or the
requirement that every proper minor of a hypothetical counterexample be
six-colourable while the original graph is not.

Accordingly the live theorem must use at least one genuinely host-level
ingredient to break the balanced-face concentration: an order-seven
compatible separation, a strict operation-selected descent, or a further
minor-critical response which forces a fourth clean column label.  Static
five-colour response incidence and pairwise noncommutation are insufficient.
