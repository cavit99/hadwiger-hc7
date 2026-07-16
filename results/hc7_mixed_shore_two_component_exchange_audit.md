# Audit: component exchange in the mixed-shore support-six model

**Verdict:** **GREEN.**  The two Menger arguments have the correct sharp
budgets, their stopped paths avoid the reserved components and all old
branch sets that must remain disjoint, and the displayed branch sets in
Theorems 2.1 and 3.1 realize all 21 adjacencies of a `K_7`-minor model.

**Audited source:**
[`results/hc7_mixed_shore_two_component_exchange.md`](hc7_mixed_shore_two_component_exchange.md)

**Audited source SHA-256:**
`f3c857b85a06b5ae38e98564fede44271e686531f53495112b352f1242a26957`.

**Audit history.**  The earlier draft had SHA-256
`52454dba12b810e141613caca518370a9bb04fd82f43949fca7ad63ce5902722`.
An attempted metadata-only rebind did not initially reproduce that hash
exactly and was not accepted as the basis of promotion.  This audit instead
rechecked the final results revision at the displayed final SHA-256 from
its hypotheses through both explicit minor models.  The fresh audit
supersedes the attempted metadata rebind.

This is a separate internal audit of the conditional theorems as stated.
It does not audit the upstream argument producing the mixed-shore
support-six model.  Corollary 2.2 additionally invokes the separately
audited residual-component contact theorem; the proofs of Theorems 2.1 and
3.1 themselves do not depend on that theorem.

## 1. Common setup and component neighborhoods

Because `U` and `V` are distinct components of `G-S`, there is no edge
between them.  If `C` is a component of `V-v`, it has no edge to another
component of `V-v`.  Connectedness of `V` forces `C` to have a neighbour
at `v`; otherwise `C` would be a component of `V` disjoint from `v`.
Thus every assertion in the proofs that a path can enter `C` only through
`v` or through `S` is valid.

The six vertices supporting (1.1) are distinct.  The four singleton
branch sets form a clique, the edge branch `{v,t}` is connected, and the
five old branch sets are pairwise adjacent.  In particular, for `h=3`
the edge `u_iw` used in Theorem 3.1 is forced for every `i`, while the
edge `u_it` is part of the stated normalization.

## 2. Audit of Theorem 2.1

Here

```text
|F_0| = 1+1+(4-h) = 6-h,
|T|   = 8-(6-h)   = h+2,
|Z|   = (4-h)+3   = 7-h.
```

The sets `A` and `T` are disjoint from `Z`.  If there were fewer than `h`
pairwise vertex-disjoint `A`--`T` paths in `G-Z`, set-Menger would give a
separator `X` of order at most `h-1`.  Since `|A|=h` and `|T|=h+2`, both
`A-X` and `T-X` are nonempty.  They lie in different components of
`G-(Z union X)`, whose deleted set has order at most

```text
(7-h)+(h-1)=6.
```

This contradicts seven-connectivity.  The two numerical edge cases are
`5+1=6` for `h=2` and `4+2=6` for `h=3`.

The resulting `h` disjoint paths use every vertex of `A` as a distinct
initial vertex and distinct vertices of `T` as their ends.  No path can
contain a second member of `A`: that member is already the initial vertex
of another path in the `h`-path linkage.  The other support vertices and
`s` belong to `Z`.

Before the first visit to `T`, a path cannot enter `C`.  Its predecessor
on a first entry into `C` would have to be `v` or a boundary vertex.  The
vertex `v` and all boundary vertices outside `T` are deleted, so the first
possible boundary predecessor lies in `T`, where the path has already
been stopped.  This argument also covers an untruncated path that might
later enter another component of `V-v`.

Let `E={v,t}`.  The complete adjacency count among

```text
R_1,R_2,R_3,R_4,E,C,{s}
```

is as follows.

* The six pairs among the four `R_i` retain the old `K_5`-model
  adjacencies.
* The four `R_i`--`E` pairs retain the old model adjacencies.
* Each enlarged `U`-row is adjacent to `C` through its terminal in `T`,
  and each unchanged `{w_j}` is adjacent to `C` because
  `w_j in S-{t}`: four `R_i`--`C` pairs.
* Every `R_i` contains a boundary vertex, which is adjacent to `s`: four
  `R_i`--`{s}` pairs.
* `E` is adjacent to `C` through `v`, and to `{s}` through `st`.
* `C` is adjacent to `{s}` because `s != t`.

The count is `6+4+4+4+1+1+1=21`.  Connectivity and disjointness also
hold: every enlargement retains its initial singleton, the stopped paths
are mutually disjoint and avoid `C`, and `C`, `E`, and `{s}` are mutually
disjoint.  Theorem 2.1 is therefore valid.

## 3. Audit of Theorem 3.1

For `h=3`, the deletion set in (3.2) has order four and `T` has order
five.  Failure of three disjoint `A`--`T` paths would give a separator of
order at most two in `G-Z`; together with `Z` this would be a cut of order
at most six.  Again, at least one vertex survives in each of `A` and `T`.
Thus the Menger argument is valid.

The same first-entry argument shows that the stopped paths avoid all of
`V-v`, and hence both `C_s` and `C_w`.  Their terminals lie in
`T=S-{s,w,t}`.  Therefore every terminal is adjacent to each component:
`C_s` misses only `s`, and `C_w` misses only `w`.

Put

```text
A_0 = C_s union {w},
D_0 = C_w union {v}.
```

Both sets are connected: `C_s` is adjacent to `w`, and `C_w` is adjacent
to `v`.  They are disjoint from one another, the three stopped paths, and
the singleton sets `{t}` and `{s}`.  The 21 adjacencies among

```text
R_1,R_2,R_3,A_0,{t},D_0,{s}
```

are exhausted as follows.

* The three pairs among the `R_i` retain the singleton-clique edges.
* For each `i`, the four pairs from `R_i` to `A_0,{t},D_0,{s}` are
  witnessed respectively by `u_iw`, `u_it`, the terminal's contact with
  `C_w`, and the terminal's edge to the boundary-universal vertex `s`.
  This contributes 12 pairs.
* The remaining six pairs are:
  `A_0`--`{t}` through a `C_s`--`t` edge;
  `A_0`--`D_0` through a `C_s`--`v` edge;
  `A_0`--`{s}` through `ws`;
  `{t}`--`D_0` through `tv`;
  `{t}`--`{s}` through `ts`; and
  `D_0`--`{s}` through a `C_w`--`s` edge.

Thus `3+12+6=21`, with no unlisted adjacency assumed.  Theorem 3.1 is
valid.

## 4. Falsification attempts and exact scope

The local quotient data were checked for every injection of the `h`
linkage terminals into the sets `T` of orders four and five.  The branch
adjacency checks above depend only on the required contact sets, so changing
the terminal assignment, deleting every optional boundary edge, or making
each component and each stopped path as small as possible leaves the same
complete seven-branch-set quotient.  No small contact configuration
satisfying the displayed hypotheses avoids the constructed minor.

The following adversarial path shapes were also tested against the proof:
a path using another member of `A`, a path entering `C` before reaching
the boundary, and a path traversing another component of `V-v`.  The first
is excluded because an `h`-path linkage from an `h`-vertex start set uses
all starts; the second is excluded by the deleted first-entry boundary;
and the third can occur only after a first boundary visit and is removed
by truncation.

Corollary 2.2 follows from the separately audited contact theorem plus
Theorem 2.1.  Corollary 3.2 is then a direct two-label exhaustion.  The
result does **not** align missed contacts when `h=2`, handle `V={v}`, or
produce the mixed-shore model from a general `HC_7` counterexample.  It
therefore eliminates exactly the infinite conditional families stated in
Theorems 2.1 and 3.1 and no more.
