# Elimination of the concentrated three-owner response component

**Status:** written proof; separate internal audit GREEN in
[`hc7_three_owner_concentration_elimination_audit.md`](hc7_three_owner_concentration_elimination_audit.md).
This note uses the exact hypotheses returned by the audited three-owner
concentration theorem.  It strengthens the connected-transversal argument
used there and eliminates that concentrated order-eight configuration.  It
does not claim that every remaining order-eight interface enters this
configuration, and it does not prove `HC_7`.

## 1. A connected-transversal lemma

### Lemma 1.1

Let `C` be a finite connected graph.  Let `B,A_1,A_2,A_3` be nonempty
subsets of `V(C)`, and suppose

\[
                         |A_i|\ge 2\qquad(1\le i\le3).       \tag{1.1}
\]

There is a nonempty connected set `L proper subset V(C)` such that

1. `C-L` is connected;
2. `C-L` meets `B,A_1,A_2,A_3`; and
3. `L` meets at least one of `A_1,A_2,A_3`.

#### Proof

Choose an inclusion-minimal vertex set `T subseteq V(C)` such that `C[T]`
is connected and `T` meets each of `B,A_1,A_2,A_3`.

We first show that some vertex of `A_1 union A_2 union A_3` lies outside
`T`.  Suppose otherwise.  Then every `A_i` is contained in `T`, and (1.1)
implies `|T|>=2`.  Take a spanning tree of `C[T]`.  Removing a leaf leaves
a connected vertex set.  By the minimality of `T`, each leaf is therefore
the unique member of `T` belonging to at least one of the four prescribed
sets.  No leaf can be the unique member of an `A_i`, since all of `A_i` is
contained in `T` and `|A_i|>=2`.  Hence every leaf would have to be the
unique member of `B cap T`.  A tree has two distinct leaves, and two
distinct vertices cannot both be the unique member of the same nonempty
set `B cap T`.  This is a contradiction.

Choose

\[
                x\in(A_1\cup A_2\cup A_3)-T
\]

and let `L` be the vertex set of the component of `C-T` containing `x`.
Then `L` is nonempty, connected, and meets at least one `A_i`.  Every
component of `C-T` has an edge to `T`, since `C` is connected.  Therefore
the union of `T` with all components of `C-T` other than `L` is connected.
This union is `C-L`, and it contains `T`, so it meets all four prescribed
sets.  Thus `L` has all the asserted properties. \(\square\)

The point of Lemma 1.1 is that it requires only two literal portals for
each owner.  Pairwise intersections between the three portal sets are not
needed.

## 2. Concentrated three-owner setting

Let `G` be seven-connected, seven-chromatic and `K_7`-minor-free, and
assume that every proper minor of `G` is six-colourable.  Suppose `V(G)` is
partitioned into the connected branch sets of a spanning labelled
`K_7`-minus-one-edge model

\[
                 X,Y,D,U,F_1,F_2,F_3,                         \tag{2.1}
\]

whose only possible missing branch-set adjacency is `X-Y`.

Fix the following data.

* There is a selected boundary equality partition and a fixed connected
  response subgraph in `D`.
* A fixed edge joins that response subgraph to the connected retained part
  `U_0` of `U`, and the prescribed root of `U` belongs to `U_0`.
* Among all models preserving the labels, prescribed roots, selected
  partition and response subgraph, the model first maximizes the relaxed
  literal first-hit rank and, subject to that, minimizes `|U|`.
  The ranked label set contains `U`; paths with another terminal label
  avoid all of `U` before their terminal first hit.

Assume that

\[
                         U=U_0\mathbin{\dot\cup}C,             \tag{2.2}
\]

where `U_0` and `C` are nonempty and connected and are adjacent.  Let

\[
                 I=\{R_1,R_2,R_3\}
                 \subseteq\{X,Y,F_1,F_2,F_3\}                 \tag{2.3}
\]

be an inclusion-minimal deficient owner family.  For `1<=i<=3`, put

\[
                         A_i=N_G(R_i)\cap C,
        \qquad            B=N_G(U_0)\cap C.                    \tag{2.4}
\]

Assume the complete concentrated-component conclusions supplied by the
audited concentration theorem:

1. `A_1,A_2,A_3` and `B` are nonempty;
2. every old `U-R_i` contact has its `U`-end in `C`, so the sets `A_i`
   contain all owner portals;
3. every proper subfamily of `I` has a full labelled portal linkage; in
   particular, for each `i!=j` the two paths for the owner pair terminate
   at distinct vertices, one in `A_i` and one in `A_j`;
4. there is a two-vertex set `K subseteq U_0` such that

   \[
        N_G(C)\cap U=K,
        \qquad |N_G(C)|=8;                                   \tag{2.5}
   \]

5. `C` is adjacent to each of the six branch sets different from `U`.
6. `U_0` retains an edge to every branch set outside the owner family
   `I`; in particular, the fixed response edge retains its adjacency to
   `D`.

Conditions 4 and 5 imply the following exact contact count:

\[
 \text{each branch set different from `U` contains exactly one vertex of
 }N_G(C).                                                     \tag{2.6}
\]

Indeed, `K` contributes two vertices of `N_G(C)` inside `U`, while the six
other branch sets contribute at least one each and the total is eight.

## 3. Elimination theorem

### Theorem 3.1

The setting of Section 2 is impossible.  More explicitly, its hypotheses
produce either an explicit `K_7`-minor model or another compatible spanning
labelled `K_7`-minus-one-edge model which preserves all selected response
data and the maximum relaxed first-hit rank but has a strictly smaller
branch set labelled `U`.

#### Proof

### Step 1: some owner has a unique portal in `C`

Suppose first that `|A_i|>=2` for all three owners.  Apply Lemma 1.1 to
`C,B,A_1,A_2,A_3`, and let `L` be the resulting connected set.  Choose an
index `i` for which `L cap A_i` is nonempty, and put

\[
                         U^*=U_0\cup(C-L),
            \qquad      R_i^*=R_i\cup L.                       \tag{3.1}
\]

The set `U^*` is connected: `C-L` is connected and meets `B`, and a vertex
of `B` has an edge to connected `U_0`.  The set `R_i^*` is connected
because `L` meets `A_i`.  Since `C` is connected and `L` and `C-L` are
nonempty, an edge between them gives the required `U^*-R_i^*` adjacency.

For every `j`, the set `C-L` meets `A_j`, so `U^*` remains adjacent to
every owner `R_j`.  Every nonowner adjacency of `U^*` survives through
`U_0`, and the fixed response edge preserves the `D-U^*` adjacency.
Enlarging `R_i` cannot destroy any of its old adjacencies; all pairs not
involving `U` or `R_i` are unchanged.  Thus the seven modified sets are
connected, disjoint, spanning, and retain every required adjacency except
possibly the already permitted missing pair `X-Y`.  If moving `L` repairs
that pair, they form an explicit `K_7`-minor model.  Otherwise they form a
compatible spanning labelled near-complete model with

\[
                            |U^*|<|U|.                         \tag{3.2}
\]

Every prescribed root stays in its old labelled branch set: the root of
`U` is in `U_0`, and no other old branch set loses a vertex.  The selected
boundary partition and fixed connected response subgraph are unchanged,
and the fixed response edge still enters `U_0 subseteq U^*`.

The relaxed first-hit rank does not decrease.  Every ranked path ending in
a label different from `U` avoided all of the old branch set `U`, and
hence avoids `L`; it remains valid after `R_i` is enlarged.  A ranked
`U`-path ending in `U^*` remains unchanged.  If the old `U`-path ended in
`L`, keep its designated response port, join that port inside the fixed
connected response subgraph to the fixed response edge, and use that edge
to enter `U_0`.  As in the audited rank-preservation theorem, overlaps
inside the response subgraph are permitted, while outside it the new tail
has only its terminal in `U_0`, which every other ranked path avoided.
Thus the new model has rank at least the selected maximum and therefore the
same maximum rank.

The `K_7` outcome and the smaller compatible-model outcome both contradict
the hypotheses.  Consequently, after relabelling,

\[
                              A_1=\{s\}                         \tag{3.3}
\]

for some vertex `s in C`.

### Step 2: deleting the unique portal leaves the donor connected

For `j in {2,3}`, the full labelled portal linkage for the proper owner
subfamily `{R_1,R_j}` terminates at two distinct vertices, one in `A_1`
and one in `A_j`.  Since `A_1={s}`, it follows already that

\[
                              A_j-\{s\}\ne\varnothing.          \tag{3.4}
\]

In particular, `C-{s}` is nonempty.

Let `L` be a component of `C-s`.  We claim that `L` has a neighbour in
`K`.  Suppose not.  Componenthood gives

\[
 N_G(L)\subseteq \{s\}\cup
   \bigcup_{R\ne U,R_1}\bigl(N_G(C)\cap R\bigr).                \tag{3.5}
\]

There is no contribution from `U_0`, by (2.5) and the assumption that `L`
misses `K`; there is no contribution from `R_1`, by (3.3); and there are
no edges to other components of `C-s`.  By (2.6), each of the five branch
sets displayed in (3.5) contributes at most one literal vertex.  Hence

\[
                              |N_G(L)|\le6.                       \tag{3.6}
\]

The set `U_0` is nonempty and lies outside `L union N_G(L)`, so (3.6) is a
genuine separation contradicting seven-connectivity.  Thus every component
of `C-s` has an edge to `K subseteq U_0`.

It follows that

\[
                              U^*=U-\{s\}                         \tag{3.7}
\]

is connected: it consists of connected `U_0` together with the components
of `C-s`, each attached to `U_0`.

### Step 3: move the unique portal to its owner

Equation (3.4) says that `U^*` remains adjacent to both `R_2` and `R_3`.

Now replace

\[
                              U\longmapsto U^*=U-\{s\},
            \qquad            R_1\longmapsto R_1^*=R_1\cup\{s\}.
                                                                    \tag{3.8}
\]

The new owner branch set is connected because `s in A_1`.  The new donor
is connected by Step 2.  Since the old connected branch set `U` is the
disjoint union of the two nonempty sets `\{s\}` and `U^*`, an edge between
them supplies the new `R_1^*-U^*` adjacency.  Equation (3.4) preserves the
other two owner adjacencies.  All nonowner adjacencies of `U^*`, including
the fixed `D-U^*` adjacency, survive through `U_0`.  Enlarging `R_1`
preserves all of its old adjacencies, and every other pair is unchanged.

Therefore the two replaced sets in (3.8), together with the five unchanged
branch sets, either form an explicit `K_7`-minor model (if `X-Y` has been
repaired) or another compatible spanning labelled `K_7`-minus-one-edge
model.  The prescribed roots, selected partition, fixed response subgraph and fixed
response edge are preserved for the same reasons as in Step 1.  The
first-hit-rank argument is also identical: only a `U`-path ending at `s`
needs replacement, and the fixed response subgraph followed by its fixed
edge into `U_0` supplies it.  Hence the maximum rank is retained, while

\[
                              |U^*|=|U|-1.                       \tag{3.9}
\]

This contradicts the secondary minimality of `|U|`.  The concentrated
three-owner setting is impossible. \(\square\)

## 4. Consequence and trust boundary

The theorem eliminates the complete concentrated three-owner residue to
which the operation-specific three-edge probes were previously applied.
It does so before regenerating a `K_6` model: the minimum Rado circuit,
the exact order-eight contact count, seven-connectivity and the existing
label-preserving rank normalization already force a strict host-level
descent.

The conclusion is conditional on every item in Section 2.  In particular,
it does not prove that an arbitrary two- or three-component order-eight
interface has a branch-set-contained component, an inclusion-minimal owner
family of order three, the exact contact count (2.5), or a fixed response
edge entering the retained donor.  Those are entry obligations elsewhere
in the active frontier.

## 5. Dependencies

- the audited
  [three-owner concentration theorem](../results/hc7_three_owner_reserved_component_concentration.md),
  for the complete setting in Section 2;
- the audited
  [first-hit rank-preservation theorem](../results/hc7_first_hit_rank_preserving_branch_set_transfer.md),
  for the response-path replacement used in Steps 1 and 3; and
- elementary connectedness and seven-connectivity.
