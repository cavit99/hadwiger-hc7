# Contact-span packing and opposite-state barriers

## Status

Two exact witnesses separate the two missing mechanisms behind the
distributed-row exchange.

1. An eleven-vertex literal two-cycle/three-row host has no four disjoint
   duty-complete sectors, but its complete-sector family has actual-vertex
   transversal number three, not two.  It is `K7`-minor-free by an explicit
   width-five elimination order.
2. A thirteen-vertex Hajós join is 7-chromatic, and every single vertex
   deletion, edge deletion, and edge contraction is six-colourable.  It
   realizes disjoint equality-state families across opposite open shores
   of one actual separation.

The first witness is only three-connected.  The second has connectivity
two.  Thus neither is compatible with the full seven-connectivity axiom.
They prove, respectively, that the proposed packing-to-two-hit implication
is false for circular spans and that the full menu of one-step operation
states alone does not force opposite-shore state collision.

The executable certificate is
`hc7_contact_span_packing_barrier_verify.py`.

## 1. Smallest literal four-port schema

Let

\[
 L=(\ell_0\ell_1\ell_2\ell_3\ell_0),\qquad
 R=(r_0r_2r_1r_3r_0),
\]

and add the four matching edges `ell_i r_i`.  Add a row triangle
`f_0f_1f_2f_0`.  Use the three distinct contact rows

\[
\begin{array}{c|c}
f_0&\ell_0,r_1,\ell_2\\
f_1&\ell_0,r_1,r_2\\
f_2&r_0,r_1,\ell_2.
\end{array}                                             \tag{1.1}
\]

There are no other edges.  Thus every fixed row genuinely meets **both**
cycle shores; the obstruction is not the absence of a shore-level row
contact.  The three row-support patterns are also distinct.

A literal port sector at `i` is

\[
       T=A\cup\ell_i r_i\cup B,                        \tag{1.2}
\]

where `A` is a subpath of `L` containing `ell_i` and `B` is a subpath of
`R` containing `r_i`.  Call it **duty-complete** when it is adjacent to
all three fixed rows.

### Proposition 1 (packing number and transversal number both three)

Every duty-complete sector contains at least one of the three neighbours
`ell_0,ell_2,r_1` of `f_0`.  Therefore four pairwise vertex-disjoint
duty-complete sectors do not exist.

On the other hand, the three two-vertex sectors

\[
                 \{\ell_i,r_i\},\qquad i=0,1,2,       \tag{1.3}
\]

are duty-complete and pairwise disjoint.  Consequently no set of at most
two actual vertices hits every duty-complete sector.  Conversely, the
three anchors in (1.1) hit every complete sector, so both parameters are
exactly three.

#### Proof

The only neighbours outside the row triangle of `f_0` are
`ell_0,ell_2,r_1`.  A sector adjacent to `f_0` must contain one of those
anchors; duty-completeness in particular has this property.  Four disjoint
sectors would need four different `f_0`-anchors, but only three exist.

By (1.1), each sector in (1.3) has a (possibly different) endpoint
adjacent to each of the three rows, so the sectors are complete.  A transversal of the whole
complete-sector family must meet all three disjoint members (1.3), and
hence has order at least three.  The first paragraph shows that the three
anchors themselves are a transversal.  \(\square\)

The same three anchors are an **actual vertex cut** in this witness:
deleting `ell_0,ell_2,r_1` isolates `ell_1` from the other seven
remaining vertices.  This is a property of the displayed host, not a
general consequence of a three-point sector transversal.

This is order-minimal in the literal four-port schema: mismatched cycles
need four named ports, hence eight cycle vertices, and three disjoint fixed
rows require three further vertices.

### Proposition 2 (no hidden packet completion)

The host has treewidth at most five and hence no `K7` minor.  One valid
elimination order is

\[
 \ell_1,\ell_3,r_0,f_0,f_1,f_2,\ell_0,\ell_2,r_1,r_2,r_3,
\]

with filled-neighbour counts

\[
                         3,3,4,5,5,5,4,3,2,1,0.
\]

In particular there is no choice of four rooted corner bags together with
disjoint off-skeleton repair packets that repairs all twelve corner-row
duties: by the audited simultaneous packet-promotion theorem, such a
choice would itself be a literal `K7` model.

Thus the obstruction is not an artefact of naming only the three tiny
sectors in (1.3); every legal packet completion is excluded.

Nevertheless the host already contains the precise near-clique demanded
by the proof spine.  In the following order, its seven branch sets are

\[
 \{f_0\},\ \{f_1\},\ \{r_1\},\ \{r_0,f_2\},\
 \{\ell_0,\ell_1\},\ \{\ell_2,r_2\},\ \{\ell_3,r_3\}.
                                                               \tag{1.4}
\]

They are pairwise disjoint and connected.  Every pair is adjacent except
exactly the pairs `(6,0)` and `(6,1)`, namely

\[
  \{\ell_3,r_3\}\not\sim\{f_0\},\qquad
  \{\ell_3,r_3\}\not\sim\{f_1\}.
\]

Thus (1.4) is a literal `K7^vee` model: its two missing pairs share the
single deficient bag `\{ell_3,r_3\}`.  The near-`K7` structure therefore
survives this counterexample; what fails is precisely the high-connectivity
or critical exchange needed to repair it.

## 2. Disjoint one-step operation states in a Hajós host

Let the actual adhesion be `S={s,t}`.  The equality shore `C` consists of
a `K5` on `c_0,...,c_4`, with both `s,t` complete to the `K5` and
nonadjacent to each other.  In every six-colouring of `C`, the clique uses
five colours and `s,t` are both forced to use the sixth.  Hence

\[
                         \operatorname{Ext}(C,S)=\{s=t\}.       \tag{2.1}
\]

The inequality shore `O` consists of a `K6` on `d_0,...,d_5`, together
with

\[
 t\sim d_0,d_2,d_3,d_4,d_5,qquad s\sim d_1.          \tag{2.2}
\]

The `K6` uses all six colours.  Equation (2.2) forces `t` to have the
colour of `d_1`, while `sd_1` forces `s` to have a different colour.
Thus

\[
                         \operatorname{Ext}(O,S)=\{s\ne t\}.    \tag{2.3}
\]

The shores meet exactly in `S`, with no edge between their open parts.
Their union `J` is the Hajós join of two copies of `K7`: delete `st` in
the first copy, delete `td_1` in the second, identify the two copies of
`t`, and add `sd_1`.  Equations (2.1)--(2.3) prove `chi(J)=7` directly.

The verifier establishes the stronger one-step statement:

* every vertex deletion is six-colourable;
* every edge deletion is six-colourable; and
* every edge contraction is six-colourable.

This does **not** make `J` contraction-critical in the standard
all-proper-minors sense.  In fact it contains a literal `K7` model:

\[
 \{c_0\},\{c_1\},\{c_2\},\{c_3\},\{c_4\},\{t\},
 \{s,d_1,d_0\}.                                      \tag{2.4}
\]

The last bag is connected by `s-d1-d0` and meets `{t}` through `d0t`;
it meets every `c_i` through `s`, while the first six bags are pairwise
adjacent.  Thus a sequence of contractions can recover `K7` even though
every **single** edge contraction is six-colourable.  Chromatic number is
not minor-monotone, so the one-step checks cannot be promoted to an
all-proper-minor claim.

Now perform one of the verified single operations strictly inside `C-S`.
The unchanged inequality shore still forces every resulting six-colouring
to induce `s!=t`.  Perform one instead strictly inside `O-S`; the unchanged
equality shore forces `s=t`.
Therefore the two opposite-shore operation-state families remain
disjoint.  Minor-criticality by itself does not create the state collision
needed by the equality splice.

The exact graph has graph6 string

```text
L~~~oCD?wF_^?~
```

and connectivity two, witnessed by `S`.  Seven-connectivity is exactly the
missing axiom; it must either destroy the actual low-order separation,
create a literal packet exchange around it, or propagate one coherent
rural/two-apex structure.

## 3. Consequence for the proposed contact-span dichotomy

The raw implication

\[
 \text{no four disjoint complete sectors}
 \Longrightarrow
 \text{two actual vertices hit every obstructing span}
\]

is false even in the smallest literal mismatched four-port schema.  Adding
the alternative “opposite single-operation states collide” does not repair
it using the one-step operation data alone: the Hajós witness has every such
state and keeps the two equality families disjoint.  It is not a
contraction-critical host because of the explicit multi-contraction model
(2.4).

A viable positive theorem must use seven-connectivity in a literal way.
For example, it may conclude a four-sector/packet exchange, a separator of
order at least seven whose extra vertices force a state collision, or one
coherent cofacial two-apex expansion.  A circular-arc packing theorem with
a universal two-point transversal is unavailable.
