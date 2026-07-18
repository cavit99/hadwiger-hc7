# Exact matching languages and disjoint Kempe bridges at degree seven

**Status:** written proof; separate internal audit GREEN.  This is a conditional
theorem for the sole-exterior, degree-seven branch of the bounded-interface
programme.  It does not prove `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph with `chi(G)=7`, no `K_7` minor, and
every proper minor six-colourable.  Let `u` have degree seven and suppose

\[
                       G-N[u]=C
\]

is nonempty and connected.  Put

\[
 S=N(u),\qquad H=G[S],\qquad F=\overline H,
 \qquad A=G[C\cup S],\qquad B=G[N[u]].                 \tag{1.1}
\]

Dirac's contraction-critical neighbourhood inequality gives
`alpha(H)<=2`.  Thus every independent block of a proper colouring of
`H` has order at most two.  Equality partitions of `S` are consequently
encoded by matchings of `F`: every matching edge is one two-vertex colour
block and every unmatched vertex is a singleton block.

The audited bounded-interface theorem also gives `chi(H)<=4`; this input
is used only in Corollary 3.2 to guarantee a matching of order three.

For a closed shore `Y` containing `S`, let `M(Y)` be the matchings of `F`
whose corresponding equality partition is induced by a proper
six-colouring of `Y`.

## 2. Exact language collapse

### Theorem 2.1

Under the setup above,

\[
 \boxed{
 M(A)=\{\{e\}:e\in E(F)\},\qquad
 M(B)=\{M\subseteq E(F):M\text{ is a matching and }|M|\ge2\}.}
                                                               \tag{2.1}
\]

In particular, the two extension languages are separated exactly by
matching size, not merely by an unspecified boundary-colouring state.

### Proof

A proper six-colouring of `B=G[N[u]]` gives `u` a colour absent from
`S`, because `u` is complete to `S`.  Hence at most five colour blocks
occur on `S`.  Conversely, every proper equality partition of `H` with at
most five blocks extends to `B` by assigning its blocks distinct colours
and giving `u` a fresh sixth colour.  A matching `M` encodes `7-|M|`
blocks, proving the asserted description of `M(B)`.

The graph `A=G-u` is a proper minor and is six-colourable.  Every boundary
partition arising from such a colouring has at most six blocks, so its
matching is nonempty.  If it had at least two edges, the same partition
would belong to `M(B)`.  Permuting one palette to agree on the common
boundary partition and gluing the two closed-shore colourings would
six-colour `G`, a contradiction.  Thus every member of `M(A)` has exactly
one edge.

It remains to show that every edge `ab` of `F` occurs.  Contract the
connected star `G[{u,a,b}]` to one vertex.  In a six-colouring of this
proper minor, expand `a,b` with the colour of the contracted vertex and
restrict to `A`.  Every member of `S-{a,b}` was adjacent to `u`, so none
has that colour.  Thus `{a,b}` is an exact boundary block.  The preceding
paragraph excludes every additional two-vertex block, and the induced
matching is exactly `{ab}`.  This proves (2.1).  \(\square\)

## 3. Simultaneous failed lifts are a disjoint path bundle

### Theorem 3.1 (matching-augmentation bridge bundle)

Let

\[
                    M=\{e_0,e_1,\ldots,e_r\}             \tag{3.1}
\]

be a matching of `F`, where `r>=1`.  There is a proper six-colouring `c`
of `A` whose sole nonsingleton boundary block is `e_0`, and, for every
`i=1,...,r`, there is a path `P_i` joining the ends of `e_i` such that

1. every internal vertex of `P_i` lies in `C`;
2. `P_i` is bichromatic in `c`, using precisely the two colours on the
   ends of `e_i`; and
3. the paths `P_1,...,P_r` are pairwise vertex-disjoint.

Equivalently, every independent matching augmentation of the one-edge
state `{e_0}` fails to lift through `A` in a different pair of colours,
and the failed lifts coexist as disjoint literal paths in the same
colouring.

### Proof

Theorem 2.1 supplies `c` with sole boundary pair `e_0`.  Its other five
boundary vertices have five distinct colours, all different from the
colour on `e_0`.

Fix `e_i=p_iq_i`, and write the colours of its ends as `alpha_i,beta_i`.
They are distinct, and `p_iq_i` is absent from `H`.  On the boundary, the
`alpha_i`--`beta_i` graph therefore has the two singleton components
`{p_i}` and `{q_i}`.  If these two vertices lay in different components of
`A[alpha_i,beta_i]`, interchange the two colours on the component
containing `p_i`.  The resulting colouring of `A` would have boundary
matching `{e_0,e_i}`, contrary to Theorem 2.1.  Hence they lie in one
component.  A shortest path between them in that component has no internal
boundary vertex, because no other boundary vertex uses either colour.
This is `P_i`.

For distinct `i,j`, the four ends of `e_i,e_j` are distinct singleton
blocks of `c`; hence the two colour pairs
`{alpha_i,beta_i}` and `{alpha_j,beta_j}` are disjoint.  The corresponding
two induced bichromatic subgraphs have disjoint vertex sets.  Therefore
the chosen paths are pairwise vertex-disjoint.  \(\square\)

### Corollary 3.2 (two simultaneous bridges)

Since `chi(H)<=4`, the complement `F` has a matching of order three.
Consequently there are three disjoint nonedges `e_0,e_1,e_2` of `H` and
two vertex-disjoint paths through `C` joining the ends of `e_1,e_2`, in
one proper six-colouring whose only repeated boundary pair is `e_0`.

### Proof

A proper four-colouring of the seven-vertex graph `H` partitions `S` into
at most four independent blocks.  Since every block has order at most two,
at least three blocks have order two.  They are a matching of order three
in `F`.  Apply Theorem 3.1.  \(\square\)

### Corollary 3.3 (the full colour-indexed path system)

Fix `e_0 in E(F)` and a colouring `c` supplied by Theorem 2.1.  For every
edge `pq` of `F-V(e_0)`, choose a shortest `p-q` path in the two-colour
component of `A` determined by the colours of `p,q`.  All its internal
vertices lie in `C`.  Moreover, paths belonging to vertex-disjoint edges
of `F-V(e_0)` are vertex-disjoint.

### Proof

The one-edge matching `{e_0}` can be augmented by any edge of
`F-V(e_0)`, so the proof of Theorem 3.1 supplies every asserted path in
the same fixed colouring.  Vertex-disjoint complement edges have four
different singleton colours, and hence their two bichromatic subgraphs are
disjoint.  \(\square\)

Thus the exterior does not merely contain two arbitrarily selected paths:
for each repeated pair it contains a colour-indexed realization of the
entire missing-edge graph on the other five roots, with disjointness on
every matching.  This is the precise matching form of the external-path
system used in rooted-minor arguments.

### Corollary 3.4 (disjoint pair or concentrated star)

Fix `e_0` and put `U=S-V(e_0)`.  If `F[U]` has at least four edges, then
exactly one of the following useful alternatives is present.

1. `F[U]` contains two vertex-disjoint edges, and Corollary 3.3 gives the
   corresponding two vertex-disjoint paths through `C` in one colouring.
2. All edges of `F[U]` have one common end `w`.  In particular, because
   `|U|=5`, at least four edges force `F[U]` to be the spanning star
   `K_{1,4}`; the other four vertices induce a `K_4` in `H`, and the fixed
   colouring gives four `w`-to-leaf bichromatic paths through `C`.

### Proof

If a graph has matching number at most one, any two of its edges meet.
A pairwise-intersecting family of two-element sets is either a star or the
three edges of a triangle.  The latter is impossible because `F` is
triangle-free.  Hence failure of outcome 1 makes `F[U]` a star.  Four
distinct edges on the five-vertex set `U` use all four possible leaves,
giving outcome 2.  The path assertions follow from Corollary 3.3.
\(\square\)

This dichotomy identifies the two geometric obstructions rather than
creating further matching cases.  The disjoint-pair branch needs a
label-preserving split of two paths; the star branch has a literal boundary
`K_4` and needs one connected subgraph of `C` reserved from the star paths.
Neither reservation follows from matching data alone.

### Theorem 3.5 (uniform rooted `K_5` or a full model separator)

Fix any edge `e_0=ab` of `F` and put `U=S-{a,b}`.  Then either `G`
contains a `K_7` minor, or there are

* a `U`-rooted `K_5` model `(B_x:x in U)` in `A-{a,b}`; and
* an inclusion-minimal `a-b` separator

  \[
                         Z\subseteq\bigcup_{x\in U}B_x,
                         \qquad |Z|\ge6,               \tag{3.3}
  \]

  such that the components of `A-Z` containing `a` and `b` are both
  adjacent to every vertex of `Z`.

Some rooted branch set contains at least two vertices of `Z`.
Furthermore, `Z union {u}` is an actual separation boundary in `G` of
order `|Z|+1>=7`, and both distinguished open sides are adjacent to every
vertex of that boundary.

### Proof

Take the exact one-edge colouring for `e_0` from Theorem 2.1.  The five
roots in `U` have five distinct colours.  By Corollary 3.3, for every edge
of the missing-edge graph `F[U]`, its two roots lie in one bichromatic
component, and all those components avoid `a,b`.

The graph `F[U]` is triangle-free, so Mantel's theorem gives

\[
                              |E(F[U])|\le6.             \tag{3.4}
\]

Let `A'` be the subgraph of `A` induced by the five colour classes meeting
`U`; equivalently, delete the sixth colour class containing `a,b`.  The
restriction of the fixed colouring to `A'` has exactly five colour classes,
and `U` is a transversal of them.  Every bichromatic path used above has
both colours represented in `U`, so it survives in `A'`.

Kriesell--Mohr's Theorem 7 says that every graph on five vertices with at
most six edges has the required Kempe-chain packaging property.  Applied
to `F[U]` in the five-coloured graph `A'`, it gives an `F[U]`-rooted
certificate.  The missing root adjacencies are supplied by those
bichromatic components, while every complementary root pair is a literal
edge of `H[U]`.  Together these adjacencies make the five connected bags a
`U`-rooted `K_5` model in `A-{a,b}`.

Finally, `{a,b}` jointly dominates `U`.  Otherwise some `x in U` would
make `{a,b,x}` an independent set of `H`, contradicting `alpha(H)<=2`.
All hypotheses of the independently audited
[rooted-`K_5` connector-or-separator theorem](../results/hc7_exact7_rooted_k5_connector_separator.md)
are now satisfied, with its vertex `v` equal to `u` and its graph `G-v`
equal to `A`.  That theorem gives either
an explicit `K_7` model, or precisely the separator and fullness assertions
in (3.3).  Six separator vertices distributed among five disjoint rooted
branch sets force one branch set to contain at least two of them.

Since `A=G-u`, deleting `Z union {u}` from `G` leaves the two distinguished
components separated.  Each is adjacent to all of `Z`; the first contains
`a` and the second contains `b`, so both are also adjacent to `u`.  This
proves the final actual-separation assertion.
\(\square\)

Theorem 3.5 is the reusable alternating-path conclusion at degree seven.
Two paths alone do not force a minor, but the entire matching-indexed system
packages into a rooted model and turns failure of a reserved `a-b`
connector into a literal full separator inside five named branch sets.

### Corollary 3.6 (exact order seven or seven-fold linkage)

For every `ab in E(F)`, one of the following holds:

1. `G` contains a `K_7` minor;
2. `G` has an actual order-seven separation whose two distinguished open
   sides are both adjacent to all seven separator vertices; or
3. `A` contains seven internally vertex-disjoint `a-b` paths, and every
   such path meets the rooted `K_5` union from Theorem 3.5.

### Proof

The graph `A=G-u` is six-connected.  If the minimum order of an `a-b`
separator in `A` is six, choose an inclusion-minimal separator `Q` of that
order.  The standard minimal-separator argument makes the components of
`A-Q` containing `a,b` adjacent to every member of `Q`.  Then
`Q union {u}` is an order-seven separator in `G`, and the two components
are also adjacent to `u` through `a,b`, respectively.  This is outcome 2.

If the minimum order is at least seven, Menger's theorem gives seven
internally vertex-disjoint `a-b` paths in `A`.  In the non-`K_7` outcome
of Theorem 3.5, its rooted-model union separates `a,b`, so every one of
these paths meets it.  This is outcome 3.  \(\square\)

Thus the separator obstruction is exact: after excluding an order-seven
boundary, the remaining branch is not merely a large separator but a
seven-fold linkage through five named rooted branch sets.  Any further
bag split may start from the guaranteed fact that at least one of the five
bags meets at least two linkage paths.  More sharply, after assigning each
path to one bag that it meets, either one bag receives at least three paths
or two bags receive at least two paths each.

## 4. Proper-minor dynamics in the same matching language

The exact language collapse also converts contraction-criticality into a
sharp internal-edge transition.

### Proposition 4.1

Let `h=vw` be an edge of `G[C]`.  Every proper six-colouring of `G-h`
makes `v,w` monochromatic, and its boundary matching on `S` has order two
or three.  A six-colouring of `G/h`, expanded to `G-h`, has the same two
properties.  Likewise, for every `v in C`, every six-colouring of `G-v`
induces on `S` a matching of order two or three.

### Proof

The opposite closed shore `B` is unchanged by each displayed operation.
The restriction of the proper-minor colouring to `B` is therefore a proper
six-colouring of `B`, so Theorem 2.1 says that its boundary matching has
order at least two (and at most three on seven vertices).

If a colouring of `G-h` gave `v,w` different colours, restoring `h` would
six-colour `G`.  Thus they are monochromatic.  Expanding the contracted
vertex in a colouring of `G/h` gives precisely such a colouring of `G-h`.
The vertex-deletion assertion follows by the same unchanged-shore
restriction.  \(\square\)

Consequently `A` is a boundary-minor-critical realizer of the one-edge
matching language: every internal deletion or contraction returns a
matching of order at least two, while the unmodified shore returns only
one-edge matchings.  This is the host-level information absent from an
abstract pair of disjoint partition languages.

The path conclusion of Theorem 3.1 is consistent with, and may also be
viewed as a specialization of, the standard Rolek--Song external-path
lemma in the equality case `d(u)=7`, `alpha(N(u))=2`.  The additional
content here is the exact classification (2.1) of both closed-shore
languages and the resulting internal proper-minor transition in
Proposition 4.1.  No novelty claim should be based on path existence alone.

## 5. A rigorous minor-model exit

The two paths can safely be treated as subdivisions of their two matching
edges, but no other part of `C` may simultaneously be treated as a branch
set without an explicit disjointness argument.

### Corollary 5.1

Use the notation of Corollary 3.2.  If

\[
                         H+e_1+e_2
\]

contains a `K_6` minor, then `G` contains a `K_7` minor.

### Proof

Replace the two added edges by the internally disjoint paths `P_1,P_2`.
Subdividing edges does not destroy a clique minor: whenever a subdivided
edge was used inside one branch set, add the corresponding path to that
branch set; whenever it supplied an edge between two branch sets, divide
the path at one of its edges between those two sets.  The two replacements
are compatible because their paths are internally disjoint and have four
distinct ends.

This gives a `K_6` model in `H union P_1 union P_2` in which every branch
set contains a vertex of `S`, because the original model lived in the
seven-vertex graph `H+e_1+e_2`.  The singleton `{u}` is adjacent to every
branch set and completes the model to a `K_7` model in `G`.  \(\square\)

Thus a hypothetical counterexample must satisfy the finite but structural
condition

\[
 H+(M-\{e\})\text{ is }K_6\text{-minor-free}            \tag{5.1}
\]

for every order-three matching `M` of `F` and every `e in M`.

## 6. Exact remaining obstruction

Theorem 3.1 is stronger than two independently selected Kempe paths: it
puts both failed lifts in one colouring and makes them disjoint by colour.
It still does not by itself produce a strict host descent.  In the remaining
case (5.1), an attempted proof must use how the rest of `C` attaches to
the two paths.  Connectivity of `C`, boundary fullness, and the abstract
matching data do not justify reserving a third connected subgraph after
the two paths have been allocated.

The next valid exchange statement must therefore prove one of the
following from literal first attachments to `P_1 union P_2`:

1. a split of the two paths and their attached components that supplies
   the missing adjacencies of a `K_6` model;
2. a connected component with full neighbourhood of order seven and
   strictly smaller order than `C`; or
3. a boundary matching of order at least two extending through `A`, which
   is immediately a common partition by Theorem 2.1.

Merely obtaining another pair of paths is no progress: Theorem 3.1 already
supplies the maximum possible pair of disjoint paths on the six vertices
outside the unmatched boundary vertex.

The existing [essential-portal counterexample](../barriers/hc7_sole_exterior_reserved_connector_barrier.md)
shows why a shore-local reserved-connector assertion cannot be used for the
last step, even under strong internal connectivity and local minor
exclusion.  A valid completion has to spend Proposition 4.1's proper-minor
response or the global `K_7`-minor exclusion with the literal boundary
labels.

## 7. What failure of a reserved connector actually returns

The following elementary accounting is the strongest unconditional
separator conclusion available from seven-connectivity.  It applies to a
vertex-minimal Steiner tree containing the selected path interiors, but is
stated for an arbitrary connected subgraph so that no hidden minimality is
used.

### Proposition 7.1 (defect--attachment trichotomy)

Let `Z` be a nonempty connected subgraph of `C`.  For every component `R`
of `C-Z`, put

\[
 d(R)=|S-N_S(R)|,\qquad a(R)=|N_Z(R)|.                \tag{7.1}
\]

Then one of the following occurs.

1. Some `R` is `S`-full (`d(R)=0`), and is a connected subgraph reserved
   from `Z`.
2. Some nonfull `R` satisfies `a(R)=d(R)`.  Its full neighbourhood is

   \[
              N_G(R)=N_S(R)\mathbin{\dot\cup}N_Z(R)  \tag{7.2}
   \]

   and has order exactly seven, so it is an actual order-seven separation
   with `|R|<|C|`.
3. Every component `R` is nonfull and has strict attachment surplus

   \[
                            a(R)\ge d(R)+1.            \tag{7.3}
   \]

### Proof

There are no edges from `C` to `V(G)-(C\cup S)`, and a component of
`C-Z` has no neighbour in another such component.  This proves (7.2).
If `R` is nonfull, its complement contains `u`, so seven-connectivity gives

\[
 7\le |N_G(R)|=(7-d(R))+a(R),
\]

or `a(R)>=d(R)`.  Equality is outcome 2; strict inequality for every
nonfull component is outcome 3.  The remaining possibility is outcome 1.
\(\square\)

If `Z` is chosen as a vertex-minimal tree spanning the internal vertices
needed by the two disjoint paths (or by the four arms of the star in
Corollary 3.4), Proposition 7.1 makes the obstruction precise.  Failure of
both a reserved connected subgraph and an order-seven separator is not an
unstructured remainder: every component behind the tree has at least one
more tree attachment than the number of boundary labels it misses.

In addition, Proposition 4.1 applies to every edge of this tree: deletion
or contraction of that edge produces a boundary matching of order at least
two.  Thus the live atomic obstruction is exactly

\[
 \boxed{
 \begin{array}{c}
   a(R)\ge d(R)+1\text{ for every component }R\text{ of }C-Z,\\
   \text{and every tree edge has a proper-minor response of matching
   order at least two.}
 \end{array}}                                             \tag{7.4}
\]

The missing theorem has to couple one response in the second line to the
literal surplus attachments in the first.  Neither line alone gives a
well-founded reduction; in particular, (7.3) permits arbitrarily long
trees with concentrated boundary contacts.

## 8. Dependencies and citation boundary

The proof uses the following promoted repository inputs.

* The [bounded low-degree interface theorem](../results/hc7_low_degree_adjacent_pair_alignment.md)
  supplies `alpha(H)<=2` and `chi(H)<=4` in the present setting.
* The [rooted-`K_5` connector-or-separator theorem](../results/hc7_exact7_rooted_k5_connector_separator.md)
  is invoked exactly once, in Theorem 3.5.

The external rooted-minor input is M. Kriesell and S. Mohr,
[*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
Theorem 7: every graph on five vertices with at most six edges has property
`(*)`.  Theorem 3.5 applies it only after verifying the five distinct root
colours and every required bichromatic connection in one fixed colouring.

Mantel's theorem is used only for the elementary bound that a triangle-free
five-vertex graph has at most six edges.  Menger's theorem is used only in
Corollary 3.6 to turn local `a-b` connectivity at least seven into seven
internally vertex-disjoint paths.  No unquoted linkedness, rooted-clique, or
nonseparating-minor theorem is assumed.

The existence portion of Theorem 3.1 agrees with the external-path lemma
recorded as Lemma 2.4 of M. Lafferty and Z.-X. Song,
[*Every graph with no `K_8^{-4}` minor is 7-colorable*](https://arxiv.org/abs/2208.07338).
The proof here is included because the exact matching-language collapse
also gives the simultaneous disjointness directly; that cited lemma is not
a logical dependency.
