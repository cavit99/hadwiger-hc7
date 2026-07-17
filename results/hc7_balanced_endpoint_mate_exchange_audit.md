# Independent audit: endpoint-mate exchange at the balanced order-eight boundary

**Verdict:** GREEN for the theorem content at the exact source revision below,
with the scope and preservation qualification in Section 6.

**Source:** [`hc7_balanced_endpoint_mate_exchange.md`](hc7_balanced_endpoint_mate_exchange.md)

**Audited SHA-256:**
`d2ec5f3a4a55520441b7cfe4bb1b22086a97e509d00e5b565fe7ed7124cd0ce0`

The independently audited mathematical revision had SHA-256
`fbd38c916fd79c95df98d27c24b3388e924eca4a3d40aca918bfdb07f2b5a50b`.
The promoted revision differs only in its opening status paragraph, which
now records this GREEN audit; no theorem statement or proof step changed.

This is an independent internal mathematical audit, not external peer
review.  It checks the explicit minor model, the complete finite
classification of failed endpoint choices, the forced-theta specialization,
and the minimum-degree calculations.  It does not re-audit the upstream
balanced-boundary reductions or the canonical-web and split-edge results
invoked in Section 5 of the source.

## 1. The mate existence lemma

For `q=e`, every endpoint has a neighbour in `C` by literal boundary
fullness.  Its only possible neighbours in `C` are in `H` or at
`lambda_e=ell_f`, because `ell_e` is anticomplete to `e`.  Hence
`I_e union L_e=V(e)`.  Both sets are nonempty by the stated contacts.

If `V(e)={u,v}`, `u in I_e`, and `O_e` were empty, then `v notin L_e`.
The union identity puts `v in I_e`, after which emptiness of `O_e` gives
`u notin L_e`.  This contradicts `L_e` being nonempty.  The argument for
`f` is symmetric.  Lemma 2.1 is correct.

## 2. The explicit `K_7`-minor model

For selected `z_q in O_q`, its mate `u_q` lies in `L_q`, so
`{lambda_q,u_q}` is connected.  The branch set

```text
V(H) union {x,z_e,z_f}
```

is connected because each added vertex has a neighbour in the connected
graph `H`.  The remaining branch sets are the three `R` singletons and
`V(D)`, so all seven sets are pairwise disjoint and connected.

The twenty-one adjacencies decompose as follows.

1. The three `R` singletons give three pairs.
2. Each `R` singleton meets the two leaf-and-mate sets through the two
   leaves, giving six pairs.
3. Each `R` singleton meets `D` by boundary fullness, giving three pairs.
4. Each `R` singleton meets the `H` branch set through `H union {x}`, or,
   for a member of `M`, through the covering endpoint in (2.2), giving
   three pairs.
5. The two leaf-and-mate sets meet along `ell_e ell_f`.
6. Each leaf-and-mate set meets the `H` branch set through the leaf's
   edge to `H`, giving two pairs.
7. Each leaf-and-mate set meets `D` through its boundary mate, giving two
   pairs.
8. The `H` branch set meets `D` through the boundary vertex `x`.

The total is `3+6+3+3+1+2+2+1=21`.  No edge between the open components
is used.  Theorem 2.2 is correct.

## 3. Classification of failure

Write `T(z)=N_R(z) cap M`.  Collective adjacency of each defect edge to
every vertex of `R` gives

```text
union_{z in V(q)} T(z) = M.
```

The absence of the model from Section 2 is exactly the assertion that no
choice from `O_e times O_f` covers `M`.

If `M={r}`, either `O`-set of order two contains an endpoint seeing `r`
and therefore gives a covering pair with an arbitrary endpoint from the
other nonempty `O`-set.  Thus both `O`-sets are singletons, their members
miss `r`, and collective adjacency makes their mates see `r`.

If `M={r,s}` and, say, `O_e=V(e)`, its two traces cover `M`.  Neither can
equal `M`, since it would cover with any member of `O_f`; therefore the
two traces are exactly `{r}` and `{s}`.  Both `O`-sets cannot have order
two, since an endpoint on one edge seeing either row can be paired with
the complementary endpoint on the other edge.  Hence `O_f={z_f}` and
`T(z_f)` is empty.  Its mate sees both `r,s`.  The nonempty, pairwise
disjoint endpoint nonneighbour sets in `R` then force the mate to miss
exactly the third vertex `t` and force `z_f` to see `t`.  If both
`O`-sets are singletons, failure is precisely a common missed member of
`{r,s}`.  These alternatives are exhaustive and disjoint.  Theorem 3.1
is correct.

## 4. Forced-theta specialization

The standing balanced-branch input that `H` misses at most two boundary
vertices is essential here.  If `|M|=2`, the two missed `R` vertices
consume the entire allowance, so all four endpoints of `e,f` meet `H`;
equivalently `I_e=V(e)=I_f`.

The switching alternative of Theorem 3.1 contains an endpoint missing
both vertices of `M`.  It is impossible in both possible orientations:

- if the universally adjacent vertex `p` belongs to `M`, every endpoint
  sees `p`;
- if `M` consists of the other two vertices, every endpoint sees exactly
  one of them in the forced-theta incidence.

Thus both `O`-sets are singletons.  When `I_q=V(q)`, taking mates is a
bijection from `L_q` to `O_q`; consequently both `L`-sets are also
singletons.  Corollary 3.2, including the all-four-contacts conclusion,
is correct.

## 5. Degree calculations

Every leaf has a specified nonneighbour in a defect edge, and every defect
endpoint has both endpoints of the other defect edge as nonneighbours.
If one of these vertices had degree seven in a seven-connected graph, its
seven-vertex open neighbourhood would separate it from such a
nonneighbour.  Thus exclusion of an actual order-seven separation gives
degree at least eight for every vertex to which Section 4 applies.

For `lambda_q`, the neighbours outside `H` are exactly the other leaf,
the three vertices of `R`, the members of `L_q`, and possibly `x`.
There are no neighbours in the other defect edge or in `D`.  This proves
(4.1) and both bounds in (4.2).

For an endpoint `z in q`, its possible neighbours are exactly its mate,
its `3-k(z)` neighbours in `R`, possibly `lambda_q` and `x`, and its
neighbours in `H,D`.  The other leaf and the other defect edge contribute
none.  Comparing this exact degree expression with seven and eight proves
(4.3).

Finally, in the forced-theta branch `|L_q|=1`.  With the separately
established tight-core input `x lambda_q notin E(G)`, (4.1) and degree at
least eight give `|N_H(lambda_q)|>=3` for both leaves.  The source
correctly does not infer the prescribed two-path linkage from this degree
bound.

## 6. Scope and preservation qualification

The source uses two previously established inputs which are described in
its surrounding text rather than included in the numbered setup:

- `H` misses at most two vertices of `S`; and
- in the final minimum-degree specialization, neither leaf is adjacent to
  `x`.

The GREEN verdict is conditional on those inputs exactly as stated.  For a
standalone promoted version, they should be listed explicitly in the
relevant corollary hypotheses.

The older audited
[`hc7_balanced_endpoint_allocation.md`](../archive/hc7_balanced_endpoint_allocation.md)
(SHA-256
`85a575e9103b0f8d1440d64d8ae2322cf089cafe958225cbcf7e4f4649e920c8`)
must not be discarded as superseded.  Its row-cover theorem permits every
legal leaf-anchor pair and proves, in the general balanced boundary, that
at least one complete leaf-anchor set is a singleton.  The present theorem
instead couples each absorbed endpoint to its mate and gives the sharper
trace classification of that coupled choice.  In the forced-theta,
two-missed-row specialization the two formulations agree and both prove
that the two leaf-anchor sets are singletons and all four endpoints meet
`H`; outside that specialization the older row-cover statement is broader.

Accordingly the mate-exchange theorem is a valid refinement, not a
replacement for the prior endpoint-allocation theorem.  Neither result
supplies the remaining labelled two-path system, an order-seven
separation, or a proof of `HC_7`.
