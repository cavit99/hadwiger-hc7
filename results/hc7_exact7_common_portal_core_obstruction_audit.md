# Independent audit: common-portal core obstruction

**Verdict:** GREEN.

**Audited source:**
`results/hc7_exact7_common_portal_core_obstruction.md`

**Source SHA-256:**
The mathematical body audited before promotion had SHA-256
`1f89f8c7e473c04503d5e7a2d2b9d1acd636a51a327670d45c16210d523e3de3`.
Promotion changed only the status line and file location; the promoted source
hash is
`2e451605a0dab023b68cddf591ac71551f8c52685a0ee53d04b0c0078ee0338d`.

The audit checks only the stated local hypotheses: a literal separation
`L dotcup S dotcup R`, two disjoint connected `S`-full packets `P,Q` in
`R`, and a literal `P-Q` edge.  It does not infer a `K_7` contradiction
from a `K_7^vee` handoff.

## 1. Definitions and disjointness

For `T subseteq S`, every vertex of `L_T` is literally adjacent to every
member of `T`.  Since `L`, `S`, and `R` are pairwise disjoint, any branch
bags in `L_T`, the packet bags `P union {a}` and `Q union {b}`, and a
singleton `{c}` are mutually vertex-disjoint whenever `a,b,c` are distinct.

The packet bags are connected: `P,Q` are connected and `S`-full, so `a`
has a neighbour in `P` and `b` has a neighbour in `Q`.

## 2. Theorem 2.1

Let `B_1,...,B_4` be the displayed `K_4` model in `L_{a,b,c}`.

* The four `B_i` are connected, disjoint, and pairwise adjacent by the
  definition of a minor model.
* Every `B_i` is adjacent to `P union {a}`, `Q union {b}`, and `{c}`
  through literal edges from its vertices to `a`, `b`, and `c`.
* `P union {a}` and `Q union {b}` are adjacent through the assumed
  literal `P-Q` edge.
* Each packet bag is adjacent to `{c}` because both packets are `S`-full.

Thus all 21 bag pairs are adjacent.  The seven displayed bags are a
literal `K_7` model.  No boundary edge, completion edge, or unproved
packet-to-bag adjacency is used.

## 3. Corollary 2.2

The contrapositive of Theorem 2.1 correctly implies that `L_T` is
`K_4`-minor-free in a `K_7`-minor-free host.

The degeneracy step is valid.  If a finite graph were not two-degenerate,
one of its nonempty subgraphs would have minimum degree at least three.
The standard elementary theorem that every finite graph of minimum degree
at least three contains a `K_4` minor would then put a `K_4` minor in the
original graph.  Hence every `K_4`-minor-free graph is two-degenerate.
This argument applies to disconnected graphs and to every subgraph, as
required by the definition of degeneracy.

## 4. Theorem 3.1

For a `K_4` model `B_1,...,B_4` in `L_{a,b}`, the six bags

`B_1,B_2,B_3,B_4,P union {a},Q union {b}`

form a literal `K_6`: the only adjacency not internal to the `K_4` model
or supplied through the common literals `a,b` is the packet-packet
adjacency, which is exactly the assumed `P-Q` edge.

The singleton `{c}` is adjacent to both packet bags by `S`-fullness and,
by hypothesis, to at least two distinct `B_i`.  It is therefore adjacent
to at least four of the six rim bags.  Consequently at most two bag pairs
are absent, and every absent pair is incident with `{c}`.  After ignoring
any surplus adjacencies, these bags contain precisely the labelled
`K_7^vee` pattern (`K_7` with at most two missing edges having a common
endpoint).  Connectivity and disjointness were already verified above.

Corollary 3.2 is the exact contrapositive under the explicitly stronger
local assumption that the host has no `K_7^vee` minor.  It correctly says
only that a fixed boundary literal meets at most one bag of each fixed
`K_4` model; it does not assert a model-independent owner.

## 5. Scope check

The proofs use no connectivity, colouring state, boundary edge, Dirac
inequality, or planar embedding beyond the hypotheses stated in the note.
The final two-degeneracy and one-bag-trace conclusions are therefore valid
uniform restrictions.  The note also correctly treats `K_7^vee` as a
near-model handoff rather than as closure of `HC_7`.
