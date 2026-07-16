# Audit: residual-component contacts in the mixed-shore model

**Verdict:** **GREEN.**  The neighborhood identity, the sharp
order-seven separator, the Menger count, the truncation before the reserved
component, and all adjacencies in the resulting `K_7`-minor model are valid.

**Promoted audited source:**
[`results/hc7_mixed_shore_component_contacts.md`](hc7_mixed_shore_component_contacts.md)

**Final audited source SHA-256:**
`21fcd20ad551cb61e78a5747226fe5cc464785f972e8f005d26438536c59d928`.

**Revision identity.**  The original audited draft had SHA-256
`ea485fa009e4487096cfbf74ecc676e8af0c9a27636d8df4427c5fbdec92e261`.
Repairing the two notation issues recorded below, and making no other
change, produced the pre-status SHA-256
`a6e47728b37701cd116c14215a0ff5a4402357e42b407e01fe59bd222af9a696`.
Replacing only the opening status paragraph by the promoted-audit status
produced the final hash above.  Restoring the old status paragraph in
memory reproduces the pre-status hash exactly.  The proof and mathematical
conclusion are therefore identical to the audited revision.

The audit treats Theorem 1.1 as a conditional result from the displayed
mixed-shore model.  It does not depend on the proof that produces that
model upstream.

## 1. Exact neighborhood and the seven-separator branch

For a component `C` of `V-v`, every neighbor outside `C` lies in `S` or is
`v`.  There is no `C`--`U` edge because `U,V` are distinct components of
`G-S`, and there is no edge from `C` to another component of `V-v` by the
definition of those components.  Conversely, connectedness of `V` forces
an edge from `v` to every component of `V-v`: otherwise that component
would also be disconnected from `v` in `V`.  Thus the identity

```text
N_G(C) = {v} union N_S(C)
```

is exact, and the union is disjoint.

Deleting this neighborhood leaves `C` and also leaves every vertex of
`U`.  Hence it is genuinely a vertex cut, so seven-connectivity gives
`1+|N_S(C)|>=7`.  When `|N_S(C)|=6`, put

```text
Q = N_G(C),
L = C union Q,
R = V(G)-C.
```

Then `L cap R=Q`, there is no edge between the two open sides, `L-Q=C` is
nonempty, and `R-Q` contains `U`.  This is an actual separation of order
seven, not merely a boundary count.

## 2. Menger budget

All six displayed support vertices are distinct.  With
`A={u_1,...,u_h}`, the set `Z` consists of the other `6-h` support
vertices and `s`, so

```text
|Z| = 7-h.
```

Under `F_0 subseteq N_S(C)`, the set
`T=N_S(C)-F_0` is disjoint from both `A` and `Z`, and

```text
|F_0| = 6-h,
|T| >= 6-(6-h) = h.
```

If `G-Z` had fewer than `h` pairwise vertex-disjoint `A`--`T` paths,
set-Menger would give an `A`--`T` separator `X` of order at most `h-1`.
Because both `A` and `T` have at least `h` vertices, at least one vertex of
each survives `X`; those surviving vertices lie in different components
of `G-(Z union X)`.  The cut has order at most

```text
(7-h)+(h-1) = 6,
```

contrary to seven-connectivity.  This checks both sharp cases: for `h=2`
the two contributions are `5+1`, and for `h=3` they are `4+2`.

The `h` disjoint paths use all `h` vertices of `A` as distinct starts and
have distinct ends in `T`.  In particular, no path can contain a different
member of `A` internally; that vertex is already the start of another
disjoint path.

## 3. Truncation avoids the reserved component

Consider the first entry of one of the paths into `C`, if an entry occurs.
The preceding vertex must lie in

```text
N_G(C) = {v} union F_0 union T.
```

The vertices `v` and all of `F_0` lie in `Z`, so a path in `G-Z` cannot use
them.  Its first possible entry into `C` is therefore preceded by a vertex
of `T`.  Truncating on the first visit to `T` stops the path at that
boundary vertex and strictly before entry into `C`.  This remains true even
if an untruncated path travels through another component of `V-v` first.

Thus every truncated path is disjoint from `C`, from `s`, and from every
old support vertex other than its own start.  The truncated paths are still
pairwise vertex-disjoint.

## 4. Complete branch-adjacency audit

Let the five enlarged old branch sets be `B_1,...,B_5`.  They are connected
and pairwise disjoint by the preceding section.  They retain all original
pairwise adjacencies because each enlargement retains its original branch
set.  They are also disjoint from `C` and from `{s}`.

Every remaining unordered pair among

```text
B_1, B_2, B_3, B_4, B_5, C, {s}
```

has the required adjacency:

* An enlarged `U` branch meets a terminal in `T subseteq N_S(C)`, so it is
  adjacent to `C`.
* Each singleton branch `{w_j}` and the edge branch `{v,t}` are adjacent to
  `C` through `w_j` and `t`, respectively, because these vertices lie in
  `F_0 subseteq N_S(C)`.  The edge branch is also adjacent through `v`.
* The universal boundary vertex `s` is adjacent to every enlarged `U`
  branch through its terminal in `T`, to each `{w_j}`, and to `{v,t}`
  through `t`.
* Finally, `s` is adjacent to `C` because
  `s in F_0 subseteq N_S(C)`.

These are all `21` unordered branch-set pairs.  Hence the seven displayed
sets are an explicit `K_7`-minor model.

## 5. Exhaustion and counterexample search

After excluding the separator branch, `|N_S(C)|` is seven or eight.  Eight
contacts contain `F_0` and trigger the explicit minor.  With seven
contacts, a missed vertex outside `F_0` again leaves all of `F_0` present
and triggers the minor; a missed vertex in `F_0` is exactly outcome 3.

As an independent finite check, all subsets of an eight-element boundary
of order at least six were enumerated for both `h=2` and `h=3`.  Every one
was classified by the order-six separator, containment of `F_0`, or the
exact-seven missing-`F_0` outcome; no contact pattern escaped.  Adversarial
checks of paths entering `C`, linkages using another start, and the two
sharp Menger budgets likewise produced no counterexample.

There are no unresolved mathematical assumptions in the conditional
theorem.  The promoted source repairs the two harmless notation issues
found in the original audit: equation (1.2) now prints `v\in V,\quad`, and
the intended hypothesis `x\in S-\{s\}` is explicit.  The latter only makes
the intended normalized setting formal; the proof remains uniform in `x`
and uses no new inference from the repair.
