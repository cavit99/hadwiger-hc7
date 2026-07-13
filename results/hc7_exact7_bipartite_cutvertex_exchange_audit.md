# Independent audit: bipartite thin-shore cutvertex exchange

**Status:** GREEN.

## Verdict

**Theorem: GREEN after four explicit corrections.**  The theorem correctly
closes the cutvertex branch of an actual order-seven adhesion with a
nonempty bipartite boundary, thin packet number one, and at least two rich
packets, except for the displayed crossed two-lobe cell.

**Barrier: GREEN within its stated trust boundary.**  The 24-vertex graph
really is seven-connected, has exact packet vector `(1,2)`, satisfies every
literal Dirac neighbourhood inequality at parameter seven, and has no
disjoint carriers for the natural bipartition.  It deliberately contains a
literal `K_7` and is not contraction-critical, so it refutes only the raw
connectivity-plus-Dirac carrier principle.

The audited theorem is
[`hc7_exact7_bipartite_cutvertex_exchange.md`](hc7_exact7_bipartite_cutvertex_exchange.md).
The barrier and its verifier are
[`hc7_exact7_bipartite_carrier_connectivity_dirac_barrier.md`](../barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier.md)
and
[`hc7_exact7_bipartite_carrier_connectivity_dirac_barrier_verify.py`](../barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier_verify.py).

## 1. Corrections made before the GREEN verdict

The first draft had four formal defects.  They are now repaired.

1. Dirac's inequality requires strong seven-contraction-criticality, not
   merely six-colourability of every proper minor.  The hypotheses now say
   explicitly that `chi(G)=7` and every proper minor is six-colourable.
2. The proof used connectedness of `L` without deriving it.  The corrected
   proof observes that every component of `G[L]` is `S`-full by
   seven-connectivity; packet number one therefore makes `L` connected.
3. The scope is now restricted explicitly to the nonempty
   bipartite-boundary branch.  The proof does not address arbitrary
   boundaries.
4. The first Dirac refinement was written only for bipartition sizes four
   and three, although its final residual statement used `d_L(z)>=3`
   without that qualifier.  The corrected calculation works for every
   possible class size.

No mathematical conclusion was weakened by these repairs.

## 2. Exact audited scope

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,
\]

with no edge from `L` to `R` and both shores nonempty.  Assume:

* `G` is seven-connected;
* `chi(G)=7` and every proper minor of `G` is six-colourable;
* the packet number of `L` is one;
* `R` contains two vertex-disjoint `S`-full packets; and
* `H=G[S]` is nonempty and bipartite, with a fixed bipartition
  `S=I dotcup J`.

The proof only needs the existence of two rich packets, not the assertion
that the rich packet number is exactly two.  Thus it applies to the exact
`(1,2)` residue and, formally, to any richer opposite shore as well.

## 3. Connectedness and the lobe defect bound

For a component `C` of `G[L]`, actual separation gives
`N_G(C) subseteq S`.  The nonempty opposite shore remains after deleting
`N_G(C)`, so this neighbourhood is a vertex cut.  Seven-connectivity and
`|S|=7` imply

\[
                         N_G(C)=S.
\]

Every component is consequently an `S`-full packet.  Packet number one
forces `G[L]` to have exactly one component.

Now let `z` be a cutvertex of `G[L]`, and let
`C_1,...,C_k` be the components of `L-z`.  Connectedness makes every
`C_i` adjacent to `z`.  Since

\[
                         N_G(C_i)\subseteq S\cup\{z\},
\]

and the opposite shore is nonempty, seven-connectivity gives

\[
                         |N_S(C_i)|\ge6.
\]

Thus every lobe defect `D_i=S-N_S(C_i)` has order at most one.  No stronger
connectivity than seven is used.

## 4. Three or more lobes

For each `j`, define

\[
                  X_j=\{z\}\cup\bigcup_{i\ne j}C_i.
\]

It is connected, is disjoint from `C_j`, and is adjacent to `C_j`.  Its
literal boundary defect is exactly

\[
 S-N_S(X_j)=\bigl(S-N_S(z)\bigr)\cap\bigcap_{i\ne j}D_i.
\]

If `k>=3` and every `X_j` has a nonempty defect, then for each `j` all the
singleton defects with index different from `j` coincide and that same
vertex is missed by `z`.  Comparing two values of `j` forces every `D_i`
to be one common singleton missed by `z`.  Then all of `L` misses that
boundary vertex, contradicting the established `S`-fullness of `L`.

Hence some `X_j` is full.  Since `C_j` misses at most one boundary vertex,
it contacts every member of at least one of the two nonempty bipartition
classes.  Assign `C_j` to such a class and the full `X_j` to the other.
These are disjoint adjacent connected carriers.

## 5. Exactly two lobes

Let the two defects be `D_1,D_2`.

* If either defect is empty, that lobe is a carrier for either class; the
  other lobe contacts one whole class.  Adding `z` to the full lobe if
  necessary supplies carrier adjacency.
* If the two singleton defects lie in opposite bipartition classes, assign
  each lobe to the class containing the other defect.  Again, adding `z`
  to one lobe makes the carriers adjacent.
* If `z` contacts a lobe's missing boundary vertex, adjoining `z` makes
  that lobe full, reducing to the first case.

Therefore failure of this carrier construction requires

\[
 D_1=\{a\},\qquad D_2=\{b\},
\]

where `a,b` lie in the same bipartition class and `z` misses both.  The
vertices are distinct: if `a=b`, both lobes and `z` miss `a`, contradicting
the fullness of `L`.  This is exactly the theorem's residual contact
geometry.  The alternatives need not be exclusive: extra internal
routing inside a residual lobe may still produce the carriers, but the
displayed contact data are precisely what the elementary lobe assignment
does not decide.

## 6. Bipartition parity

Bipartitions of distinct connected components of `H` can be flipped
independently.  Thus defects in different components can be placed in
opposite classes.  Inside one connected bipartite component, two vertices
are in the same class exactly when their distance is even.  Consequently
the crossed residue can survive all choices of bipartition only when `a,b`
belong to the same boundary component at even distance.  This quantifier is
correct even when `H` has isolated vertices.

## 7. Exact two-carrier state and `(1,2)` gluing

This step was checked independently because the source criterion occurs in
a section originally developed for a `(1,3)` shore.

Let `T_I,T_J subseteq L` be the disjoint adjacent connected carriers.
Because `I,J` are independent, both

\[
                         T_I\cup I,
                         \qquad T_J\cup J
\]

are connected and disjoint.  Contract them in the thin closed shore.  The
two images are adjacent, so any six-colouring of the resulting proper minor
induces exactly the equality state `I|J` on the untouched rich closed
shore.

Conversely, choose the two disjoint `S`-full packets in `R` and contract
one together with `I` and the other together with `J`.  Their images are
adjacent because either packet contacts every literal vertex of the other
block.  A six-colouring of this proper minor induces exactly the same state
on the untouched thin closed shore.  A palette permutation aligns the two
block colours, and the two closed-shore colourings glue because there is no
`LR` edge.

Only two rich packets occur in this construction.  The third packet from
the older `(1,3)` context is not used.  There is also no hidden singleton
contact condition: here `Q` is empty because `I dotcup J=S`.

## 8. Dirac refinement

In the crossed cell, name the defect class `I`, put `p=|I|`,
`r=d_L(z)`, and `Z=N_S(z)`.  There are no `LR` edges, so

\[
                         d_G(z)=r+|Z|.
\]

Both bipartition classes are independent.  Strong
seven-contraction-criticality gives Dirac's inequality

\[
                 \alpha(G[N(z)])\le d_G(z)-5.
\]

Using the independent sets `Z cap I` and `Z cap J` yields

\[
             r+|Z\cap J|\ge5,
             \qquad r+|Z\cap I|\ge5.
\]

Since `I` contains the distinct missed vertices `a,b`, while `J` is the
other class,

\[
        2\le p\le6,
        \qquad |Z\cap I|\le p-2,
        \qquad |Z\cap J|\le7-p.
\]

It follows that

\[
                    r\ge\max\{7-p,p-2\}\ge3.
\]

Because there are exactly two lobes and each meets `z`, one lobe contains
at least two distinct neighbours of `z`.  This conclusion is valid for all
bipartition sizes, not merely `4+3`.

## 9. Barrier construction

The verifier builds:

* the seven-vertex boundary `P_7` with classes of orders four and three;
* an 11-vertex thin shore obtained by deleting one vertex from the
  icosahedral graph;
* four unique portals around the outer five-cycle in alternating class
  order, while every thin vertex contacts the other three boundary labels;
  and
* a rich `K_6`, two of whose vertices are individually `S`-full while all
  four others miss the same boundary vertex.

The counts are exact:

\[
              |V(G)|=7+11+6=24,
              \qquad |E(G)|=121.
\]

An independent exhaustive check deleted every vertex set of order at most
six: all `190051` resulting graphs were connected.  The literal boundary
`S` is a seven-vertex cut, so the node connectivity is exactly seven.

The packet numbers also have direct certificates.

* The whole thin shore is full.  Every thin full packet must contain each
  of the four unique portal vertices, so two such packets cannot be
  disjoint.  Its packet number is one.
* The two distinguished rich vertices are disjoint singleton full packets.
  Every rich full packet must contain one of them because every other rich
  vertex misses `s_0`; a third disjoint full packet is impossible.  Its
  packet number is two.

For every one of the 24 vertices, exhaustive maximum-independent-set
calculation in its literal neighbourhood verifies

\[
                       \alpha(G[N(x)])\le d_G(x)-5.
\]

The four unique thin portals occur in cyclic order `I,J,I,J` on the outer
face.  An `I`-carrier must connect the two `I` portals and a `J`-carrier
must connect the two `J` portals.  Two disjoint such connected subgraphs
would contain vertex-disjoint paths joining alternating boundary points of
a planar disc, impossible by the Jordan curve theorem.  Exhaustive
enumeration of all connected thin-shore subsets independently confirms
that no carrier pair exists.

## 10. Trust boundary and exact remaining gap

The barrier is not a counterexample to the cutvertex theorem: its thin
shore is highly connected and has no cutvertex.  More importantly, the
rich `K_6` together with `s_1` is a literal `K_7`, and the graph is not
contraction-critical.  It establishes only that

\[
 \text{seven-connectivity + packet `(1,2)` + static Dirac inequalities}
 \not\Longrightarrow
 \text{the two bipartition carriers}.
\]

After the theorem, the cutvertex branch retains exactly the crossed
two-lobe geometry: distinct same-class defects in one boundary component at
even parity, both missed by the cutvertex, with at least three cutvertex-to-
lobe neighbours.  Eliminating that cell requires `K_7`-minor-freeness or a
genuine proper-minor state transition; neither the theorem nor the barrier
claims that it is already closed.
