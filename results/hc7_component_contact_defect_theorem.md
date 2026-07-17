# Component-contact defect for a colour-matched path

**Status:** written proof; separate internal audit.  The theorem gives a
uniform sufficient condition for completing the unique-deficiency
colour-matched-path construction.  It also identifies the sharp
`K_7`-minor-free equality structure as a two-tree.  It does not prove that
the equality structure is incompatible with contraction-criticality, and it
does not prove `HC_7`.

## 1. A component-count density lemma

Let `B_1,...,B_7` be pairwise disjoint nonempty vertex sets in a graph.  They
need not be connected.  Write

\[
 c_i=\operatorname{cc}(G[B_i]),\qquad
 r_{ij}=\operatorname{cc}(G[B_i\cup B_j]),\qquad
 n=\sum_{i=1}^7c_i .                                \tag{1.1}
\]

### Lemma 1.1

If

\[
                  \sum_{1\le i<j\le7}r_{ij}\le n+14,                \tag{1.2}
\]

then `G` contains a `K_7` minor.

#### Proof

Contract every component of every `G[B_i]` to one vertex, delete all other
vertices, and suppress parallel edges.  The resulting simple minor `J` has
`n` vertices.  For each pair `i<j`, its bipartite subgraph on the component
vertices arising from `B_i` and `B_j` has `r_{ij}` components, and hence at
least

\[
                              c_i+c_j-r_{ij}           \tag{1.3}
\]

edges.  Edges belonging to different index pairs are disjoint.  Therefore

\[
 |E(J)|\ge
 \sum_{i<j}(c_i+c_j-r_{ij})
 =6n-\sum_{i<j}r_{ij}
 \ge5n-14.                                           \tag{1.4}
\]

Since `n>=7`, Mader's exact extremal theorem for `K_7` minors applies and
gives a `K_7` minor in `J`, hence in `G`.  \(\square\)

## 2. The component-contact graph at a path cut

Use the unique-deficiency setup and notation of the audited all-cut interval
exchange theorem.  In particular, a cut `q` of the colour-matched path gives
three pairwise adjacent connected sets

\[
                              C_q,\quad U_q,\quad\{z\}.               \tag{2.1}
\]

For each protected branch set
\(K\in\{X,D_1,D_2,D_3\}\), choose a nonempty collection
\(\mathcal L_K\) of components of \(G[K-V(P)]\).  Assume every chosen
component

1. has `q` in its valid-cut interval, and therefore is adjacent to both
   `C_q` and `U_q`; and
2. is adjacent to `z`.

The **component-contact graph** `J` has the chosen components as its vertices;
two vertices are adjacent precisely when the corresponding connected
subgraphs are adjacent in `G`.  It is naturally four-partite.  Put

\[
 c_K=|\mathcal L_K|,\qquad C=\sum_Kc_K,\qquad
 r_{KK'}=\operatorname{cc}
       \bigl(J[\mathcal L_K\cup\mathcal L_{K'}]\bigr).               \tag{2.2}
\]

Define the **component defect**

\[
 \begin{aligned}
 \Delta(J)
  &=\sum_{K<K'}(r_{KK'}-1)-\sum_K(c_K-1)\\
  &=\sum_{K<K'}r_{KK'}-C-2.                         \tag{2.3}
 \end{aligned}
\]

### Theorem 2.1

Each of the following conditions implies that `G` contains a `K_7` minor.

1. The component-contact graph `J` contains a `K_4` minor.
2. \(\Delta(J)\le 0\).

Consequently, in a `K_7`-minor-free graph every such selection in which all
four collections are nonempty satisfies \(\Delta(J)\ge 1\).

#### Proof

For item 1, let four disjoint connected branch sets of a `K_4` model in `J`
be given.  Replace every quotient vertex by its corresponding connected
subgraph of `G`, and include the host edges represented by the edges of the
quotient branch sets.  This lifts the four quotient branch sets to four
disjoint connected subgraphs of `G`.  They are pairwise adjacent.  Every one
is adjacent to each set in (2.1), while the three sets in (2.1) are pairwise
adjacent.  These seven sets are an explicit `K_7`-minor model.

For item 2, one may apply Lemma 1.1 directly.  The three sets in (2.1) are
connected.  Their three pairwise unions are connected, and the union of any
one of them with any selected protected union is connected.  Thus fifteen
of the twenty-one pair component counts equal one.  Lemma 1.1 reduces to

\[
              \sum_{K<K'}r_{KK'}\le C+2,             \tag{2.4}
\]

which is exactly `Delta(J)<=0`.

There is also a useful proof entirely inside `J`.  For every pair `K<K'`,
put

\[
 \rho_{KK'}=c_K+c_{K'}-r_{KK'},                       \tag{2.5}
\]

the rank of a spanning forest of that bichromatic graph.  Because every
part occurs in three pairs,

\[
       \sum_{K<K'}\rho_{KK'}
           =3C-\sum_{K<K'}r_{KK'}
           =2C-2-\Delta(J).                           \tag{2.6}
\]

Choose a spanning forest independently in each bichromatic graph.  Their
edge sets are disjoint.  If `Delta(J)<=0`, their union is a spanning
subgraph of `J` with at least `2C-2` edges.  The exact extremal bound for
`K_4` minors says that a `K_4`-minor-free graph on `C>=4` vertices has at
most `2C-3` edges.  Hence `J` has a `K_4` minor and item 1 applies.
\(\square\)

Theorem 2.1 is stronger than requiring the four protected unions to have
pairwise connected unions.  A `K_4` model in `J` may use vertices from more
than one protected label in one quotient branch set; the lift remains valid
because the three sets in (2.1) are adjacent to every selected quotient
vertex.

## 3. Exact equality structure

A **two-tree** is obtained from a triangle by repeatedly adding a new vertex
adjacent to both ends of an existing edge.  Equivalently, for order at least
three it is an edge-maximal `K_4`-minor-free graph.

### Theorem 3.1

Suppose all four selected collections are nonempty and `J` has no `K_4`
minor.  Then

\[
       \Delta(J)=1
       \quad\Longleftrightarrow\quad
       J\text{ is a two-tree}.                        \tag{3.1}
\]

#### Proof

If `Delta(J)=1`, equation (2.6) gives spanning forests in the six
bichromatic graphs whose disjoint union has `2C-3` edges.  That union is a
`K_4`-minor-free spanning subgraph of `J` attaining the extremal bound.  It
is therefore a two-tree.  Since adding any further edge would exceed the
`K_4`-minor-free bound, it already equals `J`.

Conversely, suppose `J` is a two-tree.  It is chordal.  Every bichromatic
induced subgraph is bipartite and contains no cycle: a shortest such cycle
would have length at least four and no chord within the same bichromatic
graph, contradicting chordality of `J`.  Hence the six bichromatic graphs
are forests.  Their forest ranks sum to all the edges of `J`, namely
`2C-3`.  Equation (2.6) now gives `Delta(J)=1`.  \(\square\)

Thus the first value not closed by the density theorem is a standard
infinite class, rather than a finite labelled residue.  In particular, the
next structural object is a simplicial degree-two vertex of a two-tree and
the connected host subgraph represented by it.

## 4. Exact change under elementary quotient moves

The component defect has a simple local calculus.

### Proposition 4.1 (adding one component)

Add a vertex `v` to part `K` of a selected component-contact graph.  For
each other part `K'`, let `t_{K'}` be the number of components of the old
bichromatic graph `J[mathcal L_K union mathcal L_{K'}]` which contain a
neighbour of `v`; put `t_{K'}=0` when `v` has no such neighbour.  Then

\[
             \Delta(J+v)-\Delta(J)
                 =2-\sum_{K'\ne K}t_{K'}.             \tag{4.1}
\]

#### Proof

In the pair `K,K'`, the new vertex either forms a new component or merges
the `t_{K'}` old components that it meets.  In both cases

\[
                  r'_{KK'}-r_{KK'}=1-t_{K'}.          \tag{4.2}
\]

The total component count `C` increases by one, and the other three pair
counts do not change.  Substitution in (2.3) proves (4.1).  \(\square\)

In particular, from a defect-one selection in a `K_7`-minor-free host, an
additional eligible component can meet at most two old bichromatic
components in total.  Meeting three would make the new defect nonpositive
and Theorem 2.1 would give a `K_7` minor.

### Proposition 4.2 (splitting one component)

Replace a vertex `v` in part `K` by `s>=1` vertices in that same part, with
no edges among them.  Assume their contacts merely distribute the old
contacts of `v`, so no replacement vertex meets a component of
`J-v` which did not belong to the old bichromatic component containing
`v`.

For each other part `K'`, delete `v` from its old bichromatic component,
contract each resulting component to one vertex, add the `s` replacement
vertices with their new incidences, and let `kappa_{K'}` be the number of
components of this incidence graph.  Then

\[
          \Delta(J')-\Delta(J)
             =\sum_{K'\ne K}\kappa_{K'}-s-2.          \tag{4.3}
\]

#### Proof

All old bichromatic components except the one containing `v` are
unchanged.  The latter one is replaced by `kappa_{K'}` components, so

\[
                    r'_{KK'}-r_{KK'}=\kappa_{K'}-1.  \tag{4.4}
\]

Meanwhile `C` increases by `s-1`.  Substitution in (2.3) yields (4.3).
\(\square\)

Equations (4.1) and (4.3) isolate the equality obstruction.  A legal move
can preserve defect one only by concentrating its contacts into sufficiently
few old bichromatic components.  Duplicate literal contacts inside one
quotient component do not change the defect.

## 5. Sharp purely combinatorial obstruction

The part-respecting pairwise-connected-union conclusion is false even when

- every selected component has the full valid-cut interval and is adjacent
  to all three anchor sets;
- all six pairs of protected labels have an edge; and
- the component-contact graph is edge-maximal `K_4`-minor-free.

Let

\[
 \begin{aligned}
 \mathcal L_A&=\{a\},&
 \mathcal L_B&=\{b\},&
 \mathcal L_C&=\{c\},&
 \mathcal L_D&=\{d_1,d_2\},
 \end{aligned}
\]

and give the component-contact graph the edges

\[
 ab,ac,bc,ad_1,cd_1,ad_2,bd_2.                       \tag{5.1}
\]

This is the two-tree obtained from triangle `abc` by adding `d_1` on edge
`ac` and `d_2` on edge `ab`.  Hence it has no `K_4` minor and has defect
one.  Every pair of labels occurs on an edge.  Nevertheless no nonempty
choice of unions has all six bichromatic unions connected.  The singleton
parts force `a,b,c` to be chosen.  Connectivity with `b` forces the
`D`-choice to contain `d_2` and omit `d_1`, while connectivity with `c`
forces it to contain `d_1` and omit `d_2`, a contradiction.

The audited 44-vertex joined-triangulation example gives the smallest
version of the same equality phenomenon at one cut: its natural quotient is
`K_4` minus one edge.  Here `C=4`, the six bichromatic component counts sum
to seven, and

\[
                              \Delta=7-4-2=1.         \tag{5.2}
\]

The colour-matched path repairs the original missing branch-set adjacency
while moving the single unit of defect to another protected pair.  That host
is six-colourable and already has an order-seven separation, so it does not
refute an `HC_7` theorem using all proper-minor colouring constraints.

## 6. Remaining contraction-critical step

Theorems 2.1 and 3.1 reduce the sharp branch to a host lift of a two-tree.
Choose a simplicial quotient vertex `v` with two adjacent quotient
neighbours.  The represented connected subgraph is adjacent to the three
sets in (2.1) and to those two neighbouring represented subgraphs.  To close
this branch one must use the full contraction-critical colouring responses
to prove one of the following:

1. a label-preserving split or rerouting creates a quotient contact meeting
   three old bichromatic components, and (4.1) or (4.3) lowers the defect to
   zero;
2. the represented connected subgraph has an actual neighbourhood of order
   seven; or
3. the same obstruction yields two vertices meeting every `K_5` model,
   which by the promoted transversal theorem forces an actual order-seven
   separation.

Seven-connectivity alone cannot force item 1: arbitrarily many literal
neighbours may represent duplicate contacts inside the same five quotient
neighbours.  The needed input is therefore a contraction-critical
**label-preserving contact-distribution statement**, not another
unlabelled connectivity bound.  The general side-wise saturation fact for a
contracted bipartite subgraph is a necessary input: in every six-colouring
after contracting such a subgraph, each side of its bipartition sees every
noncontracted colour.  What remains is to align those colour contacts with
the five named neighbouring subgraphs, or else turn the failure of alignment
into item 2 or 3.

## 7. Dependencies and external input

- [all-cut interval exchange](hc7_colour_matched_path_all_cut_interval_exchange.md)
- [component exchange or separation](hc7_colour_matched_path_exchange_or_separator.md)
- [two-vertex transversal forces an order-seven separation](hc7_k5_transversal_order7_separator.md)
- [joined-triangulation barrier](../barriers/hc7_three_common_geodesic_two_apex_barrier.md)

The `K_7` extremal input is W. Mader, *Homomorphiesatze fur Graphen*,
Math. Ann. **178** (1968), 154--168, DOI `10.1007/BF01350657`: a simple
`K_7`-minor-free graph on `n>=7` vertices has at most `5n-15` edges.  The
other external extremal input is the standard bound that a simple
`K_4`-minor-free graph on `n>=2` vertices has at most `2n-3` edges.
