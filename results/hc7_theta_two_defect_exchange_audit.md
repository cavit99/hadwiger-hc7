# Audit: two-defect exchange in the mixed-shore support-six model

**Verdict:** **GREEN.**  The theorem is valid under its stated hypotheses.
The two-path anchoring argument has the correct separator budget, the
endpoint matching exhausts all possibilities, and each displayed family
consists of seven pairwise disjoint connected branch sets realizing all
21 adjacencies of a `K_7`-minor model.  The two corollaries then follow
from the cited audited component-contact results and an exact neighbourhood
calculation.

**Audited source:**
[`results/hc7_theta_two_defect_exchange.md`](hc7_theta_two_defect_exchange.md)

**Audited source SHA-256:**
`89d473f266a3298f726e55a1315011f22c123fd63762a1f107f334aa9afc2dcf`.

The mathematical revision originally audited in `active/` had SHA-256
`b1fed5c84032dd6f8096f4c7793da3dc3cede7cd8b209d2336ba9db10fbaa91c`.
Promotion changed only the opening status paragraph.  Replacing the
promoted paragraph by the exact pre-promotion paragraph reproduces that
pre-promotion hash; all text from `## 1. The exchange theorem` onward is
byte-for-byte unchanged.  The GREEN mathematical audit therefore transfers
exactly to the promoted path and final hash above.

This is a separate internal audit of the conditional theorem as stated.
It does not independently re-audit the upstream derivation of the
mixed-shore support-six model.  An earlier draft omitted from the theorem
statement the hypothesis that `t` misses at least one of `w_1,w_2`, even
though its proof used that fact.  The audited revision adds that explicit
hypothesis.  No conclusion from the earlier revision is used here.

## 1. Setup and forced adjacencies

The six vertices in the support-six model are distinct.  Since `U,V` are
different components of `G-S`, there is no `U`--`V` edge.  The four
singleton branch sets therefore force the clique edges in (1.5), while
adjacency of `{v,t}` to `{u_i}` must be supplied by `tu_i`.  Every
component of `V-v` has a neighbour at `v`, since `V` is connected.

For each `b in {s,w_1,w_2}`, the set

```text
L(b) = {e in {v,t} : eb is an edge}
```

is nonempty.  For `s`, this follows from boundary universality and
`t in S-{s}`.  For each `w_j`, it follows from adjacency between the old
branch sets `{w_j}` and `{v,t}`.

## 2. Menger anchoring and disjointness

The sets in (1.7) satisfy

```text
|A|=2,  |Z|=5,  |T|=4.
```

If two disjoint `A`--`T` paths did not exist in `G-Z`, set-Menger would
give a separator `X` of order at most one.  At least one vertex remains in
each of `A-X` and `T-X`, and

```text
|Z union X| <= 5+1 = 6,
```

contradicting seven-connectivity.  Hence the two paths use the two
different vertices of `A` and have different ends `p,q in T`.

Before its first visit to `T`, such a path stays out of `V-v`.  It starts
in `U`; passage from `U` to `V` requires either the deleted vertex `v` or
a first visit to `S`, and all vertices of `S-T` are deleted.  Truncation
at that first visit also ensures that each stopped path contains exactly
one vertex of `T`.  Thus every

```text
r in T-{p,q}
```

is disjoint from both enlarged branch sets `R_1,R_2`.  The paths are
mutually disjoint and avoid `C,D` and all reserved model vertices.

Each `R_i` remains adjacent to the other one and to `{w_1},{w_2},{t}` by
the old model edges.  Its terminal is seen by `C` and `D`, because those
components miss vertices only in `{s,w_1,w_2}`, which is disjoint from
`T`; the same terminal is adjacent to `s`.  This verifies (1.8)--(1.9)
without assuming an optional boundary edge.

## 3. Endpoint matching case

Two nonempty subsets `L(y),L(z)` of the two-element set `{v,t}` fail to
have distinct representatives exactly when their union has order one.
Thus either they have distinct representatives or

```text
L(y)=L(z)={e}
```

for one endpoint `e`.  This is the complete two-set form of Hall's
condition.

In the distinct-representative case, orient the representatives as
`e_C in L(y)` and `e_D in L(z)`.  The sets `C union {e_C}` and
`D union {e_D}` are connected: a component is adjacent to `v`, and it is
also adjacent to `t` because its unique missed contact lies among
`s,w_1,w_2`.  Each enlarged set meets its missed boundary vertex through
its assigned endpoint and meets the other two boundary vertices through
its component.

The 21 adjacencies in (1.13) split as follows.

* One pair joins `R_1,R_2`.
* Each `R_i` is adjacent to the other five sets, giving ten pairs.
* The three boundary singleton sets form a triangle, giving three pairs.
* Each enlarged component set is adjacent to all three boundary
  singletons, giving six pairs.
* The two enlarged component sets are adjacent: if their endpoints are
  `v,t`, the component in the `t`-set has an edge to the `v` in the other
  set.  This gives the final pair.

The count is `1+10+3+6+1=21`.  The seven sets are disjoint because the
endpoints `v,t` are assigned to different components and the stopped
paths avoid both components.

## 4. First Hall obstruction: common endpoint `v`

If `L(y)=L(z)={v}`, neither missed contact is `s`, since `ts` is an edge.
Because `y,z` are distinct, they are `w_1,w_2` after relabelling.  Hence
`t` misses both boundary singleton vertices and `v` meets both, exactly as
in (1.15).

For the seven sets in (1.16), connectivity is immediate for `D union {r}`
from the `D`--`r` contact and for `{v,w_2}` from `vw_2`.  Disjointness
uses `r notin R_1 union R_2`, the distinct components `C,D`, and the fact
that `v` lies in neither component of `V-v`.

The 21 adjacencies can be checked without any optional edge:

* `R_1R_2` is retained, and each `R_i` meets each of the other five sets
  through, respectively, its terminal contact with `C`, the old `u_it`
  edge, its terminal edge to `s`, its terminal contact with `D`, and the
  old `u_iw_2` edge.  This accounts for 11 pairs.
* Among the remaining five sets, `C,{t},{s}` form a triangle because `C`
  misses only `w_1`.
* `D union {r}` meets those three sets through `Cr`, `Dt`, and `Ds`.
* `{v,w_2}` meets them through `Cv`, `tv`, and `sw_2`.
* Finally, `D union {r}` meets `{v,w_2}` through a `D`--`v` edge.

The latter count is `3+3+3+1=10`; together with the first 11 pairs it
exhausts all 21.

## 5. Second Hall obstruction: common endpoint `t`

Suppose `L(y)=L(z)={t}`.  The pair `{y,z}` cannot be `{w_1,w_2}` under
the explicit hypothesis that `t` misses at least one of those vertices.
Thus it is `{s,w_j}`; after relabelling it has the form in (1.17).  The
same explicit hypothesis, together with `tw_2 in E(G)`, gives
`tw_1 notin E(G)`.  The equalities of the two `L`-sets also give
`vs,vw_2 notin E(G)`.

In (1.18), `D union {t}` and `{s,r}` are connected through `Dt` and `sr`.
They are disjoint from the stopped paths and all other displayed sets.
Again all 21 adjacencies are forced:

* `R_1R_2` and the ten pairs from `R_1,R_2` to the other five sets use
  their terminal contacts with `C`, the old edges to `w_1,w_2,t`, and
  their terminal edges to `s`.
* `C,{w_1},{w_2}` form a triangle because `C` misses only `s` and
  `w_1w_2` is an old singleton-clique edge.
* `D union {t}` meets those three sets through `Ct`, `Dw_1`, and `tw_2`.
* `{s,r}` meets them through `Cr`, `sw_1`, and `sw_2`.
* The last two sets meet through `ts`.

This is again `11+(3+3+3+1)=21`.  No adjacency from `v` is used in this
construction.

The distinct-representative case and the two common-singleton cases are
exhaustive, proving Theorem 1.1.

## 6. Corollaries and trust boundary

Corollary 2.1 uses the separately audited component-contact theorem to
restrict a missed boundary contact to `s,t,w_j`, the separately audited
component-exchange theorem to eliminate `t` and align the `h=3` case, and
Theorem 1.1 for `h=2`.  Thus two different missed contacts would always
give a `K_7` minor.

For Corollary 2.2, connectedness of `V` implies that every component of
`V-v` has a neighbour at `v`.  The common-contact conclusion says that
every such component sees every vertex of `S-{y}` and none sees `y`.
There is no edge from `V-v` to `U`.  Consequently

```text
N_G(V-v) = {v} union (S-{y}).
```

This set has order eight.  Its deletion leaves the nonempty set `V-v`
separated from the nonempty component `U` (the surviving vertex `y` may
remain with `U` but has no neighbour in `V-v`).  It is therefore an actual
order-eight separator.

The proof does not use the theta structure of the endpoint-rigid boundary,
does not handle the resulting common-missed-label order-eight separation,
and does not by itself prove `HC_7`.  Any mathematical alteration to the
audited source requires a new hash and a fresh audit.
