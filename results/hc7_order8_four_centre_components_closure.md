# Four components behind a response centre force a `K_7` minor

**Status:** written proof; [separate internal audit](hc7_order8_four_centre_components_closure_audit.md)
GREEN.  This is an unbounded host-level closure inside the two-component
order-eight response problem.  It does not prove `HC_7`.

## 1. A connected bipartition lemma

### Lemma 1.1

Let `H` be connected and let `P_0,Q_0` be disjoint nonempty connected
subgraphs.  Then there is a partition

\[
                         V(H)=P\mathbin{\dot\cup}Q     \tag{1.1}
\]

such that `H[P]` and `H[Q]` are connected, `P_0 subseteq P`,
`Q_0 subseteq Q`, and an edge joins `P` to `Q`.

#### Proof

Contract `P_0` and `Q_0` separately and take a spanning tree of the
resulting connected graph.  Delete any edge on the tree path between the
two contracted vertices.  The two resulting tree components, expanded
through the contractions, give `P,Q`. \(\square\)

## 2. The four-component closure

### Theorem 2.1

Let `G` be a seven-connected, seven-contraction-critical graph.  Let `S`
be an eight-vertex set and let `C,C'` be distinct components of `G-S`,
where `C'` is adjacent to every vertex of `S`.  Let `v in C` have a
neighbour in `S`.  Suppose `C-v` has exactly four components

\[
                           A_1,A_2,A_3,A_4,            \tag{2.1}
\]

each adjacent to all but at most one vertex of `S`.  Then `G` contains an
explicit `K_7`-minor model.

#### Proof

Every `A_i` is adjacent to `v`, because `C` is connected.  We distinguish
whether one component contains two neighbours of `v`.

### Case 1: a component contains two centre neighbours

Suppose `A_1` contains distinct neighbours `a,b` of `v`.  For
`i=2,3,4`, let `m_i` denote the possible unique boundary vertex missed by
`A_i`; omit it if there is none.  Put

\[
                       M=\{m_i:2\le i\le4\}.           \tag{2.2}
\]

Choose `p_0 in N_G(v) intersect S` and set

\[
                       Y=S-(M\cup\{p_0\}).             \tag{2.3}
\]

Then `|Y|>=4`, and every member of `Y` is adjacent to each of
`A_2,A_3,A_4`.

In `G[A_1 union Y]`, apply set-Menger between `{a,b}` and `Y`.  If two
vertex-disjoint paths do not exist, a separator `Z` of order at most one
leaves one of `a,b` outside `Z`.  Let `R` be the component of
`G[A_1-Z]` containing that surviving source and separated from `Y`.
Componenthood of `A_1` in `C-v` gives

\[
                N_G(R)\subseteq \{v\}\cup M\cup\{p_0\}\cup Z,
                \qquad |N_G(R)|\le6.                  \tag{2.4}
\]

The other component `C'` lies outside `R union N_G(R)`, so (2.4)
contradicts seven-connectivity.  Hence there are two disjoint paths using
both sources and having distinct ends `x,y in Y`.  Truncate each at its
first vertex of `Y`; after deleting `x,y`, their remaining portions are
disjoint connected subgraphs of `A_1` containing `a,b`, respectively.
Lemma 1.1 extends them to a connected partition

\[
                         A_1=P\mathbin{\dot\cup}Q,     \tag{2.5}
\]

where `P,Q` are adjacent, `a in P`, `b in Q`, and
`P union {x}`, `Q union {y}` are connected.

It remains to choose representatives for `A_2,A_3,A_4`.  Put

\[
                         U=S-\{p_0,x,y\};              \tag{2.6}
\]

so `|U|=5`.  Greedily choose distinct `z_i in U` adjacent to `A_i`
for `i=2,3,4`, while forbidding a mutual defect pair

\[
          A_i\not\sim z_j\quad\hbox{and}\quad A_j\not\sim z_i.     \tag{2.7}
\]

At a step with `k` earlier representatives, at most `k` used vertices,
the one possible vertex missed by the current component, and at most one
reciprocal missed vertex are forbidden.  Since `k<=2`, fewer than the five
members of `U` are forbidden.  Thus the choice exists.

The following seven sets are pairwise disjoint and connected:

\[
 \{v\},\quad C'\cup\{p_0\},\quad P\cup\{x\},\quad Q\cup\{y\},
 \quad A_2\cup\{z_2\},\quad A_3\cup\{z_3\},
 \quad A_4\cup\{z_4\}.                               \tag{2.8}
\]

The first is adjacent to every component-derived bag through
`a,b` and one `v`--`A_i` edge, and to the second bag through `vp_0`.
The second bag meets every other non-singleton bag through fullness of
`C'`.  The two bags derived from `A_1` are adjacent by (2.5), and each is
adjacent to every bag derived from `A_2,A_3,A_4` because `x,y in Y`.
Finally, (2.7) guarantees pairwise adjacency among the last three bags.
Thus (2.8) is a `K_7`-minor model.

### Case 2: every component contains one centre neighbour

Assume each `A_i` contains exactly one neighbour `a_i` of `v`.  The four
vertices `a_1,...,a_4` are independent, because they lie in different
components of `C-v`.  Dirac's neighbourhood-independence inequality for a
seven-contraction-critical graph gives

\[
                    4\le\alpha(G[N_G(v)])\le d_G(v)-5.             \tag{2.9}
\]

Put `t=|N_G(v) intersect S|`.  There are no other neighbours of `v`, so
`d_G(v)=t+4`; equation (2.9) gives `t>=5`.

The four components collectively miss at most four vertices of `S`.
Consequently some

\[
       q\in N_G(v)\cap S
\]

is adjacent to every `A_i`.  Choose a different
`p_0 in N_G(v) intersect S` and put `U=S-{p_0,q}`, so `|U|=6`.
As above, greedily choose distinct representatives
`z_i in U` adjacent to `A_i`, without a mutual defect pair.  At the last
step, at most three used values, one current missed value and one
reciprocal missed value are forbidden, fewer than the six available
vertices.

Now the seven sets

\[
 \{v\},\quad C'\cup\{p_0\},\quad\{q\},
       \quad A_i\cup\{z_i\}\quad(1\le i\le4)          \tag{2.10}
\]

are pairwise disjoint and connected.  The vertex `v` meets all six other
bags; fullness of `C'` joins its bag to `{q}` and to every representative;
`q` meets every `A_i`; and the absence of reciprocal defects makes the
four component-derived bags pairwise adjacent.  Thus (2.10) is a
`K_7`-minor model. \(\square\)

## 3. Consequence for an order-eight response fan

### Corollary 3.1

Let `G` be seven-connected, seven-contraction-critical and
`K_7`-minor-free.  Let `S` be an eight-vertex set, let `C,C'` be distinct
components of `G-S`, assume `C'` is adjacent to every vertex of `S`, and
let `v in C` have a neighbour in `S`.  Then either

1. some component `A` of `C-v` has `|N_G(A)|=7`, and its full vertex
   neighbourhood is the boundary of an actual separation; or
2. `C-v` has at most three components.

#### Proof

The centre-component clique decoder gives the first outcome or leaves at
most four components.  In the absence of the first outcome, each remaining
component is adjacent to all but at most one vertex of `S`.  If exactly
four remain, Theorem 2.1 gives a `K_7` minor, contrary to the hypothesis.
Thus at most three remain. \(\square\)

This removes all component counts at least four without bounding the
orders of the components.

## 4. Exact contribution and trust boundary

The theorem is a reusable host-level exchange principle.  It converts
nearly complete boundary contact in four connected components into seven
branch sets in `G`, using contraction-criticality only in the exact
no-repeated-neighbour case.  The proof is not finite enumeration.

It does not close the cases in which `C-v` has one, two or three components,
nor does it prove that the returned order-seven separation carries one
complete equality partition through both shores.  Those remain the
response-coupling problem.

## 5. Dependencies

- Dirac's neighbourhood-independence inequality for contraction-critical
  graphs;
- vertex Menger's theorem; and
- elementary connected bipartition and representative selection.
