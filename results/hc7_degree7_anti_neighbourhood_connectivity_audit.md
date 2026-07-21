# Independent audit: degree-seven anti-neighbourhood connectivity

## Verdict

**GREEN** at the exact source revision

```text
a73429c60377546d55f9578a7795eb45634a98fdc87d84604ee62865880a90f3  results/hc7_degree7_anti_neighbourhood_connectivity.md
```

Theorem 1 is correct.  Its order-seven separation is oriented correctly,
the maximum packing numbers really are `(1,2)` in the only surviving
two-component case, and the singleton-component closure applies to the
side containing `{u}` and the other component of `G-N[u]` without reversing
the shores.

The checked revision also removes the superseded pre-promotion warning.  The
change is status-only: the theorem statement, proof, cited input revisions,
and trust boundary are unchanged.

Corollary 2 is also correct.  Its final “Audited inputs” paragraph records
the corrected GREEN-audited exact-block Kempe reduction at source hash

```text
19382ff7bc0065bc18a7caaeffd5c5fff46cf4ddc226d40036c751081a9853ff  results/hc7_bounded_interface_exact_block_kempe_reduction.md
```

The audit of that result is pinned to the displayed corrected hash.  Its
fixed-colour qualification does not affect Corollary 2: the application uses
Theorem 5.1, whose endpoint colour names are explicitly aligned before the
Kempe sequence.  The present theorem does not prove `HC_7`; it proves that
the anti-neighbourhood of a
degree-seven vertex is one nonempty connected component under the stated
hypothetical-counterexample assumptions.

## 1. Hypotheses and criticality

The assumptions say that `G` is not six-colourable and every proper minor
is six-colourable.  For any vertex `v`, the proper minor `G-v` is
six-colourable, and assigning a seventh colour to `v` gives a seven-colouring
of `G`.  Hence

\[
                              \chi(G)=7.
\]

Thus the contraction-critical inputs used later, including Dirac's
neighbourhood inequality, are within scope.  Seven-connectivity and
`K_7`-minor-freeness are stated explicitly.  The proof uses the established
case `HC_6` only in the initial nonemptiness argument.

## 2. Lines 20--25: nonemptiness

Put `S=N(u)`, where `d(u)=7`.  If `G-N[u]` were empty, then `u` would be
universal.  The graph `G-u` is six-colourable by proper-minor minimality.  It
cannot be five-colourable, because such a colouring plus a fresh colour on
`u` would six-colour `G`.  Therefore

\[
                            \chi(G-u)=6.
\]

The proved case `HC_6` supplies a `K_6` minor in `G-u`.  Universality of `u`
makes the singleton branch set `{u}` adjacent to all six branch sets, giving
a `K_7` minor.  This contradicts the hypothesis, so `G-N[u]` is nonempty.

No spanning assumption on the `K_6` model is needed: a universal vertex is
adjacent to every vertex of every branch set.

## 3. Lines 27--36: literal fullness of every component

Let `D_1,...,D_m` be the components of `G-N[u]`.  For each `D_i`,

\[
                         N_G(D_i)\subseteq S.
\]

There is no edge from `D_i` to `u`, because `D_i` lies outside `N[u]`, and
there is no edge to another `D_j`, by componenthood.  The vertex `u` remains
outside `D_i` after deleting `N_G(D_i)`, so `N_G(D_i)` is a genuine
separator.  Seven-connectivity gives `|N_G(D_i)|>=7`; since `|S|=7`,

\[
                           N_G(D_i)=S.                     \tag{3.1}
\]

Thus each component is a nonempty connected subgraph adjacent to every
literal boundary vertex.  The proof does not assume that one vertex of the
component is complete to `S`.

## 4. Lines 38--56: excluding three or more components

For fixed `D_1`, define the open sides

\[
 L=D_1,
 \qquad
 R=\{u\}\mathbin{\dot\cup}D_2\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}D_m.
\]

Together with `S`, these sets partition `V(G)`, and there is no `L-R` edge.
Both open sides are nonempty: `D_1` is nonempty and `u` belongs to `R`.
Consequently this is an actual separation with literal boundary `S` of
order seven.

By (3.1), `D_1` is `S`-full.  The singleton `{u}` is also `S`-full because
`S=N(u)`, and every `D_i` is `S`-full by (3.1).  These sets are pairwise
vertex-disjoint.  If `m>=3`, then `L` contains one full connected subgraph
and `R` contains the three disjoint full connected subgraphs

\[
                           \{u\},D_2,D_3.
\]

The adaptive exact-seven `(1,3)` theorem requires only the existence of
these packets, not equality of the maximum packing vector.  At its current
source hash

```text
14690180c44a9e5836591a54c4c7cdb7a26f1a2c78147470257072d5bc425e96  results/hc7_exact7_adaptive_packet_reflection.md
```

its proof gives either a `K_7`-minor model or a six-colouring of `G`.  Both
contradict the present hypotheses.  Therefore `m<=2`.

I independently checked the current adaptive proof: the thin-side
contraction is pulled back only to the opposite closed shore; the rich-side
reflection assigns its full connected subgraphs only after the exact
boundary partition is known; and the two exact block partitions align by a
permutation of the six colours.  No same-shore expansion is used.

## 5. Lines 58--67: the packing vector when `m=2`

Assume `m=2` and let `nu_L,nu_R` be the maximum numbers of disjoint
`S`-full connected subgraphs in the two open sides.  Then

\[
                    \nu_L\ge1,
                    \qquad
                    \nu_R\ge2,                              \tag{5.1}
\]

witnessed respectively by `D_1` and by `{u},D_2`.

The exact-seven packing theorem, at current source hash

```text
501f581d764607ef9cd13b854150dae95ea251efde0fdd28c77bb9632415fc57  results/hc7_exact_seven_packet_packing.md
```

proves

\[
             \nu_L+\nu_R\le4,
             \qquad
             \min\{\nu_L,\nu_R\}=1.                       \tag{5.2}
\]

Since `nu_R>=2`, (5.2) forces `nu_L=1`.  If `nu_R>=3`, one may choose one
full connected subgraph in `L` and three in `R` and apply the adaptive
`(1,3)` theorem again.  Hence `nu_R<=2`, and (5.1) yields

\[
                          (\nu_L,\nu_R)=(1,2).               \tag{5.3}
\]

This verifies the orientation used later: `L=D_1` is the packing-thin side,
whereas `R={u}\dot\cup D_2` is the side with two disjoint full components.
There is no inference that packing number one means a singleton, a small
transversal, or a connected shore beyond the component `D_1` already chosen.

The current packing proof was checked independently at each of its two
engines.  Its branch-set lift anchors each full connected subgraph at a
different boundary vertex and needs no edge between two such subgraphs.  Its
colour-gluing contraction is expanded only on the untouched opposite shore.
The seven-vertex triangle-free partition lemma was also rerun as described in
Section 8 below.

## 6. Lines 69--82: residual boundary and singleton closure

Let `H=G[S]`.  From (5.3), the packet-packing clique bound gives

\[
                              \omega(H)\le3.                 \tag{6.1}
\]

The adaptive `(1,2)` boundary theorem at current source hash

```text
df8d47261337659ade312bf8a6dfab22453c92bae5841bbb6b6fd303eadf6533  results/hc7_exact7_adaptive_12_boundary_closure.md
```

eliminates the separation whenever `H` has either its robust independent
block or its two-anchor `K_4`-minor configuration.  Thus a surviving `H`
belongs to the invariantly defined 129-graph residual.  This is exactly the
scope in which the later finite classification is used; the proof does not
classify all seven-vertex graphs.

Dirac's contraction-critical neighbourhood inequality gives

\[
             \alpha(H)=\alpha(G[N(u)])
                  \le d_G(u)-7+2=2.                         \tag{6.2}
\]

I independently reproduced the residual classification from the complete
NetworkX atlas.  Among the 129 residual isomorphism classes, exactly two have
independence number two.  They have 11 and 12 edges and are respectively
isomorphic to the displayed Moser spindle `M` and `M+13`.  This is a
classification *inside the residual*, exactly as the draft states.

It remains to verify that the singleton-component closure is applied with
the correct shore.  In the present orientation,

\[
                         G[R]=G[\{u\}\dot\cup D_2].
\]

There is no edge from `u` to `D_2`, because `D_2` is a component outside
`N[u]`.  Hence `G[R]` has exactly the two connected components `{u}` and
`D_2`, with `{u}` a singleton.  All hypotheses of the singleton-component
closure are now literal:

- the separation is actual and has order seven;
- its maximum packing vector is `(nu_L,nu_R)=(1,2)` in that orientation;
- `H` lies in the frozen 129 residual; and
- the rich open shore `R` has exactly two components, one singleton.

The current singleton closure has source hash

```text
a68b0f0efe5b526d050261fbec3e0c3df47a96d022cb90f95ae5b3ca9616d8d4  results/hc7_exact7_two_component_singleton_closure.md
```

and its existing audit is pinned to this exact hash.  I nevertheless checked
the direction of both contractions in its `M+13` branch.  To colour the
closed side containing `D_i`, the operation contracts through the opposite
component `D_j` together with `{u}`; no contracted connected subgraph is
expanded back onto its own side.  Both operations return the exact partition

\[
                         25\mid46\mid0\mid1\mid3,
\]

which glues on the two exterior components, and the sixth colour then extends
to `u`.  In the pure-Moser branch, the cited complete two-component theorem
has current source hash

```text
c0336db32657a971dd42cb73f45c449136af61eeaf74764de470cef38e9f6463  results/hc7_exact7_moser_two_component_closure.md
```

and its hypotheses match after replacing its distinguished vertex by `u`:
`N(u)=S` is the pure Moser spindle and `G-N[u]=D_1\dot\cup D_2` consists of
exactly two nonempty connected components.

Thus the singleton-component theorem excludes both residual possibilities.
The case `m=2` is impossible.  Nonemptiness and `m<=2` leave exactly `m=1`,
which proves Theorem 1.

## 7. Lines 87--112: pole-free paths

For Corollary 2, take the degree-seven vertex `u`, its sole exterior
component

\[
                         C=G-N[u],\qquad S=N(u),
\]

and the closed shores used by the bounded-interface theorem:

\[
                         A=G[C\cup S],\qquad B=G-C.
\]

Theorem 1 implies

\[
                         V(B)=S\cup\{u\},
\]

so `B-(S union {u})` is empty.  The GREEN-audited exact-block Kempe theorem
says that a returned pole-free path has its internal vertices wholly in `C`
or wholly in `B-(S union {u})`.

Its ends lie in two distinct components of a two-colour subgraph of `G[S]`.
An edge between the ends would put them in the same such component.
Therefore the ends are nonadjacent and the path has at least one internal
vertex.  It cannot have its nonempty interior in the empty second set.
Consequently all internal vertices lie in `C`, as claimed.

The current exact-block source hash and audit hash are

```text
19382ff7bc0065bc18a7caaeffd5c5fff46cf4ddc226d40036c751081a9853ff  results/hc7_bounded_interface_exact_block_kempe_reduction.md
45aad8373ed15a2ba961df4079ac8858b5332a01257b19d31f750d54fa444e20  results/hc7_bounded_interface_exact_block_kempe_reduction_audit.md
```

The source audit explicitly pins the corrected source hash.

## 8. Reproduced finite checks

All cited verifier files are Git-tracked.  I reran the three finite checks
supporting the repository inputs at the following exact revisions.

### 8.1 Seven-vertex triangle-free partition

```text
4c14537e9cec47afc5fd6860000d9c7529f9f21bd5aa5c2bfb19c3a7f17d6d84  results/hc7_exact_seven_partition_probe.cpp
```

Compiled with `c++ -O2 -std=c++17`; it returned exit status zero and

```text
GREEN labelled_triangle_free_graphs=133501 candidates=546 nonbip_no_singleton=0 nonbip_no_balanced_singleton=0
```

### 8.2 Adaptive `(1,2)` boundary census

```text
9e988ecc2daf2849850f540d549719b03bd0896c7bceeda47ac28e6dfcc632d8  results/hc7_exact7_adaptive_12_boundary_verify.py
```

It returned exit status zero, `VERIFIED`, 685 `K_4`-free unlabelled
boundaries, 876 proper equality partitions, 446 robust-block closures, and
the exact two-anchor residual distribution

```text
alpha=2,some_safe=False: 1
alpha=2,some_safe=True:  1
alpha=3,some_safe=False: 9
alpha=3,some_safe=True: 87
alpha=4,some_safe=True: 31
```

It also confirmed that the ten absolute-demand-three residuals all contain
two vertex-disjoint triangles.

### 8.3 Three-full-subgraph quotient census

```text
0c44a69f09e560d8122e776c3f7c14f6a60a71dc6fd3e166ab6c259d50be4833  results/hc7_exact7_adaptive_12_packet_quotient_probe.py
39955585e1c160d531499c485c4511eebb78fe507feaf002425422e7b5959d6  results/hc7_exact7_adaptive_12_boundary_probe.py
```

It returned exit status zero and reproduced

```text
graphs=685
robust_independent_block=446
two_anchor_k4_lift=246
overlap=136
no_robust_I_no_packet_k7=129
combined_residual_by_minimum_demand={2: 119, 3: 10}
connected_rich_one_anchor_extra=33
connected_rich_residual_by_alpha_demand={(4, 2): 22, (3, 2): 67, (3, 3): 7}
```

As an additional independent identity check, the residual probe at hash

```text
b30af6f324292347a830d8a7abfea6966a37bfc34c4cffabc99f3879c89ade60  results/hc7_exact7_adaptive_12_residue_probe.py
```

returned exactly one `(alpha,edges)=(2,11)` and one `(2,12)` residual.  A
fresh isomorphism test identified them as `M` and `M+13`, respectively.

These are finite boundary classifications only.  The audit makes no
realizability inference beyond the conceptual closure theorems that use
them.

## 9. Exact dependency revisions

The direct repository dependencies checked in this audit are:

| result | source SHA-256 | audit SHA-256 | finding |
|---|---|---|---|
| exact-seven packing | `501f581d764607ef9cd13b854150dae95ea251efde0fdd28c77bb9632415fc57` | `d6599c87be38904c04341afdba0098a2799608201353a55c7ac863cebaba11ac` | independently rechecked GREEN |
| adaptive `(1,3)` reflection | `14690180c44a9e5836591a54c4c7cdb7a26f1a2c78147470257072d5bc425e96` | `5cc57094a89db1b7554db21a0c38d26003244fd030df8e2235b776067291825f` | independently rechecked GREEN |
| adaptive `(1,2)` closure | `df8d47261337659ade312bf8a6dfab22453c92bae5841bbb6b6fd303eadf6533` | `57f9a3612ce2f832fcb987947d7e03de431dbb7c6b1500609bb6ae2c8970914b` | independently rechecked GREEN |
| singleton-component closure | `a68b0f0efe5b526d050261fbec3e0c3df47a96d022cb90f95ae5b3ca9616d8d4` | `db70f6f55328f4cf51043b4b49cf30e1a4ffb8f82e91144abc320c9e8ff2c942` | audit pinned; application rechecked GREEN |
| pure-Moser two-component closure | `c0336db32657a971dd42cb73f45c449136af61eeaf74764de470cef38e9f6463` | `498e6587741ef4421dd747abd784e23830509fa163a8e8bde90ef5878dac5426` | transitive singleton-closure branch rechecked GREEN |
| low-degree adjacent-pair interface | `263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca` | `001e27eecf24c938d2e93f70e428e5c82e39d1a2835bcaa49450aa0132f4f027` | exact bounded-interface setup for Corollary 2 |
| exact-block Kempe reduction | `19382ff7bc0065bc18a7caaeffd5c5fff46cf4ddc226d40036c751081a9853ff` | `45aad8373ed15a2ba961df4079ac8858b5332a01257b19d31f750d54fa444e20` | corrected audit pinned; fixed-colour Corollary 2 application rechecked GREEN |

The first three legacy audits did not themselves record their current source
hashes.  This audit checked the displayed current sources directly and pins
them here.  The source hashes agree with the audit-integrity table in the
draft theorem.

## 10. Scope and residual risks

1. The theorem depends on the established external results `HC_6` and
   Dirac's contraction-critical neighbourhood inequality; neither is newly
   proved here.
2. The conclusion is restricted to a degree-seven vertex.  The replacement
   boundary associated with another anti-neighbourhood component at degree
   eight or nine need not be the original full neighbourhood.
3. The theorem proves connectedness of `G-N[u]`, not two-connectivity or a
   labelled branch-set split inside that component.
4. Corollary 2 localizes the already-proved Kempe obstruction paths.  It does
   not compose them, preserve a boundary colouring through a contraction, or
   construct a `K_7` model.
5. The finite residual census is used only under the invariant 129-residual
   hypothesis.  Independence number at most two alone would not imply the
   Moser alternatives.

Subject to these explicit limits, no omitted case, shore reversal,
same-side colouring expansion, or stale finite count was found.
