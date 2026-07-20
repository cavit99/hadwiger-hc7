# Independent audit: prescribed omission and paired columns

**Verdict:** **GREEN.** The proofs and their stated trust boundary are correct.

Source under review:
[prescribed omission and paired columns](hc7_order8_prescribed_omission_paired_column_decoder.md)

Mathematical source SHA-256 audited:

    d86e3504b87cfd9fced2ea81bb85613d7b145c70ef177894e634b7ee8edc7358

The source was changed after this review only by replacing its pending-audit
status line with the GREEN verdict.  The resulting promoted source SHA-256 is
recorded at the end of this audit.

## 1. Scope and method

This audit independently checked:

1. the prescribed-first-edge Menger argument in Theorem 2.1, including
   terminal-containing separators and the cases with direct fan limbs;
2. the proper-minor response interpretation and strictness assertion in
   Corollary 2.2;
3. the common-end counts and direct-saturation exception in Corollary 2.3;
4. the two all-boundary fans, the paired columns, and every branch-set
   disjointness and adjacency in Theorem 3.1; and
5. the icosahedral sharpness example and the exact scope of what it refutes.

No pending-audit text in the source or in the earlier audit plan was used as
proof.

## 2. Theorem 2.1: prescribed omission

Let

\[
 D_0=\{v_i\in S\},\qquad U_0=\{v_i\in C-v\},
 \qquad d=|D_0|,quad k=|U_0|=7-d.
\]

Because `C` is a component of `G-S`, every prescribed neighbour not in `C`
lies in `S`; because the graph is simple and the seven incident edges are
distinct, their other ends are distinct.  For `r\in S-D_0`, the target set

\[
 T=S-(D_0\cup\{r\})
\]

has exactly `k` vertices and is disjoint from `U_0`.

If `k=0`, the seven direct edges end precisely at `S-\{r\}`.  Suppose
`k>0`.  The vertex-set form of Menger's theorem for two vertex sets allows a
separating set to contain terminals.  It gives either `k` pairwise
vertex-disjoint `U_0`--`T` paths or a set `Z` of order at most `k-1` for
which no component of `H-Z` meets both `U_0-Z` and `T-Z`, where

\[
 H=G[(C-\{v\})\cup T].
\]

In the linkage case, all `k` source vertices and all `k` target vertices are
used.  Truncating at the first target preserves vertex-disjointness and
ensures that no path contains another boundary vertex.  Prepending the
prescribed edges from `v` and adding the `d` direct edges produces seven
paths, disjoint outside `v`, with end set exactly `S-\{r\}`.  Direct limbs
cannot collide with an internal limb because their ends lie in `D_0`, while
the internal linkage lies in `(C-\{v\})\cup T`.

In the separator case, some `u\in U_0-Z` survives because
`|Z|<|U_0|`.  Let `A` be its component in `H-Z`.  No surviving target lies
in `A`.  Every neighbour of `A` in `C-\{v\}` or in `T` which is not in `Z`
would lie in the same component, while vertices of `S` omitted from `H` are
exactly `D_0\cup\{r\}`.  There are no edges from `C` to the other component
`D`.  Hence

\[
 N_G(A)\subseteq \{v\}\cup D_0\cup\{r\}\cup Z
\]

and

\[
 |N_G(A)|\le 1+d+1+(k-1)=8.
\]

The set `A` is nonempty, connected, and proper in `C` because it omits `v`.
The component `D` lies outside `A\cup N_G(A)`, so the full neighbourhood is
the separator of an actual separation with two nonempty open sides.
Seven-connectivity gives `|N_G(A)|\ge7`.  Finally, `u` is the other end of
one prescribed edge `vu`; since `u\in A` and `v\notin A`, that prescribed
edge crosses the returned full neighbourhood.  This verifies all cases of
Theorem 2.1.

## 3. Corollaries 2.2 and 2.3

For the returned crossing edge `uv`, every six-colouring of the proper minor
`G-uv` makes `u` and `v` equal; otherwise the edge can be restored and `G`
would be six-colourable.  Its restrictions give the same labelled equality
partition on `N_G(A)` on the edge-deleted closed `A`-side and on the intact
opposite side.  If that partition extended through the intact closed
`A`-side, a bijection between its boundary colour blocks, extended to a
permutation of the six-colour palette, would align the two restrictions and
six-colour `G`.  Thus the intact `A`-side rejects the complete partition.
When the boundary has order eight, `A\subsetneq C` makes the connected
response side strictly smaller.  The corollary correctly does not claim that
an order-seven response already supplies compatible intact-shore colourings.

In Corollary 2.3, `p` is a direct prescribed end at both centres, so neither
fan can omit it.  A common omission exists exactly when

\[
 (S-D_C)\cap(S-D_D)=S-(D_C\cup D_D)
\]

is nonempty.  With omissions `r_C,r_D`, the common non-`p` end set is

\[
 S-\{p,r_C,r_D\},
\]

which has six vertices when the omissions agree and five otherwise.  Hence
`D_C\cup D_D=S` is exactly the exception to guaranteed common omission.
Nothing in this count identifies a colour with a branch-set label, and the
source makes no such inference.

## 4. Theorem 3.1: paired all-boundary columns

Apply the fan form of Menger's theorem in `G[C\cup S]`.  If there is no
eight-fan from `v` to the eight vertices of `S`, there is a set
`Z\subseteq V(G[C\cup S])-\{v\}` of order at most seven separating `v`
from every surviving boundary vertex.  The `v`-component `A` of the graph
minus `Z` lies in `C` and has `N_G(A)\subseteq Z`; no neighbour can lie in
`D`, because `C,D` are distinct components of `G-S`.  A vertex
`s\in S-Z` exists.  Boundary-fullness gives it a neighbour in `C`, and no
such neighbour outside `Z` can lie in `A`; in either event `C` contains a
vertex outside `A`.  Thus `A` is a nonempty connected proper subset of
`C`.  The untouched component `D` makes the separation genuine, and
seven-connectivity forces `|N_G(A)|=7`.  The symmetric argument applies at
`w`.

Otherwise truncate an eight-fan at first entry into `S`, so its paths meet
`S` only at their distinct ends.  Replacing the `p`-limb by the direct edge
`vp` is safe: no other limb contains `p`, and the new limb intersects the
others only at `v`.  The same holds for `wp` in the other component.

For every `s\in S-\{p\}`,

\[
 L_s=(P_s^C-v)\cup(P_s^D-w)
\]

is connected through the common literal end `s`.  This remains true if one
or both fan paths are direct edges, when the corresponding centre-deleted
piece is just `\{s\}`.  Distinct columns are disjoint because each fan is
disjoint outside its centre, their boundary ends are distinct, and their
interiors lie in the disjoint components `C,D`.  They avoid `v,w,p`.

The root sets `R_C=\{v,p\}` and `R_D=\{w\}` are connected, disjoint from all
columns, and adjacent through `pw`.  The first edge of the `s`-limb at `v`
joins `R_C` to `L_s`; the first edge of the corresponding limb at `w` joins
`R_D` to `L_s`.  Thus these nine disjoint connected sets realize
`K_2\vee J`, with precisely the inter-column adjacencies recorded in `J`.
If `J` has a `K_5` minor, taking unions of columns over its five connected
branch sets and adjoining the two root sets gives seven disjoint connected
and pairwise adjacent branch sets in `G`.  This is an explicit `K_7`-minor
model.  The converse is neither needed nor asserted.

## 5. Sharpness example

For the displayed capped-antiprism labelling of the icosahedron, direct
adjacency checking gives

\[
 C=\{u_3,u_4,w_3,w_4\},\qquad D=\{u_1,w_1\}
\]

as the two components outside `S`; each has neighbours at all eight vertices
of `S`.  Moreover `C-u_3` is a triangle and `D-u_1=\{w_1\}`.  The graph
`K_2\vee I` is seven-connected: if at least one universal vertex survives a
deletion of at most six vertices it connects the remainder, and if both are
deleted then at most four vertices have been deleted from the
five-connected icosahedron.

It is `K_7`-minor-free.  In any putative clique-minor model, a branch set
containing a universal vertex may be replaced by that singleton.  If the two
universal vertices occupy two distinct bags, the remaining five bags give a
`K_5` minor in the planar graph `I`.  If fewer than two distinct universal
bags are used, at least six of the seven bags can be chosen wholly in `I`,
giving an even larger forbidden clique minor there.  Both contradict
planarity.

The vertices `u_3,u_1` are nonadjacent in the displayed icosahedral
labelling.  Contracting both incident edges `pu_3,pu_1` therefore leaves the
contraction image and `q` as adjacent universal vertices over an induced
planar subgraph, hence a six-colourable minor whose expansion is proper after
deleting the two named edges; this gives `(equal,equal)`.  Contracting only one
edge gives `(equal,proper)` or `(proper,equal)`, because the uncontracted edge
remains an edge.  A proper six-colouring of the original join exists since
the icosahedron is four-colourable, and gives `(proper,proper)`.  Every
icosahedral vertex has degree seven in the join, so its open neighbourhood
is an actual order-seven separator.

Accordingly, the example shows only that the paired fan geometry and the
three positive two-edge signatures cannot force a `K_7` minor without the
universal rejection of `(proper,proper)` (or equivalent operation-specific
criticality) and literal information inside the columns.  It does not meet
the critical-host hypotheses and does not refute the live disjunction.

## 6. Trust-boundary verdict

The source correctly distinguishes its two unbounded host-level theorems
from the unresolved colouring-to-labelled-column coupling step.  It does
not claim that the columns span either shore, that a shore-specific contact
graph is connected, that an order-seven response already glues, or that a
palette colour names a column.  No hidden stronger connectivity assumption
or quotient-to-host lift was found.

The mathematical source at the audited hash is therefore **GREEN**.

Promoted source SHA-256 after the status-only edit:

    7ea7d3a9558113b2143369bd936950918e71dec454c5ae22c5e90f85adb01160
