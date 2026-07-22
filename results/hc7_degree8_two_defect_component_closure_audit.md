# Audit: degree-eight two-defect component closure

**Audit type:** separate internal cold audit with independent finite rerun

**Verdict:** **GREEN**

Audited theorem:
[`hc7_degree8_two_defect_component_closure.md`](hc7_degree8_two_defect_component_closure.md)

Audited theorem SHA-256:

```text
85e4f2d55545254f8a0bedc5e190f9299cf2f69afc960c0a4c186c9f00819857
```

Audited mathematical verifier:
[`hc7_degree8_two_defect_component_closure_verify.py`](hc7_degree8_two_defect_component_closure_verify.py)

Audited verifier SHA-256:

```text
b93e9a55dda0b61f35ce925fafaf5fca42441ec8b2249e647740621fd6f0e48f
```

This is an internal mathematical audit, not external peer review or a
proof-assistant certificate.  The result does not prove `HC_7`.

## 1. Independent finite run and coverage

Running the documented command against nauty's complete unlabelled
order-eight catalogue reproduced the recorded output exactly:

```text
order8_graphs 12346
compact_boundaries 185
missed_sets 37
tested_missed_set_orientations 253265
anchor_certificates 253265
anchor_certificate_sha256 882a558c46dfc7a6b68008a598dd0e30aed3d51b8b05f5e15bca1554ea863d44
failures 0
PASS degree8_two_defect_component_closure
```

The run was repeated under ordinary `python3` and under `python3 -O`, both
with explicit `geng -q 8` input and with the verifier invoking `geng` after
reading EOF.  All four runs produced the displayed output byte for byte.
The sibling imports resolve under the documented repository-root command.
Their source hashes are

```text
hc7_degree8_nonedge_bipartition_classification_verify.py
c01f145349831eb34f3af0ef772c6fe07d82b4b00f9630cabe9ba557eb0be8a9

hc7_order8_three_component_boundary_verify.py
d4677fcd39be4e4411176b8c916ae637057d34a70758ba3bbde70ed16badd68e
```

The finite predicates match the strengthened Section 1 directly.
`has_independent_four` is true exactly when `alpha(H)>=4`, and
`has_compact_k4` exhausts all two-vertex deletions and applies an exact
deletion--contraction `K_4`-minor test.  The verifier therefore retains
exactly the `185` unlabelled graphs satisfying (1.1), including
`K_1 vee C_7`; it makes no choice of `I,T,p,q` and uses no aligned-boundary
classification.

There are exactly

\[
                1+\binom81+\binom82=37
\]

subsets of an eight-set of order at most two.  The outer product visits
every ordered pair `(M_E,M_F)`, so the exact coverage count is

\[
                         185\cdot37^2=253265.
\]

Every labelled theorem instance is carried by an isomorphism to one of
these unlabelled graphs together with one of the enumerated ordered
missed-set pairs.  No boundary labelling or additional structure is needed
by the strengthened theorem.

The per-graph cache only identifies a missed-set pair with its shore
reversal.  The certificate predicate is symmetric under that reversal:
if the anchor tuple is `(e_0,e_1,f_0,f_1)`, then
`(f_0,f_1,e_0,e_1)` is a certificate for the reversed pair, with the same
two singleton anchors.  Nonexistence is symmetric for the same reason.
The verifier performs exactly this half-tuple swap and then independently
calls `valid_certificate` on every one of the `253,265` ordered instances.
Thus the cache is an optimization, not a quotient of the asserted cases.

Within either shore the two connected sets have identical hypotheses and
their only required mutual relation is symmetric adjacency, so enumerating
their two anchors as an unordered combination is complete.  The same is
true of the two singleton branch sets.  The search ranges over every edge
`rs`, every eligible two-anchor choice on each shore, and every disjoint
combination of those choices.

## 2. The certificate gives all 21 adjacencies

Let the four augmented bags be

```text
B_E^0 = A_E^0 union {a_E^0},  B_E^1 = A_E^1 union {a_E^1},
B_F^0 = A_F^0 union {a_F^0},  B_F^1 = A_F^1 union {a_F^1}.
```

The four anchors are distinct, avoid the missed set of their own
connected set, and lie in `S`.  Each augmented bag is therefore connected.
The four original sets are pairwise disjoint and avoid `S union {u}`;
the anchors, `r,s`, and `u` are all distinct, so the seven branch sets are
pairwise disjoint.

The 21 required adjacencies divide exactly as follows.

1. The two same-shore bag pairs are adjacent by hypothesis.
2. For each of the four cross-shore bag pairs, the checker requires either
   the left connected set to see the right anchor, the right connected set
   to see the left anchor, or an edge between the anchors in `H`.
3. Each of the four bags is adjacent to each of `{r},{s}`: the checker
   requires either direct visibility from the connected set or an
   anchor--singleton edge.  These are eight adjacencies.
4. The checker requires `rs` to be an edge.
5. The six remaining adjacencies join `{u}` to the four augmented bags and
   to `{r},{s}`.  They are automatic because all six selected boundary
   vertices lie in `S=N(u)`.

Thus the hypotheses supply eight automatic adjacencies and the checker
tests the other thirteen.  Their total is `21`, with no assumed edge
between an `E`-set and an `F`-set.  Connectivity, disjointness, and all
pairwise adjacencies required for an explicit `K_7`-minor model follow.

## 3. Universal connector--carrier entanglement

Fix a shore `Q`, a root connector `R subseteq Q`, and a carrier
`K subseteq Q` for one block `B`, and suppose `R` and `K` are disjoint.
Let `A` be the other block.  Assign `u` to the same open side as `Q`; this
is a valid application of the reflection theorem because `u` has no
neighbour in the opposite open shore.

For the merged response, the three contracted sets are

```text
A union {u},   B union K,   R union {p,q}.
```

They are pairwise disjoint, connected, and contain edges.  Their images
form a triangle: `u` supplies the first--second and first--third
adjacencies, while a root-to-`B` boundary edge supplies the
second--third adjacency.  The required root contacts, and the edge between
`I,T` used below, follow from `alpha(G[S])<=3` in the imported degree-eight
setup.  Pulling a six-colouring of the proper minor back only to the
opposite shore gives the exact merged partition.

For the split response, the root-connector reflection theorem applies to
the three pairwise disjoint open-side sets `R,K,{u}`.  The set `K` is a
carrier for `B`, while `{u}` is a carrier for `A`; the aligned boundary
supplies the edge between the blocks and all four root-to-block contacts.
It gives the exact split partition on the same opposite closed shore.

The fixed `Q`-shore realizes one of these two partitions.  Selecting the
matching opposite-shore colouring, aligning its block colours, and gluing
gives a six-colouring of `G-u`.  At most four colours occur on `S`, so a
fifth or sixth colour extends to `u`.  This contradicts `chi(G)=7`.

The choices of `R`, the block `B`, and its carrier `K` were arbitrary.
Accordingly the proof establishes the stated universal intersection
quantifiers; it does not silently replace them by selected path witnesses.

Corollary 3.2 follows with the same universal quantifier.  Since `pq` is a
nonedge, every `p`--`q` path in the named graph has nonempty connected open
interior, which is a root connector.  Theorem 3.1 therefore makes every
block carrier meet every such path, exactly the assertion that its vertex
set separates `p` from `q`.  Its intersections with internally
vertex-disjoint paths are distinct carrier vertices, proving the stated
cardinality bound without upgrading edge-disjointness to
vertex-disjointness.

## 4. Coherence of the missed pair

The audited four-incidence-split corollary forces every residual component
to miss a member of each independent triple.  If `m_D=2`, these are its
only two boundary misses, so `D` sees exactly two members of `I` and two of
`T`, as well as both roots.

Suppose two such components missed different vertices of `I`.  Their two
neighbour pairs in the three-set `I` overlap, and their union is all of
`I`.  In the incidence graph the two component vertices and their shared
boundary neighbour therefore put all three vertices of `I` in one
connected component, contradicting the split.  Hence every two-defect
component on the shore misses the same member of `I`.  The identical
argument for `T` gives one coherent pair `M_Q`.

This uses only connectivity in the incidence graph.  It does not assume
that the residual components are adjacent or that their path attachments
occur in any prescribed order.

## 5. Path-segment bags and host closure

Because `Q` is connected and the aligned path has nonempty interior, each
component of `Q-V(P_Q^circ)` has a neighbour on that interior.  For two
selected components, choose attachment vertices `x_0,x_1`.

If the attachments coincide, adjoining their common vertex to one
component makes two disjoint connected sets adjacent through the edge to
the other component.  If they differ, the `x_0`--`x_1` segment of the
path lies wholly in its open interior.  Splitting this segment across one
edge and adjoining the two sides to their respective components produces
two disjoint connected sets adjacent across that edge.  Each set retains
its original component and hence all contacts with `S-M_Q`.

Applying this construction independently in `E` and `F` gives four
pairwise disjoint sets; the only required within-shore adjacencies are the
two chosen split edges.  The compact boundary hypotheses are exactly those
of the finite allocation theorem, so its seven branch sets lift directly
in the unchanged host.  This proves Theorem 4.1 without turning a residual
component into an alleged component of `G-N[u]`.

## 6. Trust boundary and reproducibility note

The finite result trusts nauty's complete unlabelled order-eight catalogue,
CPython, and the two imported exact graph routines at the hashes above.
The verifier's coverage totals and certificate checks use explicit
`require` calls rather than removable `assert` statements.  The ordinary
and optimized runs therefore enforce the same acceptance conditions and,
as recorded above, return the same certificate digest.  The digest is
deterministic for the documented catalogue order and is reproducibility
metadata; coverage rests on visiting and validating every retained ordered
instance, not on treating the digest as a proof certificate.

No mathematical gap was found at the audited hashes.  The result excludes
two two-defect residual components on both aligned shores.  It does not
bound path-contact multiplicities, turn a post-path component into a
same-host anti-neighbourhood component, close the odd-wheel branch, or
prove `HC_7`.
