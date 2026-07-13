# Exact-seven full-packet packing

## 1. Statement

Let `G` be seven-connected, `K_7`-minor-free, and strongly
seven-contraction-critical:

\[
 \chi(G)=7\quad\text{and every proper minor of }G\text{ is
 six-colourable}.                                           \tag{1.1}
\]

Let `(G_1,G_2)` be an actual separation with literal common boundary

\[
 S=V(G_1)\cap V(G_2),\qquad |S|=7,                         \tag{1.2}
\]

and with both open shores `V(G_i)-S` nonempty.  A connected subgraph
`P\subseteq G_i-S` is **`S`-full** if every literal vertex of `S` has a
neighbour in `P`.  Let `nu_i` be the maximum number of pairwise
vertex-disjoint `S`-full packets in open shore `i`.

### Theorem 1 (exact-seven packet theorem)

\[
 \nu_1+\nu_2\le4,\qquad \min\{\nu_1,\nu_2\}=1,             \tag{1.3}
\]

and

\[
 \omega(G[S])\le6-(\nu_1+\nu_2).                          \tag{1.4}
\]

Consequently the only packing vectors, up to interchanging the shores,
are `(1,1)`, `(1,2)`, and `(1,3)`.  In particular every actual
seven-adhesion has one connected open shore containing no two disjoint
`S`-full connected subgraphs.

## 2. Fullness and literal packet lifting

Every component `C` of an open shore satisfies `N_G(C)=S`.  Indeed,
`N_G(C)\subseteq S`; it separates `C` from the nonempty opposite shore,
so seven-connectivity gives `|N_G(C)|\ge7`.  Thus every component is an
`S`-full packet and

\[
                         \nu_1,\nu_2\ge1.                  \tag{2.1}
\]

### Lemma 2 (packet-plus-clique lift)

If `P_1,...,P_r` are disjoint `S`-full packets, from either shore, and
`Q\subseteq S` is a clique of order `7-r`, then `G` has a literal
`K_7` model.

#### Proof

Write `S-Q={x_1,...,x_r}`.  Use

\[
 P_i\cup\{x_i\}\quad(1\le i\le r),\qquad
 \{q\}\quad(q\in Q).                                     \tag{2.2}
\]

The bags are disjoint and connected.  For `i\ne j`, fullness of `P_i`
at `x_j` joins the packet bags; fullness at `q` joins every packet bag to
every singleton; and `Q` joins the singleton bags.  Hence (2.2) is a
`K_7` model. \(\square\)

No adjacency between two packets is assumed in this lemma.

## 3. Packet-funded equality synchronization

Call

\[
 S=I_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}I_m
      \mathbin{\dot\cup}Q                                 \tag{3.1}
\]

**admissible** when `m\ge1`, every `I_j` is independent of order at
least two, and `Q` is a clique, possibly empty.  The intended equality
blocks are the `I_j`; vertices of `Q` are singleton blocks.

### Lemma 3 (opposite packet contractions synchronize a state)

If each open shore contains `m` disjoint `S`-full packets and (3.1) is
admissible, then `G` is six-colourable.

#### Proof

Choose packets `P_1^1,...,P_m^1` in shore 1.  The sets

\[
                         P_j^1\cup I_j                     \tag{3.2}
\]

are disjoint and connected.  Contract all of them.  This is a proper
minor, so it has a six-colouring by (1.1).  If `z_j` is the image of
(3.2), then

\[
                         z_1,...,z_m,Q                     \tag{3.3}
\]

is a clique: packet fullness supplies every adjacency involving a
`z_j`, and `Q` supplies the rest.  Its order is at most six, since

\[
 m+|Q|=7-\sum_j(|I_j|-1)\le7-m\le6.                       \tag{3.4}
\]

Restrict the colouring to the untouched open shore 2 and expand each
literal set `I_j` with the colour of `z_j`.  This properly colours the
closed side `G_2`: `I_j` is independent, and every edge from `I_j` into
the untouched shore was represented at `z_j`.  The clique (3.3) makes
the equality partition on literal `S` exactly (3.1).

Repeat symmetrically with `m` packets in shore 2.  The resulting
colouring of closed side `G_1` induces the same exact partition.  A
permutation of the six colour names aligns the block colours, after which
the two colourings glue because the open shores are anticomplete.  Thus
`G` is six-colourable. \(\square\)

This argument expands only independent boundary blocks; it never expands
a contracted packet.

## 4. The seven-vertex boundary lemma

### Lemma 4

Every triangle-free graph on seven vertices has an admissible partition
with at most two nontrivial independent blocks.

#### Proof

If the graph is bipartite, use its two parts.  A part of order one may be
put in `Q`; an empty part may be discarded; and an independent part of
order at least four may be split if two nontrivial blocks are desired.

Otherwise choose a shortest odd cycle `C`.  It has order five or seven.
If `|C|=7`, no chord is possible: a distance-two chord creates a triangle
and a distance-three chord creates a shorter odd cycle.  Hence the graph
is `C_7`; put one vertex in `Q` and bipartition the remaining `P_6`.

Let now `C=v_0v_1v_2v_3v_4v_0`, with outside vertices `x,y`.  The cycle
is induced, and each of `N_C(x),N_C(y)` is independent on `C`, hence has
order at most two.

If, say, `x` has no neighbour on `C`, then either `y` has a neighbour
`v_i`, in which case delete the clique `Q={y,v_i}`, or neither outside
vertex meets `C`, in which case take `Q={v_i}`.  The remainder is a
four-vertex path together with at most an isolated vertex or one edge, and
has a bipartition whose nonempty classes have order at least two.

Assume both outside vertices meet `C`.  For `v=v_i\in N_C(x)`, delete
the clique `{x,v}`.  The remaining graph is `C-v=P_4` together with `y`.
It is nonbipartite exactly when `y` meets both ends of that path, namely

\[
                       N_C(y)=\{v_{i-1},v_{i+1}\}.          \tag{4.1}
\]

If some `v\in N_C(x)` does not satisfy (4.1), its deletion with `x`
works.  Otherwise distinct cycle vertices have distinct neighbour pairs,
so

\[
 N_C(x)=\{v_i\},\qquad N_C(y)=\{v_{i-1},v_{i+1}\}.         \tag{4.2}
\]

Now delete the clique `{y,v_{i-1}}`.  The remainder is `P_4` with `x`
attached only at the endpoint `v_i`, so it is bipartite with both classes
of order at least two.  The two bipartition classes and the deleted clique
give the required admissible partition. \(\square\)

The argument is unchanged if the two outside vertices are adjacent.  In
the no-neighbour branch their surviving edge is bipartite; in every branch
where both meet `C`, the displayed clique deletion removes at least one of
them.

## 5. Proof of Theorem 1

Put `r=nu_1+nu_2`.  If `r\ge7`, seven packets anchored at the seven
vertices of `S` give `K_7`.  If `r=6`, use any singleton boundary clique
in Lemma 2.  If `r=5` and `G[S]` has an edge, use that edge as the
two-vertex clique in Lemma 2.  If instead `S` is independent, the
one-block partition `I_1=S` and one packet on each shore invoke Lemma 3.
Every case `r\ge5` is impossible, so

\[
                              r\le4.                       \tag{5.1}
\]

If both packet numbers were at least two, (5.1) would force
`nu_1=nu_2=2`.  A triangle in `G[S]`, together with the four packets,
would give `K_7` by Lemma 2.  If the boundary is triangle-free, Lemma 4
and the two packets on each shore invoke Lemma 3.  Both alternatives are
impossible.  Hence one packet number equals one by (2.1).

Finally, if `G[S]` contained a clique of order `7-r`, Lemma 2 applied to
all `r` packets would give `K_7`.  Therefore

\[
                         \omega(G[S])\le6-r,               \tag{5.2}
\]

which completes the proof. \(\square\)

## 6. Exact scope

The theorem strengthens the earlier component inequality `|S|\ge2m`:
it controls internally disjoint full packets inside one connected
component and orients every exact-seven adhesion toward one packet-thin
shore.  It does **not** imply that the thin shore has a one- or two-vertex
transversal, a planar embedding, a common equality state, or an apex pair.
Those require additional portal geometry or proper-minor state exchange.
