# The `2K3+K1` boundary: rooted triangles and the pendant-portal lock

## 1. Setting

Let `G` be seven-connected and `K7`-minor-free.  Let

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}\{c\},\qquad
 |A|=|B|=3,
\]

and suppose

\[
 G[S]=K_1\vee K_{3,3};
\]

thus the missing-edge graph on `S` is `2K3+K1`, with the two triangles
on `A` and `B`.  Suppose `G-S` has exactly two connected components
`D_1,D_2`, each with neighbourhood exactly `S`.

For `T` equal to `A` or `B`, a **`T`-rooted triangle in `D`** means
three pairwise adjacent, pairwise disjoint connected sets in `G[D union T]`,
each containing a different member of `T`.

### Lemma 1.1 (neither full shore is a singleton)

In the counterexample-derived setting, `|D_1|,|D_2|>=2`.

### Proof

Suppose `D_1={h}`.  Contract the connected set `D_1 union A` to one
vertex.  The resulting proper minor has a six-colouring.  Expanding the
contracted image back over `A` gives a six-colouring of `G-h` in which
the three vertices of `A` form one exact colour block.  At most five
colours consequently occur on the seven vertices of `S`.  Since `h`
has no neighbours outside `S`, give it a sixth colour absent from `S`.
This six-colours `G`, a contradiction.  The other shore is symmetric.

## 2. The elementary rooted-triangle criterion

### Lemma 2.1

Let `H` be connected and let `x_1,x_2,x_3` be distinct vertices.  If
`H` has no `K3`-model rooted at these three vertices, then `H` has a
separation of order at most one with roots on both open sides.

### Proof

Use the block-cutvertex tree of `H`.  If no cutvertex separates the
three roots, they lie in a common nontrivial 2-connected block.  A
2-connected graph has a rooted `K3` at any prescribed three vertices.
Take a cycle through two roots.  If the third root lies on the cycle,
split the cycle into three nonempty rooted arcs; otherwise take a
two-fan from the third root to two distinct points of the cycle and
split the resulting theta subgraph into three rooted branch sets.
Hence, in the absence of the rooted model, an
edge of the minimal block-cutvertex subtree joining the three roots
gives the asserted separation.  (A bridge block cannot contain three
distinct roots.)

## 3. Unique-portal consequence of seven-connectivity

### Lemma 3.1

Let `D` be either full shore and let `T` be `A` or `B`.  If `D` has no
`T`-rooted triangle, then some `t in T` has exactly one neighbour in
`D`.

### Proof

Apply Lemma 2.1 to the connected graph `H=G[D union T]`.  The separating
set cannot be empty.  Let its vertex be `z`, and choose a component `K`
of `H-z` containing exactly one root `t` (among three roots distributed
over at least two open sides, such a component exists).

Put `X=K intersect D`.  If `X` is nonempty, then `z` must lie in `D`:
if `z` were a root, the connected set `D` would remain in one component
of `H-z`, and all other roots, each having a neighbour in `D`, would lie
in that same component.  Moreover

\[
 N_D(X)\subseteq\{z\},\qquad N_T(X)\subseteq\{t\}.
\]

The four vertices of `S-T` are the only other possible boundary
neighbours.  Distinct components of `G-S` are anticomplete, so

\[
 N_G(X)\subseteq\{z,t\}\cup(S-T),
 \qquad |N_G(X)|\le6.
\]

This separates the nonempty set `X` from the opposite shore, contrary
to seven-connectivity.  Therefore `X` is empty.  The component `K` is
the singleton root `t`, so all its neighbours in `D` consist of the
single vertex `z`.

### Corollary 3.2

If every member of `T` has at least two neighbours in `D`, then `D`
contains a `T`-rooted triangle.

## 4. Opposite rooted triangles close the boundary

### Lemma 4.1

If `D_1` contains an `A`-rooted triangle and `D_2` contains a
`B`-rooted triangle (or conversely), then `G` contains a `K7` minor.

### Proof

Use the six rooted triangle bags and the singleton bag `{c}`.  Bags
rooted in the same triple are pairwise adjacent by definition.  Every
`A`-rooted bag is adjacent to every `B`-rooted bag through the complete
bipartite boundary `G[A,B]`, and `{c}` sees every rooted bag.

## 5. Exact form of a failed rooted triangle

Fix a shore `D`, a triple `T={t,t',t''}`, and let `U=S-T`.  Suppose
`t` has the unique neighbour `z` in `D`, as supplied by Lemma 3.1.

### Lemma 5.1 (all components beyond the portal are full)

Every component `R` of `D-z` has neighbourhood containing all six
vertices of `S-{t}`.

### Proof

The connectedness of `D` makes `z` adjacent to `R`.  The set
`N_G(R)` separates `R` from the opposite shore.  Since `t` has no
neighbour in `R`,

\[
 N_G(R)\subseteq\{z\}\cup(S-\{t\}).
\]

Seven-connectivity forces equality, proving the assertion.

### Lemma 5.2 (branching at the portal gives `K7`)

The graph `D-z` has at most one component.

### Proof

Suppose it has distinct components `X,Y`.  Write

\[
 T=\{t,t',t''\},\qquad U-\{c\}=\{u,u',u''\},
\]

where the latter set is the other independent triple, and let `D'` be
the opposite full shore.  By Lemma 5.1, both `X` and `Y` are full to
`S-{t}`.  The following seven bags form a `K7` model:

\[
 \{t\},\quad \{u\},\quad \{c\},\quad D',\quad
 \{t',u'\},\quad X\cup\{u''\},\quad
 Y\cup\{z,t''\}.                                      \tag{5.1}
\]

The last bag is connected because `Y` sees `t''` and `z` sees `Y`;
the sixth is connected because `X` sees `u''`.  The first and last
bags are adjacent through `tz`.  All remaining nontrivial adjacencies
follow either from fullness of `X,Y,D'` or from the complete bipartite
graph between the two triples.  This checks all 21 bag pairs.

### Lemma 5.3 (a nontrivial portal has no second contact in its triple)

If `D-z` is nonempty, then `z` is adjacent to neither `t'` nor `t''`.

### Proof

Let `R=D-z`, which is connected by Lemma 5.2 and nonempty by hypothesis.
Suppose, by symmetry, that `zt'` is an edge.  With the
notation of Lemma 5.2, the bags

\[
 \{t\},\quad \{u\},\quad \{c\},\quad D',\quad
 \{t'',u'\},\quad R\cup\{u''\},\quad \{z,t'\}          \tag{5.2}
\]

form a `K7` model.  Connectivity is clear.  The last bag sees `{t}`
through `zt`, the fifth and sixth through the complete bipartite
boundary, and the other bags through their boundary roots.  The shore
bag containing `R` is full to `S-{t}` by Lemma 5.1.  Again all 21
adjacencies follow.

### Lemma 5.4 (the portal has at most one opposite-triple contact)

Let `U-\{c\}=\{u,u',u''\}` be the other independent triple.  Then `z`
is adjacent to at most one of `u,u',u''`.

### Proof

Suppose, after relabelling, that `zu'` and `zu''` are edges.  Put
`R=D-z`, which is nonempty, connected, and full to `S-\{t\}` by Lemmas
1.1, 5.1, and 5.2.  Let `D'` be the opposite full shore.  The seven bags

\[
 \{t'\},\quad \{u'\},\quad \{c\},\quad R,\quad
 \{t,u\},\quad \{z,u''\},\quad D'\cup\{t''\}         \tag{5.3}
\]

form a `K7` model.  The two mixed boundary bags are connected through
the complete bipartite graph between the triples, `\{z,u''\}` is
connected by the assumed edge, and the last bag is connected by fullness
of `D'`.  The bag `R` sees every boundary-containing bag either through
its fullness to `S-\{t\}` or, for `\{z,u''\}`, through an edge to `z`.
The singleton `\{u'\}` sees `\{z,u''\}` through `u'z`; all other pairs
are adjacent through the complete bipartite boundary, `c`, or the full
shore `D'`.  This contradicts `K7`-minor-freeness.

### Theorem 5.5 (four-foot pendant-portal lock)

If a shore fails to contain a rooted triangle on one of the two
independent boundary triples, then it has a vertex `t` of that triple
with a unique shore neighbour `z`, while `D-z` is nonempty, connected,
and full to `S-{t}`, and `z` has no neighbour in the other two vertices
of the triple.  It has at most one neighbor in the opposite independent
triple and at least four distinct neighbors in `D-z`.  In particular,

\[
 |D|\ge5.                                             \tag{5.4}
\]

### Proof

Only the last assertion remains.  The boundary neighbors of `z` consist
of `t`, at most one vertex of the opposite triple by Lemma 5.4, and
possibly `c`; Lemma 5.3 excludes `t',t''`.  Hence `z` has at most three
neighbors in `S`.  It has no neighbor in the opposite shore.  Since
`\delta(G)\ge7`, it has at least four distinct neighbors in `D-z`.

## 6. Degree orientation across the two shores

Every member `s` of `A union B` has four neighbours in `S` and no
neighbours outside `S union D_1 union D_2`.  Since a contraction-critical
counterexample has minimum degree at least seven,

\[
 |N_{D_1}(s)|+|N_{D_2}(s)|\ge3.                       \tag{6.1}
\]

Thus a vertex can be a unique portal in at most one shore.  Lemma 1.1
removes the singleton alternative.  Consequently, if neither shore
contains a rooted triangle for a fixed triple, Theorem 5.5 gives two
distinct locked roots, one for each shore.  This is the exact
remaining geometry for the `2K3+K1` boundary after the rooted-triangle
and web alternatives have been removed.

The pendant lock is now superseded by the two-piece surgery theorem in
`hadwiger_k331_two_piece_closure.md`.  That theorem forces every shore
to be four-connected and every individual portal row to lie in one
cross-triangle.  Fullness then supplies three distinct portals for each
of (A) and (B), and two-connectivity packages either triple into a
rooted triangle.  Taking an (A)-rooted triangle in one shore and a
(B)-rooted triangle in the other closes this boundary with a
(K_7)-model.  Thus the pendant configurations described above are
useful intermediate locks, but none survives the full two-piece
argument.
