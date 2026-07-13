# The order-eight wheel supports a uniform dynamic selector state

## 1. Purpose

The static wheel in
`hadwiger_order8_atomic_web_curvature_counterarchitecture.md` does not
become rigid merely because one uses every internal deletion and
contraction state.  There are two boundary partitions `sigma,tau` such
that

* the intact wheel accepts `sigma` and rejects `tau`;
* deleting **or contracting any internal wheel edge** makes the wheel
  accept the same partition `tau`; and
* `sigma` and `tau` have the same five-colour core and differ by one
  shadow vertex moving between its anchor colour and the sixth colour.

This note gives the complete hand certificate and then realizes the
two states with an explicit opposite-side selector.  The resulting graph
is not seven-connected and is not a candidate counterexample.  Its point
is exact: absolute partition novelty, critical-edge equality, all eight
wheel operations, and crossed-state disagreement do not force a change
of the cyclic portal geometry.  A valid closure has to use global
seven-connectivity (or an equivalent rooted-model theorem) on the
opposite selector side.

## 2. The two wheel states

Use the atomic wheel notation

\[
 B=(x,p,q,c_0,c_2,c_4,c_5,z),\qquad
 K=(v_0,v_1,v_2,v_3,h).
\]

The wheel contacts are

\[
\begin{array}{c|c}
v_0&x,c_5,c_0,z,p\\
v_1&c_5,c_2,c_0,z,p\\
v_2&c_2,c_4,c_0,z,q\\
v_3&c_4,x,c_0,z,q\\
h&c_0,z,p,q.
\end{array}                                                \tag{2.1}
\]

Define the boundary partitions by the following canonical colour rows:

\[
\begin{array}{c|rrrrrrrr}
 &x&p&q&c_0&c_2&c_4&c_5&z\\ \hline
\sigma&0&1&1&1&0&2&3&4\\
\tau  &0&1&1&1&2&3&4&5.
\end{array}                                                \tag{2.2}
\]

Thus the five blocks represented by

\[
             \{p,q,c_0\},\quad \{c_2\},\quad
             \{c_4\},\quad \{c_5\},\quad \{z\}          \tag{2.3}
\]

are rainbow in both states.  In `sigma`, the shadow `x` has the colour
of `c_2`; in `tau`, it has the sixth colour.

### Lemma 2.1 (intact and forbidden states)

The intact boundaried wheel accepts `sigma` and rejects `tau`.

### Proof

For `sigma`, in the order `(v_0,v_1,v_2,v_3,h)`, use

\[
                         (5,2,5,3,0).                       \tag{2.4}
\]

All checks are immediate from (2.1).

Under `tau`, the lists left at the five wheel vertices are

\[
\begin{array}{c|c}
v_0&\{3,4\}\\
v_1&\{0,4\}\\
v_2&\{0,5\}\\
v_3&\{3,5\}\\
h&\{0,3,4,5\}.
\end{array}                                                \tag{2.5}
\]

Adjacent rim vertices must differ, while opposite rim vertices have
disjoint lists.  Hence the four rim vertices receive four distinct
colours, necessarily all of `0,3,4,5`.  No colour remains for the hub.
Therefore `tau` does not extend.  QED.

### Lemma 2.2 (one common state is unlocked by every wheel edge)

For every `e in E(K)`, the graph `K-e` accepts `tau` in a colouring
whose ends of `e` have the same colour.  Consequently `K/e` also accepts
`tau`.

### Proof

The following table gives the wheel colours in the order
`(v_0,v_1,v_2,v_3,h)`:

\[
\begin{array}{c|ccccc}
e&v_0&v_1&v_2&v_3&h\\ \hline
hv_0&3&0&4&2&3\\
hv_1&3&0&4&2&0\\
hv_2&3&0&4&2&4\\
hv_3&2&3&0&4&4\\
v_0v_1&3&3&4&2&0\\
v_0v_3&2&3&4&2&0\\
v_1v_2&3&0&0&2&4\\
v_2v_3&2&0&4&4&3.
\end{array}                                                \tag{2.6}
\]

Every row respects the lists (2.5), every retained wheel edge is
proper, and the ends of the edge named in the first column agree.
Identifying those equal-coloured ends gives the contraction statement.
QED.

The conclusion is stronger than the existence of a novel state for each
edge: the **same** novel state works for all eight edges.  Neither the
literal active-root order

\[
                    x-c_5-c_2-c_4-x                         \tag{2.7}
\]

nor the graph-theoretic `p|q` half-rim distribution changes.  Only the
colour of the shadow `x` moves.

## 3. An explicit opposite-side selector

This section realizes the state flip without an abstract extension-
relation theorem.

Retain the old boundary

\[
                 S=\{c_0,c_1,\ldots,c_5,z\},               \tag{3.1}
\]

where the missing-edge graph on the `c_i` is `C_6` and `z` is universal
to the six cycle vertices.  Add a proxy clique

\[
                    Y=\{y_0,y_1,y_2,y_3,y_4\}.              \tag{3.2}
\]

For six colours, write `E_6(a,b)=K_7-ab`, with `a,b` the nonadjacent
pair.  Its other five vertices form a clique and force `a,b` to have
the same colour in every six-colouring.

Attach equality gadgets forcing

\[
\begin{aligned}
 &(c_0,y_0),\ (c_2,y_1),\ (c_4,y_2),\ (c_5,y_3),\ (z,y_4),\\
 &(p,c_0),\ (q,c_0),\ (c_1,c_0).
\end{aligned}                                               \tag{3.3}
\]

Join each of `x,c_3` to

\[
                         y_0,y_2,y_3,y_4,                   \tag{3.4}
\]

and add the selector edge

\[
                              f=xc_3.                       \tag{3.5}
\]

Call this boundaried graph `F`.  Since `Y` uses five colours, (3.3)
makes the five classes in (2.3), with `z` as the fifth singleton,
rainbow.  Each of `x,c_3` has exactly two available colours: the colour
of `c_2=y_1`, or the sixth colour.  The edge `f` forces them to choose
oppositely.  Hence `F` has exactly the following two boundary modes:

\[
\begin{array}{c|cc}
 &x&c_3\\ \hline
\rho&c_2&\hbox{sixth colour}\\
\tau&\hbox{sixth colour}&c_2.
\end{array}                                                \tag{3.6}
\]

The restriction of `rho` to `B` is `sigma`; the restriction of the
second row is `tau`.  If `f` is deleted or contracted, there is also the
mode

\[
                              \mu:x=c_3=c_2.                 \tag{3.7}
\]

## 4. The full local transition graph

Let `H` be the union of the boundaried wheel and `F`, together with the
old boundary graph on `S` and the literal edge `xc_0`.  Add a vertex `v`
adjacent to all of `S`, and call the result `G_*`.

### Theorem 4.1 (complete two-shore transition table)

The graph `G_*` has the following properties.

1. `G_*` is not six-colourable.
2. The proper star minor obtained by contracting `v,c_0,c_1` is
   six-colourable; its expansion on `H` is the exact trace `rho`.
3. For every internal wheel edge `e`, both `G_*-e` and `G_*/e` are
   six-colourable in the common state `tau`.
4. Both `G_*-f` and `G_*/f` are six-colourable in the state `mu`.
5. On the exact eight-gate `B`, the wheel-operation state is pinned at
   the singleton block `{x}`, whereas the opposite selector-operation
   state is unpinned.  Thus their marked states are different, exactly
   as required by the crossed-state theorem.

### Proof

In mode `rho`, give

\[
 (c_0,c_1,c_2,c_3,c_4,c_5,z)=(1,1,0,5,2,3,4).             \tag{4.1}
\]

The wheel accepts its gate restriction `sigma` by Lemma 2.1.  The seven
vertices of `S` use all six colours, so `v` cannot be coloured.

In mode `tau`, give

\[
 (c_0,c_1,c_2,c_3,c_4,c_5,z)=(1,1,2,2,3,4,5),             \tag{4.2}
\]

and give `x` colour zero.  Now `v` may also receive colour zero, but the
intact wheel rejects `tau` by Lemma 2.1.  These are the only two modes
of `F`, proving item 1.

Equation (4.1), with the contracted star vertex given colour one, colours
the star minor and proves item 2.  For a wheel edge operation, use (4.2),
give `v` colour zero, and use the appropriate row of (2.6).  The operated
ends agree, so the same certificate handles deletion and contraction.
This proves item 3.

After operating on `f`, put `x=c_3=c_2`, keep the other five core
classes, and give `v` the unused sixth colour.  The gate state is `sigma`,
so (2.4) colours the intact wheel.  Again the operated ends agree,
proving item 4.

In the wheel-operation state (4.2), colour zero is absent from `S` and
occurs on `B` exactly at `x`; the state is pinned at `{x}`.  In the
selector-operation state (3.7), the apex uses the sixth colour, which is
absent from all of `B`; this state is unpinned.  Item 5 follows.  QED.

## 5. Exact consequence

The graph `G_*` is deliberately not seven-connected.  Each equality
gadget is attached through its two named terminals, so the selector side
has many two-separations.  It may also have clique minors irrelevant to
the target-free setting.  Therefore it is not an `HC_7` counterexample.

It does prove that the following proposed dynamic inference is false:

> all internal wheel operations are novel, their deleted ends are
> critical-edge equal, and opposite operation states are crossed-state
> incompatible; therefore some operation breaks the wheel orientation or
> creates the two protected columns.

All eight wheel operations can instead move coherently to the single
state `tau`, while one opposite operation moves to the distinct state
`mu`.  Absolute novelty and crossed-state disagreement are both obeyed.

The missing axiom is now geometric and two-sided:

> **Seven-connected selector exclusion.**  A seven-connected full-gate
> realization cannot implement the two-mode relation (3.6) across the
> atomic wheel without producing a labelled two-path linkage, a nested
> exact-seven cut, or a `K_7` minor.

Equivalently, the next theorem must turn a far-side realization of the
exclusive-or relation

\[
 (x=c_2)\ \mathbin{\mathrm{xor}}\ (c_3=c_2)                \tag{5.1}
\]

into a rooted model or a small adhesion.  State counting, operation-edge
choice, and disk curvature cannot do this: the selector above satisfies
all three local tests.  This is a finite-boundary version of the desired
uniform rooted-model principle, and it identifies precisely where
seven-connectivity has not yet been spent.

### Exact next target (not a broad state conjecture)

The construction isolates the following finite-boundary statement.  It
is stronger than what is currently proved, but contains no arbitrary
portal graph or arbitrary extension relation.

> **Atomic three-state selector lemma.**  Let `G` be a proper-minor-
> minimal non-six-colourable, `K_7`-minor-free graph, let `v` have the old
> neighbourhood `S`, and suppose a component
> `K` of `G-(B union {v})` is exactly the four-rim wheel with the eight
> gate vertices and contacts (2.1).  Suppose also that, after one palette
> normalization, the following three full labelled partitions occur:
>
> 1. the contraction of the star `v-c_0,v-c_1` has the trace
>    \[
>    \rho:\quad
>    \{v,p,q,c_0,c_1\}\mid\{x,c_2\}\mid\{c_3\}
>    \mid\{c_4\}\mid\{c_5\}\mid\{z\};
>    \]
> 2. every internal wheel-edge operation has a colouring with state
>    \[
>    \tau:\quad
>    \{v,x\}\mid\{p,q,c_0,c_1\}\mid\{c_2,c_3\}
>    \mid\{c_4\}\mid\{c_5\}\mid\{z\};
>    \]
> 3. some boundary-faithful operation on the opposite open side has a
>    colouring with state
>    \[
>    \mu:\quad
>    \{v\}\mid\{x,c_2,c_3\}\mid\{p,q,c_0,c_1\}
>    \mid\{c_4\}\mid\{c_5\}\mid\{z\}.
>    \]
>
> Then either `G` contains a `K_7` minor, or the opposite open side has a
> proper fragment whose external neighbourhood has order at most six.

In a seven-connected graph the separator conclusion is impossible, so
this exact lemma eliminates the whole coherent wheel state at once.  Its
hypotheses are precisely the three states realized by `G_*`; no claim is
made about other boundary relations.  The equality-selector realization
fails its conclusion only through the two-terminal attachments of the
`E_6` gadgets, which is why an order-six separator is the correct
alternative rather than a vague appeal to high connectivity.

## 6. Verification

`order8_wheel_dynamic_selector_verify.py` constructs `G_*` and checks
with an independent SAT encoding that

* `G_*` is not six-colourable;
* the exact star contraction is six-colourable;
* every internal wheel deletion and contraction is six-colourable; and
* the selector-edge deletion and contraction are six-colourable.

The displayed colour rows (2.4), (2.6), (4.1), and (4.2) are the hand
certificates; the solver is not needed for the proof.
