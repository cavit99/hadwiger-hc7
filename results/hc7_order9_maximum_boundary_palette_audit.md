# Independent audit of the maximum-boundary-palette theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order9_maximum_boundary_palette.md`](hc7_order9_maximum_boundary_palette.md)
at SHA-256

```text
261ebe7a6c19c8b8c45b3bc7a2119305c025e8e493b8733069222e26da41ebfa
```

The palette count, one-vertex recolouring, iteration to a six-colour
boundary trace, maximum-palette dichotomy, simultaneous construction of the
two list-critical kernels, and final order-nine dichotomy are correct.  The
conditional statement that both kernels span has been scoped explicitly to
the additional host hypotheses and the exclusion of the audited proper-
kernel transfer; it is not asserted under the elementary hypotheses of
Section 1 alone.

## 1. Exact-block palette count

An exact-`I` colouring assigns colour six to every vertex of `I` and to no
vertex of `B-I`.  Therefore, if `q(phi)` colours occur on the boundary, the
number of colours occurring on `B-I` is exactly

```text
r=q(phi)-1.
```

The set `B-I` is nonempty, so `r>=1`.  If `q(phi)<6`, then `r<=4` and at
least one of the first five colours is unused on all of `B`.  Since
`|B-I|>=5`, the pigeonhole principle gives a colour class of `B-I` with at
least two literal vertices.

Recolour one member of that repeated class with an unused first-five
colour.  This preserves properness of `G[B]`: no boundary neighbour, or
indeed any boundary vertex, had the new colour.  The old colour remains on
another vertex of the repeated class, so no old colour disappears and
exactly one new colour is introduced.  No vertex of `I` changes, and the
new colour is not six, so colour six still occurs exactly on `I`.

Thus the new boundary colouring is proper and exact at `I`, and its palette
has order `q(phi)+1`.  The same hypotheses remain valid after every step.
In particular, when five colours are present, four occur on the at least
five vertices of `B-I`, so another repeated class still exists.  Iteration
therefore terminates with an exact-`I` boundary colouring using all six
colours.  No recolouring step is claimed to extend through either shore.

## 2. Full-palette dichotomy and the role of `p`

Hypothesis 2 supplies at least one exact-`I` boundary trace extending each
closed shore, so the finite maximum `p` is defined.  Necessarily `p<=6`.
Independently, Lemma 2.1 supplies at least one full-six exact trace.

No fixed boundary trace can extend both shores.  Two such extensions induce
the same labelled boundary colouring and glue across `B`, since `A,D` are
anticomplete, contradicting the hypothesis that `G` is not six-colourable.

It follows that exactly one of the source's two alternatives holds.  If
some full trace extends neither shore, alternative 1 holds.  Otherwise every
full trace extends at least one shore and, by the preceding gluing
obstruction, at most one; hence every full trace extends exactly one shore,
which is alternative 2.  These alternatives are definitionally disjoint.

The maximum `p` gives an additional one-way implication.  If `p<6`, start
from a maximizing trace and apply the palette-completion lemma until a
full-six exact trace `psi` is obtained.  This new trace need not extend the
shore from which the maximizing trace came.  Instead, `q(psi)=6>p` proves
directly from the definition of `p` that it extends neither shore, so
alternative 1 holds.  Consequently alternative 2 forces `p=6`.  The
converse is false in general and is not claimed: when `p=6`, one full trace
extends a shore while a different full trace may still be rejected by both.

Thus the source does not silently treat any boundary recolouring as a valid
closed-shore Kempe operation.

## 3. Two simultaneous list-critical kernels

Fix a full-six trace `psi` rejected by both shores.  On the `A` shore,
extending `psi` is exactly the same as colouring `G[A]` from

```text
L_A(v)=[6]-psi(N_G(v) intersect B).
```

The forward implication is restriction.  Conversely, an `L_A`-colouring
combines with `psi`: the lists exclude every colour used on a literal
boundary neighbour, so all `A-B` edges are proper.  Since no extension
exists, `G[A]` has a non-`L_A`-colourable induced subgraph minimal by vertex
inclusion.  Such a subgraph is connected, because otherwise one of its
components would already be a smaller obstruction.  The identical
construction in `D` uses the same trace `psi` and gives a disjoint second
kernel.  This justifies “paired”: both kernels arise simultaneously from
one labelled boundary trace.

No boundary fullness, critical host, Kempe connectivity, or minor-model
label is needed for this elementary kernel construction.

## 4. The clean order-nine dichotomy

The palette-completion lemma gives at least one full-six exact trace in the
order-nine exact-`{d}` application.  Such a trace cannot extend both shores,
by the gluing argument above.  Hence exactly one of the following holds:

1. some full-six exact trace is rejected by both shores, giving the paired
   list-critical kernels; or
2. every full-six exact trace extends through at least one, and therefore
   exactly one, closed shore.

If `p<6`, every full trace is rejected by both, so the first alternative
holds.  The second alternative consequently forces `p=6`.  Conversely,
`p=6` alone does **not** force the second alternative: another full trace
may still be rejected by both.  The revised source states the dichotomy in
this exact form.

## 5. Conditional spanning normalization

The source invokes
[`hc7_large_boundary_singleton_response_descent.md`](../results/hc7_large_boundary_singleton_response_descent.md)
only under its additional seven-connected, proper-minor-critical live-host
hypotheses.  Its current promoted source and audit hashes are

```text
bce97974e2d3d543aaf9ae2f07ff13b61684ddc9cb6bdf08bacdb750c2be2c97  source
5f9afb54fada161d51476e57fd8d1036d29c2ab00a4ac5d1fc88f063945d78df  audit
```

That theorem says that if a selected kernel is a proper induced subgraph
of its shore, a complementary component gives a strictly smaller connected
rejected response under a fresh proper-minor colouring.  Therefore, after
this transfer outcome has been separately excluded for each of the two
selected kernels, both kernels span their respective shores.  This is a
valid normalization of the live endpoint.

It is not a recursive state-preserving descent.  The smaller response may
have a different boundary, a different trace, and no inherited branch-set
labels.  Nor does rejection by both shores, without explicitly excluding
the proper-kernel outcome, itself imply that either kernel spans.

## 6. Trust boundary

The theorem eliminates the need for surjectivity-preserving Kempe
connectivity only in the maximum-palette branch `p<6`.  It does not prove
that the two shore extension languages intersect, close the one-sided
full-six alternative, construct a `K_7` minor, or return a compatible
order-seven separation.  The surviving alternative is precisely that every
full-six exact trace extends through exactly one shore.  Closing it requires
an internal proper-minor operation or literal path/separator information;
no whole-host re-entry is inferred from the palette argument alone.
