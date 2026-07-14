# Barrier: the two-spare Kempe Hall shortcut is false on a three-connected page

**Status:** exact finite counterarchitecture.  The companion verifier is
[`hc7_exact7_two_spare_kempe_hall_barrier_verify.py`](hc7_exact7_two_spare_kempe_hall_barrier_verify.py).

The construction is a properly six-coloured, planar, three-connected,
`S`-full page.  Its boundary colouring realizes the paired-triangle equality state, six
distinct portals in the common-face order, and a literal reversed
three-linkage.  Nevertheless, the stronger two-by-two Kempe proposal has no
successful injective assignment, while its failed tests force none of:

1. two disjoint carriers for the two original outer duties;
2. a reversed rooted-`K_4` expansion; or
3. two interior vertices meeting every lock path in the failed family.

This is not a seven-connected host or a hypothetical `HC_7` counterexample.
Its scope is precise: three-connected common-face geometry and literal
reversal do not, by themselves, discharge a Kempe Hall residue.

## 1. The exact generic reduction

Write

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 \Pi=\bigl\{\{a_i,t_i\}:i\in[3]\bigr\}\cup\{\{c\}\}.
 \tag{1.1}
\]

Colour `a_i,t_i` with colour `i`, colour `c` with colour `4`, and suppose
colours `u,v` are absent from `S`.  For `i in {1,3}` and `s in {u,v}`, call
`(i,s)` successful when `a_i,t_i` lie in different components of the
subgraph on colours `{i,s}`.  A swap in the component of one endpoint then
splits exactly `B_i={a_i,t_i}`.

The successes form a bipartite graph between `{B_1,B_3}` and `{u,v}`.
There are two safe generic conclusions.

* A perfect matching gives two swaps on disjoint colour sets.  Their
  supports are disjoint, the swaps commute, and both outer blocks split.
* If two tests using different blocks and different spare colours both
  fail, shortest lock paths use disjoint colour sets and are therefore two
  disjoint original-duty carriers.

If the success graph has no perfect matching, Hall leaves exactly the
overlapping residue types:

* a **zero row**, where one block fails against both spares; or
* a **zero column**, where both blocks fail against one common spare.

The construction below realizes a zero column and defeats the proposed
three-way discharge.

## 2. The stellated three-by-three page

Start with crossings

\[
                         v_{ij}\qquad (i,j\in[3]).       \tag{2.1}
\]

Subdivide every horizontal grid edge by `h_ij` and every vertical grid edge
by `g_ij`:

\[
 v_{ij}h_{ij}v_{i,j+1}\quad(i\in[3],j\in[2]),\qquad
 v_{ij}g_{ij}v_{i+1,j}\quad(i\in[2],j\in[3]).           \tag{2.2}
\]

For each of the four bounded grid cells add a vertex `f_ij` adjacent to all
eight vertices on that cell's subdivided rim.  Call the resulting
25-vertex graph `C`.  It is planar and three-connected.  All four face
centres are needed to make this particular subdivided-grid architecture
three-connected.

Give the open page the colours

\[
 \kappa(v_{ij})=6,\qquad
 \kappa(h_{ij})=1,\qquad
 \kappa(g_{ij})=3,\qquad
 \kappa(f_{ij})=2.                                      \tag{2.3}
\]

Its boundary contacts are

\[
\begin{array}{c|c}
a_1&v_{11},v_{21},v_{31}\\
t_1&v_{13},v_{23},v_{33}\\
a_3&v_{11},v_{12},v_{13}\\
t_3&v_{31},v_{32},v_{33}\\
a_2&v_{11}\\
t_2&v_{33}\\
c&v_{12}.
\end{array}                                              \tag{2.4}
\]

On `S`, retain the triangle `a_1a_2a_3`, the three edges `ca_i`, and no
edge `a_it_i`.  These edges witness every required inter-block adjacency
of (1.1), and (2.3)--(2.4) extend the displayed boundary colours to a
proper six-colouring of the closed page.

## 3. Exact zero-column trace

Take `u=5` and `v=6`.  Colour `5` is absent from the entire page, so both
tests against `5` succeed.  Against colour `6`, the three horizontal rows
are internally disjoint `{1,6}` lock paths from `a_1` to `t_1`, and the
three vertical columns are internally disjoint `{3,6}` lock paths from
`a_3` to `t_3`.  Thus the success matrix is

\[
\begin{array}{c|cc}
 &5&6\\ \hline
B_1&\mathrm{success}&\mathrm{lock}\\
B_3&\mathrm{success}&\mathrm{lock}.
\end{array}                                              \tag{3.1}
\]

There is no perfect matching.  Moreover, the three row interiors are
pairwise disjoint.  Any set meeting every `{1,6}` row lock has order at
least three.  In particular, no named pair of interior vertices is a
transversal even for this one failed lock family.

There are also no two disjoint original-duty carriers.  To see this without
identifying colours with topology, attach four artificial terminals to the
four portal sets for `a_1,a_3,t_1,t_3`.  The augmented graph is planar with
the terminals cofacial in alternating order

\[
                         a_1,a_3,t_1,t_3.                \tag{3.2}
\]

Disjoint carriers for `B_1` and `B_3` would extend to disjoint paths joining
the two alternating terminal pairs, contradicting the disk crossing
obstruction.

## 4. Literal reversal and failed rooted expansion

Choose the six distinct portals

\[
\begin{array}{c|cccccc}
\text{literal}&a_1&a_2&a_3&t_1&t_2&t_3\\ \hline
\text{portal}&v_{21}&v_{11}&v_{12}&v_{23}&v_{33}&v_{32}.
\end{array}                                              \tag{4.1}
\]

Starting at `v_21`, they occur on the outer face in exactly the displayed
literal order.  The reversed three-linkage is literal:

\[
\begin{aligned}
H_1&=v_{21}f_{21}v_{32},\\
H_2&=v_{11}f_{11}v_{22}f_{22}v_{33},\\
H_3&=v_{12}f_{12}v_{23}.
\end{aligned}                                            \tag{4.2}
\]

These paths are pairwise vertex-disjoint and have traces
`a_1-t_3`, `a_2-t_2`, and `a_3-t_1`.

The verifier exhaustively encodes four disjoint nonempty connected bags
`R,H_1,H_2,H_3`, all six pairwise adjacencies, the three named reversed
traces, and the requirement that `c` see one bag.  Strictly decreasing
depths give a complete connectivity encoding.  The formula is
unsatisfiable.  Hence this page has no reversed rooted-`K_4` expansion.

## 5. Trust boundary and the HC7-specific missing input

The page proves that none of the following is enough to discharge the Hall
residue:

* the exact paired equality state and two unused colours;
* planarity and three-connectivity of the rich component;
* one common face containing the six selected portals;
* a literal distinct-portal reversed linkage; or
* the bichromatic lock paths themselves.

The construction deliberately does not satisfy the full host hypotheses.
In particular it is not seven-connected, it is not installed in an actual
`(1,2)` adhesion with the second full packet, and it uses no
contraction-criticality, nonreflection, or terminal exclusion.

There is one concrete host-level constraint unavailable to the shortcut.
In the actual common-face setting, if `x` is a vertex of `C` not incident
with the common face, then `x` has no boundary neighbour in `S-{c}`.  Since
`C` is a component of `G-S` and a seven-connected host has minimum degree
at least seven,

\[
                              d_C(x)\ge6.                \tag{5.1}
\]

The four internal rail subdivision vertices of this barrier have degree
four in `C`, so (5.1) excludes this exact page from an `HC_7` host.  The
degree inequality still does not discharge a zero row or zero column from
the Kempe data alone.

The host-specific repair is now isolated separately in
[`hc7_exact7_cross_lobe_curvature_exchange.md`](../results/hc7_exact7_cross_lobe_curvature_exchange.md).
It adds the missing **full three-duty nonreflection** and the six-label
portal SDR.  A circle-incidence bound then contradicts planar curvature and
minimum degree seven.  Thus the actual cross-lobe family can close without
promoting this two-spare shortcut to a state-transition rule; the shortcut
itself remains false in the exact scope certified here.
