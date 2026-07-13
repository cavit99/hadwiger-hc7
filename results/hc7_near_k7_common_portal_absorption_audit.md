# Independent audit: common-row portal absorption

## Verdict

**GREEN after correction.**  The literal absorption construction is
correct and does not assume the false abstract four-connected carrier
theorem.  Corollary 4 now states the edge/minor-critical colouring
hypotheses required by the critical-pinch theorem, cites its audited
location, and claims the unconditional equality state rather than an
unproved bypass dichotomy.

No conclusion here terminates a rotation chain.  In particular, the
square-antiprism shared-label counterexample lies cleanly in the declared
residue: its singleton common portal is anticomplete to both endpoint
roots, so Theorem 1 does not purport to absorb it.

## Audit of the literal seven bags

For the first orientation the proposed bags are

\[
 X,\quad (Z-K)\cup W,\quad F_a\cup K,\quad F_i\ (i\ne a).
\]

They are pairwise disjoint, nonempty and connected.

1. `F_a union K` is connected because `P_a` is nonempty, lies in `K`,
   and every member of `P_a` has an `F_a` neighbour.
2. Since `K` is a nonempty proper subset of the connected graph `G[Z]`,
   a literal `K--(Z-K)` edge joins the enlarged row to the residual donor.
3. Old-purity gives connectivity of the residual donor and all its row
   contacts except the deliberately replaced `F_a` contact.
4. The literal `XW` edge joins `X` to the residual donor.  The assumed
   `XK` edge repairs `XF_a`.  The old centre retains every spoke outside
   `D={a,b}`, and therefore misses only `F_b` after the repair.
5. `F_a` itself retains all adjacencies to the other four fixed rows.

Thus every pair of bags is adjacent except possibly `X,F_b`, and in fact
that pair is anticomplete by the rotation datum.  This is a literal
`K_7^-` model with unchanged centre `X`.  There is no quotient-lifting or
hidden adjacency assumption.

The second orientation is exactly symmetric.  New-purity supplies
`X union (Z-K)` as the residual donor; the literal `WX` edge joins it to
the centre; `WK` repairs `WF_a`; and `W` remains anticomplete only to
`F_c`.  Hence Theorem 1 is **GREEN**.

## Audit of the consequences

### Corollary 2

In the no-`K_7^-` branch, Theorem 1 is an immediate contradiction.  In
the height-gap branch, its output is a one-hole model whose centre is
literally the same order-`mu` bag `X` or `W`; the audited height-gap theorem
requires every one-hole centre to have order at least `mu+1`.  Subject to
the stated phrase "the height-gap theorem applies", this is **GREEN**.

### Corollary 3

Take `K={p}`.  If `U-p` is connected and `p` is not the unique endpoint of
all `U-F_i` edges for any `i!=a`, then the residual donor meets every such
row; this is precisely old-purity.  The `pX` edge triggers Theorem 1.
The rotated statement is identical with donor `X union Z` and edge `pW`.

The apparent edge case `Z={p}` causes no gap.  In the old orientation,
`W` misses `F_c`, while the old donor `U` meets it, so `p` is necessarily
the unique `U-F_c` portal.  In the new orientation, `X` misses `F_b`, so
`p` is necessarily the unique `(X union Z)-F_b` portal.  Thus whenever
neither listed obstruction holds, `K={p}` is automatically a proper
subset to which Theorem 1 applies.  Corollary 3 is **GREEN**.

This also justifies the phrase "two-row monopoly": `p` already owns the
common row `a`.  In the corrected label-exact statement, the second row
can only be `c` in the old donor and only `b` in the rotated donor,
because `W` and `X`, respectively, retain every other row.

### Corollary 4: corrected hypotheses

The corrected corollary states that `G` is not six-colourable and that
every proper minor and every proper edge-deleted subgraph is
six-colourable.  Then `p in N(W)`, the edge `pw` is literal, and `F_c`
is disjoint from `W union N(W)` because `W` is anticomplete to `F_c`.
Thus `N(W)` is an actual adhesion and the audited critical-pinch theorem
supplies its equality state.  The corrected citation points to
`../results/hc7_near_k7_critical_pinch_state.md`.

The obsolete bypass disjunction has been deleted.  Corollary 4 is
therefore **GREEN**.

## Falsification check against the exact shared-label barrier

In the square-antiprism obstruction

\[
 (\alpha,\beta,p,b,c)=(0,5,1,3,6),\qquad
 D=\{p,b\},\quad E=\{p,c\},
\]

with singleton portal sets, the quadrilateral face
`(c,alpha,beta,b)=(6,0,5,3)` blocks the two nontrivial carrier splits.
The common portal `p=1` is adjacent to neither `alpha=0` nor `beta=5`.
It therefore satisfies neither attachment hypothesis of Theorem 1 and
falls exactly under the stated "internal to the connector and anticomplete
to one endpoint centre" residue.  The barrier does not falsify the
absorption theorem, and the theorem does not eliminate the crossed rural
cell.

## Trust boundary

The audited output is strictly local:

* a genuinely detachable attached common portal gives `K_7^-`;
* a protected singleton which attaches to an endpoint is a donor
  cutvertex or a second-row monopoly; and
* under the full criticality hypotheses, a singleton attached to both
  endpoints gives an actual-adhesion equality state.

It does not prove that an opposite-shore operation reproduces the state,
that a cut/monopoly pinch is rural, or that all rural orders share one
apex pair.  Those are still the composition gap.
