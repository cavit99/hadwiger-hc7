# A two-vertex boundary-contact transversal gives a repair or a web

**Status:** written proof; separate internal audit.  This is a
conditional structural theorem for one component behind an order-seven
separation.  It does not preserve a previously selected minor model or a
boundary colouring, and it does not prove `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph, let `T` be a set of seven vertices,
and let `D` be a component of `G-T`.  Assume that

\[
                 V(G)-(V(D)\cup T)\ne\varnothing .       \tag{1.1}
\]

Thus `T` is an actual boundary and seven-connectivity gives

\[
                         N_G(D)=T.                       \tag{1.2}
\]

Fix `b in T` and a two-element set

\[
                         I\subseteq T-\{b\}.             \tag{1.3}
\]

For `t in T`, its **portal set** in `D` is

\[
                         P_t=N_D(t).                     \tag{1.4}
\]

A set `W subseteq V(D)` is a **boundary-contact transversal** when
`W cap P_t` is nonempty for every `t in T`.  In particular, when `W`
consists of the two ends of an edge, that edge is a connected subgraph
adjacent to all seven boundary vertices.

A **repair support** is a connected subgraph of `D` adjacent to `b` and
to at least one member of `I`.  A **residual boundary-full subgraph** is
a connected subgraph of `D`, disjoint from the repair support, adjacent
to every member of `T`.

We use the classical Two Paths theorem in the following form.  For four
distinct vertices `s_1,t_1,s_2,t_2` of a graph `H`, either `H` has
vertex-disjoint paths joining `s_1` to `t_1` and `s_2` to `t_2`, or `H`
is a spanning subgraph of an `(s_1,s_2,t_1,t_2)`-web.  This is Lemma 2
of R. Fabila-Monroy and D. R. Wood, *Rooted K4-Minors*, Electronic
Journal of Combinatorics **20** (2013), #P64.

## 2. Two elementary reductions

### Lemma 2.1 (a unique portal gives an exact boundary)

Suppose that `D` is two-connected.  If some `t in T` has a unique
neighbour `z` in `D`, then

\[
                         N_G(D-z)=\{z\}\cup(T-\{t\}),   \tag{2.1}
\]

an actual order-seven separation boundary.

#### Proof

The graph `D-z` is connected and nonempty.  Its neighbourhood is contained
in the seven-set on the right of (2.1), while (1.1) supplies a nonempty
opposite side.  Seven-connectivity forces equality. \(\square\)

### Lemma 2.2 (a common repair vertex)

Suppose that `D` is three-connected and no boundary vertex has a unique
portal in `D`.  If

\[
       z\in N_D(b)\cap\bigcup_{i\in I}N_D(i),           \tag{2.2}
\]

then `{z}` is a repair support and `D-z` is a residual boundary-full
subgraph.

#### Proof

The one-vertex graph on `z` is adjacent to `b` and to a member of `I`.
Three-connectivity makes `D-z` connected.  For every `t in T`, the
assumption that `z` is not its unique portal gives a neighbour of `t` in
`D-z`. \(\square\)

## 3. The adjacent-pair theorem

### Theorem 3.1

Suppose that `D` is three-connected and that an edge `pq of D` has the
property

\[
                         \{p,q\}\cap P_t\ne\varnothing
                         \quad(t\in T).                 \tag{3.1}
\]

Then at least one of the following holds.

1. `G` has an actual order-seven separation boundary contained in
   `V(D) union T`.
2. `D` contains a repair support disjoint from a residual boundary-full
   subgraph.

#### Proof

If a boundary vertex has a unique portal, apply Lemma 2.1.  If a vertex
of `D` is adjacent to both `b` and a member of `I`, apply Lemma 2.2.  We
may therefore assume that neither event occurs.

Put `W={p,q}` and

\[
 X=N_D(b)-W,
 \qquad
 Y=\left(\bigcup_{i\in I}N_D(i)\right)-W.             \tag{3.2}
\]

Both sets are nonempty.  Indeed, if `X` were empty and `b` had only one
neighbour in `W`, that neighbour would be the unique portal of `b`.
Otherwise `b` is adjacent to both `p` and `q`; since (3.1) supplies a
neighbour in `W` for every member of `I`, one of `p,q` would then satisfy
(2.2).  For `Y`, choose any `i in I`.  If `i` has only one neighbour in
`W` and no neighbour outside `W`, that neighbour is its unique portal.  If
it has both neighbours in `W`, one of them is also adjacent to `b` and
satisfies (2.2).

The sets `X,Y` are disjoint by the exclusion of (2.2).  Since `D` is
three-connected, `D-W` is connected.  Choose `x in X`, `y in Y`, and an
`x-y` path `P` in `D-W`.  Its vertex set is a repair support.  The edge
`pq` is disjoint from `P`, connected, and adjacent to every member of `T`
by (3.1).  It is the required residual boundary-full subgraph. \(\square\)

The proof uses no virtual edge and no contraction.  Thus every adjacent
two-vertex transversal is completely eliminated by either an exact
order-seven boundary or two literal disjoint connected subgraphs.

### Theorem 3.2 (connected remainder after a contractible transversal)

Keep the hypotheses of Theorem 3.1, and let `w` be the vertex obtained by
contracting the edge `pq`.  If the resulting simple graph `D/pq` is
three-connected, then either outcome 1 of Theorem 3.1 holds, or there is a
repair path `P` for which

\[
                         D-V(P)\text{ is connected and boundary-full}. \tag{3.3}
\]

#### Proof

As in Theorem 3.1, a unique portal gives the exact order-seven outcome,
while a common repair vertex `z` gives the one-vertex path `P=z`; in the
latter case `D-z` is connected and boundary-full by Lemma 2.2.

In the remaining case, the sets `X,Y` in (3.2) are nonempty and disjoint.
Choose `x in X` and `y in Y`.  Apply Tutte's nonseparating-path theorem
in `D/pq` to the three distinct vertices `x,y,w`.  It gives an `x-y` path
`P` avoiding `w` such that `(D/pq)-V(P)` is connected.  The path lies
literally in `D-\{p,q\}` and is a repair support.  Replacing the contracted
vertex `w` by the connected edge `pq` shows that `D-V(P)` is connected.
It contains `p,q`, so (3.1) makes it boundary-full. \(\square\)

### Lemma 3.3 (the exact obstruction to contraction)

Suppose `|V(D)|>=5`.  The graph `D/pq` is not three-connected if and only
if there is a vertex `z in V(D)-\{p,q\}` such that

\[
                            \{p,q,z\}\text{ is a vertex cut of }D.    \tag{3.4}
\]

For every component `A` of `D-\{p,q,z\}`,

\[
                    N_G(A)=\{p,q,z\}\mathbin{\dot\cup}N_T(A),
                    \qquad |N_T(A)|\ge4.               \tag{3.5}
\]

In particular, `|N_T(A)|=4` gives an actual order-seven separation.

#### Proof

Put `H=D/pq`.  The graph `H` is two-connected.  Deleting its contracted
vertex leaves `D-\{p,q\}`, which is connected; deleting any other vertex
gives a contraction of the connected graph obtained by deleting that
vertex from `D`.

If `H` is not three-connected, it has a two-vertex cut.  Such a cut must
contain the contracted vertex `w`: otherwise its deletion in `H` would be
a contraction of the connected graph obtained by deleting the same two
vertices from `D`.  Write the cut as `{w,z}`.  Then
`H-\{w,z\}=D-\{p,q,z\}` is disconnected, proving the forward implication.
The reverse implication is immediate from the same equality.

Let `A` be a component displayed in (3.4).  Its neighbourhood inside `D`
is contained in `{p,q,z}` and must have order at least three by
three-connectivity; hence it is exactly that set.  All remaining neighbours
belong to `T`, proving the equality in (3.5).  This is a genuine separation
because (1.1) supplies an opposite side.  Seven-connectivity gives the
stated lower bound, and equality gives order seven. \(\square\)

## 4. All transversals of order at most two

### Theorem 4.1 (repair or alternating web)

Suppose that `D` is three-connected and the family `(P_t:t in T)` has a
boundary-contact transversal of order at most two.  Then at least one of
the following holds.

1. `G` has an actual order-seven separation boundary contained in
   `V(D) union T`.
2. `D` contains a repair support disjoint from a residual boundary-full
   subgraph.
3. There is a two-vertex transversal `W={p,q}` with `pq notin E(D)` such
   that, after possibly interchanging `p,q`,

   \[
          N_D(b)\cap W=\{p\},
          \qquad
          N_D(i)\cap W=\{q\}\quad(i\in I),             \tag{4.1}
   \]

   and, on putting

   \[
     X=N_D(b)-W,
     \qquad
     Y=\left(\bigcup_{i\in I}N_D(i)\right)-W,          \tag{4.2}
   \]

   the sets `X,Y` are nonempty and disjoint, and for every
   `x in X`, `y in Y`, the graph `D` is a spanning subgraph of an
   `(x,p,y,q)`-web.

#### Proof

If a one-vertex transversal exists, the audited universal-contact theorem
`hc7_boundary_full_universal_vertex_split.md` gives outcome 1 or 2.
Suppose that `W={p,q}` is a two-vertex transversal.

As before, a unique portal gives outcome 1 by Lemma 2.1 and a common
repair vertex gives outcome 2 by Lemma 2.2.  In their absence, the proof
of Theorem 3.1 shows that the sets `X,Y` in (4.2) are nonempty and
disjoint.  Moreover, `b` cannot be adjacent to both `p,q`: every member
of `I` has a neighbour in `W`, which would then be a common repair vertex.
After interchanging `p,q`, assume `N_D(b) cap W={p}`.  No member of `I`
can be adjacent to `p`, again by the common-vertex reduction, so the
transversal property forces (4.1).  If `pq` is an edge, Theorem 3.1 gives
outcome 1 or 2.  We may therefore assume that `p,q` are nonadjacent.

Fix `x in X` and `y in Y`.  The four vertices `x,p,y,q` are distinct.  If
`D` has disjoint paths `P,Q`, where `P` joins `x` to `y` and `Q` joins
`p` to `q`, then `P` is a repair support.  The path `Q` is connected and,
because it contains the transversal `W`, is adjacent to every member of
`T`.  Thus `Q` is a disjoint residual boundary-full subgraph, giving
outcome 2.

If outcome 2 is absent, this linkage fails for every `x in X`, `y in Y`.
Lemma 2 of Fabila-Monroy and Wood applied with

\[
        (s_1,t_1,s_2,t_2)=(x,y,p,q)
\]

says exactly that `D` is a spanning subgraph of an `(x,p,y,q)`-web.
This is outcome 3. \(\square\)

### Corollary 4.2 (literal size of every web attachment)

Assume outcome 3 of Theorem 4.1 and fix one of its web completions.  Let
`K` be a facial triangle of the planar web skeleton and let `A` be a
nonempty component of `D-K` contained in the clique part inserted behind
`K`.  Then

\[
                         N_G(A)=K\mathbin{\dot\cup}N_T(A),
                         \qquad |N_T(A)|\ge4.           \tag{4.3}
\]

If `|N_T(A)|=4`, this is an actual order-seven separation boundary.
Consequently, in a survivor with no such boundary, every nonempty literal
web-attachment component is adjacent to at least five vertices of `T`.
If, in addition, Theorem 4.1 outcome 2 is absent, then every such component
satisfies exactly one of

\[
             N_T(A)=T-I,
             \qquad\hbox{or}\qquad
             b\notin N_T(A)\text{ and }|N_T(A)|\ge5.   \tag{4.4}
\]

#### Proof

By the definition of a web completion, vertices in the clique part behind
`K` have no neighbours outside that clique part and `K`.  Since `A` is a
component after deleting `K`, it follows that `N_D(A) subseteq K`.
The four outer web vertices cannot all belong to the three-set `K`, so
`D-K` has a vertex outside `A`.  Three-connectivity of `D` now forces
`N_D(A)=K`.

The graph `D` is a component of `G-T`, hence every remaining neighbour of
`A` belongs to `T`, proving the equality in (4.3).  The opposite side in
(1.1) makes this a genuine separation.  Seven-connectivity gives
`3+|N_T(A)|>=7`.  Equality is exactly the asserted order-seven case.

It remains to prove (4.4).  The graph `D-A` is connected.  Indeed, every
other component of `D-K` has all three vertices of `K` as neighbours by
three-connectivity, and the component containing an outer web vertex is
present and connects the three vertices of `K` inside `D-A`.  Moreover,
`D-A` contains `p,q`, since the transversal vertices are outer web
vertices rather than vertices of an inserted clique part.  It therefore
contains a `p-q` path, which is a boundary-full connected subgraph.

If `A` were adjacent to `b` and to a member of `I`, then `A` itself would
be a disjoint repair support, giving Theorem 4.1 outcome 2.  In its
absence, `A` misses `b` or misses both members of `I`.  In the latter case
the lower bound `|N_T(A)|>=5` forces `N_T(A)=T-I`; in the former case it
gives the second alternative in (4.4).
\(\square\)

### Corollary 4.3 (five-contact component or a bare planar web)

Assume that outcomes 1 and 2 of Theorem 4.1 are absent.  Fix
`x in X`, `y in Y` and a corresponding web completion from outcome 3.
Then either

1. `D` contains a connected web-attachment component with at least five
   boundary contacts and one of the two traces in (4.4); or
2. every inserted clique part of that completion is empty, so `D` is a
   spanning subgraph of the planar web skeleton and `x,p,y,q` lie on one
   face in that cyclic order.

#### Proof

If an inserted clique part is nonempty, take any component left inside it
after deleting its supporting facial triangle and apply Corollary 4.2.
If every part is empty, the web completion is just its planar skeleton;
the asserted embedding and outer order are part of the definition of the
web. \(\square\)

## 5. Exact residual obstruction

Theorem 4.1 reduces every two-vertex boundary-contact transversal to one
standard infinite family.  A survivor has all of the following literal
properties:

- the transversal vertices are nonadjacent;
- no boundary vertex has a unique portal;
- no vertex of `D` is simultaneously a portal for `b` and for `I`;
- both repair sides have portals outside the transversal; and
- for every choice of one such portal on each side, there is a
  corresponding Two-Paths web in which that choice alternates with the
  transversal pair.  The theorem does not assert that all choices use one
  common web completion.

This is a structural obstruction, not a terminal conclusion.  The web may
contain clique pieces behind facial triangles, and completion edges of the
web are not edges of `G`.  Corollary 4.2 says that every surviving literal
clique piece has at least five boundary contacts.  Further progress must
use the proper-minor
colouring response or the already named branch sets to break the web, or
must turn a facial three-separator and its literal boundary contacts into
an order-seven separation with compatible shore colourings.

Theorem 3.1 and Theorem 4.1 only assert the existence of a connected
boundary-full subgraph disjoint from the repair support; they do not in
general assert that the whole graph left after deleting the repair path is
connected.  Theorem 3.2 identifies a substantial exact case where that
stronger conclusion holds, and Lemma 3.3 identifies its three-cut
obstruction.
