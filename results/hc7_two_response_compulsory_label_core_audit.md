# Audit of the two-response compulsory-label core

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_two_response_compulsory_label_core.md`](hc7_two_response_compulsory_label_core.md)
at SHA-256

```text
ccf454c4324ee0364e09b4c7c10c48de97a504bf72ab398ee42b073f5f99056f
```

The pre-promotion source SHA-256 was

```text
991143c4b9ffb47b25db3dd21b988ad6f661ed377cba82ca6998d6798de3c6f8
```

Promotion changed only the opening status paragraph, replacing the pending
audit marker by a link to this GREEN audit.  The exact-seven setup, Hall-core
lemma, boundary-multiplicity deductions, and trust boundary are unchanged.
This is therefore a metadata-only promotion of the mathematical revision
checked below, now pinned to the current source path and hash.

The source proves exactly its stated Hall-theoretic and boundary-multiplicity
conclusions.  It does not identify palette colours with branch-set labels,
does not produce disjoint paths or a `K_7`-minor model, and does not prove
that the common boundary colouring extends through both closed shores.

## 1. Setup and saturation

The repaired setup explicitly assumes `chi(G)=7`.  No additional
contraction-criticality hypothesis is needed for the deductions made in
this note, because the two six-colourings and their single Kempe
interchange are assumed directly.

Let `D` be the switched component of the `alpha,beta`-coloured subgraph of
`H=G-{va,vb}`, with `v in D` and `a,b notin D`.

- If `s in N_G(D)-{a,b}` had colour `alpha` or `beta`, an edge from `s`
  to `D` would be present in `H` and would put `s` in the same
  `alpha,beta` component as `D`.  This proves (1.5).
- The two colourings differ only on `D`, so they agree pointwise on the
  open neighbourhood `S=N_G(D)`.
- If the `alpha`-coloured side of `D` had no neighbour of an untouched
  colour `theta`, recolouring that whole side with `theta` would be
  proper.  The side is independent; it has no `theta`-neighbour by
  assumption; and the restored edges become `theta-alpha` and
  `theta-beta`.  The result would be a proper six-colouring of `G`,
  contradicting `chi(G)=7`.

Thus every untouched colour occurs on `S`, and all four rows `R_theta`
are nonempty.  This recolouring argument needs no extra condition such as
`ab in E(G)`.

Because the minor model is spanning and its root branch set is exactly
`{v}`, every vertex of `S` has exactly one of the six foreign branch-set
labels.  Equation (1.5), together with the displayed colours of `a,b`,
shows that `b` is the unique `beta`-coloured boundary vertex in `phi` and
`a` is the unique `alpha`-coloured boundary vertex in `psi`.  Hence the
response-specific rows really are

```text
M_phi={B},  M_psi={A}.
```

This is a literal boundary-label statement, not a colour-to-label
identification.

## 2. Hall-core lemma

Assume the four common rows satisfy Hall.  Their four-element SDR image
sets form the nonempty family `mathcal B`.

For a further row `M`, a five-row SDR exists exactly when some common-row
SDR has image `C` and `M-C` is nonempty.  Therefore it fails exactly when
`M` is contained in every `C in mathcal B`, equivalently when
`M subseteq K`.  This proves (2.4).

Applying this to the singleton rows `{B}` and `{A}` gives `A,B in K` when
both responses fail.  Since `A` and `B` are distinct and every member of
`mathcal B` has order four, `2 <= |K| <= 4` follows.

For `k in K`, deleting `k` from the label ground destroys every common-row
SDR.  Hall gives a nonempty row set `I` with
`|N(I)-{k}|<|I|`.  Original Hall gives `|N(I)|>=|I|`, and deleting one
label changes cardinality by at most one.  Both equalities in (2.6) are
therefore forced.  No matroidal or path-packing assumption is hidden in
this step.

## 3. Boundary consequences

Every common-row SDR uses both compulsory labels `A,B`.  It consequently
selects boundary vertices of two distinct untouched colours in branch
sets `A,B`.  These vertices differ from `a,b`, proving (3.1).

The four SDR vertices have four distinct labels, including `A,B`; adding
`a in A` and `b in B` accounts for six of the seven boundary vertices
with multiplicities `(2,2,1,1)`.  The last vertex either introduces one
new label, repeats one of the two singleton labels, or repeats `A` or
`B`.  These are precisely the three patterns in (3.2).

Finally, `a,b` use the two operated colours, while the other five boundary
vertices use all four untouched colours.  The common colour partition has
block sizes `(2,1,1,1,1,1)`.  The selected vertices in `A` and `B` use
distinct untouched colours, so at most one is in the unique two-vertex
block.  The other, together with `a` or `b` in the same branch set, gives
the asserted same-label pair in distinct singleton blocks.

## 4. Trust boundary

The audited result establishes only a finite label-allocation obstruction
and its literal boundary consequences.  In particular it does **not**
establish any of the following:

- that an SDR corresponds to vertex-disjoint response paths;
- that two vertices with one branch-set label can be separated into valid
  branch sets;
- that a path between the singleton blocks avoids the other boundary
  vertices;
- that either shore realizes the complete displayed boundary partition;
- that a `K_7` minor, compatible order-seven separation, or strict
  host-level descent follows.

Those are correctly left as subsequent host-level obligations in the
source.
