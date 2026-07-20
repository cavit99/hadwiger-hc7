# Independent audit: connected-piece transfers do not canonically permute branch-set labels

**Verdict:** GREEN for the exact source revision identified below.

This is a separate internal mathematical audit.  It checks the literal
inheritance relation, the anchored-cover calculation, the convention-dependent
positional transposition, the reduced rotation-triangle witness, and the
boundary-colouring statement.  It does not prove `HC_7` and does not exclude a
more highly decorated transition system which retains literal vertices,
portals, and operation-specific colouring responses.

## Audited revision

The audited file is
[`hc7_order8_transfer_holonomy_barrier.md`](hc7_order8_transfer_holonomy_barrier.md).

**Source SHA-256:**
`54e62e7b51378565a157c25057d7c268c160b649b63019686cfd310b2d4be912`.

The status-linked source first had SHA-256
`04c306f7a90e950603deff9740392a683c31fd3d1210c422b8b8ea8c0a790a22`.
The current source has SHA-256
`f65d81020e03b4af9121b43fcddb970efb362fb23b3944253e21020f296a264f`.
Relative to the audited mathematical revision, the first change only added
the opening status line and link recording this GREEN audit.  The second is
the one-line terminology replacement
`rooted carrier split` -> `rooted connected-subgraph split` in the list
following Proposition 2.1.  The replacement matches the defined object more
precisely and changes no hypothesis, conclusion, calculation, or proof.
The GREEN verdict therefore applies to the current source hash.

## 1. Literal inheritance is genuinely nonfunctional

Before the transfer, the seven branch sets are

\[
                    X,\ U,\ F_1,\ldots,F_5,
\]

and afterwards they are

\[
                    W,\ X'=X\cup Z,\ F_1,\ldots,F_5,
\]

where `U=Z dotcup W`, the sets `Z,W` are nonempty, and all branch sets in
each displayed model are pairwise disjoint.  Direct intersection therefore
gives exactly

\[
 \{(F_i,F_i):1\le i\le5\}
 \cup\{(X,X'),(U,W),(U,X')\}.
\]

There are no omitted pairs: `X` is disjoint from `U` and all fixed branch
sets, while `Z,W` partition `U` and remain disjoint from the fixed branch
sets.  The old branch set `U` has the two distinct images `W,X'`, so the
relation is not the graph of a partial function.  The new branch set `X'`
has the two distinct preimages `X,U`, so the inverse relation is not the
graph of a partial function either.  Proposition 1.2 is correct.

This is a one-step inheritance statement.  Ordinary relational composition
alone can forget which literal vertex witnessed an intermediate
intersection.  The source's final formulation correctly requires the
relation **together with** transferred vertex support and portal data; it
does not claim that the undecorated relation is a faithful multi-step
ancestry invariant.

## 2. The anchored connected cover has identity transport

In Corollary 1.3, `P_0 subseteq Q_0` and `P_1 subseteq Q_1` are prescribed
literal connected subgraphs.  The transferred set satisfies
`Z subseteq Q_0-P_0`; after the move the correspondingly named parts still
contain `P_0` and `P_1`.  Neither the literal boundary `S` nor either
prescribed subgraph changes.  Thus the induced transport on

\[
                         S\cup\{P_0,P_1\}
\]

is exactly the identity.  Only ownership of the unnamed vertices of `Z`
changes.  No permutation-valued gauge variable is supplied by the anchored
cover normalization itself.

This does not say that an independently overlaid rooted minor model has no
additional labels.  It says only that such labels and their transport are
extra data, not consequences of the anchored bipartition.

## 3. The positional transposition is a convention

If the old centre label is deliberately made to follow `X` into the new
donor `X'`, and the old donor label is made to follow the residual set `W`
into the new centre, the two positional roles are exchanged.  The five
fixed roles remain fixed, so the assigned permutation is the transposition

\[
                         \tau=(\mathsf C\ \mathsf U).
\]

Assigning the names afresh by current role instead gives the identity, while
retaining every literal intersection gives the nonfunctional relation from
Section 1.  Hence the transposition is not canonical.  Once that convention
is imposed, every transfer word of length `k` is assigned `tau^k`; the
listed portal, response, missing-label, and host data do not occur in this
definition.  Proposition 2.1 is therefore correct, but intentionally
tautological: it diagnoses how little the forced positional convention
records.

## 4. The reduced rotation triangle is a valid witness

The cited source
[`hc7_global_invariant_rotation_triangle.md`](hc7_global_invariant_rotation_triangle.md)
has source SHA-256
`09c964ec1b08f3fac7e9cbfc90970e15dfe8c1c5132cc74b3605433e7da3b54f`.
Its deterministic verifier has SHA-256
`f5cedc773de6f11979ca65a945b7a34587e310dd87e248f28bb4a2f9839e0024`.
The verifier was rerun during this audit and printed:

```text
GREEN length=1: core connectivity 5, host connectivity 7; literal reduced rotation triangle verified
GREEN length=8: core connectivity 5, host connectivity 7; literal reduced rotation triangle verified
fixed frame and active carrier union are constant around the cycle
common fixed pair: {p,q}; deleting it leaves the planar tube
```

The three transfers fit the notation of the present source exactly:

1. `X={T}`, `U={u_0} union C`, `Z={u_0}`, `W=C`;
2. `X=C`, `U={T,u_0}`, `Z={T}`, `W={u_0}`;
3. `X={u_0}`, `U={T} union C`, `Z=C`, `W={T}`.

They return to the starting literal configuration and keep the same five
fixed branch sets and the same active vertex union.  The imposed
transposition convention assigns `tau^3=tau`; naming the two positions by
their current roles assigns the identity.  This proves the claimed
convention dependence on an actual legal cycle.

For the barrier it is enough to use the verified icosahedral host.  The same
top-two-ring transfer pattern remains valid in longer capped pentagonal
tubes by absorbing every deeper ring into `F_3`; the length-eight instance
is independently verified.  No conclusion of the present note depends on
an unverified exhaustive claim about arbitrary tube length.

The host is seven-connected and `K_7`-minor-free, and deleting the fixed
pair `{p,q}` leaves its planar core.  Consequently the example does not
refute a theorem allowed to return that coherent pair.  It proves only that
the pair is not encoded by the positional value `tau`.

## 5. Colour-name quotient and response languages

For a fixed closed shore `(H,S)`, changing a selected minor model changes
neither the graph `H`, the literal boundary, nor the set `Ext(H,S)` of
extendable equality partitions.  Modulo a global permutation of the six
colour names, the boundary datum is precisely such an equality partition.
The connected-piece transfer therefore supplies no nonidentity action on
this set and no rule selecting a colouring for a different proper-minor
operation.

The cited opposite-side response theorem is GREEN at its promoted source
hash
`ce7c762b58ca4e109d31d8baa07b11ac73b5349439f4dd9b7f60d8f26ec0af0c`.
It places the donor-interface response in one set difference

\[
 Ext(H_2,S)\setminus Ext(H_1,S)
\]

and each newly lost labelled-contact response in the reverse set
difference.  These differences are disjoint.  The present source correctly
concludes that identifying the two operation-specific responses would need
a new theorem; it is not induced by quotienting colour names.

## 6. Trust boundary

The audited note proves that none of the following, by itself, is a
canonical permutation holonomy carrying the information needed by the
order-eight programme:

- literal branch-set intersections across a split-and-amalgamate transfer;
- the anchored full-subgraph labels of a repartitioned connected shore;
- a forced centre/donor positional convention; or
- equality partitions modulo global colour renaming.

It does **not** prove that every enriched transfer groupoid is trivial.  A
transition object retaining literal vertex provenance, portal ownership,
branch-set roots, and the selected proper-minor response may contain useful
global information.  Classifying such enriched closed transition
components remains the open composition problem.
