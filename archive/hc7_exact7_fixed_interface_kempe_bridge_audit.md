# Independent audit: fixed-interface Kempe bridge

**Archive note:** the broader source draft was discarded before promotion
because its correct colouring statement was subsumed by the sharper audited
exact-cell theorem, while its duty specialization was only conditional.
This audit is retained as provenance for that decision; it is not a live
result.

Audited draft: `hc7_exact7_fixed_interface_kempe_bridge.md` (not retained).

## Verdict

**YELLOW, with a short scope repair.**  Lemma 1.1 and Theorem 2.1 are
GREEN as colouring and literal-path statements.  The word “exactly” and
the final if-and-only-if in Lemma 1.1 are correct.  The bilateral gluing is
correct for `H_1 union H_2`, and the displayed union is a genuine
`U`-clean path or cycle, including the possible trivial first-hit path.

Section 3 overstates the model consequence.  Equation (3.1) produces a
literal `U`-clean root connector for a pair listed in `D`; it is not yet a
carrier discharging the partition-dependent attained duty if its interior
meets a fixed frame bag or if that duty has additional retained-contact
requirements.  In the Moser labelling, `{z_1,z_2}` is indeed the unique
**absent literal root edge between the two displayed pair traces**, but
the source has not proved that an arbitrary current duty `D_U(B)` is
exactly this singleton.  The Moser paragraph must therefore be made
conditional on that particular attained duty.  After those wording changes
the note is GREEN.

## 1. Lemma 1.1: exclusivity and the iff claim

Let `mathcal C_alpha` be the set in the source.  An `alpha/beta` component
swap does not change the component partition; it only interchanges its two
colour names.  Every originally `alpha`-coloured neighbour of `w` must have
its component switched an odd number of times before `w` can receive
`alpha`.  Since `c(w)=beta` and `c` is proper, `w` has no originally
`beta`-coloured neighbour.  Hence switching precisely all components in
`mathcal C_alpha` removes every `alpha` obstruction and creates no new one.

It follows that the two displayed outcomes are complementary:

* if no forced component meets `F`, the simultaneous switch fixes `F`
  pointwise and recolouring `w` works;
* if a forced component meets `F`, that component cannot be switched an
  odd number of times while fixing `F` pointwise.

This also proves the final iff, provided “a collection of component swaps”
has its natural meaning: swaps of the original `alpha/beta` components,
with only parity relevant.  Allowing arbitrary recolourings involving
third colours would be a different and false interpretation, but the
source does not use it.

If the chosen neighbour `p` already lies in `F`, the shortest `p-F` path
has order one.  The lemma remains correct when such trivial paths are
allowed.  This convention should be stated explicitly.

## 2. Bilateral gluing and the path/cycle

If the first application of Lemma 1.1 succeeds, the modified `c_1` agrees
with `c_2` on `U union {w}`.  Every edge of `H_1 union H_2` belongs to one
of the two subgraphs, and there is no open-side edge omitted by the
interface description, so the colourings glue.  The symmetric argument on
side 2 is identical.  In an ambient application one must additionally
state that the two closed sides cover the ambient graph; this is true in
the exact terminal separation.

Assume both switches fail.  A shortest first-hit path on side `i` meets
`U` only in its final vertex `u_i`, except that its initial neighbour may
already equal `u_i`.  All its other vertices lie in the corresponding open
side.  Consequently the two `w-u_i` arms have disjoint interiors.

If `u_1 ne u_2`, their concatenation is a simple path and its only `U`
vertices are its two ends.  If `u_1=u_2=u`, their union gives two distinct
internally disjoint `u-w` paths.  They cannot both be the one-edge path
`uw`: the first would require the common colour of `u` to be `alpha`,
whereas the second would require it to be `beta`.  Hence their union
contains a literal cycle meeting `U` exactly at `u`.  This verifies every
claim in Theorem 2.1, including the degenerate first-hit cases.

The theorem colours and glues `H_1 union H_2`; it does not by itself give
the final missing colour at the original apex.  That final palette count
belongs to the exact HC7 specialization, not this abstract theorem.

## 3. Gate sets and partition-dependent duty

When recolouring fails on both sides, `Z_1,Z_2` are nonempty.  For any
distinct `z_1 in Z_1,z_2 in Z_2`, Theorem 2.1 gives a literal path joining
them whose interior avoids `U`.  Thus (3.1) correctly detects whether the
two gate sets contain the ends of a requested root pair.

The safe conclusion is

\[
 \text{(3.1)}\quad\Longrightarrow\quad
 \text{a literal `U`-clean connector for one requested root pair}. \tag{3.1a}
\]

It is not yet

\[
 \text{a branch-set carrier discharging }D_U(B).               \tag{3.1b}
\]

The connector may run through a previously selected frame bag.  Moreover,
an attained duty can prescribe the block to which the connector must be
assigned and the contacts which the complementary pieces must retain.
Those are not encoded by the unordered endpoint pair alone.  The final
paragraph of the source notices the first issue, but that caveat must also
be reflected in the affirmative sentence immediately after (3.1).

## 4. The Moser singleton claim

In missing-cycle order

\[
                    z_0z_1z_2z_3z_4z_0,
\]

the four cross pairs between `{z_0,z_1}` and `{z_2,z_3}` are

\[
 z_0z_2,\quad z_0z_3,\quad z_1z_2,\quad z_1z_3.
\]

Exactly `z_1z_2` is an edge of the missing cycle; the other three are
literal edges of the present five-cycle complement.  Therefore

\[
 D_{\rm cross}=\{\{z_1,z_2\}\}                         \tag{4.1}
\]

is the exact set of absent literal **cross-root adjacencies** between the
two pair traces.  Negating the two possible orientations of this pair in
`Z_1 times Z_2` gives (3.2), so that formula is correct.

What is not established is the unconditional identity

\[
                         D_U(B)=D_{\rm cross}.          \tag{4.2}
\]

For the application in which the attained duty is specifically to supply
the sole absent cross-root adjacency, (4.2) is an explicit hypothesis and
the Moser specialization is valid.  For another returned partition, or a
carrier that must preserve additional named contacts, the relevant
`D_U(B)` can be different or strictly richer.  The source should replace
“the cross-block duty ... is” by:

> For the particular sub-duty of supplying the sole absent literal
> cross-root adjacency between these pair traces, the requested endpoint
> set is `D_cross={{z_1,z_2}}`.  If the attained duty has exactly this
> endpoint requirement and the connector is clean relative to the selected
> bags, (3.1) discharges it; otherwise (3.2) is only the ordered gate
> obstruction for this sub-duty.

This is the partition-dependent formulation required by the current S3
spine.

## 5. Trust boundary

After the two scope repairs, the proved chain is

\[
 \begin{array}{c}
 \text{failure of both fixed-interface Kempe recolourings}
 \\[1mm]\Downarrow\\[1mm]
 \text{two literal first-hit gates and a `U`-clean through-`w`
 connector for every selected cross-pair}
 \end{array}
\]

with no palette-to-branch-label inference.  Converting one connector into
the attained carrier duty still requires a clean first-hit normalization,
frame reselection, or a label-preserving gate descent.  The theorem does
not reduce `(1,2)` to Moser and does not license an unconditional
defect-at-most-two carrier.
