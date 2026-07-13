# Independent audit: adaptive `(1+3)` packet reflection

## Verdict

**GREEN for the exact `(1,3)` application.**

The proposed adaptive argument is valid: in a graph in which every proper
minor is six-colourable, one `S`-full packet on one open shore and three
pairwise disjoint `S`-full packets on the other force either a literal
`K_7` model or two closed-shore colourings with the same exact equality
partition of the literal seven-set `S`.  The colourings then glue.  Hence an
actual exact-seven adhesion with packet vector `(1,3)` cannot occur in a
hypothetical minimal `HC_7` counterexample.

Two qualifications to the stand-alone packet-reflection lemma are now
explicit in the promoted source:

1. at least one block must actually be assigned to a packet, so that the
   operation is a proper minor; and
2. the requested partition must use at most six blocks, or else the clique
   of block representatives is itself a `K_7` obstruction rather than a
   six-colourable reflected state.

When seven block representatives arise, their original packet--block sets
and retained singleton sets are already a literal `K_7` model, so this is
the first outcome of the patched lemma.  Both qualifications also hold
automatically in the colouring application.  The first block is
the independent set `I` of order three or four, so it cannot be one of the
retained singleton representatives; and the partition `Pi` is read from an
actual six-colouring of the first proper minor, so `|Pi|<=6`.

## 1. Frozen hypotheses and packet arithmetic

The argument uses exactly the following data:

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no `LR` edge; every proper minor of `G` is six-colourable; `L`
contains one connected `S`-full packet `Q`; and `R` contains three
pairwise vertex-disjoint connected `S`-full packets `P_1,P_2,P_3`.

If the packet maxima are `(nu_L,nu_R)=(1,3)`, these objects exist by
definition.  No claim that the thin shore has only one connected component,
that a packet spans its shore, or that packets on the same shore are
adjacent is used.  Since `L`, `S`, and `R` are disjoint, `Q` is automatically
disjoint from all three `P_i`; thus the proof really has four disjoint full
packets when it invokes the triangle branch.

## 2. Literal triangle branch

Suppose `H=G[S]` contains a triangle `c_1c_2c_3`.  Let

\[
 S-\{c_1,c_2,c_3\}=\{a_0,a_1,a_2,a_3\}
\]

and put `W_0=Q`, `W_i=P_i` for `1<=i<=3`.  The seven proposed bags are

\[
 W_i\cup\{a_i\}\quad(0\le i\le3),
 \qquad \{c_1\},\{c_2\},\{c_3\}.
\]

They are disjoint, and each packet bag is connected by fullness at its own
anchor.  Packet bag `i` is adjacent to packet bag `j` through a literal
edge from `W_i` to the anchor `a_j`; no packet--packet edge is assumed.
Every packet bag is adjacent to every triangle singleton by fullness, and
the three singleton bags are pairwise adjacent by the literal triangle.
This accounts for

\[
 \binom42+4\cdot3+\binom32=6+12+3=21
\]

literal adjacencies.  The branch is a valid literal `K_7` model.
Consequently the non-`K_7` branch may assume that `H` is triangle-free.

## 3. The first, thin-packet contraction

Since `H` is triangle-free on seven vertices, `alpha(H)>=3`.  Choose an
independent set `I` of order four if `alpha(H)>=4`, and a maximum independent
set `I` of order three otherwise.

The set

\[
                         V(Q)\cup I
\]

is connected: `Q` is connected and every literal vertex of `I` has a
neighbour in `Q`.  Contracting a spanning tree is a legitimate proper minor
operation supported in the closed shore `L union S`.  It is proper because
`I` is nonempty and every member of `I` has a packet edge; in fact the
contracted set has at least four vertices.  The nonempty opposite shore is
untouched.

Let `z` be the contracted image and six-colour the proper minor.  Pull the
colouring back **only** to `G[R union S]`: retain the colours on `R` and
`S-I`, and give every member of `I` the colour of `z`.  This is proper.
There is no edge inside `I`; every edge from `I` to the retained graph became
an edge incident with `z`; and all other retained edges are unchanged.

The block `I` is exact on literal `S`.  For every `s in S-I`, fullness gives
an edge from `Q` to `s`, which becomes `zs`; hence `s` cannot have the colour
of `z`.  Let `Pi` be the complete equality partition of `S` returned by this
colouring.  Since it comes from a six-colouring,

\[
                              |Pi|\le6.                 \tag{3.1}
\]

No colour is identified with a portal, gate, lobe, or pre-existing model
bag.

## 4. Exact packet reflection

Let `Pi={B_1,...,B_k}` be any partition of `S` into independent blocks.
Let `U` be a clique in `H` consisting only of vertices whose blocks in `Pi`
are singletons.  Assign every block not represented by a vertex of `U` to a
different full packet.  If their number is `m<=q`, put

\[
                         Z_i=V(P_i)\cup B_i
                         \qquad(1\le i\le m).
\]

The `Z_i` are disjoint and connected.  After contracting each to `z_i`, the
set

\[
                         \{z_1,...,z_m\}\cup U          \tag{4.1}
\]

is a literal clique with one representative for every block of `Pi`:

* `z_i z_j` is witnessed by an edge from `P_i` to a literal vertex of
  `B_j`;
* `z_i u` is witnessed by fullness of `P_i` at `u`; and
* the vertices of `U` form a clique by choice.

In the application, the non-singleton block `I` is assigned to a packet, so
at least one contraction occurs and the minor is proper.  By (3.1), (4.1)
has order at most six.  A six-colouring of the minor therefore gives all
block representatives distinct colours.

Pull this colouring back only to the opposite closed shore `G[L union S]`.
For a contracted block `B_i`, give its literal vertices the colour of `z_i`;
retain each `u in U` and all of `L`.  The pullback is proper edge by edge:

* each `B_i` is independent;
* a `B_i`--`L` edge became a `z_i`--`L` edge;
* an edge between different blocks has endpoints represented by distinct
  members of the clique (4.1); and
* edges involving retained singleton blocks are covered by the same
  `z_i u` adjacency.

Thus the equality partition on the literal vertices is exactly `Pi`.  No
packet is expanded and no colouring is lifted onto the shore in which its
contraction occurred.  This rules out the suspected same-side lifting error.

Equivalently, if `sing(Pi)` denotes the singleton-block vertices and

\[
 d_H(Pi)=|Pi|-\omega(H[sing(Pi)]),
\]

then `q` packets reflect `Pi` whenever `d_H(Pi)<=q`, subject to the harmless
properness qualification above.

## 5. Audit of the `alpha=4` and `alpha=3` demands

The complete arithmetic is:

| independent block | possible `k=|Pi|` | retained singleton clique | packets required |
|---|---:|---:|---:|
| `|I|=4` | `k<=3` | none | `k<=3` |
| `|I|=4` | `k=4` | any one of the three outside singletons | `3` |
| `|I|=3=alpha(H)` | `k<=3` | none | `k<=3` |
| `|I|=3=alpha(H)` | `k=4` | one of the two singleton outside blocks | `3` |
| `|I|=3=alpha(H)` | `k=5` | an adjacent pair among the four outside singletons | `3` |

For `|I|=4`, `k<=1+|S-I|=4`; if equality holds, all three outside
vertices are singleton blocks.  For `|I|=3`, `k<=5`.  At `k=4`, the four
outside vertices have block-size pattern `2,1,1`.  At `k=5`, all four are
singletons.  They cannot be independent, since `alpha(H)=3`, so two form a
literal edge and may be retained as the two-vertex clique `U`.  Every row
requires at most three packets.  There is no omitted `k=6` case because the
fixed block `I` already has order at least three.

As an independent finite check, I enumerated all 107 unlabelled
triangle-free graphs on seven vertices, all 877 set partitions of the
literal seven-set, every eligible independent `I` of order four (when
`alpha>=4`) or maximum order three, and every proper partition containing
`I` as a block.  There were 2,285 eligible `(H,I,Pi)` states.  Their packet
demands were distributed as 1,720 states of demand two and 565 states of
demand three; none had demand greater than three.  This agrees with the
case arithmetic and found no omitted partition type.

## 6. Gluing and exactness

The thin-side contraction gives a proper colouring of `G[R union S]`; the
three-packet reflection gives a proper colouring of `G[L union S]`.  Both
induce the same partition `Pi` on the same literal vertices.  Exactness makes
the block-to-colour maps injective, so their correspondence extends to a
permutation of the six colour names.  After applying it on one side the
colourings agree vertexwise on `S`.  They glue because there is no `LR`
edge.

This proves the claimed six-colouring in the triangle-free branch.

## 7. Counterexample search and trust boundary

I tried to break the proof at the only plausible interfaces:

1. **Packets on the same shore need not be adjacent.**  Every alleged
   adjacency instead uses a packet-to-literal-anchor edge; the constructions
   remain valid.
2. **A boundary contraction cannot be expanded on its own shore.**  The
   proof never does so.  Each contraction is pulled back only after deleting
   its packet shore from the colouring under consideration.
3. **Different blocks might accidentally share a colour.**  The literal
   clique (4.1) prevents this.
4. **A vertex outside `I` might share the forced colour.**  The first packet
   is full at that literal vertex, creating the edge `zs`.
5. **The reflected minor might not be proper.**  The non-singleton block
   `I` is necessarily among the packet-contracted blocks.
6. **The packet demand might be four.**  The five possible returned-state
   cases in Section 5 exhaust the integer partitions of the complement of
   `I`; the maximum demand is exactly three.

No counterexample or hidden lifting error survives these checks.  The proof
does not use the lobe, gate, portal-rank, or matching hypotheses.  It should
not be generalized without further work to packet vectors `(1,1)` or
`(1,2)`, where the reflected demand can exceed the available packets.

## 8. Exact promoted consequence

Under the exact packet-vector assumptions

\[
                         (\nu_L,\nu_R)=(1,3),
\]

choose one packet from `L` and three disjoint packets from `R`.  The audited
dichotomy gives a literal `K_7` if `G[S]` contains a triangle and a global
six-colouring otherwise.  Both contradict the defining properties of a
hypothetical minimal `HC_7` counterexample.  Therefore the entire `(1,3)`
actual exact-seven adhesion cell is eliminated.
