# Independent audit of the exact-core seven-fan closure

**Verdict:** GREEN.

This is a separate internal mathematical and computational audit, not
external peer review.  No unresolved assumption or proof gap was found
within the exact-core theorem or the stated arbitrary-subdivision
consequences.

## Audited revisions

- theorem note:
  [`hc7_atomic_two_bridge_exact_core_seven_fan_closure.md`](hc7_atomic_two_bridge_exact_core_seven_fan_closure.md),
  SHA-256
  `8b9f49194481008bdbae246b439ed1a47a3a8919209e3787e87c1f5767fb1b86`;
- retained verifier:
  [`hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py`](hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py),
  SHA-256
  `4d82cc207c05c1d6a5bf9495ad130acbe4495a47c4b7d600d08b6aec0ed6d319`.

The mathematically promoted revision changed only the status line from audit
pending to GREEN: replacing that line
by the former text reproduces the draft SHA-256
`b0861b4debbf040c42b0965b68fc8f752dd0128cfc61847e0188914c161302a8`.
The verifier is byte-identical.  The original audit did not alter either
audited file.  In addition to rerunning the retained verifier, I reconstructed the graph
independently from its literal edge description, rechecked every branch-set
pair in the five augmented models, and derived the surviving route skeleton
directly from the edge set.

The current theorem-note hash above includes one later documentation-only
correction: the displayed verifier command now uses the tracked `results/`
path instead of the stale former `active/` path.  The mathematical statement,
proof, certificates, and verifier are unchanged; the immediately preceding
promoted source hash was
`dc5536fa551f1445fc002b54222cf3fa0199f0b68fe095371a9dcfcbf386cca0`.

## 1. Exact graph and five positive certificates

The graph `H_0` has `21-2+4=23` edges.  Subdividing `fa`, `ga`, and `fg`
once and `ac` twice adds five vertices and increases the edge count by five.
Adding `eh,hx,pr,sq` therefore gives

```text
|V(C)|=13,  |E(C)|=32,  N_C(q)={a,g,s}.
```

This agrees with both implementations.  The ordered replacement of `ac` is
literally `a-r-s-c`; in particular, the added edges are `pr` and `sq`, not
edges already present on that route.

For each of `u=b,d,f,h,p`, I checked that the displayed seven sets:

1. are nonempty and partition all thirteen vertices;
2. induce connected subgraphs of `C+qu`; and
3. have an edge between every one of their 21 unordered pairs.

The independent reconstruction reproduced 21 contacts for every row.  Thus
all five rows are genuine spanning `K_7`-minor models.  The proof uses only
these positive certificates and does not rely on the exploratory assertion
that there are no other terminal nonedges.

The retained verifier ran successfully:

```text
GREEN exact two-path atomic-core seven-fan closure
core: vertices=13 edges=32 q_neighbours=a,g,s
terminal_endpoints: b,d,f,h,p; five K7 models verified
forced_fan_endpoints: a,c,e,g,r,s,x
final_model: seven branch sets and 21 named contacts verified
```

## 2. Seven-fan argument and final model

The target set `S=V(C)-{q}` has twelve vertices, so the seven-fan lemma
applies at `q` in a seven-connected host.  Its paths have distinct ends in
`S` and meet pairwise only at `q`.  Truncating at first contact with `S`, if
necessary, makes every path interior disjoint from `S`; simplicity also
keeps `q` out of every interior.  Hence all interiors avoid `V(C)`.

If an endpoint is in `U={b,d,f,h,p}`, contracting the clean fan path up to
one last edge produces `C+qu` as a minor while retaining every edge and
label of `C`.  The five positive certificates exclude all such endpoints
in a `K_7`-minor-free host.  The seven distinct endpoints must consequently
be the whole seven-element set

```text
A={a,c,e,g,r,s,x}.
```

For the paths to `x,e`, let `y` be the predecessor of `e`.  The proposed
bag `X` is connected even when the `q`--`e` path is a single edge, in which
case `y=q`.  The two fan paths otherwise intersect only at `q`; their
interiors avoid the retained graph, `x` belongs only to `X`, and `e` is
omitted from `X`.  Thus the seven final bags are disjoint and connected.
The path `a-p-r-s-c` verifies connectivity of `A_0`, and `fh` verifies
connectivity of `F`.

I checked the full contact table.  In particular, the contacts involving
the fan bag are exactly

```text
qs, xb, xd, ye, xh, qg,
```

and the remaining fifteen are literal retained edges.  The use of `cg` for
`A_0`--`G_0` avoids the `ga` route containing `q`.  The checker independently
validates the same 21 named contacts on two longer representative fan
paths.  The seven bags therefore form the claimed `K_7` model.

## 3. Arbitrary-subdivision statements

Let `K` be a subdivision of `C`.  A `K`-clean path from `q` to a named
terminal `u` has no internal vertex in any retained route.  Together with
`K` it is a subdivision of `C+qu`, so the corresponding positive model
lifts.  Two internally disjoint clean paths from `q` to `e,x` similarly
give a subdivision of the exact augmentation used by the final model;
minor transitivity, or allocation of each unused route interval to one
incident bag, gives the stated lift.

For the first-hit component `D_q`, any neighbour outside `V(K)-{q}` would
belong to the same component.  Hence

```text
Omega_q=N_G(D_q) is contained in V(K)-{q}.
```

If its order were at most six, it would separate `D_q` from one of the many
remaining vertices of `K`, contradicting seven-connectivity.  At equality,
at least five vertices of the thirteen labelled core remain on the opposite
side, so `Omega_q` is the boundary of an actual order-seven separation.

Every attachment in `Omega_q` supplies a clean path from `q`: take a path
inside `D_q` to a neighbour of the attachment and append the last edge.
This proves the literal exclusion (4.2).  If instead the attachment `z` is
internal on the subdivision of a core edge `uv` with `u in U`, contracting
the `z`--`u` part of that route merges `z` into `u` while the remaining
part still represents the original `uv` edge.  Contracting the interior of
the clean `q`--`z` path then supplies the new `qu` edge.  Thus `C+qu` is a
minor without losing the original core edge, which verifies the claimed
extension of (4.2) along every route incident with `U`.

Deleting the five vertices `U` from the literal core leaves exactly the
edges

```text
qa qg qs ar rs sc ae ax ce cg cx eg.
```

Every other core edge is incident with `U`.  The independent edge-set check
reproduced this list exactly, so (4.3) is the precise surviving subdivision
skeleton.  It is only a confinement statement; the source correctly makes
no converse assertion that every point of the skeleton is nonterminal.

Finally, a seven-fan from `q` to `V(K)-{q}` may be truncated so that every
path except its endpoint lies in `D_q`.  Its endpoints are therefore
distinct members of `Omega_q`.  If both literal endpoints `e,x` occurred,
their two paths would be internally disjoint and `K`-clean, and the lifted
final model would give a `K_7` minor.  Thus the endpoint assertion is valid.
The note correctly leaves extraction of a fan containing both endpoints,
or a separator/response consequence of its failure, as an obligation rather
than claiming an arbitrary-subdivision closure.

## 4. Trust boundary

The verifier checks a finite thirteen-vertex graph, the five displayed
positive models, and one representative final model.  NetworkX and Python
assertion execution are inside its software trust boundary; the independent
literal reconstruction and the written fan argument provide separate
checks of the finite and unbounded steps.

The unbounded conclusion applies only when the exact suppressed graph `C`
is retained as a subgraph of a seven-connected host.  The arbitrary-
subdivision section proves the positive lifts, the first-hit boundary and
route confinement, and the prohibition on a seven-fan containing both
`e,x`; it does not prove that such a fan can be selected, that the remaining
attachments are laminar, or that their obstruction already yields a strict
same-form reduction.  These are explicit scope limits, not gaps in the
audited claims.
