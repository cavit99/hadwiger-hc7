# Literal decoders for a paired five-root fan

**Status:** active draft; written proof; no separate audit.  This note
isolates two terminal constructions available after the paired five-root
fan at a boundary-full order-eight separation.  It also identifies the
exact residue not supplied by the fan and the three available two-edge
colouring responses.  It does not prove that either terminal construction
must occur and does not prove `HC_7`.

## 1. The paired-fan setting

Let `G` be a graph, let `S` be an eight-vertex set, and let `C,Q` be
distinct components of `G-S`.  Assume that both components are adjacent to
every literal vertex of `S`.

Let

\[
 T=\{t_1,t_2,t_3,t_4,t_5\}\subseteq S
\tag{1.1}
\]

and let `P` be a path in `G[C]`.  Suppose there are five paths
`L_1,...,L_5` such that

1. `L_i` joins `P` to `t_i`;
2. `t_i` is the only vertex of `S` on `L_i`; and
3. the five paths are pairwise vertex-disjoint outside `P`.

Put

\[
 F=P\cup\bigcup_{i=1}^5\bigl(V(L_i)-\{t_i\}\bigr).
\tag{1.2}
\]

Thus `F` is a nonempty connected subgraph of `C`, and `F` has a literal
edge to every `t_i`.

In the order-eight application, the five vertices in `T` have the five
distinct common branch-set labels

\[
                 U,D,F_1,F_2,F_3.
\tag{1.3}
\]

Two of the paths are the independent edges

\[
                 e=a_1t_i,\qquad f=a_2t_j,
\quad a_1,a_2\in V(P),\quad i\ne j.
\tag{1.4}
\]

No colour name is identified with any label in (1.3).

## 2. A clean rooted model is terminal

Choose any vertex `x in S-T`.  Since `C` is connected and adjacent to
`x`, there is a connected subgraph `A_0` of `C` which contains `F` and a
neighbour of `x`.  Put

\[
                            A=A_0\cup\{x\}.
\tag{2.1}
\]

The set `A` is connected and has an edge to `Q`, by boundary-fullness of
`Q` at `x`.

### Theorem 2.1 (clean rooted-`K_5` decoder)

Suppose there are five pairwise disjoint connected subgraphs

\[
                         B_1,\ldots,B_5
\tag{2.2}
\]

such that

1. `t_i in B_i` for every `i`;
2. the `B_i` are pairwise adjacent; and
3. every `B_i` is disjoint from `A union Q`.

Then `G` contains a `K_7` minor.  More precisely,

\[
                         A,\ Q,\ B_1,\ldots,B_5
\tag{2.3}
\]

are seven explicit branch sets of a `K_7`-minor model.

#### Proof

The seven displayed sets are nonempty, connected and pairwise disjoint.
The five sets `B_i` are pairwise adjacent by hypothesis.  For every `i`,
the last edge of `L_i` joins a vertex of `F subseteq A` to
`t_i in B_i`, so `A` is adjacent to `B_i`.  Boundary-fullness of `Q` at
`t_i` gives an edge from `Q` to `B_i`.  Finally `A` and `Q` are adjacent
through `x`: the construction of `A` includes `x`, while `Q` has a
neighbour at `x`.  Hence every two sets in (2.3) are adjacent.  They form
the claimed `K_7`-minor model. \(\square\)

### Corollary 2.2 (the exact rooted-model obstruction)

In a `K_7`-minor-free host, every `T`-rooted `K_5`-minor model meets
`A union Q` outside its five roots.  Equivalently, the inherited unrooted
`K_5` on the five common model labels cannot simply be trimmed to five
rooted branch sets disjoint from the paired-fan subgraph and one opposite
boundary-full component.

#### Proof

A model which avoids `A union Q` outside its roots satisfies Theorem 2.1
and gives a `K_7` minor. \(\square\)

This corollary is a literal rooted-model statement.  The fact that the
five labels in (1.3) form an unrooted `K_5` model does not establish its
hypothesis: a branch set or a branch-set adjacency may use vertices of
`Q`, and removing those vertices need not preserve all five rooted bags
and their ten adjacencies.

## 3. Oppositely placed edge responses glue

The second terminal construction is independent of Theorem 2.1.

Let

\[
               V(G)=L\mathbin{\dot\cup}Y\mathbin{\dot\cup}R
\tag{3.1}
\]

be a separation with no `L-R` edges.  Let `e` and `f` be edges such that

\[
 e\in E(G[L\cup Y])-E(G[Y]),\qquad
 f\in E(G[R\cup Y])-E(G[Y]).
\tag{3.2}
\]

Thus `e` belongs only to the closed `L`-shore and `f` belongs only to the
closed `R`-shore.

Let `c_e` be a proper six-colouring of `G-e` in which `f` is proper, and
let `c_f` be a proper six-colouring of `G-f` in which `e` is proper.  Write
`Pi_e,Pi_f` for their equality partitions on the literal boundary `Y`.

### Theorem 3.1 (opposite-edge partition gluing)

If

\[
                             \Pi_e=\Pi_f,
\tag{3.3}
\]

then `G` is six-colourable.

#### Proof

The restriction of `c_f` to `G[L union Y]` is proper in the intact closed
`L`-shore.  The only edge absent from its host is `f`, and (3.2) puts that
edge outside `G[L union Y]`; the edge `e` is present there and is proper
under `c_f`.  Symmetrically, `c_e` restricts to a proper colouring of the
intact closed `R`-shore.

Equality (3.3) gives a bijection between the colours used by the common
blocks on the two shores.  Extend it to a permutation of the six-colour
palette and apply that permutation to one restriction.  The two
colourings now agree at every literal vertex of `Y`.  Since there are no
`L-R` edges, they glue to a proper six-colouring of `G`. \(\square\)

### Corollary 3.2 (paired critical edges at an order-seven boundary)

Suppose `G` is not six-colourable and every proper minor is
six-colourable.  For the independent edges in (1.4), let `c_e,c_f` be the
standard one-edge responses, with signatures respectively
`(equal,proper)` and `(proper,equal)` in the common deletion
`G-{e,f}`.

If an actual order-seven separation has `a_1,a_2` in opposite open shores,
has `t_i,t_j` on its boundary, and places `e,f` as in (3.2), then the two
response partitions on that boundary are distinct.

#### Proof

If they were equal, Theorem 3.1 would six-colour `G`. \(\square\)

## 4. Why the simultaneous-equality response is not yet terminal

Contraction-criticality also supplies a colouring of `G-{e,f}` with
signature `(equal,equal)`, obtained by expanding a colouring of `G/e/f`.
On a separation satisfying (3.2), that colouring is improper on both
intact closed shores: the monochromatic edge `e` lies in one and the
monochromatic edge `f` lies in the other.  It therefore cannot replace
either of the two one-edge restrictions used in Theorem 3.1.

Likewise, the five paths in Section 1 lie on the `C`-side of the original
order-eight separation.  The one-edge response partitions are proper on
the unchanged opposite closed shore and reject the intact `C`-side.  Thus
the paired fan is on the wrong open shore for direct transported-partition
reflection of either selected response.  A successful use of the
simultaneous-equality response must first create a new transition or a
new separation; its mere existence is not a common boundary colouring.

## 5. Exact irreducible residue

Under `K_7`-minor exclusion and non-six-colourability, the two literal
decoders leave the following simultaneous obstruction.

1. For every opposite boundary-full component `Q`, every choice of
   `x in S-T`, and every connected enlargement `A` in (2.1), no clean
   `T`-rooted `K_5` model avoids `A union Q` outside its roots.
2. Every actual order-seven separation which puts `e` and `f` on opposite
   closed shores gives distinct equality partitions in the two exclusive
   one-edge responses.
3. The simultaneous-equality response is one-sidedly improper on both of
   those intact shores and therefore supplies no third gluing restriction
   without an additional operation-specific transition.

The explicit paired-fan barrier shows that the five paths and the three
positive response signatures are compatible with `K_7`-minor exclusion
when the forbidden fourth signature `(proper,proper)` is allowed.  Hence a
proof beyond this residue must spend the universal prohibition of that
fourth signature to obtain either the clean rooted model, an
opposite-edge separation with equal boundary partitions, or a strict
host-level descent.  Neither the fan nor the opposite full component alone
contains that implication.

## 6. Dependencies and trust boundary

- the paired five-root fan from
  [`hc7_order8_common_label_paired_fan.md`](../results/hc7_order8_common_label_paired_fan.md);
- the standard one-edge and simultaneous-contraction responses for two
  independent critical edges; and
- the explicit
  [paired-fan barrier](../barriers/hc7_common_label_paired_fan_k7_barrier.md).

Theorem 2.1 and Theorem 3.1 are terminal, literal-host constructions.
They use no contracted object as one separator vertex and make no
palette-to-model-label inference.  The note does not prove existence of
the clean rooted model, the oppositely placed order-seven separation, or
the common equality partition.
