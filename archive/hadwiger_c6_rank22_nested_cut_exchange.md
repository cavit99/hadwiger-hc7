# Rank-two C6 transitions: pole orientation and exact-cut descent

## 1. Scope

This note records two rigorous consequences of the canonical opposite-visible
two-cut state in the unresolved `C6 dotunion K1` boundary.  They do not close
the full SPQR residue.  They replace an arbitrary canonical two-cut transition
by (i) one binary pole orientation on each side and (ii) strictly smaller
exact seven-cuts with fixed boundary cores.  No assumption that the two
completed sides are R-torsos is needed: the orientation argument applies
to every component bridge of a two-cut in a two-connected shore.

Write the six missing-cycle labels as `c0,...,c5`, put

\[
 M_i=\{c_i,c_{i+3}\}\quad(i=0,1,2),
\]

and let `z` be universal in the original seven-boundary.  Up to a dihedral
symmetry, the canonical maximal opposite-visible two-cut has components
`A,B` and poles `p,q` with

\[
 N_S(A)=S-M_1,\qquad N_S(B)=S-M_0,
 \qquad N_S(p),N_S(q)\subseteq M_2\cup\{z\}.       \tag{1.1}
\]

Thus `c0,c3` occur only on the `A` side, `c1,c4` only on the `B`
side, and `c2,c5` are the shared portal labels.

## 2. The pole-orientation lemma

For a side `A`, call orientation 0 feasible if there are disjoint paths

\[
 P_0\longrightarrow p,\qquad P_3\longrightarrow q,             \tag{2.1}
\]

and call orientation 1 feasible when the two poles are interchanged.
Here `P_i=N_D(c_i)`, and the starts are required to be distinct.  Define
the orientations of `B` analogously, using `P1,P4` in that order.

### Lemma 2.1 (unique opposite pole states)

Assume `D` is two-connected, the six portal classes have an SDR, and there
is no `P0-P1 | P3-P4` linkage in `D`.  Then each side has exactly one
feasible orientation, and the two feasible orientation bits are different.

#### Proof

First use the standard bridge fact that

\[
 H_A=D[A\cup\{p,q\}]+pq                              \tag{2.2}
\]

is two-connected; the same holds for `B`.  Indeed both poles have a
neighbour in `A`, since otherwise the other pole separates `A` in `D`.
Thus `H_A` is connected.  If `x in A`, every component of `A-x` has a
neighbour in `{p,q}`: a component without one has all its neighbours in
`D` contained in `{x}`, contradicting two-connectivity of `D`.  The edge
`pq` therefore joins all components of `H_A-x`.  If `x` is one of the
poles, the connected graph `A` and the other pole (which has a neighbour
in `A`) remain connected.  Hence `H_A` has no cutvertex.

The SDR supplies distinct starts in `P0,P3` on the `A` side and in
`P1,P4` on the `B` side.  The two-set form of Menger's theorem in the
two-connected bridge gives a linkage from each start pair onto the two
distinct poles.  Shorten each path when it first reaches `{p,q}`.  The
paths then avoid the added edge `pq`, so they are literal paths of `D`.
Thus both orientation sets are nonempty.

If one feasible orientation of `A` has the same bit as one feasible
orientation of `B`, join the two paths with endpoint `p`, and separately
join the two paths with endpoint `q`.  The interiors of the sides are
disjoint, so these unions are disjoint connected carriers for

\[
 P_0P_1\mid P_3P_4,
\]

contrary to the hypothesis.  Since both orientation sets are nonempty,
one side cannot contain both bits: either bit would agree with the fixed
bit available on the other side.  The same applies symmetrically.  Hence
both sets are singletons and their bits differ.  \(\square\)

This is precisely the binary `web flip` which the invalid one-frame SPQR
argument tried to infer.  Here it follows from actual two-fans in arbitrary
two-cut bridges and the full crossless state, without claiming that a face
survives reflection or that a virtual edge is literal.

In particular, the lemma is uniform over every canonical contact lock in an
SPQR tree.  It does not depend on either incident node being an R-node: an
arbitrary `{p,q}`-bridge, completed by the virtual edge `pq`, already has the
two-connectivity needed for the unordered two-fan.

### Lemma 2.2 (shared-label pins)

Retain Lemma 2.1 and also exclude the internal antipodal linkages

\[
 P_2P_3\mid P_5P_0,
 \qquad P_1P_2\mid P_4P_5.                         \tag{2.3}
\]

Then:

* if `p in P5` and `q in P2`, the orientation bits are `(A,B)=(1,0)`;
* if `p in P2` and `q in P5`, the bits are `(A,B)=(0,1)`.

In particular both displayed incidence patterns cannot hold at once.

#### Proof

Under the first incidence pattern, orientation 0 on `A` would turn its
two disjoint pole paths into carriers for `P5-P0` and `P2-P3`, forbidden
by (2.3).  Hence `A` has bit 1.  Orientation 1 on `B` would analogously
give carriers for `P1-P2` and `P4-P5`; hence `B` has bit 0.  The second
case is the symmetric calculation.  If both patterns held, each side
would be forced to have both opposite values.  \(\square\)

Thus every surviving rank-two transition is not an arbitrary SPQR flip:
all shared-label incidences at the two poles must respect one coherent
binary orientation.

## 2.3 A colourful rooted-`K4` alternative on each bridge

The same canonical rows expose a rooted-model principle which does not
depend on a choice of web face.

### Lemma 2.3 (four-class Hall alternative)

The four portal classes

\[
 P_0\cap A,\quad P_2\cap A,\quad P_3\cap A,\quad P_5\cap A
                                                               \tag{2.4}
\]

have an SDR unless `|A|<=3`.  Symmetrically,
`P1 cap B,P2 cap B,P4 cap B,P5 cap B` have an SDR unless `|B|<=3`.

#### Proof

Suppose Hall fails on the `A` side.  For a nonempty subfamily indexed by
`I subseteq {0,2,3,5}`, let `U` be the union of its portal sets and put
`r=|I|`; then `|U|<=r-1`.  If `A-U` is nonempty, a component `C` of
`A-U` has all its external neighbours among

\[
 U\cup\{p,q,z\}\cup\{c_i:i\in\{0,2,3,5\}-I\}.
\]

This set has order at most

\[
 (r-1)+3+(4-r)=6
\]

and separates `C` from the old opposite shore, contrary to
seven-connectivity.  Hence `A=U` and `|A|<=r-1<=3`.  The proof for `B`
is identical. \(\square\)

The argument has the following parameter-uniform form.  Let `G` be
`k`-connected, let `A` lie behind two nonboundary gates `p,q`, and suppose
its old-boundary row is

\[
                         L\dot\cup\{z\},qquad |L|=k-3.
\]

For `ell in L`, put `P_ell=N_A(ell)`.  Then the family
`(P_ell:ell in L)` has an SDR unless `|A|<=k-4`.  Indeed a Hall-deficient
subfamily of order `r` has union `U` of order at most `r-1`; a component
of `A-U`, if present, is separated from the far shore by

\[
 U\cup\{p,q,z\}\cup(L-I),
\]

of order at most `(r-1)+3+(k-3-r)=k-1`.  Otherwise `A=U` has order at
most `k-4`.  Thus the distinct-root supply in Lemma 2.3 is itself a
uniform two-gate portal-Hall principle, not a peculiarity of six labels.

### Lemma 2.4 (dominating-edge rooted completion)

Choose distinct representatives `a_i in P_i cap A` for
`i in {0,2,3,5}`.  If the completed bridge

\[
                       H_A=D[A\cup\{p,q\}]+pq
\]

has a `K4` minor rooted at `a0,a2,a3,a5`, then `G` has a `K7` minor.
The symmetric statement holds on `B`.

#### Proof

First expand a possible use of the virtual edge `pq` through the connected
other component `B`.  If `p,q` lie in one rooted branch bag, add a
`p-q` path through `B` to that bag.  If they lie in two different bags and
`pq` supplies their adjacency, split such a path at one edge and add its
two sides to the two bags.  In every other case the virtual edge is unused.
This gives four literal rooted clique bags in `D`.

Adjoin `c_i` to the bag rooted at `a_i`, for
`i in {0,2,3,5}`.  Add as the other three bags the old full shore `H`,
the singleton `{z}`, and the connected boundary edge `{c1,c4}`.  The four
rooted bags remain pairwise adjacent.  Each sees `H` and `z` through its
distinct boundary anchor.  Each anchor in `{c0,c2,c3,c5}` is adjacent to
at least one of `c1,c4` in the complement-of-`C6` boundary, and fullness
gives all adjacencies from `H` to the last two boundary bags.  These seven
bags form a `K7` model. \(\square\)

Consequently, when `|A|>=4`, every four-root choice supplied by
Lemma 2.3 is a rooted-`K4` obstruction in the completed bridge.  This is
the label-preserving form in which rooted-`K4` structure theory may be
applied: a rooted model closes immediately, while its failure must expose
a rooted web or a further two-separation.  No independently chosen portal
representatives are identified across different linkage witnesses.

## 3. Every canonical transition descends to an exact seven-cut

The descent is an instance of a parameter-uniform two-gate principle.

### Theorem 3.0 (uniform two-gate full descent)

Let `G` be `k`-connected, let `S` be a `k`-cut, and suppose `G-S` has
exactly two connected components `D,H`, both full to `S`.  Suppose
`{p,q}` separates the two-connected shore `D` into exactly two components
`A,B`.  Assume

\[
 |N_S(A)|=|N_S(B)|=k-2,                            \tag{3.0a}
\]

and that each old boundary vertex missed by one interior is contacted by
the other:

\[
 S-N_S(A)\subseteq N_S(B),\qquad
 S-N_S(B)\subseteq N_S(A).                         \tag{3.0b}
\]

Then both

\[
              N_S(A)\cup\{p,q\},\qquad
              N_S(B)\cup\{p,q\}                  \tag{3.0c}
\]

are `k`-cuts with exactly two full shores, one of which is respectively
`A` and `B`.

#### Proof

Two-connectivity of `D` makes each pole adjacent to each component of
`D-{p,q}`.  Hence

\[
 N_G(A)=N_S(A)\cup\{p,q\},
\]

which has order `k` by (3.0a), and every member of this set sees `A`.
After deleting it, all remaining vertices outside `A` form one connected
component: `B` is connected, the two vertices of `S-N_S(A)` attach to
`B` by (3.0b), and the old full shore `H` attaches to those old boundary
vertices.  Every old-boundary member of `N_S(A)` sees `H`, while both
poles see `B`; consequently this opposite component is also full to the
new cut.  Interchanging `A` and `B` proves the second assertion. \(\square\)

The theorem is label-free and valid for every `k`.  The `C6` transition
below is its `k=7` instance, with the two missed label pairs prescribed by
the exact contact atlas.

### Lemma 3.1 (nested full cut)

Assume the original cut `S` has exactly two full shores `D,H`, and
`D-{p,q}` has exactly the two components `A,B` satisfying (1.1).  Then

\[
 S_A=\{p,q,c_0,c_2,c_3,c_5,z\}=N_G(A)              \tag{3.1}
\]

is an exact seven-cut.  The graph `G-S_A` has exactly two components,
and both are full to `S_A`.

#### Proof

Equation (1.1) and the fact that `p,q` are the two gates give (3.1).
The component `A` is one shore.  The other vertices consist of `B`, the
two omitted old boundary labels `c1,c4`, and the old opposite shore `H`.
The component `B` is adjacent to both `c1,c4` by (1.1), while `H` is full
to the old boundary; hence these vertices form one connected component.

Every vertex of `S_A` sees `A`: this is clear for the five old boundary
vertices from (1.1), and each pole has a neighbour in every component of
a separation pair in a two-connected graph.  Every vertex of `S_A` also
sees the opposite component: the poles see `B`, and the five old boundary
vertices see the old full shore `H`.  Thus both new shores are full.
\(\square\)

The construction is symmetric and gives more than one nested cut.

### Lemma 3.2 (two-sided nested full cuts)

Under the hypotheses of Lemma 3.1, also

\[
 S_B=\{p,q,c_1,c_2,c_4,c_5,z\}=N_G(B)              \tag{3.2}
\]

is an exact seven-cut.  The graph `G-S_B` has exactly two components,
and both are full to `S_B`.

#### Proof

The canonical contact rows give

\[
 N_G(B)=\{p,q\}\cup(S-M_0)
       =\{p,q,c_1,c_2,c_4,c_5,z\}.
\]

After deleting this set, one component is `B`.  All remaining vertices
form the connected set consisting of `A`, the omitted old boundary roots
`c0,c3`, and the old opposite shore `H`: the component `A` is adjacent to
both `c0,c3`, while the full shore `H` is adjacent to both of them.  Every
vertex of `S_B` sees `B`; the poles do so because they meet every component
of a two-separation of a two-connected graph, and the five old boundary
vertices do so by the contact row of `B`.  The poles see `A`, and each of the
five old boundary vertices sees `H`, so the other component is full as well.
\(\square\)

### Corollary 3.3 (quantitative fragment descent)

Every canonical rank-two/rank-two transition in a two-connected shore `D`
produces a full exact-seven fragment of order at most

\[
                  \frac{|D|-2}{2}.                 \tag{3.3}
\]

#### Proof

The two interiors partition `D-{p,q}`, so
`|A|+|B|=|D|-2`.  Lemmas 3.1 and 3.2 say that both `A` and `B` are full
fragments of exact seven-cuts.  Choose the smaller one. \(\square\)

### Corollary 3.4 (interaction with a globally minimum fragment)

If the split shore `D` itself is a globally minimum component among all
exact-seven cuts of `G`, then a canonical rank-two/rank-two transition in
`D` is impossible.

More generally, let `m` be the minimum order of any exact-seven fragment.
If the other old shore `H` has order `m` and the high-owner shore `D`
contains a canonical transition, then necessarily

\[
                         |D|\ge 2m+2.              \tag{3.4}
\]

#### Proof

In the first case, either of the proper nonempty sets `A,B` is an
exact-seven fragment by Lemmas 3.1--3.2 and has order strictly below
`|D|`, contradicting the choice of `D`.  In the second case the same
lemmas and global minimality give `|A|,|B|\ge m`; since
`D=A\dot\cup B\dot\cup\{p,q\}`, inequality (3.4) follows. \(\square\)

The first conclusion cannot be applied merely by choosing a globally
minimum fragment somewhere in the graph.  Frame ownership need not assign
the high-owner role to the smaller of the two old shores.  If the globally
minimum shore is the low owner, the proved conclusion is the size gap
(3.4), not a contradiction.  Thus global minimum-fragment normalization
eliminates every canonical transition *in the chosen minimum shore*, but
does not by itself eliminate a transition in its larger opposite shore.

## 4. The fixed boundary core

Order the new boundary as

\[
 (c_0,c_2,c_3,c_5,z,p,q)=(0,1,2,3,4,5,6).
\]

Its missing graph always contains

\[
 12,03,05,25,06,26.                                \tag{4.1}
\]

The only other possible missing edges are

\[
 15,35,45,16,36,46,56,                             \tag{4.2}
\]

corresponding respectively to absent `p-c2,p-c5,p-z`, the three
analogous `q` contacts, and the pole edge `pq`.

### Proposition 4.1 (zero/one pole-defect closure)

If none of the seven edges in (4.2) is missing, the two-full-shore
quotient already contains `K7`.  If exactly one is missing, then:

* a missing pole--boundary contact is one of the audited direct
  cyclic-hull types 4 or 13 and closes by the two-shore web theorem;
* a missing pole edge is seven-edge type 1, whose nonbipartite
  compatibility graph gives `K7` or a further nested exact seven-cut.

#### Certificate

`c6_rank22_nested_boundary_atlas.py` independently regenerates the
seven-edge atlas and asserts these identifications.  In the zero-defect
case it returns the explicit quotient bags

\[
 \{1\},\{3\},\{4\},\{5\},\{6\},\{h_A\},\{0,h_B\}.
\]

Every quotient model lifts through the two connected full shores.

## 5. Transverse one-step states at a multi-defect transition

The pole defects force genuine interface capacity, and minor-criticality
turns that capacity into two geometry-preserving operation states.

For `x in {p,q}`, let `r_x` be the number of missing contacts from `x`
to `{c2,c5,z}`, and put `epsilon=1` when `pq` is an edge and `0`
otherwise.  Write `d_A(x)=|N_A(x)|` and define `d_B(x)` similarly.

There are two connected allocations of the poles:

\[
 X_0=A\cup\{p\},\quad Y_0=B\cup\{q\},
 \qquad
 X_1=A\cup\{q\},\quad Y_1=B\cup\{p\}.             \tag{5.1}
\]

Their interface orders are

\[
 m_0=d_B(p)+d_A(q)+\epsilon,
 \qquad
 m_1=d_A(p)+d_B(q)+\epsilon.                       \tag{5.2}
\]

### Lemma 5.1 (transverse interface capacity)

One has

\[
 m_0+m_1\ge 8+r_p+r_q.                            \tag{5.3}
\]

Each interface contains a matching of size two.  In every surviving
canonical state, at least one shared contact among

\[
 pc_2,pc_5,qc_2,qc_5                               \tag{5.4}
\]

is absent; consequently `r_p+r_q>=1` and one allocation in (5.1) has
at least five interface edges.

#### Proof

The canonical rows give exactly `3-r_p` old-boundary neighbours of `p`.
The pole has no neighbour in the old opposite shore, so minimum degree
seven gives

\[
 d_A(p)+d_B(p)\ge 7-(3-r_p)-\epsilon
                    =4+r_p-\epsilon.              \tag{5.5}
\]

The analogous inequality holds for `q`.  Adding them and then adding the
two copies of `epsilon` in (5.2) proves (5.3).

Both poles meet both components.  Thus `E(p,B)` and `E(q,A)` supply two
independent edges in the first interface, while `E(p,A)` and `E(q,B)` do
so in the second.  Finally, if all four edges in (5.4) were present, both
incidence patterns in Lemma 2.2 would hold, which is impossible.  The last
claim follows from (5.3).  \(\square\)

### Lemma 5.2 (two transverse critical-state witnesses)

Assume `G` is proper-minor-minimal non-six-colourable.  There are distinct
interface edges

\[
 e_0\in E(p,B)\subseteq E(X_0,Y_0),
 \qquad
 e_1\in E(p,A)\subseteq E(X_1,Y_1)                 \tag{5.6}
\]

and six-colourings of `G-e_i` inducing boundary states `Pi_i` on the old
boundary `S`, such that:

1. deleting `e_i` preserves both connected pieces in (5.1), their fixed
   contact rows `S-M1,S-M0`, the covering property, and a remaining
   interface edge;
2. `Pi_i` extends over the operated shore `D-e_i` and the old opposite
   shore, but not over the original shore `D`; and
3. if `alpha_i` is the common colour of the ends of `e_i`, then for every
   other colour `gamma`, either `G[D]-e_i` has an
   `alpha_i/gamma` path between those ends, or their two bichromatic
   components are distinct and both anchored at `S`.

#### Proof

Choose the edges in (5.6).  In the first allocation an edge of `E(q,A)`
remains after deleting `e0`; in the second an edge of `E(q,B)` remains
after deleting `e1`.  Hence all geometry in item 1 survives literally.

Minor-criticality colours each proper minor `G-e_i`.  Restoring `e_i`
would colour `G` unless its ends have one common colour `alpha_i`.  The
restriction to `S` is accepted by the unchanged opposite shore and by
`D-e_i`.  If it extended over `D`, colour permutation and gluing would
six-colour `G`; hence the state is strict.  The final alternative is the
standard edge-critical Kempe switch: when the two endpoint components are
different, either one unanchored component can be switched and `e_i`
restored, or both are boundary-anchored.  \(\square\)

Lemma 5.2 gives two transverse operation witnesses on one fixed adhesion.
Each witness state is incompatible with the original shore while compatible
with its own operated shore and with the unchanged opposite shore.  The proof
does **not** show that `Pi_0` and `Pi_1` are distinct or mutually
incompatible; they may be the same equality partition of `S`.

The state strictness and Kempe alternative are the specialization of the
general bad-split interface exchange to the two allocations (5.1).  The new
content here is the canonical capacity calculation, the guaranteed surviving
second interface edge in each allocation, and the simultaneous placement of
the two operation witnesses across the same pole and the same two contact
rows.  Every failure of an internal rerouting still comes with two labelled
boundary anchors, but no cross-state compatibility conclusion is inferred.

There is also one genuinely coupled colouring witness, obtained by operating
on both transverse arms at once.

### Lemma 5.3 (coupled transverse star lock)

Choose `a in N_A(p)` and `b in N_B(p)`.  There is a six-colouring of

\[
                         G-\{pa,pb\}               \tag{5.7}
\]

in which `p,a,b` have one colour `alpha`.  For each other colour `beta`,
let `K_beta(a),K_beta(b)` be the two `alpha/beta` components at the
leaves.  Then:

1. at least one of `K_beta(a),K_beta(b)` contains `p`;
2. if `beta` is supported only through `b` and `gamma` only through `a`,
   then the unsupported components `K_beta(a),K_gamma(b)` either meet in
   an `alpha` vertex or have an edge between a `beta` vertex and a
   `gamma` vertex; and
3. consequently either one leaf is connected to `p` in all five
   bichromatic palettes, or the two nonempty exclusive-colour sets have
   the complete cross-interaction described in item 2.

Every vertex outside `{p,a,b}` which is adjacent in `G` to at least one of
`p,a,b` avoids `alpha` in this colouring.  Equivalently, every neighbour of
one of the three vertices in the operated graph (5.7) avoids `alpha`.

#### Proof

The vertices `a,b` are nonadjacent because they lie in distinct components
of `D-{p,q}`.  Contract the connected star on `p,a,b`, colour the proper
minor, and expand its image while leaving the two star edges deleted.  This
gives (5.7), and the contraction vertex forces every old neighbour of any
of the three vertices to avoid `alpha`.

If neither leaf component for some `beta` contained `p`, switch both of
them; the leaves move to `beta`, `p` stays `alpha`, and both star edges can
be restored.  For two oppositely exclusive colours, switch the two
unsupported components simultaneously.  The only possible new
monochromatic edge between them had colours `beta,gamma` before the
switches, so absence of both an intersection and such a cross-edge would
again restore the star.  These contradictions prove items 1--2.  If one
exclusive-colour set is empty, the opposite leaf supports all five
colours; otherwise item 2 applies to every cross pair, proving item 3.
\(\square\)

Unlike two unrelated edge colourings, Lemma 5.3 aligns all five palettes in
one state.  Its unresolved residue is concrete: either a full five-colour
fan is concentrated through one side of the two-cut, or two exclusive
palette families form a complete interaction grid.  Turning that fan/grid
into the colourful rooted `K4` of Lemma 2.4, or showing that all its
`alpha` intersections lie behind one colour-gluable adhesion, is the next
new step.

The exact contact rows force one whole side of the interaction grid to meet
one named adhesion of order six.

### Lemma 5.4 (exclusive-family six-gate anchoring)

In the colouring of Lemma 5.3 put

\[
\begin{aligned}
 E_B&=\{\beta:p\in K_\beta(b),\ p\notin K_\beta(a)\},\\
 E_A&=\{\gamma:p\in K_\gamma(a),\ p\notin K_\gamma(b)\}.
\end{aligned}                                      \tag{5.8}
\]

Define the two six-vertex first-exit gates

\[
\begin{aligned}
 T_A&=S_A-\{p\}=\{q,c_0,c_2,c_3,c_5,z\},\\
 T_B&=S_B-\{p\}=\{q,c_1,c_2,c_4,c_5,z\}.
\end{aligned}                                      \tag{5.9}
\]

Then one of the following holds.

1. One leaf supports all five colours from `p` (the concentrated-fan
   outcome of Lemma 5.3).
2. Both exclusive sets in (5.8) are nonempty and every component
   `K_beta(a)`, `beta in E_B`, meets `T_A`.
3. Both exclusive sets are nonempty and every component
   `K_gamma(b)`, `gamma in E_A`, meets `T_B`.

Thus in the genuine grid case, one entire exclusive palette family is
anchored at one named adhesion of order six.  Every cross-interaction in
which the opposite component stays in its own interior is forced to pass
through that adhesion.

#### Proof

If one exclusive set is empty, the other leaf supports every colour, as in
Lemma 5.3.  Assume both are nonempty.  If outcome 2 fails, choose
`beta in E_B` with `K_beta(a)` disjoint from `T_A`.  This component contains
`a`, does not contain `p`, and can leave `A` only through
`N_G(A)={p} union T_A`; hence it is contained in `A`.  If outcome 3 also
fails, some `K_gamma(b)`, `gamma in E_A`, is similarly contained in `B`.

The components `A,B` are anticomplete.  The two selected Kempe components
therefore neither meet nor have an edge between them, contradicting item 2
of Lemma 5.3.  At least one of outcomes 2--3 follows.  \(\square\)

This is the first conversion of the coupled star state into the requested
adhesion alternative.  It does not yet prove colour gluing: several
different palette components may use the same `alpha` vertex of the
six-gate set.  The remaining alternatives are now sharply separated into
a concentrated five-colour fan and a six-gate anchored interaction grid.

The proof is parameter-uniform.  In a `k`-critical graph, let `a,b` be
nonadjacent neighbours of `p` lying in anticomplete regions `A,B`, with

\[
 N(A)\subseteq A\cup\{p\}\cup T_A,
 \qquad N(B)\subseteq B\cup\{p\}\cup T_B.
\]

The colouring obtained by contracting the star `p-a-b` has `k-2`
non-alpha palettes.  Either one leaf is Kempe-connected to `p` in all of
them, or both exclusive families are nonempty and one whole family meets
its named gate `T_A` or `T_B`.  This **coupled-star gate theorem** uses no
`C6` labels; only the later six-gate size and alpha bound are specific to
the present boundary.

The possible coincidence at the gate has a bounded exact form.

### Lemma 5.5 (palette-labelled anchors or a three-vertex alpha warehouse)

Suppose outcome 2 of Lemma 5.4 holds.  Put

\[
 Z_\alpha=\{t\in T_A:c(t)=\alpha\}.                 \tag{5.10}
\]

Partition `E_B` into the colours `beta` for which
`K_beta(a) cap T_A` contains a `beta`-coloured vertex and the remaining
colours.  The first subfamily has distinct colour-labelled representatives
in `T_A`.  Every component belonging to the remaining subfamily meets
`Z_alpha`, and

\[
                           |Z_\alpha|\le3.          \tag{5.11}
\]

The symmetric assertion holds in outcome 3 with `T_B`.

#### Proof

Every vertex of the bichromatic component `K_beta(a)` has colour `alpha`
or `beta`.  Hence an intersection with `T_A` is either a colour-labelled
`beta` anchor or lies in `Z_alpha`.  Anchors carrying different non-alpha
colours are automatically distinct, proving the asserted partial
transversal.

On the five old boundary vertices in `T_A`, an alpha colour class is an
independent set of the boundary graph.  The vertex `z` is universal.  On
`{c0,c2,c3,c5}` the only missing boundary edges are `c0c5` and `c2c3`,
so such an independent set has order at most two.  The additional gate
vertex `q` raises the bound by at most one, proving (5.11).  \(\square\)

Thus the grid branch has a palette-labelled-or-coherent-overlap shape: it
exposes distinct colour-labelled gate representatives for one subfamily,
while every remaining palette meets an alpha set of cardinality at most
three.  These are **palette** labels, not the portal classes `P_i`; the
partial transversal does not by itself satisfy the Hall hypothesis of
Lemma 2.4.  Moreover “warehouse” means only a common set of at most three
vertices; it asserts neither three disjoint routes nor three distinct
representatives.  The missing theorem is a protected-column lift aligning
palette anchors with portal classes, together with a colour-gluing rule when
the warehouse is used.

## 6. Exact remaining gap

Modulo another exact-cut descent, a canonical two-cut survivor
therefore has all of the following simultaneous structure:

1. one opposite binary pole orientation on the two completed sides;
2. every shared-label pole incidence respects that orientation; and
3. the nested boundary has at least two additional pole defects beyond
   the fixed core (4.1).

It also has one transverse interface of order at least five, the two
strict, Kempe-decorated states of Lemma 5.2, and the single-state coupled
fan/grid of Lemma 5.3.  In the grid branch, Lemma 5.4 anchors one whole
exclusive family at one of the two explicit six-gate adhesions, and
Lemma 5.5 reduces its overlap to a three-vertex alpha warehouse.

This is an infinite-family reduction and an actual labelled-rerouting
lemma, but not a closure of `C6 dotunion K1`.  The missing step is now
sharper: combine two or more pole defects with the proper-minor transition
state to obtain either a labelled rerouting across the unique orientation
or a common boundary colouring state.
