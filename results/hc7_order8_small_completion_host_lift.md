# Host lift for a small five-terminal completion

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_small_completion_host_lift_audit.md`](hc7_order8_small_completion_host_lift_audit.md).  This is a
conditional host-level reduction inside the connected order-eight
opposite-response branch.  It removes the small Xie-completion outcome as
an exceptional case, but it does not prove that the resulting separation
has compatible colourings and does not prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G. \tag{1.1}
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |S|=8,                                      \tag{1.2}
\]

where `G[L]` and `G[R]` are connected.  Retain the normalized partition

\[
                         L=E\mathbin{\dot\cup}D       \tag{1.3}
\]

from the ordered two--three allocation reduction: `G[E]` and `G[D]` are
connected and adjacent, and for distinct `d,e in S`,

\[
 N_G(E)\cap S=S-\{e\},
 \qquad
 N_G(D)\cap S=S-\{d\}.                              \tag{1.4}
\]

Put

\[
                         W=N_G(E)\cap D.              \tag{1.5}
\]

The set `W` is nonempty because `E,D` are adjacent.  Let `c` be the fixed
six-colouring of `G[L\cup S]` used in the merged-root response.  Thus

\[
 S=\{d,e\}\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
 \qquad |X|=|Y|=3,                                  \tag{1.6}
\]

and `c` induces the exact equality partition

\[
                         X\mid Y\mid\{d,e\}           \tag{1.7}
\]

on `S`.  Let `pi` denote the equality partition induced by `c` on any
boundary under discussion.

The intended application is the unresolved Xie completion on
`G[E\cup\{x_e\}]` when that graph has order at most six, equivalently
`|E|<=5`.  The theorem below does not need that size bound.

## 2. Exact host boundary

### Theorem 2.1 (small-completion host lift)

With

\[
                         B=N_G(E),                    \tag{2.1}
\]

one has the disjoint equality

\[
                         B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |B|=7+|W|.                                  \tag{2.2}
\]

Consequently at least one of the following holds.

1. `G` has an actual separation of order seven.
2. `|W|=1`, and the small-boundary lobe theorem gives a strict
   boundary-full order-eight descent with open side `E`.
3. `|W|>=2`; hence `|B|>=9`, and `E` is a connected side with **positive
   boundary excess** consisting of all seven permitted literal vertices
   of `S` together with at least two literal vertices of `D`.

In alternatives 1 and 2, no compatibility of the two closed-shore
colourings is asserted.

#### Proof

There is no edge from `E subseteq L` to `R`.  Equation (1.4) gives all
neighbours of `E` in `S`, and (1.3) says that every remaining neighbour
of `E` lies in `D`.  This proves (2.2).

The set `E` is a nonempty connected proper subset of the component `L` of
`G-S`; it is proper because `D` is nonempty.  The component `R` of `G-S`
lies outside `E\cup B`, so `B` is an actual separation boundary.

If `|W|=1`, then

\[
 |N_{G[L]}(E)|+|N_G(E)\cap S|=1+7=8.
\]

The audited small-boundary lobe theorem applies.  It gives either an
actual separation of order seven or a strict boundary-full order-eight
descent with open side `E`, which are alternatives 1 and 2.  If
`|W|>=2`, (2.2) gives alternative 3.  These cases exhaust the nonempty set
`W`.  \(\square\)

### Corollary 2.2 (the Xie-completion small-order outcome is not separate)

Assume the selected Xie completion on `G[E\cup\{x_e\}]` has order at most
six.  Then `|E|<=5`, but the same three alternatives of Theorem 2.1 apply.
Thus small completion order does not create a new fourth kind of residue:
it is already a small-boundary descent or a positive-excess connected side.

## 3. Retained operation-specific colouring obstruction

### Proposition 3.1

Let `pi_B` be the equality partition induced by `c` on
`B=(S-\{e\}) dotcup W`.  For every edge `uv` with `u in E` and `v in B`,
every proper six-colouring `c_{uv}` of `G-uv` satisfies

\[
                         c_{uv}(u)=c_{uv}(v),          \tag{3.1}
\]

and the restriction of `c_{uv}` to `G-E` induces on `B` an equality
partition different from `pi_B`.

#### Proof

The graph `G-uv` is a proper minor and is six-colourable by (1.1).  If a
six-colouring assigned different colours to `u,v`, restoring `uv` would
give a six-colouring of `G`, contrary to `chi(G)=7`.  This proves (3.1).

Suppose the restriction of `c_{uv}` to `G-E` induced `pi_B` on `B`.
Permute the six colour names so that it agrees vertexwise on `B` with the
restriction of `c` to `G[E\cup B]`.  These two colourings then glue to a
proper six-colouring of `G`: the inner colouring supplies every edge with
an end in `E`, and the outer colouring supplies every other edge.  This is
again a contradiction.  Hence the two partitions differ. \(\square\)

In the merged-root colouring, the restriction of `pi_B` to the seven
vertices `S-\{e\}` is the explicitly named three-block partition

\[
                     X\mid Y\mid\{d\}.               \tag{3.2}
\]

The colours and equality classes of the vertices in `W` are not fixed by
the quotient notation.

## 4. Exact gain and trust boundary

The small-completion outcome of the ordered two--three allocation theorem
can be deleted from the list of qualitatively distinct residues.  Even
when `|E|<=5`, the literal host sees either

* the existing small-boundary descent; or
* a connected side whose boundary is exactly seven named boundary
  vertices plus at least two vertices in the opposite connected part,
  together with the operation-specific incompatible response in
  Proposition 3.1.

This is stronger than merely recording that a graph on at most six
vertices cannot be six-connected.  It is not a terminal theorem.  Positive
boundary excess is not a well-founded parameter, and neither (2.2) nor
(3.1) assigns palette colours to the labels of `P_0,P_1,A_d,A_e`.  An
order-seven separation returned by the small-boundary theorem remains
structural unless a common complete boundary partition is proved
separately.

## 5. Dependencies

- the normalized connected partition `L=E dotcup D` in the ordered
  two--three allocation reduction;
- the [small-boundary lobe
  descent](../results/hc7_order8_small_boundary_lobe_descent.md); and
- elementary minor-critical edge-colouring and colour-gluing arguments.
