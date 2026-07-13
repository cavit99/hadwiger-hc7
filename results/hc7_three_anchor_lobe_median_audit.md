# Independent audit: three-anchor lobe-median exchange

## Verdict

**GREEN.**  The owner/minimality and spine-scope repairs in Section 6
have all been applied and rechecked.  The two complementary bag
constructions are sound.  With ownership defined over all actual
interbag edges, their
missing-pair counts are exact, Theorem 3's numerical dichotomy is
exhaustive, the `K_3 join C_4` carrier is literal, and the two-packet
promotion gives a genuine `K_7` model.

The repaired note also keeps the exact trust boundary: an abstract
failed bag-to-bag linkage is a valid next input but is not automatically
the rural side of the guarded-cycle theorem until a specific connector
or adhesion is supplied.

## 1. Ownership and detachable-part minimality

For every foreign row `Q`, ownership must mean

\[
 E_G(F,Q)\ne\varnothing
 \quad\text{and every edge in }E_G(F,Q)
 \text{ has its }F\text{-end in }L.                    \tag{A.1}
\]

All five row contacts are required, so the nonemptiness is automatic.
Definition (A.1), rather than ownership of one chosen model edge, is
what makes `F_0-Q` absent exactly when `Q` is owned.

The theorem itself may simply retain (1.5) as an explicit hypothesis.
If the note also derives it, the valid comparison statement is:

* the host is in the no-`K_7` branch;
* `F_0-A` is retained, as already assumed in (1.2); and
* `F` is minimal in a comparison class permitting every nonmissed row
  `R_i` to be enlarged by a detachable part of `F`.

With no owner, delete `L`.  With sole owner `R_i`, move `L` into
`R_i`; an actual `L-R_i` edge connects the enlarged row, the
`L-F_0` cut edge restores its contact with the residual row, and every
other contact survives.  With sole owner `D`, the same transfer uses
the assumed `L-D` edge, repairs `AD` through `L-A`, and restores
`D-F_0` across the cut.  The seven bags are then a literal `K_7`,
contrary to the no-`K_7` branch.  Thus at most one owner is impossible.

The phrase “after the other six labelled bags have been fixed” must be
removed or replaced by this permitted-transfer comparison class.  If
exact absence of `AD` is required throughout the comparison class, the
sole-`D` move is a terminal `K_7` outcome, not a smaller member of that
class.

## 2. Rotation model

Put `D'=D union L` and retain `F_0`.  The bags are disjoint.  `D'` is
connected through `L-D`; `F_0` is connected; the nonempty cut
`E(L,F_0)` gives `D'F_0`; `L-A` repairs `AD'`; and the retained
`F_0-A` edge preserves the centre contact.

All pairs not incident with old `F` survive.  For a neutral row `R_i`,
(A.1) gives

\[
                E(F_0,R_i)=\varnothing
                \quad\Longleftrightarrow\quad
                R_i\in\Omega(L).
\]

Ownership of `D` causes no missing pair because the cut edge supplies
`D'F_0`.  Therefore the missing pairs are **exactly**

\[
            \{F_0R_i:R_i\in\Omega(L)\cap
              \{R_1,R_2,R_3,R_4\}\},                  \tag{A.2}
\]

not merely an unspecified subset.  They form a missing star of order
`o` at `F_0`.

## 3. Median model and numerical dichotomy

For `X=A union F_0` and `Y=L`, connectivity follows from `A-F_0` and
the lobe hypotheses, while the lobe cut gives `XY`.  The edge `YD` is
assumed, every `XR_i` uses the old `A-R_i` edge, and the five bags
`D,R_1,...,R_4` retain their clique adjacencies.

Since `AD` is genuinely absent,

\[
 XD\text{ is absent}\iff F_0D\text{ is absent}
        \iff D\in\Omega(L).
\]

Likewise `YR_i` is absent exactly when `L` does not meet `R_i`.  Hence
the median model has exactly `d+4-k` missing pairs, with the first
possible defect at `XD` and all remaining ones incident with `Y`.

Theorem 3's cases are exhaustive:

* if `o<=2`, (A.2) gives the missing-star model with at most two spokes;
* for `o>=3`, one has `k>=o>=3`;
* if `d=0`, then `d+4-k<=1`;
* if `d=1,k=4`, the count is one; and
* the sole remaining case is `d=1,k=o=3`.

In that last case, after relabelling, `D,R_1,R_2,R_3` are exactly the
owners, `L` meets precisely `R_1,R_2,R_3`, and the median model misses
exactly `XD` and `YR_4`.  These two pairs have four different endpoints.
There is no omitted ownership/contact pattern.

## 4. The literal carrier and packet promotion

In the exceptional case the three rows `R_1,R_2,R_3` are pairwise
adjacent and meet each of `X,Y,D,R_4`.  The latter four bags contain the
literal cycle

\[
                          X-Y-D-R_4-X:
\]

use respectively the lobe cut, `L-D`, the old `D-R_4` edge, and the
old `A-R_4` edge inside `X-R_4`.  Its only absent diagonals are `XD`
and `YR_4`.  Thus these seven bags model exactly
`K_3 join C_4=K_7-2K_2`.

For Lemma 4, `X union K_1` and `Y union K_2` are disjoint connected
bags.  The contacts `K_1-D` and `K_2-R_4` repair the two diagonals;
all old contacts, including `X-Y`, survive.  Together with
`D,R_1,R_2,R_3,R_4` they are seven pairwise adjacent connected bags, a
literal `K_7` model.

The equivalent path formulation is also correct.  Since `XD` and
`YR_4` are absent, each prescribed path has a nonempty connected
interior outside the seven bags.  Vertex-disjointness makes the two
interiors disjoint, and their end edges give exactly (4.1).

## 5. Exact HC7-spine contribution

The theorem eliminates all row **support patterns** at this lobe:

1. a missing star with at most two spokes is a legitimate input to the
   existing one-/two-hole height and rotation machinery;
2. `K_7` is terminal and `K_7^-` is a legitimate near-clique spine
   input; and
3. the exceptional state is a fixed `K_3 join C_4` carrier with two
   independent repair demands.

This is substantive local progress, but outcome 3 is not yet a rural
or two-apex conclusion.  Failure of the two packets is a set-to-set
two-linkage problem.  To invoke a set-root rural theorem one still needs
the four portal sets to be nonempty and pairwise disjoint inside a fixed
4-connected connector.  To invoke the guarded-cycle theorem one needs
an actual cyclic-shore/adhesion realization.  Without one of those
extra structures, the carrier alone does not supply a facial order or a
coherent disk.

## 6. Repairs applied and verified

1. In (1.3) and both model proofs, replace “old model edge” by every
   actual edge between the two displayed bags.
2. Repair the paragraph deriving (1.5): use the no-`K_7`, permitted-
   transfer comparison class in Section 1, and handle a sole owner `D`
   as a literal terminal `K_7`.  Do not say the other six bags remain
   fixed while enlarging one of them.
3. In Lemma 1, state that the missing set is exactly (A.2).
4. Qualify the end of Corollary 3.1, Lemma 4, and Section 5: the exact
   carrier/linkage is ready for a set-root web or guarded-cycle analysis
   **once** the required connector/adhesion is produced; it is not by
   itself the web-side outcome.

All four changes now appear in the source note.  The local theorem is
GREEN.  The note should remain active because its final
linkage-to-adhesion composition is not proved here.
