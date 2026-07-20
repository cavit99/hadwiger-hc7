# Structure of a seven-column contact graph

**Status:** written proof; independently audited **GREEN** in
[`hc7_seven_column_contact_structure_audit.md`](hc7_seven_column_contact_structure_audit.md).
This note proves a quotient-level structure theorem and a literal
clean-bridge consequence for the paired-column model at an order-eight
boundary.  It does **not** turn a quotient separator into a small separator
of the host graph, synchronize two boundary colourings, or prove `HC_7`.

## 1. The seven-vertex graph theorem

### Theorem 1.1 (low degree or a pentagonal bipyramid)

Let `J` be a graph on seven vertices with no `K_5` minor.  Then exactly one
of the following statements applies.

1. `J` has a vertex of degree at most three.
2. `J` is the pentagonal bipyramid

   \[
                      \overline{K_2\mathbin{\dot\cup}C_5}.
                                                              \tag{1.1}
   \]

The graph in (1.1) is planar, four-connected and edge-maximal
`K_5`-minor-free.  Consequently, if `J` has minimum degree at least four,
then adding any missing edge to `J` creates a `K_5` minor.

#### Proof

Assume that `delta(J)>=4` and put `H=overline J`.  Thus
`Delta(H)<=2`.  Extend `H`, on its fixed seven-vertex set, to an
edge-maximal graph `H^+` of maximum degree at most two.  Then

\[
                         \overline {H^+}\subseteq J.            \tag{1.2}
\]

We first classify `H^+`.  Any two nonadjacent vertices of degree at most
one could be joined without making a degree exceed two.  Hence the set of
vertices of degree at most one is a clique and has order at most two.

If it has order two, its two vertices form a `K_2` component and the other
five vertices form a cycle.  If it has order one, the handshaking lemma
forces that vertex to be isolated; the other six vertices form either one
cycle or two triangles.  If it is empty, all vertices have degree two and
form either one cycle or a triangle and a quadrilateral.  Thus

\[
 H^+\in\{C_7,\ C_3\mathbin{\dot\cup}C_4,\
 C_6\mathbin{\dot\cup}K_1,\
 2C_3\mathbin{\dot\cup}K_1,\
 C_5\mathbin{\dot\cup}K_2\}.                           \tag{1.3}
\]

The complements of the first four graphs in (1.3) contain the following
explicit `K_5` models.  Cycle subscripts below are read in their displayed
cyclic order.

| `H^+` | five branch sets in `overline{H^+}` |
|---|---|
| `C_7=01234560` | `{0,3}`, `{1,5}`, `{2}`, `{4}`, `{6}` |
| `C_3(012) dotcup C_4(3456)` | `{0,3}`, `{1,5}`, `{2}`, `{4}`, `{6}` |
| `C_6(012345) dotcup {6}` | `{0,2,4}`, `{1}`, `{3}`, `{5}`, `{6}` |
| `C_3(012) dotcup C_3(345) dotcup {6}` | `{0,3}`, `{1,4}`, `{2}`, `{5}`, `{6}` |

In every row each nonsingleton set is connected in the complement, the
singleton sets are pairwise adjacent, and every two displayed sets have a
complement edge between them.  Thus (1.2) and the hypothesis on `J` force

\[
                         H^+=C_5\mathbin{\dot\cup}K_2.          \tag{1.4}
\]

Write the cycle as `c_0c_1c_2c_3c_4c_0` and the `K_2` as `ab`.  If
`H` is a proper subgraph of `H^+`, choose an edge of `H^+-H`.

If that edge is `ab`, then `J` contains two adjacent vertices complete to
the five-cycle `overline{C_5}\cong C_5`.  Contracting that five-cycle to a
triangle gives a `K_5` minor.

Otherwise, after a cyclic relabelling, the missing edge is `c_0c_1`.
In `J` the five sets

\[
             \{a,c_2,c_4\},\quad \{b\},\quad
             \{c_0\},\quad\{c_1\},\quad\{c_3\}               \tag{1.5}
\]

form a `K_5` model.  The first set is connected because `a` is adjacent
to every cycle vertex.  The four singleton sets form a clique: `b` is
complete to the cycle, `c_0c_1` is the newly present edge, and
`c_0c_3,c_1c_3` are complement edges of the original cycle.  The first
set is adjacent to every singleton set (to `b` through `c_2`, and to the
cycle singletons through `a`).

Both possibilities contradict the exclusion of a `K_5` minor.  Hence
`H=H^+`, proving (1.1).  The graph in (1.1) is the planar bipyramid over a
five-cycle, so it has no `K_5` minor.  The two constructions just given
show that adding any one of its six missing edges creates a `K_5` minor.
Its four-connectivity is immediate from the description.  After deleting
at most three vertices, a surviving pole joins all surviving rim vertices
and, through any such rim vertex, the other surviving pole.  If neither
pole survives, at most one rim vertex was deleted and the remaining
five-cycle is connected.  This completes the proof.
\(\square\)

### Corollary 1.2 (the only four-connected quotient obstruction)

If `J` is as in Theorem 1.1, then either `J` has a separation of order at
most three isolating one vertex, or `J` is the pentagonal bipyramid.

#### Proof

In outcome 1 of Theorem 1.1 choose `x` with `d_J(x)<=3`.  The two vertex
sets

\[
          \{x\}\cup N_J(x),\qquad V(J)-\{x\}                 \tag{1.6}
\]

define a separation with intersection `N_J(x)`.  Both open sides are
nonempty because at least three vertices lie outside `N_J[x]`.  Outcome 2
is four-connected by Theorem 1.1.  \(\square\)

The separation in Corollary 1.2 is a separation of the **contact graph**.
Its separator vertices represent whole connected subgraphs of the host and
therefore do not constitute an order-three separator in the host graph.

## 2. Literal paired columns

Let `G` contain nine pairwise vertex-disjoint connected subgraphs

\[
                         R_0,R_1,L_1,\ldots,L_7              \tag{2.1}
\]

such that `R_0R_1` is an adjacent pair and each `R_i` is adjacent to every
`L_j`.  Let `J` be the contact graph on `[7]`, where

\[
 ij\in E(J)\quad\Longleftrightarrow\quad
 E_G(L_i,L_j)\ne\varnothing.                                \tag{2.2}
\]

This includes the paired all-boundary columns produced from the two
relative fans in the order-eight response interface.

### Theorem 2.1 (seven-column structural decoder)

If `G` has no `K_7` minor, then one of the following holds.

1. Some column `L_x` contacts at most three of the other columns.  At the
   quotient level its neighbours separate its label from at least three
   other column labels.
2. The seven column contacts form the pentagonal bipyramid.  In this case
   suppose `L'_1,...,L'_7` are pairwise disjoint connected subgraphs,
   disjoint from the fixed roots, each adjacent to both roots, and their
   contact graph contains `J+xy` for some nonedge `xy` of `J`.  These
   modified columns produce an explicit `K_7`-minor model using the same
   two root subgraphs.

#### Proof

If `J` had a `K_5` model, taking unions of columns over its five branch
sets and adjoining `R_0,R_1` would give a `K_7` model in `G`.  Hence `J`
is `K_5`-minor-free and Theorem 1.1 applies.

In its low-degree outcome, (2.2) says literally that `L_x` has no edge to
any column outside `N_J[x]`.  Corollary 1.2 gives the asserted quotient
separation.

In the other outcome, Theorem 1.1 gives a `K_5` model in `J+xy`.  Since the
modified contact graph contains this graph, its five branch sets lift, by
taking the unions of the corresponding modified literal columns, to five
pairwise adjacent connected subgraphs.  Together with the unchanged
`R_0,R_1` these are an explicit `K_7` model.  \(\square\)

### Lemma 2.2 (clean first-hit augmentation)

Suppose `L_x,L_y` do not contact one another and there is an `L_x`--`L_y`
path `P` whose internal vertices avoid all nine subgraphs in (2.1).  Then
replacing

\[
             L_x\quad\hbox{by}\quad L_x\cup(V(P)-V(L_y))       \tag{2.3}
\]

gives another nine-subgraph system of the form (2.1), and its contact graph
contains `J+xy`.

In particular, if `J` is the pentagonal bipyramid, this path gives an
explicit `K_7` minor.  More generally, if the system was chosen to maximize
`|E(J)|` among all systems with the same two roots and seven distinguished
column labels, no such path exists in a `K_7`-minor-free host.

#### Proof

Truncate `P` at its first vertex of `L_y` and, after reversing if needed,
at its last vertex of `L_x`.  The set in (2.3) is connected, remains
disjoint from all other bags, retains its old root contacts, and is now
adjacent to `L_y` through the last edge of `P`.  All old inter-column
contacts remain.  The pentagonal-bipyramid conclusion follows from
Theorem 2.1.  In the general extremal statement, the modified contact graph
either contains a `K_5` minor, giving a `K_7` minor, or is a strictly
larger admissible contact graph, contradicting the choice.  \(\square\)

### Corollary 2.3 (localization of unused connected pieces)

Choose a system (2.1) maximizing `|E(J)|`, and assume that `G` has no
`K_7` minor.  If `Z` is a component of

\[
        G-\bigl(R_0\cup R_1\cup L_1\cup\cdots\cup L_7\bigr),  \tag{2.4}
\]

then the set of column labels met by `Z` is a clique of `J`.

Consequently, in the pentagonal-bipyramid outcome, every such `Z` meets at
most three columns, and its column labels lie in one set consisting of one
pole and the ends of one rim edge.

#### Proof

If `Z` met two nonadjacent columns, connectedness of `Z` would give a path
as in Lemma 2.2, contrary to its extremal conclusion.  Thus all labels met
by `Z` are pairwise adjacent in `J`.  In a pentagonal bipyramid the two
poles are nonadjacent and the rim has clique number two.  Its maximal
cliques are exactly one pole together with the two ends of a rim edge.
\(\square\)

## 3. Exact contribution and trust boundary

Theorem 2.1 replaces an arbitrary seven-vertex `K_5`-minor-free contact
graph by one of two reusable structures:

- a column with at most three column neighbours, giving a genuine
  order-at-most-three separation of the quotient contact graph; or
- one fixed four-connected planar graph which is saturated for the desired
  `K_5` minor.

Lemma 2.2 couples this classification to literal first-hit paths: a clean
path to a missing column label is either terminal in the bipyramid case or
strictly improves an edge-maximal column system.  Corollary 2.3 localizes
every unused connected piece to a clique of column labels.

The following limitations are essential.

- A vertex of `J` represents an entire connected column.  A separator of
  `J` of order three is **not** an order-three, order-seven or otherwise
  bounded separator of `G`.
- A first-hit path is usable in Lemma 2.2 only when its interior avoids all
  root and column subgraphs.  A path running through an old column cannot
  be treated as a new contact without a label-preserving split of that
  column.
- Maximizing `|E(J)|` is a finite normalization of column systems, not a
  decrease of the operated response shore and not a substitute for the
  selected-response rank.
- The theorem does not force the operation-specific colour paths to have
  distinct first-hit column labels.  In the low-degree outcome they may
  continue to concentrate in the three neighbouring columns; in the
  bipyramid outcome they may continue to enter columns along existing
  contact edges.

Thus the remaining response-coupling theorem must use proper-minor
nonextension to turn this three-label concentration or the bipyramid's
facial-triangle localization into a compatible order-seven boundary, a
label-preserving column split, or a selected-response descent.

## 4. Dependencies

- the definition and elementary lifting property of a minor model; and
- the paired-column decoder only for the application in Section 2.

No finite graph census or external structure theorem is used in the proof.
