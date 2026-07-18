# Independent audit: two-vertex boundary-contact transversal

**Verdict:** **GREEN.**  The adjacent-transversal construction, the
nonseparating-path refinement, the three-cut obstruction, and the
alternating-web reduction are valid under the stated hypotheses.  Every
repair support, residual boundary-full subgraph, and separation boundary
used in the proof is a literal object in the host graph.  No edge added by a
web completion is treated as an edge of the host graph.

**Audited source:**
`results/hc7_two_vertex_boundary_contact_transversal.md`.

**Source SHA-256:**
`74825bfc670a9e24049eb2242d747c1096ee23b9e57264e3d4f36f59b181459b`.

## 1. Setup and terminology

Because `D` is a component of `G-T`, its external neighbourhood is contained
in `T`.  The hypothesis that a vertex remains outside `D union T` makes this
neighbourhood a genuine separator.  Seven-connectivity and `|T|=7` therefore
give the exact equality

\[
                         N_G(D)=T.
\]

Thus every portal set `P_t=N_D(t)` is nonempty.  The definition of a
boundary-contact transversal is literal: it asks that the chosen vertices
of `D` meet all seven portal sets.  In the special case used in Theorem 3.1,
where the transversal consists of the endpoints of an edge, that edge is a
connected subgraph adjacent to every member of `T`.

The source does not assume that a general two-vertex transversal is adjacent,
and it does not infer connectedness from the transversal property alone.

## 2. Elementary exact-boundary reductions

### Lemma 2.1

If `t` has the unique portal `z`, two-connectivity makes `D-z` connected and
nonempty.  It has no neighbour at `t`, so

\[
              N_G(D-z)\subseteq \{z\}\cup(T-\{t\}).
\]

The right side has order seven.  The fixed nonempty opposite side remains
outside this set, so seven-connectivity gives the reverse cardinality bound
and hence equality.  The conclusion is therefore an actual order-seven
separation boundary, not merely an upper bound on a neighbourhood.

### Lemma 2.2

If `z` is adjacent to `b` and to a member of `I`, the singleton subgraph on
`z` is a valid repair support.  Three-connectivity makes `D-z` connected.
For each `t in T`, either `z` is not a portal for `t`, or the exclusion of a
unique portal supplies another neighbour of `t` in `D-z`.  Thus `D-z` is a
literal residual boundary-full subgraph disjoint from the repair support.

## 3. Adjacent two-vertex transversals

### Theorem 3.1

After excluding Lemmas 2.1 and 2.2, the sets

\[
 X=N_D(b)-\{p,q\},\qquad
 Y=\left(\bigcup_{i\in I}N_D(i)\right)-\{p,q\}
\]

are nonempty.  If `X` were empty, the absence of a unique portal would force
both `p` and `q` to be portals for `b`; the transversal property for `I`
would then give a common repair vertex.  The same argument, with one fixed
member of `I`, proves that `Y` is nonempty.  Their intersection is empty by
the exclusion of a common repair vertex.

Deleting `p,q` from the three-connected graph `D` leaves a connected graph.
Consequently an `X-Y` path exists in `D-\{p,q\}`.  It is adjacent to `b` at
one end and to a member of `I` at the other, so it is a repair support.  The
literal edge `pq` is vertex-disjoint from that path and, because its endpoint
set is the transversal, is adjacent to every vertex of `T`.  It is therefore
a valid residual boundary-full subgraph.  No contraction or auxiliary edge
is used in this construction.

### Theorem 3.2

The external input is Tutte's nonseparating-path theorem in the following
form: if a graph `H` is three-connected and `x,y,w` are distinct, then
`H-w` contains an `x-y` path `P` such that `H-V(P)` is connected.  This is
the form recorded as Theorem 1.2.1 in Yingjie Qian, *Non-Separating Paths in
Graphs* (PhD dissertation, Georgia Institute of Technology, 2022), where it
is attributed to W. T. Tutte, *How to Draw a Graph*, Proceedings of the
London Mathematical Society (3) **13** (1963), 743--767.

Here `x,y` lie outside `\{p,q\}` and in the disjoint sets `X,Y`, while `w`
is the vertex produced by contracting `pq`; hence the three nominated
vertices in `D/pq` are distinct.  The returned path avoids `w`, so it is a
literal path of `D-\{p,q\}`.  Expanding `w` back into the connected edge
`pq` preserves connectedness of the complement of the path.  That complement
contains `p,q`, and the transversal property makes it boundary-full.  The
theorem correctly retains the exact-boundary alternative when a unique
portal is present.

### Lemma 3.3

For `|V(D)|>=5`, the simple contraction `H=D/pq` is two-connected.  Deleting
the contracted vertex leaves `D-\{p,q\}`, which is connected; deleting any
other vertex leaves a contraction of a connected vertex-deleted subgraph of
`D`.  If `H` is not three-connected, a two-cut exists.  A two-cut avoiding
the contracted vertex would lift to deletion of two vertices from `D`,
contradicting three-connectivity.  Thus it has the form `\{w,z\}`, and

\[
          H-\{w,z\}=D-\{p,q,z\}.
\]

This proves both directions of the asserted equivalence.  For every
component `A` of the latter graph, three-connectivity forces all of
`p,q,z` into `N_D(A)`.  Since all remaining neighbours of `A` lie in `T`,

\[
 N_G(A)=\{p,q,z\}\mathbin{\dot\cup}N_T(A).
\]

The fixed opposite side makes this a genuine separation.  Seven-connectivity
therefore gives `|N_T(A)|>=4`, with equality exactly the order-seven case.

## 4. Nonadjacent two-vertex transversals and the web outcome

### External Two Paths theorem

Lemma 2 of R. Fabila-Monroy and D. R. Wood, *Rooted K4-Minors*, Electronic
Journal of Combinatorics **20** (2013), #P64, states that for distinct
`s_1,t_1,s_2,t_2`, either there are disjoint paths joining `s_1` to `t_1`
and `s_2` to `t_2`, or the graph is a spanning subgraph of an
`(s_1,s_2,t_1,t_2)`-web.  The source applies this with

\[
             (s_1,t_1,s_2,t_2)=(x,y,p,q),
\]

so the resulting outer order is exactly `(x,p,y,q)`.  The orientation in
Theorem 4.1 is correct.

### Theorem 4.1

The one-vertex-transversal branch invokes the separately audited universal
boundary-contact theorem with the same hypotheses and conclusions.  In the
remaining branch, absence of a one-vertex transversal and of the two
elementary reductions forces, after interchanging `p,q` if necessary,

\[
 N_D(b)\cap\{p,q\}=\{p\},\qquad
 N_D(i)\cap\{p,q\}=\{q\}\quad(i\in I).
\]

The associated sets `X,Y` are nonempty, disjoint, and avoid `p,q`, so the
four terminals of the Two Paths theorem are distinct.  If the requested
linkage exists, its `x-y` path is a repair support and its disjoint `p-q`
path contains the full transversal, hence is a literal residual
boundary-full subgraph.  If no repair/residual pair exists, the linkage must
fail for every choice of `x in X`, `y in Y`, giving precisely the stated
alternating-web outcome for each choice.  The proof correctly refrains from
claiming that these choices have one common web completion.

## 5. Literal web attachments

### Corollary 4.2

Fix one web completion, let `K` be a facial triangle of its planar skeleton,
and let `A` be a component of `D-K` contained in the clique part associated
with `K`.  The completion permits no neighbour of a clique-part vertex
outside that clique part and `K`.  Since `A` is a component after deleting
`K`, this gives `N_D(A) subseteq K` using only literal edges of `D`.

At least one of the four outer web vertices lies outside the three-set `K`
and outside `A`, so `D-K` has another component.  Hence `N_D(A)` is a
separator.  Three-connectivity forces it to have order at least three, and
therefore

\[
                       N_D(A)=K.
\]

This conclusion uses the three vertices of the facial triangle only; it
does not assume that any of the three facial-triangle edges belongs to `D`.
Adding the boundary neighbours gives the literal equality

\[
                     N_G(A)=K\mathbin{\dot\cup}N_T(A).
\]

The nonempty opposite side and seven-connectivity yield
`|N_T(A)|>=4`, with equality an actual order-seven boundary.

The assertion that `D-A` is connected is also valid.  Every other component
of `D-K` must have all three vertices of `K` as neighbours, again by
three-connectivity.  One such component contains an outer web vertex and
connects all three vertices of `K` inside `D-A`; all further components
attach to those same three vertices.  Thus `D-A` is connected.  The outer
vertices `p,q` do not lie in an inserted clique part, so they remain in
`D-A`; a literal `p-q` path in `D-A` is boundary-full.

If `A` itself meets `b` and a member of `I`, it and that `p-q` path give the
excluded repair/residual pair.  Otherwise `A` misses `b` or both vertices of
`I`.  Together with `|N_T(A)|>=5` in a survivor, this yields exactly the two
disjoint alternatives in (4.4).

### Corollary 4.3

If an inserted clique part is nonempty, deleting its supporting facial
triangle leaves at least one literal component contained in that part, to
which Corollary 4.2 applies.  If all inserted parts are empty, the completion
is its planar skeleton and `D` is a spanning subgraph of that skeleton.
Deleting skeleton edges can merge faces but cannot destroy the fact that
`x,p,y,q` occur on a common face in their stated cyclic order.  Thus the
five-contact-component versus bare-planar-web dichotomy is valid.

## 6. Completion-edge and disjointness audit

No proof step uses an edge belonging only to a web completion:

- the repair and residual paths in Theorem 4.1 are paths of `D` returned by
  the linkage;
- Corollary 4.2 uses only vertex containment and literal neighbourhoods;
- connectivity of `D-A` is supplied by literal components and their forced
  literal contacts with the three separator vertices; and
- Corollary 4.3 states only that `D` is a spanning subgraph of the planar
  skeleton in its second outcome.

Every claimed repair support is disjoint from its accompanying residual:
the disjointness is immediate from the linkage in Theorem 4.1, from deletion
of the repair vertex in Lemma 2.2, or from the construction in
`D-\{p,q\}` in Theorems 3.1 and 3.2.

## 7. Trust boundary

The GREEN verdict is conditional on the exact hypotheses in the source:
an actual order-seven boundary, a three-connected component `D`, and a
boundary-contact transversal of order at most two.  The theorem does not:

- produce such a transversal in every `HC_7` residue;
- preserve a previously selected labelled minor model inside `D`;
- preserve or synchronize a boundary colouring across the separation;
- assert that the whole residual after an arbitrary repair path is
  connected, except in the explicit setting of Theorem 3.2; or
- prove `HC_7`.

These are scope limitations, not gaps in the audited conditional theorem.
