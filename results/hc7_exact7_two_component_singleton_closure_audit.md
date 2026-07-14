# Independent audit: singleton component closure in the residual `(1,2)` cell

Audited file:
`results/hc7_exact7_two_component_singleton_closure.md`.

Audited SHA-256:
`a68b0f0efe5b526d050261fbec3e0c3df47a96d022cb90f95ae5b3ca9616d8d4`.

This differs from the byte stream originally audited only in promoting the
status line from “pending independent audit” to “independently audited”;
the mathematical text is unchanged.

**Verdict:** **GREEN.**

The orientation at the singleton is valid, the frozen 129-residual
extraction and pure-Moser closure are used at exactly their audited scopes,
and the direct `M+13` construction contracts the correct shore.  Its two
minor colourings pull back to the two original closed sides with the same
exact five-block boundary state; they therefore glue to colour `G-q`, after
which the sixth boundary colour extends to `q`.

## 1. Global criticality and fullness

The hypotheses make `G` a seven-contraction-critical graph.  Indeed `G` is
not six-colourable, while every proper minor is six-colourable; deleting any
vertex also shows that `G` is at most seven-colourable.  Dirac's
neighbourhood inequality is therefore available with parameter seven.

Let `{q}` be the singleton component of `G[R]`.  Seven-connectivity makes
every component of either open shore `S`-full: if a component missed a
literal `s in S`, its entire external neighbourhood would lie in
`S-{s}`, a separator of order at most six.  Componenthood and the actual
separation exclude every other exit.  Consequently `{q}` being `S`-full
gives

\[
                         N_G(q)=S,
\]

not merely `S subseteq N(q)`: `q` has no neighbour in the other component
of `G[R]`, and there is no `L-R` edge.  Thus `d(q)=7`, and Dirac gives

\[
            \alpha(G[N(q)])\le d(q)-7+2=2.
\]

Since `G[N(q)]=G[S]=H`, the claimed bound `alpha(H)<=2` follows.

## 2. Reorientation and the role of `nu_L=1`

Every component of `G[L]` is a connected `S`-full packet.  If `G[L]` had
two components, those components would be two vertex-disjoint full packets,
contrary to `nu_L=1`.  The actual separation makes `L` nonempty, so `G[L]`
is one nonempty connected component.

Writing `C` for the other component of `G[R]`, removal of `N[q]=S union
{q}` leaves exactly

\[
                         G[L]\mathbin{\dot\cup}C.
\]

Both terms are nonempty, connected, `S`-full, and anticomplete.  This is the
precise two-exterior-component orientation required later; no connectedness
of an arbitrary packet union is being inferred.

## 3. Frozen 129-residual extraction

The theorem explicitly assumes that `H` lies in the frozen 129-graph
residual of the audited adaptive `(1,2)` boundary closure.  Inside that
residual, the independently audited singleton extraction identifies exactly
two graphs with independence number at most two:

\[
                            M\quad\text{and}\quad M+13.
\]

This is precisely the conditional implication used in the proof.  It is not
being promoted to a classification of all seven-vertex graphs with
independence number two.

The frozen verifier was rerun successfully.  Its 129-graph residual has
exactly one `alpha=2` orbit with a safe abstract state and one without; the
audited targeted isomorphism extraction identifies these as the displayed
eleven-edge Moser spindle and its twelve-edge extension `M+13`.

## 4. Applicability of the pure-Moser closure

When `H=M`, apply the complete pure-Moser two-component theorem with its
distinguished degree-seven vertex `v` replaced by `q`.  All of its
hypotheses are literal here:

* `G` is seven-connected, `K_7`-minor-free, and proper-minor-minimal
  subject to not being six-colourable;
* `N(q)=S` induces exactly the displayed pure Moser spindle; and
* `G-N[q]` consists of exactly the two nonempty connected components
  `G[L]` and `C`.

The cited theorem is its full two-component closure, not merely its
order-at-most-three sublemma.  Hence it excludes the pure-Moser branch at
the stated scope.

## 5. The `M+13` contraction model

For `H=M+13`, the displayed edge list verifies that `25` and `46` are
vertex-disjoint nonedges, while `01`, `03`, and the added edge `13` make
`013` a literal triangle.

Put `A_1=G[L]` and `A_2=C`.  For fixed `i` and `j ne i`, define

\[
             U=\{q,2,5\},\qquad V=A_j\cup\{4,6\}.
\]

These are disjoint connected sets.  The first is a star through the
`S`-full singleton `q`; the second is connected because `A_j` is connected
and has a neighbour at each of `4,6`.  The images of `U,V` are adjacent via
`q4` (and also via `q6`).  Each of `0,1,3` is adjacent to the image of `U`
through `q` and to the image of `V` through the `S`-full component `A_j`.
Together with the literal triangle `013`, the five images

\[
                         U,V,\{0\},\{1\},\{3\}
\]

form a literal `K_5`.  Contracting spanning trees of `U` and `V` is a
proper minor operation.

## 6. Expansion, exactness, and gluing direction

Six-colour the minor from Section 5 and retain only the untouched original
side `A_i`.  Expand boundary vertices `2,5` with the colour of the image of
`U`, and `4,6` with the colour of the image of `V`; the internal vertices
`q` and `A_j` are not expanded into this side colouring.  This is proper:

* `25` and `46` are independent;
* every edge from `A_i` to one of those boundary vertices appeared at the
  corresponding contracted image; and
* all other vertices of `S union A_i` were untouched.

The `K_5` forces its five representatives to have distinct colours, so the
boundary partition is exactly

\[
                         25\mid46\mid0\mid1\mid3,
\]

not a coarsening.

For `i=1`, the operation is supported through `q` and `A_2=C` and returns a
colouring of the original closed `A_1`-side.  For `i=2`, it is supported
through `q` and `A_1=G[L]` and returns a colouring of the original closed
`A_2`-side.  Thus the direction is not reversed and no colouring is pulled
back through a contracted carrier on the side where that carrier is used.

The two exact five-block traces can be aligned by a permutation of the six
colour names.  Since `A_1` and `A_2` are anticomplete, the aligned side
colourings glue to a six-colouring of `G-q`.  Exactly five colours occur on
`S`; the remaining colour can be assigned to `q` because `N(q)=S`.  This
contradicts the defining non-six-colourability of `G`.

## 7. Scope and trust boundary

The conclusion is restricted correctly to the frozen 129-boundary residual.
The only finite input is the already-audited identification of its two
independence-two orbits.  The direct `M+13` exclusion is conceptual and uses
no finite minor search.  The mention of exact-seven packet packing in the
dependency list is bookkeeping for the oriented packet vector; once
`(nu_L,nu_R)=(1,2)` is assumed in the theorem, no additional packing claim
is used in Section 3.
