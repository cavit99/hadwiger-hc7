# Cold audit of the one-split balanced `|W|=4,5` predecessor closure

**Verdict:** GREEN.  The uniform four-link is correctly localized, retaining
each extra `W` endpoint makes it a simultaneous two-packet carrier, and the
seven quotient bags have exactly one possible missing pair.  Splitting one
marked edge repairs that pair with literal predecessor contacts.  All
twenty-one adjacencies and branch-set disjointness checks pass.

Audited source:
[`hc7_marked_three_clique_w45_predecessor_closure.md`](hc7_marked_three_clique_w45_predecessor_closure.md).
Its SHA-256 at audit time is

```text
a8036e262c03ebff2419209bdfaea02e19dc019a5f301ac104755df93ea99e9e
```

The two source interfaces were checked at SHA-256

```text
700e1195f0328d20157497ef0848a89da7520d431932a181995422c35c493e0a  hc7_marked_three_clique_cut_reduction.md
9880cf63240a1e8b5505aee7501ec1ac234523472c612d9f935d1b803cf5da5c  hc7_three_split_minimal_bad_contraction.md
```

## 1. Balanced-cell input

Put `w=|W|` and `m=6-w`.  In either live case `w in {4,5}`:

* `|B_i|=m`, there are `m` large traces, and each trace has order three;
* the symmetric-difference separator has order
  `w+m+3-2r=9-2r`, so an intersection of order at least two contradicts
  six-connectivity;
* consequently each row meets each large trace once;
* secondary cell maximality makes each large cell connected; and
* the source Mader construction puts every row tail in residual singleton
  cells, hence outside the large cells.

For `w=4`, the other large cell supplies a vertex outside the
symmetric-difference shore and separator.  For `w=5`, the incidence claim is
immediate because there is one singleton row and one three-element trace.
The source note does not invoke a nonexistent second large cell there.

The binary marked-cut theorem applies to each

\[
                         S_i=W\cup B_i,\qquad |S_i|=6.
\]

It makes `P_i=A_i-B_i` one connected `S_i`-full component.  The source
separations make the three tails disjoint and anticomplete.

Here are the source dependencies in full.  The Mader certificate partitions
`H-W` into cells `Y_j`, has `X_j subseteq Y_j`, puts every named-clique
vertex of a cell in its trace, and gives

```text
N(Y_j-X_j) subseteq W union Y_j.
```

The auxiliary graph is obtained from `H-W` by deleting every edge internal
to a cell, and `A_i` is a union of its components meeting `L_i-W`.  In the
balanced equality cell the large traces are exactly the `m` three-sets and
the disjoint rows partition their union.  A vertex of `Y_j-X_j` is isolated
in the auxiliary graph and is not a named terminal, so it belongs to no
`A_i`; an `A_i` vertex in `X_j` belongs to `B_i`.  Therefore
`P_i cap Y_j=emptyset` for every large cell, as the decoder requires.

If a large `Y_j` were disconnected, refinement into its graph components
preserves the boundary and terminal axioms, and every old cell-internal
witness edge stays in one refined cell.  For the order-three trace the new
budget contribution is at most

\[
 \sum_C\left\lfloor |X_j\cap C|/2\right\rfloor\le1.
\]

Thus the refinement contradicts the chosen secondary maximum.  No
`X_j`-empty component is hidden: its neighbourhood would lie in `W`, of
order at most five, contrary to six-connectivity.

## 2. Clean row and exact four-link

Let `E=W-{z_1,z_2,z_3}`.  Since `|E|<=2` and the three `K_5` cliques are
disjoint, at most two of them meet `E`; a clean row `h` with
`E` disjoint from `L_h` exists.  Thus

\[
                         Q_h=L_h-z_h\subseteq P_h\cup B_h.
\]

For `{a,b,h}={1,2,3}`, the target

\[
                         T_h=B_h\cup E\cup\{z_a\}
\]

has order

\[
                         (6-w)+(w-3)+1=4.
\]

The graph `H-{z_h,z_b}` is four-connected.  After taking trivial paths at
the common vertices of `Q_h` and `B_h`, set-Menger gives the remaining
paths.  A nontrivial path starts in `P_h`; its surviving row boundary is
exactly `T_h`, so shortening
at its first target localizes every internal vertex in `P_h`.  This checks
both the count and localization.

There are exactly four clique-rooted bags:

* for `w=4`, two augmented cells, the one full extra-target path, and
  `R_a`;
* for `w=5`, one augmented cell, two full extra-target paths, and `R_a`.

Here `R_a` omits its endpoint `z_a`, whereas every extra-target path keeps
its literal endpoint `e in E`.  These bags are disjoint because the four
paths are disjoint, their targets are distinct, the tails avoid the large
cells, and distinct cells are disjoint.  They are pairwise adjacent through
their four distinct roots in the literal clique `Q_h`, and each meets
`{z_h}` through its root.  An extra `e` may belong to `L_a` or `L_b`; this
causes no overlap, because those terminal cliques are not branch bags and
`e in W` lies in neither packet.

## 3. Exhaustive quotient defect check

Append

\[
                         D_a=P_a\cup\{z_a\},\qquad
                         D_b=P_b\cup\{z_b\}.
\]

Both appended bags are connected by fullness at their own marks.  They are
disjoint from one another and from the five core bags: `P_a,P_b,P_h` are
pairwise disjoint, the outside packets avoid every large cell, the retained
extra endpoints lie in `E`, the path to `z_a` omits that endpoint, and
`z_b` was deleted from the linkage host.  Thus all seven quotient bags are
connected and pairwise disjoint before adjacency is considered.

For a count which is uniform in both cases, let

\[
 \mathcal U=\{C_j:1\le j\le m\}\cup\{R_e:e\in E\}.
\]

Since `m+|E|=3`, this is a three-bag family.  The seven quotient bags are
`\mathcal U`, `R_a`, `Z={z_h}`, `D_a`, and `D_b`.  The following table is
an exhaustive partition of their twenty-one unordered pairs.

| Pair class | Count | Literal witness in `H` |
|---|---:|---|
| two bags of `\mathcal U` | 3 | their two distinct roots in `Q_h` |
| `\mathcal U-R_a` | 3 | the two distinct roots in `Q_h` |
| `\mathcal U-Z` | 3 | the root--`z_h` edge in `L_h` |
| `\mathcal U-D_a` | 3 | `P_a-b_{aj}` for `C_j`; `P_a-e` for `R_e` |
| `\mathcal U-D_b` | 3 | `P_b-b_{bj}` for `C_j`; `P_b-e` for `R_e` |
| `R_a-Z` | 1 | the root--`z_h` edge in `L_h` |
| `R_a-D_a` | 1 | the omitted last edge of the path to `z_a` |
| `R_a-D_b` | 1 | **not forced** |
| `Z-D_a` | 1 | `z_h-P_a` fullness |
| `Z-D_b` | 1 | `z_h-P_b` fullness |
| `D_a-D_b` | 1 | `P_a-z_b` fullness |

The first five rows give fifteen pairs and the final six rows give the six
pairs among `R_a,Z,D_a,D_b`.  Thus exactly twenty are forced, and the only
undecided pair really is

\[
                              R_aD_b.                \tag{3.1}
\]

Retaining the extra endpoints is essential: omitting one would create two
additional defects.  The source theorem retains them.

## 4. One split and the literal repair

The predecessor hypothesis has the exact advertised provenance.  In
[`../results/hc7_three_split_minimal_bad_contraction.md`](../results/hc7_three_split_minimal_bad_contraction.md),
let the inclusion-minimal bad set have size three.  For each
`e_a in F`, the proper quotient `G/(F-{e_a})` is seven-connected by
inclusion-minimality; this is exactly the graph called `H_a` here.  The same
result gives six-connectivity of `H` and inclusion of all three contracted
images in every six-cut.  Its vertex-disjoint model supports give the
matching and the three disjoint literal cliques.  Hence no stronger or
unstated predecessor property is being imported.

In the one-edge predecessor `H_a`, replacing `z_a` in each row cut `S_i`
by the two ends `x_a,y_a` produces an actual order-seven separator.
Deleting both ends has exactly the same graph outside the boundary as
deleting `z_a` in `H`, so its two open components are unchanged.
Seven-connectivity makes the cut minimum, hence every boundary vertex is
full to both components.  In particular,

\[
                         x_a,y_a\in N(P_i)
\]

for every row `i`.

Name `x_a` as the endpoint hit by the lifted last edge of `R_a`.  Replace

\[
                         R_a\mapsto R_a+x_a,\qquad
                         D_a\mapsto P_a+y_a.
\]

The replacement bags are disjoint and connected.  The split edge gives
their mutual adjacency, and `x_aP_b` repairs (3.1).  To audit every pair
after the split, keep the same three-bag family `\mathcal U`, put

\[
 R'=R_a\cup\{x_a\},\qquad Z=\{z_h\},\qquad
 A'=P_a\cup\{y_a\},\qquad B'=P_b\cup\{z_b\}.
\]

Indeed, `x_a` and `y_a` are the two new preimages of the removed vertex
`z_a`, so no unchanged bag contains either one; assigning one to each
replacement bag preserves disjointness.  The lifted last edge joins `x_a`
to `R_a`, and expanded-cut fullness joins `y_a` to `P_a`, proving
connectivity of both replacements.  The other five bags are unchanged.

The twenty-one pairs are exhausted as follows.

| Pair class | Count | Literal witness in `H_a` |
|---|---:|---|
| two bags of `\mathcal U` | 3 | their two distinct roots in `Q_h` |
| `\mathcal U-R'` | 3 | the two distinct roots in `Q_h` |
| `\mathcal U-Z` | 3 | the root--`z_h` edge in `L_h` |
| `\mathcal U-A'` | 3 | `P_a-b_{aj}` for `C_j`; `P_a-e` for `R_e` |
| `\mathcal U-B'` | 3 | `P_b-b_{bj}` for `C_j`; `P_b-e` for `R_e` |
| `R'-Z` | 1 | the old root--`z_h` edge |
| `R'-A'` | 1 | the literal split edge `x_ay_a` |
| `R'-B'` | 1 | the expanded-cut contact `x_a-P_b` |
| `Z-A'` | 1 | `z_h-P_a` fullness |
| `Z-B'` | 1 | `z_h-P_b` fullness |
| `A'-B'` | 1 | `P_a-z_b` fullness |

Again the counts are fifteen plus six.  Every witness avoids the removed
quotient vertex `z_a`; in particular `A'` retains all old duties of `D_a`
through `P_a`, while its old `R_a-D_a` duty is replaced by the split edge.
This accounts for all twenty-one pairs.

The fact that an extra vertex `e` might lie in `L_a` is harmless: the
packet contact is the literal edge from `e` to `P_a` supplied by row-cut
fullness, not an appeal to clique membership.

## 5. Scope and the deficient-row probe

The decoder is valid for both remaining balanced equality cells in the
actual minimal-three-edge predecessor branch.  It also specializes to the
already audited `w=3` decoder.

A superficially similar proposed extension to a row of order
`|B_h|=5-w` is **not** obtained merely by asking that its vertices lie in
distinct connected cells.  If such a row had a nonempty separated tail,
then `W union B_h` would be a separator of order five, contradicting
six-connectivity.  Thus the localized tail carrying `Q_h-B_h` is already
absent.  Moreover, even in a different interface supplying a carrier, each
cell used as a branch bag would have to contain contacts for both outside
rows; distinctness of the `B_h` cells alone does not force those two duties
outside the balanced one-per-row incidence matrix.

The theorem does not eliminate an unbalanced Mader outcome and does not
apply to an abstract marked quotient without the seven-connected split
predecessor.
