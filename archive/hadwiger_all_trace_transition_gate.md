# All-trace edge transitions force a two-shore gate

## 1. Setting

Let (r\geq 2), and let (G) be a graph which is not
(r)-colourable although every proper minor of (G) is
(r)-colourable.  Fix (v\in V(G)), and put

\[
        H=G-v,\qquad N=N_G(v).
\]

The purpose of this note is to retain information which is absent from
the static haven/linkage statements.  We use simultaneously

* every exact trace obtained by contracting a star at (v); and
* the colouring transition obtained after deleting an arbitrary edge
  away from (v).

The resulting theorem is uniform in (r).  Its conclusion is an actual
two-shore state obstruction: the same boundary state cannot carry an
unpinned edge transition on both sides unless every free neighbourhood
colour has capacity on both sides.

For a colouring (a) of a graph containing a set (X), write
(\Pi_X(a)) for the equality partition of (X): two vertices of (X)
belong to the same block precisely when they have the same (a)-colour.

## 2. The two automatic families of colourings

### Lemma 2.1 (all independent traces)

For every nonempty independent set (S\subseteq N), there is a proper
(r)-colouring (c_S) of (H) such that one colour has trace exactly
(S) on (N).  Moreover all (r) colours occur on (N).

#### Proof

Contract the connected star (G[\{v\}\cup S]) to a vertex (z), and
colour the resulting proper minor.  On deleting (z), expand the
vertices of (S) with the colour of (z).  Every vertex of (N-S)
was adjacent to (z), so it avoids that colour.  Independence of (S)
and the definition of contraction show that the expansion is a proper
colouring of (H).

If a colour were absent from (N), it could be assigned to (v),
giving an (r)-colouring of (G).  Hence every colour occurs on (N),
and the colour of (z) has trace exactly (S).  \(\square\)

In particular, if

\[
                         |N-S|=r-1,                 \tag{2.1}
\]

then the vertices of (N-S) have pairwise distinct colours, each
private on (N).

### Lemma 2.2 (edge transitions)

Let (e=xy\in E(H)).  Every proper (r)-colouring (d) of (G-e)
satisfies

\[
                         d(x)=d(y),                 \tag{2.2}
\]

and the colour

\[
                         \alpha_d:=d(v)              \tag{2.3}
\]

is absent from (N).

For every colour (\gamma\ne d(x)), the vertices (x,y) lie in the
same (\{d(x),\gamma\})-Kempe component of (G-e).

#### Proof

The graph (G-e) is a proper minor and therefore is (r)-colourable.
If (2.2) failed, restoring (e) would preserve properness and colour
(G), a contradiction.  Every edge from (v) to (N) remains in
(G-e), so (2.3) is absent from (N).

If (x) and (y) lay in different
(\{d(x),\gamma\})-components, switch those two colours in the
component containing (x).  This keeps (G-e) properly coloured and
makes (x,y) different, so (e) could again be restored.  \(\square\)

Call (d) **unpinned at (X)** when

\[
                         d(v)\notin d(X).            \tag{2.4}
\]

## 3. The transition-splicing lemma

### Theorem 3.1 (one-shore transition orientation)

Let ((A,B)) be a separation of (H), with adhesion
(X=A\cap B), and let

\[
          e\in E(H[A])\setminus E(H[B]).            \tag{3.1}
\]

Let (c) be any proper (r)-colouring of (H), and let (d) be any
proper (r)-colouring of (G-e).  Suppose

\[
                         \Pi_X(c)=\Pi_X(d).           \tag{3.2}
\]

Then the following assertions hold.

1. If (d) is unpinned at (X), then

   \[
          [r]-c(X)\ \subseteq\ c\bigl(N\cap(A-X)\bigr).      \tag{3.3}
   \]

2. If (d(v)\in d(X)), let (Q) be its block in
   (\Pi_X(d)=\Pi_X(c)), and let (\delta) be the common (c)-colour
   on (Q).  Then

   \[
                         \delta\in c(N\cap A).        \tag{3.4}
   \]

#### Proof

Equality (3.2) gives a bijection from the colours used by (d) on
(X) to those used by (c) on (X).  Extend it to a permutation
(\pi) of the whole palette so that

\[
                         \pi d(x)=c(x)\quad(x\in X).  \tag{3.5}
\]

Put (\delta=\pi(d(v))).  Suppose, for a contradiction, that

\[
                         \delta\notin c(N\cap A).     \tag{3.6}
\]

Use (c) on (A), use (\pi d) on (B-A), and give (v) the
colour (\delta).  The two restrictions agree on (X).  Every edge
of (H[A]), including (e), is properly coloured by (c).  Every
edge having a vertex in (B-A) is an edge of (G-e), and is properly
coloured by (\pi d).  No edge joins the two open shores.  Finally,
vertices of (N\cap A) avoid (\delta) by (3.6), while vertices of
(N\cap(B-A)) avoid (\delta) because (d(N)) avoids (d(v)).
This is an (r)-colouring of (G), a contradiction.

If (d(v)\in d(X)), its image under every extension of (3.5) is the
fixed colour (\delta) in (3.4), so the contradiction just proved
forces (3.4).

If (d(v)\notin d(X)), then, as (\pi) ranges over all extensions of
the fixed boundary bijection, (\pi(d(v))) ranges over every colour
outside (c(X)).  Each such colour must therefore occur on
(N\cap A).  Since it is absent from (c(X)), its occurrence lies in
(A-X), proving (3.3).  \(\square\)

The asymmetry in (3.1) is essential only to ensure that the side
coloured with (d) does not contain the deleted edge.  The theorem has
the evident version with (A,B) interchanged.

### Corollary 3.2 (private-root orientation)

Under Theorem 3.1, suppose (d) is unpinned and (\gamma\notin c(X))
is private on (N) in the colouring (c).  Its unique root lies in

\[
                              N\cap(A-X).             \tag{3.7}
\]

Thus an unpinned transition does not merely orient a numerical linkage;
it orients every free private root to the shore containing the restored
edge.

## 4. The uniform two-shore capacity--state theorem

### Theorem 4.1 (two unpinned transitions consume double capacity)

Let ((A,B)) be a separation of (H), with adhesion (X).  Let

\[
 e_A\in E(H[A])\setminus E(H[B]),\qquad
 e_B\in E(H[B])\setminus E(H[A]).                         \tag{4.1}
\]

Let (c) be a proper (r)-colouring of (H).  Suppose that for
(i\in\{A,B\}) there is an unpinned (r)-colouring (d_i) of
(G-e_i) satisfying

\[
                         \Pi_X(d_i)=\Pi_X(c).          \tag{4.2}
\]

Then every colour outside (c(X)) occurs on (N) in both open
shores.  In particular,

\[
 |N-X|\ \geq\
 2\bigl(r-|c(X)|\bigr).                                  \tag{4.3}
\]

Consequently no colour outside (c(X)) is private on (N).

The later crossed-transition theorem in
hadwiger_fixed_model_transition_gate.md strengthens this statement:
the two unpinned transitions in (4.2) cannot coexist at all.  Cross the
two restrictions, using each transition on the side containing the
other transition's restored edge; their common unpinned boundary state
allows the two apex colours to be aligned.  The capacity conclusion
above remains a valid one-trace splice calculation, but is no longer
the sharp two-transition conclusion.

#### Proof

Apply Theorem 3.1 to (e_A), and then to (e_B) after interchanging
(A,B).  This gives

\[
 [r]-c(X)\subseteq c(N\cap(A-X))
 \quad\hbox{and}\quad
 [r]-c(X)\subseteq c(N\cap(B-X)).                         \tag{4.4}
\]

For every free colour choose one occurrence in each open shore.  These
are (2(r-|c(X)|)) distinct vertices, proving (4.3).  A private colour
cannot satisfy (4.4).  \(\square\)

### Corollary 4.2 (exact-trace exclusion)

Let (S\subseteq N) be independent with (|N-S|=r-1), and use the
exact trace (c_S) of Lemma 2.1.  If

\[
                         |c_S(X)|\le r-2,             \tag{4.5}
\]

then opposite internal edges cannot both have unpinned transition
colourings inducing (\Pi_X(c_S)).

#### Proof

The (r-1) colours on (N-S) are private.  At least one of them is
absent from (c_S(X)) under (4.5).  Theorem 4.1 would say that this
private colour occurs in both open shores.  \(\square\)

More generally, Theorem 4.1 applies to every independent trace from
Lemma 2.1.  Even when the non-(S) colours are not private, it forces
the quantitative double-capacity condition (4.3).  This is where using
all traces is stronger than retaining a single haven colouring.

## 5. A pinned transition is a Kempe-fan gate

The word *pinned* is not a disposal category.  A transition which
cannot be made unpinned carries a canonical fan through the adhesion.

### Theorem 5.1 (minimal pinning gives a full missing-colour fan)

Fix (e\in E(H)) and (X\subseteq V(H)).  Among all proper
(r)-colourings (d) of (G-e), choose one minimizing the cardinality of

\[
 P=P(d,X):=\{x\in X:d(x)=d(v)\}.                            \tag{5.1}
\]

If (P\ne\varnothing), then, for every colour
(\gamma\notin d(X)), every vertex of (P) lies in the
(\{d(v),\gamma\})-Kempe component containing (v).

Consequently, for every (p\in P) and every such (\gamma), there is
a (p)-to-(v) bichromatic path in (G-e).  Removing its last edge at
(v) gives a path in (H-e) from (p) to a neighbour of (v) of
colour (\gamma).

#### Proof

Put (\alpha=d(v)).  Suppose that an (\alpha)-coloured vertex
(p\in P) lies in an (\{\alpha,\gamma\})-component not containing
(v).  Switch (\alpha,\gamma) on that component.  No vertex of
(X) initially has colour (\gamma), so the switch introduces no new
(\alpha)-coloured vertex in (X), while it removes at least (p)
from (P).  The vertex (v) is unchanged.  This contradicts the
minimal choice of (d).

Thus every (p\in P) lies in the component containing (v), giving
the stated bichromatic path.  Since the neighbour of (v) immediately
before (v) on such a path has colour (\gamma), deleting (v) and
that last edge gives the final assertion.  \(\square\)

For (|X|<r), at least one colour is missing from (d(X)), so a
nonempty minimum pin is accompanied by a genuine Kempe path.  When
several colours are missing, the gate carries one bichromatic layer for
each missing colour.

### Corollary 5.2 (canonical fan-or-state-change across a transit adhesion)

In the setting of Theorem 4.1, fix an exact trace (c_S) satisfying
(4.5).  For each (i\in\{A,B\}), choose a colouring (d_i) of
(G-e_i) which globally minimizes

\[
       |\{x\in X:d_i(x)=d_i(v)\}|                         \tag{5.2}
\]

among all colourings of that edge-deleted graph.  At least one of the
following occurs:

1. (\Pi_X(d_i)\ne\Pi_X(c_S)) for at least one side (i); or
2. one of the two globally minimum transitions has a nonempty pinned
   block on (X), and that block carries the missing-colour Kempe fan
   of Theorem 5.1.

In particular, an adhesion crossed by a model-transit bag cannot be
transparent to the same exact trace on both sides.  It is forced to be
either a **partition-changing gate** or a **pinned Kempe-fan gate**.

#### Proof

If either chosen minimum transition changes the boundary partition,
outcome 1 holds.  Otherwise both induce the trace state.  If both pinned
blocks were empty, Corollary 4.2 would give a contradiction.  Hence one
chosen transition is pinned, and its global minimality lets Theorem 5.1
supply the fan.  \(\square\)

This is an operation-sensitive conclusion, unlike a static linkage or
same-haven assertion.  It applies in particular when (e_A,e_B) are
essential edges of the same branch bag on opposite sides of a proposed
cleaning cut.

## 6. Sharpness: pinning cannot simply be discarded

Let (G=C_7), in cyclic order

\[
                         v,1,2,3,4,5,6,v,
\]

and take (r=2).  This graph is edge-minimal non-two-colourable, although
it is not proper-minor-minimal (it has a (C_5) minor).  It satisfies
the local hypotheses actually used in Theorems 3.1--5.1 for the two
displayed edge deletions and for the displayed exact singleton trace.
Put (H=G-v), let

\[
 A=\{1,2,3\},\quad B=\{3,4,5,6\},\quad X=\{3\}.
\]

The unique two-colouring of (H) has the two private neighbourhood
roots (1,6).  Boundary equality partitions on the singleton (X)
are automatic.

For (e_A=12), every two-colouring of (G-e_A) gives (v) and (3)
the same colour: the transition is pinned.  For (e_B=56), they have
opposite colours: the transition is unpinned.  Thus the tempting
strengthening "every internal edge has an unpinned transition at every
proper adhesion" is false even for an edge-critical graph satisfying all
the local splice hypotheses.  The pinned side carries exactly the
bichromatic path predicted by Theorem 5.1.

At the same time, the example realizes the sharp polarity of the splice
argument: the two opposite transitions cannot both be unpinned in the
common exact-trace state.  No claim is made that it is a counterexample
inside the full proper-minor-minimal class.

## 7. What has and has not been proved

The theorem closes a genuine abstract loophole exposed by
`hadwiger_same_haven_cleaning_counterexample.md`.  Full component
alignment plus a Rado linkage was static and allowed an arbitrary transit
comb.  In a proper-minor-minimal apex obstruction, a transit adhesion is
additionally constrained as follows:

\[
\begin{array}{c}
\text{same exact boundary state on both shores}\cr
\Downarrow\cr
\text{double neighbourhood capacity, or a pinned Kempe fan;}\cr
\text{a private free trace colour rules out double capacity.}
\end{array}
\]

What remains is geometric: convert the pinned fan into a
label-preserving split of the transit bag, or show that its common
Kempe gate realizes a two-sided rooted clique partition and is therefore
colour-gluable.  The present result does not assert that every pinned fan
can be so packaged.  It does prove that a surviving obstruction must be
operation-state rigid; it cannot be another static model-cleaning
counterexample.
