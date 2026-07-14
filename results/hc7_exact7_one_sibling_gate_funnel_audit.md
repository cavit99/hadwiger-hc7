# Independent audit: exact-seven one-sibling gate funnel

**Verdict: GREEN.**  The parameter-uniform Hall principle, the specialized
missing-label matching, the paired-state carrier contraction, the support
dichotomy, the concentrated-gate conclusion, and the static treewidth
barrier are all valid under the hypotheses stated in
`hc7_exact7_one_sibling_gate_funnel.md`.

This audit does not claim that the one-sibling configuration, `HC_7`, or
Hadwiger's Conjecture is closed.

## 1. Exact-state reflection

For distinct `x in U_i` and `y in V_j`, with `i!=j`, the three rich-side
carriers are

\[
                  K\cup\{x\},\qquad J\cup\{y\},\qquad Q.
\]

They are pairwise disjoint: `K,J` are different components of `C-X`, the
gate vertices are distinct, and `Q` lies outside `C`.  The first two are
connected because every lobe hits every member of `X`; `Q` is connected by
hypothesis.  There is also a literal edge from `x` to `J`, so the first two
interior carriers are adjacent.

The definition of `U_i` makes `K union {x}` contact both members of `B_i`:
`K` contacts `a_i` and `x` contacts `t_i`.  The definition of `V_j` makes
`J union {y}` contact every member of `B_j`: `J` contacts the members
already in `B`, and `y` contacts all missing members.  Fullness lets `Q`
fund the third block.  Hence all three carrier--block unions are connected.

Every pair of contracted representatives is adjacent through the stated
literal edge between its two assigned boundary blocks (and the `Q` carrier
also contacts every boundary literal).  The retained singleton `c` sees
each representative through its prescribed `c-B_i` edge.  The contraction
is proper and gives exactly the equality partition `Pi` on the untouched
closed shore.  A palette permutation therefore aligns it with the legally
attained copy of `Pi`.  No colour is identified with a gate vertex or an
uncontracted model label.

## 2. Uniform Hall separator

In the parameter-uniform lemma, Hall failure gives a nonempty
`U subseteq D` such that

\[
                        |N_X(U)|<|U|.
\]

The proposed cut

\[
                        Z=(S-U)\cup N_X(U)
\]

has order

\[
                        k-|U|+|N_X(U)|<k,
\]

because `S` and `X` are disjoint.  Since `X` is a proper subset of the
component `C`, every vertex of `C-X` survives.  A surviving component
meeting `C-X` cannot reach `U`: every `U-C` edge has its `C` endpoint in
`X`, and every such endpoint lies in the deleted set `N_X(U)`.  It cannot
reach the far shore `L` directly because the separation is actual, cannot
enter another component of `G[R]` because `C` is a component of `G[R]`,
and every boundary exit other than `U` was deleted.  The nonempty far shore
`L` survives, so `Z` is a genuine separator below `k`, a contradiction.

No connectedness of `C-X` is needed.  The proper-subset condition is the
exact hypothesis ensuring that a component-side vertex survives.

For the one-sibling specialization,

\[
 D=S-(A\cup B)=T-B.
\]

Neither `K` nor `J` contacts `D`, and `C-X=K dotcup J`, so every `D-C`
edge ends in `X`.  Both lobes are nonempty, making `X` proper.  The uniform
lemma therefore supplies the claimed matching saturating `D`.

## 3. Support dichotomy

If `J` funds `B_j` and `D` is nonempty, choose `t_i in D`.  Then `i!=j`.
The Hall matching supplies `x in U_i`; since `J` already funds `B_j`,
`V_j=X`, and a gate vertex `y!=x` exists.  The exact-state reflection
applies.  Thus every nonreflecting duty-bearing sibling has `D=emptyset`,
equivalently `T subseteq B`.

If `J` funds no duty, its support contains at most `c` and one endpoint of
each of the three independent pairs.  The lower bound `|B|>=4` therefore
forces exactly

\[
                    B=\{c,r_1,r_2,r_3\},
                    \qquad r_i\in B_i.
\]

Here `D` consists precisely of those `t_i` for which `r_i=a_i`.  If
`|D|>=2`, two matched missing labels have distinct gate representatives.
The corresponding carriers `K union {x_i}` and `J union {x_j}` fund two
different duties, so the state reflects.  Hence `|D|<=1`: `D=emptyset`
lies in the cross-lobe family, while `|D|=1` relabels to

\[
                         B=\{c,a_1,t_2,t_3\}.
\]

These alternatives are exhaustive and do not silently reduce the general
one-sibling problem to a Moser boundary.

## 4. Concentrated-gate conclusion

Nonreflection is exactly the assertion that for `i!=j` there cannot be
distinct

\[
                         x\in U_i,\qquad y\in V_j.
\]

In the dutyless support every block contributes one endpoint `r_i`, and
with `W_i=N_X(\bar r_i)` one has `V_i=W_i`.  In the normalized
single-missing case, `U_1=W_1` is nonempty by the Hall matching.

If any one of `U_2,U_3,W_2,W_3` is nonempty, compare it with `W_1` or
`U_1`, using the opposite index.  The nonreflection condition says that
every element of the two nonempty sets must be equal.  Thus both are one
common singleton `\{z\}`.  Repeating the comparison with `U_1` or `W_1`
shows that every other nonempty set among

\[
                       U_1,U_2,U_3,W_1,W_2,W_3
\]

is the same singleton.  If all four other sets are empty,
`U_1=W_1` may be an arbitrary nonempty subset of `X`.  These are exactly
the two alternatives stated in the theorem; there is no omitted mixed
pattern.

The additional cross-lobe restrictions are also correct.  If
`j in F={i:B_i subseteq B}`, then `V_j=X`; hence any nonempty `U_i` with
`i!=j` supplies a distinct second gate and reflects.  One funded duty
allows only its homologous `U_j`; two funded duties force every `U_i` to
be empty.

## 5. Static quotient barrier

The displayed graph has the fourteen vertices and 37 literal edges stated
in the theorem.  Direct graph6 encoding gives

```text
MeB?_?@?]jl]~_~_?
```

The boundary verification is exact:

* every `a_i-t_i` is absent;
* `c` sees `B_1,B_2,B_3` through `ca_1,ca_2,ca_3`;
* the three block pairs are witnessed by `a_1a_2`, `a_1a_3`, and
  `a_2t_3`;
* `N_S(k)=A` and `N_S(j)=T union {a_1}`; and
* the gate triangle makes the lobe quotient on `{k,j} union X` equal to
  `K_5-kj`, which is three-connected.

Under elimination order

\[
 t_1,t_2,t_3,x_1,x_2,x_3,a_3,c,a_1,a_2,k,j,p,q,
\]

the filled later-neighbourhood orders are independently recomputed as

\[
 3,3,4,4,3,2,5,5,5,4,3,2,1,0.
\]

The resulting chordal completion has clique order at most six, so the
graph has treewidth at most five.  Since treewidth is minor-monotone and
`tw(K_7)=6`, the quotient has no `K_7` minor.

The interpretation in the theorem is appropriately narrow.  This graph
falsifies a static contact-plus-triangle-gate implication only.  It is not
asserted to have legal state attainment, seven-connectivity, or
contraction-criticality, and is not a counterexample to `HC_7`.

## 6. Trust boundary

The proved gain is the parameter-uniform Hall principle and its
state-specific one-sibling funnel.  The live families remain:

1. `T subseteq N_S(J)`, requiring a label-faithful cross-lobe split or a
   regenerated near-`K_7` handoff; and
2. `N_S(J)=\{c,a_1,t_2,t_3\}`, with the exact isolated/concentrated gate
   alternatives.

The audit does not infer a fixed pair, a new attained state on the descended
boundary, or a literal `K_7` from either residue.

## 7. Independent adversarial replay

A second checker independently enumerated all `64` sibling supports of
order at least four and imposed only the Hall matching and literal
cross-incidence obstruction.  Exactly `18` support types survived:

* the `15` sets containing all of `T` and a nonempty subset of `A`; and
* the three duty relabellings of `\{c,a_i,t_j,t_k\}`.

It also solved the single-missing portal constraints symbolically.  Their
negation is inconsistent: either all four off-index portal sets are empty,
or every nonempty relevant set is the same singleton.  Finally, it decoded
the displayed graph6 barrier independently and reproduced its `37` edges
and the complete fill sequence.  No additional hypothesis or survivor was
found.
