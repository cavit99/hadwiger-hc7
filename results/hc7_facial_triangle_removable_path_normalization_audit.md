# Independent audit: removable path through the facial critical triangle

**Audited file:** `results/hc7_facial_triangle_removable_path_normalization.md`
**SHA-256:** `2409fb7da889757b60b68476c0741df085e41cf2930126481a2bf3a791642bdc`
**Verdict:** **GREEN.**  Theorem 1.1 is a correct application and
truncation of the cited removable-path theorem.  Theorem 2.1 gives a valid
explicit `K_7`-minor model under its stated splitting hypothesis.  The note
correctly leaves the existence of that split open.

The hash above rebinds this verdict after promotion from `active/` to
`results/`.  Only the status/link metadata changed; the theorem statements,
proofs, application, gap statement, and reference are unchanged from the
revision audited below.

## 1. External theorem

The cited result is exactly Theorem 1.5 of Xiying Du, Yanjia Li, Shijie
Xie, and Xingxing Yu, *Linkages and removable paths avoiding vertices*,
Journal of Combinatorial Theory, Series B **169** (2024), 211--232,
<https://doi.org/10.1016/j.jctb.2024.06.006>.

It states that, for distinct vertices

```text
a1,...,am,b1,b2
```

in a `(2m+2)`-connected graph, there is a `b1-b2` path avoiding all the
`a_i` whose vertex deletion leaves a connected graph.  Taking `m=2`,
avoided vertices `a,b`, and ends `w,q` gives precisely the path `P'` used
in Theorem 1.1.  The six nominated vertices are distinct because
`a,b,w` are distinct and outside `R`, while `q` belongs to `R`.

## 2. First-hit truncation

Let `r` be the first vertex of `R` encountered from `w` on `P'`, and let
`P` be the initial `w-r` subpath.  The path avoids `a,b`, and first-hit
minimality gives

```text
V(P) intersection ({a,b} union R) = {w,r}.
```

If `r=q`, then `P=P'`, so its complement is connected directly by the
cited theorem.  If `r` is not `q`, the vertices strictly after `r` on
`P'` induce a connected suffix containing `q`.  The graph `G-V(P')` is
connected and contains `a`, while `q` is adjacent to `a` because `a` is
complete to `R`.  Restoring the suffix first attaches `q` to that connected
complement and then attaches every other suffix vertex along the path.
The restored graph is exactly `G-V(P)`, so it is connected.  This validates
the only non-immediate step in Theorem 1.1.

## 3. Branch-set audit

The seven proposed branch sets are

```text
{a}, {b}, {s}, {t}, V(P_w), V(P_r), V(B).
```

They are nonempty, connected, and pairwise disjoint.  The intersection
property for `P` keeps `a,b,s,t` off the path.  The definition of `B` keeps
it disjoint from both path pieces and all four singleton sets.

All 21 required branch-set adjacencies are accounted for as follows:

- the six pairs among `{a},{b},{s},{t}` are edges because `ab` is an edge,
  `st` lies in the triangle `R`, and `a,b` are complete to `R`;
- `P_w` has four adjacencies to the singleton sets: to `a,b` through `w`
  and to `s,t` by hypothesis 1;
- `P_r` has four adjacencies to the singleton sets through its vertex `r`,
  since `a,b` are complete to `R` and `R` is a triangle;
- `P_w` and `P_r` are adjacent through the edge used to split `P`; and
- `B` has the remaining six adjacencies by hypothesis 2.

The count is `6+4+4+1+6=21`, so the seven sets form a complete
`K_7`-minor model exactly as claimed.

## 4. Application and trust boundary

In the balanced order-eight application, the five-clique supplies all
required edges among `a,b,R`, while the facial critical triangle supplies
`aw` and `bw`.  Seven-connectivity implies the six-connectivity needed for
Theorem 1.1.

Neither Theorem 1.1 nor the cited external theorem controls where an edge
splitting `P` can be chosen, whether the `w`-side meets both remaining
vertices of `R`, or whether the complement contains the six-adjacent
connected subgraph `B`.  Theorem 2.1 assumes all of these properties; it
does not derive them.  The final section states this gap accurately, so the
note does not prove the facial-triangle case, `HC_7`, or Hadwiger's
Conjecture.

Any mathematical change to the audited source requires a new audit or an
explicit hash update after rechecking the changed argument.
