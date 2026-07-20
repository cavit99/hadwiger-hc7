# Author self-check: isolated required-set crossing or descent

**Archive note:** this self-check is not an independent audit and is retained
only with the archived exploratory source.

**Status:** author self-check only; this is not a separate internal audit and
not external peer review.  Independent audit remains pending.

The checked source is
[`hc7_order8_isolated_required_set_crossing_or_descent.md`](hc7_order8_isolated_required_set_crossing_or_descent.md)
at SHA-256

```text
53acb7278f9a0fa1b369d516a72ac9bfe3f7e5f869fe54f8b1cbad01bb44283f
```

The dependency revisions consulted were:

```text
ordered two--three allocation
3f62092ab492815d5c21489e001e5732da76bc28454dac75206ba5aa61299dde

positive-excess normal form
b9e913fbece2258d4a9d8448c2ea414a5f2b76df7ab895ffe3a13a115becc9f3

transported-partition Hall reflection
e22e88a66d4a9eed07e1f86888adcb80c7ab826c03de99e4a5a830999f3ccbd4
```

## 1. Verdict on Theorem 1.1

**Author verdict: correct under its displayed hypotheses.**

The two attachment sets

\[
                    X_i=N_G(w_i)\cap E
\]

are nonempty because `w_i in N_G(E)`.  For two nonempty sets, failure of
distinct representatives is equivalent to both being the same singleton.
Thus the Hall step has no omitted third case.

In the positive case, the two `E` endpoints are distinct by construction,
the two middle vertices are the distinct literal vertices `w_0,w_1`, and
the far endpoints lie in the disjoint sets `Q_0,Q_1`.  Since `E`, `B`, and
the components of `G-B` are disjoint, the two displayed paths have no
unrecorded common vertex.

In the negative case, `|E|>=2` is stated explicitly.  Hence `E-u` has a
component `A`.  Connectedness of `G[E]` makes its complete internal
neighbourhood exactly `{u}`.  The common-singleton attachment identity
makes `A` miss both `w_0,w_1`, while componenthood of `E` in `G-B` excludes
every neighbour outside `E union B`.  Therefore

\[
 N_G(A)\subseteq\{u\}\cup(B-\{w_0,w_1\}),
 \qquad |N_G(A)|\le |B|-1.
\]

The component containing `Q_0,Q_1` remains outside this closed side, so
the neighbourhood is an actual separator.  Seven-connectivity supplies
the lower bound seven.

Finally, an `A`--`u` edge exists.  A six-colouring after deleting it has
equal colours on its ends, and the standard restriction-and-gluing
argument proves rejection by the intact `A`-side.  This checks all parts
of the full-neighbourhood response definition, including properness on
both operated restrictions and strict boundary order.

## 2. Entry from the live ordered setting

The isolated Hall form in the positive-excess normal form gives exactly
the cross-miss pattern used by Theorem 1.1, including distinctness of
`w_0,w_1`.  The source does not infer `|E|>=2` merely from the abbreviated
Section 1 of the positive-excess note.  It invokes the full ordered
two--three allocation input, whose Lemma 2.2 proves three distinct vertices
in `N_G(d) cap E`.  This distinction is stated explicitly in Section 2 of
the checked source.

The demand-at-least-two sharpening is also valid.  Relative to the
boundary `B`, the whole connected component `C` is one boundary-full
connected support on the coloured shore.  A demand-one partition therefore
satisfies the matching hypothesis of transported-partition reflection and
would extend through the intact `E`-shore, contradicting the retained
rejection.  Demand zero is impossible for a partition of at least nine
vertices into at most six blocks.

## 3. Proof-spine limitation

The source correctly stops short of a `K_7` conclusion.  After adjoining
`w_0,w_1` to `E`, the guaranteed connected subgraphs are only

```text
E union {w_0,w_1}, Q_0, Q_1.
```

They are disjoint, pairwise adjacent, and full to `S-{e}`.  With the
displayed boundary triangle they give six, not seven, branch sets.  No
fourth boundary-full connected subgraph is present.

The two paths also leave the vertex sets of `Q_0,Q_1` unchanged.  Hence
they do not create a Hall-incidence edge, whose definition requires one
piece to meet every literal vertex of a complete required boundary set.
The protected two-support packing in (3.4) is a sufficient missing input:
the old `P_0`--`P_1` edge makes the two connected subgraphs adjacent, and
component absorption covers all of `C` without losing either root or any
required contact.  The resulting matching is exactly the hypothesis of
transported-partition reflection.

## 4. Second Hall form

The overlap example in Section 4 is a valid literal set-system
obstruction.  A singleton-clique vertex may appear in several required
boundary sets through the anticompleteness clause in their definition.
Thus one missed vertex can delete two incidence edges at the same support.
No theorem in the checked source infers two distinct witnesses in this
case.

## 5. Unresolved assumptions and gaps

- No common equality partition is proved on the two closed shores of the
  returned exact-seven separator.
- The literal crossing pair is not shown to extend to the protected
  two-support packing (3.4).
- The one-sided two-block Hall concentration, including the case of one
  shared singleton-clique witness, remains open.
- Perfect fan augmentation is not used and would not by itself meet a
  complete required boundary set or preserve the two protected roots.

These are scope limitations, not hidden steps in Theorem 1.1.
