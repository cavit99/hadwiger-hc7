# Bichromatic saturation or a bypass at two incident critical edges

**Status:** written proof; separate internal audit GREEN.  This is a uniform
colouring lemma for two incident edges.  Its `HC_7` application supplies a
literal path which bypasses the unique donor-side attachment in the shared
boundary-vertex case, unless one of the two named edges is bichromatically
linked for every alternate colour in a single simultaneous-contraction
colouring.  It does not by itself construct a `K_7`-minor model or preserve a
full valid defect-one configuration.

## 1. Uniform theorem

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and let

\[
                             e=sw,\qquad f=st                 \tag{1.1}
\]

be two distinct incident edges.  Put

\[
                             H=G-\{e,f\}.                    \tag{1.2}
\]

Assume also that `wt` is not an edge.  Assume that the proper minor obtained
by contracting both edges is
`q`-colourable.  Expanding such a colouring to `H` gives a proper colouring
`kappa` with

\[
                         \kappa(s)=\kappa(w)=\kappa(t)=0.     \tag{1.3}
\]

For an alternate colour `i`, call one of the pairs `sw,st`
**`i`-linked** when its two ends lie in the same component of

\[
                         H[\kappa^{-1}(\{0,i\})].             \tag{1.4}
\]

### Theorem 1.1 (saturation or common-end bypass)

For every colour `i!=0`, at least one of `sw,st` is `i`-linked.  Moreover,
at least one of the following holds.

1. One of `sw,st` is `i`-linked for every colour `i!=0`.
2. The graph `H-s` contains a `w-t` path.

In the second outcome there are distinct alternate colours `i,j`, an
`{0,i}`-component `A` containing `w`, and an `{0,j}`-component `B`
containing `t`, such that neither component contains `s` and either

\[
                              A\cap B\ne\varnothing             \tag{1.5}
\]

or there is an edge from an `i`-coloured vertex of `A` to a `j`-coloured
vertex of `B`.

Moreover, interchanging `0,i` on `A` produces a proper `q`-colouring of
`G-f`, while interchanging `0,j` on `B` produces a proper `q`-colouring of
`G-e`.  Thus both opposite one-edge response colourings are obtained from
the same simultaneous-contraction colouring by one named Kempe-component
interchange, and the two interchanges cannot be performed simultaneously.

#### Proof

The nonedge `wt` ensures that expanding the contracted three-vertex class
back into `s,w,t` is proper on `H`: its only two internal host edges are
the deleted edges `sw,st`.

Fix `i!=0`.  Suppose neither pair is `i`-linked.  Let `C_s,C_w,C_t` be
the `{0,i}`-components containing `s,w,t`, respectively.  The component
`C_s` is distinct from each of `C_w,C_t`.  Interchange colours `0,i` on
every component among `C_w,C_t` (only once if `C_w=C_t`).  This remains a
proper colouring of `H`, while both `w` and `t` change colour and `s` does
not.  Both deleted edges can then be restored, giving a `q`-colouring of
`G`, a contradiction.  Thus at least one pair is `i`-linked.

Suppose neither pair is linked for all alternate colours.  Choose `i` for
which `sw` is not `i`-linked.  The first paragraph makes `st` `i`-linked.
Choose `j` for which `st` is not `j`-linked; then `sw` is `j`-linked.
Necessarily `i!=j`.

Let `A` be the `{0,i}`-component containing `w`, and let `B` be the
`{0,j}`-component containing `t`.  Since `sw` is not `i`-linked while
`st` is, the set `A` contains neither `s` nor `t`.  Symmetrically, `B`
contains neither `s` nor `w`.

Interchanging `0,i` on `A` changes the colour of `w` but neither `s` nor
`t`.  Consequently `sw` can be restored and the result is a proper
colouring of `G-f`.  Symmetrically, interchanging `0,j` on `B` and restoring
`st` gives a proper colouring of `G-e`.  These are the asserted two
one-edge responses from the common central colouring.

If `A` and `B` intersect, then their connected union gives a `w-t` path
avoiding `s`, and (1.5) holds.  Assume they are disjoint.  Interchange
`0,i` on `A` and simultaneously interchange `0,j` on `B`.  Each individual
interchange is a valid bichromatic-component interchange.  The simultaneous
assignment can fail to be proper only on an edge between `A` and `B`.
Because the old colouring is proper and the two palettes meet only in
colour `0`, the only possible newly monochromatic edge has an `i`-coloured
end in `A` and a `j`-coloured end in `B`: both ends would change to colour
`0`.

If no such edge existed, the simultaneous assignment would be a proper
colouring of `H` in which `w` has colour `i`, `t` has colour `j`, and `s`
retains colour `0`.  Restoring both `sw` and `st` would `q`-colour `G`, a
contradiction.  Hence the displayed edge exists.  It joins the two
connected subgraphs `A,B`, so their union again contains a `w-t` path
avoiding `s`.  This proves the theorem.  \(\square\)

## 2. Application to a shared rotation interface

Use the connected-subgraph rotation setup in which `W` is the transferred
connected subgraph, `s` is its unique attachment inside the old donor,
`w in W` is adjacent to `s`, and `H_0` is one newly missed named branch
set.  Suppose a selected old contact edge has the form

\[
                             sf_0,\qquad f_0\in H_0.       \tag{2.1}
\]

Thus the donor-interface edge and the lost contact edge share the literal
boundary vertex `s`.  The new deficiency makes `W` anticomplete to `H_0`,
so in particular `wf_0` is absent.  In a graph which is not six-colourable and whose
proper minors are six-colourable, contract both edges `sw,sf_0` and apply
Theorem 1.1 with `q=6`.

### Corollary 2.1 (label-faithful shared-interface alternative)

In one six-colouring obtained from the simultaneous contraction, either

1. one of the named pairs `sw,sf_0` lies in one bichromatic component for
   each of the five alternate colours; or
2. for two distinct alternate colours `i,j`, the graph
   `(G-{sw,sf_0})-s` contains a `w-f_0` path in the union of one
   `{0,i}`-component through `w`, one `{0,j}`-component through `f_0`,
   and at most one edge between those components.  Switching the first
   component gives a six-colouring of `G-sf_0`, and switching the second
   gives a six-colouring of `G-sw`.

In outcome 2, the path has a first vertex

\[
                              r\in N_G(W)-\{s\}             \tag{2.2}
\]

after it leaves `W`.  Hence it is a literal bypass of the unique
**donor-internal** attachment `N_U(W)=\{s\}`; in particular, `r` lies
outside the old donor branch set `U`.

#### Proof

Contracting the two-edge tree on `w,s,f_0` strictly reduces the graph, so
the resulting minor is six-colourable.  Theorem 1.1 gives the two stated
alternatives.  In the second, orient the path from `w` to `f_0` and take
its first vertex outside `W`.  It belongs to `N_G(W)` and is not `s`
because the path avoids `s`.  The one-vertex donor-interface theorem gives
`N_U(W)=\{s\}`, so this first exit is outside `U`.  \(\square\)

Seven-connectivity already gives an uncoloured `w-f_0` path avoiding `s`.
The new content is that this path uses at most three colours in one
simultaneous-contraction colouring and is the union of two named
bichromatic components with at most one joining edge.  The same central
colouring also generates the two opposite one-edge response colourings by
single, explicitly coupled component switches.  It is not yet a clean path
to `H_0`: it may meet another fixed branch set first.  The exact remaining
use is therefore a first-hit branch-set exchange.  The corollary eliminates
the possibility that the shared-interface response is both nonsaturated and
confined behind the unique donor vertex in the three-colour transition
system.

## 3. Sharpness at the Moser spindle

The bypass branch and its possible single cross-edge are both necessary
under the hypotheses of Theorem 1.1.  Let `G` have vertex set
`{0,1,...,6}` and edge set

\[
 \{01,02,05,06,13,16,24,25,34,36,45\}.                 \tag{3.1}
\]

This is a relabelling of the Moser spindle.  It is not three-colourable:
the two triangles on the common edge `16` force vertices `0,3` to have the
same colour, the two triangles on the common edge `25` force `0,4` to have
the same colour, and `34` is an edge.

Take `s=0,w=1,t=2` and delete `01,02`.  The resulting graph has the proper
three-colouring

\[
 (\kappa(0),\ldots,\kappa(6))=(0,0,0,1,2,1,2).          \tag{3.2}
\]

For alternate colour `1`, the pair `02` is linked through `0-5-2`, while
`01` is not linked.  For alternate colour `2`, the pair `01` is linked
through `0-6-1`, while `02` is not linked.  Thus neither named pair is
linked for every alternate colour.  The two components selected in the
proof are

\[
                             A=\{1,3\},\qquad B=\{2,4\},
\]

which are disjoint, and the edge `34` is exactly the required cross-edge.
This example is only a sharpness witness for the uniform colouring lemma;
it is not asserted to satisfy the full `HC_7` hypotheses.

## 4. Dependencies and scope

- [oppositely oriented boundary responses at a rotation](../results/hc7_rotation_opposite_boundary_responses.md)
- [connected deficient-branch-set trichotomy](../results/hc7_connected_one_hole_trichotomy.md)
- [double-contraction lock allocation for disjoint edges](../results/hc7_common_host_double_contraction_lock_allocation.md)

Theorem 1.1 is the incident-edge analogue of the component-switching part
of the last dependency.  Unlike the disjoint-edge statement, its second
outcome records the host path created when the five alternate colours are
not all assigned to one named pair.  No correspondence between palette
colours and minor-model branch-set labels is asserted.
