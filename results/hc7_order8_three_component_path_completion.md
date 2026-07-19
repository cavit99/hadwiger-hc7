# Completing two path-component configurations at an order-eight boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_three_component_path_completion_audit.md`](hc7_order8_three_component_path_completion_audit.md).
This note is not a proof of `HC_7`.

This note gives an explicit `K_7`-minor model when an order-eight boundary
has two other boundary-full components and the selected third component has
one of two specified path configurations.  The shared-portal conclusion is
uniform for every boundary containing two vertex-disjoint odd cycles.  The
strict-reversal conclusion requires an additional rooted `K_3` model in the
boundary; that condition is stated literally and is not asserted for all 82
boundary types.

Throughout, a connected subgraph is **`S`-full** if it is disjoint from `S`
and has a neighbour at every literal vertex of `S`.

## 1. The odd-cycle construction

### Lemma 1.1 (an odd cycle avoiding one prescribed vertex)

Let `S` have order eight, and suppose that `G[S]` contains two
vertex-disjoint odd cycles.  For every `d in S`, there is an odd cycle `C`
in `G[S-d]` of order three or five.  The cycle `C` has a `K_3`-minor model

\[
                         M_1,M_2,M_3                         \tag{1.1}
\]

whose union is `V(C)`.  Moreover, `S-V(C)` contains two distinct vertices
different from `d`.

#### Proof

At most one of the two vertex-disjoint odd cycles contains `d`, so the other
avoids `d`.  Two vertex-disjoint odd cycles in an eight-vertex set have
orders `(3,3)` or `(3,5)`.  Thus the cycle `C` avoiding `d` has order three
or five.

If `C` is a triangle, take its three vertices as the branch sets in (1.1).
If

\[
                         C=c_0c_1c_2c_3c_4c_0,
\]

take

\[
              M_1=\{c_0\},\qquad
              M_2=\{c_1,c_2\},\qquad
              M_3=\{c_3,c_4\}.
\]

These are three pairwise adjacent connected sets.  Finally,
`|S-V(C)|>=3`, and this complement contains `d`; hence it contains at least
two further vertices different from `d`. \(\square\)

## 2. A literal shared portal

### Theorem 2.1 (two full components complete an internal shared portal)

Let `G` be a graph and let `S subseteq V(G)` have order eight.  Suppose that
`G[S]` contains two vertex-disjoint odd cycles.  Let

\[
                        Q_0,Q_1,L,R
\]

be pairwise vertex-disjoint nonempty connected subgraphs of `G-S`, and let
`v` be a vertex outside their union and outside `S`.  Let `d,e` be distinct
vertices of `S`.  Assume that:

1. `Q_0` and `Q_1` are `S`-full;
2. `L` has a neighbour at every vertex of `S-{d}`;
3. `R` has a neighbour at every vertex of `S-{e}`; and
4. `v` has a neighbour in each of `L,R` and is adjacent to both `d,e`.

Then `G` contains a `K_7` minor.

#### Proof

Apply Lemma 1.1 to `d`, obtaining the odd cycle `C`, the `K_3`-minor model
`M_1,M_2,M_3`, and distinct vertices

\[
                  x_0,x_1 in S-(V(C) union \{d\}).       \tag{2.1}
\]

Consider the following seven sets:

\[
 Q_0\cup\{x_0\},\quad
 Q_1\cup\{x_1\},\quad
 L,\quad
 R\cup\{v\},\quad
 M_1,\quad M_2,\quad M_3.                              \tag{2.2}
\]

They are pairwise disjoint and connected.  The first two sets are connected
because `Q_0,Q_1` are `S`-full.  The fourth is connected by the edge from
`v` into `R`.

The first two sets are adjacent through an edge from `Q_0` to `x_1`.  Each
is adjacent to `L`, because `x_0,x_1 != d`, and each is adjacent to
`R union {v}`: the vertex `x_i` has a neighbour in `R` unless `x_i=e`, and
in that exceptional case it is adjacent to `v`.  The sets `L` and
`R union {v}` are adjacent through the edge from `v` into `L`.

Both `Q_i` are adjacent to every `M_j` by `S`-fullness.  Since `C` avoids
`d`, the subgraph `L` is adjacent to every `M_j`.  The connected subgraph
`R union {v}` has a neighbour at every vertex of `S`: `R` supplies all
vertices other than possibly `e`, and `v` supplies `e`.  It is therefore
adjacent to every `M_j`.  Finally, the three sets in (1.1) are pairwise
adjacent.  Hence (2.2) is an explicit `K_7`-minor model. \(\square\)

### Corollary 2.2 (the three-component internal shared-portal case)

Assume the boundary-full order-eight setting in which `G-S` has three
components, one component is the induced path

\[
                         P=p_0p_1\cdots p_m,
\]

and the other two components are `Q_0,Q_1`.  Suppose that the shared portal
in the overlapping-interval normal form is `p_q`, where `0<q<m`, and that
neither of the two path tails has already returned an actual order-seven
separation.  If `G[S]` contains two vertex-disjoint odd cycles, then `G`
contains a `K_7` minor.

#### Proof

The shared-portal normal form gives

\[
 L=P[0,q-1]\sim S-\{d\},\qquad
 R=P[q+1,m]\sim S-\{e\},
\]

while `p_q` is adjacent to `d,e` and to both nonempty tails.  Every component
of the boundary-full interface is `S`-full, so `Q_0,Q_1` satisfy Theorem
2.1. \(\square\)

## 3. A literal sufficient condition for strict reversal

The three subpaths used in the strict-reversal normal form overlap at two
portal vertices.  They therefore cannot be treated as three disjoint branch
sets while retaining all of their contacts.  The following statement uses
an honest disjoint cut of the path instead.

### Lemma 3.1 (two anchored full components and two one-defect path sides)

Let `S` have order eight.  Let `Q_0,Q_1,A,B` be pairwise vertex-disjoint
nonempty connected subgraphs of `G-S`.  Let `d,e` be distinct vertices of
`S`.  Assume that:

1. `Q_0,Q_1` are `S`-full;
2. `A` has a neighbour at every vertex of `S-{d}`;
3. `B` has a neighbour at every vertex of `S-{e}`; and
4. `A` and `B` are adjacent.

Suppose that `G[S]` has three pairwise disjoint, pairwise adjacent connected
subgraphs `M_1,M_2,M_3` and two further distinct vertices `x_0,x_1 in S`
such
that:

\[
 \begin{aligned}
 &x_0,x_1\notin \{d,e\}\cup V(M_1)\cup V(M_2)\cup V(M_3),\\
 &V(M_j)-\{d\}\ne\varnothing
   \quad\hbox{and}\quad V(M_j)-\{e\}\ne\varnothing
   \qquad(j=1,2,3).
 \end{aligned}                                         \tag{3.1}
\]

Then `G` contains a `K_7` minor.

#### Proof

The seven branch sets are

\[
 Q_0\cup\{x_0\},\quad Q_1\cup\{x_1\},\quad
 A,\quad B,\quad M_1,\quad M_2,\quad M_3.             \tag{3.2}
\]

They are disjoint and connected.  The two anchored full subgraphs are
adjacent to each other and to `A,B`, because both anchors avoid `d,e`.
The sets `A,B` are adjacent by hypothesis.  Each `Q_i` is adjacent to every
`M_j`.  Condition (3.1) gives a vertex of `M_j` different from `d` and a
possibly different vertex of `M_j` different from `e`; hence `A` and `B`
are both adjacent to every `M_j`.  The `M_j` are pairwise adjacent by
hypothesis.  Thus (3.2) is a `K_7`-minor model. \(\square\)

### Corollary 3.2 (application to a strict path reversal)

Assume the boundary-full order-eight setting in which `G-S` has three
components, one is the induced path in the no-order-seven-tail outcome of
the strict-reversal normal form, and the other two components are
`S`-full connected subgraphs `Q_0,Q_1`.  Choose any `k` with `b<=k<a` and
put

\[
                         A=P[0,k],\qquad B=P[k+1,m].
\]

Then `A,B` are disjoint adjacent connected subgraphs, `A` is adjacent to
every vertex of `S-{d}`, and `B` is adjacent to every vertex of `S-{e}`.
Consequently Lemma 3.1 completes the strict reversal whenever the boundary
objects in (3.1) exist.

#### Proof

The left tail `P[0,b]` is contained in `A` and is adjacent to `S-{d}`.
The right tail `P[a,m]` is contained in `B` and is adjacent to `S-{e}`.
The path edge `p_kp_{k+1}` joins `A` to `B`.  Apply Lemma 3.1. \(\square\)

## 4. Trust boundary

For the audited 82 three-component boundary types, the classification proves
that `G[S]` contains two vertex-disjoint odd cycles.  Thus Corollary 2.2
eliminates every **internal shared-portal** outcome of an induced path
component unless an order-seven separation was already returned.

This note does **not** establish any of the following:

- the shared-portal conclusion when `q` is an endpoint of the path;
- condition (3.1) for every strict-reversal boundary and every pair `d,e`;
- a disjoint full/one-defect pair obtained by duplicating either overlap
  vertex `p_b,p_a`;
- compatible six-colourings on an order-seven separation;
- the corresponding result when `G-S` has only two components; or
- `HC_7`.

The exact quotient analyzer
[`hc7_order8_shared_portal_quotient_probe.py`](../active/hc7_order8_shared_portal_quotient_probe.py)
checks the seven displayed branch sets over the finite 82-type list.  It is
falsification support only; the proofs above are independent of the
computation.  The check finds the boundary objects in Lemma 3.1 for 4,458
of the 4,592 ordered `(boundary,d,e)` choices and leaves 134 choices
uncovered by that displayed construction.  This count is not used to infer
anything about those remaining cases.

## 5. Dependencies

- the [overlapping-interval path normal form](../results/hc7_order8_overlapping_interval_normal_form.md), for the literal tail contacts and order-seven alternatives;
- the [three-component boundary classification](../results/hc7_order8_three_component_boundary_classification.md), only for the fact that each of the 82 surviving boundaries contains two vertex-disjoint odd cycles.
