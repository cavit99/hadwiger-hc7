# The three-face rooted obstruction is a three-edge bond with forced palette excursions

## 1. Setting

Use the all-full-deletion minimum atom of
`hadwiger_full_deletion_propagation.md`.  Thus `D` is a three-connected
minimum seven-fragment, every boundary portal class has order at least two,
and every edge of `D` carries the endpoint-complete deletion warehouse.

Choose the simultaneous portal SDR `p_0,...,p_5,p_z`.  Assume the three
antipodal-complement rooted-`K_4` views all fail inside one
three-connected planar torso and that Lemma 6.3 of the propagation note is
in its three-face outcome.  The three antipodal root pairs are

\[
              \{p_0,p_3\},\quad\{p_1,p_4\},\quad
              \{p_2,p_5\}.                         \tag{1.1}
\]

Each pair is the common edge of two of the three faces.

## 2. Duality produces an exact three-edge bond

### Lemma 2.1 (three-face bond)

The three edges in (1.1) form an edge bond

\[
                         \delta_D(X)=\{e_0,e_1,e_2\} \tag{2.1}
\]

for a connected bipartition `D=X dotcup Y`.  They are an independent
matching, and each side contains exactly one selected root from every
antipodal pair.

### Proof

In the planar dual, the three face vertices form a triangle, whose three
dual edges correspond to (1.1).  This dual triangle is not facial.  A
facial dual triangle would surround a primal vertex of degree three, while
every vertex of `D` has degree at least four by atomic surplus and the
singleton row bound.  In a three-connected plane graph, a nonfacial dual
cycle is separating; its primal edges form a bond.  Both bond shores are
connected by minimality of a bond.  The edges in (1.1) have six distinct
ends, so they form a matching and put one end of each antipodal pair on
each side.  QED.

### Lemma 2.2 (the bond is in the one-hole atlas row)

Put

\[
             d_X=S-N_S(X),\qquad d_Y=S-N_S(Y).      \tag{2.2}
\]

Then `|d_X|,|d_Y|<=2`.  If the two-piece quotient is negative, after
possibly reversing the shores there is `v in V(C_6)` such that

\[
             \{v\}\subseteq d_X,qquad
             d_Y=N_{C_6}(v),                       \tag{2.3}
\]

and `d_X` has order one or two.

Moreover, the three selected labels represented in `X` form one prism
triangle and those represented in `Y` form the other.

### Proof

The internal boundary of each shore consists of the three distinct ends
of the bond edges.  Atomic surplus gives at least five boundary contacts
on each side, proving the defect bound.

The low-defect two-piece atlas has only two negative forms: the one-hole
row (2.3), or `M_i|M_j` for two antipodal pairs.  Each shore contains a
selected root from every antipodal pair, so neither defect can contain an
entire `M_i`.  The second form is impossible, leaving (2.3).

The `Y`-root labels avoid `d_Y=N_{C_6}(v)`, while the `X`-root labels avoid
`v` (and the possible second member of `d_X`).  Since each side selects
one end of every antipodal pair, the unique forced transversal is

\[
 \{\bar v\}\cup N_{C_6}(v)quad\text{on }X,
 \qquad S-\bigl(\{\bar v\}\cup N_{C_6}(v)\cup\{z\}\bigr)
       \quad\text{on }Y,                            \tag{2.4}
\]

where `bar v` is antipodal to `v`; these are precisely the two prism
triangles.  QED.

The universal label `z` is not part of the selected triangle statement;
it may contact either or both shores.

## 3. Every deleted bond edge forces three boundary palettes

Let `e_i=x_i y_i`, with `x_i in X,y_i in Y`.  Six-colour `G-e_i` and
write

\[
                         \alpha=c(x_i)=c(y_i).       \tag{3.1}
\]

For `beta ne alpha`, let `K_beta` be the common `alpha/beta` Kempe
component containing both ends, supplied by edge criticality.

### Theorem 3.1 (three mandatory boundary palettes)

For at least three colours `beta ne alpha`, the vertices `x_i,y_i` are
disconnected in

\[
                         K_beta-S.                  \tag{3.2}
\]

Equivalently, every `alpha/beta` path between the two ends must use the
literal seven-boundary.

If `alpha` is absent from `c(S)`, these three colours give distinct
boundary vertices on both sides,

\[
 a_{\beta}\in N_S(X),\qquad b_{\beta}\in N_S(Y),
 \qquad c(a_\beta)=c(b_\beta)=\beta,                \tag{3.3}
\]

such that `a_beta,b_beta` are joined by an `alpha/beta` path in the
opposite closed shore `H union S`.  The three `a_beta` are distinct, as
are the three `b_beta`.  Equality `a_beta=b_beta` is allowed and is
exactly a literal common-row carrier.

### Proof

Fix `beta`.  A retained properly coloured edge can belong to the
`alpha/beta` subgraph for at most one value of `beta`: its unordered
endpoint-colour pair must be exactly `{alpha,beta}`.  Hence for at least
three of the five non-`alpha` colours, neither retained bond edge belongs
to the `alpha/beta` subgraph at all.  For each such colour, the common
Kempe component can pass from `X` to `Y` only through `S`.  This proves
(3.2), in the stronger form needed below.

Now suppose `alpha` is absent from `S`.  Choose an `alpha/beta` path from
`x_i` to `y_i`.  After its last departure from `X` and before its first
subsequent arrival in `Y`, it lies in the opposite closed shore `H union
S`: the old open shores are anticomplete, and neither retained bond edge
has the required colour pair.  Let `a_beta` and `b_beta` be the first and
last boundary vertices of this segment.  They have colour `beta` and
satisfy (3.3); the intervening segment is the asserted opposite-shore
path.  Different `beta` give different vertices at either end because the
colours differ.  QED.

### Corollary 3.2 (exact operation-sensitive fork)

For each of the three bond edges, its faithful deletion state satisfies
one of the following:

1. the repeated endpoint colour occurs on the seven-boundary; or
2. three distinct non-endpoint palettes have paired literal shore carriers
   joined through the opposite closed shore as in (3.3).

This conclusion uses all three facts simultaneously: the interface is the
complete three-edge bond, the operation is an actual critical edge, and
the shore boundary is literal.  It is not implied by the abstract
three-coordinate hypercube relation.

### Lemma 3.3 (common carrier or an alternating perfect state)

Retain one rung-deletion colouring and suppose its repeated colour `alpha`
is absent from `S`.  For the three paired palettes in (3.3), either

1. `a_beta=b_beta` for at least one `beta`, giving a literal common-row
   carrier; or
2. the three equality pairs `a_beta b_beta` form one of the two perfect
   matchings of the missing cycle `C_6`.

In outcome 2 the equality partition on `S` is exactly

\[
             e_1\mid e_2\mid e_3\mid\{z\},         \tag{3.4}
\]

where `e_1,e_2,e_3` are the edges of one alternating perfect matching of
`C_6`.

### Proof

If `a_beta ne b_beta`, the two boundary vertices have one colour in a
proper colouring, so they are nonadjacent in `G[S]`.  Neither is `z`, and
their pair is an edge of the missing `C_6`.  Pairs belonging to distinct
colours are vertex-disjoint.  If none is a common carrier, the three pairs
therefore form a matching of order three in the six-cycle, hence one of its
two alternating perfect matchings.  They consume all six cycle vertices;
the universal vertex `z` is the remaining singleton block, proving (3.4).
QED.

### Corollary 3.4 (three rungs force a repeated parity state)

If, in a chosen deletion colouring for each of the three bond edges, the
repeated colour is absent from `S` and no literal common-row carrier occurs,
then two of the three operations induce the same equality partition (3.4)
on `S`.

There are only two alternating perfect matchings, so this is the
pigeonhole principle applied to Lemma 3.3.  It is a genuine normalized
state repetition on two different rungs.  It is not by itself a crossed
splice, because both operations lie in the same old shore; the final
exchange must use their different positions in the complete three-edge
bond.

## 4. Exact remaining exchange

The three-face web is now reduced to the one-hole prism-triangle bond
(2.3)--(2.4), decorated on every rung by Corollary 3.2.  A final closure
may not merely assert state repetition.  It must show one of:

* two of the paired palette paths can be chosen disjointly and split the
  prism-triangle bond into the required branch bags;
* all three repeated colours occur on `S`, forcing one common equality
  state with an opposite faithful operation; or
* the repeated alternating state in Corollary 3.4 can be spliced across
  its two different bond rungs;
* concentration of the carriers exposes a separator of order at most six.

The theorem above removes the possibility that a three-face obstruction
is a palette-free planar drawing.  Every one of its three shared facial
edges sends at least three colour channels from one bond shore to the
other through the actual seven-boundary and the opposite closed shore.
