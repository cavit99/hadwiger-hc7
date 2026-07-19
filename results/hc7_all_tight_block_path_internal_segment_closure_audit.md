# Independent audit of the all-tight multiblock closure

**Verdict:** GREEN for Theorem 2.1 and its stated application, at the
revision identified below.

**Audited source:**
[`hc7_all_tight_block_path_internal_segment_closure.md`](hc7_all_tight_block_path_internal_segment_closure.md)
at SHA-256

```text
28825bfc646bc0ff805b117c90c1ef4f21eee7332a1af676e249960cbc7dc7ba
```

This is a separate internal mathematical audit, not external peer review.
The result is conditional on the hypotheses in Section 1 and on the
already-audited full-residual defect-two carrier theorem.  It does not
prove `HC_7`, force the all-tight branch, treat positive list-degree
excess, or close the remaining one-block `K_4` and `K_5` cases.

## 1. Exhaustion of block-path shapes

The proof considers every path of at least two blocks:

1. `r>=4`;
2. `r=3` with a nonbridge middle block;
3. `r=2`; and
4. `r=3` with the middle block a bridge.

These cases are disjoint and exhaustive.  The two end lobes

```text
P_1=V(D_1)-{w_1},  P_2=V(D_r)-{w_{r-1}}
```

are nonempty, connected, disjoint, and boundary-full by the stated
hypotheses.  A bridge endblock leaves its noncut endpoint, while deleting
one vertex from a two-connected block leaves a connected graph.

## 2. Long paths and a nonbridge middle block

For `r>=4`, the internal set in (2.2) is nonempty and connected.  The
block-cutvertex path shows that its neighbours in `A` are confined to the
two displayed end articulations.  The same statement holds for a chosen
component of `D_2-{w_1,w_2}` when `r=3` and `D_2` is nonbridge.

In either case the connected set `T` is separated from the nonempty
opposite shore `B` by

```text
N_S(T) together with at most two vertices of A.
```

Seven-connectivity therefore forces `|N_S(T)|>=5`.  The three connected
sets `P_1,P_2,T` are pairwise disjoint; the first two meet all seven
boundary vertices and the third misses at most two.  These are exactly the
same-shore hypotheses of the audited full-residual defect-two carrier
theorem.  The boundary-full connected subgraph in `B` supplies its
opposite-shore hypothesis.  Thus the invocation returns a common exact
boundary partition and a valid six-colouring of `G`.

## 3. Two-block calculation

If the common articulation `w` meets at least five boundary vertices,
`T={w}` gives the same carrier-theorem application.  Otherwise,
all-tightness and minimum degree give

```text
d_A(w)=6-c(w),  d_G(w)>=9,  b(w)<=4.
```

The proof now explicitly justifies `b(w)>0`: if `b(w)=0`, then
`c(w)=0` and `d_G(w)=d_A(w)=6`, a contradiction.  Hence `c(w)>=1`, so
`d_A(w)<=5`; while `b(w)<=4` and `d_G(w)>=9` give `d_A(w)>=5`.
Therefore `d_A(w)=5`.

The two positive block contributions sum to five, so one is at most two.
A contribution of one is a bridge endblock; its leaf has at most one
neighbour in `A` and at most seven in `S`, contradicting degree at least
nine.  A contribution of two is a triangle or odd-cycle block.  Each
noncut vertex in its end lobe has exactly two neighbours in `A`, hence all
seven boundary vertices as neighbours.  There are at least two such
vertices.  Their singleton subgraphs and the opposite boundary-full end
lobe are three disjoint boundary-full connected subgraphs, contradicting
hypothesis 5.  No block type or contribution is omitted.

## 4. Three blocks with a bridge in the middle

For `T={w_1,w_2}`, boundary neighbourhood of order at least five again
invokes the carrier theorem.  If its order is at most four, then each
`b(w_i)<=4`.  The same all-tight calculation gives

```text
d_A(w_i)=5,  c(w_i)=1,  b(w_i)=4.
```

One incident contribution is the middle bridge, so the endblock
contribution is four.  A Gallai block with such a contribution is `K_5`;
an odd-cycle block contributes two.  Thus both endblocks are `K_5`.

For the five vertices of `D_1`, the articulation has four boundary
neighbours and each noncut vertex has at least five.  Hall's condition is
valid: every subfamily of order at most four has union of order at least
four, and the full five-set family contains the boundary neighbourhood of
a noncut vertex, of order at least five.  Hence distinct representatives
`s_v in N_S(v)` exist.

The seven branch sets in (2.14) are valid:

* the five sets `{v,s_v}` are connected, disjoint, and pairwise adjacent
  through the `K_5` on `D_1`;
* the two remaining sets are connected because `P_2` and `R` are
  boundary-full and respectively meet the unused vertices `p` and `q`;
* both remaining sets meet every one of the first five through the
  representative `s_v`;
* the two remaining sets meet one another through, for example, an edge
  from the boundary-full `P_2` to `q` (equivalently from `R` to `p`); and
* all seven branch sets are vertex-disjoint because they use disjoint open
  shores, disjoint end lobes, and a partition of the seven boundary
  vertices into the five representatives and `p,q`.

They therefore form an explicit `K_7`-minor model.

## 5. Application and trust boundary

The application uses the shore-filling density theorem only to enter the
all-tight Gallai-tree path with two boundary-full end lobes.  The residual
classification and packing closure supply the explicit hypotheses that
the boundary lies in the 129-graph residual and that no three disjoint
boundary-full connected subgraphs occur.  Under those hypotheses,
Theorem 2.1 eliminates all paths with at least two blocks.

The exact remaining all-tight shore-filling shapes are therefore the
one-block `K_4` and `K_5` cases already isolated by the density theorem.
This is a conditional closure of an infinite multiblock family.  It does
not establish that every shore-filling obstruction is all-tight, and it
does not supply the sought general inequality
`epsilon(v)+rho(v)<=2` in the positive-excess branch.

## 6. Audited dependency

The full-residual defect-two carrier theorem was used at source SHA-256

```text
7957de3aeb635a9f48e1e1668e34f43abbba15cac270c0f716821b2925af3fd8
```

and verifier SHA-256

```text
20ef45d8235dd6ad12b3688545473cc0bed98b4231945ef0be54c7d13c033a6b
```

Its adjacent audit records a GREEN verdict and the exhaustive output

The dependency differs from the initially checked revision only in its
opening status line and recorded audit link; its theorem statements, proof,
and verifier are unchanged.

```text
boundaries=129
cells=3741
witnesses=3741
failures=0
CERTIFIED full-residual defect-two carrier reflection
```

The present audit checked the host-graph hypotheses at every invocation;
it does not independently re-audit the earlier 129-boundary census or the
shore-filling density theorem in full.
