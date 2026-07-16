# A planar contracted-root barrier in the five-support star branch

**Status:** explicit counterexample to the intermediate claim stated below;
the deterministic checker
[`hc7_star_kernel_contracted_root_planar_barrier_verify.py`](hc7_star_kernel_contracted_root_planar_barrier_verify.py)
reconstructs the graph and verifies the finite assertions.  This note has
not yet received a separate internal audit.  It is not a counterexample to
the five-support star reduction or to Hadwiger's conjecture for `t=7`.

## 1. The false local implication

The following proposed way to finish the five-support star branch is false.

> Let `u,v` be two vertices of a highly connected graph `J`, and let
> `e,f` be disjoint edges of `H=J-{u,v}`.  Suppose that `e` is anticomplete
> to `u` and adjacent to `v`, while `f` is anticomplete to `v` and adjacent
> to `u`.  Suppose also that a literal `K_5` consists of `e`, `f`, and one
> further vertex.  If contracting `e` and `f` leaves a four-connected
> graph, then the second literal `K_5` eliminates the planar/cofacial
> alternative of the rooted-`K_4` theorem, or else `H` contains disjoint
> connected subgraphs which contain `e,f` and meet `N_J(u),N_J(v)`,
> respectively.

The construction below refutes this even when `J` and the contracted graph
are five-connected and `H` is four-connected.

## 2. A general planar obstruction

We first isolate the elementary topological mechanism.

### Lemma 2.1 (facial four-cycle blocks the paired repair)

Let `Q` be a plane graph in which

\[
                         C=u v a b u
\]

is the boundary of a face.  Put `K=Q-{u,v}`.  There do not exist
vertex-disjoint paths in `K`, one joining

\[
       a\quad\hbox{to}\quad N_Q(u)-\{v,b\},
\]

and the other joining

\[
       b\quad\hbox{to}\quad N_Q(v)-\{u,a\}.
\]

#### Proof

Suppose that such paths exist.  Call them `P_a` and `P_b`, and let their
other ends be `x` and `y`, respectively.  Replace either path by the
subpath ending at its first eligible end if necessary, so both paths are
simple.  The curve

\[
                   u x\;\cup\;P_a\;\cup\;a v\;\cup\;v u
\]

is a simple cycle `D`.  The vertex `b` lies on the side of `D` containing
the facial sector between `vu` and `va`.  Since `uv` and `va` are
consecutive around `v` on that facial side, every edge from `v` to a
vertex outside `{u,a}` starts in the opposite rotation sector.  In
particular, `vy` starts on the other side of `D`.  The edge `vy` cannot
cross `D`, and `y` is not on `D` because `P_a` and `P_b` are disjoint.
Thus `y` and `b` lie on opposite sides of `D`.

But `P_b` avoids `u,v` and is disjoint from `P_a`, including its end `a`.
It is therefore disjoint from `D`, contradicting the Jordan curve theorem.
\(\square\)

### Lemma 2.2 (cofacial induced four-cycle is facial)

Let `Q` be a three-connected plane graph.  If an induced four-cycle `C`
has all four vertices incident with one face, then `C` is the boundary of
that face.

#### Proof

The boundary of every face in a three-connected plane graph is a cycle.
The cyclic order of the four vertices on the common facial boundary must
agree, up to reversal, with their order on `C`; otherwise two independent
edges of `C` cross in the disk complementary to the face.  If the facial
arc between two consecutive vertices of `C` had an internal vertex, that
arc together with their edge in `C` would enclose all of its internal
vertices behind its two ends.  Those two ends would be a vertex cut,
contrary to three-connectivity.  Every such facial arc is therefore one
edge, so the face boundary is exactly `C`. \(\square\)

## 3. The concrete graph

Let `T` be the 32-vertex planar triangulation constructed as follows.  Start
with the standard icosahedral graph on vertices `0,...,11`.  Add one vertex
for each of its twenty triangular faces, join it to the three vertices on
that face, and join two new vertices when their corresponding faces share
an edge.  This is the planar dual of the truncated icosahedron.  The
checker verifies that `T` is five-connected.

With the deterministic face ordering used by the checker, delete the edge

\[
                              ua=12\,13.
\]

Its two common neighbours in `T` are

\[
                              v=0,\qquad b=1.
\]

Write `Q=T-ua`.  The checker verifies that `Q` remains five-connected and
that

\[
                              u v a b u                 \tag{3.1}
\]

is the boundary of a face.  The other face on the edge `ab` has third
vertex

\[
                              p=18.
\]

Now replace `a` by an adjacent pair of true twins `a,a'`, and replace `b`
by an adjacent pair of true twins `b,b'`.  In particular all four edges
between `{a,a'}` and `{b,b'}` are present.  Call the resulting graph `J`,
and put

\[
                e=aa',\qquad f=bb',\qquad H=J-\{u,v\}. \tag{3.2}
\]

Contracting `e` and `f` recovers `Q`.  Moreover:

1. `J` is five-connected;
2. `H` is four-connected;
3. `e` is anticomplete to `u` and complete to `v`;
4. `f` is anticomplete to `v` and complete to `u`; and
5. `{a,a',b,b',p}` induces a literal `K_5`.

There is nevertheless no paired repair in `H`.  Indeed, suppose disjoint
connected subgraphs `A,B` of `H` contained `e,f`, respectively, with `A`
meeting `N_J(u)` and `B` meeting `N_J(v)`.  The subgraph `A` cannot use
`b` or `b'`, because both lie in `B`; similarly, `B` cannot use `a` or
`a'`.  Contract the twin pairs and take shortest paths inside the images
of `A,B` from `a,b` to the respective boundary-neighbour sets.  This gives
the two paths forbidden by Lemma 2.1 in `Q-{u,v}`.

The checker independently encodes all possible pairs of such paths as two
vertex-disjoint directed simple flows.  Every terminal choice is
unsatisfiable.

## 4. Extension to all five normalized supports

The obstruction is compatible even with the complete five-edge incidence
pattern and connectivity stronger than the host hypothesis, although not
with the target-free hypothesis.

Add three new vertices `r,s,t` to `H`, and make

\[
                         L_0=\{u,v,r,s,t\}
\]

a clique.  Retain the old adjacencies from `u,v` into `H`.  On the
four-clique `U={a,a',b,b'}`, define

\[
\begin{array}{c|ccccc}
q     &u&v&r&s&t\\ \hline
e_q   &aa'&bb'&ab&ab'&a'b.
\end{array}                                                \tag{4.1}
\]

For each of `r,s,t`, join `q` to every vertex of `H` except the two ends
of `e_q`.  Call the resulting graph `G_0`.  The checker verifies:

1. `G_0` is eight-connected;
2. the five edges in (4.1) are distinct;
3. `e_q` is anticomplete to `q` and collectively adjacent to every vertex
   of `L_0-{q}`; hence
   `(L_0-{q}) union V(e_q)` supports the normalized five-bag model for
   every `q`; and
4. `U union {p}` remains a literal `K_5` disjoint from `L_0`.

The selected disjoint pair `e_u,e_v` still has no paired repair, because
its exterior is the unchanged graph `H`.  Thus neither seven-connectivity
nor the simultaneous five-edge incidence pattern eliminates this chosen
facial obstruction by itself.

The extension is deliberately **not** target-free.  For example, the
disjoint connected subgraphs

\[
                  \{8,a,b'\},\qquad \{b,a',15\}
\]

repair `e_s,e_t`, respectively, and together with the five singleton
vertices of `L_0` give an explicit `K_7`-minor model.  Therefore this
extension does not refute a strategy which uses `K_7`-minor-freeness to
choose a different disjoint pair.  It pinpoints that this global
target-free information, rather than the bare five-edge incidence, must be
used.

## 5. What the second literal clique really forces

The construction also identifies the exact residue of the second-clique
argument in the genuine star setup.  Let `L={ell_1,...,ell_5}` be the
literal leaf clique, choose disjoint normalized defect edges `e_i,e_j`, put

\[
 J=G-(L-\{\ell_i,\ell_j\}),
 \qquad Q=J/(e_i,e_j),
\]

and use the four roots consisting of `ell_i,ell_j` and the two contracted
edges.  Suppose `Q` is four-connected and has no rooted `K_4` at these
roots.  Theorem 6 of Fabila-Monroy and Wood,
[*Rooted K4-Minors*](https://doi.org/10.37236/3476), makes `Q` planar and
the roots cofacial.

Let `Y` be the second literal `K_5` supplied by the star-kernel theorem,
and let `r` be the number of `e_i,e_j` wholly contained in `Y`.  The image
of `Y` in `Q` is a literal clique of order `5-r`.

* If `r=0`, this is a literal `K_5`, contradicting planarity.
* If `r=1`, it is a literal `K_4`.  A four-connected planar graph of order
  at least five has no literal `K_4`: in a plane `K_4`, one of its facial
  triangles separates every additional vertex from the opposite clique
  vertex.

Consequently `r=2`.  Both defect edges lie in `Y`; since they avoid the
star centre `p`, they partition `Y-{p}`.  Their contracted images, together
with `ell_i,ell_j`, induce the four-cycle (3.1), and Lemma 2.2 makes it the
common facial boundary.  Thus the second `K_5` compresses the planar branch
to the double-internal configuration realized above, but does not eliminate
it.

## 6. Exact scope

The basic graph `J` omits three leaves, while the extension `G_0` supplies
the full leaf clique and all five normalized six-vertex supports.  Neither
construction supplies the hypotheses that must do any remaining work.  In
particular, they do **not** provide:

* a `K_7`-minor-free host (the extension has the explicit `K_7` model above);
* seven-contraction-criticality, proper-minor six-colourings, or the exact
  private-transversal family.

It proves that the disjoint second literal `K_5`, rooted-quotient
four-connectivity, all five normalized local supports, and even stronger
connectivity do not force the selected paired repair.  Any successful
argument must use `K_7`-minor-freeness to coordinate the choice of defect
edges, the proper-minor colouring data, the private-transversal condition,
or another genuinely global hypothesis.
