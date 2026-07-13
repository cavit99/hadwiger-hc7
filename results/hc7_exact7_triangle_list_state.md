# Exact-seven spanning-triangle list-state theorem

## 1. Statement

Let `G` be strongly seven-contraction-critical: `chi(G)=7` and every
proper minor is six-colourable.  Let

\[
                 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
                 \qquad |S|=7,
\]

be a literal separation with no `LR` edges.  Suppose:

1. `R` contains three pairwise vertex-disjoint connected `S`-full
   packets `P_1,P_2,P_3`; and
2. `L` has a spanning partition
   `V(L)=C_1 dotunion C_2 dotunion C_3` into three nonempty connected,
   pairwise adjacent carriers.

For each literal boundary vertex `s`, define its carrier list

\[
              Lambda(s)=\{i in \{1,2,3\}:N_L(s)cap C_i ne emptyset\}.
                                                               \tag{1.1}
\]

### Theorem 1.1 (triangle list-state gluing)

If `G[S]` has a proper list-colouring

\[
                  phi:S longrightarrow \{1,2,3\},
                  \qquad phi(s)in Lambda(s),              \tag{1.2}
\]

then `G` is six-colourable, a contradiction.

Thus, in a hypothetical minimal `HC_7` counterexample, the contact lists
of **every** spanning three-carrier clique partition of the thin shore
form an uncolourable three-palette list assignment on the literal
seven-vertex boundary.

This is a faithful palette-to-labelled-carrier theorem.  It does not
identify colour names with old model bags: both equality states are
created by contractions on opposite open shores and then aligned.

## 2. The carrier-side proper minor

For `i=1,2,3`, put

\[
                         I_i=phi^{-1}(i).                  \tag{2.1}
\]

Each `I_i` is independent because `phi` is proper.  Moreover

\[
                         A_i=C_i union I_i                 \tag{2.2}
\]

is connected: every vertex of `I_i` has a literal neighbour in `C_i` by
(1.2).  The three sets `A_i` are disjoint.  Contract each `A_i` to a
vertex `a_i`.

This is a proper minor.  Indeed the three sets cover the nonempty shore
`L` and all seven boundary vertices, while there are only three of them;
at least one contraction is nontrivial.  By contraction-criticality the
minor has a six-colouring.  The vertices `a_1,a_2,a_3` form a clique,
because the carriers `C_i` are pairwise adjacent, so all nonempty blocks
`I_i` receive different colours when expanded.

Restrict the minor colouring to `R` and expand every `s in I_i` with the
colour of `a_i`.  This gives a proper colouring `c_R` of `G[R union S]`:

* an edge inside one `I_i` does not exist;
* edges between different blocks are proper because the corresponding
  `a_i` are pairwise adjacent; and
* every edge from `s in I_i` to `R` was represented by an edge from
  `a_i` after contraction.

Consequently `c_R` induces exactly the equality partition of `S` into
the nonempty sets among `I_1,I_2,I_3`.

## 3. The packet-side proper minor

For every nonempty block `I_i`, choose a different one of the three
packets and contract

\[
                         D_i=P_i union I_i                 \tag{3.1}
\]

to a vertex `d_i`.  These sets are disjoint and connected by packet
fullness.  At least one is nontrivial, so this is a proper minor and has
a six-colouring.

The vertices `d_i` belonging to nonempty blocks form a clique.  For
`i ne j`, packet `P_i` has a neighbour at every literal vertex of the
nonempty set `I_j`, hence there is a `D_iD_j` edge.  Restrict the minor
colouring to `L` and expand each `I_i` with the colour of `d_i`.  Exactly
as above, this gives a proper colouring `c_L` of `G[L union S]` whose
equality partition on `S` is precisely the same family of nonempty
blocks `I_i`.

No empty block needs a packet.  This avoids any unjustified assertion
that two unanchored packets are adjacent.

## 4. Gluing

The block colours in each of `c_L,c_R` are pairwise distinct.  Permute
the six colour names in `c_R` so that the colours on the at most three
nonempty literal blocks agree with their colours in `c_L`.  The two
colourings now agree on every vertex of `S`.  Since there are no `LR`
edges, they glue to a proper six-colouring of all of `G`.  This proves
Theorem 1.1. `square`

## 5. Entry from the two-lobe rooted-triangle funnel

In the audited exact-seven two-lobe setting, take a `T`-rooted triangle
`(B_1,B_2,B_3)` in one nontrivial lobe `K` and extend it to span
`K union T`.  The other lobe `J` can always be assigned to these three
bags while preserving a triangle and spanning all of `L`; the simplest
choice is

\[
                  C_1=B_1 union J,\qquad C_2=B_2,
                  \qquad C_3=B_3,                         \tag{5.1}
\]

where connectivity of `C_1` uses a literal `Jt_1` edge.  More generally,
the audited other-lobe star split permits many different assignments of
the arms of `J` among the three `B_i`; its core may then be absorbed into
any adjacent carrier.  This changes the lists `Lambda(s)` without changing
the three-carrier clique property.

Seven-connectivity makes the connected shore `L` `S`-full, so every list
in (1.1) is nonempty.  Since `L` contains at least one `S`-full packet and
`R` contains three, the exact-seven packet theorem forces the packing
vector to be `(1,3)` and gives `omega(G[S])<=2`; hence the boundary is
triangle-free.
The live obstruction is now exact:

> Every spanning rooted-triangle assignment of the two lobes produces
> an uncolourable nonempty-subset list assignment from the fixed
> three-colour palette on a triangle-free graph of order seven.

The portal-rank-three closure is the transversal extreme of this theorem;
the list-state theorem additionally closes concentrated contact patterns
whenever their equality classes can be chosen independent.  A surviving
block-terminal web must therefore preserve not only its crossed portal
order but an uncolourable boundary list core under every legal arm/core
exchange.  That is the precise minor-critical state invariant to attack
next.
