# Independent internal audit: common-label paired-fan barrier

**Verdict:** GREEN for the exact revisions

```text
barriers/hc7_common_label_paired_fan_k7_barrier.md
SHA-256 c1edb8451f6dba881f417055fe79564b1cf2e117cbfb786f80aa434ea84f9438

barriers/hc7_common_label_paired_fan_k7_barrier_verify.py
SHA-256 a4a8c30a657dcc8855547cf9b9f162f879fdb1167a6b85b1f55b0d1ce2cccfcc
```

This is a separate internal mathematical audit, not external peer review.
It checked the literal graph, minor model, paired fan, operation responses,
compatible separator, and the exact trust boundary.

## 1. Host and labelled model

The verifier imports the independently checked icosahedral construction
`G=K_2\vee I`.  Exhaustive deletion checks give seven-connectivity, while
planarity of `I` excludes a `K_7` minor: after removing the at most two
branch sets containing the universal vertices, five pairwise adjacent
branch sets would remain in `I`.

The displayed eight-set has precisely the two stated complementary
components, and both components are adjacent to all eight literal boundary
vertices.  The seven displayed branch sets are nonempty, connected,
disjoint and spanning.  Every pair is adjacent except

\[
                           X=\{d\},\qquad Y=\{u_0,u_1\},
\]

which are anticomplete.  The selected component `C` lies wholly in `U`.
The retained set `U-C=\{t,u_2\}` is connected and adjacent to `C`, and the
two retained vertices are exactly the two boundary vertices labelled `U`.

## 2. Paired fan and response signatures

The source path is `u_3u_4w_4`.  All five displayed limbs are literal host
edges.  Their terminal vertices have the five distinct common labels
`U,D,F_1,F_2,F_3`; outside the source path they are pairwise disjoint and
meet the boundary only at those terminals.  The edges

\[
                           e=u_3w_2,\qquad f=w_4w_0
\]

are vertex-disjoint and have distinct boundary labels.

Each row of the colouring table was checked on every host edge.  The rows
`EE`, `EP`, and `PE` are respectively valid expansions of colourings after
contracting both designated edges, contracting only `e`, and contracting
only `f`.  The row `PP` is a proper six-colouring of the original graph.
Therefore the positive contraction responses do not force a `K_7` minor,
and the example fails precisely the no-`PP` condition within the
operation-signature coordinate.

## 3. Compatible separator and scope

The displayed seven-set is an actual separator with the two stated open
components; both designated edges cross it.  For each of `EE`, `EP`, and
`PE`, the verifier checks a proper whole-graph colouring inducing the same
equality partition on this separator.  Thus the example lands in, rather
than refutes, the compatible-separator alternative.

The source's scope qualification is necessary and correct.  Relative to
the retained donor `\{t,u_2\}`, exactly two outside branch sets have all
their donor contacts confined to `C`; the example does not realize the
full upstream three-owner concentration hypothesis.  It establishes that
the paired geometry and existential positive responses alone cannot force
branch-set repair.  It does not establish that no-`PP` is sufficient, and
it does not refute a theorem using all contraction-critical hypotheses.
