# Independent audit: two-pool completion and Hall lock

## Verdict

**GREEN AS PATCHED.**  The two-pool branch sets, the sharp treewidth
example, the ordered Hall decomposition, and the minimum-fragment
collision are correct.  Corollary 5.2 is valid only under its explicit
trace-alignment and shore-free-core assumptions; its formal conclusion
was patched so failure of an assumed core is no longer listed as an
outcome.  Three smaller precision patches put the `HC_7` frame in `G-v`,
put the rerouting path inside the defined free graph, and allow empty
right blocks in the Hall decomposition.

## 1. Two-pool completion

The bags

```text
U_1,...,U_m, B, R union T
```

are disjoint.  The first `m` form the protected clique frame, `B` is
connected, and `R union T` is connected because every vertex of `T` has
a neighbour in connected `R`.  Each frame bag sees both pools by (2.2),
and fullness supplies a `B-R` edge.  Thus all claimed adjacencies are
literal and the count is `m+2`.

Corollary 2.2 is its exact one-root specialization: since every row
contains `s`, failure to meet `S-{s}` is precisely the row `{s}`.  The
apex form uses `R={v}`, and the second pooled bag is the connected star
`{v} union (S-B)`; no connectivity within `S-B` is assumed.

The owned-root form is also overlap-safe.  Boundary vertices already in
frame bags are removed into `W` and occur in neither `B` nor `T`.  A frame
bag owning a boundary vertex sees `R` through fullness; a frame bag with
no owned boundary uses its asserted `T`-portal.  Corollary 2.6 must and
now does say that the five-frame lies in `G-v`.

## 2. Proposition 2.4: sharp singleton row

The three displayed tree-decomposition bags, in order, are

```text
U union {s}, (U-{u_0}) union {s,q}, {s,q,h}.
```

They cover every edge: the first covers the core clique and all `s-u_i`
edges, the second covers all `q-u_i` edges for `i>0`, and the third covers
`hs,hq`.  Running intersection holds: `u_0` occurs only in the first bag,
the other `u_i` in the first two, `s` in all three, `q` in the last two,
and `h` only in the last.  Every bag has order at most `m+1`, so the width
is at most `m`.  Since `tw(K_{m+2})=m+1` and treewidth is minor-monotone,
the target minor is absent.

Exactly one frame row is locked: `u_0` sees only `s`, while every other
`u_i` sees both `s,q`.  Hence the example proves static sharpness without
relying on a failed minor search.

## 3. Lemma 3.1 and ordered Hall decomposition

For an inclusion-minimal deficient left set `X`, every proper subset
satisfies Hall.  Applying this to `X-{x}` gives
`|N(X)|=|X|-1` and a matching of `X-{x}` onto `N(X)`.  If the induced
bipartite graph had multiple components, Hall on each proper left part
would sum to `|N(X)|>=|X|`; hence it is connected (with the singleton/
empty-neighbour case interpreted as the one-vertex connected graph).

The alternating search is correct.  Every reached left vertex other
than the initially unmatched one was reached through its matching edge;
therefore its matched neighbour is already reached, while all
nonmatching neighbours are traversed.  Thus `N(A)=C` and
`|C|=|A|-1`; minimality forces `A=X`, so any prescribed left vertex can
be made the unique unmatched member.

In Theorem 3.2, at step `j` a block has no neighbour among later right
vertices, giving

```text
N(X_j) subset Y_1 union ... union Y_j
```

in the original graph.  Every prefix of `d` blocks has deficiency `d`,
so no matching has more than `n-d` edges.  Independent near-perfect
matchings on the blocks plus a left-saturating matching on the remainder
attain `n-d`.  Since

```text
|T_*| = |I_*| + d,
```

exactly `d` remainder labels are exposed.  The theorem now explicitly
allows `Y_j` to be empty, as required for a singleton zero row.

Corollary 3.3 does not actually need the matching decomposition: if no
row is zero in the second pool, Corollary 2.2 already supplies the clique
minor.  The decomposition correctly explains why any larger Hall circuit
adds no further static obstruction once owner pooling is available.

## 4. Free-space frontier and colour states

The rerouting path is now stated to lie in the free graph `F`, so its
endpoint cannot invade another protected bag.  Absorbing it preserves all
old frame edges and adds the missing second-pool portal.  Failure is
exactly that the component of `F` containing `U_0` has no such portal.

Lemma 4.1 is correct: equal labelled equality partitions on a separator
can be aligned by extending the induced partial colour bijection to a
palette permutation.  Clique adhesions of order at most `r` induce the
all-singleton state on both proper sides and hence glue.  In Theorem 4.2,
the common-state branch is a contradiction exit and cannot persist in
the assumed minor-minimal counterexample; the source now says so.

## 5. Proposition 5.1 and Corollary 5.2

Coverage of the whole minimum fragment by the protected frame is
essential.  It makes `D-U_0` connected and adjacent to `U_0`.  Atomic
surplus applied to that connected split gives

```text
|N_S(U_0)| + |N_{D-U_0}(U_0)| >= k+1.
```

The singleton row makes the first term one, leaving at least `k`
distinct neighbours in the other `m-1` bags.  Pigeonhole gives exactly
`ceil(k/(m-1))`, and hence two vertices in one owner for `k=7,m=5`.

Nothing in that argument makes those two vertices terminals of a
repeated adhesion trace, and it does not produce shore-free cores for the
other labels.  Corollary 5.2 therefore correctly assumes both facts.  If
they hold, a connected `p-q` trace in the sacrificed owner avoiding the
two full shores is disjoint from the retained labelled cores and is the
transverse connector of the audited owner-exchange theorem, yielding
`K_7`.  Under the assumptions, the only target-free alternative is that
every such trace uses a shore.  If alignment or a protected core is
absent, the corollary is inapplicable rather than false; the source was
patched to make that quantifier boundary explicit.
