# Independent hostile audit: Moser cyclic-packet completion

Audited files:

* `hc7_exact7_moser_cyclic_packet_completion.md`;
* `hc7_exact7_moser_cyclic_packet_completion_verify.py`.

## Verdict

**GREEN after correcting the selected-portal endpoint case.**  Under the
literal hypotheses of Theorem 1.1, the six displayed certificates lift to
a genuine `K_7` model.  The theorem applies whether the two rich cycles lie
in the same component or different components and requires no edge or path
between them.

The endpoint correction is necessary: if `x=p_i`, one must choose gap
`g=i`, so the artificial edge `6p_g` is already the literal edge `6x`.
Using the preceding gap could route through `p_i`, which that row may place
in a different branch set.  The corrected proof now makes the safe choice
explicit.

## 1. Literal graph and cyclic order

The verifier uses exactly the stated Moser graph

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}
\]

and the portal order

\[
                        2,4,5,3,1,0.
\]

Thus the three Moser duty pairs occur around either cycle as

\[
 \{2,3\},\{1,4\},\{0,5\},
 \{2,3\},\{1,4\},\{0,5\},
\]

in alternating order.  The integer encoding is faithful:
`p_i=7+i`, `q_i=13+i`, and `t=19`.

## 2. The six base certificates

For every `g=0,...,5`, the verifier constructs both six-cycles, adds the
twelve portal edges prescribed by the displayed order, joins `t` to all
seven literal boundary vertices, deletes exactly `p_gp_{g+1}`, and adds
exactly `6p_g`.

The seven bags in each encoded row agree term-for-term with the table.  A
fresh run checks that they are nonempty, pairwise disjoint and connected,
and prints a literal edge witnessing each of the 21 pairwise adjacencies.
Across six rows this checks all 126 bag pairs.  It terminates with

```text
CERTIFIED six gap-avoiding literal K7 models
```

The assertion that `6` and `p_g` occur in the same bag is also checked in
every row.  No row uses the deleted cycle edge.

## 3. An arbitrary literal neighbour of `6`

If `x` lies in the interior of the unique open arc `A_g` from `p_g` to
`p_{g+1}`, row `g` replaces the artificial edge `6p_g` by

\[
                         6x\cup xA_gp_g.
\]

This path lies entirely in the branch set already containing `6,p_g`.
The unused remainder from `x` to `p_{g+1}` may be deleted, so it cannot meet
the bag containing `p_{g+1}`.  If `x=p_i`, the corrected choice `g=i`
makes the replacement path just the literal edge `6p_i`; no preceding arc
is consumed.

Every other subdivided cycle edge lifts in the standard way.  When both
portals lie in one bag, assigning the whole open arc to that bag preserves
connectivity.  When they lie in different bags, splitting the open arc at
one edge preserves a literal adjacency between the two connected bags.
If a base edge is unused, its internal vertices may simply be omitted.
Consequently arbitrary subdivisions create neither a collision nor a
quotient-only adjacency.

## 4. Replacing the universal vertex by the thin packet

Replacing `t` by the actual connected `S`-full packet `T` is literal.
The hypotheses make `T` disjoint from `S`, `P`, and `Q`.  If a table bag
also contains a boundary vertex `s`, fullness supplies a `T-s` edge inside
that bag.  Every cross-bag adjacency formerly witnessed by `ts` is replaced
by an actual edge from some vertex of `T` to the same literal `s`.
Distinct boundary contacts need not use distinct vertices of `T`.

Thus all seven lifted bags remain connected, disjoint and pairwise
adjacent.  They are a literal `K_7` minor, not a colouring or quotient
certificate.

## 5. Component and scope checks

The construction uses only the two cycles, their boundary portal edges,
the clean first-hit path from `6` to one cycle, the thin packet `T`, and
Moser boundary edges.  Extra
vertices and edges can be discarded.  Hence it is unchanged if `P,Q` lie
in one rich component, lie in different rich components, or have arbitrary
unused material around their cycles.

The result does not show that every alternating duty web contains one of
these cycles, and it does not reduce the general exact-seven `(1,2)` state
space to Moser.  Its exact conclusion is nevertheless a literal `K_7` for
the exceptional cyclic-packet hypotheses stated in Theorem 1.1.
