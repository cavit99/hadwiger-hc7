# Independent audit: fixed-partition coverage transition barrier

**Verdict:** **GREEN** for the exact source revision below.

This is a separate internal mathematical audit, not external peer review.  It
checks the displayed graph and colouring, the boundary partition and its
required sets, the connected-support packing calculation, the bichromatic
obstruction path, the width-four certificate, and the stated trust boundary.

## Audited revision

The audited source is
`barriers/hc7_exact7_fixed_partition_coverage_transition_barrier.md`.

**Source SHA-256:**

```text
2ddd068294d0f5d0ada9ba63a3d4aa7e4062e6e69bb0dbd8da07a242f07280ee
```

The companion verifier is
`barriers/hc7_exact7_fixed_partition_coverage_transition_barrier_verify.py`
at SHA-256

```text
6fc51021893a963975ee1ada6b7b183eb7c46de932097aa6805971e7e687cbe1
```

Running it with Python 3 prints

```text
GREEN fixed-partition coverage transition barrier
order=14 size=25 treewidth<=4 kappa_P(Pi)=1 minimum_support=4
obstruction_contacts=2,4,5,6 extension_orders=A:5,B:5,D:6
```

## 1. Graph, partition, and required sets

The graph has fourteen vertices and twenty-five edges: eleven edges in the
Moser-spindle boundary, seven edges in the induced open-side cycle, and seven
boundary--open-side edges.  The displayed boundary blocks are independent.
The only singleton block is `{6}`, so `U={6}` is the maximum clique induced
by singleton blocks.  The edges `26`, `16`, and `56` show that every one of
the three nonsingleton blocks has a boundary edge to `6`.  Hence the literal
required set

\[
D_U(C)=C\cup\{u\in U:E(u,C)=\varnothing\}
\]

is exactly `C` for each of `A`, `B`, and `D`, as claimed.  The three block
unions are pairwise adjacent through boundary edges.

The open-side graph is an induced seven-cycle.  Its listed boundary contacts
are unique, and together meet every literal boundary vertex, so it is
connected and boundary-full.

## 2. Connected-support calculation

A connected support for a block must contain both of its unique portal
vertices.  For every pair of distinct blocks the two portal pairs alternate
around the cycle.  Two vertex-disjoint connected subgraphs of a cycle cannot
connect two alternating terminal pairs.  Therefore no two distinct blocks
have vertex-disjoint connected supports.

Conversely, each block has an order-four support: the four-vertex cycle arcs
from `u0` to `u3`, from `u1` to `u4`, and from `u2` to `u5` support `A`, `B`,
and `D`, respectively.  Direct enumeration of every nonempty connected
subset of the cycle confirms both

\[
\kappa_P(\Pi)=1
\]

and minimum support order four.  Thus a maximum-coverage support system has
one represented block, and its minimum possible total order is four.

## 3. Colouring and obstruction path

Every displayed edge has differently coloured ends, so the assignment is a
proper six-colouring.  On the boundary, the colours `1` and `2` induce
exactly the two components `{1,2}` and `{3,4}`.  The path

```text
2-u0-s-u5-u4-4
```

is an alternating `1,2` path joining those components, and all four internal
vertices lie on the open side.

Its internal vertex set has boundary neighbourhood exactly `{2,4,5,6}`.
It therefore supports none of `A`, `B`, or `D`.  Exhaustive enumeration of
connected supersets gives minimum orders five, five, and six for supersets
supporting `A`, `B`, and `D`, respectively.  The path consequently neither
adds a second represented block to the fixed-partition system nor gives an
order smaller than the global minimum four.

The attempted interchange on the boundary component `{1,2}` changes the
boundary equality partition to

\[
\{1,3\}\mid\{2,4\}\mid D\mid\{6\},
\]

which is proper and differs from the original partition.  The source does
not claim that this is a legal Kempe switch in the whole displayed graph:
the obstruction path is precisely what joins the two boundary components
inside the full two-colour subgraph.

## 4. Minor exclusion

For the stated elimination order, the successive numbers of later filled
neighbours are

```text
2 3 4 4 3 3 4 4 4 4 3 2 1 0.
```

It is therefore a valid width-four elimination certificate.  Hence the
displayed graph has treewidth at most four.  Since treewidth is
minor-monotone and `tw(K_7)=6`, the graph has no `K_7` minor.

## 5. Verifier coverage and trust boundary

The deterministic verifier checks the vertex and edge counts, proper
six-colouring, the two boundary two-colour components, the obstruction path,
all connected open-side subsets, the support minima and disjoint-support
obstruction, the path-interior contacts and extension orders, and the
elimination width.

It does not separately assert that the cycle is induced and boundary-full,
that the displayed partition is proper, that `U` is maximum, that the three
required sets equal their blocks, that the block unions are pairwise
adjacent, or that the changed boundary partition is proper.  All these facts
follow directly from the encoded constants and were checked independently
above; these are verifier-coverage limitations, not mathematical gaps.

The example refutes only the fixed-partition augmentation inference stated
in the source.  It is neither seven-connected nor contraction-critical and
has no opposite shore, operation-coupled response, or inherited branch-set
labels.  It is therefore not a counterexample to `HC_7` or to a theorem that
uses those omitted host-level hypotheses.  No mathematical error or scope
overstatement was found.
