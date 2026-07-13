# Global two-cut closure for the two-component pure-Moser cell

## Theorem

Use the hypotheses and labelling of
`hadwiger_moser_global_cutvertex_closure.md`.  Suppose one exterior
component has a two-vertex cut.  Then $G$ contains a $K_7$-minor.

The quotient part of the proof first reduces to the two unordered
boundary-defect pairs

\[
\boxed{\{13,24\}\quad\text{or}\quad\{14,23\}.}       \tag{1}
\]

Here, for example, $\{13,24\}$ means that one shore misses boundary
vertices $1,3$ and the other misses $2,4$.  Both pairs are subsequently
eliminated by complementary-defect colour gluing.  The theorem is
independent of the selected exact trace and support word.

## Proof

The global cutvertex theorem lets us assume that the split component has no
cutvertex.  Let $\{z_1,z_2\}$ be a two-cut and let $D$ be one component
behind it.  Every component of the deletion meets both cut vertices;
otherwise one cut vertex alone would disconnect the exterior component.
Put

\[
J_1=D\cup\{z_1\},\qquad J_2=C_1-J_1.
\]

Then $J_1,J_2$ are disjoint, connected and adjacent.  Seven-connectivity
and

\[
N_G(D)\subseteq N\cup\{z_1,z_2\}
\]

give at least five boundary attachments for $J_1$; a second component
behind the cut gives the same bound for $J_2$.  Thus their defect sets
$\Delta_1,\Delta_2$ have order at most two.  They are disjoint because
$J_1\cup J_2=C_1$ and $N_G(C_1)=N$.

The other exterior component $C_2$ is connected and meets all seven
boundary vertices.  Contract $J_1,J_2,C_2$ to shore vertices
$h_1,h_2,h_3$, retaining $h_1h_2$, their exact boundary contacts, and
the Moser graph on $N$.  Every $N$-meeting $K_6$-model in this
ten-vertex quotient lifts to $G-v$; adding $\{v\}$ then gives $K_7$.

There are 29 possible defect sets of order at most two and 260 unordered
disjoint pairs.  The dependency-free verifier
`moser_global_2cut_verify.py` exhausts every used vertex subset of the
ten-vertex quotient and every partition into six nonempty bags.  It checks
that every bag meets $N$, is connected, and is adjacent to the other five
bags.  A model exists for 258 defect pairs.  The only quotient failures
are exactly (1).

It remains to exclude those two failures.  The complete expansion audit is
given in `hadwiger_moser_global_2cut_exceptions_closed.md`; the argument is
summarized here.  Orient the shores as $A,B$, with defects $r,e$,
respectively, where

\[
(r,e)=(13,24)\quad\hbox{or}\quad(14,23).
\]

In either case $N-(r\cup e)=\{0,5,6\}$, whose only internal Moser edge is
$56$.  Contracting $\{v\}\cup r$ and $C_2\cup e$ produces on the
split-component side exactly one of the three boundary states

\[
\{r,e\},\qquad\{r,e,05\},\qquad\{r,e,06\}.             \tag{2}
\]

On the other side, contract $A\cup e$, $B\cup r$, and, respectively,

\[
\{v,0\},\qquad\{v,0,5\},\qquad\{v,0,6\}.
\]

The resulting boundary blocks form a $K_5$, $K_4$, and $K_4$,
respectively, so these three proper minors force each of the exact states
in (2).  Select the state produced on the first side, align the matching
state on the second, glue the two anticomplete exterior components, and
colour $v$ with a colour absent from $N$.  This contradicts
$\chi(G)=7$ and eliminates (1). \(\square\)

## Corollary

Together with the global cutvertex theorem, neither exterior component has
a vertex separator of order one or two.  Thus every exterior component of
order at least four is 3-connected.  In particular, all 33 two-cut pairs
from the selected four-plus-one trace are eliminated, and the same
conclusion applies to the balanced support families.
