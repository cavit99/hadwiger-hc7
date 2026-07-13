# Independent audit: critical-pinch adhesion state

## Verdict

**GREEN.**  The theorem constructs an equality-partition state on the
literal adhesion and proves that the same state cannot be supplied by an
operation in the opposite open shore.  It does not prove that such a
collision occurs, nor that the five Kempe paths are disjoint or aligned
with the five near-clique rows.

## Checks

1. In every six-colouring of `G-sw`, the endpoints must receive the same
   colour; otherwise restoring `sw` colours `G`.  For every other colour
   `i`, a Kempe interchange in the `{0,i}` component containing `s`
   separates the endpoint colours unless `s,w` are in the same component.
   This proves the five bichromatic paths without any connectivity
   assumption on `G`.
2. The first exit of a path from `W` lies in the literal open
   neighbourhood `S=N(W)`.  If exits for distinct colours coincide, the
   common vertex has a colour in `{0,i} cap {0,j}={0}`.  If the exit is
   `s`, its predecessor is a literal `s-W` neighbour of colour `i`; it
   cannot be the deleted edge `sw`.
3. The restrictions to `C-sw` and `O` agree on `S` as equality
   partitions.  Equality of partitions is sufficient for gluing: the
   bijection between the colours actually used on the boundary extends
   to a permutation of all six colour names.  There are no edges between
   the two open shores, so the aligned colourings give a proper colouring
   of their union `G`.
4. Therefore the state lies in
   `Ext(C-sw,S) cap Ext(O,S)` but not in `Ext(C,S)`.  This conclusion does
   not require all six colours to occur on `S`.
5. A colouring of `G/sw` lifts to a colouring of `G-sw` with `s,w` equal.
   Keeping the original labelled copy of `s` in `S`, the preceding proof
   applies verbatim.  The assertion is about the lifted equality
   partition on the original boundary; it does not require treating the
   contracted vertex as simultaneously belonging to both open shores.
6. A deletion or contraction whose entire support is in
   `V(G)-(W union S)` leaves the induced closed side `C` unchanged.  If a
   colouring after that operation induced the pinch partition on `S`,
   its restriction would put that partition in `Ext(C,S)`, contradicting
   item 4.  Equivalently it glues to the `O` restriction of the pinch-edge
   colouring.  This verifies Corollary 2 for either operation.
7. Under Corollary 3's extra assumptions, no first exit can be `s`, since
   `sw` is deleted and there is no other `s-W` edge.  Since `s` is the
   sole zero-coloured boundary vertex, the five exits have respective
   colours `1,...,5` and are distinct.  On a seven-vertex boundary the
   remaining vertex repeats one nonzero colour, giving exactly one
   doubleton block and five singleton blocks.
8. In the rotation application, `s in Z` is adjacent to the chosen
   `w in W`.  For every new defect label `e`, the whole fixed bag `F_e`
   is anticomplete to `W`, so it is disjoint from `W union N(W)`.  Hence
   the far open shore is genuinely nonempty.  If the ambient graph is
   seven-connected, the resulting actual adhesion additionally has order
   at least seven; this size claim is not needed by Theorem 1 itself.

## Trust boundary

The note correctly stops at a state exclusion.  Neither edge criticality
nor seven-connectivity forces an opposite-shore operation to reproduce
the same partition.  The five paths may intersect and their palette
colours have no proved correspondence with the fixed row labels.  Any
use claiming a labelled carrier, a state collision, or a six-colouring
without separately proving one of those facts is outside this GREEN
audit.
