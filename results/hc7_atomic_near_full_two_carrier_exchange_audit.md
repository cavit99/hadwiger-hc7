# Independent audit: atomic near-full two-carrier state exchange

## Verdict

**GREEN** at frozen source SHA-256
`5665dd7255a879b8c6506d2697ee8f3468ca00b00cde2a1fd7226463b876bf5d`.

The nonspanning near-full carrier theorem, its clean-edge specialization,
and the two-connectivity corollary are all correct under the stated atomic
hypotheses.  In the connected bipartite frontier, the two tailored contraction sets are
literal, disjoint, connected, nontrivial, and produce a proper minor.  Its
restriction has exactly one of the two displayed boundary partitions;
accidental equality can only decide which of those two occurs.  Both have
packet demand at most two, so exact reflection and palette gluing are
legal.  In the exceptional frontier, the bad defects must be two claw
leaves and the seven displayed bags have every required literal adjacency.

No spanning condition `X union Y=A` is used: vertices of the thin shore
outside the two carriers remain in the proper minor and are discarded only
when its colouring is restricted to the rich closed shore.  The cutvertex
argument supplies two such near-full carriers, so every nonsingleton atomic
thin shore is two-connected and has order at least three.

The result still does not allocate a fully crossed bridge hull or transport
a state across a new adhesion.

## 1. Exact near-full defect reduction

The source assumes disjoint nonempty connected adjacent sets
`X,Y subseteq A`, with `z in X`, and

\[
                         |N_S(X)|,|N_S(Y)|\ge 6.
\]

Since `zu` is the unique `A-u` edge, `X` contacts `u` and `Y` does not.
Thus `Y` has the singleton defect `{u}`.  The defect of `X` is empty or a
singleton different from `u`, because `X` already contacts `u`.  It follows
directly that every boundary contact list is nonempty even though
`X union Y` need not be all of `A`.

In the sole bad two-list case the defect of `X` is a distinct literal `p`.
This verifies

\[
 S-N_S(X)=\{p\},\qquad S-N_S(Y)=\{u\}.
\]

The exact two-list theorem says that a bad pair lies in the same connected
component and the same bipartition side of the audited frontier `F` while
being forced to opposite carrier labels.  No additional parity assumption
is introduced in the source.

## 2. Connected bipartite frontier: contraction legality

Here `F=H=G[S]` is connected and bipartite.  Let its bipartition be

\[
                         S=I\mathbin{\dot\cup}J,
                         \qquad p,u\in I.
\]

The set `I-{p}` is nonempty because it contains `u`, and `J` is nonempty
because the connected graph `H` has an edge and a nonempty opposite
bipartition class.

Define

\[
 Z_X=X\cup(I-\{p\}),\qquad Z_Y=Y\cup J.
\]

These sets satisfy every minor requirement.

* **Disjointness.**  `X,Y` are disjoint subsets of the open shore, `I,J`
  partition the boundary, and `p` is omitted from both sets.  No vertex of
  `A-(X union Y)` belongs to either contraction set.
* **Connectedness.**  The only defect of `X` is `p`, so every member of
  `I-{p}` has a literal neighbour in `X`.  The only defect of `Y` is `u`,
  so every member of `J` has a literal neighbour in `Y`.
* **Nontriviality.**  Each set contains a nonempty carrier and a nonempty
  boundary block joined to it by a literal edge.
* **Adjacency.**  The fixed literal `X-Y` edge remains an edge between the
  two sets.
* **Properness of the minor.**  Contracting spanning trees of the two
  nontrivial sets strictly reduces the graph.  The nonempty rich shore is
  untouched, so the result is not the vacuous contraction of the whole
  graph.  Vertices of `A-(X union Y)` simply remain as ordinary vertices.

Let `x,y` be the two representatives.  The edge induced by `h` forces

\[
                             c(x)\ne c(y).
\]

The literal `p-Y` contact follows from the fact that `Y` has sole defect
`u`; it forces `c(p)\ne c(y)`.  On the other hand, `p` has no edge to
`X`, and it has no edge to `I-{p}` because `I` is independent.  Hence no
edge joins `p` to `Z_X`, so `p` is genuinely nonadjacent to `x` in the
minor.

## 3. Exact returned boundary state

Restrict a six-colouring of the proper minor to `G[R union S]`, expanding
the colour of `x` over `I-{p}` and the colour of `y` over `J`.

The expansion is proper: both expanded blocks are independent, and every
edge from either block to a retained vertex was represented by an edge at
the corresponding contracted image.  The two blocks have different
colours because `xy` is an edge.  The literal `p` cannot use the `J` colour
because `py` is an edge.  It may either use the `I-{p}` colour or a third
colour.  There are no other boundary vertices.  Consequently the exact
partition is precisely

\[
                         I\mid J
\]

or

\[
                         (I-\{p\})\mid\{p\}\mid J.
\]

This exhausts accidental equalities: `p` cannot merge with `J`, the two
contracted blocks cannot merge with each other, and in the second case no
other boundary vertex can share the third colour.

The first state has two blocks and therefore packet demand at most two.
The second has three blocks and contains the singleton block `{p}`; hence

\[
 d_H(\Pi)=3-\omega(H[\operatorname{sing}(\Pi)])\le 3-1=2.
\]

This remains true if either of the other two blocks is also a singleton.

## 4. Reflection side and palette gluing

The contraction sets lie wholly in `A union S`.  After restriction and
expansion, the colouring on `G[R union S]` is therefore a colouring of the
intact original rich closed shore with the actual returned state above.
The unused vertices of `A-(X union Y)` are discarded at this restriction;
their presence in the minor cannot create an omitted edge inside
`G[R union S]` and imposes no lifting obligation.

The two disjoint `S`-full packets in `R` may now be used in the audited
exact packet-reflection theorem.  Since the returned state has demand at
most two, it produces a colouring of the intact original thin closed shore
`G[A union S]` with exactly that partition.  Any exceptional `K_7` output
is already terminal and is excluded by the setup.

The colours of corresponding blocks can be aligned by a permutation of the
six-colour palette.  There is no `A-R` edge, so the two aligned closed-shore
colourings glue to a proper six-colouring of `G`.  No colour name is
identified with a carrier label; the literal contractions manufacture the
blocks before palette alignment.

## 5. Exceptional frontier

Now

\[
 H=K_{1,3}\mathbin{\dot\cup}K_3,
 \qquad F=K_{1,3}\mathbin{\dot\cup}K_2
\]

after retaining one legal triangle vertex, with `u in V(F)`.  Two distinct
vertices in the `K_2` component lie in opposite bipartition sides.  In the
claw, the centre is alone in one side and the three leaves form the other.
Thus two distinct vertices in one component and one bipartition side must
be two claw leaves.  The bad pair `p,u` is therefore disjoint from all three
triangle vertices.

Let the triangle be `k_1k_2k_3`.  The five bags

\[
 X\cup\{u\},\quad Y\cup\{p\},\quad
 \{k_1\},\quad\{k_2\},\quad\{k_3\}
\]

are pairwise disjoint.  The first is connected through the literal `zu`
edge; equivalently, `X` contacts every boundary literal except `p`.  The
second is connected because `Y` contacts `p`.  They are adjacent through
the fixed literal `X-Y` edge.

Both `X` and `Y` contact every triangle vertex: their sole defects are
`p` and `u`, respectively, and neither defect is a triangle vertex.  The
three singleton bags are pairwise adjacent because they induce the literal
triangle.  Hence these five sets are connected, pairwise adjacent, and
each contains a different literal member of `S`.

The two rich packets are disjoint from these five bags and from one another.
They are adjacent by hypothesis.  Each is adjacent to every one of the five
bags through the boundary literal contained in that bag, because each
packet is `S`-full.  These are seven pairwise disjoint connected pairwise
adjacent literal bags, so they form a `K_7` model.

No completion edge, virtual adjacency, or palette contact is used in this
model.

## 6. Consequences

### Clean-edge specialization

The audited clean-edge split supplies disjoint adjacent connected carriers
which partition `A`, each with support at least six.  Naming the carrier
containing `z` as `X` meets every hypothesis of Theorem 2.1.  Thus
Corollary 3.1 is immediate and does not retain the former parity exception.

### Two-connectivity of a nonsingleton atom

The audited root-deletion normalization proves `A-z` connected, so `z` is
not a cutvertex.

Suppose `v != z` is a cutvertex.  Choose a component `D` of `A-v` not
containing `z`, and put

\[
                         Y=D,\qquad X=A-D.
\]

The set `Y` is connected.  Every component of `A-v` is adjacent to `v`
because `A` is connected.  Consequently `X`, consisting of `v` and all
the other components, is connected; `X,Y` are adjacent and `z in X`.

For every component `K` of `A-v`, all external neighbours lie in
`S union {v}`: distinct components are anticomplete, and there is no
`A-R` edge.  Its literal neighbourhood separates nonempty `K` from the
nonempty rich shore.  Seven-connectivity therefore gives

\[
                         |N_S(K)|+1\ge7,
                         \qquad |N_S(K)|\ge6.
\]

Applying this to `D` gives the support bound for `Y`.  Applying it to the
component containing `z`, which is a subset of `X`, gives the support bound
for `X`.  Theorem 2.1 rules out `v`.  Hence `A` has no cutvertex.

It remains to check the order convention.  If `|A|=2`, write
`A={z,a}`.  Connectedness gives the literal edge `za`.  Root deletion
makes `{a}` full to all six vertices of `W`, so it has boundary support
six.  The frozen minimum-degree bound gives `d_G(z)>=7`; `z` has no rich
neighbour and at most the one internal neighbour `a`, so it has at least
six boundary neighbours.  The adjacent singleton carriers `{z},{a}` then
satisfy Theorem 2.1, a contradiction.  Thus `|A|>=3`.

Connectedness, order at least three, and absence of a cutvertex prove
Corollary 3.2 exactly.

## 7. Trust boundary

The proof uses all of the following.

* two literal disjoint connected adjacent carriers with support at least
  six; they need not span `A`;
* the unique `A-u` edge with its thin endpoint `z` on the named carrier
  `X`;
* one of the two audited frontier forms;
* two disjoint `S`-full rich packets for reflection; and
* their literal adjacency in the exceptional `K_7` construction.

It proves that any such near-full rooted carrier pair closes, that no clean
edge of the normalized core survives, and that a nonsingleton atomic shore
is two-connected.  Therefore a remaining core is fully crossed by literal
`T`-bridges in a two-connected ambient thin shore.  It does not turn the
resulting edge-disjoint routing into vertex-disjoint labelled carriers,
decode a web completion, or provide a state-carrying exact-seven descent.
