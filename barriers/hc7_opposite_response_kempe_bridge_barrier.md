# An exact-order-eight barrier to boundary transitions through the common deletion

**Status:** computer-assisted finite barrier, with a written construction,
proof, and
[separate internal audit](hc7_opposite_response_kempe_bridge_barrier_audit.md).
The deterministic verifier is
[`hc_opposite_response_transition_barrier_verify.py`](hc_opposite_response_transition_barrier_verify.py).
This graph is not a counterexample to `HC_7`: it contains a `K_7` minor and
is not minor-minimal subject to being non-six-colourable.

## 1. The inference that fails

Let `(A,S,B)` be a vertex separation, let `g` be an edge internal to `A`,
let `h` be an edge internal to `B`, and put

\[
                         H=G-\{g,h\}.
\]

The following data do not, even together, force a common boundary
partition for the two one-edge-deletion responses or a direct Kempe
interchange between them:

1. `G` is seven-chromatic and eight-connected;
2. `|S|=8`, and both open shores are connected and adjacent to every
   vertex of `S`;
3. `G-g`, `G-h`, and `G/g/h` are six-colourable;
4. `H` is connected, exactly six-chromatic, and contains a literal `K_6`;
5. the three allowed edge-equality patterns

   \[
       (\mathsf{equal},\mathsf{equal}),\quad
       (\mathsf{equal},\mathsf{proper}),\quad
       (\mathsf{proper},\mathsf{equal})
   \]

   all occur in six-colourings of `H`, while
   `(proper,proper)` does not; and
6. the two one-edge response families are joined in the Kempe
   reconfiguration graph of `H` by a path of length two through an
   `(equal,equal)` colouring.

In the construction below, every colouring of `G-g` induces one fixed
partition of the literal boundary, every colouring of `G-h` induces a
different fixed partition, and no single Kempe interchange in `H` moves
between the two response families.  Thus connectedness in the common
deletion's colouring space is not a state-transfer theorem.  The
intermediate colouring may have the desired boundary partition while
being monochromatic on the edge that must be restored.

## 2. A ten-vertex three-colour core

Start with vertices

\[
 a,b,a',b',p_a,q_a,p_b,q_b,c,d.
\]

For each of the pairs `(a,a')` and `(b,b')`, add a copy of `K_4` minus
the edge between the displayed pair.  Explicitly,

\[
 p_aq_a, ap_a, aq_a, a'p_a, a'q_a
\]

are edges, and the analogous five edges with subscript `b` are edges.
Every proper three-colouring therefore gives `a` and `a'` one common
colour and gives `b` and `b'` one common colour.

Make both `c` and `d` adjacent to both `a'` and `b'`.  Finally add

\[
                         g=ab,\qquad h=cd.
\]

Call the resulting graph `J`, and put `J_0=J-{g,h}`.  There is a
separation with

\[
 \begin{aligned}
 A_0&=\{a,b,p_a,q_a,p_b,q_b\},\\
 S_0&=\{a',b'\},\\
 B_0&=\{c,d\}.
 \end{aligned}
\]

There is no `A_0-B_0` edge, and `g,h` are internal to the respective
open shores.

### Exact colouring relation

The equality gadgets reduce the colour constraints to the four effective
vertices `a,b,c,d` of `K_4`, with `g,h` as a deleted matching.  It follows
that:

* `J` is not three-colourable;
* in every three-colouring of `J-g`, `a'=b'`;
* in every three-colouring of `J-h`, `a'` and `b'` have different colours;
* `J_0` realizes exactly the three edge-equality patterns `EE, EP, PE`;
  and
* `PP` is impossible, since restoring both edges would three-colour `J`.

The verifier enumerates all colourings.  It finds 24 colourings of each
one-edge deletion and 72 colourings of `J_0`, with exactly the asserted
relations.

The entire Kempe reconfiguration graph of the 72 three-colourings of
`J_0` is connected.  Nevertheless, no one Kempe interchange sends a
colouring of `J-h` to a colouring of `J-g`.  The minimum distance is two.
For example, with the vertex colours

\[
\begin{array}{c|cccccccccc}
 &a&a'&p_a&q_a&b&b'&p_b&q_b&c&d\\ \hline
\rho_0&0&0&1&2&1&1&0&2&2&2
\end{array}
\]

the edge pattern is `PE`.  Interchange colours zero and one on the
component `\{b,b',p_b\}` to obtain `EE`; then interchange colours one and
two on the singleton component `\{d\}` to obtain `EP`.

## 3. The six-colour, order-eight lift

Take a triangle

\[
                         T=\{t_0,t_1,t_2\}
\]

and join every member of `T` to every vertex of `J`.  Add three pairwise
nonadjacent vertices `w_0,w_1,w_2`, each adjacent to every vertex of `J`
and to `t_1,t_2`, but not to `t_0`.  Let the resulting graph be `G`.

The displayed separation is

\[
 \begin{aligned}
 A&=A_0,\\
 S&=\{a',b',t_0,t_1,t_2,w_0,w_1,w_2\},\\
 B&=B_0.
 \end{aligned}                                      \tag{3.1}
\]

It has order eight.  Both `A` and `B` are connected in `G`, and each is
adjacent to every literal vertex of `S`.

### Connectivity

Write \(U=T\cup\{w_0,w_1,w_2\}\).  Every vertex of `U` is adjacent to
every vertex of `J`.  If at most seven vertices are deleted and both
`U` and `J` remain nonempty, this complete join makes the remainder
connected.  Deleting all ten vertices of `J` is impossible, while deleting
all six vertices of `U` leaves all but at most one vertex of the
two-connected graph `J`.  To see the latter assertion directly, each
equality gadget is two-connected, and the two gadgets are joined by the
edge `ab` and by the two internally disjoint paths `a'cb'` and `a'db'`.
Deleting one vertex leaves at least one of these joins, while every
remaining vertex of either gadget and each of `c,d` still reaches it.
Hence `G` is eight-connected.  Deleting the
eight-set in (3.1) separates `A` from `B`, so the connectivity is exactly
eight.  The verifier independently checks every deletion of at most seven
vertices.

### Chromatic and minor data

The graph `J` is four-chromatic, so \(T\vee J\) is seven-chromatic.  The
vertices `w_i` can all receive the colour of `t_0`; hence `chi(G)=7`.

The graph `J_0` is exactly three-chromatic.  Consequently
`G-{g,h}` is exactly six-chromatic.  It contains the literal `K_6`

\[
                       T\cup\{a,p_a,q_a\}.
\]

Every six-colouring assigns three colours to `T`, three disjoint colours
to `J_0`, and the colour of `t_0` to every `w_i`.  The boundary partitions
of the two response families are therefore exactly

\[
\begin{aligned}
G-g:\quad&\{t_0,w_0,w_1,w_2\}\mid\{t_1\}\mid\{t_2\}
          \mid\{a',b'\},\\
G-h:\quad&\{t_0,w_0,w_1,w_2\}\mid\{t_1\}\mid\{t_2\}
          \mid\{a'\}\mid\{b'\}.
\end{aligned}                                      \tag{3.2}
\]

They are disjoint, as required by opposite-shore incompatibility.  The
`EE` colouring descends to a six-colouring of `G/g/h`, so the named
double-contraction response is genuinely present.

The two-switch path from Section 2 lifts unchanged.  A Kempe interchange
using two colours assigned to `J_0` is precisely a core interchange.  An
interchange using a colour of `T` and a colour of `J_0` swaps two whole
colour classes across the complete join and preserves all four endpoint
equalities.  Interchanges using only colours of `T` also preserve those
equalities.  Therefore the absence of a direct response-to-response
interchange in the core remains true in the six-colour lift.

## 4. Exact trust boundary

The example deliberately retains the local data most tempting for a
colouring-space transition argument:

* the `HC_7` palette;
* connectivity stronger than seven;
* an actual order-eight separation with two connected full shores;
* all three proper-minor edge-equality patterns;
* a common connected six-chromatic host containing `K_6`; and
* a shortest Kempe route through the simultaneous-equality pattern.

It fails two indispensable global hypotheses of the real kernel.

First, `G` is not minor-minimal subject to being non-six-colourable:
deleting any one `w_i` leaves the seven-chromatic subgraph `T vee J`.
Second, `G` contains a `K_7` minor.  Explicit branch sets are the three
singletons of `T` together with

\[
 \{a,p_a,a'\},\quad
 \{b,p_b,b'\},\quad
 \{c\},\quad
 \{d\}.
\]

Thus this is not a counterexample to the desired terminal-disjunctive
`HC_7` theorem.  It establishes a narrower and useful warning:

> A path in the Kempe reconfiguration graph of the common two-edge
> deletion cannot be converted into boundary-state gluing merely because
> it joins the two one-edge response families.  A valid proof must use
> minor-minimality or `K_7`-freeness to decode the intermediate `EE`
> colouring, and it must retain which deleted edge can legally be
> restored at each step.
