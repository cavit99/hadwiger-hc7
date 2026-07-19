# Colouring fork for two jointly persistent incident edges

**Status:** written proof; separate internal audit GREEN in
[`hc7_joint_persistent_incident_colour_fork_audit.md`](hc7_joint_persistent_incident_colour_fork_audit.md).

This note separates the two possible geometries of a jointly
deletion-persistent incident pair.  When the two outer ends are
nonadjacent, the existing simultaneous-contraction theorem gives its
five-colour saturation-or-bypass alternative.  When the outer ends are
adjacent, the three vertices form a critical triangle.  The common
two-edge-deletion graph then has exactly two response signatures.  Either
those signatures lie in different Kempe components, or a transition
between them exposes a colour-saturated connected bipartite subgraph.  Its
full neighbourhood is a commonly coloured separator unless the subgraph
dominates; in the latter case its complement is a five-chromatic
`K_6`-minor-free core.

No colour is identified with a branch-set label.

## 1. Setup

Let `q>=2`, and let `G` satisfy

\[
 \chi(G)=q+1,
 \qquad\text{and every proper minor of }G\text{ is }q\text{-colourable}.
                                                               \tag{1.1}
\]

Let

\[
                         e=va,\qquad f=vb                 \tag{1.2}
\]

be distinct edges, and put

\[
                         H=G-\{e,f\}.                     \tag{1.3}
\]

Suppose additionally that fixed pairwise disjoint connected sets form a
spanning labelled minor model in `H`.  In the application they are the
same seven branch sets of a jointly deletion-persistent labelled
`K_7`-minus-one-edge model.  The colouring statements below do not alter
those sets, but do not identify their labels with colours.

## 2. Nonadjacent outer ends

### Proposition 2.1

Suppose `ab` is not an edge.  There is a proper `q`-colouring `kappa` of
`H` and a colour `alpha` such that

\[
 \kappa(v)=\kappa(a)=\kappa(b)=\alpha,
 \qquad
 N_G(v)\cap\kappa^{-1}(\alpha)=\{a,b\}.                \tag{2.1}
\]

For every other colour `i`, at least one of `va,vb` has its ends in one
component of `H[kappa^{-1}({alpha,i})]`.  Moreover, either

1. one of `va,vb` has this property for all `q-1` alternate colours; or
2. `H-v` contains an `a-b` path which is the union of two named
   bichromatic components and at most one edge between them.  Interchanging
   one component gives a `q`-colouring of `G-f`, and interchanging the
   other gives a `q`-colouring of `G-e`.

#### Proof

Contract the connected three-vertex star on `v,a,b`.  This is a proper
minor, so (1.1) gives a `q`-colouring.  Since `ab` is absent, expanding the
contracted vertex gives a proper colouring of `H`.  Every vertex of
`N_G(v)-{a,b}` is adjacent to the contracted vertex, proving the exact
trace (2.1).

The remaining assertions are Theorem 1.1 of the audited
[bichromatic saturation-or-bypass theorem](../results/hc7_shared_interface_bichromatic_bypass.md),
applied with `s=v,w=a,t=b`.  \(\square\)

## 3. Adjacent outer ends

Assume throughout this section that

\[
                              ab\in E(G).                \tag{3.1}
\]

For a `q`-colouring of `H`, record whether the ends of `e` and `f` are
equal or proper.  Let `X` be the set of colourings with signature
`(equal,proper)`, and let `Y` be the set with signature
`(proper,equal)`.

### Theorem 3.1 (critical-triangle transition)

The following statements hold.

1. Every `q`-colouring of `H` belongs to exactly one of `X,Y`, and both
   sets are nonempty.  Each set contains a contraction colouring with the
   exact trace

   \[
   N_G(v)\cap c^{-1}(c(v))=\{a\}
   \quad\text{or}\quad
   N_G(v)\cap c^{-1}(c(v))=\{b\},                       \tag{3.2}
   \]

   respectively.
2. Either no Kempe component of the colouring reconfiguration graph of
   `H` meets both `X` and `Y`, or there are colourings `phi in X` and
   `psi in Y` differing by one Kempe interchange on a connected
   bichromatic subgraph `D`.
3. In the second alternative, write

   \[
        \phi(v)=\phi(a)=\alpha,\qquad \phi(b)=\beta.
                                                               \tag{3.3}
   \]

   The interchange uses exactly the colours `alpha,beta`, and precisely
   one of the following holds:

   - `v in D` and `a,b notin D`; or
   - `a,b in D` and `v notin D`.

   In the first case the `alpha`-coloured side of `D` has a neighbour of
   every colour outside `{alpha,beta}`.  In the second case both colour
   sides of `D` have a neighbour of every colour outside
   `{alpha,beta}`.
4. Put `S=N_G(D)`.  The colourings `phi,psi` agree on `S`, and

   \[
   S-\{a,b\}\subseteq
       \bigcup_{\theta\notin\{\alpha,\beta\}}\phi^{-1}(\theta)
                                                               \tag{3.4}
   \]

   in the first placement, while

   \[
   S-\{v\}\subseteq
       \bigcup_{\theta\notin\{\alpha,\beta\}}\phi^{-1}(\theta)
                                                               \tag{3.5}
   \]

   in the second.  If `G-N_G[D]` is nonempty, then `S` is the boundary
   of an actual separation.  In a `k`-connected host it has order at
   least `k`; equality gives an exact order-`k` separation carrying the
   common boundary assignment of the two opposite one-edge responses.

#### Proof

No colouring of `H` can make both deleted edges proper, since it would
colour `G`.  Nor can it make both pairs equal: then
`a,b` would have the common colour of `v`, contrary to the edge `ab` of
`H`.  Hence every colouring lies in exactly one of `X,Y`.

Colour the proper minor `G/e` and expand the contracted edge.  This gives
a colouring of `G-e=H+f`, so `f` is proper and `e` must have equal ends.
Every other neighbour of `v` is adjacent to the contracted vertex, giving
the first exact trace in (3.2).  Contracting `f` gives the other response
and trace.  Thus both response sets are nonempty.

If one Kempe component meets both sets, a shortest path in that component
has consecutive colourings of opposite signatures; call them `phi,psi`.
This proves item 2.

Consider the one interchange between them.  Breaking the equality of
`v,a` forces the common colour `alpha` to be one of the two interchanged
colours and puts exactly one of `v,a` in `D`.  Creating equality between
`v,b` then forces the other interchanged colour to be `beta`.  If `v` is
the changed endpoint, `b` is unchanged and `D` contains `v` but neither
`a` nor `b`.  If `a` is the changed endpoint, then `v` is unchanged and
`b` must change from `beta` to `alpha`; hence `D` contains the adjacent
pair `a,b` but not `v`.  These are the two placements in item 3.

Suppose first that `D` contains `v`.  If the `alpha`-coloured vertices of
`D` had no neighbour of some colour `theta` outside `{alpha,beta}`, they
could all be recoloured `theta`.  That set is independent, and the assumed
absence of a `theta`-neighbour makes the recolouring proper.  The vertex
`v` would then differ from both `a` and `b`, producing a `q`-colouring of
`G`, a contradiction.

Now suppose `D` contains `a,b`.  The same argument applied to the
`alpha`-side in `phi` makes `va` proper while `vb` is already proper, so
that side sees every untouched colour.  After the interchange, the old
`beta`-side contains `b`, has colour `alpha`, and is the equality side of
`vb`; recolouring it to any missing untouched colour would again colour
`G`.  Thus both sides have the asserted contacts.

The set `D` is one component of the `alpha,beta` subgraph of `H`.  Hence
no edge of `H` joins it to an outside vertex of either colour.  The only
such possible edges in `G` are the deleted edges `va,vb`, which gives
(3.4)--(3.5).  The interchange changes only vertices of `D`, so `phi` and
`psi` agree on its open neighbourhood `S`.

If a vertex lies outside `N_G[D]`, deleting `S` leaves both the connected
nonempty set `D` and a nonempty opposite side, with no edge between them.
Thus `S` is an actual separator.  Connectivity gives the order bound and
the equality conclusion.  \(\square\)

### Corollary 3.2 (the dominating transition component in `HC_7`)

Assume in addition that `q=6`, `G` is seven-connected and has no `K_7`
minor.  In the transition outcome of Theorem 3.1, either

1. `N_G(D)` is the boundary of an actual separation of order at least
   seven, on which the two opposite one-edge responses agree; or
2. `D` is a connected dominating bipartite subgraph and

   \[
                    \chi(G-D)=5,
       \qquad K_6\not\preccurlyeq G-D.                 \tag{3.6}
   \]

#### Proof

If `D` does not dominate, Theorem 3.1 gives the first outcome.  Suppose it
does.  A `K_6` minor in `G-D`, together with the connected dominating
subgraph `D` as a seventh branch set, would give a `K_7` minor.  Hence
`G-D` is `K_6`-minor-free, and `HC_6` gives `chi(G-D)<=5`.  On the other
hand, the two colour classes of `D` and a four-colouring of `G-D` would
give a six-colouring of `G`, so `chi(G-D)>=5`.  This proves (3.6).
\(\square\)

## 4. Application to the jointly persistent model

Let the seven fixed branch sets be those supplied by the jointly
persistent-edge theorem.  They remain the same spanning labelled
`K_7`-minus-one-edge model throughout `H`; no recolouring or Kempe
interchange modifies their vertex sets.

Thus the jointly persistent branch has the following exhaustive colouring
fork.

- If `ab` is absent, Proposition 2.1 gives a five-colour-saturated named
  edge or a three-colour `a-b` bypass avoiding `v`.
- If `ab` is present, Theorem 3.1 gives two exact critical-triangle
  response families.  They are either Kempe-separated, or a transition
  gives an actual separator on which the two opposite one-edge responses
  agree, or the connected-dominating five-chromatic core of Corollary 3.2.

The theorem does not force the Kempe-separated families to meet, bound a
separator above by seven, or assign the saturated palette colours to the
six foreign labels of the fixed minor model.  The repository's
two-root Kempe-class barrier shows why generic Kempe connectivity cannot
be assumed even in a highly connected graph with a spanning rooted model;
that example is excluded from the present `HC_7` application by its
`K_7` minor and actual order-seven separator.

## 5. Dependencies

- [Bichromatic saturation or a bypass at two incident critical edges](../results/hc7_shared_interface_bichromatic_bypass.md).
- Hadwiger's Conjecture for parameter six, used only in Corollary 3.2.
- [Kempe-class barrier for two root orientations](../barriers/hc7_two_root_kempe_class_icosahedron_barrier.md), used only as a guardrail.
