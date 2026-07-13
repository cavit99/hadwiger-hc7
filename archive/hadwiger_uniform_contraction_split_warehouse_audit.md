# Adversarial audit: uniform contraction--split warehouse theorem

**Verdict: GREEN AS PATCHED.**  The structural theorem in
`hadwiger_uniform_contraction_split_warehouse.md` is valid under its stated
hypotheses.  It neither assumes that the clique model is spanning nor
proves the missing label-preserving exchange.  Four small repairs were
made during audit: the root-torso alternatives are no longer called
mutually exclusive; the singleton root-bag block convention is explicit;
the least-parameter dependencies are written out; and the multi-branch
sharpness construction now includes its minimality proof.

This is an internal mathematical audit, not external peer review or a
novelty determination.

## 1. Audit matrix

| Item | Verdict | Adversarial check |
|---|---|---|
| Lemma 1.1, rooting at `z` | GREEN | A shortest path from `z` to the old model has no internal vertex in any old bag. Adding it to the first met bag preserves disjointness and every old adjacency. No spanning assumption is used. |
| Theorem 2.1, zero-delete/one-rotate | GREEN | For zero monopoly, `T-X` retains every labelled contact. For a unique monopoly `j`, `C_j union X` is connected because an old `T-C_j` edge has its `T` endpoint in `X`; the `X-(T-X)` edge restores the root--`j` adjacency. Rotation changes an external bag legally and strictly reduces the root bag. |
| Corollary 2.2 | GREEN | Since `z in T-X`, every direct `z-C_i` contact survives; hence a monopolized label is a direct root defect. |
| Theorem 3.1, lobe packing | GREEN | Rooted lobes are descendant vertex sets in the block--cutvertex tree and hence laminar. Minimal lobes are disjoint. For each label, the nonempty set of all root-bag endpoints of its contacts cannot lie in two disjoint lobes. Monopoly sets are therefore disjoint and the `floor(|Delta_z|/2)` count follows. The `|T|=1` case and bridge-block convention are now explicit. |
| Expansion through `G/e` | GREEN | Lifting a spanning tree of `H[T]` and adding `xy` connects all preimages of `z`; every `z-C_i` incidence lifts to an `x-C_i` or `y-C_i` incidence. The unchanged bags avoid both endpoints and remain disjoint. |
| Proposition 4.1 | GREEN | The seven/model-order count is exact: the two connected sides are adjacent by `xy`, see every named old bag by hypothesis, and old bag adjacencies are unchanged. |
| Theorem 4.2, torso ordering | GREEN AS PATCHED | Each off-torso component has exactly one torso attachment, or it would enlarge the block. Prefixes and suffixes of an `st`-order are connected. Non-singleton portal sets give nonempty integer intervals; a common cut is a full split, while empty total intersection yields two ordered owner classes. A singleton outcome can coexist with another outcome, so the former phrase “exactly one” was incorrect; the theorem now states “at least one” with a prioritized proof. |
| Corollary 4.3 and Theorem 4.4 | GREEN | An internal singleton cell is detachable and hence owns at least two labels. For two disjoint owner sets, 2-connectivity plus set-Menger gives two disjoint corridors; for a one-vertex overlap, deleting the common vertex leaves a path between the remaining owners. |
| Theorem 5.1, endpoint/full adhesion | GREEN | If a lobe misses both endpoints, a separator from the connected lobe to the edge exists. Inclusion-minimality makes every separator vertex adjacent to both distinguished components, yielding genuine fullness. Ambient `s`-connectivity gives order at least `s`. No model-union coverage is used. |
| Theorem 6.1, state splicing | GREEN | The contraction is wholly in `Q-Z` and leaves closed `P` literal; warehouse operations are expressly confined to `P-Z` and leave closed `Q` literal. Equal equality partitions permit a palette permutation and exact gluing. Boundary operations are not silently allowed. |
| Lemma 6.2 | GREEN | In a contraction colouring the endpoints share a colour. Absence of another colour at either endpoint permits recolouring that endpoint and restores `xy`, contradicting criticality. |
| Theorem 6.3, trace rank | GREEN | Contracting components of `B-Z` gives a connected terminal/component incidence graph. A spanning tree contributes one unit per terminal edge and `d-1` per degree-`d` component node, totaling exactly `p-1`. Nontrivial carriers lie in distinct components of `B-Z`, so are disjoint. |
| Corollary 6.4 | GREEN | For at most four named disjoint bags covering `Z`, summing `p_i-1` gives `|Z|-q >= |Z|-4`. The note correctly does **not** turn two rank units into two distinct or label-aligned repairs. |
| Section 7, least failing parameter | GREEN AS PATCHED | Proper-minor minimality makes `G` connected and every proper minor `(k-1)`-colourable. A hypothetical `(k-2)`-colouring of `G/e` lifts to `G-e` and one new endpoint colour would `(k-1)`-colour `G`. Thus `chi(G/e)=k-1`; least-parameter `HC_{k-1}` then gives `eta(G/e)=k-1`. These dependencies are now explicit. |
| Section 8, sharpness | GREEN AS PATCHED | One branch can own arbitrarily many labels. Partitioning labels into groups of size at least two and using paths `z-s_j-q_j` realizes `floor(r/2)` minimal lobes. The added proof shows every external model bag must contain exactly one clique vertex, forcing the root to contain both vertices of every branch. The examples intentionally have low connectivity and no criticality claim. |

## 2. Scope checks which survived

### No spanning-model assumption

Every operation is internal to named bags or to an actual ambient
separation.  Unused vertices outside the model union play no role in the
rotation, expansion, torso, or splicing arguments.  The full-adhesion
proof works in the ambient graph and therefore does not confuse an unused
component with a model bag.

### Rooting and contraction are compatible

The model is first rooted at the contracted vertex `z` in `G/e`, then the
minimum is taken over all rooted models.  Expansion replaces only `z` by
`x,y`.  A lobe avoids `z`, so it has the same vertex set before and after
expansion; this justifies applying the lobe charge inside `G`.

### Boundary operations are excluded

The state theorem needs the two minor operations on opposite *open*
shores.  Its definition of `Sigma_K(Z)` requires all nontrivial warehouse
operations to be supported in `P-Z` and to retain closed `Q` literally.
It therefore makes no claim for deleting or contracting a boundary vertex
or boundary edge.  This restriction is essential and correctly retained.

### Trace rank is geometric, not label ownership

The hypercarrier lemma supplies a connected terminal trace and numerical
rank.  A single carrier incident with three boundary vertices contributes
two units; it need not be two carriers.  Nor does the lemma identify those
units with the two monopoly labels of a warehouse.  The source note states
this limitation, preventing the most tempting false conclusion.

## 3. Exact frontier consequence

For a least-parameter counterexample at parameter `k`, expand any edge
contraction from a minimum rooted `K_{k-1}` model.  The audited theorem now
proves, uniformly:

1. every detachable off-root piece owns at least two of the `k-2` external
   clique labels, all of them direct root defects;
2. minimal hanging warehouse lobes have disjoint charges, so there are at
   most `floor((k-2)/2)`;
3. after those lobes are compressed, the root torso is a full split, an
   endpoint/internal pin, or an ordered two-owner corridor;
4. each non-endpoint lobe lies behind a genuine full adhesion of order at
   least the ambient connectivity; and
5. every boundary-faithful warehouse operation state at such an adhesion
   is disjoint from every state of the reference edge contraction.

For `k=7`, this means at most two minimal warehouse lobes, and every
non-endpoint one lies behind a full adhesion of order at least seven.  A
four-bag cover of a six-or-larger adhesion also carries at least two exact
trace-rank units.

This does **not** close `HC_7`.  The remaining theorem must align one of
the root-torso corridors or adhesion trace units with the named monopoly
labels, or force agreement between two opposite proper-minor equality
states.  Neither connectivity alone nor the audited rank count supplies
that dynamic label/state alignment.

## 4. Final disposition

The source is suitable for the high-level ledger as a proved internal
structural package.  Its correct headline is “uniform bounded warehouses
and full-adhesion state incompatibility,” not “contraction bags always
split.”  The precise live object is a label-preserving two-path/state
exchange across at most `floor((k-2)/2)` charged warehouses and the
cutvertex-free root torso.
