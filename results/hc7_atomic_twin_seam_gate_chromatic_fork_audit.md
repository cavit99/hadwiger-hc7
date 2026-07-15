# Independent audit: atomic twin-seam gate chromatic fork

**Verdict:** GREEN for the chromatic dichotomy, localized common-neighbour
system, generalized ordered paths, model regeneration, row split, triangle
chamber, and matched gate responses.  One conclusion should be weakened:
the existence of two spanning frames and a split-or-separator test does not
by itself prove that the entire target-free residue is already a
“two-frame row-duty lock.”  That phrase is justified only after both frames
have been contact-maximized and every split/transfer alternative has been
exhausted.  The audited source now states this qualification explicitly.

**Audited source:**
`results/hc7_atomic_twin_seam_gate_chromatic_fork.md`.

**Source SHA-256:**
`c9fcaa59038e1f664cc76c7846aa9593d451e4e44173aa26ab8651145d690733`.

## 1. Chromatic dichotomy

Vertex-criticality gives `chi(G-{d,t})<=6`.  A colouring with at most four
colours would extend by assigning two fresh colours to the adjacent
vertices `d,t`, contradicting `chi(G)=7`.  Therefore the only values are
five and six, so the two numerical branches are exhaustive and exclusive.

When the value is five, extending a five-colouring `kappa` by one fresh
colour `gamma` on both `d,t` gives a colouring of `G-f`, and hence of
`G/f`.  The fresh colour occurs nowhere else.  Since `t` lies on both twin
boundaries and `d` lies on neither, `{t}` is literally a singleton block
in both boundary restrictions.  The crossed-state theorem quantifies over
every colouring of `G/f`, so the two mismatches and four previously stated
demand inequalities apply to this canonical response.

## 2. Common neighbours and their localization

Fix an old colour `i`.  If no colour-`i` vertex were common to `d,t`,
recolour every colour-`i` neighbour of `d` with the fresh colour `gamma`,
give `d` colour `i`, and leave `t` in `gamma`.  The recoloured neighbours
are independent and none meets `t`; all other edges remain proper.  This
would six-colour `G`.  Thus every old colour supplies a distinct common
neighbour `v_i`.

The localization is exact.  Since `d in D` and the external neighbourhood
of `D` is `N_G(D)=Omega_D`, every neighbour of `d` lies in
`D union Omega_D`.  If a common neighbour is an old-boundary vertex in
`T_D`, adjacency
to the gate `t` and

\[
                         N_S(t)\subseteq I
\]

put it in `I`.  If it lies in `Z`, it is the other gate.  It is not `t`
itself.  Hence

\[
                         v_i\in D\cup(K-\{t\}).
\]

There are five distinct vertices and only four literals in `K-{t}`, so at
least one `v_i` lies internally in `D`.  The five paths `d-v_i-t` are
internally vertex-disjoint and lie in the `D`-closed side.

Because `gamma` occurs only at `d,t`, the full union of the five
`gamma-i` layers has no internal `gamma` vertex and therefore no common
internal `gamma` palette gate.

## 3. Generalized ordered paths

The ordered-path statement is valid, but should be attributed directly to
Proposition 3.3 of Kawarabayashi--Pedersen--Toft rather than left to the
brief “shortest occurrence” summary.  For a prescribed nonempty sequence
of distinct old colours, extend `kappa` with `gamma` on `d,t` and use the
cyclic permutation

\[
                         (\gamma,i_1,\ldots,i_s).
\]

If the generalized Kempe chain from `d` omitted `t`, rotating the chain
would give a six-colouring of `G-f` with distinct colours at `d,t`, hence
of `G`.  The proposition then yields the literal path

\[
                         d,v_1,\ldots,v_s,t,
             \qquad \kappa(v_j)=i_j.
\]

Although the paper develops the proposition in a globally double-critical
section, its displayed proof uses only `chi(G)=7` and the five-colouring
of `G-{d,t}`.  Thus it applies edge-locally here.

## 4. Regenerated model and first hits

If `chi(G-{d,t})=6`, known `HC_6` gives a `K_6` model in that graph.
Deleting two vertices from a seven-connected graph leaves a connected
(indeed five-connected) graph.  Every component outside the current model
union has an edge to it and may be absorbed wholly into one adjacent bag;
iterating gives a spanning model without losing a clique adjacency.

The path `C-f` is a simple `d-t` path containing the internal edge
`e=zu`.  Hence it contains at least the two distinct internal vertices
`z,u`.  Since the six model bags span `G-{d,t}`, the first model vertex
encountered from each end exists; simplicity and the two internal vertices
make the two first hits distinct.  The source phrase “stop immediately
before” should be read as stopping **at** the first model vertex.

If both hits lie in one row, they are distinct neighbours in that row of
the adjacent poles `d,t`.  Lemma 4.1 of the audited two-pole contact
trichotomy applies verbatim with these poles.  Splitting a spanning tree of
the row at an edge on the path between the hits gives two nonempty,
connected, adjacent pieces.  If both retain all five foreign-row duties,
the seven displayed bags form `K_7`; otherwise the neighbourhood of the
piece missing a duty is an actual separator, of order at least seven by
connectivity.

The same cycle, after deleting `e`, supplies the symmetric first-hit path
for the independently regenerated frame in `G-{z,u}`.  What is not yet
proved is that both frames are already in the residual row-duty-lock
normal form.  Distinct-row first hits, an unoptimized frame, or a separator
of order greater than seven may still require further normalization.

## 5. Triangle chamber and cross-edge check

The contractions of `e=zu` and a spanning tree of the triangle `dvt` are
on disjoint vertex sets.  Lift a colouring of the resulting proper minor,
so

\[
                       c(z)=c(u),\qquad c(d)=c(v)=c(t).
\]

Suppose `z` has an available alternate colour and the free sets of `d,v`
have distinct representatives.  Recolour `z,d,v` with those three repair
colours.  The edge `e` and all three triangle edges are then proper.

The seam geometry excludes every cross-edge except possibly `zt`:

* `z` has no neighbour in `D`, since `D,E` are different components of
  `A-Z`;
* `u` has no neighbour in `D`, because `u in T_E-T_D`; and
* `ut` is absent because `u in B_0` while `N_S(t) subseteq I`.

If `zt` exists, the contracted colouring already gives
`c(z) ne c(t)`, and the colour `c(t)` is present in
`N(z)-{u}`.  It is therefore unavailable for the recolouring of `z`.
Thus this last possible cross-edge remains proper.  The definitions of the
free sets protect every external edge of `d,v`.  The simultaneous repair
would six-colour `G`, proving the stated saturation/matching fork.

For two nonempty free sets, matching number at most one is equivalent to
both being the same singleton: if their union contained two colours, two
distinct representatives could be assigned.  The equivalence in Lemma
2.3 is correct.

Only `z,d,v` are recoloured, and all three lie outside both twin
boundaries.  The retained literals `u,t` keep their colours, so the exact
boundary state is preserved literally.

## 6. Matched gate responses

Under the common singleton free set `{eta}`, recolour `z` with one
available alternate colour.  Recolouring `v` with `eta` leaves precisely
`d,t` equal inside the triangle and gives a colouring of `G-f`; recolouring
`d` instead leaves precisely `v,t` equal and gives a colouring of `G-vt`.
The preceding cross-edge check remains valid, and all edges leaving the
triangle are protected by free-set membership.

The two responses change only the off-boundary vertices `z,d,v` and hence
agree literally on every vertex of both twin boundaries.  Corollary 2.4 is
therefore GREEN.

## 7. Exact correction and scope

The safe conclusion of the equality-six branch is:

> both named edges regenerate spanning `K_6` frames, and the named cycle
> supplies a distinct first-hit pair on each frame; a same-row pair gives
> a literal `K_7` or an actual separator.

Calling every remaining target-free case a “two-frame row-duty lock” adds
an unproved normalization.  Subject to deleting or qualifying that phrase,
the theorem is GREEN.  Neither chromatic branch yet assigns palette
colours to old-boundary duties or model rows, and neither supplies a ranked
receiver.
