# Exact-seven pair-list bicycles lift to a literal `K_7`

## 1. Statement

Retain the exact-seven `(1,3)` setting.  Let

\[
                         C_1,C_2,C_3
\]

be a spanning partition of the thin shore `L` into three nonempty connected
pairwise adjacent carriers.  For `s in S`, put

\[
 \Lambda(s)=\{q\in\{1,2,3\}:N_G(s)\cap C_q\ne\varnothing\}. \tag{1.1}
\]

Assume

1. `G[S]` is triangle-free and `|S|=7`;
2. every `Lambda(s)` has order exactly two; and
3. every carrier colour occurs on at least four boundary vertices:

\[
             |\{s:q\in\Lambda(s)\}|\ge4
                       \qquad(q=1,2,3).                  \tag{1.2}
\]

### Theorem 1.1 (pair-bicycle completion)

Either `G[S]` is properly colourable from `Lambda`, or `G` contains a
literal `K_7` minor.

In the strongly contraction-critical setting, the first outcome six-colours
`G` by the audited spanning-triangle list-state theorem.  Hence no
hypothetical exact-seven counterexample admits a raw pair-only carrier state
satisfying (1.2).

The result is a rooted-model principle: the implication bicycle of every
uncolourable pair-list state supplies four literal boundary-rooted clique
carriers.  It is not a palette-to-old-bag identification.

## 2. The literal auxiliary graph

Let `F=G[S]`.  Form `Q` from `F` by adding three vertices `c_1,c_2,c_3`
which induce a triangle, and add the literal incidence edge

\[
                         sc_q
       \quad\Longleftrightarrow\quad q\in\Lambda(s).    \tag{2.1}
\]

An **anchored `K_4`** in `Q` means four disjoint connected pairwise adjacent
bags which together use exactly four vertices of `S`, one in each bag.
Every occurrence of `c_q` in such a bag can be replaced by the whole carrier
`C_q`.  The carriers placed in one bag are connected to one another by their
literal pairwise carrier edges, and the boundary root has a literal neighbour
in at least one of them; all incidences (2.1) are literal.  Thus an anchored
`K_4` in `Q`
lifts to four disjoint connected pairwise adjacent subgraphs of
`G[L union S]`, each containing a different literal boundary vertex.

Anchor the three disjoint `S`-full packets in `R` at the other three
vertices of `S`.  The six pairs among the first four bags are the anchored
`K_4` edges, the twelve mixed pairs are supplied by packet fullness at the
four literal anchors, and the three packet--packet pairs are supplied by
fullness at the other packets' anchors.  These `6+12+3=21` literal
adjacencies give a `K_7` model.

It therefore remains only to find the anchored `K_4`.

## 3. Reduction to five bicycle cores

Use the audited triangle-free three-palette critical-core classification.
An uncolourable pair-list instance contains, after vertex and edge deletion
and list enlargement, one of its ten templates `T1`--`T10`.  At every
vertex displayed with a pair list, the original list is that exact pair:
an original two-set contained in the displayed two-set must be equal to it.
At a displayed full-list vertex, the original list is one of `12,13,23`.

The support bound (1.2) eliminates all but the following possibilities.

* `T1` has order five and every core list is `12`.  The two deleted
  vertices can put colour `3` on at most two additional lists, so colour
  `3` cannot have support four.
* `T3` has order seven and every list is `12`, so it is impossible.
* `T7,T8,T9` use all seven vertices.  Replacing each displayed full list
  by any pair leaves some palette colour with support at most three.  The
  three, three, and nine possible replacements, respectively, are checked
  directly in the audit verifier.
* `T2,T4,T5,T6` already have pair lists and satisfy (1.2).
* `T10` survives for each of the three possible pair replacements of its
  displayed full list at vertex `6`.

The support arithmetic is finite but label-free: it depends only on a
three-colour pair system on at most seven vertices.  The accompanying
verifier independently enumerates every triangle-free seven-vertex graph
and every one of its `3^7` pair-list assignments, rather than assuming this
template reduction.

## 4. Four literal bags in every surviving core

Use the vertex and edge labels from the audited template table, and write
`c_q` for carrier colour `q`.  The following table gives four anchored bags.

| core | four bags in `Q` |
|---|---|
| `T2` | `{0,c_2,c_3}`, `{1,c_1}`, `{2}`, `{3}` |
| `T4` | `{0,c_1}`, `{1,c_2,c_3}`, `{2}`, `{3}` |
| `T5` | `{0,c_1,c_3}`, `{1,c_2}`, `{2}`, `{3}` |
| `T6` | `{0,c_1}`, `{1,c_2,c_3}`, `{2}`, `{3}` |
| `T10` | `{0,c_2,c_3}`, `{1,c_1}`, `{2}`, `{3}` |

For `T10` the same bags work for all three possible original pair lists at
vertex `6`, because vertex `6` is not used.  Each displayed bag is connected:
the carrier vertices in one bag are adjacent, and its boundary root contacts
at least one of them according to the template list.  The six adjacencies
between the four bags follow from the carrier triangle, the template
incidences, and the retained template edges.  Explicitly, the verifier tests
connectivity and all six bag pairs for every row, including all three `T10`
refinements.

Template containment only deletes edges and vertices and enlarges lists.
The four bags above use pair-list vertices, so every carrier incidence used
by a bag is present in the original raw state; every displayed boundary edge
is a retained original edge.  Extra original edges and vertices cannot
destroy the model.  Thus the anchored `K_4` lifts from the core to `Q`, and
Section 2 lifts it literally to `G` and then to `K_7`.  This proves
Theorem 1.1. `square`

## 5. A full raw list also closes literally

The pair-only theorem has a complementary one-line carrier lift.

### Lemma 5.1 (full-list completion)

Suppose `C_1,C_2,C_3` are as in Section 1, every carrier colour has
support at least four, and some `s in S` has

\[
                         \Lambda(s)=\{1,2,3\}.
\]

Then `G` contains a literal `K_7` minor.

#### Proof

The singleton carrier `{s}` is adjacent to all three `C_q`.  After deleting
`s` from their portal sets, each `C_q` still has at least three boundary
representatives available.  Three sets of order at least three have an SDR,
so choose distinct `s_q in S-{s}` with `s_qC_q` literal.  The four bags

\[
                    C_q\cup\{s_q\}\ (q=1,2,3),
                         \qquad\{s\}
\]

are disjoint, connected, and pairwise adjacent.  Anchor the three opposite
full packets at the remaining boundary vertices.  As in Section 2, the
`6+12+3` literal adjacencies give `K_7`. `square`

## 6. Block-chain consequence

In the canonical crossed-chain states of
`hc7_exact7_block_chain_list_exchange.md`, each of the three carrier colours
has literal support at least four.  Therefore every such state in a
hypothetical counterexample has no full raw list by Lemma 5.1, and it cannot
consist entirely of pair lists by Theorem 1.1.  Since every list is nonempty,
**every crossed-chain state has at least one singleton raw list.**  The entire
pair-only implication-bicycle branch and the full-contact branch are closed
by literal minors, rather than left as ordered obstructions.

This conclusion concerns the raw carrier-contact lists.  Singleton
propagation can create pair lists from initially full lists, so the theorem
does not eliminate the propagated bicycles in the general list-core
classification.
