# Independent audit: canonical `K_6` model after deleting the outer-edge pair

**Theorem revision audited:** SHA-256
`a4e21f3ee4c31c68b091be83798f160972b44f72a80f502f57a62638c08fb30b`.

**Promoted source:** `hc7_outer_edge_canonical_k6_rotation.md`, SHA-256
`4fd9ac24605c69c3801c331524cbdc6159162065053215a26fdeb76de70b1396`.
The only change is the status-line update recorded in the revision note.

**Dependencies checked:**

- [`../results/hc7_order_eight_simultaneous_singletonization.md`](../results/hc7_order_eight_simultaneous_singletonization.md),
  SHA-256
  `ac7b9116d1e1a6fff1916b462d0b10d581cb0c6ab7808cf8bfcfeab48df7360e`,
  and its adjacent GREEN audit;
- [`../results/hc7_atomic_two_pole_contact_trichotomy.md`](../results/hc7_atomic_two_pole_contact_trichotomy.md),
  SHA-256
  `6bce1f570c12a93a7d1830f53905cb1e033bd2e40abed948a70a21ce5100c03d`,
  and its adjacent GREEN audit;
- [`../results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md`](../results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md),
  SHA-256
  `8bc8ebcab599fd614afae5075c8e77384408d1f4750da55c5566439bd1c6d36b`,
  and its adjacent GREEN audit; and
- [`../results/hc7_outer_edge_common_neighbour_completion.md`](../results/hc7_outer_edge_common_neighbour_completion.md),
  SHA-256
  `d9ceb0e832e55ff659dc701ecefa0974a87058fcd6303443b96cc33ec7864731`,
  and its adjacent GREEN audit.

## Verdict

**GREEN.**  Under the displayed balanced-boundary hypotheses, the source
constructs a spanning `K_6`-minor model in `G-{z,u}` without invoking
`HC_6`.  The connected pair `{z,u}` meets exactly five of its six branch
sets.  If the host is `K_7`-minor-free, five is therefore the exact maximum
joint contact over spanning `K_6` models.  The model is reversibly coupled
to the pre-existing singleton-centred spanning `K_7`-minus-one-edge model,
with the same missed singleton branch set.  The adjacent-root colouring
cover and the five Kempe-component connections are also correct.

The note correctly withholds the missing colour-to-branch-set transition.
It neither aligns the six colour classes with the six model branch sets nor
bounds the separator returned by a failed branch-set split.

Two expository qualifications should remain explicit when the theorem is
promoted.  First, the assertions that the separator from the split has
order at least eight and that `G-{z,u}` is five-connected use the canonical
application's additional assumptions that `G` is seven-connected and that
actual order-seven separations have been excluded; they do not follow from
the seven numbered hypotheses in Section 1 alone.  The source currently
states the first assertion conditionally and uses the second only in a
contextual paragraph, so this is not a mathematical defect.  Second, the
phrase in Corollary 3.3 about “the two singleton poles” must be read through
the cited split lemma: the actual seven branch sets are
`{z} union X_z`, `{u} union X_u`, and the five foreign rows, not nine
separate sets.

## 1. Audit of the singletonization input

Hypotheses 1--2 and the two-component boundary-fullness assumption contain
the exact graph-model hypotheses of the simultaneous singletonization
theorem.  Hypothesis 6 is stronger than the admissibility condition needed
there: for every selected admissible endpoint its nonneighbour set in `R`
is nonempty and has order at most one, hence has order exactly one.  Thus no
mate is assigned to `V^+`, and the source's formula

\[
                         V^+=D\cup\{x\}
\]

is exact.  Each mate belongs to precisely one `R`-rooted branch set.  If
both mates enter the same such set, each is adjacent to its common root, so
the set remains connected.  The seven sets in (2.4) are therefore disjoint,
connected, and partition `V(G)`, and their only missing adjacency is the
one between the selected singleton endpoints `q,b`.

## 2. Audit of Theorem 3.1

Put `z=ell_f` and let `u` be its unique neighbour on `e`.  The edge `zu`
makes the deleted pair connected.

### Case `q=u`

Deleting the singleton branch set `{u}` and deleting `z` from the `C`
branch set leaves the six sets in (3.1).  The identity

\[
 C-\{z\}=H\cup\{\ell_e\}
\]

is exact.  This set is connected because `H` is connected and has a
neighbour at `ell_e`.  All five required foreign adjacencies survive:

- `ell_e` is complete to `R`, so the modified `C` set meets every `W_r`;
- the edge from `x` into `H` joins it to `V^+`;
- boundary-fullness gives `b` a neighbour in `C`, and that neighbour is
  not the deleted vertex `z` because `f` is anticomplete to `z`; and
- all adjacencies among `V^+`, the `R`-rooted sets, and `{b}` are unchanged.

The six sets continue to partition `V(G)-{z,u}`.

### Case `q` is not `u`

Here `q'=u`, and because `M_R(q)` is a singleton, `u` lies in exactly the
set `W_{r_q}`.  Removing it leaves the root `r_q` and possibly `b'`.  If
`b'` is present, collective adjacency of `f` to `r_q` supplies the edge
`r_qb'`; hence this reduced branch set is nonempty and connected.

Boundary-fullness gives `q` a neighbour in `C`.  It is adjacent neither to
`z` (by uniqueness of `u`) nor to `ell_e` (because `e` is anticomplete to
`ell_e`), so it has a neighbour in `H`.  Consequently
`(C-{z}) union {q}` is connected.  The surviving root `r_q` preserves the
old adjacencies of its row to the modified `C` row, `V^+`, and the other
`R`-rooted rows.  It meets `{b}` directly unless `b` misses `r_q`; in the
latter case the retained mate `b'` supplies the mate edge.  Absorbing `q`
into `C-{z}` loses no adjacency.  Thus the six sets in (3.2) are pairwise
disjoint, connected, pairwise adjacent, and partition `V(G)-{z,u}`.

### Exact joint contact

In both cases `{b}` is anticomplete to `z` because `f` is anticomplete to
`z`, and to `u` because `e` and `f` are anticomplete.  The other five rows
are contacted as follows:

- `z` has a neighbour in `H`, so it contacts the modified `C` row;
- boundary-fullness gives `u` a neighbour in `D subseteq V^+`; and
- `z` is complete to `R`, so it contacts every reduced `W_r` at its
  surviving root.

These are five distinct rows, proving exact contact five.  A sixth contact
in any `K_6` model, spanning or not, would let the connected set `{z,u}`
serve as a seventh branch set.  Hence a `K_7`-minor-free host has maximum
joint contact exactly five, as claimed in Corollary 3.2.

As an additional falsification check, all 144 possible endpoint-to-`R`
adjacency patterns satisfying the nonempty-disjoint-defect hypotheses were
enumerated on a minimal boundary-full scaffold.  Across all 324 admissible
choices of `q,b`, the displayed sets partitioned `G-{z,u}`, formed a
`K_6` model, and had contact vector with exactly five positive entries and
missed row `{b}`.  This finite test is only a consistency check; the written
argument above proves the unbounded statement.

## 3. Audit of the common-row split

If `q=u`, let `M_R(u)={r_0}`.  The set `W_{r_0}` contains the distinct
vertices `r_0,q'`; the vertex `z` meets `r_0` because it is complete to
`R`, and `u` meets `q'` through the edge `e`.  If `q` is not `u`, the
modified `C` branch set contains the distinct vertices `q` and a neighbour
of `z` in `H`; the edge `uq` supplies the other pole contact.  Thus in both
cases the hypotheses of the audited rooted row-split lemma are literal.

That lemma partitions the common row into adjacent connected pieces
`X_z,X_u`.  If both pieces meet every foreign row, the seven branch sets

\[
       \{z\}\cup X_z,\qquad \{u\}\cup X_u,
       \qquad F_i\quad(i\ne h)
\]

form a `K_7` model.  Otherwise one piece is anticomplete to a foreign row,
so its whole-graph open neighbourhood is an actual separator.  The cited
lemma gives order at least seven only under seven-connectivity.  Exclusion
of order-seven separations then raises this to at least eight, but no upper
bound follows from counting the seven labelled contact requirements.  The
source states this limitation correctly.

## 4. Audit of the reversible exchange

When `q=u`, the forward move transfers `z` from `C` into the singleton
centre `{u}`; the inverse returns it to `C`.  Connectivity is preserved by
a `z-H` edge.

When `q` is not `u`, the forward move transfers `z` and `u=q'` to the pair
centre and transfers `q` from its singleton centre into `C-{z}`.  The
inverse returns `q` to its singleton centre, `z` to `C`, and `u` to
`W_{r_q}`.  Connectivity is witnessed respectively by a `q-H` edge, a
`z-H` edge, the mate edge `qu`, and the forced edge `ur_q`.  Every move is
between disjoint named branch sets, and the reverse assignments recover
exactly (2.1)--(2.4).  The missed branch set is `{b}` at both ends.

Therefore joint contact and branch-set order cannot strictly orient this
two-way exchange.  This conclusion is structural and does not depend on
the separately cited icosahedral example.

## 5. Audit of the colouring cover

Let `J=G-{z,u}` and let `phi` be a six-colouring of `J`.  If each pole
misses a colour in its `J`-neighbourhood and two distinct missed colours
can be selected, assigning those two colours to the adjacent poles would
six-colour `G`.  Hence either one pole misses no colour or both missing sets
are the same singleton.  This proves Proposition 5.1's cover.

A six-colouring of the proper minor `G/zu` restricts to `J`.  It still uses
all six colours because `chi(J)=6`.  The colour of the contracted vertex is
absent from both pole neighbourhoods, so the cover forces the common
singleton outcome.  Its colour class in `J` is nonempty and anticomplete to
both poles, while each pole sees all other five colours.

After giving both poles the common missing colour in `G-zu`, suppose that
for another colour the poles lie in distinct two-colour components.  A
Kempe interchange on the component containing one pole gives the poles
distinct colours and permits restoration of the edge `zu`, a forbidden
six-colouring of `G`.  Thus all five two-colour component connections in
Corollary 5.2 are valid.

If `G` is seven-connected, then `J` is five-connected, so Menger's theorem
does give five vertex-disjoint paths between selected five-element pole
neighbour sets.  The resulting end-colour matching is merely a permutation,
and the paths need not be bichromatic.  The source correctly treats this as
an observation and does not use it to align colours with branch-set labels.

## Exact scope

The canonical deletion model is stronger than the unrooted consequence of
`HC_6`: it is explicit, spanning, has exact joint contact five, and belongs
to a reversible labelled one-hole exchange with the old near-complete
model.  This closes the proposed low-contact optimization route.

It does not close the six-chromatic branch.  Static contact data and the
five Kempe connections do not show that any branch set corresponds to a
colour class, do not produce a common boundary partition, and do not bound
the separator produced by the common-row split.  Those are the exact
remaining obligations.

## Revision note

The audited source had SHA-256
`a4e21f3ee4c31c68b091be83798f160972b44f72a80f502f57a62638c08fb30b`.
Promotion changed only its status line from “independent audit pending” to
“separately audited”; every mathematical statement and proof is otherwise
unchanged from the audited revision.
