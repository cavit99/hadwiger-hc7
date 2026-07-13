# Independent audit: exact-seven pair-bicycle completion

## Verdict

**GREEN.**  The theorem is correct.  The critical-core reduction exhausts
`T1`--`T10`, the support calculation leaves exactly `T2,T4,T5,T6` and the
three pair refinements of `T10`, every displayed four-bag certificate is a
literal anchored `K_4`, and replacing carrier vertices by the actual
carriers followed by the three-packet lift gives all 21 adjacencies of a
literal `K_7` model.

The exhaustive verifier was rerun successfully and independently covers all
107 triangle-free unlabelled graphs of order seven and every relevant
pair-list assignment.  It printed

```text
VERIFIED
triangle_free_graphs=107
support_ge_4_pair_assignments=112350
uncolourable_assignments=1206
all_uncolourable_assignments_have_anchored_K4=True
template_rows_checked=7
full_list_refinements=T7:0,T8:0,T9:0,T10:3
```

There is one nonfatal verifier-description qualification.  The helper
`verify_template_bags()` invokes the general anchored-`K_4` search on each
template; it proves that each row has *some* anchored `K_4`, but it does not
pin the exact four bags printed in the theorem's table.  Those exact bags are
audited directly in Section 5 below and are all valid.  The main exhaustive
verification and the theorem are unaffected.  If the executable is later
used as a certificate specifically for the displayed table, the table bags
should be encoded explicitly.

## 1. Exhaustive search space

`networkx.graph_atlas_g()` contains one representative of every unlabelled
simple graph on at most seven vertices.  The verifier retains precisely the
order-seven graphs for which `nx.triangles()` is identically zero.  The
resulting count 107 agrees with the independent census used in the promoted
triangle-free list-core classification.  Disconnected boundary graphs are
included, as the theorem requires.

For each graph, the loop

```python
product((0b011, 0b101, 0b110), repeat=7)
```

visits all `3^7` assignments of the pair lists `12,13,23`.  There is no
symmetry pruning, so an assignment transported onto an atlas representative
is necessarily visited.

The support filter is exact.  A pair list is equivalently specified by its
one missing colour.  Requiring every colour to occur on at least four lists
means that every missing-colour count is at most three.  The possible count
vectors are permutations of `(3,3,1)` and `(3,2,2)`, so the number of
supported assignments per graph is

\[
 3\frac{7!}{3!3!1!}+3\frac{7!}{3!2!2!}
 =420+630=1050.
\]

Thus the independently expected total is

\[
                       107\cdot1050=112350,
\]

exactly the number printed by the verifier.

## 2. Colourability and anchored-model search

`colourable()` is an exact finite backtracking search.  It visits every
permitted colour at the selected vertex and rejects only a colour already
used by a coloured neighbour.  The static degree/list ordering affects only
search order.  Acceptance occurs exactly after all seven vertices have been
properly coloured.  Atlas vertices have labels `0,...,6`, so tuple indexing
is correct.

The auxiliary graph tested by `anchored_k4()` has seven boundary vertices
and the three carrier vertices.  Its adjacency predicate is exact:

* distinct carrier vertices are adjacent because the three carriers are
  pairwise adjacent;
* two boundary vertices are adjacent exactly when their edge belongs to
  `G[S]`; and
* a boundary vertex and carrier vertex are adjacent exactly when the
  carrier's colour belongs to that boundary list.

The routine selects each of the `binom(7,4)=35` possible root sets.  For each
of the three carrier vertices it selects one of four bags or leaves it
unused, giving all `5^3` allocations.  This is exhaustive for the definition
in the theorem: each of four bags has exactly one boundary root and may
contain any subset of the three carrier vertices, while a carrier vertex can
belong to at most one disjoint bag.  Breadth-first search under the exact
adjacency predicate checks bag connectivity, and the six bag pairs are each
required to contain an edge.

Consequently the assertion inside the main loop is an exact certificate that
every uncolourable supported pair state has an anchored `K_4`.  The printed
count 1,206 is diagnostic rather than needed for completeness: every state
passing the support filter is visited before the assertion.

## 3. Audit of the `T1`--`T10` reduction

The promoted critical-core theorem says that an uncolourable residual state
contains one of `T1`--`T10` after vertex and edge deletion and list
enlargement.  Since every original list here is a pair, a displayed pair
list is necessarily the same exact original pair.  A displayed `123` list
may arise from any of the three original pairs.

The eliminations and survivors are exhaustive.

* `T1` has five vertices, all with list `12`.  Only the two deleted boundary
  vertices can contain colour `3`, so its original support is at most two.
* `T3` uses all seven vertices with list `12`, so colour `3` has support
  zero.
* `T7` uses all seven vertices.  Its fixed pair lists give colour `3`
  support two; replacing its sole full list by a pair raises this to at most
  three.
* `T8` uses all seven vertices.  Its fixed pair lists give colour `3`
  support two; its sole full-list refinement raises this to at most three.
* `T9` uses all seven vertices.  Colour `3` can occur only in the pair
  refinements of its two full lists, so its support is at most two.
* `T2` has two occurrences of each of `12,13,23`; each palette colour already
  has support four.  Its one deleted vertex is irrelevant to that lower
  bound.
* The fixed pair systems of `T4,T5,T6` have support vectors respectively
  `(4,5,5)`, `(6,4,4)`, and `(5,5,4)`, up to the displayed palette order.
* The first six lists of `T10` again consist of two occurrences of each of
  `12,13,23`, so every colour already has support four.  Every one of the
  three pair refinements at its displayed full-list vertex `6` survives.

The verifier independently enumerates all refinements of every displayed
full list and obtains exactly

```text
T7: 0, T8: 0, T9: 0, T10: 3.
```

No template or pair refinement is omitted.

Template containment is in the correct direction for lifting a model.  Each
displayed core edge is a retained original boundary edge; each displayed
pair incidence used below is an exact original carrier contact.  Deleted
vertices, deleted-to-form-the-core edges, and other extra original edges
cannot destroy an existing minor model.  Graph isomorphisms and palette
permutations merely transport the four bags and permute the three actual
carriers.

## 4. Notation for the explicit certificates

Write `A_0,A_1,A_2,A_3` for the four bags in a table row and retain the
theorem's colour notation `c_1,c_2,c_3`.  A root may contact only one of two
carrier vertices in its own bag.  This is sufficient: the carrier vertices
induce a triangle, so the root-to-one-carrier edge and the carrier--carrier
edge connect the entire bag.  No proof step requires the root to contact
every carrier in its bag.

All boundary edges cited below occur in the corresponding promoted template
edge list.  Every root--carrier edge cited below follows from the exact pair
list printed at that root.

## 5. Every displayed anchored `K_4`

### `T2`

The bags are

\[
 A_0=\{0,c_2,c_3\},\quad A_1=\{1,c_1\},
 \quad A_2=\{2\},\quad A_3=\{3\}.
\]

The first is connected by `0-c_2-c_3`, and the second by `1-c_1`.  The six
bag adjacencies are

| Pair | Witness |
|---|---|
| `A_0A_1` | `c_2c_1` |
| `A_0A_2` | `c_2-2` |
| `A_0A_3` | `c_2-3` |
| `A_1A_2` | retained edge `12` |
| `A_1A_3` | `c_1-3` |
| `A_2A_3` | retained edge `23` |

### `T4`

The bags are

\[
 A_0=\{0,c_1\},\quad A_1=\{1,c_2,c_3\},
 \quad A_2=\{2\},\quad A_3=\{3\}.
\]

They are connected by `0-c_1` and `1-c_3-c_2`.  The six adjacencies are

| Pair | Witness |
|---|---|
| `A_0A_1` | `c_1c_2` |
| `A_0A_2` | `c_1-2` |
| `A_0A_3` | `c_1-3` |
| `A_1A_2` | `c_2-2` |
| `A_1A_3` | `c_3-3` |
| `A_2A_3` | retained edge `23` |

### `T5`

The bags are

\[
 A_0=\{0,c_1,c_3\},\quad A_1=\{1,c_2\},
 \quad A_2=\{2\},\quad A_3=\{3\}.
\]

They are connected by `0-c_1-c_3` and `1-c_2`.  The six adjacencies are

| Pair | Witness |
|---|---|
| `A_0A_1` | `c_1c_2` |
| `A_0A_2` | `c_1-2` |
| `A_0A_3` | `c_3-3` |
| `A_1A_2` | retained edge `12` |
| `A_1A_3` | `c_2-3` |
| `A_2A_3` | retained edge `23` |

### `T6`

The bags are the same sets as for `T4`.  They are connected by
`0-c_1` and `1-c_3-c_2`.  The six adjacencies are

| Pair | Witness |
|---|---|
| `A_0A_1` | `c_1c_2` |
| `A_0A_2` | `c_1-2` |
| `A_0A_3` | `c_1-3` |
| `A_1A_2` | `c_3-2` |
| `A_1A_3` | `c_2-3` |
| `A_2A_3` | retained edge `23` |

### `T10`, all three refinements

The bags are the same sets as for `T2`.  They use only vertices
`0,1,2,3` and carrier vertices.  Their connectivity and six adjacencies have
the same witnesses as in the `T2` row: the retained edges `12,23`, the exact
pair lists at vertices `0,1,2,3`, and the carrier triangle.  Vertex `6` does
not occur in a bag, so replacing its displayed full list by any of
`12,13,23` changes none of the witnesses.  The certificate is therefore
valid for all three `T10` refinements.

In every row the four bags are disjoint and each contains exactly one of the
four distinct literal boundary roots `0,1,2,3`.

## 6. Lifting the auxiliary bags to `G[L\cup S]`

Replace every occurrence of `c_q` by the whole connected carrier `C_q`.
Each carrier occurs in at most one auxiliary bag, so disjointness is
preserved.  The actual carriers are disjoint from `S`, and the four roots
are distinct.

Connectivity lifts edge by edge.  A `c_qc_r` edge becomes a literal edge
between the pairwise adjacent carriers `C_q,C_r`; an `s-c_q` edge means by
definition that literal root `s` has a neighbour in `C_q`.  Boundary-root
edges remain literal edges of `G[S]`.  The same substitutions preserve every
edge between two distinct auxiliary bags.  Hence the result is four disjoint
connected, pairwise adjacent literal subgraphs of `G[L\cup S]`, each carrying
one distinct vertex of `S`.

This argument remains valid when an auxiliary bag contains two carrier
vertices but its root contacts only one: the two actual carriers are adjacent,
so their union with the root is connected.

## 7. Three-packet lift and all 21 adjacencies

Let the four lifted bags have boundary anchors `s_0,s_1,s_2,s_3`, and let
`r_1,r_2,r_3` be the other three literal vertices of `S`.  For the three
pairwise disjoint connected `S`-full packets in `R`, put

\[
                         E_h=P_h\cup\{r_h\}.
\]

The seven bags are disjoint and connected.  Their 21 pairwise adjacencies
are:

| Bag pairs | Count | Literal witness |
|---|---:|---|
| among the four lifted bags | 6 | the anchored-`K_4` edges |
| `E_h` to a lifted bag anchored at `s_l` | 12 | an edge `P_h-s_l`, by `S`-fullness |
| among `E_1,E_2,E_3` | 3 | an edge `P_h-r_l`, by `S`-fullness |

Thus all `6+12+3=21` edges required among seven branch sets are literal.
This proves a `K_7` minor.  No packet--packet edge is assumed without an
anchor, and no carrier colour is identified with a pre-existing model-bag
label.

## 8. Full raw list completion

Lemma 5.1 is **GREEN**.  Let

\[
 P_q=\{x\in S:q\in\Lambda(x)\}\qquad(q=1,2,3).
\]

The hypotheses give `|P_q|>=4` and put the full-list vertex `s` in every
`P_q`.  Hence each set `P_q-\{s\}` has order at least three.  These three
sets have an SDR: a one-member subfamily has union of order at least three,
a two-member subfamily also has union of order at least three (hence at
least two), and the full three-member family has union of order at least
three.  Thus there are distinct

\[
                  s_q\in P_q-\{s\}\qquad(q=1,2,3).
\]

The four proposed bags

\[
          C_1\cup\{s_1\},\quad C_2\cup\{s_2\},
          \quad C_3\cup\{s_3\},\quad\{s\}
\]

are disjoint and connected.  The first three are pairwise adjacent because
the carriers are pairwise adjacent; the singleton bag is adjacent to each
of them because `s` has a literal neighbour in every `C_q`.  They therefore
form four literal clique carriers with four distinct boundary anchors.

Anchor the three disjoint `S`-full packets at the remaining three boundary
vertices.  The final 21 adjacencies are exactly six among the four carriers,
12 from packets to their four anchors, and three among packet bags through
the other packets' anchors.  Packet fullness supplies every one of the last
15 edges.  Hence the construction is a literal `K_7` model.  No boundary
edge inside `G[S]` and no palette-to-model identification is assumed.

Consequently the strengthened block-chain conclusion is valid: since every
raw list is nonempty, a surviving support-at-least-four state can be neither
all pairs nor contain a full list, and therefore must contain a singleton
raw list.

## 9. Exact scope

In a strongly contraction-critical exact-seven cell, the promoted
carrier-list theorem handles the colourable outcome, while the present
literal construction handles every uncolourable raw pair-only state with
support at least four per colour.  Lemma 5.1 also closes every state having
a full raw list.  Therefore a canonical crossed-chain raw state must contain
at least one singleton.

The theorem does not apply after unit propagation merely because all
remaining lists are pairs: propagation may delete boundary vertices, change
the order, and remove colours from lists whose **raw** carrier support was
full.  It supplies no monotonicity of propagated bicycles.  The note states
this limitation correctly.
