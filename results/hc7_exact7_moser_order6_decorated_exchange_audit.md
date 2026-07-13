# Independent audit: exact-order-six decorated Moser exchange

Audited file: `results/hc7_exact7_moser_order6_decorated_exchange.md`.

**Verdict:** **GREEN under the explicitly stated exact-order-six
hypothesis.**

The result is the focused promoted form of the corrected Sections 4--5 of
the independently audited sole-exterior bridge-exchange draft.  It does not
promote that draft's unproved stable-rank endpoint.

## Decorated state transfer

The definition of a supported root decoration includes both geometric
contact and literal independence of `{w} union trace(K)`.  Therefore merging
the `w`-carrier with `K` creates a legal equality block.  In Theorem 2.1(1)
the two sides realize the same three independent blocks, so the audited
bilateral transfer theorem applies.  In case 2, the singleton side is
adjacent to every core block and can make the same admissible merge.  In
case 3, the four traces `e,f,{r},{w}` are independent and pairwise adjacent;
the side-terminal edge supplies the extra star visibility required for the
portal-only block.  No colour is identified with an existing branch-set
label.

## The extra portal misses both terminals

If `wa` is present, the seven displayed bags in (3.2) are disjoint and
connected.  Triangle `012` and the fixed Moser edges certify the first five
bags; literal fullness of `D_a,D_b` certifies all remaining contacts.  In
particular `D_a` sees `D_b union {w}` through `w`, and `wa` makes the last
bag see `{a}`.  The Moser automorphism handles `wb`.  Lemma 3.1 is GREEN.

## Admissible rank

The revised `sigma_D(w)` counts exactly geometrically supported decorations
whose merged trace is independent.  Hence two rank-at-least-two subsets of
the three named blocks intersect in a common legal decoration, proving
Corollary 4.1.

For Lemma 4.2, raw-but-not-admissible contact is precisely a literal edge
from `w` to a root in that block's independent trace.  If `K_w` is empty,
all open-shore neighbours of `w` lie in the unique contacted core block.  If
`K_w` is nonempty, deleting the core leaves mutually anticomplete components;
with raw rank at most one, every external neighbour of `K_w` lies in one
named block or in `{w,t}`.  This whole-graph neighbourhood separates `K_w`
from `v`, so seven-connectivity gives at least seven distinct vertices and
hence at least five in the named block.  The displayed closed-shore
separation follows directly from `Q=N_J(K_w)`.

## Trust boundary

The exact adhesion `T=U dotcup {w}` is assumed.  The general rooted-model
separator may be larger and need not contain the literal roots.  The audit
does not assert a common crossed frame on both shores, does not convert
segment stability into block rank, and does not close the central-core
residue of the five-attachment lock.  These limitations are correctly
retained in the promoted theorem.

## Degree surplus and pendant-lobe promotion

The newly promoted Lemmas 5.1--5.3 are also **GREEN**, under the same
exact-cell exhaustion hypothesis.

For Lemma 5.1, `w` has no neighbours outside `U,D_a,D_b`: it misses `v` by
definition and `a,b` by Lemma 3.1.  Thus the displayed degree identity is
exact, and the admissibility statements are simply the intersection counts
for blocks of sizes `2,2,1`.

For Lemma 5.2, every one of the four displayed rows was checked pairwise.
The fixed Moser edges make the four ordinary bags a clique, fullness makes
both shore bags see all ordinary bags and `{v}`, and their mutual edges are
respectively `34,16,12,35`.  The five-cycle calculation leaves precisely
the six listed negative triples.  The independent quotient verifier in
`active/hc7_exact6_w_boundary_quotient_probe.py` regenerates the same four
minimal positive contact sets; its negative output is used only as a
guardrail, not as proof for uncontracted shores.

For Lemma 5.3, removing one component outside the protected tree leaves the
old block connected, while the two stipulated endpoint contacts make the
enlarged target block connected.  The protected `K-L` portal, old `M-L`
edge, and a component-to-tree edge preserve all three block adjacencies.
Since the protected tree contains the whole old adhesion trace, the moved
component contains no adhesion vertex and the trace change is exact.

These lemmas do not prove the central-core case left when every relevant
foreign portal avoids every pendant lobe containing a `W`-attachment.
