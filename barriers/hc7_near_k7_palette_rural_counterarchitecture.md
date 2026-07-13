# A seven-connected rural counterarchitecture to local palette/model alignment

## 1. Result

The palette-to-model gap cannot be closed from endpoint Kempe saturation,
literal repeated owner portals, and a five-colour transversal of a fixed
`K_5` frame alone.  All of those objects coexist in a seven-connected
`K_7`-minor-free graph.

### Proposition 1.1 (literal rural counterarchitecture)

There is a graph `G`, an edge `xy`, a proper six-colouring `c` of
`G-xy`, five disjoint fixed branch bags

\[
                         U_1,\ldots,U_5,
\]

and a two-pole lobe `C` with the following properties.

1. `G` is seven-connected and has no `K_7` minor.
2. `c(x)=c(y)=alpha`.  For every one of the other five colours `beta`,
   the vertices `x,y` lie in one `alpha/beta` component of `G-xy`.
   In particular both endpoints have a neighbour of every non-`alpha`
   colour.
3. The `U_i` form a fixed `K_5` model, disjoint from `x,y`.  They contain
   a transversal of vertices having the five distinct non-`alpha`
   colours.
4. After deleting the planar vertices of the fixed frame, `C` is a
   component behind two actual poles.  It misses exactly one fixed bag,
   has two distinct portals in another fixed bag, and its external
   neighbourhood in `G` has order exactly seven.
5. The obstruction is coherently rural: two vertices `a,b` satisfy
   `G-{a,b}` planar.

Thus a valid uniform rooted-model principle must retain a rural/two-apex
outcome, or use the genuinely dynamic rejection supplied by
proper-minor criticality.  Even a palette-colour SDR in the five fixed
model bags does not align Kempe components with branch-set ownership.

## 2. Construction

Let `I` be the icosahedron.  Subdivide every edge once and, inside each
old triangular face, join its three edge-midpoints in a triangle.  Call
the resulting frequency-two triangular refinement `P`.  It has 42
vertices and 120 edges.  It is planar and five-connected.  The latter is
also checked directly in the verifier; geometrically this is the usual
frequency-two geodesic icosahedron.

Let

\[
                         G=K_2\vee P,
\]

and denote the two adjacent universal vertices by `a,b`.  Then `G` is
seven-connected.  It is `K_7`-minor-free: in a hypothetical seven-bag
model, discard the at most two bags containing `a,b`.  The five remaining
bags lie in `P` and form a `K_5` model, contradicting planarity.

The deterministic numbering, full colouring, and every incidence below
are recorded in
`palette_model_rural_counterarchitecture_verify.py`.  The operation edge
is

\[
                         xy=0\,12,
\]

and both ends have colour zero after its deletion.  The planar graph uses
colours `0,1,2,3`, while `a,b` use colours `4,5`.  For the three planar
nonzero colours, explicit bichromatic paths are

\[
\begin{array}{c|l}
1&0,16,38,7,35,8,23,17,19,18,12,\\
2&0,13,12,\\
3&0,15,12.
\end{array}
\]

For colours four and five the paths are `0-a-12` and `0-b-12`.
This proves the endpoint-complete common-component state literally, not
just numerically.

Use the five fixed bags

\[
       U_1=\{a\},\quad U_2=\{b\},\quad
       U_3=\{21,27\},\quad U_4=\{22\},\quad U_5=\{26\}.
\]

The edge `21-27` connects `U_3`; the planar contacts

\[
              21\,22,\qquad 21\,26,\qquad 22\,26
\]

make the last three bags a `K_3` model, and the two universal singleton
bags complete a `K_5` model.  The representatives

\[
                         a,b,21,22,26
\]

have colours `4,5,1,3,2`, respectively.  Hence the five palette labels
do have an SDR in the five fixed model labels.

Remove the four planar frame vertices `21,27,22,26` and put

\[
                         W=\{25,28\},\qquad C=\{3\}.
\]

Then `C` is a component after deleting the two poles `W`, and

\[
             N_G(C)=\{a,b,21,27,26,25,28\}.                 \tag{2.1}
\]

Thus `C` misses exactly `U_4`, contacts `U_3` at the two distinct
vertices `21,27`, contacts `U_5` at `26`, and has the exact global
seven-cut displayed in (2.1).  This is precisely the local portal
multiplicity erased by a quotient contraction.

## 3. What the example rules out

The example is stronger than the abstract wheel state obstruction in
three directions:

* the ambient graph is genuinely seven-connected;
* the owner multiplicity consists of two literal vertices behind a
  literal two-pole gate; and
* the five model bags already contain a distinct-colour transversal.

Therefore none of the following implications is valid without a rural
alternative or a dynamic criticality hypothesis:

\[
\begin{split}
&\text{endpoint-complete five-palette state}
  +\text{ fixed }K_5\text{ model} \Longrightarrow K_7,\\
&\text{the same}+\text{ repeated actual owner portal}
  \Longrightarrow\text{ labelled owner split},\\
&\text{the same}+\text{ a palette SDR in the model bags}
  \Longrightarrow\text{ palette/model alignment}.
\end{split}
\]

The graph is six-colourable, so it is not a counterexample to `HC_7` and
does not satisfy operation-state rejection.  That is the exact point:
proper-minor criticality must be used as an exchange axiom, rather than
only as a source of one saturated colouring.

## 4. Sharpened common target

The common missing statement in the joint-edge, repeated-owner, and
selector routes should now be stated as follows.

> **Critical palette/model trichotomy.**  In a seven-contraction-critical
> `K_7`-minor-free graph, suppose a labelled operation state supplies an
> endpoint-complete five-palette warehouse relative to a fixed `K_5`
> frame, and a real lobe has a repeated portal in one owner.  Then either
> the owner/frame admits a labelled split giving `K_7`, the operation
> state transports faithfully across the relevant adhesion and
> six-colour gluing applies, or all operation lobes and owner portals are
> represented in one coherent two-apex rural expansion.

Proposition 1.1 realizes the third outcome sharply.  Consequently the
next proof cannot be a stronger static packing lemma.  It has to show
that the rural expansion is incompatible with **state rejection under
every internal deletion and contraction**, or else turn a nonrural
crossing into the labelled split.

## 5. Verification

Run

```text
PYTHONPATH=active/runtime/deps python3 \
    barriers/hc7_near_k7_palette_rural_counterarchitecture_verify.py
```

The script reconstructs `P`, checks planarity and five-connectivity,
checks seven-connectivity of `G`, verifies the colouring and all five
bichromatic connections, verifies the fixed `K_5` frame and its palette
SDR, and verifies the exact lobe neighbourhood (2.1).
