# Independent audit: rooted `K_5` connector-or-separator theorem

Audited file: `results/hc7_exact7_rooted_k5_connector_separator.md`.

Audited SHA-256:

```text
2ee51a2af500d8d208964e130ac3008e937b2c05dcc1231e7f13cf7ce340dda8
```

**Verdict:** **GREEN**.

This focused theorem is exactly the independently audited GREEN part of the
sole-exterior bridge-exchange draft.  The later decorated-adhesion claims in
that draft are not dependencies of this result.

## Exact trace and rooted model

In the pure-Moser instance, contracting the star on `{v,a,b}` and expanding
the independent pair gives a six-colouring of `H=G-v`.  Every palette colour
must occur on `N(v)`, or the absent colour extends to `v`.  Because `ab` is
one exact block, the five vertices of `U` therefore use the other five
colours one each.

For a missing root edge `xy`, if the two roots lay in different components
of their two-colour graph, swapping the component containing `x` would make
one of those colours absent from `N(v)`.  It would again extend to `v`.
Thus the missing-cycle Kempe system is connected, and the audited
Kriesell--Mohr five-root theorem gives the rooted `K_5` while avoiding
`a,b`.  The general statement is careful to list this rooted model as a
hypothesis.

## Connector outcome

Let `W` be the union of the five bags.  An `a-b` path in one component of
`H-W` is disjoint from every bag.  Joint domination of the literal roots
makes that path adjacent to each rooted bag.  These six branch sets are
pairwise adjacent, and `{v}` sees all of them.  This is a literal `K_7`;
there is no colour-to-bag identification.

## Separator outcome

If `W` separates `a,b`, an inclusion-minimal separator `Z subseteq W`
exists.  Since deleting `v` from a seven-connected graph leaves a
six-connected graph, `|Z|>=6`.

For each `z in Z`, inclusion-minimality gives an `a-b` path whose only
vertex in `Z` is `z`.  Its two sides place neighbours of `z` in the
distinguished components `R_a,R_b`.  Components of `H-Z` have no external
neighbours outside `Z`, so both distinguished components are literally
`Z`-full.  Finally six separator vertices distributed over five disjoint
bags force a double hit.

The scope warning is necessary and correct: the argument gives neither an
order-six separator nor the special form `U union {w}`.  It proves a full
model-carried separator, not the still-open label-preserving bag split.
