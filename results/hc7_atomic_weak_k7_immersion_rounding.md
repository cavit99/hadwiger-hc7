# Atomic weak `K_7` immersions round to a near-clique model

**Status:** written proof; separate internal audit GREEN.

This note records the exact positive content of the weak-immersion route at
its first non-topological case.  One atomic collision can be rounded without
losing literal branch labels.  The result is a `K_7` minor in the easy
crossing pattern, and otherwise a spanning `K_7`-minus-one-edge model with
singleton ends of the missing edge.

The theorem does **not** show that a collision-minimal weak immersion has
only one collision.  Nor does it complete the resulting singleton-root
near-`K_7` model.  Those two omissions are the exact global and local gates
left by this approach.

## 1. Roles and atomicity

Use the path formulation of a weak immersion.  A weak `K_t` immersion in a
simple graph `G` consists of distinct branch vertices

\[
                         v_1,\ldots,v_t
\]

and, for every pair `ij`, a simple `v_i`--`v_j` path `P_ij`, with all of the
paths pairwise edge-disjoint.  A branch vertex is allowed to occur internally
on a path for a different pair.

At a vertex `x`, count one **branch role** if `x` is a branch vertex, and one
**transit role** for every immersion path on which `x` is internal.  Let
`r(x)` be the number of these roles.  A vertex is a **collision vertex** when
`r(x)>=2`.

The immersion is **atomic** if exactly one vertex `x` is a collision vertex,
`r(x)=2`, and every other vertex has at most one role.  There are then exactly
two possible collision types.

1. `x` is not a branch vertex and is internal on exactly two paths.
2. `x` is a branch vertex and is internal on exactly one foreign path.

This definition deliberately counts transit through a branch vertex.  A
definition which counts only intersections of path interiors would miss the
second case.

## 2. A path-allocation lemma

### Lemma 2.1 (singleton-root allocation)

Let `Q` be a subdivision of `K_t-ab` in `G`, with branch vertices labelled by
`V(K_t)`.  Then `G[V(Q)]` has a `K_t-ab` minor model in which the branch sets
labelled `a,b` are the literal singletons `{v_a},{v_b}`.

#### Proof

For every retained subdivided edge incident with `a` or `b`, assign all of
its internal vertices to its other endpoint.  Assign all internal vertices
of every other subdivided edge to either one of its endpoints.  For each
label, take its branch vertex together with all path interiors assigned to
it.

The resulting sets are disjoint.  Each is connected because every assigned
path interior ends at its labelled branch vertex.  Along every retained
subdivided edge, either the original edge joins its two branch vertices or
the last edge between the two endpoint assignments gives the required
branch-set adjacency.  No internal vertex was assigned to `a` or `b`, so
their branch sets are the claimed singletons.  \(\square\)

### Lemma 2.2 (spanning absorption)

Let `G` be `t`-connected and let

\[
                         A_1,\ldots,A_t
\]

be a `K_t-ab` minor model in `G` with `A_a={v_a}` and `A_b={v_b}`.  The model
can be made spanning while those two branch sets remain unchanged.

#### Proof

Put `U=A_1 union ... union A_t`, and let `D` be a component of `G-U`.  If
some vertex of `U` is not in `N(D)`, then `N(D)` separates that vertex from
`D`, so `t`-connectivity gives `|N(D)|>=t`.  If every vertex of `U` lies in
`N(D)`, the same inequality follows from `|U|>=t`.  Thus in either case `D`
has at least `t` distinct neighbours in `U`.

At most two of those neighbours are the singleton vertices `v_a,v_b`.
Consequently `D` has a neighbour in some non-root branch set.  Assign all of
`D` to one such branch set.  Doing this independently for every component
of `G-U` preserves disjointness, connectedness, all old adjacencies, and the
two literal singleton roots, and covers `V(G)`.  \(\square\)

## 3. Atomic rounding

### Theorem 3.1 (atomic weak-immersion rounding)

Let `t>=3`, let `G` be a `t`-connected simple graph, and let `I` be an atomic
weak `K_t` immersion in `G`, with unique collision vertex `x`.

1. If `x` is a non-branch vertex and its two transit paths represent two
   edges of `K_t` with a common end, then `G` contains a `K_t` minor.
2. If `x` is a non-branch vertex and its two transit paths represent
   disjoint edges `ab` and `cd`, then `G` has two spanning near-`K_t` models:
   one is a `K_t-cd` model with singleton deficient roots `v_c,v_d`, and the
   other is a `K_t-ab` model with singleton deficient roots `v_a,v_b`.
3. If `x=v_h` is a branch vertex internal on the foreign path `P_ab`, then
   `G` has a spanning `K_t-ab` model with singleton deficient roots
   `v_a,v_b`.

In items 2 and 3, if the two singleton roots are adjacent in `G`, the
displayed model is already a `K_t` minor.  Thus in a `K_t`-minor-free host
each returned near-clique model is exact.

#### Proof

Atomicity implies that, apart from the displayed collision, path interiors
are mutually disjoint and contain no branch vertex.

First suppose `x` is not a branch vertex and lies internally on `P_ab` and
`P_ac`, where `a` is their common demand endpoint.  Put into the branch set
labelled `a` the vertex `v_a`, the two initial segments from `v_a` to `x`,
and `x` itself.  Put each remaining open segment from `x` to `v_b` or `v_c`
into the branch set at its far endpoint.  Allocate every other path interior
to either endpoint as in Lemma 2.1.  Atomicity makes all the resulting sets
disjoint.  They are connected, and the two edges leaving `x` toward the
open far segments realize the `ab` and `ac` adjacencies.  Every other
adjacency is realized along its own immersion path.  These sets form a
`K_t` minor model, proving item 1.

Now suppose the two paths through the non-branch vertex `x` are `P_ab` and
`P_cd`, where `ab` and `cd` are disjoint.  Omit `P_cd`.  The retained paths
are a subdivision of `K_t-cd`: their interiors are pairwise disjoint and
avoid all branch vertices.  Lemma 2.1 gives a `K_t-cd` model with literal
singleton roots `v_c,v_d`, and Lemma 2.2 makes it spanning without changing
those roots.  Omitting `P_ab` instead gives the symmetric spanning
`K_t-ab` model with singleton roots `v_a,v_b`.  This proves item 2.

Finally suppose `x=v_h` is a branch vertex and occurs internally on
`P_ab`.  Necessarily `h` differs from `a,b`.  Omit `P_ab`.  Because this was
the unique collision, the remaining paths form a subdivision of `K_t-ab`.
Apply Lemmas 2.1 and 2.2 to obtain the asserted spanning model.  This proves
item 3.

If the singleton deficient roots in any returned model are adjacent, that
literal edge supplies the only absent model adjacency and yields a `K_t`
model.  The last assertion follows.  \(\square\)

### Corollary 3.2 (the exact `HC_7` landing point)

Let `G` be seven-connected and `K_7`-minor-free.  Every atomic weak `K_7`
immersion in `G` gives a spanning exact `K_7`-minus-one-edge model whose
deficient branch sets are nonadjacent singleton vertices.  In the
non-branch, disjoint-demand case it gives two such models with disjoint
deficient pairs.

#### Proof

The common-end case of Theorem 3.1 is excluded by the absence of a `K_7`
minor.  Every remaining case gives a spanning near-clique model, and the
last sentence of the theorem makes it exact.  \(\square\)

### Theorem 3.3 (common-frame collision-to-interface theorem)

Take `t=7` in the non-branch, disjoint-demand case of Theorem 3.1, with
collision paths `P_ab,P_cd` meeting at `x` and with remaining branch labels
`e,f,g`.
There is a spanning partition

\[
                    V(G)-\{x\}=D_a\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}D_g                 \tag{3.1}
\]

into nonempty connected sets such that

1. every two sets are adjacent except possibly `D_a,D_b` and `D_c,D_d`;
   and
2. `x` is adjacent to each of `D_a,D_b,D_c,D_d`.

If `G` has no `K_7` minor, then `x` is anticomplete to at least one of the
three clean bags `D_e,D_f,D_g`.  For a component `C` of `G-N[x]` containing
such a bag, the set

\[
                              S=N_G(C)                   \tag{3.2}
\]

satisfies

\[
                 S\subseteq N_G(x),\qquad 7\le |S|\le d_G(x), \tag{3.3}
\]

when `G` is seven-connected.  Both `C` and the singleton `{x}` are adjacent
to every vertex of `S`.

#### Proof

Delete `x`.  Put each of the two open arms of `P_ab` into the seed bag at
its endpoint, and do the same for `P_cd`.  All other route interiors are
mutually disjoint and avoid the branch vertices, so assign each whole
interior to either endpoint.  This gives seven disjoint connected seed
bags.  Every demanded adjacency is retained except possibly `ab` and `cd`,
and the last edge of each collision arm shows that `x` meets the four bags
at `a,b,c,d`.

The graph `G-x` is connected.  Every component outside the seed bags
therefore has an edge to at least one seed bag; absorb it wholesale into one
such bag.  This produces the spanning partition (3.1) and preserves all the
listed properties.

Suppose that `x` also meets `D_e,D_f,D_g`.  The seven sets

\[
 \{x\},\quad D_a\cup D_c,\quad D_b,\quad D_d,\quad
 D_e,\quad D_f,\quad D_g                                  \tag{3.4}
\]

form a `K_7` minor model.  The merged set is connected because `D_a,D_c`
are adjacent.  It meets `D_b` through the retained `cb` adjacency and
`D_d` through the retained `ad` adjacency; these are precisely the two
checks which repair the possible missing pairs.  All other adjacencies
follow from (3.1), and `{x}` meets every other bag by construction and the
supposition.

Thus in a `K_7`-minor-free graph, `x` misses some clean bag, say `D_e`.
That bag lies in `G-N[x]`; let `C` be its component there.  Every neighbour
of `C` outside `C` belongs to `N[x]`.  The vertex `x` has no neighbour in
`C`, so in fact `S=N(C)` is a subset of `N(x)`.  It separates the nonempty
connected set `C` from `x`.  Seven-connectivity now gives `|S|>=7`, while
`S subseteq N(x)` gives the upper bound in (3.3).  By its definition every
vertex of `S` has a neighbour in `C`, and the inclusion in `N(x)` makes the
singleton `{x}` full to `S`.  \(\square\)

### Corollary 3.4 (bounded collision interface)

Under the hypotheses of Theorem 3.3, if `G` is seven-connected,
`K_7`-minor-free, and `d_G(x)<=9`, then the atomic collision produces an
actual full separation of order seven, eight, or nine, with the singleton
`{x}` on one open side and one clean immersion bag contained in the other.

If in addition `G` is seven-chromatic and every proper minor of `G` is
six-colourable, then for every nonempty independent set `I` of `G[S]`,
each closed shore has a proper six-colouring in which `I` is one exact
boundary colour block.  In a hypothetical minor-minimal counterexample to
`HC_7`, the audited
[low-degree adjacent-pair theorem](hc7_low_degree_adjacent_pair_alignment.md)
records the same full-interface geometry.  The atomic argument does not
select the named boundary edge used by the stronger response alignment,
and the immersion theorem does not force `d_G(x)<=9`.

#### Proof

Apply Theorem 3.3.  Its bounds give `7<=|S|<=d_G(x)<=9`, and its last
sentence gives the two full connected subgraphs.

For the response on `G[C union S]`, contract the connected set `{x} union I`
and six-colour the resulting proper minor.  Expand every member of `I` with
the contracted vertex's colour and restrict to `C union S`.  Independence
of `I` makes the expansion proper, while the adjacency from `x` to every
vertex of `S-I` makes the block exact.

For the response on `G-C`, contract the connected set `C union I` instead.
Fullness of `C` makes the contracted vertex adjacent to every vertex of
`S-I`.  Expanding `I` and restricting to `G-C` again gives a proper
six-colouring with `I` as one exact boundary block.  These arguments use
exactly the hypothesis that every proper minor of `G` is six-colourable;
they do not require the collision vertex to be the specially selected pole
in the cited theorem.
\(\square\)

### Theorem 3.5 (paired linkage inside the missed clean bag)

Retain the partition in Theorem 3.3 and suppose that `x` meets `D_f,D_g`
but misses `D_e`.  Suppose `D_e` contains disjoint connected sets `L_ab`
and `L_cd` such that

\[
 \begin{aligned}
 L_{ab}&\text{ is adjacent to both }D_a\text{ and }D_b,\\
 L_{cd}&\text{ is adjacent to both }D_c\text{ and }D_d.
 \end{aligned}                                             \tag{3.5}
\]

Then `G` contains a `K_7` minor.  Consequently, in a `K_7`-minor-free host
the missed clean bag has no such paired linkage.

#### Proof

Use the seven branch sets

\[
 \{x\},\quad D_a\cup L_{ab},\quad D_b,\quad
 D_c\cup L_{cd},\quad D_d,\quad D_f,\quad D_g.           \tag{3.6}
\]

They are nonempty, connected and pairwise disjoint.  The two added
connected sets give the only two adjacencies not already guaranteed by
Theorem 3.3, namely the second--third and fourth--fifth pairs.  The
singleton `{x}` sees the four collision-arm bags by Theorem 3.3 and sees
`D_f,D_g` by hypothesis.  Every other pair is adjacent in the original
spanning partition.  Thus (3.6) is an explicit `K_7` model.  \(\square\)

This is the extra local problem exposed by retaining the atomic route
provenance.  Failure of (3.5) is a genuine two-disjoint-path obstruction
inside one named connected bag.  Turning that obstruction into a smaller
response-preserving interface or a canonical planar structure remains a
separate theorem; merely renaming it as a branch-set allocation does not
close the atomic gate.

### Corollary 3.6 (the residual octahedral frame)

Under the hypotheses of Theorem 3.5, if `G` has no `K_7` minor, then
`D_a` is anticomplete to `D_b` and `D_c` is anticomplete to `D_d`.
Consequently the bag-adjacency graph on

\[
                       \{x\},D_e,D_a,D_b,D_c,D_d
\]

is exactly `K_{2,2,2}`, with nonedges
`\{x,D_e\},\{D_a,D_b\},\{D_c,D_d\}`.

#### Proof

If `D_a` and `D_b` were adjacent, then

\[
 \{x\},\quad D_a,\quad D_b,\quad D_c\cup D_e,\quad
 D_d,\quad D_f,\quad D_g
\]

would form a `K_7` model.  The union `D_c\cup D_e` is connected, its
adjacency to `D_d` is supplied by `D_e`, and `{x}` meets it through
`D_c`; all other adjacencies follow from Theorem 3.3.  This is impossible.
Interchanging the pairs `ab` and `cd` gives the second anticompleteness
claim, using `D_a\cup D_e` to repair the missing `ab` adjacency.  Theorem
3.3 supplies every other edge in the displayed bag-adjacency graph, while
`x` misses `D_e` by hypothesis.  \(\square\)

### Proposition 3.7 (contact-preserving singletonization)

Retain a spanning provenance partition constructed in the proof of Theorem
3.3 and satisfying the hypotheses of Theorem 3.5: `x` misses `D_e` and
meets `D_f,D_g`.  There is another spanning common-frame partition
`D'_a,...,D'_g` such that `x` still meets `D'_f,D'_g` and

\[
                              D'_e=\{v_e\}.               \tag{3.7}
\]

Consequently Theorem 3.5 is not forced by connectivity: obtaining a useful
nontrivial missed bag requires a deliberate ownership choice for vertices
outside the route skeleton.

#### Proof

Choose an `x`-neighbour `y_f` in `D_f` and a path `Q_f` in `G[D_f]` from
`v_f` to `y_f`.  Define `y_g,Q_g` symmetrically.  The two paths are disjoint
because `D_f,D_g` are disjoint.

Rebuild the route seed bags in `G-x`.  Keep `Q_f` in the `f`-seed and `Q_g`
in the `g`-seed.  Assign every internal vertex of every route incident with
`v_e` to its other endpoint.  If another route interior meets `Q_f` or
`Q_g`, assign that entire interior to `f` or `g`, respectively; this is
consistent because the original provenance partition places a route
interior in an endpoint bag.  Assign every remaining route interior to
either endpoint, and put the four collision arms into their endpoint bags
as in Theorem 3.3.

The seven resulting seeds are disjoint and connected, preserve every
common-frame adjacency, leave the `e`-seed equal to `{v_e}`, and retain the
edges `xy_f,xy_g` to the `f`- and `g`-seeds.

Let `R` be a component of `(G-x)` minus the union of the seven seed
bags.  Its neighbourhood in `G` has order at least seven: otherwise that
neighbourhood separates `R` from one of the seven branch vertices.  At
most two of those neighbours are `x` and `v_e`, so `R` has a neighbour
in a seed bag with label different from `e`.  Absorb `R` into such a bag.
Repeating this for every such component gives the required spanning
partition, leaves (3.7) unchanged, and preserves the two selected `x`
contacts.  Since the old `D_e` was anticomplete to `x`, the edge `xv_e`
is absent, so `x` misses `D'_e`.
\(\square\)

Proposition 3.7 is the impact gate for Theorem 3.5.  The paired-linkage
formulation is useful only if a new label-preserving optimization proves
that outside material can be assigned to `D_e` so as to create (3.5), or
turns the failure of every such assignment into the required strict
response-preserving reduction.  Without that theorem, the formulation has
only renamed the global allocation problem.

## 4. Impact on the weak-immersion programme

DeVos, Kawarabayashi, Mohar and Okamura prove in Theorem 3 of
[*Immersing small complete graphs*](https://users.fmf.uni-lj.si/mohar/Reprints/Inprint/BM08_Preprint_DeVos_ImmersingSmallCompleteGraphs.pdf)
(*Ars Mathematica Contemporanea* 3 (2010), 139--146,
doi:10.26493/1855-3974.112.b74) that every simple graph of minimum degree at
least six has a weak `K_7` immersion.  A seven-connected graph satisfies
that degree hypothesis.
Indeed, after deleting any prescribed vertex `u`, the remaining graph still
has minimum degree at least six, so the published theorem supplies an
immersion avoiding `u`.

The source theorem does not prescribe its branch vertices, make the
immersion strong, or bound the number or load of collision vertices.  For
an immersion `I`, put

\[
 \begin{aligned}
 M(I)&=\sum_x\max\{0,r(x)-1\},\\
 T(I)&=\sum_{i=1}^7
   |\{jk:v_i\text{ is internal on }P_{jk}\}|,\\
 Q(I)&=|\{x:r(x)>=2\}|,\\
 H(I)&=M(I)-Q(I)=\sum_x\max\{0,r(x)-2\},\\
 L(I)&=\sum_{ij}|E(P_{ij})|.
 \end{aligned}                                             \tag{4.1}
\]

The candidate well-founded bookkeeping potential is `(M,T,H,L)` in
lexicographic order.  The concentration coordinate `H` distinguishes a
high-load hub from the same excess distributed among binary collisions;
using `Q` itself as an ascending tie-break would prefer the hub.  Atomicity
is exactly `M=1`.  Theorem 3.1 normalizes that value to the near-clique and
interface gates; it does not establish one of the terminal outcomes in the
persistent goal, nor prove that the minimum possible `M` is at most one.  A
global collision-descent theorem would still be required to reach this
atomic gate from an arbitrary guaranteed immersion.

At the two ends of this potential, `M=0` is already decisive: the routes
then form a subdivision of `K_7`, and hence a `K_7` minor.  At `M=1`,
however, minimizing excess alone does not control the collision degree.
Mader's extremal bound for `K_7`-minor-free graphs gives
`2|E(G)|<=10|V(G)|-30`.  Together with minimum degree seven it implies
that at least ten vertices have degree at most nine: if `L` is their set,
then

\[
 10|V(G)|-3|L|\le 2|E(G)|\le10|V(G)|-30,
 \qquad\text{so}\qquad |L|\ge10.                         \tag{4.2}
\]

No proved incidence relation puts an atomic collision on this low-degree
set.  In fact, applying the published immersion theorem after deleting a
prescribed low-degree vertex produces an immersion avoiding that vertex,
not one anchored there.  The high-degree branch-transit witness in the
companion guardrail further shows that an `M=1` minimizer need not itself
collide at low degree, although its positive `T` leaves open the full
lexicographic tie-break.

The extremal input is the `p=7` case of W. Mader,
[*Homomorphiesätze für Graphen*](https://eudml.org/doc/161741),
Math. Ann. **178** (1968), 154--168, DOI `10.1007/BF01350657`: a simple
`K_7`-minor-free graph on `n>=7` vertices has at most `5n-15` edges.

At the local end, Corollary 3.2 lands exactly in the frozen
[singleton-root completion-or-separation programme](../active/hc7_two_root_colouring_space_frontier.md).
If one forgets the nearly topological route system and keeps only the
spanning near-clique model, no new completion mechanism has been obtained.
In the disjoint-demand case, the genuinely additional datum is the pair of
opposite near-clique models supported by the same edge-disjoint route
system, the full interface of Theorem 3.3, and the exact octahedral residual
frame of Corollary 3.6.  The accompanying icosahedral guardrail shows that
even this exact atomic configuration can occur sharply in a seven-connected
`K_7`-minor-free graph, and that avoiding the old collision may merely move
it without lowering `(M,T,H,L)`.  Proposition 3.7 also shows that an
arbitrary paired-linkage demand inside the missed bag is not intrinsic: the
same route provenance can be reallocated while preserving the two useful
`x` contacts and making that bag a singleton.

Thus the next valid gate is not another reformulation of the near-clique
model.  It must either

1. use the retained redundant route capacity together with proper-minor
   colouring responses in a label-preserving extremal allocation to force
   completion or an order-seven separation; or
2. give a well-founded collision reduction which works before the atomic
   case is reached.
