# An all-boundary fan from a connected subgraph at an eight-separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_all_boundary_source_fan_audit.md`](hc7_order8_all_boundary_source_fan_audit.md).
This note
gives an unconditional host-level fan-or-separation theorem and records the
exact interval obstruction to dividing the resulting boundary-contact limbs
between two connected subgraphs.  It does not identify a boundary vertex
with its inherited minor-model branch set, supply prescribed attachment
roots inside a connector, force the interval condition, or prove `HC_7`.

## 1. All eight boundary vertices can be reached simultaneously

### Theorem 1.1 (all-boundary fan or an order-seven separation)

Let `G` be seven-connected, let `S` be an eight-vertex set, and let `C` be
a component of `G-S`.  Assume that `G-S` has another component and that

\[
                         N_G(C)=S.                     \tag{1.1}
\]

Let `P` be any nonempty connected subgraph of `G[C]`.  Then at least one
of the following holds.

1. There are eight paths from `P` to the eight distinct literal vertices
   of `S`.  The paths are pairwise vertex-disjoint outside `P`, and each
   path meets `S` only at its terminal vertex.
2. There is a nonempty connected proper set `A subsetneq C` such that

   \[
                            |N_G(A)|=7.                 \tag{1.2}
   \]

   Its full neighbourhood is the boundary of an actual separation with
   two nonempty open sides.

Moreover, in outcome 1, let

\[
                        p_1s_1,\ldots,p_rs_r           \tag{1.3}
\]

be any edges with `p_i in V(P)` and with distinct ends `s_i in S`.  The
eight paths may be chosen so that the path ending at `s_i` is the literal
edge `p_is_i` for every `i`.

#### Proof

Contract a spanning tree of `P` to one vertex `p` in the graph

\[
                         H=G[C\cup S]/P.               \tag{1.4}
\]

Apply the fan form of Menger's theorem from `p` to the eight-set `S`.
If an eight-fan exists, lift the contraction and stop each path at its
first vertex of `S`.  The lifted paths have the properties in outcome 1.

For every prescribed edge `p_is_i`, the contracted graph contains the
edge `ps_i`.  Replace the fan path ending at `s_i` by that edge.  Since
the terminal vertices are distinct, these replacements create no
intersection away from `p`.  Lifting the contraction replaces `ps_i` by
the prescribed literal edge `p_is_i`, proving the final assertion.

Suppose no eight-fan exists.  Menger's theorem gives a set

\[
          Z\subseteq V(H)-\{p\},\qquad |Z|\le7,        \tag{1.5}
\]

which separates `p` from `S-Z`.  Let `A` be the literal lift in `C` of the
component of `H-Z` containing `p`.  No member of `S` belongs to `A`, and
componenthood in (1.4), together with the fact that `C` is a component of
`G-S`, gives

\[
                            N_G(A)\subseteq Z.          \tag{1.6}
\]

The set `A` is nonempty and connected.  Since `|S|=8>|Z|`, choose
`s in S-Z`.  Boundary-fullness gives an edge from `s` to `C`; no end of
such an edge belongs to `A`, by the definition of the `p`-component.
Thus `A` is a proper subset of `C`.  The vertex `s`, and also every vertex
of the other component of `G-S`, lies outside `A\cup N_G(A)`.  Hence
`N_G(A)` is a genuine separator.  Seven-connectivity and (1.5)--(1.6)
force

\[
                   7\le |N_G(A)|\le |Z|\le7.           \tag{1.7}
\]

Therefore `N_G(A)=Z` and (1.2) holds.  This is outcome 2. \(\square\)

### Minimum-shore application (nonterminal)

If `C` lies properly inside the connected shore of a minimum-order generic
exact-seven response interface in the fixed graph `G`, outcome 2 supplies
an actual order-seven separation with a smaller connected open side.  An
edge from that side to its full neighbourhood and an edge-deletion
six-colouring give the data used by the generic restart theorem.  In that
specific setting minimality therefore excludes outcome 2.

This is an application of the separately proved generic restart theorem,
not an additional conclusion of Theorem 1.1.  Proper containment is
essential: without it, outcome 2 is an exact order-seven return but need not
be a strict restart relative to an independently selected shore or preserve
any previously selected boundary partition.

## 2. What the fan proves about two boundary-contact subgraphs

In outcome 1, replace every lifted path by the suffix beginning at its last
vertex of `P`.  Denote the resulting path ending at `s` by `L_s`, and its
unique vertex on `P` by `x_s`.  If `P` is a path, then

\[
             T_P=P\cup\bigcup_{s\in S}L_s             \tag{2.1}
\]

is a tree: its eight limbs have distinct ends and are pairwise disjoint
outside the spine `P`.

For a nonempty set `Q subseteq S`, let `I_P(Q)` be the smallest subpath of
`P` containing all attachment vertices `x_s`, `s in Q`, and put

\[
 T_P(Q)=I_P(Q)\cup
        \bigcup_{s\in Q}\bigl(L_s-s\bigr).             \tag{2.2}
\]

The terminal vertices themselves are omitted in (2.2), so the resulting
subgraph lies in `C`, is disjoint from `S`, and has a literal edge to each
member of `Q`.  Disjointness from a whole inherited minor-model branch set
containing a terminal requires a separate containment hypothesis.

### Theorem 2.1 (exact interval criterion inside the fan)

Let `Q_1,Q_2` be disjoint nonempty subsets of `S`.  The fan tree `T_P`
contains vertex-disjoint connected subgraphs `R_1,R_2` such that `R_i`
contains `L_s-s` for every `s in Q_i` if and only if

\[
                         I_P(Q_1)\cap I_P(Q_2)=\varnothing. \tag{2.3}
\]

When (2.3) holds, the two subgraphs can be enlarged, using only vertices of
connected `C`, to a partition

\[
                         C=C_1\mathbin{\dot\cup}C_2    \tag{2.4}
\]

into nonempty connected adjacent sets with `T_P(Q_i) subseteq C_i`.

#### Proof

The graph `T_P` is a tree.  Every connected subgraph containing the rooted
limbs `L_s-s`, `s in Q_i`, contains their spine attachment vertices and
the unique paths between them, and therefore contains `I_P(Q_i)`.  Thus
disjoint rooted subgraphs imply (2.3).

Conversely, under (2.3), the two sets `T_P(Q_1),T_P(Q_2)` are connected
and vertex-disjoint.  If they are not adjacent, take a shortest path in
connected `G[C]` between them and assign its internal vertices to the first
set.  They remain disjoint and connected and become adjacent.  Contract
the two sets, extend their joining edge to a spanning tree of the resulting
connected graph, and delete that tree edge.  Lifting its two components
gives (2.4) and preserves both rooted subgraphs. \(\square\)

## 3. Exact remaining obstruction

The all-boundary fan removes repeated boundary endpoints and supplies one
literal contact with every inherited boundary label.  It does **not** make
two chosen demand intervals disjoint.  If they overlap, the
unique paths in the fan tree force both proposed rooted connected subgraphs
to use a common spine vertex.  This is the literal portal-order obstruction
which must be changed by a proper-minor response or converted into a
compatible order-seven separation.

Nor does Theorem 2.1 supply a rotation datum.  Its subgraphs omit every
boundary terminal, including any terminal informally described as an
"attachment root".  In the audited rotation theorem the roots are literal
vertices already lying inside the connector, while the order-eight fan
terminals lie in the separator outside `C`.  These objects cannot be
identified.

A valid application to a near-`K_7` rotation would therefore need additional
host data: five whole pairwise-adjacent branch sets; two literal roots inside
one connector; disjoint paths from those roots into the two interval
subgraphs; and, for every required row, the final interior portal of its fan
limb, with the separator terminal itself omitted.  It must also prove that
all these objects lie in the connector and remain disjoint.  Only after that
independent rooting and containment work could Theorem 2.1 divide the row
contacts between two sides.  No such embedding is asserted here.

## 4. Dependencies and trust boundary

- the fan form of Menger's theorem;
- the [generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md),
  used only in the nonterminal minimum-shore application above.

Theorem 1.1 and Theorem 2.1 are the only promoted mathematical claims in
this note.  They are unbounded literal-host statements.  The note does not
produce the attachment-root paths required by a near-`K_7` rotation, preserve
a selected boundary equality partition in outcome 2, force the interval
condition, or prove the active order-eight theorem.
