# Independent audit of the landing-star closure

**Verdict:** GREEN.

This is a separate internal mathematical audit, not external peer review.  No
unresolved assumption or proof gap was found within the stated landing-star,
star-avoidance, or bounded-response conclusions.

## Audited revision and planned promotion

The audited source was the temporary draft
`/private/tmp/hc7_atomic_two_bridge_subdivision_landing_stars.md`, SHA-256

```text
38c51219e826fa5b0e2a00b7a3de1f65f1f273eaa8ef8892fbf93366e64f12ca
```

The planned promoted source
[`hc7_atomic_two_bridge_subdivision_landing_stars.md`](hc7_atomic_two_bridge_subdivision_landing_stars.md)
differs from that revision only by replacing the status metadata
`active draft; unaudited` with
`written proof; separate internal audit GREEN`.  That exact status-only
replacement has expected promoted SHA-256

```text
2f0156a2ec45b01265703b120b3eb18ad0560bbeaa1cebf0bfb665812efc67c7
```

No theorem statement, proof text, construction, or dependency citation changes
under that replacement.

On 21 July 2026, documentation synchronization narrowed the Section 4
heading and its later summary from the ambiguous phrase "every first-hit
separator" to the exact quantifier already stated and audited in Theorem
4.1: one minimum-cardinality contained separator carries the response when
its order is at most nine; otherwise all contained separators have order at
least ten.  The theorem statement and proof are unchanged.  The resulting
current source SHA-256 is

```text
4430ad1bdb42e9de8f89080dbd4e99e0e5c23389a3dc14b3e02ba2259440bc32
```

## 1. Setup and clean first-hit paths

I reconstructed the thirteen-vertex graph `C` from its literal description:
start with `K_7-{ab,cd}`, add `xa,xb,xc,xd`, replace
`fa,ga,fg,ac` by `f-p-a,g-q-a,f-h-g,a-r-s-c`, and add
`eh,hx,pr,sq`.  This agrees with the cited exact-core theorem.

In `G-(V(K)-{q})`, the component `D_q` contains `q` and no other vertex of
the retained subdivision.  Every neighbour of `D_q` outside it is therefore
in `V(K)-{q}`, so

```text
Omega_q=N_G(D_q) is contained in V(K)-{q}.
```

For each `z in Omega_q`, a path in `D_q` from `q` to a neighbour of `z`,
followed by its last edge, is a `q`--`z` path whose only vertices in `K` are
its ends.  Thus the two clean paths invoked in Theorem 2.1 exist under exactly
the stated hypotheses.

## 2. Branch-set connectedness and disjointness

For arbitrary choices `z_x in X^circ` and `z_e in E^circ`, the proposed bag
`X` is connected.  The path `Q_x` joins `q` to `z_x`, the suffix `L_x` joins
`z_x` to `x`, and `Q_e-{z_e}` is a connected path from `q` to the predecessor
of `z_e`.  Hence all three pieces meet through `q` or `z_x`.  Arbitrary mutual
intersections of `Q_x,Q_e` cause no conflict because every such vertex is
assigned to this same bag.

The other nonsingleton bags are connected for the displayed reasons:

```text
A is the subdivided path a-p-r-s-c,
E is the landing suffix from z_e to e,
F is the subdivided path f-h.
```

The clean-path interiors lie outside `K`.  Their only vertices in `K` are
their prescribed ends, and the two landing regions use distinct core edges.
Although an `x`-landing edge and an `e`-landing edge can share the labelled
end `a` or `c`, both landing suffixes omit that nonlanding end.  Consequently
the seven initial bags are pairwise disjoint.  Allocating each unused route
interval contiguously to a bag containing one of its labelled ends preserves
both connectedness and disjointness and leaves one boundary edge whenever the
two ends belong to different bags.

## 3. All 21 contacts and all landing positions

I checked the following six contacts involving `X`:

```text
XA:qs,  XB:xb,  XD:xd,  XE:yz_e,  XF:xh,  XG_0:qg.
```

The edge `yz_e` is valid for every `Q_e`, including the single-edge case in
which `y=q`.  The remaining fifteen contacts are

```text
AB:cb,   AD:ad,   AE:ae,   AF:pf,   AG_0:cg,
BD:bd,   BE:be,   BF:bf,   BG_0:bg,
DE:de,   DF:df,   DG_0:dg,
EF:ef,   EG_0:eg,
FG_0:hg.
```

These contacts remain valid in every landing category.

- If `z_x=x`, no `x`-landing route is split.  If `z_x` is internal to
  `K_ax` or `K_cx`, that route is split between `A` and `X`, but neither
  route is needed in the displayed contact list; all six named `X` contacts
  remain unchanged.
- If `z_e=e`, no `e`-landing route is split.  If `z_e` is internal to
  `K_ae`, the retained boundary edge is precisely the displayed `AE`
  contact.  If it is internal to `K_eg`, the boundary edge is precisely the
  displayed `EG_0` contact.  If it is internal to `K_ce`, the split creates
  an additional `A`--`E` contact while the displayed contacts through
  `K_ae` and `K_eg` remain unchanged.

Thus every unordered pair of bags has a contact for every possible arm and
every possible position on that arm.  As a supplementary independent check,
I constructed a representative subdivision with three internal vertices on
every core edge, allowed the two external paths to split and rejoin, and
checked all 82 centre/interior landing combinations.  Every combination
reproduced seven connected, disjoint bags and all 21 named contacts.  The
written argument, not this finite representative check, covers arbitrary
route lengths.

## 4. Star avoidance

The cited exact-core theorem excludes from `Omega_q` the five labels

```text
U={b,d,f,h,p}
```

and every internal point of a subdivided core edge incident with a member of
`U`.  The neighbours of `x` are `a,b,c,d,h`; after removing `X^circ`, the
only remaining parts of its open subdivided star lie on `xb,xd,xh`, all
incident with `U`.  The neighbours of `e` are `a,b,c,d,f,g,h`; after removing
`E^circ`, the remaining parts lie on `eb,ed,ef,eh`, again all incident with
`U`.  Therefore a first-hit boundary meeting both complete stars meets both
`X^circ` and `E^circ`, and Theorem 2.1 gives a `K_7` minor.  The stated
one-whole-star avoidance alternative follows exactly.

## 5. Minimum-separator response dichotomy

Under the hypotheses of Theorem 4.1, the terminal certificate gives
`b notin Omega_q`.  The vertex `q` lies in `D_q`, while `b` was deleted when
`D_q` was formed.  Since every edge leaving `D_q` meets its open neighbourhood
`Omega_q`, that neighbourhood is itself a `q`--`b` separator.  Hence the
family of such separators contained in `Omega_q` is nonempty and has a
minimum-cardinality member `S`.

A minimum-cardinality `S` is inclusion-minimal.  If `|S|>=10`, its minimality
proves that every `q`--`b` separator contained in `Omega_q` has order at least
ten, and Corollary 3.1 supplies the simultaneous star-avoidance alternative.
If `|S|<=9`, the audited full response-boundary theorem applies with

```text
r=q,  t=b,  Z=S.
```

Its terminal-disjointness hypothesis holds because
`S subseteq Omega_q subseteq V(K)-{q}` and `b notin Omega_q`.  Its remaining
hypotheses are exactly `HC_5`, seven-connectivity, seven-chromaticity,
`K_7`-minor-freeness, and six-colourability of every proper minor.  It yields
`7<=|S|<=9`, fullness of both distinguished components, four-colourability
of `G[S]`, every exact independent-block response on both closed shores, and
the selected entrance-edge responses.  Finally, `S subseteq Omega_q` and the
exact-core route confinement put every boundary vertex literally on the
stated eight-vertex route skeleton.

## 6. Dependency revisions and trust boundary

The exact dependency revisions checked were:

- exact-core theorem
  [`hc7_atomic_two_bridge_exact_core_seven_fan_closure.md`](hc7_atomic_two_bridge_exact_core_seven_fan_closure.md),
  SHA-256
  `8b9f49194481008bdbae246b439ed1a47a3a8919209e3787e87c1f5767fb1b86`;
- adjacent exact-core audit
  [`hc7_atomic_two_bridge_exact_core_seven_fan_closure_audit.md`](hc7_atomic_two_bridge_exact_core_seven_fan_closure_audit.md),
  SHA-256
  `c5326e4e3f7d68d241c885e3cfde7afe3dbf2bae9630a52b12c5420f2c5917ea`;
- retained exact-core verifier
  [`hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py`](hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py),
  SHA-256
  `4d82cc207c05c1d6a5bf9495ad130acbe4495a47c4b7d600d08b6aec0ed6d319`;
- full response-boundary theorem
  [`hc7_atomic_path_absence_response_boundary.md`](hc7_atomic_path_absence_response_boundary.md),
  SHA-256
  `d6fc8e0024b31439fbdd7fe4f2e20593ba5e01553bef937e2d26aec0032da036`;
- adjacent response-boundary audit
  [`hc7_atomic_path_absence_response_boundary_audit.md`](hc7_atomic_path_absence_response_boundary_audit.md),
  SHA-256
  `775af93aae1c2643e1493ccfd5a60f9219253f0b083e391a89d4003e888eeadd`.

The retained exact-core verifier reran GREEN under `.venv/bin/python`.  This
audit checks the hypotheses and exact use of the two promoted dependencies;
it does not reopen the proofs internal to those hash-matched audited results.
The exact-core source differs from the originally audited promoted revision
only by correcting the displayed verifier command from its former `active/`
path to its tracked `results/` path; its theorem and proof are unchanged.
The landing-star theorem does not force the first-hit boundary to meet both
stars and does not turn the surviving large one-star-avoidance case into a
strict same-form reduction.  Those are explicit scope limits, not gaps in
the audited claims.
