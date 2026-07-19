# Independent internal audit: an endpoint shared portal at an order-eight boundary

**Verdict:** **GREEN** for Theorem 1.1 and Corollary 1.2 at the exact
revision below.  This is an internal mathematical audit, not external peer
review.  The result does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_endpoint_shared_portal_completion.md`](hc7_order8_endpoint_shared_portal_completion.md)
at SHA-256

```text
8de56da2b11d62cc6b138413d7a8dfed9d808f15186f3db1984ecd5fabb4814c
```

This is the promoted `results/` revision of the source previously audited
at SHA-256

```text
a536dcdc79a22e135804c8b9a8aa08544f2dcf745f775bf4cf1c09e8ea4869e9
```

The promotion changed only status and repository-path metadata.  The
theorem statements, proof, corollary, dependency roles, and trust boundary
are mathematically unchanged.  The complete promoted source was compared
with the sections audited below before carrying the GREEN verdict to the
current hash.

The current promoted paths and hashes of the four mathematical dependencies
are:

```text
c973d105dd9441840de98bf9ebf0c7a362a76f4980400ea3a9e403bd5b116560
  results/hc7_order8_overlapping_interval_normal_form.md
1d976b6ece78b66c08a87df36cfc3f31a3e8511d57aa6990aeaa28c7c67c76b3
  results/hc7_order8_three_component_boundary_classification.md
1aa7c959a181b8d86075eb5c2822c5328c2438c5f2e4f47c0ee8c2a3bb18c059
  results/hc7_order8_strict_reversal_completion.md
a9e4e17e5a66fc9767388f7983607cce9b68393a83189f2e6aad4583f96a4570
  results/hc7_order8_three_component_path_completion.md
```

Each dependency has its own adjacent audit.  This promotion repin does not
alter or enlarge those separate verdicts.

No unresolved assumption or gap remains in the displayed statements.

## 1. The endpoint neighbourhood and the choice of the second defect

After reversing the induced path if necessary, the shared portal is `p_0`.
The normal form gives the literal edges `p_0d,p_0e`, and its suffix
alternative either already returns an order-seven separation or makes
`B=P[1,m]` adjacent to every vertex of `S-{e}`.  Since `m>=1`, this suffix
is nonempty.

Because `P` is an induced component of `G-S`, the only neighbour of `p_0`
outside `S` is `p_1`.  Hence

```text
N_G(p_0)=(N_G(p_0) cap S) dot-union {p_1}.
```

Deleting this neighbourhood isolates `p_0`, while either of the two other
components of `G-S` remains nonempty.  It is therefore a genuine separator.
Seven-connectivity gives at least six boundary neighbours.  If there are
exactly six, the displayed neighbourhood has order seven and is an actual
order-seven separation.

Otherwise `p_0` has seven or eight neighbours in the eight-set `S`.  In the
seven-neighbour case its unique missed vertex `f` is not `e`, because
`p_0e` is an edge.  In the eight-neighbour case any `f!=e` works.  Thus the
proof legitimately obtains distinct `f,e` for which `A={p_0}` is adjacent
to every vertex of `S-{f}`.  It does not assume that `A` misses `f`.

## 2. The boundary odd-cycle dichotomy

The hypotheses of the audited three-component classification are present:
the three components are boundary-full, every proper minor is
six-colourable, `G` is not six-colourable, and `G` is `K_7`-minor-free.
Consequently `G[S]` contains two vertex-disjoint odd cycles.

If `G[S-{f,e}]` is nonbipartite, a shortest odd cycle has order three or
five.  The audited strict-reversal Lemma 1.1 applies to the four pairwise
disjoint connected subgraphs `Q_0,Q_1,A,B`: the first two are boundary-full,
`A` meets `S-{f}`, `B` meets `S-{e}`, and `A,B` are adjacent through
`p_0p_1`.  Its explicit seven branch sets therefore give a `K_7` minor.
That lemma needs only the asserted lower bounds on boundary contacts.

Suppose instead that `S-{f,e}=X dot-union Y` is bipartite.  Each of the two
disjoint odd cycles must contain `f` or `e`.  Neither can contain both,
because the other would then avoid both and be an odd cycle in the
bipartite graph.  The cycles therefore contain different distinguished
vertices.  Removing that vertex from its odd cycle leaves a nonempty path
of odd length with endpoints in opposite bipartition classes.  Hence
`X,Y` are nonempty and each of `f,e` has a neighbour in each of `X,Y`, as
used later.

## 3. The nonadjacent-defect contraction

When `fe` is absent, the partition

```text
X | Y | {f,e}
```

is proper.  Giving its three blocks distinct colours and giving the induced
path two fresh colours properly colours the closed path side.

For fixed distinct `i,j`, the three sets

```text
A union X,  B union Y,  Q_j union {f,e}
```

are pairwise disjoint and connected.  Their contraction images form a
triangle: the first two are adjacent through `p_0p_1`, the first meets the
third through `p_0e`, and the second meets it through an edge from `B` to
`f`.  At least one edge is contracted, so the resulting graph is a proper
minor.  Expanding its colouring only on `G[Q_i union S]` is safe: `X,Y`,
and `{f,e}` are independent, the triangle gives the three distinct block
colours, and every original boundary-to-`Q_i` edge is represented after
contraction.  Thus the exact displayed boundary partition is obtained on
both full-component sides and glues to the path-side colouring.

## 4. The adjacent-defect contraction

When `fe` is an edge, the partition

```text
X | Y | {f} | {e}
```

is proper.  The two connected sets `A union X` and `B union Y` are disjoint,
and their contraction images together with the unchanged vertices `f,e`
form a four-clique:

- the images meet through `p_0p_1`;
- the first image meets `e` through `p_0e` and meets `f` through the
  previously proved edge from `f` into `X`;
- the second image meets `f` through `B` and meets `e` through the
  previously proved edge from `e` into `Y`; and
- `fe` is present.

Since `X,Y` are nonempty, these contractions make a proper minor.  A
six-colouring assigns four distinct colours to the clique, and expansion
on either untouched full-component side induces exactly the four-block
boundary partition.  Those two colourings align with the direct path-side
colouring and glue.

Additional contacts of `A` to `f` or of `B` to `e` do not invalidate any
contraction or colouring.  No step silently strengthens “adjacent to every
vertex except possibly one” to an exact one-defect neighbourhood.

## 5. Exhaustion and trust boundary

For an overlapping pair of demand intervals, the audited normal form has
either strict reversal (`a>b`) or a shared portal (`a=b=q`).  Strict
reversal is covered by its adjacent GREEN completion.  A shared portal is
either internal (`0<q<m`), covered by the adjacent GREEN path-component
construction, or is one of the two endpoints, covered by Theorem 1.1 after
reversing the path when necessary.  Because `m>=1`, these cases are
exhaustive.

The GREEN verdict is confined to the exact three-component,
boundary-full, induced-path setting in the source.  It does not cover a
singleton selected component, a non-path component, an order-eight
interface with only two components, or compatibility of the colourings on
the returned order-seven separation.
