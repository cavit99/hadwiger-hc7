# The seven-vertex coloured two-cycle barrier

## Exact object

Keep the two cyclic orders

\[
 C=(0,1,2,3,4,5,6),\qquad
 D=(0,1,4,6,5,2,3)
\]

and the colour map

\[
 0,1\mapsto A,\quad 2,3\mapsto B,\quad
 4,5\mapsto C,\quad 6\mapsto D.
\]

Equivalently the colours in numerical order are `AABBCCD`.

The cycles have different dihedral orders, so the audited rural-cycle
exchange returns crossing independent `D`-edges relative to `C`.  However,
**no such crossing pair has one endpoint of each colour**.  The complete
list is

\[
\begin{array}{c|c}
\text{crossing pair}&\text{endpoint colours}\\ \hline
14,52&ACCB\\
14,30&ACBA\\
46,52&CDCB\\
52,30&CBBA.
\end{array}
\]

Thus the tempting coloured strengthening

> a mismatch of two boundary cycles automatically returns a crossing
> pair with four differently labelled ends

is false.  A proof needing four prescribed row labels must use a further
exchange, choose roots after seeing the subdivision, or exploit contacts
inside the rooted bags; the uncoloured cyclic-order theorem alone does not
supply the label diversity.

## Trust boundary

This example does **not** say that the union lacks every rainbow rooted
`K4`.  In fact seven of the eight choices of one representative from each
of `A,B,C,D` are rootable.  The sole nonrootable transversal is
`{0,2,5,6}`.  The barrier is exactly to extracting four distinct colours
as the endpoints of the two crossing `D`-edges.

The exhaustive certificate is
`hc7_colored_two_cycle_rainbow_barrier_verify.py`.
