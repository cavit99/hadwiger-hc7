# Maximum boundary palette forces a two-sided full-six-colour obstruction

**Status:** written proof; separate internal audit GREEN in
[`hc7_order9_maximum_boundary_palette_audit.md`](hc7_order9_maximum_boundary_palette_audit.md).

This note closes the branch in which every exact-root colouring extending
through either closed shore uses fewer than all six colours on the
nine-vertex boundary.  The argument is independent of Kempe connectivity:
unused colours can be introduced by splitting boundary colour classes, and
maximality then forces the resulting full-six-colour trace to be rejected by
both shores.

## 1. Setting

Let

\[
 V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
 \qquad E_G(A,D)=\varnothing,
\]

where `A,D` are nonempty.  Fix a nonempty independent set `I subseteq B`
and six labelled colours.  A proper colouring of `G[B]` is **exact at
`I`** if colour six occurs on `B` exactly at `I`.

Assume:

1. `|B-I|>=5`;
2. each of the two closed shores `G[A union B]` and `G[D union B]` has a
   proper six-colouring exact at `I`; and
3. `G` is not six-colourable.

For an exact-`I` boundary colouring `phi`, write `q(phi)` for the number of
colours occurring on `B`.  Let

\[
 p=\max\{q(\phi):\phi\text{ extends through }G[A\cup B]
                  \text{ or }G[D\cup B]\}.
\tag{1.1}
\]

The maximum exists by hypothesis 2.  In the live application `I={d}` and
`|B|=9`, so `|B-I|=8`.

## 2. Palette completion

### Lemma 2.1

Let `phi` be any proper boundary colouring exact at `I` which uses fewer
than six colours.  Then there is a proper boundary colouring `phi'`, also
exact at `I`, such that

\[
                         q(\phi')=q(\phi)+1.
\tag{2.1}
\]

Moreover `phi'` is obtained by recolouring one literal vertex of `B-I`
with one previously unused colour from `{1,...,5}`.

#### Proof

Put `r=q(phi)-1`, the number of colours used on `B-I`.  Since
`q(phi)<6`, one of the first five colours is unused on `B`.  Also `r<=4`,
whereas `|B-I|>=5`, so one of the `r` colour classes on `B-I` contains at
least two vertices.  Recolour one vertex of that class with an unused
colour.

The new assignment is proper because the introduced colour occurred
nowhere on `B`.  The old colour remains on the other vertex of its class,
so exactly one new colour is added.  No vertex of `I` is changed and none
receives one of the first five colours, hence the colouring remains exact
at `I`.  This proves (2.1).  \(\square\)

Iterating Lemma 2.1 produces an exact-`I` boundary colouring using all six
colours.

### Theorem 2.2 (maximum-palette dichotomy)

Under the hypotheses of Section 1, exactly one of the following holds.

1. Some exact-`I` boundary colouring `psi` using all six colours extends
   through neither closed shore.
2. Every exact-`I` boundary colouring using all six colours extends through
   exactly one of the two closed shores.

In alternative 1, each open shore contains a connected induced
vertex-minimal subgraph which is uncolourable from the lists left by
`psi` on its literal boundary neighbours.

Moreover, `p<6` forces alternative 1.  Thus alternative 2 forces `p=6`,
but `p=6` alone does not force alternative 2: another full trace may still
be rejected by both shores.

#### Proof

Lemma 2.1 produces at least one exact-`I` boundary colouring using all six
colours.  No boundary colouring can extend through both closed shores:
after a permutation of colour names, the two extensions would agree on
`B` and glue to a six-colouring of `G`.

If some full trace extends through neither shore, fix one such trace as
`psi`; alternative 1 holds.
Otherwise every full trace extends through at least one shore and, by the
preceding paragraph, through at most one.  Hence every full trace extends
through exactly one shore, which is alternative 2.  The alternatives are
exclusive by definition.

Suppose `p<6`.  Choose a boundary colouring `phi` attaining (1.1), and
apply Lemma 2.1 repeatedly until an exact-`I` colouring `psi` using all
six colours is obtained.  Since `q(psi)=6>p`, the definition of `p` says
that `psi` extends through neither closed shore.  Thus alternative 1 holds.

Extending `psi` through the `A`-shore is equivalent to colouring `G[A]`
from the lists

\[
 L_A(v)=[6]-\psi(N_G(v)\cap B).
\]

Because no extension exists, choose an induced non-`L_A`-colourable
subgraph minimal by vertex inclusion.  It is connected, since otherwise
one of its components would already be a smaller obstruction.  The same
argument applies in `D`.  \(\square\)

### Corollary 2.3 (the order-nine endpoint)

In the order-nine exact-`{d}` two-full-shore setting, a full-six-colour
exact trace exists, and exactly one of the following holds.

1. Some full-six-colour exact trace is rejected by both shores and hence
   supplies the paired list-critical subgraphs required by the audited
   full-six endpoint.
2. Every full-six-colour exact trace extends through exactly one closed
   shore.

Indeed, Lemma 2.1 gives existence.  No trace can extend through both shores,
because its two extensions would glue.  Thus failure of alternative 1 says
that every full trace extends through at least one shore and hence through
exactly one.  In particular `p<6` forces alternative 1, while alternative 2
forces `p=6`.

Under the additional seven-connected, proper-minor-critical host hypotheses
of the audited proper-kernel transfer, a selected list-critical subgraph
which is proper in its shore returns that theorem's smaller connected
rejected response.  Consequently, after this transfer outcome has been
explicitly excluded for both selected kernels, the two kernels span their
respective shores.  This is a normalization in the live application, not a
consequence of the hypotheses in Section 1 alone.

Thus the only case not entering the paired full-six endpoint or its stated
proper-kernel transfer is alternative 2.

## 3. Exact scope

The theorem removes the need for surjectivity-preserving Kempe
connectivity in the `p<6` branch.  Its recolouring steps are boundary
operations, not claimed to extend through either shore; maximality is used
precisely to show that the final full-six-colour trace is rejected by both.

The theorem does **not** close all cases with `p=6`.  Although one full
trace then extends through a shore, a different full trace may still be
rejected by both and enter alternative 1.  The true residual is alternative
2, in which every full trace extends through exactly one shore.  The
disconnected surjective-Kempe-space barrier shows why static boundary
connectivity cannot automatically transfer that trace to the opposite
shore.  Closing the residual case requires an internal proper-minor
operation or a literal path/separator argument.

## 4. Dependencies

- the exact-block contraction anchors, for the existence of exact-`I`
  extensions through both closed shores; and
- the audited
  [proper-kernel transfer](../results/hc7_large_boundary_singleton_response_descent.md),
  only for the conditional spanning normalization in Corollary 2.3; and
- the elementary boundary-colouring/list-colouring correspondence.
