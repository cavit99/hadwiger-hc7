# Adaptive three-carrier exchange and the two-component rich shore

**Status:** proved and independently audited after correcting the carrier
connectivity test to require that the missed literal is absent from the
assigned independent block.

## 1. Scope

Use the exact-seven packet setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
 \qquad (\nu_L,\nu_R)=(1,2),
\]

in a 7-connected, strongly 7-contraction-critical, `K_7`-minor-free
graph.  Every component of an open shore is `S`-full.  This note concerns
the ten audited absolute-demand-three boundary orbits left after robust
block reflection and the two-anchor lift.

The result is an infinite-family closure: if the rich shore has two
components, neither component can have a cutvertex.  The finite boundary
calculation only selects the exact contraction witness; it does not bound
or enumerate either exterior component.

## 2. A general three-carrier reflection criterion

Let `Pi` be a proper equality partition of `S`.  Choose a maximum clique
`C` among the literal vertices that are singleton blocks of `Pi`.  Suppose

\[
                             d_H(\Pi)=3,
\]

so exactly three blocks of `Pi` are not represented by the retained
singletons in `C`; call them `B_1,B_2,B_3`.

### Lemma 2.1 (labelled carrier reflection)

Suppose one closed shore contains three pairwise disjoint nonempty
connected subgraphs `T_1,T_2,T_3` and a bijection between these carriers
and `B_1,B_2,B_3` such that, writing `B(T_i)` for the assigned block:

1. `T_i union B(T_i)` is connected for every `i`;
2. for every `i!=j`, the sets
   `T_i union B(T_i)` and `T_j union B(T_j)` are adjacent; and
3. for every `c in C` and every `i`, either `T_i` contacts `c` or some
   vertex of `B(T_i)` is adjacent to `c` in `H=G[S]`.

Then the partition `Pi` can be reflected across that shore.  In the
exact-seven contraction-critical setting, if `Pi` was returned by a
proper contraction on the opposite shore, then `G` is six-colourable.

#### Proof

Contract each connected set

\[
                         T_i\cup B(T_i).
\]

Conditions 2 and 3 say that the three representatives together with the
literal clique `C` form a clique indexed by every block of `Pi`.  The
contraction is proper, hence its graph has a six-colouring.  On the
untouched opposite closed shore, the boundary vertices have equality
partition exactly `Pi`: vertices in one contracted block expand to one
colour, while distinct block representatives are pairwise adjacent.
Permute its palette to align it with the colouring that originally
returned `Pi`, then glue across the literal boundary `S`. `square`

This is the reusable exchange principle.  It separates the palette issue
from the geometry: no carrier is assigned a block until after the actual
proper-minor state has been returned.

## 3. The adaptive finite boundary theorem

For a connected carrier `X`, put `D(X)=S-N_S(X)`.

### Theorem 3.1 (one full plus two adjacent near-full carriers)

Let `H` be one of the ten audited absolute-demand-three boundary orbits.
Let `a,b` be distinct boundary vertices.  There is a nonempty independent
set `I=I(H,a,b)` with the following property.

Every proper equality partition `Pi` containing `I` as an exact block
has demand exactly three and can be reflected by any three disjoint
connected carriers `Q,X,Y` satisfying

\[
 D(Q)=\varnothing,qquad D(X)\subseteq\{a\},qquad
 D(Y)\subseteq\{b\},qquad E(X,Y)\ne\varnothing.          \tag{3.1}
\]

#### Proof

For any returned `Pi`, choose a maximum singleton clique `C` and let
`B_1,B_2,B_3` be the three remaining blocks.  The full carrier `Q` can
fund any one of them.  A carrier missing only `a` can fund a block `B`
provided

* `a notin B`, which makes `X union B` connected (the blocks are
  independent, so a missed literal cannot be connected through another
  member of its own block); and
* if `a in C`, then `a` has a boundary neighbour in `B`, which repairs
  the only possibly missing carrier-to-`C` adjacency.

The symmetric criterion holds for `Y` and `b`.  Once the three blocks are
assigned subject to these two tests, Lemma 2.1 applies: `XY` is an edge,
and the full carrier `Q` is adjacent to each of the other representative
sets through their assigned nonempty boundary blocks.

It remains only to verify that `I` can be selected before `Pi` is known.
The following compact certificate uses graph6 labels in graph-atlas
vertex order.  For the first nine orbits the displayed `I` works for
every ordered pair of distinct defects.

| graph6 | `I` |
|---|---|
| ``FCc`G`` | `012` |
| ``FKc`G`` | `015` |
| ``F`ooo`` | `026` |
| `Feo`G` | `234` |
| `FMs`G` | `015` |
| ``F`NBW`` | `036` |
| `FhMMG` | `135` |
| `FlBHo` | `024` |
| `FBjN_` | `012` |

The authoritative literal graph6 strings are also stored in the verifier.

The tenth orbit is the Moser spindle in the standard labeling

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Take `I={1,5}`, except when `{a,b}={3,4}`, when take `I={0,5}`.

The deterministic verifier

`results/hc7_exact7_three_carrier_state_probe.py`

enumerates all proper partitions of the seven literal vertices, all
maximum singleton cliques, all six assignments of the remaining three
blocks, and every ordered pair of distinct defects.  It checks both
`d_H(Pi)=3` and the two carrier tests above.  Its terminal assertion is

`CERTIFIED adaptive three-carrier exchange`.

Thus every possible returned state has a Lemma 2.1 assignment. `square`

## 4. Geometric consequence

### Corollary 4.1 (rich two-component cutvertex closure)

Suppose `G[R]` has two components.  If either component has a cutvertex,
then `G` is six-colourable.  Consequently every component of a
two-component rich shore in a counterexample is cutvertex-free.

#### Proof

Let `Q` be one rich component and let `K` be the other, with cutvertex
`w`.  Both `Q` and `K` are `S`-full.  Choose a component `D` of `K-w` and
put

\[
                              X=D,qquad Y=K-D.
\]

Both are nonempty and connected, and an edge from `D` to `w` is an `XY`
edge.  Moreover

\[
 N_G(D)\subseteq S\cup\{w\}.
\]

Seven-connectivity gives `|N_S(X)|>=6`.  Apply the same argument to any
other component of `K-w`; it is contained in `Y`, so `|N_S(Y)|>=6`.
Thus `X,Y` are near-full.  Because `X union Y=K` is `S`-full, their
singleton defects, when both exist, are distinct.  If one carrier is
actually full, choose an arbitrary distinct pseudo-defect; the extra
contact only strengthens (3.1).

Select `I=I(H,a,b)` from Theorem 3.1 and contract the thin full packet
together with the literal independent set `I`.  Strong contraction
criticality returns a proper six-colouring whose boundary equality state
contains `I` as an exact block.  Theorem 3.1 reflects that actual state
using `Q,X,Y`, and Lemma 2.1 glues the two shore colourings.  Hence `G` is
six-colourable, contrary to the counterexample hypothesis. `square`

## 5. Exact residue

This closes every two-component rich shore in which one component has a
cutvertex, for all ten absolute-demand-three boundary orbits.  It does
not close:

* singleton or other cutvertex-free rich components;
* the connected rich shore, where two full packets may be interlaced
  across a cutvertex and no disjoint full third carrier is automatic; or
* boundary orbits already outside the audited ten-orbit hard core.

Those qualifications are geometric, not palette-related.  The
palette-to-labelled-carrier step for the three-carrier configuration is
completely discharged by Lemma 2.1 and Theorem 3.1.
