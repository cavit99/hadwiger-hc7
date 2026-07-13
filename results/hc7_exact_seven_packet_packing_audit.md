# Independent audit: exact-seven full-packet packing

## Verdict

**GREEN, with two scope clarifications.**  The packet inequalities and the
packing-vector conclusion are correct when `7-contraction-critical` has its
strong standard meaning

\[
 \chi(G)=7\quad\text{and every proper minor of }G\text{ is
 six-colourable}.
\]

The statement is about an **actual** separation: the two open shores are
nonempty and anticomplete, and their common literal vertex set is the
seven-vertex adhesion `S`.  It does not turn packing number one into a small
transversal or an apex set.

The theorem is not wholly new relative to this repository.  Its two proof
engines already occur in the full-shore reserve lift and shore-capacity
gluing.  Its useful new packaging is the sharp conclusion about arbitrary
internally disjoint `S`-full packets, rather than merely the components of
`G-S`.

## 1. Corrected exact statement

Let `G` be seven-connected, `K_7`-minor-free, and strongly
seven-contraction-critical.  Let `(G_1,G_2)` be a separation with

\[
 S=V(G_1)\cap V(G_2),\qquad |S|=7,
\]

and with both `V(G_i)-S` nonempty.  A packet in open shore `i` is a connected
subgraph of `G_i-S`; it is `S`-full if every literal vertex of `S` has a
neighbour in it.  Let `nu_i` be the maximum number of pairwise
vertex-disjoint `S`-full packets in shore `i`.  Then

\[
 \nu_1+\nu_2\le4,\qquad \min\{\nu_1,\nu_2\}=1,                 \tag{1.1}
\]

and

\[
 \omega(G[S])\le 6-(\nu_1+\nu_2).                            \tag{1.2}
\]

Consequently, after interchanging the shores, the only possible packing
vectors are

\[
                    (1,1),\quad(1,2),\quad(1,3).              \tag{1.3}
\]

## 2. Fullness and positivity of the packet numbers

Let `C` be a component of one open shore.  The separation implies
`N_G(C)\subseteq S`.  The opposite open shore is nonempty, so `N_G(C)` is an
actual vertex cut.  Seven-connectivity gives `|N_G(C)|\ge7`, and hence

\[
                              N_G(C)=S.                       \tag{2.1}
\]

Thus every open-shore component is itself an `S`-full packet.  In
particular

\[
                              \nu_1,\nu_2\ge1.                 \tag{2.2}
\]

This verifies proposed step 1.  Notice that collective fullness is all that
is used: no individual shore vertex is assumed complete to `S`.

## 3. Literal packet-plus-clique lift

Take `r` pairwise disjoint `S`-full packets
`P_1,...,P_r`, from either or both shores, and a clique `Q\subseteq S` of
order `7-r`.  Enumerate `S-Q={x_1,...,x_r}` and use the seven bags

\[
 P_i\cup\{x_i\}\quad(1\le i\le r),
 \qquad \{q\}\quad(q\in Q).                                  \tag{3.1}
\]

Every packet bag is connected because `x_i` has a neighbour in `P_i`.
They are disjoint because the packets and anchors are disjoint.  For
`i\ne j`, fullness of `P_i` at `x_j` gives an edge from the `i`-th bag to
the `j`-th bag.  Fullness at every `q in Q` gives all packet--clique
adjacencies, while `Q` supplies the remaining singleton adjacencies.
Thus (3.1) is a literal `K_7` model.

Edges between packets are neither assumed nor needed.  This proves proposed
step 2.  In a `K_7`-minor-free graph it gives, whenever `r\le7`,

\[
  \omega(G[S])<7-r.                                           \tag{3.2}
\]

For `r>7`, any seven packets already give a `K_7` by anchoring them at all
seven vertices of `S`.

## 4. Exact equality-state transfer from packets

The colour-gluing step is valid, but its proper-minor construction must be
spelled out.

Suppose each open shore contains `m` disjoint `S`-full packets and

\[
 S=I_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}I_m
      \mathbin{\dot\cup}Q,                                  \tag{4.1}
\]

where each `I_j` is independent of order at least two and `Q` is a clique.
Choose packets `P_1,...,P_m` on shore 1 and contract the pairwise disjoint
connected sets

\[
                              P_j\cup I_j.                    \tag{4.2}
\]

The resulting graph is a proper minor: every set (4.2) contains a nonempty
packet and at least two boundary vertices.  Let `z_j` be its image.  The
vertices

\[
                              z_1,...,z_m,\ Q                  \tag{4.3}
\]

form a clique.  Indeed, `P_j` is full at every vertex of `I_k` for
`j\ne k` and at every vertex of `Q`; the vertices of `Q` are mutually
adjacent.  Moreover

\[
 m+|Q|\le m+(7-2m)=7-m\le6,                                  \tag{4.4}
\]

so there is no palette-size problem.

Strong contraction-criticality gives a six-colouring of this proper minor.
Restrict it to the untouched closed shore 2 and expand each `I_j`
monochromatically with the colour of `z_j`.  Expansion is proper because
`I_j` is independent, and every edge from `I_j` to the untouched shore was
represented by an edge from `z_j`.  The clique (4.3) makes the induced
boundary equality partition **exactly** (4.1): different `I_j` blocks and
the singleton vertices of `Q` have distinct colours.

Repeating the construction with packets on shore 2 gives a colouring of
closed shore 1 with the same exact partition.  Extend the bijection on the
used block colours to a permutation of the six-colour palette, align the two
boundary colourings, and glue.  The open shores are anticomplete, so this is
a six-colouring of `G`, a contradiction.

This proves proposed step 3.  It also covers `m=1`; in that case one
independent block may be all of `S` and `Q` may be empty.

## 5. The total packing bound

Put `r=\nu_1+\nu_2` and take maximum packet families on both shores.

* If `r\ge7`, seven packets anchored at the seven boundary vertices give a
  `K_7` model.
* If `r=6`, take any singleton boundary clique `Q` and apply Section 3.
* If `r=5` and `G[S]` has an edge, use that edge as the two-vertex clique
  `Q` in Section 3.
* If `r=5` and `S` is independent, use one full packet on each shore in
  Section 4 with the one-block partition `I_1=S`.

Every case `r\ge5` is therefore impossible, proving

\[
                              \nu_1+\nu_2\le4.                 \tag{5.1}
\]

Now (3.2), applied to all `r` packets, is exactly

\[
                    \omega(G[S])\le6-r,                       \tag{5.2}
\]

which verifies proposed step 4 and the claimed clique bound.

## 6. The seven-vertex partition lemma

The remaining combinatorial assertion is correct.

### Lemma 6.1

Every triangle-free graph `J` on seven vertices has a partition

\[
 V(J)=I_1\mathbin{\dot\cup}I_2\mathbin{\dot\cup}Q,            \tag{6.1}
\]

where `I_1,I_2` are independent and have order at least two, and `Q` is a
clique.

### Proof

If `J` is bipartite, take a bipartition when both sides have order at least
two.  If one side is empty, split the other side into two sets of order at
least two and take `Q` empty.  If one side is a singleton, put that vertex
in `Q` and split the independent six-vertex side into two sets of order at
least two.

Suppose `J` is nonbipartite and take a shortest odd cycle `C`.  Its order is
five or seven.  If it is seven, it has no chord: a distance-two chord makes
a triangle and a distance-three chord makes a five-cycle.  Thus `J=C_7`;
delete one cycle vertex into `Q` and bipartition the remaining `P_6` into
classes of order three.

It remains that

\[
 C=c_0c_1c_2c_3c_4c_0                                       \tag{6.2}
\]

is an induced five-cycle, with two outside vertices `x,y`.  Each set
`N_C(x),N_C(y)` is independent on `C`, hence has order at most two.
For a cycle vertex `c_i`, the graph `C-c_i` is a path with two bipartition
classes of order two.

If `xy` is absent, each outside vertex forbids at most one choice of `i`:
a two-element independent neighbourhood `{c_j,c_{j+2}}` meets both parity
classes of `C-c_i` only when `i=j+1`, and a neighbourhood of order at most
one forbids none.  Choose one of the at least three un-forbidden `c_i`.
Then `x` and `y` extend independently to a two-colouring of `J-c_i`.

If `xy` is present, triangle-freeness makes `N_C(x)` and `N_C(y)` disjoint.
An empty neighbourhood is harmless: colour that outside vertex opposite
its mate after choosing a deletion allowed by the other.  When both are
nonempty, the disjoint independent neighbourhood pairs have, up to a
dihedral symmetry of `C` and interchange of `x,y`, exactly the following
five forms.  The last column gives a cycle vertex whose deletion permits
`x,y` to receive opposite colours:

\[
\begin{array}{c|c|c}
N_C(x)&N_C(y)&\text{deleted vertex}\\ \hline
\{c_0\}&\{c_1\}&c_0\\
\{c_0\}&\{c_2\}&c_0\\
\{c_0\}&\{c_1,c_3\}&c_0\\
\{c_0\}&\{c_1,c_4\}&c_1\\
\{c_0,c_2\}&\{c_1,c_3\}&c_0
\end{array}                                               \tag{6.3}
\]

Reading the parity classes of the resulting four-vertex path verifies each
row directly.  Hence in all cases some `c_i` has `J-c_i` bipartite.  Its
two classes each already contain two vertices of `C-c_i`, so both have
order at least two.  Put `Q={c_i}` to obtain (6.1).  This proves the lemma.
\(\square\)

As a dependency-free check, `results/hc7_exact_seven_partition_probe.cpp`
enumerates all `2^21` labelled graphs, finds exactly `133501`
triangle-free graphs, and verifies (6.1) for every one.  It also verifies
that every nonbipartite instance admits the balanced singleton deletion
used in the hand proof.

## 7. Excluding two packet-rich shores

If `\nu_1,\nu_2\ge2`, (5.1) forces

\[
                              \nu_1=\nu_2=2.                  \tag{7.1}
\]

A triangle in `G[S]`, together with the four packets, gives `K_7` by
Section 3.  If the boundary is triangle-free, apply Lemma 6.1 and then the
two-block transfer of Section 4, using two packets on each shore.  That
six-colours `G`, again a contradiction.  Therefore the two shores cannot
both have packing number at least two.  In view of (2.2),

\[
                              \min(\nu_1,\nu_2)=1,             \tag{7.2}
\]

and (1.3) follows from (5.1).  This verifies proposed step 5.

## 8. Exact overlap with existing results

1. `archive/hadwiger_full_shore_reserve_lift.md` contains the anchored
   full-shore branch-set mechanism used in Section 3.  The present packet
   version observes that the full connected objects need only be disjoint;
   they need not be whole components or pairwise anticomplete.
2. `archive/hadwiger_shore_capacity_hall.md` and
   `archive/hadwiger_uniform_full_cut_inequalities.md` contain the exact
   proper-minor state-transfer and colour-gluing mechanism used in Section
   4.  The present theorem specializes it to two shores carrying the same
   one- or two-block partition.
3. `archive/hadwiger_uniform_full_cut_inequalities.md` already proves that
   a minimum cut of order `c` with `m` components satisfies `c>=2m`.
   Thus `c=7` already implies at most three components of `G-S`.  The new
   assertion is stronger internally: it constrains disjoint full packets
   within a single component and gives the packing vectors (1.3).
4. `archive/hadwiger_reserve_zero_row_capacity_state_exchange.md` contains
   the analogous fact that two disjoint full carriers complete a fixed
   `K_5` frame.  Its frame is a branch-model interface rather than the
   literal seven-boundary interface here.

Thus the exact-seven packet theorem is a sound reusable corollary of two
existing mechanisms, with a genuinely sharper packet-thin conclusion at
an actual seven-adhesion.

## 9. Immediate pure-Moser application

The proposed application to
`results/hc7_moser_crossing_carrier.md` is valid, but it is already proved
there as Corollary 3.3.

After the rooted `K_4` bags `B_1,...,B_4` are fixed, every `N`-full packet
inside the opposite component `C_2` meets `1`, `3`, and every selected duty
root.  If `C_2` contained two disjoint such packets, Lemma 2.2 of that note
enlarges them inside connected `C_2` to disjoint adjacent connected sets
without losing contacts.  Assigning one to row `1` and the other to row `3`
satisfies every hypothesis of its Theorem 2.1, whose seven displayed bags
form a literal `K_7` model.  Since `C_2` itself is connected and full to
`N`, its packet number is at least one.  Hence every surviving Moser carrier
shore has packet number exactly one.

This conclusion needs neither the global packet theorem nor an inferred
transversal.  It is a direct label-preserving consequence of the already
audited carrier completion theorem.

## 10. Trust boundary

The audit proves only packet-number restrictions.  In particular,

\[
 \nu_i=1\not\Rightarrow
 \text{a one-vertex or two-vertex transversal of all `S`-full packets},
\]

and it does not produce a common equality state, a planar society, or a
coherent apex pair.  Those remain separate structural tasks.
