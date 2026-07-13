# The omitted-colour dichotomy for a maximal bipartite society

## Status

This note gives a uniform, label-free consequence of combining a maximal
connected induced bipartite society with the proved four-colour Strong
Hadwiger theorem.  In the `HC_7` setting, any choice of four colours gives
an actual boundary-rooted `K_4`-model.  The omitted fifth colour is not
forced into one additional branch bag.  What is forced is the following
sharp alternative:

* some omitted-colour exterior component sees all four rooted bags and is
  the fifth bag; or
* that component lies behind a full adhesion of order at least seven, and
  the equality states of proper-minor operations on opposite open shores
  are disjoint.

A mixed Kempe lemma also shows that the omitted colour cannot be isolated
from any one of the four retained colours.  An exact ten-vertex example
shows why this still need not concentrate the four connections in one
component.  Thus maximality plus one contraction colouring and Strong
`HC_4` do not by themselves produce the fifth bag; the all-proper-minor
state lock in the second outcome is indispensable.

## 1. Maximal society and the four-colour core

Let `G` be a proper-minor-minimal graph which is not six-colourable and
has no `K_7` minor.  Let

\[
                         S=A\mathbin{\dot\cup}B
\]

be inclusion-maximal subject to `G[S]` being a nontrivial connected
induced bipartite graph.  Contract `S` to a vertex `z`, put `Q=G/S`, and
fix a proper six-colouring `c` of `Q`.  Write `c(z)=alpha`.  Every external
neighbour of `S` avoids `alpha`, and maximality gives

\[
 N_G(w)\cap A\ne\varnothing\ne N_G(w)\cap B
 \quad\text{for every }w\in N_G(S)-S.                 \tag{1.1}
\]

Choose a colour `beta != alpha`, let `Gamma` be the other four colours,
and set

\[
 J=Q[c^{-1}(\Gamma)],\qquad
 X=(N_G(S)-S)\cap V(J).                              \tag{1.2}
\]

The parity-rooted-core theorem says that `X` is four-colour-saturating in
`J`.  The proved four-colour Strong Hadwiger theorem therefore gives an
`X`-rooted `K_4`-model

\[
                         \mathcal B=(B_1,B_2,B_3,B_4)  \tag{1.3}
\]

in `J`.  Put `M=\bigcup_i B_i`.  Notice that every bag meets the external
neighbourhood of `S`, but the bags need not correspond to the four named
classes of the reference colouring `c`.

## 2. The omitted colour has a mixed Kempe component with every retained colour

Put

\[
             P_\delta=(N_G(S)-S)\cap c^{-1}(\delta)
\]

for every colour `delta != alpha`.  Two-shore saturation makes every
`P_delta` nonempty.

### Lemma 2.1 (mixed omitted-colour components)

For every `gamma in Gamma`, some component of

\[
                       Q[c^{-1}(\{\beta,\gamma\})]
\]

meets both `P_beta` and `P_gamma`.

#### Proof

Suppose not.  Let `R` be the union of all beta--gamma components meeting
`P_beta`, and interchange beta and gamma on `R`.  Every old beta portal
becomes gamma.  No old gamma portal becomes beta, by the assumed absence
of a mixed portal component.  Hence beta is now absent from the entire
external neighbourhood of `S`; alpha was already absent there.

Keep the switched colouring outside `S`, colour `A` with alpha, and
colour `B` with beta.  Internal society edges cross the bipartition, and
no external edge at either shore is monochromatic.  This is a proper
six-colouring of `G`, a contradiction.  \(\square\)

This lemma is simultaneous only at the level of existence.  Its four
components may be different, and a component may enter the rooted model
through only one bag.

### Corollary 2.2 (first-entry certificate)

For each `gamma in Gamma`, choose a path in a mixed component from a beta
portal to a gamma portal.  Let `C` be the component of `G-S-M` containing
its beta end.  Either the path reaches a gamma portal while still in `C`,
or its first vertex in `M` lies in some `B_i`, and then `C` is adjacent to
`B_i`.

No injectivity of `gamma -> i` is implied.  This is the exact point at
which four Kempe witnesses can collapse onto repeated bag labels.

## 3. Fifth bag or a full seven-adhesion

The next theorem needs only connectivity, not the colouring used above.

### Theorem 3.1 (omitted-colour component dichotomy)

Assume in addition that `G` is seven-connected.  Let `C` be any component
of `G-S-M` which meets `P_beta`.  Then one of the following holds.

1. `C` is adjacent to every one of `B_1,...,B_4`.  Consequently
   `(C,B_1,...,B_4)` is an `N_G(S)`-rooted `K_5`-model in `G-S`.
2. For some `j`, `C` is anticomplete to `B_j`, and there is a separation
   `(L,R)` of `G` with

   \[
       C\subseteq L-R,\qquad B_j\subseteq R-L,
       \qquad Z=L\cap R\subseteq S\cup M,
       \qquad |Z|\ge7,                               \tag{3.1}
   \]

   such that the components of `G-Z` containing `C` and `B_j` are both
   full to `Z`.

#### Proof

The first conclusion is immediate: `C` is connected and contains a beta
portal, the four model bags are pairwise adjacent and each contains a
portal, and all five sets are disjoint.

Otherwise choose `B_j` anticomplete to `C`.  Because `C` is a component
of `G-S-M`, every neighbour of `C` lies in `S union M`.  Thus `N_G(C)`
separates `C` from `B_j`.  Choose an inclusion-minimal separator
`Z subseteq N_G(C)` between fixed vertices of `C` and `B_j`.  The two
distinguished components of `G-Z` are full to `Z`, by minimality of the
separator.  Seven-connectivity gives `|Z|>=7`, and the associated
separation has all the properties in (3.1).  \(\square\)

The adhesion conclusion is not merely a large cut.  Minor-criticality
puts an exact exchange lock on it.

### Lemma 3.2 (crossed operation-state lock)

Let `(L,R)` be any separation of `G` with boundary `Z=L cap R`.  Let
`o_L` and `o_R` be proper minor operations supported strictly inside
`L-R` and `R-L`, respectively; neither operation may identify, delete, or
otherwise alter a boundary vertex.  For a six-colouring of an operated
graph, record on `Z` only its equality partition into colour classes.

No colouring of `o_L(G)` and colouring of `o_R(G)` induce the same
equality partition on `Z`.

#### Proof

If the two partitions agreed, permute the six colour names in one
colouring so that the assignments agree vertex by vertex on `Z`.  Use the
colouring of `o_R(G)` on the untouched side `G[L]`, and the colouring of
`o_L(G)` on the untouched side `G[R]`.  They agree on `Z`; since there are
no edges between the two open shores, they splice to a proper
six-colouring of the original graph `G`, a contradiction.  \(\square\)

Thus outcome 2 supplies exactly the kind of model-relative, faithful
state lock that a dynamic exchange argument can attack.  A statement
about one reference colouring would be strictly weaker and is false as a
route to the fifth bag.

## 4. When the rooted `K_5` does finish the split

Suppose outcome 1 of Theorem 3.1 holds, and denote its five external bags
by `D_1,...,D_5`.  In each `D_i` choose a portal `w_i in N_G(S)`, and by
maximality choose neighbours

\[
                         a_i\in A,\qquad b_i\in B.       \tag{4.1}
\]

### Lemma 4.1 (common tree-edge split)

Let `T` be a spanning tree of `G[S]`.  If one edge `e in E(T)` belongs to
all five tree paths `T[a_i,b_i]`, then `G` contains a `K_7` minor.

#### Proof

The two components `S_1,S_2` of `T-e` are connected and adjacent, and
every pair `a_i,b_i` is separated by the cut.  Hence every `D_i` is
adjacent to both `S_1` and `S_2`.  The five mutually adjacent external
bags together with `S_1,S_2` are seven pairwise adjacent disjoint
connected branch sets.  \(\square\)

Accordingly, even the positive `K_5` outcome leaves a precise
label-preserving society-split problem when the five portal paths have no
common tree edge.  This is a finite tree-frame obstruction, not an
automatic consequence of bipartiteness.

## 5. Sharp local counterexample to automatic fifth-bag concentration

The following graph shows that Theorem 3.1 cannot be replaced by an
automatic fifth-bag conclusion using only the local hypotheses in
Sections 1--2.

Take the society edge `S={0,1}`.  Let `x_1,...,x_4` induce a `K_4`, let
`y_1,...,y_4` be independent, and add only the edges `x_i y_i` between
these two sets.  Join every `x_i` and every `y_i` to both `0` and `1`.

* `S` is inclusion-maximal induced bipartite: adjoining any outside
  vertex creates a triangle with `01`.
* After contracting `S`, colour the contraction alpha, the four `x_i`
  with four distinct gamma colours, and every `y_i` beta.
* The singleton `x_i` are an external-neighbour-rooted `K_4`.
* For each gamma colour, the edge `y_i x_i` is the required mixed
  beta--gamma component.
* Every component outside the four rooted bags is one vertex `y_i` and
  sees exactly one bag.  The exterior has no `K_5` minor, and the whole
  graph has no `K_7` minor.

The graph is deliberately six-colourable, so it does not refute the use
of all proper-minor states in a hypothetical counterexample.  It proves
that maximality, one contraction colouring, four mixed Kempe witnesses,
and a rooted `K_4` do not logically imply concentration into a fifth bag.

The script
`maximal_bipartite_fifth_colour_counterexample.py` exhaustively checks
maximality of `S` and verifies the two negative minor assertions with the
workspace's exact branch-set search.

## 6. Exact frontier

The new uniform rooted-model target is now:

> Across the full adhesion in Theorem 3.1(2), use the disjoint equality
> states of *all* opposite proper-minor operations to force either one
> beta component to absorb four rooted-bag labels or a common tree-edge
> split of the resulting five portal pairs.

The ten-vertex obstruction lacks precisely this all-operation
minor-critical exchange system.  Any claimed proof which uses only a
single contraction colouring or the four separate Kempe components will
also apply to that obstruction and is therefore invalid.
