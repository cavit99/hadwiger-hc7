# Independent audit: three-path matching-defect barrier

## Verdict

**GREEN** at the exact source revisions

```text
83fb3c4dcfdc8dcea94d0b11a3e694fbb1f6fd1f318c0266bcae23d839da0ff2  barriers/hc7_stable_theta_three_path_matching_barrier.md
de9c7eb1c0da62b8de703e14071946cf26d447ea7b04c4ad67a6c6eb8ba60362  barriers/hc7_stable_theta_three_path_matching_barrier_verify.py
```

The graph is defined unambiguously, the order-seven separation and all
connected-set contacts are literal, the three terminal-capacitated paths
have the stated disjointness, and the nonadjacency graph is exactly the
two-edge nonmatching star claimed in (3.6).  The source accurately records
the hypotheses absent from the example.

The deterministic verifier was rerun at the revisions above and printed

```text
stable-theta three-path matching barrier: PASS
```

## 1. Construction and separation

The vertex sets `T,L,R` are disjoint and cover the graph.  The set `T`
has order seven.  The five `x_i` form a cycle, and `v` is adjacent to all
five of them, so `G[L]` is connected.  The set `R={d,e,f}` induces a
triangle and is connected.  No construction rule adds an `L-R` edge.
Consequently `T` is an actual order-seven separation with the two nonempty
open sides `L` and `R`.

The only neighbours of `v` are the three members of `B` and the five
vertices `x_0,...,x_4`.  Thus `d_G(v)=8`, and the five non-`B` neighbours
are exactly the nominated vertices in the five cyclic connected sets.

## 2. Connected sets and contacts

For `0<=i<=3`, the edge `u_i x_i` makes

```text
C_i=G[{u_i,x_i}]
```

connected; `C_4={x_4}` is connected.  These sets are nonempty and
pairwise disjoint.  The cycle edges `x_i x_{i+1}` give every consecutive
adjacency, including `C_4-C_0` through `x_4x_0`.  Each `C_i` contains the
specified neighbour `x_i` of `v`, and the four roots `u_0,...,u_3` lie in
four distinct sets.

The triangle `D=G[R]` is disjoint from all five sets and from `B`.  Since
every vertex of `R` is adjacent to every vertex of `T`, `D` contacts each
of the three singleton labels in `B` and each of `C_0,...,C_3` through
`u_0,...,u_3`.  It has no contact with `C_4={x_4}`, because `x_4` lies in
`L` and `L` is anticomplete to `R`.  Hence `D` contacts exactly seven of
the eight labels.

## 3. The three paths

The edges between `R` and `T` make

```text
b-d-u0,  b-e-u0,  b-f-u0
```

literal paths.  Relative to the allowed terminal set
`{b,u0,u2}`, their interiors are respectively `{d}`, `{e}`, `{f}` and
are pairwise disjoint.  Repetition of the terminal `u0` is expressly
allowed by the refuted terminal-capacitated claim, so the example matches
that hypothesis exactly.

## 4. Exact nonmatching defect

All edges from `B` to the sector vertices are present except

```text
r-u1,  r-x1,  r-x4.
```

Both vertices of `C_1={u1,x1}` therefore miss `r`, and the singleton
`C_4={x4}` misses `r`.  Every other `B-C_i` pair has at least one edge:
`b` and `q` are complete to all sector vertices, while `r` contacts both
vertices of each of `C_0,C_2,C_3`.  The bipartite nonadjacency graph is
therefore exactly

```text
{r-C1, r-C4}.
```

Its two edges share `r`, so it is not a matching and in particular is not
a matching of order at most two.

## 5. Trust boundary

The verifier gives `d_G(x_1)=6`; this alone implies that the graph is not
seven-connected.  The construction does not impose the universal
six-colouring responses of a strongly contraction-critical host and makes
no claim of `K_7`-minor exclusion.  Thus it refutes only the incidence
inference from the three displayed combinatorial outputs.  It does not
refute a continuation that materially uses seven-connectivity,
contraction-criticality, or `K_7`-minor exclusion, exactly as stated in
the source.
