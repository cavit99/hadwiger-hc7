# Independent audit of the shared-interface bichromatic-bypass lemma

**Verdict:** GREEN for the exact source revision identified below.

This is a separate internal mathematical audit.  It verifies the uniform
Kempe-component theorem, its conditional application to a shared endpoint in
the connected-subgraph rotation, and the displayed Moser-spindle sharpness
witness.  It is not external peer review and does not prove the outstanding
branch-set exchange.

## Audited revision

The audited file is
`results/hc7_shared_interface_bichromatic_bypass.md`.

**Source SHA-256:**
`5d5a5eda08701262a1bf6b821194aacd7192a41f0ecf997134764b5b59c80961`.

The mathematical source was audited at SHA-256
`aeba9771ecf2fa454322bc10aabfccd7896f2bf29350497a68e6716097e7a0aa`.
The promoted revision changes only the status line from “independent audit
pending” to “separate internal audit GREEN”; restoring the former line
reproduces the audited hash exactly.  No mathematical content changed.

## 1. Expansion of the simultaneous contraction

The two distinct incident edges have the form `sw,st`, with distinct
vertices `s,w,t`.  Contracting both identifies exactly these three vertices.
The hypothesis `wt notin E(G)` is essential: after deleting `sw,st`, it
ensures that the three vertices form an independent set in `H`.  A colouring
of the contracted minor can therefore be expanded by assigning the
contracted colour to all three vertices.  Every other edge of `H` maps to an
edge incident with the corresponding contraction class, so its ends retain
different colours.  Thus the expanded colouring `kappa` used in Theorem 1.1
is proper.

The argument also remains valid if a nominal alternate colour is initially
unused.  In that case the relevant colour-`0` vertices are separate
components unless joined by a colour-`0` path, which a proper colouring
cannot contain; the component-switch contradiction works unchanged.

## 2. The first Kempe-component assertion

Fix an alternate colour `i`.  If neither named pair is `i`-linked, the
`{0,i}`-component containing `s` differs from the components containing `w`
and `t`.  Switching the latter two components, once if they coincide,
preserves properness of `H`, changes both `w,t` from colour `0` to colour
`i`, and leaves `s` at colour `0`.  Restoring both deleted edges would then
give a proper `q`-colouring of `G`.  This contradicts the hypothesis, so at
least one named pair is linked for every alternate colour.

No disjointness between the two switched components is missing here: they
are either identical or distinct components of the same induced
bichromatic graph.

## 3. The nonsaturated alternative and the two responses

If neither named pair is linked for all alternate colours, choose `i` with
`sw` not `i`-linked and `j` with `st` not `j`-linked.  The preceding result
forces `st` to be `i`-linked and `sw` to be `j`-linked, and hence `i!=j`.

Let `A` be the `{0,i}`-component through `w` and `B` the `{0,j}`-component
through `t`.  The linked and unlinked relations imply

\[
  s,t\notin A,\qquad s,w\notin B.
\]

Consequently switching `A` makes `sw` proper while leaving `st`
monochromatic, so restoring `sw` gives a proper colouring of `G-st`.
Switching `B` symmetrically gives a proper colouring of `G-sw`.  The source
therefore correctly obtains both opposite one-edge response colourings from
one simultaneous-contraction colouring.

If `A` and `B` intersect, any common vertex has old colour `0`, and their
connected union contains a `w-t` path avoiding `s`.  If they are disjoint,
performing both assignments can create a new monochromatic edge only when
an old `i`-coloured vertex of `A` is adjacent to an old `j`-coloured vertex
of `B`; both endpoints then change to `0`.  The other three possible old
colour pairs across `A|B` remain differently coloured, while a `0-0` edge
was already forbidden.  If no `i-j` edge existed, both deleted edges could
be restored and `G` would be `q`-colourable.  Thus such an edge exists and
joins the two connected components into the asserted path.

This verifies the phrase that the two named interchanges cannot be carried
out simultaneously: in the intersecting case their assignments disagree on
a common colour-`0` vertex, while in the disjoint case an `i-j` cross-edge
becomes monochromatic.

## 4. Conditional application to the connected-subgraph rotation

The application is correctly conditional on the lost contact edge having
the special form `sf_0`; the general rotation theorem only guarantees an
edge `t_Hf_H` with `t_H` somewhere in the residual donor side.  Under the
stated shared-endpoint assumption, `W` is anticomplete to the newly missed
branch set `H_0`, so `wf_0` is indeed absent and Theorem 1.1 applies to the
two-edge tree `w-s-f_0`.  Minor-criticality supplies the required
six-colouring after contraction.

The theorem's path lies in `(G-{sw,sf_0})-s`.  Starting at `w in W`, its
first vertex `r` outside `W` belongs to `N_G(W)` and is not `s`.  The audited
one-vertex donor-interface identity `N_U(W)={s}` then implies `r notin U`.
Thus Corollary 2.1 proves exactly a bypass of the unique **donor-internal**
attachment, together with the two explicitly coupled one-edge response
colourings.

The source states the necessary limitation: the path may first enter a
different fixed branch set and therefore is not yet a clean connector to
`H_0` preserving the near-`K_7` model.

## 5. Moser-spindle witness

For the displayed eleven-edge graph, the triangles `016,136` sharing edge
`16` force vertices `0,3` to have the same colour in every putative
three-colouring.  The triangles `025,245` sharing edge `25` similarly force
`0,4` to have the same colour, contradicting edge `34`.  Hence the graph is
not three-colourable.

After deleting `01,02`, the displayed vector

\[
 (0,0,0,1,2,1,2)
\]

is proper.  Since `12` is absent and vertices `0,1,2` have one colour, it
also descends to a proper three-colouring after contracting both incident
edges, so every hypothesis used for the sharpness claim holds.

In the `0,1` subgraph the relevant components are `{0,2,5}` and `{1,3}`;
in the `0,2` subgraph they are `{0,1,6}` and `{2,4}`.  Thus neither named
pair is linked for both alternate colours, the selected components are
exactly `A={1,3}` and `B={2,4}`, and their only required joining edge is
`34`.  The example therefore genuinely shows that the nonsaturated bypass
branch, including its single cross-edge subcase, cannot be removed from the
uniform theorem.

## 6. Trust boundary

At the audited hash the source proves:

1. a uniform incident-edge saturation-or-bypass theorem for a fixed
   simultaneous-contraction colouring;
2. two opposite one-edge response colourings obtained by explicitly coupled
   Kempe-component switches; and
3. in the shared-endpoint rotation subcase, a label-faithful three-colour
   bypass of the unique donor-internal attachment.

It does **not** prove that the path avoids all other branch sets, that either
one-edge response has the boundary partition needed by the opposite shore,
that the bypass can be absorbed while preserving a full defect-one
configuration, or that `G` contains a `K_7` minor.  No unresolved gap remains
inside Theorem 1.1, Corollary 2.1, or the Moser-spindle sharpness calculation
at the audited source revision.
