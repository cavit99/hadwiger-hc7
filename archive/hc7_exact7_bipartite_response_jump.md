# A coupled boundary-state jump from a bipartite shore

**Status:** written proof; unaudited active result.  Section 3 is the
exact-seven specialization of the already audited bilateral full-palette
and two-block state-jump theorems; the new content here is the
size-sensitive boundary classification and the explicit crossed-contact
`K_7` decoder in Section 4.  This note does not prove that the conditional
defect-one argument always reaches this exit, and it does not prove `HC_7`.

## 1. Setup and boundary notation

Let `G` satisfy

\[
  \chi(G)=7,
  \qquad\text{and every proper minor of }G\text{ is six-colourable}.
\]

Assume that

\[
  V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
  \qquad |S|=7,
\]

is an actual separation with nonempty open shores, and that `G[A]` is
connected.  Seven-connectivity implies that every component of `G-S` is
adjacent to every vertex of `S`; in particular

\[
                         N_G(A)=S.                    \tag{1.1}
\]

Assume that

\[
                         G[S]\cong K_2\vee C_5.       \tag{1.2}
\]

Write the adjacent universal vertices as `p,q`.  Label the cycle vertices
cyclically as `v_0,...,v_4`, but index the five nonedges on them as
`e_0,...,e_4` in cyclic order.  There are exactly ten equality partitions
of `S` induced by proper colourings with at most six colours:

* `s_i` has the single nonsingleton block `e_i` and has six blocks; and
* `d_i` has the two nonsingleton blocks in the perfect matching of the
  complementary five-cycle after its vertex `v_i` is deleted, and has five
  blocks.

Thus `p,q,v_i` are the three singleton blocks of `d_i`.

Let `Ext_B(S)` denote the equality partitions on `S` induced by proper
six-colourings of `G[B\cup S]`.

## 2. The size-sensitive compulsory response

### Theorem 2.1

The following conclusions hold.

1. If `A={a}`, then every six-colouring of `G-a` induces one of the
   six-block states `s_i` on `S`.
2. If `A={x,y}` and `xy` is its edge, then every six-colouring of `G-xy`
   induces one of the five-block states `d_i` on `S`.  In the corresponding
   state, each of `x,y` is adjacent to `p,q,v_i` and to at least one endpoint
   of each of the two double blocks.
3. Suppose that `|A|>=2` and `G[A]` is bipartite.  Every six-colouring of
   the proper minor `G/A` induces one of the states `d_i` on `S`.

#### Proof

If `A={a}`, then (1.1) gives `N_G(a)=S`.  In every six-colouring of
`G-a`, every one of the six colours occurs on `S`; otherwise the missing
colour can be assigned to `a`.  A proper partition of seven vertices using
six colours has exactly one double block.  The only possible double blocks
of `K_2\vee C_5` are the five nonedges among the cycle vertices.  This is
exactly a state `s_i`.

Suppose next that `A={x,y}`.  In every six-colouring `c` of `G-xy`, one
has `c(x)=c(y)=alpha`, since otherwise the deleted edge can be restored.
For every colour `beta!=alpha`, each endpoint has a neighbour of colour
`beta`: if, say, `x` did not, recolour `x` with `beta` and restore `xy`.
Every vertex of `S=N_G({x,y})` is adjacent to at least one of `x,y`, so
colour `alpha` is absent from `S`; the preceding saturation shows that all
other five colours occur there.  Since the independence number of
`K_2\vee C_5` is two, the seven boundary vertices split into two double
blocks and three singleton blocks.  This is a state `d_i`.  Endpoint
saturation gives the asserted literal contacts to every colour block; a
singleton block has its unique literal vertex as the contact.

Finally suppose `G[A]` is bipartite and nontrivial.  Contract `A` to one
vertex `a^*` and six-colour the proper minor.  Put `alpha=c(a^*)`.  By
(1.1), colour `alpha` is absent from `S`.  If a second colour `beta` were
also absent from `S`, the two bipartition classes of `G[A]` could be
coloured `alpha,beta`, respectively, and combined with `c` on `G-A`.
This would six-colour `G`.  Therefore all five colours other than `alpha`
occur on `S`, and the same independence-number argument gives a state
`d_i`.  \(\square\)

The singleton conclusion sharply distinguishes a true critical host from
the joined-triangulation shadow used elsewhere in the project.  In any
six-colouring of that shadow, deleting a vertex leaves its former colour
absent from its neighbourhood, so the universal singleton conclusion above
fails.

## 3. One total-contraction state forces a different state

### Corollary 3.1 (coupled exact-seven state jump)

Assume `|A|>=3` and `G[A]` is bipartite.  Fix a six-colouring `c` of
`G/A`, and let its boundary state be `d_i` as in Theorem 2.1.  For every
spanning tree `T` of `G[A]`, there is an edge of `T` whose deletion gives a
partition

\[
                         A=A^-\mathbin{\dot\cup}A^+       \tag{3.1}
\]

such that

1. `A^-` and `A^+` are nonempty, connected, and adjacent;
2. each of them has a neighbour of every colour in `c(S)`; hence each is
   adjacent to `p,q,v_i` and to at least one endpoint of each double block
   of `d_i`; and
3. after contracting `A^-` and `A^+` separately, every six-colouring of
   the resulting proper minor induces on `S` a state different from `d_i`.

Consequently `Ext_B(S)` contains the state `d_i` and at least one other
state, obtained from two operations on the same literal shore and the same
tree cut.

#### Proof

Apply the audited bipartite bilateral full-palette theorem to the fixed
colouring `c` and the spanning tree `T`.  It gives (3.1), with both sides
having an outside neighbour of every colour other than `c(a^*)`.  All
outside neighbours of `A` lie in `S`, and these are exactly the five
colours on `S`.  This proves items 1 and 2.

Let `G_2` be obtained by contracting `A^-` and `A^+` separately.  Since
`|A|>=3`, at least one contraction is nontrivial, so `G_2` is a proper
minor and has a six-colouring.  Suppose one such colouring induced `d_i`
on `S`.  Permute its colour names so that it agrees with `c` on every
literal vertex of `S`.  Use this colouring on the two contracted vertices
and `S`, and use `c` on `G-A`.  These assignments splice because `S` is
the full external neighbourhood of `A`.

Under the fixed exterior colouring `c`, item 2 says that each of the two
contracted vertices sees every colour except `alpha=c(a^*)`; hence each is
forced to colour `alpha`.  They are adjacent, a contradiction.  Thus no
six-colouring of `G_2` induces `d_i`.  Restricting any six-colouring of
`G_2` to the untouched closed shore `G[B\cup S]` gives the second member
of `Ext_B(S)`.  \(\square\)

This is stronger than two independently chosen proper-minor responses: the
forbidden equality state is the exact total-contraction state, and the
second operation uses the two connected pieces certified from that same
state.

## 4. Minor exclusion orders the literal contacts

Retain Corollary 3.1.  Delete `v_i` from the boundary cycle and write the
remaining induced path in order as

\[
                         r_1r_2r_3r_4.                 \tag{4.1}
\]

The two double blocks of `d_i` are

\[
                         \{r_1,r_3\},\qquad\{r_2,r_4\}. \tag{4.2}
\]

### Proposition 4.1 (no crossed contact frame)

If `G` has no `K_7` minor, the following crossed pattern is impossible,
up to interchanging `A^-` and `A^+`:

\[
 \begin{aligned}
  A^-&\text{ is adjacent to }r_1,r_4,\\
  A^+&\text{ is adjacent to }r_2,r_3.
 \end{aligned}                                           \tag{4.3}
\]

Because the two sides together are adjacent to every vertex of `S`, the
minimal contact pattern is therefore serial rather than crossed: after
reversal and interchange, `A^-` contacts `r_1,r_2` and `A^+` contacts
`r_3,r_4`.  Additional contacts are allowed, but none may create the
crossed pattern (4.3).

#### Proof

Under (4.3), the five sets

\[
          A^-,\quad A^+,\quad\{v_i\},\quad
          \{r_1,r_2\},\quad\{r_3,r_4\}                  \tag{4.4}
\]

are pairwise disjoint, connected, and pairwise adjacent.  The first two
sets are adjacent by Corollary 3.1.  The two path-edge sets are connected
and adjacent through `r_2r_3`; each is adjacent to `v_i` through one end
of the cycle path.  The contacts in (4.3) make each of `A^-`,`A^+`
adjacent to both path-edge sets, and Corollary 3.1 makes both adjacent to
`v_i`.

Thus (4.4) is a `K_5`-minor model in the graph obtained after omitting
`p,q`.  Adding the singleton branch sets `{p},{q}` gives a `K_7`-minor
model, a contradiction.

For the final assertion, each side meets both pairs in (4.2), and their
union meets all four literal vertices by (1.1).  Choosing one guaranteed
contact from each pair gives either the crossed pattern, or, after the
stated symmetries, the serial pattern.  Extra contacts are harmless unless
they supply the crossed choice already excluded.  \(\square\)

## 5. Exact remaining gap

Theorems 2.1--3.1 use precisely the universal nonextendability absent from
the six-colourable shadow.  They convert it into a label-faithful boundary
transition and, under `K_7`-minor exclusion, into a literal serial order of
the contacts on the four-vertex path (4.1).

They still do not force a common boundary state.  The new state supplied by
the two-block contraction can be a six-block state `s_j` or another
five-block state `d_j`; proper colourings of the small serial quotient
permit both possibilities.  Nor does the serial order bound the number of
literal edges between `A^-` and `A^+`, so it does not by itself yield an
order-seven separator or a smaller valid defect-one configuration.

The irreducible next statement is therefore a host-level **serial-contact
transition theorem**: use the full minor-critical response inside one of
the two serial pieces to force either a crossed contact (and the explicit
minor above), a state in the opposite closed-shore language, or a connected
proper subpiece which retains the complete defect-one labels.  Boundary
partition data and the one total/two-block operation pair do not determine
which of these occurs.

## 6. Dependencies

- [bipartite bilateral full-palette split](../results/hc7_near_k7_bipartite_total_contraction.md)
- [classification of exact seven-vertex boundary states](../barriers/hc7_exact7_pentagonal_dynamic_language_barrier.md)
- [classification of five-chromatic exact-seven boundaries](../results/hc7_exact7_no_rigid_trace.md)
