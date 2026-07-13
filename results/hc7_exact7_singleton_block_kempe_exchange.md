# Exact singleton-block Kempe exchange

**Status:** proved and independently audited.

## Lemma

Let `J` be a graph, let `S subseteq V(J)`, and let `c` be a proper
colouring of `J`.  Let `Pi` be the equality partition induced by `c` on
the literal set `S`.  Suppose `{x}` and `{y}` are singleton blocks of `Pi`
and `xy` is not an edge.

Then exactly one of the following operations is available:

1. a Kempe swap produces another proper colouring whose equality partition
   on `S` is obtained from `Pi` by replacing `{x},{y}` with `{x,y}`; or
2. `J` contains an `x-y` path using only the two colours `c(x),c(y)`, and
   every internal vertex of this path lies in `V(J)-S`.

The alternatives need not be logically exclusive as graph properties; the
claim is that the standard two-colour component test always supplies one of
the two stated outputs.

## Proof

Let `K` be the subgraph of `J` induced by the two colour classes
`c^{-1}({c(x),c(y)})`.

If `x` and `y` lie in different components of `K`, interchange the two
colours on the component containing `x`.  A Kempe swap preserves properness.
Because `{x}` and `{y}` are singleton equality blocks on `S`, no vertex of
`S-{x,y}` has either of these two colours.  The swapped component therefore
contains no other boundary vertex.  After the swap, `x` has colour `c(y)`,
`y` retains that colour, and every other equality block on `S` is unchanged.
This is outcome 1.

If `x` and `y` lie in the same component of `K`, take a shortest `x-y` path
in that component.  It uses only the two displayed colours.  Again no vertex
of `S-{x,y}` has either colour, so every internal vertex lies outside `S`.
This is outcome 2.  `square`

## HC7 use and trust boundary

For a closed shore `J=G[R union S]`, outcome 2 is a literal bichromatic
connection whose internal vertices lie in the open shore `R`; it is not an
abstract equality relation.  Outcome 1 merges exactly the two requested
singleton blocks and changes no other boundary block.

The lemma does not make the returned path disjoint from preselected packets,
branch sets, or connectors.  Any packet-escape application must prove that
additional disjointness separately.
