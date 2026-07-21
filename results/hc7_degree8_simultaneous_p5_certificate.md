# A fixed-colouring `P_5` subdivision and the exact dirty-certificate residue

**Status:** written proof; [separately audited GREEN](hc7_degree8_simultaneous_p5_certificate_audit.md).
This note is nonterminal.  It does not prove `HC_7`, an avoidance form of the
five-root packaging theorem, or a strict same-form reduction.

## 1. Setting and statement

Let `G` be a finite simple graph which is not six-colourable but every proper
minor of which is six-colourable.  Let `u` have degree eight.  Suppose that

\[
 Q=\{q_1,q_2,q_3\}\subseteq N_G(u)
\]

is independent, put `U=N_G(u)-Q`, and label

\[
 U=\{a,b,c,d,e\},\qquad E(G[U])=\{ab,cd\}.                 \tag{1.1}
\]

Thus `G[U]` is `2K_2+K_1`, with isolated vertex `e`.

### Theorem 1.1 (one fixed colouring supplies both paths and the certificate)

There is a proper six-colouring `phi` of `G-u`, with one colour `gamma` on
all of `Q`, having the following properties.

1. The five vertices of `U` receive the five colours other than `gamma`,
   each exactly once.
2. Every two vertices `x,y` of `U` lie in one `phi(x)`--`phi(y)`
   bichromatic component.
3. There are vertex-disjoint paths `P_ea,P_bc` such that `P_xy` is a
   shortest `phi(x)`--`phi(y)` bichromatic `x`--`y` path.  Every internal
   vertex of either path lies outside `N_G[u]`, and the internal vertices of
   each individual path lie in one component of `G-N_G[u]`.  Moreover

   \[
              P_{ea}\cup ab\cup P_{bc}\cup cd              \tag{1.2}
   \]

   is a subdivision of the path with rooted order `e,a,b,c,d`.
4. Let `Gamma` be the `gamma` colour class in `G-u` and put

   \[
                       X=(G-u)-\Gamma .                         \tag{1.3}
   \]

   Then `chi(X)=5`, and `U` receives all five colours in every proper
   five-colouring of `X`.
5. Put `T=e-a-b-c-d` and let

   \[
                       D=K_U-E(T).                              \tag{1.4}
   \]

   The graph `D` has six edges.  There are pairwise disjoint connected
   vertex sets

   \[
                       (B_x:x\in U)                             \tag{1.5}
   \]

   in `X`, with `x\in B_x`, such that `B_x` and `B_y` are adjacent whenever
   `xy\in E(D)`.

The only bag adjacencies not guaranteed by (1.5) or by the literal edges
`ab,cd` are `ea,bc`.  Let

\[
   \mathcal M=\{xy\in\{ea,bc\}:B_x\text{ and }B_y\text{ are nonadjacent}\}.
                                                               \tag{1.6}
\]

Thus `\mathcal M` is the set of adjacencies that this particular certificate
actually lacks.  They can all be repaired under the following
certificate-relative condition.

For a path `P` and distinct bag labels `x,y`, call a subpath `I` of `P` an
`xy` **consecutive-bag interval** if its ends lie respectively in `B_x` and
`B_y` and its internal vertices avoid

\[
                            W=\bigcup_{z\in U}B_z.               \tag{1.7}
\]

If, for every `xy\in\mathcal M`, the union `P_ea\cup P_bc` contains an `xy`
consecutive-bag interval, then the bags can be enlarged, without changing
their roots, to a `U`-rooted `K_5` model.

Consequently, if this enlargement criterion fails for the certificate
(1.5), then for at least one actually missing pair `xy\in\mathcal M`, neither
path has consecutive visits to `B_x,B_y`.  In particular, on the designated
path `P_xy`, every `B_x`--`B_y` subpath has an internal vertex in a foreign
bag `B_z`, where `z\notin\{x,y\}`.  This is the exact model-relative
dirty-path residue.

## 2. The star-contraction colouring

Contract the connected star `G[\{u\}\cup Q]` to one vertex `w`.  The result
is a proper minor of `G`, so it has a proper six-colouring.  Expanding `w`
and giving `u` and all three vertices of `Q` the colour of `w`, denoted by
`gamma`, gives a proper six-colouring of

\[
                         G-E_G(u,Q).                             \tag{2.1}
\]

Its restriction `phi` to `G-u` is a proper six-colouring.  Every vertex of
`U` avoids `gamma`, since all edges from `u` to `U` remain in (2.1).

If one of the other five colours were absent from `U`, give `u` that absent
colour.  The vertices of `Q` still have colour `gamma`, and `N_G(u)=Q\cup U`,
so this would properly six-colour the original graph `G`.  Therefore all
five non-`gamma` colours occur on the five vertices of `U`, once each.  This
proves item 1.

Fix distinct `x,y\in U`.  Suppose that they lie in different components of
the subgraph induced by their two colours.  Interchange those colours on
the component containing `x`.  The vertex `y` is not changed.  Before the
interchange, `x` was the unique vertex of `U` with colour `phi(x)`; after
the interchange that colour is absent from `U`.  No member of `Q` is
changed because `Q` has colour `gamma`.  Giving `u` the now-absent colour
again properly six-colours `G`, a contradiction.  This proves item 2.

## 3. Simultaneous localized paths and the five-colour core

For each pair `x,y\in U`, choose a shortest bichromatic `x`--`y` path in
the component from item 2.  Its internal vertices avoid `N_G(u)`: the
vertices of `Q` have colour `gamma`, while among `U` only `x,y` have either
of the two colours.  The path is in `G-u`; hence every internal vertex lies
outside `N_G[u]`.  Its nonempty interior is connected and therefore lies
in one component of `G-N_G[u]`.

Apply this to `ea` and `bc`.  These are nonedges by (1.1), so both paths
have nonempty interiors.  Their two colour pairs are disjoint, and hence
the two paths themselves are vertex-disjoint.  Adding the literal edges
`ab` and `cd` gives exactly the rooted subdivision in (1.2).  This proves
item 3.

The colouring `phi|X` uses the five non-`gamma` colours, so `chi(X)\leq5`.
If `X` had a proper four-colouring, colour the independent set `Gamma` with
a fifth colour and give `u` a sixth colour.  This would properly colour
`G`, so `chi(X)=5`.

Now take any proper five-colouring `eta` of `X`.  If some one of its five
colours were absent from `U`, colour all of `Gamma` with a sixth colour and
give `u` the colour absent from `U`.  This is proper: `Gamma` is independent,
and

\[
                         \Gamma\cap N_G(u)=Q.                    \tag{3.1}
\]

It would again six-colour `G`.  Thus every proper five-colouring of `X`
uses all five colours on `U`, proving item 4.

## 4. The six-demand rooted certificate

The colouring `phi|X` has five colour classes and `U` is a transversal.
Every pair of roots lies in one bichromatic component, and all the
corresponding paths lie in `X` because neither colour is `gamma`.  Thus the
routing graph of `(X,phi|X,U)` is `K_U`.

Kriesell and Mohr's Theorem 7 states that every graph on five vertices with
at most six edges has property `(*)`: whenever it is a spanning subgraph of
such a routing graph, the coloured graph has a rooted certificate for it.
Apply that theorem to the six-edge graph `D` in (1.4).  It gives exactly the
five connected, pairwise disjoint rooted bags in (1.5), with every adjacency
prescribed by `D`, whose edge set is

\[
                         \{eb,ec,ed,ac,ad,bd\}.                  \tag{4.1}
\]

Additional bag adjacencies are harmless.  This proves item 5.

## 5. Consecutive defect intervals

Let `I_xy` be an `xy` consecutive-bag interval, where `xy\in\mathcal M`.
Write its ends as `p\in B_x` and `q\in B_y`.  Replace

\[
                         B_x\quad\hbox{by}\quad
                         B_x\cup(V(I_{xy})-\{q\}).                \tag{5.1}
\]

The enlarged bag is connected, remains disjoint from every other bag, and
the last edge of the interval makes it adjacent to `B_y`.  No old contact
is lost.

If `\mathcal M=\{ea,bc\}`, the two selected intervals are automatically
vertex-disjoint.  Indeed, their four endpoint bags are distinct; if two
intervals on one simple path overlapped, an endpoint of one would be an
internal vertex of the other, contrary to the definition.  Intervals on the
two disjoint paths are plainly disjoint.  When `|\mathcal M|\leq1` there is
no simultaneous-disjointness issue.  We may therefore perform (5.1) for
every pair in `\mathcal M`.  The six adjacencies of `D`, the literal root
edges `ab,cd`, the contacts already present for pairs outside `\mathcal M`,
and the repaired contacts for pairs in `\mathcal M` are all ten edges of
`K_U`.  This proves the enlargement criterion.

For either path, record in order the labels of the maximal visits to the
five bags, suppressing consecutive repetitions of the same label.  Two
distinct labels are consecutive in this reduced trace exactly when the
intervening subpath is a consecutive-bag interval.  If the criterion fails,
some actually missing pair `xy\in\mathcal M` has no such transition in either
reduced trace.  The designated path for that pair starts in one endpoint bag
and ends in the other, so every passage between them contains a visit to a
bag with a third label.  This proves the final assertion of Theorem 1.1.

## 6. The exact full-separator consequence

The next consequence records precisely what a successful repair gives in
the minor-minimal `HC_7` setting.  It is stated separately because it uses
connectivity and the standard neighbourhood independence bound, not merely
the star-contraction colouring.

### Corollary 6.1 (rooted completion or a model-contained full separator)

In addition to the hypotheses of Theorem 1.1, assume that `G` is
seven-connected and

\[
                         \alpha(G[N_G(u)])\leq3.                 \tag{6.1}
\]

For a minor-minimal `HC_7` counterexample this is the established
contraction-critical bound `alpha(G[N_G(u)])\leq d_G(u)-5` specialized to
`d_G(u)=8`.

Suppose the consecutive-interval criterion gives a `U`-rooted `K_5` model
`(B'_x:x\in U)` in `G-u`, and put `W'=\bigcup_xB'_x`.  Then one of the
following holds.

1. `G` contains an explicit `K_7`-minor model.
2. For some distinct `q_i,q_j\in Q`, there is an inclusion-minimal
   `q_i`--`q_j` separator

   \[
                              Z\subseteq W',\qquad |Z|\geq6,     \tag{6.2}
   \]

   in `H=G-u`.  If `R_i,R_j` are the components of `H-Z` containing
   `q_i,q_j`, respectively, then

   \[
                    N_H(R_i)=N_H(R_j)=Z                         \tag{6.3}
   \]

   and, in the original graph,

   \[
             N_G(R_i)=N_G(R_j)=Z\cup\{u\}.                      \tag{6.4}
   \]

   Thus `Z\cup\{u\}` is the boundary of an actual separation of order at
   least seven, with two distinguished open components full to every
   boundary vertex.  Moreover at least one of the five rooted bags contains
   two vertices of `Z`.

### Proof

Condition (6.1) and the independence of `Q` imply that `Q` jointly dominates
`U`: otherwise `Q\cup\{x\}` would be an independent four-set for some
`x\in U`.

Every completed bag lies in `X`, while `Q\subseteq\Gamma`, so `Q` is
disjoint from `W'`.  If one component `K` of `(G-u)-W'` contains all three
vertices of `Q`, then the seven sets

\[
                         \{u\},\quad K,\quad (B'_x:x\in U)       \tag{6.5}
\]

are pairwise adjacent.  The rooted bags form a `K_5` model; `u` sees every
bag through its root and sees `K` through `Q`; and `K` sees every bag because
`Q` jointly dominates `U`.  Hence (6.5) is an explicit `K_7`-minor model.

Otherwise two vertices `q_i,q_j` of `Q` lie in different components of
`(G-u)-W'`.  Choose an inclusion-minimal `q_i`--`q_j` separator `Z` contained
in `W'`.  Deleting one vertex from a seven-connected graph leaves a
six-connected graph, so `|Z|\geq6`.  Minimality says that every `z\in Z`
has a neighbour in each of the two distinguished components; componenthood
gives the reverse containment.  This proves (6.3).

The only vertex of `G-H` is `u`, and `u` is adjacent to `q_i` and `q_j`.
Therefore (6.4) follows.  Finally, six or more vertices of `Z` distributed
among five disjoint bags force one bag to contain at least two.  This proves
the corollary.  \(\square\)

## 7. Trust boundary and source

Theorem 1.1 uses one fixed star-contraction colouring for both localized
paths and for the Kriesell--Mohr certificate.  It therefore has no
cross-colouring splice.  What it does **not** prove is that the returned
certificate avoids either path.  In the dirty alternative, a path may run
through a common-neighbour bag, and splitting or reassigning that bag need
not preserve its root or all of its old contacts.  The consecutive-interval
condition is sufficient, not necessary, for a rooted `K_5` completion.

The full separator in Corollary 6.1 is literal but is not the strict
same-form restart required by the bounded-interface programme.  Its order
is unbounded; `Z` may contain vertices outside `N_G(u)`; the distinguished
components contain members of `Q\subseteq N_G(u)` and hence are not
components of `G-N_G[u]`; and neither a named aligned response nor a strict
decrease of a chosen anti-neighbourhood component has been proved.

Only the six-edge graph `D`, not `K_5`, is submitted to property `(*)`.
Kriesell and Mohr explicitly leave property `(*)` for `K_5` open.

**Primary source.** Matthias Kriesell and Samuel Mohr,
[“Kempe Chains and Rooted Minors,” Theorem 7](https://arxiv.org/abs/1911.09998),
arXiv:1911.09998v2.
