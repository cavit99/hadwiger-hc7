# Audit of the strengthened root-connector reflection theorem

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_root_connector_reflection.md`

**Audited SHA-256:**
`dd2b25e2f9e3918661f4fbb4900c82a661cbe72a170941d9f315ce5d7f565a79`

**Promoted source SHA-256:**
`15f6fe1052426a0ccc0ee96a02d377370acfc00f0826d73c7ba5f1076106ddcc`

The promoted revision changes only the status paragraph to record this
re-audit.  Its theorem statements, proofs, dependencies, and trust boundary
are identical to the audited revision.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## 1. Scope of the material strengthening

The preceding revision required the two open-side sets supporting `X,Y` to
induce connected subgraphs.  The strengthened theorem instead assumes only
that

```text
G[X union F_X]  and  G[Y union F_Y]
```

are connected and contain an edge.  Thus a carrier set may be disconnected
before its independent boundary block is adjoined.  The audit checks that
every later use needs connectivity only after that adjoining operation.

## 2. Theorem 2.1: simultaneous contractions

The three contracted vertex sets are

```text
V(D) union {d},   F_X union X,   F_Y union Y.
```

They are pairwise disjoint.  The open-side sets `V(D),F_X,F_Y` are pairwise
disjoint by hypothesis, and the boundary sets `{d},X,Y` are pairwise
disjoint and disjoint from the open shore.

Each contracted set is connected and contains an edge:

1. `D` is connected and has a neighbour at `d`;
2. the definition of an `X`-carrier is exactly that `G[X union F_X]` is
   connected and contains an edge; and
3. the same holds for `Y union F_Y`.

Consequently each set has a spanning tree, even when `F_X` or `F_Y` has
several components which are connected only through boundary vertices.
The spanning trees are vertex-disjoint, so they may be contracted
simultaneously.  At least one edge, in fact an edge in every displayed tree,
is contracted; the result is a proper minor.  The proof never contracts a
disconnected carrier before adjoining its boundary block.

## 3. The four-object clique and exact pullback

Let the three contraction images be `Z_d,Z_X,Z_Y`, retaining `e` as a
singleton.  The six clique adjacencies are literal:

1. `Z_d-e` comes from a `D-e` edge;
2. `Z_d-Z_X` and `Z_d-Z_Y` come from the assumed `d-X` and `d-Y` edges;
3. `e-Z_X` and `e-Z_Y` come from the assumed `e-X` and `e-Y` edges; and
4. `Z_X-Z_Y` comes from the assumed `X-Y` edge.

Thus the four objects form a `K_4` in the proper minor and receive four
distinct colours in every proper six-colouring.

For the pullback, only vertices of `L`, the untouched vertex `e`, and the
boundary blocks are retained.  Give every vertex of `X` the colour of
`Z_X`, every vertex of `Y` the colour of `Z_Y`, and `d` the colour of
`Z_d`.  This is proper because:

* `X,Y` are independent bipartition classes and `de` is absent;
* all four block colours are distinct;
* every boundary edge between different blocks is represented between the
  corresponding contraction images; and
* every edge from `L` to a contracted boundary vertex is represented by an
  edge from `L` to the relevant image.  There are no `L-R` edges, so a
  carrier vertex creates no additional pullback constraint on `L`.

The four block colours are distinct, so the induced equality partition is
exactly

```text
X | Y | {d} | {e}.
```

If both closed shores realize this labelled partition, a permutation of
the six colour names aligns its four block colours.  The open shores are
anticomplete, so the colourings glue.

## 4. Corollaries 3.1 and 4.1

Corollary 3.1 is the direct negation of the three disjoint contraction
sets in Theorem 2.1.  It does not claim a generic linkage or a connected
support before the boundary block is adjoined.

For Corollary 4.1, if a common root neighbour `q` lies outside
`Q_0 union Q_1`, then `{q}`, `V(Q_0)`, and `V(Q_1)` are pairwise disjoint.
Boundary fullness and connectedness of each `Q_i` make its vertex set a
carrier for either nonempty independent boundary class.  Theorem 2.1
therefore applies exactly as stated.

## 5. Incidence-graph equivalence in Corollary 4.2

Let the components of `G[V(Q_i)-{q}]` form one part of the incidence graph
and let `Z` form the other.

### Incidence component implies carrier

Suppose an incidence component contains every vertex of `Z` and at least
one open-side component.  Take the union `F_Z` of the open-side components
represented there.  Each such component is connected.  Every incidence
edge represents a literal boundary-to-component edge, and connectedness of
the incidence component therefore makes `G[Z union F_Z]` connected.  Since
the incidence component meets both parts, this graph contains an edge.
Thus `F_Z` is a boundary-block carrier.  It is disjoint from `q` and from
the other full connected subgraph, so Theorem 2.1 gives the contradiction.

### Carrier implies incidence component

Conversely, let `F_Z subseteq V(Q_i)-{q}` be a carrier.  A path in the
connected graph `G[Z union F_Z]` alternates between boundary vertices and
maximal open-side subpaths.  Every such open-side subpath lies in a unique
component of `G[V(Q_i)-{q}]`; replacing it by that component gives a walk
in the incidence graph.  Hence all vertices of `Z` lie in one incidence
component.  Because `Z` is independent and the carrier graph contains an
edge, connectedness supplies at least one boundary-to-open-side edge, so
that incidence component also contains an open-side component.

This proves both directions, including the edge case `|Z|=1`.  The
“contains an edge” clause in the carrier definition rules out treating an
isolated singleton boundary vertex as a carrier.

## 6. Corollary 4.3

If `G[V(Q_i)-{q}]` is empty, then `V(Q_i)={q}`.  Boundary fullness makes
`q` the unique `Q_i`-neighbour of every member of both `X` and `Y`.

Otherwise let `K` be its unique component.  Fix `Z in {X,Y}`.  If every
vertex of `Z` had a neighbour in `K`, then all vertices of `Z` and `K`
would lie in one incidence component, contrary to Corollary 4.2.  Hence
some `z in Z` has no neighbour in `K`.  Boundary fullness gives `z` a
neighbour in `Q_i`; because the only vertex of `Q_i` outside `K` is `q`,
that neighbour is `q`, and it is the unique `Q_i`-neighbour of `z`.
Applying this argument separately to `X` and `Y` proves the conclusion.

No unmentioned 2-connectivity or induced-subgraph hypothesis is used.

## 7. Opposite-response application and trust boundary

In Section 5 the shore containing `Q_0,Q_1` is precisely the split-response
shore required in Sections 3--4; the opposite shore lacks that response.
The orientation is therefore consistent.

The theorem does not eliminate the incidence-entangled configuration,
split a full connected subgraph through a common root neighbour, produce a
three-carrier packing, or derive an order-seven separator.  Those
limitations are stated explicitly.  The opposite-response theorem is used
only for the application in Section 5, not in Theorem 2.1 itself.

Within this exact scope, no gap was found.
