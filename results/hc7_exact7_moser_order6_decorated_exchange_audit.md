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
segment stability into block rank, and does not close the five-attachment
lock.  These limitations are correctly retained in the promoted theorem.
