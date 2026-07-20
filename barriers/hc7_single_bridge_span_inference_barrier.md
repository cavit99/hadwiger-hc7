# Single-bridge failure does not certify the negative Two Paths case

**Status:** explicit counterexample to an intermediate claim; deterministic
finite verification; separate internal audit GREEN in
[`hc7_single_bridge_span_inference_barrier_audit.md`](hc7_single_bridge_span_inference_barrier_audit.md).
This is not a counterexample to any `HC_7` statement.

## Refuted statement

The following bridge-local inference is false, even when the host of the
fixed path is two-connected:

> Let `D` be a fixed `d`--`e` path and let `p,q` be two further root
> labels.  If no individual `D`-bridge has an off-path component meeting
> both root portal sets, and no open path segment spanned by an individual
> bridge meets both portal sets, then there are no disjoint `d`--`e` and
> `p`--`q` paths.

Consequently, failure of every individual bridge-span exchange cannot by
itself be interpreted as a planar-web certificate.  One must test the
whole Two Paths instance or an equivalent chain of bridges.

## Construction

Let `C` have vertices

\[
                         v_0,v_1,\ldots,v_5,a
\]

and edges

\[
 v_iv_{i+1}\ (0\le i<5),\qquad v_0v_5,qquad av_0,av_1. \tag{1}
\]

Thus `C` is a six-cycle with a new vertex forming the triangle
`a v_0 v_1 a`; in particular, `C` is two-connected.  Add four labelled
terminals with the only terminal--`C` edges

\[
                         dv_0,quad ev_5,quad pv_1,quad qa. \tag{2}
\]

Fix the path

\[
                         D=v_0v_1v_2v_3v_4v_5.        \tag{3}
\]

There are exactly two `D`-bridges:

1. the trivial bridge `v_0v_5`, whose open span is
   `v_1v_2v_3v_4`; it meets the `p`-portal but not the `q`-portal; and
2. the bridge with interior `{a}` and attachments `v_0,v_1`; its open
   span is empty, while its interior meets the `q`-portal but not the
   `p`-portal.

Hence every individual bridge test fails.  Nevertheless the paths

\[
                         d v_0 v_5 e,
                 \qquad p v_1 a q                  \tag{4}
\]

are vertex-disjoint.  Equivalently, the first bridge supplies the root
detour while the span of that bridge composes with the interior of the
second bridge to supply the other rooted path.

## Verification

Run

```text
python3 barriers/hc7_single_bridge_span_inference_barrier_verify.py
```

Expected output:

```text
GREEN single-bridge span inference barrier
C: vertices=7 edges=9 connectivity=2
D-bridges: chord span={v1,v2,v3,v4} hits={p}; triangle interior={a} hits={q}
disjoint linkage: d-v0-v5-e ; p-v1-a-q
scope: bridge-local inference only; no HC7 criticality claim
```

## Exact scope

The construction is not seven-connected, seven-chromatic,
contraction-critical, boundary-full, or `K_7`-minor-free.  It does not
refute the selected proper-minor response theorem.  It only proves that
the bridge-by-bridge failure condition is too weak: different bridges may
compose into the positive linkage.  The classical Two Paths theorem must
be applied to the complete linkage instance, not separately to its
individual bridges.
