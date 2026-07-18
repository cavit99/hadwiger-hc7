# Audit of the atomic three-path quotient completion theorem

**Verdict:** **GREEN** for the theorem exactly as stated.  This is a
separate internal audit, not external peer review.

## Audited revision

- theorem: `results/hc7_atomic_three_path_quotient_completion.md`
- theorem SHA-256:
  `00877886de71201cd7b0472d70a1f65fecc4664fa6abef77695ac324708c41b6`
- checker: `results/hc7_atomic_three_path_quotient_completion_verify.py`
- checker SHA-256:
  `b0033dc11358589931fe1b2cc7066b2e6f8172a6b90226985ff6ea9ee4812c41`

## Verdict

The eighteen labelled vertices are required to be distinct, and the three
displayed systems are valid `K_7`-minor models under exactly the incidences
listed in Section 1.  The three cases exhaust the required contact from
`b_0` to `z_0,z_1,z_2`.

The conclusion is monotone under adding vertices or edges to the host, so it
does apply to an unbounded family of host graphs containing this labelled
configuration.  Its structural content is nevertheless a fixed
eighteen-vertex quotient completion.  It does **not** prove that arbitrary
connected branch sets in the degree-eight three-path problem can be
compressed to this quotient while preserving their labels.

The theorem hash above differs from the line-by-line audited revision
`6f4bd38c88b30596f359fdfa5d13d3c01bad30defef0ddfb5d3bd20491b449e5`
only because its status line was updated from "audit pending" to the GREEN
verdict recorded here; the theorem statement and proof are unchanged.

## Branch-set audit

Number the branch sets in each display from left to right.  Distinctness in
(1.1) makes them pairwise disjoint.  The following edges give spanning trees
inside every nonsingleton branch set.

- For `b_0z_0`, branch set 3 is spanned by
  `u_3a_J,a_Jz_0,u_3u_2,u_2a_I,u_2x_2,x_2x_1,x_1x_0`, and branch set 6 by
  `z_2b_1,b_1z_1`.
- For `b_0z_2`, branch set 1 is spanned by
  `x_1u_1,u_1u_2,u_2a_I,u_2x_2,x_1x_0`, branch set 4 by `z_0b_1`, branch set
  5 by `a_Ju_3,a_Jz_1,u_3x_3`, and branch set 6 by `z_2b_0`.
- For `b_0z_1`, branch set 1 is spanned by
  `u_0x_0,u_0z_0,x_0x_4,z_0a_J`, branch set 2 by `b_0z_1`, branch set 3 by
  `x_2b_2`, branch set 5 by `u_3u_2,u_2a_I`, branch set 6 by `z_2b_1`, and
  branch set 7 by `vx_1,x_1u_1`.

For completeness, one witness edge for every unordered pair of branch sets
is listed below.  The pair `ij` refers to branch sets `i` and `j`.

```text
b0-z0:
12 b0-b2   13 b0-z0   14 b0-x3   15 b0-x4   16 b0-b1   17 b0-v
23 b2-aJ   24 b2-x3   25 b2-x4   26 b2-b1   27 b2-v
34 u3-x3   35 x0-x4   36 aI-z1   37 x0-v
45 x3-x4   46 x3-b1   47 x3-v
56 x4-b1   57 x4-v    67 b1-v

b0-z2:
12 x0-b2   13 x0-x4   14 aI-z0   15 aI-z1   16 aI-z2   17 x0-v
23 b2-x4   24 b2-b1   25 b2-aJ   26 b2-b0   27 b2-v
34 x4-b1   35 x4-x3   36 x4-b0   37 x4-v
45 b1-x3   46 b1-b0   47 b1-v
56 aJ-z2   57 x3-v    67 b0-v

b0-z1:
12 aJ-z1   13 aJ-b2   14 x4-x3   15 aJ-u3   16 aJ-z2   17 aJ-u1
23 b0-b2   24 b0-x3   25 z1-aI   26 b0-b1   27 b0-v
34 b2-x3   35 x2-u2   36 b2-b1   37 b2-v
45 x3-u3   46 x3-b1   47 x3-v
56 aI-z2   57 u2-u1   67 b1-v
```

Every edge in this certificate occurs in items 1--7 of Section 1.  Thus the
proof does not rely on an unlisted edge.  The alternatives `b_0z_0`,
`b_0z_1`, and `b_0z_2` exhaust item 7, even when more than one of them is
present, because any one applicable model suffices.

## Checker replay

The checker constructs precisely the edge set of Section 1 plus the selected
`b_0z_k` edge.  Its explicit `require` checks test nonemptiness,
disjointness, connectedness, and all 21 pairwise adjacencies.  It contains no
correctness-critical Python `assert`.

Both commands completed successfully with the same output:

```text
python3 results/hc7_atomic_three_path_quotient_completion_verify.py
python3 -O results/hc7_atomic_three_path_quotient_completion_verify.py

b0-z0: K7 model verified
b0-z2: K7 model verified
b0-z1: K7 model verified
GREEN: the three possible b0-to-{z0,z1,z2} contacts are exhausted
```

## Trust boundary

This audit certifies the explicit minor construction only.  It does not
certify a label-preserving compression from nonsingleton connected branch
sets, distinct first hits of three paths, seven-connectivity,
contraction-criticality, or any implication establishing that every
hypothetical `HC_7` counterexample contains this quotient.
