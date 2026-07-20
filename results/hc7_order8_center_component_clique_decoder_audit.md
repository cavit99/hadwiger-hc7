# Audit of the centre-component clique decoder

**Audited file:** `hc7_order8_center_component_clique_decoder.md`
**Mathematical revision SHA-256:**
`500be975489c25c5060f4397d47ff08a90f656a17dacc8ef9e8878dce14946a5`
**Promoted revision SHA-256:**
`23cf75d1aa0d64866fa2c33e6a53579bbf1d4153d8137d7bbe57d80baf2c5189`
**Audit date:** 2026-07-20
**Verdict:** **GREEN.**  The representative lemma, every branch-set
adjacency in both explicit `K_7` constructions, and all order-eight
corollaries are correct at the audited revision.

The promoted revision differs from the mathematical revision only in its
status line and link to this audit.

## 1. Representative selection

At the `i`th greedy step, the set

\[
                      J_i=\{j<i:x_j\in F_i\}
\]

has order at most one because the previous representatives are distinct
and `|F_i| <= 1`.  If `J_i` is empty, the forbidden set has order at most
`i`.  If `J_i={j}`, then `F_i={x_j}` is already among the previous
representatives, so adding `F_j` still leaves at most `i` forbidden
elements.  Since `i <= m < |N|`, a new representative exists.

Excluding `F_j` precisely when `x_j in F_i` prevents both
`x_j in F_i` and `x_i in F_j`.  Thus the induction proves the claimed
absence of mutual defect pairs.

## 2. The seven branch sets

The number of displayed sets is

\[
                         m+1+1+(5-m)=7.
\]

They are disjoint by construction.  Each `B_i=A_i union {x_i}` is
connected, as is `D union {p}`.  If `B_i,B_j` lacked an edge in one
direction, the absence of a mutual defect supplies it in the other.
The remaining adjacencies are witnessed by:

- an `A_i`--`v` edge for `B_i`--`{v}`;
- `vp` for `{v}`--`D union {p}`;
- the assumed `v`--`Q` edges;
- an edge from `D` to `x_i` for `D union {p}`--`B_i`;
- the fullness of `D` for `D union {p}`--`{q}`;
- the assumed `A_i`--`q` edges for `B_i`--`{q}`; and
- clique edges inside `Q`.

This exhausts every pair and gives the explicit `K_7`-minor model.

For the paired-centre theorem, the representative ground set has order
`k+1`, while the `k` forbidden sets again have order at most one.  Its
seven branch sets are one connected subgraph `H`, the `k` augmented
components, and `6-k` clique singletons.  The hypotheses supply all
`H`--component, `H`--clique and component--clique edges, while the same
representative lemma supplies pairwise component adjacency.

## 3. Eight-separation consequences

Every component `A` of `C-v` is adjacent to `v`, because `C` is connected.
It has no neighbour in another component of `C-v` or in the opposite
component `D`, so

\[
                         N_G(A)\subseteq \{v\}\cup S.
\]

If `A` meets at most six boundary vertices, the other component `D`
witnesses that its neighbourhood is the boundary of a genuine separation
of order at most seven.  Seven-connectivity forces exact order seven.

If no such component exists and `C-v` has at least five components, any
five instantiate Theorem 2.1 with `m=5`, empty `Q`, and the given boundary
neighbour `p` of `v`.  This gives a `K_7` minor.  The clique restriction for
one through four selected components is exactly the contrapositive of the
same theorem with nonempty `Q`.

For two centres joined through a common boundary vertex `p`, every
component after deleting a centre has neighbourhood contained in `S` plus
that centre.  Missing at least two boundary vertices therefore gives an
actual order-seven separation.  Otherwise six selected components satisfy
the paired-centre theorem with connected subgraph `G[{v,p,w}]` and empty
clique `Q`, yielding `K_7`.  Hence the two centre-deleted graphs have at
most five components in total.

## 4. Trust boundary

The theorem does not align a colouring with the selected representatives,
split a remaining connected component, or close the cases in which the
smaller component counts lack the required common-neighbour clique.  It
therefore supplies an unbounded host-level reduction, not a proof of the
full response-coupling theorem or `HC_7`.
