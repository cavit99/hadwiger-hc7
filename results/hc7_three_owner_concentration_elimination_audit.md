# Independent audit of the concentrated three-owner elimination

**Verdict:** **GREEN** for the exact source revision

```text
results/hc7_three_owner_concentration_elimination.md
SHA-256 ba23b59ee96c43b98bdb8e6c35e3fe36e5ccf191ff451f6ae4508253e11635e3
```

This is a separate internal mathematical audit, not external peer review.
The audit checked the connected-transversal lemma independently, the exact
order-eight neighbourhood count, the use of seven-connectivity after the
unique owner portal is removed, every branch-set adjacency and prescribed
root, and preservation of the selected response data and relaxed literal
first-hit rank.  No counterexample or unstated connectivity assumption was
found.

After the mathematical audit, one clerical sentence in Step 3 was changed
from an ambiguous count to “the two replaced sets ... together with the
five unchanged branch sets.”  A second independent audit identified this
as the only issue and confirmed that the corrected sentence states the
same seven-set construction checked below.
Promotion changed only the status paragraph and relative audit link; the
mathematical statement and proof are unchanged from the audited revision.

## 1. Imported results and exact scope

The draft imports the following audited sources.

```text
results/hc7_three_owner_reserved_component_concentration.md
SHA-256 d30971fa491a1264101cc949b0712e9b41d87f8879499e529a124403149aea9d

results/hc7_three_owner_reserved_component_concentration_audit.md
SHA-256 8611127861cb4942142e7801592cf794ea3e20079a618240394194209b5c23ba

results/hc7_first_hit_rank_preserving_branch_set_transfer.md
SHA-256 8012e097021736357c2b91445f209c39b69dda58cfc3fa7ed7ddc3695be6290a

results/hc7_first_hit_rank_preserving_branch_set_transfer_audit.md
SHA-256 895509aeff8b3b1c60622140d798753724003900a8ab9cb502f0dcef10ddfff1
```

The first dependency supplies the spanning labelled
`K_7`-minus-one-edge model, the connected retained part `U_0`, the three
owners, the pairwise full portal linkages, the two-vertex internal
transversal, the exact order-eight neighbourhood of `C`, complete
concentration of the owner portals in `C`, and the global extremal choice
of the model.  In particular, the two paths for a proper two-owner
subfamily have distinct terminal vertices in the corresponding two portal
sets; this is the only part of the linkage geometry used in Steps 2 and 3.

The second theorem supplies the response-path replacement used to preserve
the relaxed first-hit rank.  Its applicability here is exact: the ranked
set contains `U` but not the response branch set `D`, the response subgraph
in `D` remains fixed and connected, and its fixed edge enters
`U_0`, which neither transfer changes.

The draft states these imported facts explicitly as hypotheses in Section
2.  The proof is therefore valid even if read as a conditional theorem
independently of the upstream derivation.

## 2. Audit of Lemma 1.1

Let `T` be an inclusion-minimal connected vertex set meeting
`B,A_1,A_2,A_3`.  If all three `A_i` were contained in `T`, then
`|T|>=2`.  For any leaf of a spanning tree of `C[T]`, deleting that leaf
leaves a connected set.  Minimality of `T` therefore makes the leaf the
unique member of `T` in at least one prescribed set.  It cannot be unique
for an `A_i`, because the whole set `A_i` lies in `T` and has order at
least two.  Hence every leaf would have to be the unique member of
`B cap T`, which is impossible for the two distinct leaves of the tree.

Thus some vertex of an `A_i` lies outside `T`.  If `L` is its component in
`C-T`, then `L` is nonempty and connected.  Every component of `C-T` has
an edge to `T`, so `T` together with all the other components is connected;
this set is `C-L`.  It contains `T`, hence meets all four prescribed sets.
Because `T` is nonempty, `L` is a proper subset of `V(C)`.  The proof uses
only `|A_i|>=2`; it requires neither disjointness nor pairwise intersection
conditions on the portal sets.

## 3. Exact boundary count

The two vertices of `K=N_G(C) cap U` account for two members of
`N_G(C)`.  Each of the six other, pairwise disjoint branch sets contains at
least one neighbour of `C`.  Since `|N_G(C)|=8`, equality holds in every
one of these seven contributions: `K` has its stated two vertices and each
outside branch set contains exactly one boundary vertex.  The proof later
uses only the resulting upper bound of one boundary vertex in each outside
branch set; no palette colour is identified with a branch-set label.

## 4. Step 1: the connected transfer

If all three owner portal sets have order at least two, Lemma 1.1 gives a
nonempty connected `L` such that `C-L` is connected, retains a vertex of
`B` and every owner portal set, and `L` meets some `A_i`.

Consequently:

- `U_0 union (C-L)` is connected through the retained `B-U_0` edge;
- `R_i union L` is connected through an `A_i-R_i` edge;
- an edge between the two nonempty sides of connected `C` preserves the
  `U-R_i` model adjacency;
- `C-L` retains all three owner contacts; and
- `U_0` retains every nonowner contact, the prescribed root of `U`, and
  the fixed response edge.

No old branch set other than `U` loses a vertex, so all its prescribed
roots and old adjacencies remain.  The modified sets are disjoint and
spanning.  They either repair the sole permitted missing adjacency and
give an explicit `K_7`-minor model, or give a compatible labelled
near-complete model with a strictly smaller `U`.

For the rank, a path with terminal label other than `U` avoided the whole
old branch set `U` and hence avoids `L`.  A path ending in the retained
part of `U` survives.  A path ending in `L` is replaced from the same
designated port inside the fixed response subgraph and then across the
fixed edge into `U_0`.  Overlap inside the response subgraph is allowed by
the definition of the relaxed rank, and the replacement has only its new
terminal outside that subgraph.  Thus the rank cannot decrease.  Extremal
minimality therefore forces at least one nonempty `A_i` to be a singleton.

## 5. Step 2: connectivity after deleting the singleton portal

Relabel so that `A_1={s}`.  A full linkage for each pair
`{R_1,R_j}`, `j in {2,3}`, has distinct terminal vertices in `A_1` and
`A_j`.  Hence each `A_j` contains a vertex different from `s`, and in
particular `C-s` is nonempty.

Let `L` be a component of `C-s` with no neighbour in `K`.  It has no
neighbour in `U_0`, because all `C-U` boundary vertices are the vertices
of `K`; it has no neighbour in `R_1`, because `A_1={s}`; and it has no
edge to another component of `C-s`.  Its host neighbourhood is therefore
contained in `s` together with the unique boundary vertex in each of the
five outside branch sets other than `R_1`.  Thus `|N_G(L)|<=6`.

The nonempty set `U_0` is disjoint from both `L` and its neighbourhood, so
this is a genuine separation, not merely a small neighbourhood count.
Seven-connectivity gives a contradiction.  Every component of `C-s`
therefore has an edge to `K subseteq U_0`, and their union with connected
`U_0` proves that `U-s` is connected.

## 6. Step 3: the singleton transfer

Move only `s` from `U` to `R_1`.  The enlarged owner is connected through
its defining portal edge.  The reduced donor is connected by Section 5.
Because connected `U` is partitioned into the two nonempty sets `{s}` and
`U-s`, an edge between them preserves their model adjacency.  The vertices
of `A_2-{s}` and `A_3-{s}` preserve the other owner contacts, and `U_0`
preserves every nonowner contact and the fixed response edge.  All other
branch sets, roots and adjacencies are unchanged.

The same response-path replacement proves nondecrease of the relaxed
first-hit rank.  The new `U` has exactly one fewer vertex.  Hence the
resulting model is either an explicit `K_7`-minor model or contradicts the
secondary minimum of `|U|`.  This completes the claimed elimination.

## 7. Trust boundary

The proof is an unbounded, host-level elimination of the **conditional**
concentrated three-owner order-eight configuration stated in Section 2.
It does not prove that every remaining order-eight interface contains such
a component, that every deficient owner family has order three, or that an
arbitrary returned separation has compatible closed-shore colourings.  It
also does not complete the two-owner or other residual response cases and
does not prove `HC_7`.

The theorem depends essentially on all of the following: the exact
eight-vertex neighbourhood, contact with all six outside branch sets,
pairwise full owner linkages, connected `U_0`, the fixed response edge into
`U_0`, and the maximum-rank/minimum-`|U|` choice.  Removing any of these
hypotheses is outside this audit's verdict.
