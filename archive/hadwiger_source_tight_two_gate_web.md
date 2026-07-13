# The source-tight two-gate web: audit, cut amplification, and an exact-portal closure

## 1. Setup and status

Use the co-rank-one notation of
`hadwiger_corank_one_portal_basis_descent.md`.  Thus (G) is
((r+1))-connected and proper-minor-minimal non-(r)-colourable,
(v\in V(G)), and

\[
             (B,B_1,\ldots,B_{r-1})
\]

is a labelled (K_r)-model in (G-v).  The bag (B) contains the
unique old-model neighbour (a) of (v), the other bags contain no
neighbour of (v), and the promoted co-rank-one Hall circuit has

\[
 |I|=r-1,\qquad |X|=r-2,\qquad
 R=N(v)-Q=X\mathbin{\dot\cup}Y,\qquad |Y|=2.
\tag{1.1}
\]

We assume the source-tight outcome of Theorem 4.4 in
`hadwiger_B_gated_capacity_state.md`: (Y) separates (X) from the
portal set (P\subseteq B) in the root shore.  Corollary 4.6 gives

\[
       N_U(X)\subseteq Y,
\tag{1.2}
\]

and every component of (U-Y) has a neighbour in (P).

The main result below closes a uniform infinite subfamily of this cell.
It is not special to the Moser spindle or to (r=6).

> **Exact-portal two-component closure.**  Suppose
> 
> \[
> |P|=r-1
> \]
> 
> and (U-Y) has at least two components.  If one vertex of (Y) is
> adjacent to every vertex of (X), then (G) has a (K_{r+1})-minor.

For (HC_7), this says that five portals, two web components, and one
complete gate already give a (K_7).  No assumption is made on the
order, block structure, or portal order of (B).

## 2. Audit of Theorem 4.4 and Corollary 4.6

The proof of Theorem 4.4 is valid, with the following dependencies made
explicit.

Let (M_U) be the root-shore strict gammoid on (X\cup P).  The set
(X\cup\{p,q\}) is independent.  If the third-portal exchange fails,
then for every (z\in P-\{p,q\}), the unique circuit in
(X\cup\{p,q,z\}) contains no member of (X).  The ordinary matroid
circuit-exchange axiom therefore gives

\[
                     z\in\operatorname{cl}_{M_U}\{p,q\}.
\]

(When (P=\{p,q\}), the same conclusion is vacuous but immediate.)
Consequently (r_{M_U}(P)\le2).  Vertex Menger in the vertex-split
strict-gammoid presentation gives a set of at most two vertices
separating (R) from (P) in the root shore.  Sources and portal
targets are disjoint because (R\subseteq V(G)-Q) and (P\subseteq B).

If that separator consumes (R-X), the inequalities

\[
 |R-X|\ge |R|-|X|\ge r-(r-2)=2
\]

force equality and give the source-tight outcome.  Otherwise a surviving
source component has neighbourhood contained in
(X\cup Y\cup\{v\}), and ((r+1))-connectivity forces the exact
adhesion asserted in outcome 2.  Thus the trichotomy is exhaustive.

Corollary 4.6 is also valid.  A point which can look paradoxical is that
(X\subseteq R), while (X) is not contained in (U): by definition,
(U) is a union of components of ((L-Q)-X).  Hence (U-Y) contains no
neighbour of (v).  If a component (C) of (U-Y) missed (P), then

\[
                     N_G(C)\subseteq X\cup Y
\]

would be a cut of order (r).  If it met both (X) and (P), it would
give an (X)-to-(P) path avoiding (Y).  These are exactly the two
claims used in Corollary 4.6.

No exact star-trace colouring may be identified with an internal-minor
transition colouring.  The former colours (G-v) and saturates (N(v))
with all (r) colours; the latter colours a proper minor containing (v)
and must omit the colour of (v) on (N(v)).  The crossed arguments in
Section 6 below keep these witnesses separate.

## 3. Connectivity amplifies every web component

### Lemma 3.1 (portal amplification)

For every component (C) of (U-Y),

\[
 N_G(C)\subseteq Y\cup P
 \quad\hbox{and}\quad
 |N_G(C)\cap P|\ge r-1.
\tag{3.1}
\]

In particular, (|P|\ge r-1).  If (|P|=r-1), then

\[
                         N_G(C)=Y\cup P
\tag{3.2}
\]

for every component (C) of (U-Y).

#### Proof

The promotion theorem says that a vertex of (U) can leave (U), in
(G-v), only through (X\cup P).  Distinct components of (U-Y) can
meet one another only through (Y).  Corollary 4.6 excludes neighbours
in (X), and (U-Y) contains no neighbour of (v).  This proves the
first containment in (3.1).

The deficient bags (B_i) survive outside (C\cup N(C)), so (N(C))
is a genuine vertex cut.  The ((r+1))-connectivity of (G) gives

\[
 r+1\le |N(C)|\le |Y|+|N(C)\cap P|
                  =2+|N(C)\cap P|.
\]

This proves (3.1).  If (|P|=r-1), equality holds throughout, proving
(3.2).  \(\square\)

For (HC_7), every component beyond the two gates has at least five
distinct neighbours in the accessible bag.  Thus the source-tight lock
is not a width-two portal lock; only its *routing rank* is two.

## 4. The neighbourhood support dichotomy

Minimal-counterexample criticality and Dirac's neighbourhood inequality
give

\[
                         \alpha(G[N(v)])\le2.
\tag{4.1}
\]

The independent-star contraction witness additionally says that every
nonedge of (G[N(v)]) can be selected as the repeated pair in an exact
(r)-colour trace on (G-v).  The following consequences use only the
underlying independence bound, so they are valid simultaneously for all
those exact traces.

### Lemma 4.1 (foot/gate support)

Let (Y=\{y_1,y_2\}).

1. If (a\in P), then (a) is anticomplete to (X), (X) is a
   clique, and every (y_i) nonadjacent to (a) is complete to (X).
2. If (a\notin P), then (a) is anticomplete to (Y), and hence
   (y_1y_2\in E(G)).

#### Proof

If (a\in P), an edge (ax), (x\in X), would itself be an
(X)-to-(P) path in the root shore avoiding (Y).  Thus no such edge
exists.  Two nonadjacent vertices of (X), together with (a), would
contradict (4.1), so (X) is a clique.  If (ay_i,y_ix\notin E(G)),
then \(\{a,y_i,x\}\) is independent; hence (ay_i\notin E(G)) forces
(y_i) to be complete to (X).

If (a\notin P), then no vertex of (U), in particular no (y_i), is
adjacent to (a\in B).  Now \(\{a,y_1,y_2\}\) and (4.1) force
(y_1y_2\in E(G)).  \(\square\)

### Lemma 4.2 (two complete gates close immediately)

If both (y_1,y_2) are complete to (X), then (G) contains a
(K_{r+1})-minor.

#### Proof

The clean portal-basis theorem gives disjoint paths from (y_1,y_2)
to distinct portals (p,q\in P), first meeting (B) at their respective
endpoints.  The two portal paths really are rooted at (Y): the endpoint
set contains every vertex of (X), so vertex-disjointness prevents a
portal path from starting at a root in (X).

Partition the connected graph (B) into two nonempty connected sets
(A_1,A_2), with (p\in A_1,q\in A_2), and with an edge between the
sets.  Such a partition is obtained by deleting an edge of the (p)-to-
(q) path in a spanning tree of (B).  Absorb the portal paths into
(A_1,A_2), producing rooted pieces (Z_1,Z_2).

Fix any far Hall certificate, omitting one deficient label.  Its
(r-2) suffixes, joined to their deficient clique bags, are pairwise
adjacent disjoint carriers (F_x), (x\in X), and (x\in F_x).
Both (Z_i) are adjacent to every (F_x) through the edge (y_ix),
and (Z_1\sim Z_2).  These (r) rooted bags, together with \(\{v\}\),
form a (K_{r+1})-model.  \(\square\)

In particular, when (a\in P), the case in which both gates miss the
foot is already impossible, without assuming (|P|=r-1) or multiple web
components.

### Lemma 4.3 (exact-trace carriers when the foot is not a portal)

Assume $a\notin P$.  Then, for each $y\in Y$,

\[
                         M(y)\subseteq N_X(a).
\tag{4.2}
\]

Moreover, write $Y=\{y,y'\}$.  For every $x\in M(y)$, the exact
star trace with repeated pair $\{a,y'\}$ supplies a $y$-to-$x$
Kempe path whose interior avoids $N[v]$, and every such path meets
$P$ before reaching $x$.

#### Proof

Lemma 4.1 gives $ay\notin E(G)$.  If also $ax,yx\notin E(G)$, then
$\{a,y,x\}$ is independent, contradicting (4.1).  This proves (4.2).

The pair $\{a,y'\}$ is independent.  Its star-contraction colouring
has that exact repeated pair and makes the other $r-1$ neighbours of
$v$, including $y$ and every member of $X$, uniquely coloured.  The
standard equality-cell external-path lemma therefore gives, for the
missing edge $yx$, a bichromatic $y$-to-$x$ path with interior outside
$N[v]$.

The path starts in $U$.  It cannot leave $U$ first through an internal
vertex of $X$, since $X\subseteq N(v)$, and it cannot reach its final
vertex $x$ directly from an internal vertex of $U$, because
$N_U(X)\subseteq Y$ and the other gate is also forbidden from the
interior.  Promotion says that every remaining exit from $U$ lies in
$P\subseteq B$.  Hence the path has a first portal before it reaches
$x$.  \(\square\)

This is genuine alignment between an exact trace and the source-tight
geometry: every missing gate/root adjacency has a named first portal.
It is not yet alignment with a selected far Hall carrier; the path may
first hit the wrong carrier after leaving that portal.

## 5. Exact-portal two-component closure

We need a small connected-graph lemma.  For (p\in P), define its
private region in (B) by

\[
 K_p=\{p\}\cup\bigcup\{D:D\text{ is a component of }B-p
                    \text{ with }D\cap(P-p)=\varnothing\}.
\tag{5.1}
\]

Then (K_p) is connected.  Every component of (B-K_p) contains a
vertex of (P-p).

### Lemma 5.1 (private regions are disjoint)

The sets (K_p), (p\in P), are pairwise disjoint.

#### Proof

Certainly (p\notin K_q) for (p\ne q), since the component of (B-q)
containing (p) contains the portal (p\in P-q).  If a third vertex
(z) belonged to (K_p\cap K_q), then (p) would separate (z) from
(q), while (q) would separate (z) from (p).  A simple (z)-to-
(p) path must meet (q); its (z)-to-(q) prefix then avoids (p),
a contradiction.  \(\square\)

For (j\in I), put

\[
 A_j=N_B(B_j)=\{b\in B:b\text{ has a neighbour in }B_j\}.
\]

Each (A_j) is nonempty.  Say that (p) *owns* (j) if
(A_j\subseteq K_p), and write (O(p)) for the set of labels owned by
(p).  Lemma 5.1 implies that a label is owned by at most one portal.
Therefore

\[
                    \sum_{p\in P}|O(p)|\le r-1.
\tag{5.2}
\]

Put

\[
 L(p)=\{j\in I:A_j\cap K_p\ne\varnothing\},
 \qquad
 M(y)=\{x\in X:xy\notin E(G)\}.
\tag{5.3}
\]

For a far Hall certificate omitting (b\in I), let

\[
                    \lambda_b:X\longrightarrow I-\{b\}
\tag{5.4}
\]

be the bijection defined by its four (in general (r-2)) disjoint
suffixes: the suffix beginning at (x) ends in (B_{\lambda_b(x)}).

### Theorem 5.2 (one-unit support packing)

Assume (|P|=r-1) and (U-Y) has at least two components.  Fix
(p\in P), (y\in Y), and (b\in I) such that

\[
                         O(p)\subseteq\{b\}.
\tag{5.5}
\]

If, for some far certificate omitting (b),

\[
 \bigl|\{x\in M(y):\lambda_b(x)\notin L(p)\}\bigr|\le1,
\tag{5.6}
\]

and (b\in L(p)) whenever equality holds in (5.6), then (G) has a
(K_{r+1})-minor.

#### Proof

Let (y') be the other member of (Y), and take distinct components
(C,D) of (U-Y).  Form the two root pieces

\[
 Z=\{y\}\cup C\cup K_p,
 \qquad
 Z'=\{y'\}\cup D\cup(B-K_p).
\tag{5.7}
\]

Lemma 3.1 makes these disjoint connected adjacent rooted sets.

For each (x\in X), let (F_x) be the far carrier containing
(B_{\lambda_b(x)}).  Condition (5.5) says that every retained label has
an attachment in (B-K_p), so (Z') is adjacent to every (F_x).
The set (Z) is adjacent to (F_x) either through (yx), or through an
attachment in (K_p) whenever \(\lambda_b(x)\in L(p)\).

If (5.6) has value zero, the displayed sets already form the required
(r) rooted branch sets.  Otherwise let (x_0) be its unique member.
Enlarge

\[
                         F_{x_0}\longmapsto F_{x_0}\cup B_b.
\tag{5.8}
\]

This set is connected and remains adjacent to all other far carriers,
because the old bags are clique bags.  Since (b\in L(p)), it is now
adjacent to (Z); it remains adjacent to (Z') through its retained bag
(B_{\lambda_b(x_0)}), which is not owned by (p).  Thus
(Z,Z',(F_x:x\in X)), with the possible enlargement (5.8), are (r)
pairwise adjacent rooted branch sets.  Adding \(\{v\}\) proves the
claim.  \(\square\)

The theorem makes precise the capacity of the one unused Hall label: it
repairs exactly one unsupported (X)-root, and no more.

### Corollary 5.3 (automatic support closures)

Under the hypotheses of Theorem 5.2, each of the following is sufficient
for a (K_{r+1})-minor.

1. Some gate (y) is complete to (X), and (|O(p)|\le1) for some
   (p\in P).
2. Some gate satisfies (|M(y)|\le1), and for some (p\in P),
   (|O(p)|\le1) and (L(p)\ne\varnothing).
3. For some (p\in P),
   
   \[
                         |O(p)|\le1,
                         \qquad |L(p)|\ge r-2.
   \tag{5.9}
   \]

#### Proof

For item 1, choose (p) with (|O(p)|\le1), and omit its unique owned
label if it has one; (5.6) is empty.

For item 2, do the same when (O(p)\ne\varnothing).  When (O(p)) is
empty, omit any (b\in L(p)).  There is at most one unsupported root,
and the omitted bag repairs it.

For item 3, first suppose (O(p)=\{b\}) and omit (b).  Among the
(r-2) retained labels at most one lies outside (L(p)), so (5.6) has
order at most one, and (b\in L(p)).  If (O(p)=\varnothing) and
(L(p)\ne I), then (5.9) forces (I-L(p)=\{b\}); omit that label, so
every retained label lies in (L(p)).  If (L(p)=I), omit any label.
In both latter cases (5.6) is empty.  Apply Theorem 5.2.  \(\square\)

### Theorem 5.4 (exact-portal two-component closure)

Assume (|P|=r-1), (U-Y) has at least two components, and, after
renaming, (y_1) is complete to (X).  Then (G) contains a
(K_{r+1})-minor.

#### Proof

By (5.2), choose (p\in P) with (|O(p)|\le1).  Take distinct
components (C,D) of (U-Y).  Lemma 3.1 says that both have exact
neighbourhood (Y\cup P).

Put

\[
 Z_1=\{y_1\}\cup C\cup K_p,
 \qquad
 Z_2=\{y_2\}\cup D\cup(B-K_p).
\tag{5.10}
\]

The first set is connected because (C) meets (y_1) and (p), while
(K_p) is connected.  Every component of (B-K_p) contains a portal,
and (D) meets (y_2) and every portal, so the second set is connected.
The sets are disjoint.  They are adjacent, for example through an edge
from (y_1) to (D).

If (O(p)=\{b\}), take the far Hall certificate omitting (b); if
(O(p)=\varnothing), omit any label (b).  It gives (r-2) pairwise
adjacent disjoint far carriers (F_x), (x\in X), using precisely the
bags (B_j), (j\ne b).  No retained label is owned by (p), so for
every such (j), the nonempty set (A_j) meets (B-K_p).  Hence
(Z_2) is adjacent to every far carrier.  The set (Z_1) is adjacent to
every (F_x) through (y_1x).

Thus

\[
                     Z_1,Z_2,(F_x:x\in X)
\]

are (r) disjoint pairwise adjacent connected sets, rooted at the
distinct neighbours (y_1,y_2,X) of (v).  Adding \(\{v\}\) gives the
claimed (K_{r+1})-model.  \(\square\)

### Corollary 5.5 (HC7 residual in this exact cell)

In the (HC_7) source-tight cell, suppose (|P|=5) and (U-Y) has at
least two components.  If (a\in P), then a target-minor-free residue
must satisfy

\[
                         ay_1,ay_2\in E(G).
\tag{5.11}
\]

Indeed, if one gate misses (a), Lemma 4.1 makes it complete to (X)
and Corollary 5.3(1) applies.  If both miss (a), Lemma 4.2 already
applies.

This eliminates an infinite family: the accessible bag and both web
components may have arbitrary order and arbitrary internal block
structure.

The stronger omitted-bag absorption theorem in
`hadwiger_exact_gate_omitted_bag_absorption.md` supersedes the numerical
support bounds above: if a low-owner private region sees even one
deficient label, absorb the omitted whole bag into its gate piece.  Hence,
in a target-minor-free exact cell, at least

\[
                         \left\lceil\frac{r-1}{2}\right\rceil
\tag{5.12}
\]

private portal regions are completely label-free (at least three for
(HC_7)).  Lemma 3.1 of that note gives the correct geometric normal
form: each such region is a singleton portal, or every nontrivial private
lobe exposes a named far-side shadow.  The shadow alternative cannot be
deleted without a spanning/no-shadow hypothesis.

### Lemma 5.6 (a dead lobe has a model-clean first hit)

Let (p) be one of the label-free portals supplied above, and let (E)
be a component of (K_p-p).  Then there is a path (T) with one end in
(E), the other end in

\[
             \bigl(B-(E\cup\{p\})\bigr)
             \ \cup\ \bigcup_{j\in I}B_j,
\tag{5.13}
\]

and all internal vertices in

\[
             F=V(G-v)-\bigl(Q\cup U\cup X\bigr).
\tag{5.14}
\]

Thus (T) is either a clean (B)-ear out of the private lobe, or a
clean transit from that lobe to a deficient bag.

#### Proof

Let \(\mathcal D\) be the set of components of (G[F]) having an edge
to (E), and put

\[
                         S=E\cup\bigcup_{D\in\mathcal D}D.
\]

Lemma 3.1 of `hadwiger_exact_gate_omitted_bag_absorption.md` shows that
\(\mathcal D\ne\varnothing\).  The set (F) is the union of the
components of ((G-v-Q)-X) which are not in (U).  Consequently no
member of \(\mathcal D\) has a neighbour in (U) or in a different
component of (F).

The lobe (E) meets (B-E) only at (p), has no (U)-neighbour, and,
because (L(p)=\varnothing), has no deficient-bag neighbour.  All its
neighbouring (F)-components have been included in (S).  If no member
of \(\mathcal D\) met the set in (5.13), it would follow that

\[
                         N_G(S)\subseteq X\cup\{p,v\}.
\]

This is a cut of order at most (r), while every deficient bag survives
outside it, contradicting ((r+1))-connectivity.  Hence some
(D\in\mathcal D) meets (5.13).  A shortest path through the connected
set (E\cup D) to its first vertex of (Q-(E\cup\{p\})) has precisely
the asserted form.  \(\square\)

### Corollary 5.7 (the deficient-hit case is a literal model exchange)

Suppose the path (T) in Lemma 5.6 ends in (B_j), and (E) does not
contain the unique foot (a).  Then replacing

\[
 B\longmapsto B-E,
 \qquad
 B_j\longmapsto B_j\cup V(T)\cup E
\tag{5.15}
\]

gives another labelled (K_r)-model with exactly the same contacted
labels and a strictly smaller accessible bag.

#### Proof

Because (E) is a component of (B-p), the graph (B-E) is connected.
The enlarged (B_j) is connected by (T).  It remains adjacent to all
other deficient bags through the old bag (B_j).  The equality
(L(p)=\varnothing) says that no vertex of (K_p), hence no vertex of
(E), was responsible for an edge from (B) to any (B_i).  Therefore
(B-E) retains its adjacency to every deficient bag, including the
enlarged (B_j).  All bags remain disjoint.  Finally, (E\cap N(v)) is
empty by hypothesis, and the internal vertices of (T) lie in (F),
which contains no neighbour of (v).  Thus the contact pattern is
unchanged and the accessible bag loses the nonempty set (E).  \(\square\)

### Theorem 5.8 (ear absorption gives a smaller circuit or a smaller web)

Suppose the path (T) in Lemma 5.6 ends in
(B-(E\cup\{p\})).  Enlarge (B) by the internal vertices of (T),
leaving all other old bags unchanged.  Then this is a labelled
contact-preserving (K_r)-model, and at least one of the following holds.

1. The new model-avoiding gammoid has a nonlinkable proper subset
   (J\subsetneq I), hence a Hall circuit of strictly smaller order.
2. The old set (I) remains a co-rank-one Hall circuit, while the clean
   ear destroys the private lobe (E) or merges it with another private
   lobe.  In particular, the number of components of (K_p-p) strictly
   decreases if the same source-tight cell persists.
3. The new private region at (p) sees a deficient label, in which case
   the omitted-bag absorption theorem gives a (K_{r+1})-minor.

#### Proof

Adding the internal vertices of (T) to (B) preserves connectedness,
disjointness, every old interbag adjacency, and the unique contact (a):
the internal vertices lie in (F), which has no neighbour of (v).

In the auxiliary model-avoiding digraph, the operation only removes the
newly absorbed vertices from the routing ground graph.  It cannot create
a linkage to the deficient label set (I).  Hence (I) is still
nonlinkable.  If a proper subset is now nonlinkable, an inclusion-minimal
one is the circuit in outcome 1.  Otherwise every proper subset remains
linkable, so (I) itself remains an inclusion-minimal deficit of the
same order.

The ear avoids (p) and joins (E) to a vertex of (B) outside
(E\cup\{p\}).  In (B-p), it therefore joins (E) either to a
component containing another portal, in which case (E) is no longer
private, or to another portal-free component, in which case those two
private components merge.  This proves the strict geometric decrease.

Finally, ownership cannot increase under this move: all old attachment
vertices outside the private region remain outside it.  If an absorbed
vertex creates a new deficient-label contact in the resulting low-owner
private region, Theorem 2.1 of
`hadwiger_exact_gate_omitted_bag_absorption.md` applies.  Otherwise the
region stays label-free and outcome 2 is the asserted same-circuit
descent.  \(\square\)

Together, Corollary 5.7 and Theorem 5.8 give a literal descent for every
root-free dead lobe.  A clean ear decreases the lexicographic pair

\[
  (\,|I|,\ \#\text{ private components at the low-owner portals}\,),
\]

unless it creates the target minor.  A deficient hit is instead an
explicit contact-preserving model exchange which strictly decreases the
accessible bag; it is excluded if that bag was chosen minimum within the
contact class.  The only dead lobe not covered by the size-decreasing
transfer is the unique one which may contain the foot (a).

### Corollary 5.9 (terminal exact-cell normal form)

Assume that target-minor, contact-augmentation, and smaller-Hall-circuit
outcomes have been excluded.  Among the surviving exact source-tight
models, first minimize the total number of private components at the
low-owner label-free portals, and then minimize the order of the
accessible bag (B).  Then at least

\[
                  \left\lceil\frac{r-1}{2}\right\rceil-1
\tag{5.16}
\]

of the label-free private regions are singleton portals.  In particular,
the terminal (HC_7) exact cell has at least two label-free singleton
private portals; a third dead region exists and is either another
singleton or the unique region protected by the foot (a).

#### Proof

Omitted-bag absorption gives at least
\(\lceil(r-1)/2\rceil\) pairwise disjoint label-free private regions.
At most one contains (a).  If a root-free one had a nontrivial component
(E), Lemma 5.6 would give a deficient hit or a clean ear.  The deficient
transfer (5.15) deletes (E) from (B), does not create a new private
component at any other portal, and either leaves the exact cell with a
strictly smaller accessible bag or exits through one of the outcomes
excluded in the hypothesis.  A clean ear is handled by Theorem 5.8 and
strictly decreases the circuit order or the private-component count,
unless it gives the target.  Both contradict the chosen optimization.
Thus every root-free dead private region is a singleton, proving (5.16).
\(\square\)

Corollary 5.9 uses a minimum-(B) transfer normalization and is retained
only as a fixed-model diagnostic.  The opposite maximum-(|B|) choice in
`hadwiger_exact_gate_omitted_bag_absorption.md` gives a strict
same-coordinate enlargement or exits to more contact / a smaller Hall
circuit.  It does **not** close all exits: a globally contact-maximal model
cannot carry the nontrivial Hall circuit assumed in this source-tight
cell.  The two normal forms must not be combined as simultaneous
assumptions.

## 6. Crossed operation states on the exact gate

The exact five-portal cell also has a genuinely finite dynamic interface.
The following statement uses minor-criticality and cannot be obtained from
the static portal geometry.

### Theorem 6.1 (different web components have disjoint exact-gate states)

Assume (|P|=r-1), and put

\[
                         W=Y\cup P,
 \qquad |W|=r+1.
\tag{6.1}
\]

Let (C,D) be distinct components of (U-Y).  Perform any proper
boundary-faithful minor operation supported in (C), and any such
operation supported in (D).  No (r)-colourings of the two operated
minors induce the same equality partition on (W).

#### Proof

Lemma 3.1 gives (N(C)=N(D)=W).  Use the separation

\[
       (C\cup W,\;G-C),
\]

whose adhesion is (W).  The operation in (C) is faithful to the
opposite closed shore.  The operation in (D\subseteq G-(C\cup W)) is
faithful to (C\cup W).  Equal boundary partitions would therefore
cross-splice by the boundary-faithful crossed-minor theorem and give an
(r)-colouring of (G), a contradiction.  \(\square\)

### Corollary 6.2 (finite state bound)

In the exact-portal source-tight cell,

\[
       \#\{\text{components of }U-Y\}
       \le \sum_{j=1}^{r}S(r+1,j)=\operatorname{Bell}(r+1)-1.
\tag{6.2}
\]

In particular, for (HC_7) there are at most

\[
                         \operatorname{Bell}(7)-1=876
\]

web components.

#### Proof

For each component (C), delete one vertex of (C).  Proper-minor
minimality supplies an (r)-colouring; record its equality partition on
(W).  Theorem 6.1 makes these chosen partitions distinct for distinct
components.  A partition induced by (r) colours has at most (r)
blocks.  The only partition of an ((r+1))-set omitted from the Bell
number is the all-singleton partition, proving (6.2).  \(\square\)

This is the promised matching-state alternative in a precise form: two
matching faithful states would immediately colour (G).  It also shows
why mere exact star traces cannot finish the cell.  Star traces are
colourings of (G-v), not members of these operated full-graph state
sets.

## 7. Exact remaining source-tight residue

The absorption theorem in
`hadwiger_exact_gate_omitted_bag_absorption.md` gives a strict descent
from the exact multi-component case, but its higher-contact and
smaller-circuit exits are not closed.  Within the fixed source-tight
coordinates, the remaining geometric cases are:

1. (|P|\ge r), where the web components need not share one small exact
   adhesion.
2. (|P|=r-1) but (U-Y) has one component.  This is the literal
   four-terminal two-path/web cell: the two clean (Y)-to-(P) paths
   live in one component and a swapped pairing can fail.

For former residue 3--(|P|=r-1), at least two components, with neither
gate complete to (X)--the omitted-bag theorem forces a label-free private
region.  A singleton such region admits the exact-component hub move; a
nontrivial one has a far escape, whose two endpoint types are strict model
improvements.  Hence residue 3 has no terminal representative at fixed
contact/circuit coordinates, independently of gate--(X) support.  Its
exit is the genuine contact-maximal multiply-rooted-bag lock, not yet a
target minor.

In case 2, applying a Two Paths theorem requires care: its conclusion is
a web representation of the terminal network, not a planar embedding of
the original graph.  To close the case, one must prove that every
clique-filled facial piece either supplies the swapped portal pairing or,
after adjoining (X\cup\{v\}), yields an ambient cut of order at most
(r).  That implication is not proved here.

The next dynamic target is correspondingly exact: in residues 1--2 and
at the contact-maximal exit of residue 3,
show that one exact independent-star trace forces either a complete gate
after a legitimate first-hit exchange, or the same equality partition in
two opposite boundary-faithful minor operations.  The trace and transition
colourings must remain distinct until that exchange is established.
