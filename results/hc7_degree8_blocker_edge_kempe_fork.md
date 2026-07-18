# A boundary-edge obstruction yields three far-shore Kempe connections

**Status:** written proof; separate internal audit.  This is a conditional
theorem in the degree-eight cyclic-sector configuration.  It proves the
proper-minor composition and the resulting far-shore Kempe connections.  It
does not prove that their first edges enter different labelled connected
sets, and therefore does not by itself give a `K_7` minor or a compatible
order-seven separation.

## 1. Setup

Let `G` be a graph which is not six-colourable and every proper minor of
which is six-colourable.  Let

\[
       V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
       \qquad E_G(L,R)=\varnothing,
\]

where both open sides are nonempty.  Partition

\[
 T=I\mathbin{\dot\cup}J\mathbin{\dot\cup}\{b,q,r\},
 \qquad I=\{i_0,i_1\},\quad J=\{j_0,j_1\}.
\tag{1.1}
\]

Assume that `I` and `J` are independent.

Fix `a in T`.  Assume `G[R union T]-a` contains five pairwise
vertex-disjoint connected subgraphs

\[
                         Q_I,Q_J,Q_1,Q_2,Q_3
\]

which are pairwise adjacent, are each adjacent to `a`, and cover `T-{a}`.
Assume

\[
 Q_I\cap T=I,\qquad Q_J\cap T=J,
\]

every other row trace has order at most one, and one of `Q_1,Q_2,Q_3`
misses `T`.

On the other side let `C_0,C_1,C_2,C_3` be pairwise vertex-disjoint
connected subgraphs of `G[L\cup I\cup J]` with respective boundary traces

\[
       \{i_0\},\quad\{j_0\},\quad\{i_1\},\quad\{j_1\}.
\tag{1.2}
\]

Suppose `b` has a neighbour in each of `C_0,C_2`, and `q` has a neighbour
in each of `C_1,C_3`.  Assume

\[
                         J\cup\{q\}\text{ is independent}.             \tag{1.3}
\]

Let

\[
                  F_b=E_G(\{b\},I),                                    \tag{1.4}
\]

and assume `F_b` is nonempty.  Finally assume that the two connected
supports constructed below are adjacent.  In the reserved cyclic-sector
application this last assumption is automatic: an edge from `C_0` to
`C_1` already supplies it.

## 2. The defective far-shore colouring

### Lemma 2.1

There is a proper six-colouring `c` of

\[
                         G[R\cup T]-F_b                              \tag{2.1}
\]

such that

\[
             I\cup\{b\}\text{ is monochromatic},\qquad
             J\cup\{q\}\text{ is monochromatic},                    \tag{2.2}
\]

and the two displayed colours are distinct.

#### Proof

Put

\[
              X_I=G[V(C_0)\cup V(C_2)\cup\{b\}],
       \qquad X_J=G[V(C_1)\cup V(C_3)\cup\{q\}].       \tag{2.3}
\]

The two contacts from `b` make `X_I` connected, and the two contacts from
`q` make `X_J` connected.  Their traces are

\[
       V(X_I)\cap T=I\cup\{b\},\qquad
       V(X_J)\cap T=J\cup\{q\}.                       \tag{2.4}
\]

The two subgraphs are vertex-disjoint.  By hypothesis they are adjacent.
In particular, any edge from `C_0` to `C_1` supplies this adjacency because
the entire two connected subgraphs, rather than selected internal paths,
were retained in (2.3).

Contract a spanning tree of each of `X_I,X_J` **in the original graph
`G`**.  This qualification is important.  An edge of `F_b` may be the
unique `b-C_0` or `b-C_2` contact and may therefore be essential for the
connectivity of `X_I`; the proof never asserts that `X_I-F_b` is
connected.  The two contractions give a proper minor of `G`, and hence a
proper six-colouring of that minor.

Keep its colours on the unchanged vertices of `R`.  On the literal
boundary, give every vertex of `I\cup{b}` the colour of the representative
of `X_I`, and every vertex of `J\cup{q}` the colour of the representative
of `X_J`; keep the colour of `r`.

This is a proper colouring of (2.1).  The set `I\cup{b}` is independent
after deleting all edges in `F_b`, while `J\cup{q}` is independent by
(1.3).  Every edge from an expanded boundary vertex to an unchanged vertex
survived at the relevant contraction representative.  Every edge between
the two expanded sets survived between the two representatives.  Since
the representatives are adjacent, their colours are distinct.  This
proves (2.2).  \(\square\)

## 3. Three absent-colour Kempe connections

### Theorem 3.1

Let `alpha` be the colour of `I\cup{b}` in Lemma 2.1.  At least three
colours are absent from the literal boundary `T`.  For every such absent
colour `beta`, one of the following holds.

1. `G` is six-colourable; or
2. in the `alpha,beta` subgraph of `G[R\cup T]-F_b`, the component
   containing `b` also contains a vertex of `I`.

Consequently, in a non-six-colourable host there are at least three
colour-indexed `b-I` paths in `G[R\cup T]-F_b`.  Each can be chosen so that
its internal boundary vertices are contained in `{r}`.  If the colour of
`r` is different from `alpha`, all its internal vertices lie in `R`.

Each selected path has positive even length, alternates between `alpha`
and its private absent colour, and every vertex of that private colour lies
in `R`.  If a selected path uses `r`, its two subpaths on either side of
`r` have all internal vertices in `R`.

For two different absent colours `beta,gamma`, the corresponding paths can
intersect away from their ends only at vertices coloured `alpha` (after
shortening each path to its first vertex of `I`).

#### Proof

The boundary in Lemma 2.1 is covered by the two monochromatic sets in
(2.2) and the singleton `r`.  It therefore uses at most three colours, so
at least three of the six colours are absent from `T`.

Fix an absent colour `beta` and let `K_beta` be the `alpha,beta` component
of the graph in (2.1) which contains `b`.  Suppose `K_beta` misses `I`.
Interchange `alpha,beta` on `K_beta`.  This is a proper Kempe interchange
in (2.1).  The vertex `b` changes colour, while both members of `I` retain
colour `alpha`; consequently every edge of `F_b` is now proper.  The set
`J` remains monochromatic: its colour is distinct from `alpha`, by Lemma
2.1, and `beta` was absent from the boundary.  Thus the resulting
colouring is a proper colouring of the original far closed shore
`G[R\cup T]` in which both row traces `I,J` are monochromatic.

Every other row trace has order at most one and one row misses `T`.
The five-row reflection theorem therefore reflects this boundary equality
partition through the other closed shore.  The two colourings align and
glue, giving a six-colouring of `G`.  This is outcome 1.  In a
non-six-colourable host, outcome 2 must hold for every absent `beta`.

Choose a shortest path in `K_beta` from `b` to `I`, stopped at its first
vertex of `I`.  No boundary vertex has colour `beta`.  Among boundary
vertices of colour `alpha`, the only possibilities outside
`I\cup{b}` are the singleton `r`: the colour of `J\cup{q}` is distinct.
Thus every internal boundary vertex of the path belongs to `{r}`.  If
`r` has another colour, no internal boundary vertex occurs, and the
interior lies in `R` because there is no `L-R` edge and the whole path is
in the far closed shore.

Both ends have colour `alpha`, so the path has positive even length and
alternates between the two colours.  Every `beta`-coloured vertex is
off the boundary and hence lies in `R`.  The assertion after deleting a
possible occurrence of `r` follows from the same observation.

Finally, vertices common to an `alpha,beta` path and an
`alpha,gamma` path have a colour in

\[
                  \{\alpha,\beta\}\cap\{\alpha,\gamma\}
                         =\{\alpha\}.
\]

This proves the last assertion.  \(\square\)

## 4. Relation to literal edge-deletion responses

The colouring from Lemma 2.1 can be extended across the opposite shore to
an actual six-colouring of `G-F_b` with the same equality partition on `T`.
Indeed, repeat the contraction construction in the proof of the five-row
reflection theorem, now inside `G-F_b`; its row traces are monochromatic and
one row is boundary-free.  Every minor coloured in that construction is a
proper minor of `G`.  Aligning the two closed-shore colourings gives the
claimed colouring of `G-F_b`.

In particular, suppose `F_b={e}` for one edge `e=bi`.  The preceding
construction is then an actual six-colouring of `G-e` with the prescribed
boundary equality partition.

Since `G` is not six-colourable, in every six-colouring of `G-e` the ends
of `e` have the same colour and lie in one two-colour Kempe component for
each of the other five colours.  Each endpoint also has a neighbour of
every other colour.  Thus the colouring supplied here is fully compatible
with the ordinary critical-edge response; it is not an unrelated boundary
assignment.

### The deletion/contraction square collapses at the blocker edge

There is no second, independent colouring response obtained merely by also
contracting `e`.  Proper six-colourings of `G/e` correspond exactly to
proper six-colourings of `G-e` in which the ends of `e` have the same
colour: lift the contracted vertex to both ends in one direction, and
identify the equally coloured ends in the other.  Since every six-colouring
of `G-e` already gives the ends of `e` the same colour, **all** six-colourings
of `G-e` arise this way.

Consequently the deletion and contraction responses at the blocker edge do
not supply two boundary partitions that can be compared.  A genuinely new
response must use a different proper-minor operation, for example one
supported at a first common entry vertex of the Kempe connections or inside
one of the named connected sets.

## 5. Exact remaining obstruction

The theorem proves the composition up to a labelled first-hit problem.
It does **not** imply that the three paths leave `b` through three different
connected sets, avoid a prescribed seventh branch set, or contain two
internally vertex-disjoint paths.  Their common `alpha`-coloured vertices
may concentrate all paths behind one literal portal.

Therefore the following inference remains unjustified:

\[
 \text{three absent-colour connections and endpoint saturation}
 \quad\Longrightarrow\quad
 \text{a label-preserving split of the cyclic connected sets}.        \tag{5.1}
\]

A completion must use `K_7`-minor exclusion and the universal responses to
proper minor operations at a first common portal.  The proved theorem
already supplies the exact host subgraph and the three simultaneous colour
indices on which that operation must act.

## 6. Dependency

- [five-row reflection across a separation](../results/hc7_five_row_separator_reflection.md)
- [safe boundary supports and the four contact patterns](../results/hc7_degree8_safe_support_reflection.md)
