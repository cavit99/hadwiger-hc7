# The concentrated two-defect cell is a pentagonal-bipyramid society

## Status

This note continues
`hc7_near_k7_two_defect_cut_closure.md`.  It proves that the sole
concentrated-portal residue has one exact quotient: after deleting one
fixed pair of ordinary singleton vertices, it is an expansion of the
pentagonal bipyramid.  A rural expansion therefore gives a **global**
two-apex pair, while every label-noninterval connected split gives a
literal `K_7`.

The note does not yet prove that a nonrural society must have a
label-noninterval split.  Repeated portal occurrences or nonplanarity
inside the complex pole can obstruct rurality while every coarse label set
is an interval.  That is the remaining operation-sensitive part of P4.

## 1. The unique concentrated label

Retain the notation and hypotheses of
`hc7_near_k7_two_defect_cut_closure.md`.  Thus

\[
 S=\{b_s,b_t,q_1,q_2,q_3\},\qquad X=\{x_s,x_t\},          \tag{1.1}
\]

the rows of `x_s,x_t` are exactly (1.3) of that note, `B-X` is connected,
and the target-free branch of the audited palette-to-label theorem gives

\[
                         P_i=N_B(b_i)\subseteq X           \tag{1.2}
\]

for at least one singleton label `b_i`.  Put `R=B-X`.

### Theorem 1.1 (one ordinary label is concentrated)

If `G` is seven-connected and has no `K_7` minor, there is exactly one
label `q in O={q_1,q_2,q_3}` with

\[
                              P_q=X.                        \tag{1.3}
\]

Every other singleton label has a neighbour in `R`, and

\[
                    N_G(R)=X\cup\{v\}\cup(S-\{q\}).       \tag{1.4}
\]

In particular (1.4) is an actual exact seven-boundary separating `R`
from `q`.

#### Proof

The concentrated label in (1.2) cannot be `b_s`: the witness `x_s`
misses `b_s`, so concentration would give `P_s={x_t}`.  But `b_s` has
only its four clique neighbours in `S` outside `B` and is nonadjacent to
`v`; hence its degree would be five, contradicting seven-connectivity.
The case `b_t` is symmetric.  Thus a concentrated label belongs to `O`.
Both witnesses see every member of `O`, so its portal class is exactly
`X`.

Let

\[
                   T=\{q'\in O:P_{q'}=X\}.                 \tag{1.5}
\]

This set is nonempty.  The connected set `R` is anticomplete to every
member of `T`, so its neighbourhood is an actual separator and

\[
       N_G(R)\subseteq X\cup\{v\}\cup(S-T),
       \qquad |N_G(R)|\le 2+1+(5-|T|)=8-|T|.              \tag{1.6}
\]

Seven-connectivity forces `|T|=1` and equality throughout (1.6).  This
is (1.3)--(1.4).  \(\square\)

## 2. The literal `K_2 join C_5` neighbourhood

Write

\[
                     O-\{q\}=\{h_1,h_2\}.                 \tag{2.1}
\]

### Lemma 2.1 (pentagonal boundary)

The five vertices

\[
                         b_s,b_t,x_s,v,x_t                \tag{2.2}
\]

induce the cycle in that cyclic order.  Both `h_1,h_2` are complete to
this cycle and adjacent to one another.  The concentrated vertex `q` is
complete to all seven vertices in

\[
                N(q)=\{h_1,h_2,b_s,b_t,x_s,v,x_t\}.       \tag{2.3}
\]

Consequently

\[
                            G[N(q)]\cong K_2\vee C_5.       \tag{2.4}
\]

The connected set `R` is adjacent to every vertex of `N(q)` and is
anticomplete to `q`.

#### Proof

The cycle edges in (2.2) follow respectively from the clique `S`, the
row of `x_s`, the foot edge `x_sv`, the foot edge `vx_t`, and the row of
`x_t`.  The other five possible pairs are absent: `x_s` misses `b_s`,
`x_t` misses `b_t`, the apex misses both deficient singletons, and
`x_sx_t` is absent because the witnesses lie in one bipartition class.

The remaining assertions follow from the clique on `S`, the contact rows
of the witnesses and apex, and the exact boundary (1.4).  \(\square\)

Delete the fixed pair `h_1,h_2` and put

\[
                         J=G-\{h_1,h_2\}.                  \tag{2.5}
\]

Contracting `R` in `J` gives the pentagonal bipyramid

\[
                            C_5\vee\overline{K_2},          \tag{2.6}
\]

whose two nonadjacent poles are `q` and the contraction image of `R`.

## 3. A label-noninterval split gives `K_7`

Label the cycle (2.2) by `0,1,2,3,4` in cyclic order.  For a connected
set `Y subseteq R`, put

\[
             \Lambda(Y)=\{i\in\mathbb Z_5:Y\text{ has an edge to }i\}.
                                                                  \tag{3.1}
\]

A subset of the five-cycle is a **cyclic interval** if its vertices occur
consecutively around the cycle; the empty and full sets count as
intervals.

### Lemma 3.1 (five-cycle split certificate)

Suppose

\[
                         R=A\mathbin{\dot\cup}D             \tag{3.2}
\]

where `A,D` are nonempty, connected and adjacent.  If either
`Lambda(A)` or `Lambda(D)` is not a cyclic interval, then `G` contains a
`K_7` minor.

#### Proof

By symmetry interchange `A,D` and rotate or reflect the five-cycle so
that `Lambda(A)` has one of the following two forms.  These are the only
noninterval subsets of a five-cycle up to dihedral symmetry:

\[
                         \{0,2\},\qquad \{0,2,3\}.          \tag{3.3}
\]

In the first case, fullness of `R` to the cycle makes `D` adjacent to
`1,3,4`; in the second it makes `D` adjacent to `1,4`.  Additional
contacts only help.

In either case the following five bags form a `K_5` model rooted at the
five cycle vertices:

\[
                  \{0\},\quad \{1\},\quad
                  \{2\}\cup A,\quad \{3,q\},\quad
                  \{4\}\cup D.                            \tag{3.4}
\]

They are connected and disjoint.  For completeness, the pairs not already
joined by a cycle edge are joined as follows: `0` sees `A`, `1` sees
`D`, the pole `q` sees every cycle root, and `A` sees `D` by (3.2).
In the three-element case, the extra `A-3` edge only adds an adjacency.

Each of the two singleton vertices `h_1,h_2` is adjacent to every bag in
(3.4), because every bag contains its named cycle root and both hubs are
complete to the cycle.  The hubs are adjacent to one another.  Adding
`{h_1},{h_2}` to (3.4) gives seven literal clique bags.  \(\square\)

Thus every connected split in a target-free concentrated cell has cyclic-
interval label sets on both shores.

## 4. The coherent rural output uses one fixed pair

Consider the expansion society of the connected pole `R` in the planar
quotient (2.6).  Its boundary occurrences are all edges from `R` to the
five cycle vertices, in the cyclic order `0,1,2,3,4` induced by the
pentagonal-bipyramid embedding.  Repeated occurrences at one label are
retained.

### Theorem 4.1 (rural concentration gives a fixed two-apex pair)

If this full expansion society is rural in the indicated rotation, then

\[
                            G-\{h_1,h_2\}\text{ is planar}. \tag{4.1}
\]

#### Proof

Draw the pentagonal bipyramid (2.6) in the plane, remove a small disk
around its `R`-pole, and insert the rural drawing of `G[R]`, matching
every portal occurrence in its prescribed cyclic bundle.  The other pole
`q` is already a singleton and no `q-R` edge exists.  This draws every
edge of `J` from (2.5), proving (4.1).  \(\square\)

The apex pair `{h_1,h_2}` is determined by the unique concentrated label
`q`; it is not selected independently by different pieces.  Hence this
is already a P5-compatible rural output.

## 5. Exact remaining exchange

Theorems 1.1, 3.1 and 4.1 give the following complete chain except for one
operation-sensitive implication:

\[
 \boxed{
 \begin{array}{c}
 \text{two-defect portal concentration}\cr
 \Downarrow\cr
 \text{one fixed pentagonal-bipyramid society}\cr
 \Downarrow\cr
 K_7\text{ from any label cross, or the fixed pair }\{h_1,h_2\}
 \text{ from rurality.}
 \end{array}}                                             \tag{5.1}
\]

What is not proved is

\[
 \text{nonrural full society}
    \quad\Longrightarrow\quad
 \text{a connected split with a label-noninterval shore}. \tag{5.2}
\]

The implication can fail for an arbitrary society because several portal
occurrences of one label may interleave, and because nonplanarity can lie
entirely inside `R`.  A valid proof of (5.2) here must use the
seven-contraction-critical operation states.  Equivalently, it must show
that the first nonrural ear either creates the split of Lemma 3.1 or gives
the same marked state on the two sides of its actual exact-seven boundary.

No further choice of an apex pair remains in this cell.
