# Independent audit: matching-deletion separator lift

**Verdict:** **GREEN.**

This audit covers the complete final source
[`hc7_matching_deletion_separator_lift.md`](hc7_matching_deletion_separator_lift.md),
including the exact-signature derangement theorem, the weighted separation
order, and the five-connected regeneration consequence.

**Audited source SHA-256:**
`efae06e4b2f95d1272c3f17b152a839da9e8ff418c1e039429af47b888085d71`.

**Current source SHA-256:**
`ef682c03c58df5e0618820fe2e5be2bddb97e990f0d37296f50b3b38d5932d7e`.
The only post-audit change was the status line recording this audit.

## 1. Separator budget and equality

For terminals `a in L` and `b in R`, the local form of Menger's theorem
in a `k`-connected graph gives `k` internally vertex-disjoint paths.  This
includes the adjacent-terminal case: the edge `ab`, when present, is one
of the paths.

Every path avoiding `S` uses a deleted matching edge which crosses from
`L` to `R`.  Distinct internally disjoint paths cannot share such an edge:
unless it is the direct path `ab`, at least one end would be a shared
internal vertex.  Hence boundary vertices and crossing matching edges
give at most

\[
                   |S|+|F(L,R)|
\]

paths.  At equality, all of these resources are saturated.  A path using
both a boundary vertex and a crossing row, or using two crossing rows,
would consume two resources while accounting for only one path and make
the equality impossible.  The exact resource description in Theorem 1.1
is therefore valid.

The connectivity bound for `G-F` and the stated crossing counts at cut
orders four, five, and six follow immediately.  No colouring or model
hypothesis is used here.

## 2. Literal and model-preserving lifts

Selecting one end of each crossing matching edge hits every possible
`L-R` edge of `G`.  The selected ends are distinct and outside `S`, so the
lift has order exactly `|S|+|F(L,R)|`.  With three crossing rows, any
selection using at least one end from each shore leaves an unselected end
on each shore; this proves the exact-four literal lift.

For a split model, the additional hypothesis

```text
no edge of F-{xy} has both ends in Q
```

is exactly what is needed to keep the singleton `K_4` literal in `G-F`.
It is automatic for the later three pairwise vertex-disjoint supports.
After orienting `x in L`, `y in R`, all off-boundary vertices of `Q` lie
in at most one shore, and selecting the opposite split endpoint places the
whole support in that closed shore.  The preferred-endpoint lemma is valid
at this scope.

## 3. Exceptional four-cut geometry

The legal endpoint choices form an independent product over the three
rows.  If no legal choice leaves both shores nonempty, one shore is exactly
its three matching endpoints and all three preferences are forced toward
that shore.  A boundary-contained `Q_i` would give a free choice and hence
a mixed selection, so after orientation the exceptional state is exactly

\[
 R=\{y_1,y_2,y_3\},\qquad
 \varnothing\ne Q_i-S\subseteq L.
\]

Each `y_i` has at most the four vertices of `S`, the other two vertices of
`R`, and `x_i` as neighbours.  Seven-connectivity forces all seven
adjacencies, so `R` is a triangle complete to `S`.

The graph `H=G-R` is four-connected.  An `S`-rooted `K_4` model in `H`
together with the three singleton bags of `R` would be a `K_7` model.
The four-connected case of Fabila-Monroy and Wood's rooted-`K_4` theorem
therefore makes `H` planar.  The degree accounting is correct:

\[
 \sum_{v\in V(H)}d_H(v)
 \ge 4\cdot4+3\cdot6+7(n-7)=7n-15>6n-12.
\]

This contradicts planarity and eliminates the exceptional choice.  The
resulting actual exact-seven separation retains literal model sides and
therefore admits the ordinary anchored exact-seven rank.

## 4. Exact matching signatures and derangement

If every proper minor of `G` is `p`-colourable, then every nonempty
`D subseteq F` gives the required exact signature.  The minor `G/D` is
proper.  Since `F` is a matching, every edge in `F-D` survives with two
distinct ends and is proper in its colouring; expansion makes precisely
the pairs in `D` equal in `G-F`.

For Theorem 5.1, suppose a selected endpoint set erases `L`.  Then `L=X`
consists of the `q` distinct left ends of the crossing rows.  A vertex of
`L` can see only the other `q-1` vertices of `L`, the `k-q` boundary
vertices, and its matching mate.  This is exactly `k` possible neighbours.
The inequality `delta(G)>=k` forces `L` to be a clique complete to `S`.
Those clique and boundary edges remain in `G-F`, because each vertex of
`L` is already incident with its unique matching edge.

Use the exact signature for the entire nonempty set `F(L,R)`.  The clique
vertices have distinct colours, their mates have the corresponding same
colours, and `S` avoids those colours.  For `q>=2`, a fixed-point-free
permutation of the colours on `L` preserves the clique and `L-S` edges and
makes every crossing matching edge proper.  No noncrossing matching edge
is incident with `L`, and every such edge was already proper.  This would
`(k-1)`-colour `G`, a contradiction.  The symmetric argument handles an
erased right shore, so the theorem's universal quantifier over all endpoint
selections is justified.

The uses of strong contraction-criticality are exact and limited:

* proper-minor colourability supplies every nonempty matching signature;
* `chi(G)=7` excludes the all-proper signature and supplies the final
  recolouring contradiction; and
* edge deletion gives `chi(G-F)<=6` in the later chromatic fork.

Ordinary one-edge contraction-criticality would not suffice for the
multi-edge signatures.

## 5. Weighted submodularity and the anchored rank

Interpret `K^*` as `K` plus a new length-two path `u-w_e-v` for every
deleted edge `e=uv in F` (equivalently, subdivide each edge of `F` in
`G`).  For a fixed separation of `K`, the vertex `w_e` is forced into the
boundary exactly when `u` and `v` occupy opposite open shores.  In every
other placement it can be put on a compatible closed side.  Thus the
minimum extension order in `K^*` is exactly

\[
                  |A\cap B|+|F(A-B,B-A)|.
\]

Take minimum extensions of two separations.  Their meet and join restrict
to the corresponding meet and join on `K`.  Ordinary separation-order
submodularity in `K^*`, followed by lower-bounding the two corner orders by
their minimum extension orders, proves the displayed weighted
submodularity inequality.  An exhaustive check of all `3^4=81` placements
of the two ends of one weighted edge in two separations also gives zero
failures; additivity then agrees with the subdivision proof.

Literal roots make both corners actual.  The separator budget gives
weighted order at least `k` for each, while submodularity bounds their sum
by `2k`; both therefore have order exactly `k`.  The same elementary set
containments preserve every declared model side.  The meet's rooted open
shore is the intersection of the two original rooted shores and is a
proper subset of both when they are nonnested.  Open-shore cardinality is
therefore a strict well-founded rank on the anchored weighted class.

This rank statement concerns weighted separations of `K`.  It does not
claim that every smaller weighted corner has an actual lift when exactly
one row crosses; Section 8 explicitly retains that `q=1` lock.  The
four-cut output itself has `q=3`, and its actual exact-seven lift also has
the ordinary anchored rank from Section 4.

## 6. The `HC_7` consequence and regeneration

For the frozen hypothetical minor-minimal `HC_7` counterexample, the
needed ambient facts are: `G` is seven-connected, seven-chromatic,
strongly seven-contraction-critical, and `K_7`-minor-free.  Thus the exact
six-colour signatures required by Theorem 5.1 really are available.

With three pairwise vertex-disjoint split supports, `F` is a matching and
every singleton `Q_i` remains a clique in `K=G-F`.  An exact four-cut has
all three rows crossing and weighted order seven.  Choosing each preferred
endpoint preserves all three supports, and the universal `q=3`
derangement theorem guarantees that neither shore is erased.  Hence every
`kappa(K)=4` instance returns an actual, ranked, model-preserving
exact-seven handoff.

If this branch is absent, `K` is at least five-connected.  Deleting the
four vertices of `Q_i` leaves a connected graph containing `x_i,y_i`, so
it contains an `x_i-y_i` path avoiding `Q_i`.  The path is a connected
fifth branch bag.  It retains the original contact with every singleton
of `Q_i`, because no other edge of the matching can be incident with
`x_i` or `y_i`; and `Q_i` remains a clique by pairwise support
disjointness.  This is a labelled `K_5` model in the one common deletion
graph.

The three regenerated path bags are not asserted to be pairwise disjoint,
nor to have support at most six.  The source states both limitations
correctly.  Together with the previously proved chromatic fork, the exact
residue is an at-least-five-connected `K` with `chi(K) in {5,6}`, all
seven non-all-proper signatures, and the three separately regenerated
labelled models.

## 7. Trust boundary

The proof closes every weighted-order-seven lift with at least two
crossing rows.  It does not manufacture the all-proper signature, compose
the three potentially overlapping regenerated paths, or eliminate the
single-row endpoint lock.  No stronger conclusion is used in the source.
