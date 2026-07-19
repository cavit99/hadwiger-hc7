# Boundary completion from six almost-full neighbours

**Status:** written proof; separate internal audit GREEN in
[`hc7_six_spoke_boundary_completion_audit.md`](hc7_six_spoke_boundary_completion_audit.md).
This theorem
constructs an explicit `K_7`-minor model from one boundary-full connected
subgraph and six neighbours which each miss at most one boundary vertex.  It
eliminates every wheel-shaped shore in the no-low-degree branch.  It does not
settle the general positive-list-excess core or prove `HC_7`.

## 1. A six-label injection

### Lemma 1.1

Let `D` be a set of six labels and let `r_1,...,r_5` be five objects.  Each
object has either no forbidden label or one forbidden label `m_i in D`.
There is an injection

\[
                         f:\{1,\ldots,5\}\longrightarrow D
\tag{1.1}
\]

such that

1. `f(i) ne m_i` whenever `m_i` exists; and
2. there are no distinct `i,j` for which

   \[
                         f(i)=m_j,\qquad f(j)=m_i.
   \tag{1.2}
   \]

#### Proof

Let `M` be the set of distinct forbidden labels and put `k=|M|`.

If `k<=1`, inject all five objects into the set obtained from `D` by
deleting the one forbidden label when it exists.  If `k=2`, choose one
object from the first forbidden-label class and assign it the second
forbidden label.  Inject the other four objects into `D-M`.  There is no
two-cycle because no object is assigned the first forbidden label.

Assume `k>=3`.  Choose one representative from each forbidden-label
class.  Arrange the `k` distinct labels cyclically and assign to each chosen
representative the next label on that cycle.  Assign the remaining `5-k`
objects injectively into `D-M`, which has order `6-k>=5-k`.  No assignment
uses its object's forbidden label.  A directed cycle of length at least
three has no two-cycle, and the objects assigned outside `M` cannot
participate in (1.2).  This proves the lemma.  \(\square\)

## 2. The completion theorem

### Theorem 2.1

Let

\[
 V(G)=A\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
 \qquad |Y|=7,
 \qquad E_G(A,B)=\varnothing .
\tag{2.1}
\]

Suppose `B` contains a nonempty connected subgraph `P` adjacent to every
literal vertex of `Y`.  Suppose `A` contains distinct vertices

\[
                         h,r_0,r_1,\ldots,r_5
\tag{2.2}
\]

such that

1. `hr_i in E(G)` for `0<=i<=5`;
2. `r_0` has a neighbour in `Y`; and
3. every `r_i` with `1<=i<=5` is adjacent to at least six vertices of
   `Y`.

Then `G` contains a `K_7` minor.

#### Proof

Choose `y_0 in N_Y(r_0)` and put `D=Y-{y_0}`.  Each `r_i`, `1<=i<=5`,
has at most one non-neighbour in `D`.  Apply Lemma 1.1 to these five
vertices and their possible non-neighbours, obtaining an injection
`f:[5]->D`.

Consider the seven sets

\[
 H=\{h,r_0,y_0\},\qquad V(P),\qquad
 Z_i=\{r_i,f(i)\}\quad(1\le i\le5).
\tag{2.3}
\]

They are pairwise disjoint.  The set `H` is connected through the path
`h r_0 y_0`, every `Z_i` is connected by the choice `f(i) ne m_i`, and
`P` is connected by hypothesis.

The set `H` is adjacent to `P` through `y_0`, and to every `Z_i` through
the edge `hr_i`.  The set `P` is adjacent to every `Z_i` through the
literal boundary vertex `f(i)`.  Finally, suppose `Z_i` and `Z_j` were
nonadjacent.  Then both cross-edges `r_i f(j)` and `r_j f(i)` would be
absent.  Since each of `r_i,r_j` has at most one non-neighbour in `D`, this
would give

\[
                         f(j)=m_i,\qquad f(i)=m_j,
\]

contrary to Lemma 1.1.  Thus the seven sets in (2.3) are disjoint connected
pairwise adjacent branch sets of an explicit `K_7`-minor model.  \(\square\)

### Corollary 2.2 (five-neighbour variant)

In (2.1), suppose instead that `A` contains distinct vertices
`h,r_1,...,r_5`, the edges `hr_i`, and a boundary neighbour `y_0 in N_Y(h)`.
If every `r_i` is adjacent to at least six vertices of `Y`, then `G`
contains a `K_7` minor.

#### Proof

Apply Lemma 1.1 on `Y-{y_0}` and replace `H` in (2.3) by `{h,y_0}`.  The
same adjacency check applies.  \(\square\)

## 3. Wheel shores

### Corollary 3.1

Assume (2.1), suppose every vertex of `A` has degree at least nine in `G`,
and suppose `G[A]` is a wheel whose rim has order at least five.  Then `G`
contains a `K_7` minor.

#### Proof

Every rim vertex has three neighbours in `A`, so it has at least six
neighbours in `Y`.  If the rim has order at least six, take the hub as `h`,
reserve one rim vertex as `r_0`, and choose five further rim vertices as
`r_1,...,r_5`.  Theorem 2.1 applies.

If the rim has order five, the hub has five neighbours in `A`.  Its host
degree is at least nine, so it has a neighbour in `Y`.  Corollary 2.2
applies to the five rim vertices.  \(\square\)

The parity of the rim is irrelevant.  In particular this eliminates the
entire odd-wheel family which witnesses unbounded local list-degree excess
when the host degree and opposite boundary-full subgraph hypotheses are
omitted.

## 4. Exact scope

The theorem uses no boundary edges and no colouring-state synchronization.
Its essential host inputs are the connected subgraph on the opposite shore,
its seven literal boundary contacts, and the degree-derived six contacts at
each selected neighbour.  Without the host degree condition, sparse
`K_7`-minor-free wheel interfaces realize the same local list obstruction.

The conclusion does not apply to an arbitrary positive-excess vertex: the
five or six almost-boundary-complete neighbours must be literal and share
the same centre.  The remaining positive-excess theorem must force this
geometry, another explicit minor construction, or a compatible order-seven
separation.
