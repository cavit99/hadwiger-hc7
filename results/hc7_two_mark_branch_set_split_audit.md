# Independent audit: two-mark branch-set split

## Verdict

**GREEN** at the exact source revision

```text
d146edf7783d6f29750d634ac3d224da14bdd83dd91170011293ece177240d64  results/hc7_two_mark_branch_set_split.md
```

The minimal-subtree argument, separator alternatives, `K_t`-model
construction and parameter-uniform corollary are correct.  The theorem
does not prove that its separator has minimum possible order or carries
compatible boundary colourings.

## 1. Marked tree split

Put `M=N_G(c) intersect U`.  The minimal subtree of a spanning tree of
`G[U]` containing `M union {rho}` has at least two leaves, every leaf is a
terminal, and at most one leaf is `rho`.  Thus it has a leaf
`m in M-{rho}`.  Removing its incident subtree edge from the full spanning
tree puts `m` on one side and `rho` together with at least one other member
of `M` on the other.  Branches outside the minimal subtree contain no
terminal.  The resulting vertex sets `Z,W` are connected, adjacent, and
both meet `M`.

## 2. Separation alternatives

If `Z` is anticomplete to `D`, then `D` lies outside
`Z union N_G(Z)`, so the full neighbourhood of the nonempty connected set
`Z` is an actual separator.  The same argument applies to `W` and a set
`V_j` which it misses.  No unstated connectivity assumption is used.

## 3. Explicit minor model

In the remaining case the displayed family has

\[
                      1+1+1+(t-3)=t
\]

branch sets.  The set `D union Z` is connected through a `DZ` edge; the
tree-cut edge supplies `(D union Z)W`; the two marked contacts supply the
two centre adjacencies; `D` supplies all contacts from `D union Z` to the
sets `V_j`; and `W` retains its contacts to every `V_j`.  All other
contacts are inherited from the original `K_{t-1}` model.  The sets remain
disjoint and `W` contains the protected vertex `rho`.

## 4. Connectivity and the `HC_7` corollary

In a `t`-connected graph the returned full neighbourhood has order at
least `t`.  At equality, a component missing one boundary vertex would
have a neighbourhood of order at most `t-1`; another component exists
because the separation is actual.

For a spanning one-missing-adjacency `K_7` model, every neighbour of the
centre lies in one of five common branch sets.  Minimum degree seven puts
two centre neighbours in one common bag, so the theorem applies.  The
argument works for every `t>=4` as stated.

## Trust boundary

The separation boundary is only lower-bounded.  The theorem neither
forces order seven nor supplies one equality partition extending through
both closed shores.  The source states these limitations accurately.
