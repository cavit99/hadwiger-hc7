# Co-rank-one Hall circuits: clean portal bases and exact model descent

## 1. Status and purpose

This note proves a uniform carrier-cleaning statement in the first cell in
which the Hall-circuit colour and label collisions are already aligned.
It does not assume a Moser boundary or a particular value of (r).

The main new point is stronger than the numerical estimate

\[
                         |P|\ge k-r+1.
\]

For a co-rank-one Hall circuit, the root shore contains a linkage to **all**
of the Hall interface (X) and to (k-r+1) portal vertices at the same
time.  Moreover the portal endpoints and the linkage can be chosen so that
every portal path first meets the old model at its endpoint.  Thus the
usual first-extra-portal obstruction disappears on the root shore by a
literal gammoid-basis exchange.

When (k\ge r+1), two such clean portal paths exist.  They are disjoint
from the complete (X)-linkage used by the far-side Hall certificate.  A
connected split of the multiply hit accessible bag can therefore be
performed without any hidden collision among the root paths.  The only
remaining obstruction is exact and model-labelled: after one deficient
bag is omitted, one of the two pieces misses a retained bag label.

A second theorem gives the promised descent from a first-hit carrier.  If
its (B)-piece is a safe peel, moving that piece to the deficient bag
strictly increases model contact.  In the co-rank-one cell the new model is
either fully linkable or has a Hall circuit of strictly smaller order.

The last section records a necessary negative result.  Circuit elimination
in the **original bag-terminal gammoid** cannot see two portals belonging to
one bag: they have the same artificial sink.  Thus the portal-basis gammoid
on the root shore, rather than the old bag-label gammoid alone, is essential.

## 2. Co-rank-one setup

Let (G) be (k)-connected, let (v\in V(G)), put (L=G-v), and let

\[
                  \mathcal B=(B,B_1,\ldots,B_{r-1})       \tag{2.1}
\]

be a labelled (K_r)-model in (L).  Assume the following.

1. (B) contains exactly one vertex (a\in N_G(v)), and none of
   (B_1,\ldots,B_{r-1}) meets (N_G(v)).
2. (I=\{1,\ldots,r-1\}) is a Hall circuit in the model-avoiding
   gammoid of `hadwiger_relative_deficit_circuit_promotion.md`.
3. (X) is its exact separator, (U) is the root-side union, and

   \[
                            |X|=r-2.                       \tag{2.2}
   \]

4. The promoted portal set lies in the unique accessible bag:

   \[
                  P=N_L(U)\cap B,\qquad P_i=\varnothing
                  \quad(i\in I).                          \tag{2.3}
   \]

Write

\[
                         Q=B\cup\bigcup_{i\in I}B_i,
 \qquad R=N_G(v)-Q.                                      \tag{2.4}
\]

Since (G) is (k)-connected, (d(v)\ge k); hence

\[
                         |R|=d(v)-1\ge k-1.               \tag{2.5}
\]

The Hall promotion theorem also gives

\[
                         |P|\ge k-(r-1)=k-r+1.             \tag{2.6}
\]

All paths below are paths in (L).  A root-to-(X\cup P) path is
**shore-clean** when its internal vertices lie in (U); in particular it
does not run through an old branch bag.  A family of such paths is a
linkage when the paths, including their endpoints, are pairwise
vertex-disjoint and have distinct roots in (R).

## 3. The root-shore portal-basis theorem

The rank argument is not intrinsically co-rank one.  We record its
label-free form first.  Let (I) be any promoted Hall circuit of order
(h), let (|X|=h-1), let (U,P,R) have their usual meanings, and assume
only that (G) is (k)-connected.  Define the root-shore gammoid on
(X\cup P) exactly as below.

### Proposition 3.0 (general root-shore capacity rank)

Put

\[
                         m=\min\{k-1,|R|\}.                 \tag{3.0}
\]

Then the root-shore gammoid has rank at least (m).  Consequently (X)
extends to a shore-clean linkage endpoint set

\[
                         X\mathbin{\dot\cup}Z,
 \qquad Z\subseteq P,
 \qquad |Z|\ge m-(h-1),                                  \tag{3.0a}
\]

whenever the last quantity is positive.  The endpoint set and linkage may
be chosen so that each (Z)-path first meets (P) at its endpoint.

#### Proof

The promotion theorem gives

\[
                         |X|+|P|\ge k-1,                   \tag{3.0b}
\]

so the ground set has at least (m) elements.  If the rank were
(ho<m), Menger would give a root-shore source-to-boundary separator
(Y) of order (ho).  Since (ho<|R|), a source survives outside
(Y); as in the proof of Theorem 3.1 below, its (U-Y) component has all
of its neighbours in (Y\cup\{v\}).  This is a cut of order
(ho+1\le k-1), a contradiction.  Thus the rank is at least (m).

The exact Hall linkage makes (X) independent.  Extend it to an
independent set of order (m); the added elements form (Z\subseteq P).
Minimizing total linkage length and truncating at a first earlier portal
proves the final cleaning assertion exactly as in Theorem 3.1. (square)

The source count is essential in this general form.  Connectivity cannot
force more disjoint root paths than there are unused roots.  In the
co-rank-one setup (2.1)--(2.6), (2.5) gives (|R|\ge k-1), so Proposition
3.0 attains the full ambient bound.

### Theorem 3.1 (clean portal basis)

Under the setup above there are a set

\[
                         Z\subseteq P,
 \qquad |Z|\ge k-r+1,                                  \tag{3.1}
\]

and a shore-clean linkage from distinct roots in (R) to every vertex of

\[
                         X\mathbin{\dot\cup}Z.             \tag{3.2}
\]

The set (Z) and the linkage can be chosen so that every path ending at a
vertex (z\in Z) meets (P) for the first time at (z).

In particular, if (k\ge r+1), there are distinct (p,q\in P) and a
single linkage to (X\cup\{p,q\}) whose (p)- and (q)-paths first meet
the old model at (p) and (q), respectively.

#### Proof

Form the root-shore gammoid (M_U) on ground set (X\cup P).  A set is
independent when it is the endpoint set of a shore-clean linkage from
distinct vertices of (R).  This is a strict gammoid: split every member
of (X\cup P) off as a sink and give all vertices unit capacity.  A root
which itself belongs to (X) is allowed to give the corresponding
length-zero path.

We first prove

\[
                         r(M_U)\ge k-1.                    \tag{3.3}
\]

Suppose instead that its rank is (ho\le k-2).  The vertex form of
Menger's theorem gives a set (Y) of order (ho) separating the source
set (R-Y) from ((X\cup P)-Y) in the root shore.  By (2.5), choose
(s\in R-Y).  The vertex (s) cannot lie in ((X\cup P)-Y), since the
length-zero path would evade the separator.  Hence (s\in U-Y).

Let (C) be the component of (U-Y) containing (s).  If (C) had a
neighbour in ((X\cup P)-Y), there would be an (R-Y)-to-
((X\cup P)-Y) path avoiding (Y).  By the promotion theorem all
neighbours of (U) in (L-U) lie in (X\cup P).  Consequently

\[
                         N_G(C)\subseteq Y\cup\{v\}.       \tag{3.4}
\]

The set (C) is nonempty, and every deficient bag (B_i) survives on the
other side of (3.4).  Thus (Y\cup\{v\}) is a vertex cut of order at most
(k-1), contrary to (k)-connectivity.  This proves (3.3).

The exact Hall theorem supplies a linkage to all of (X), so (X) is
independent in (M_U).  Extend (X) to an independent set of order
(k-1).  Every added ground element lies in (P); hence the added set
(Z) has order

\[
                    (k-1)-|X|=(k-1)-(r-2)=k-r+1.          \tag{3.5}
\]

Choose, over all such endpoint sets (Z) and all their linkages, one of
minimum total length.  Suppose a path ending at (z\in Z) meets another
portal (q\in P) before (z).  No other linkage path ends at (q), by
vertex-disjointness.  Truncate the path at its first such (q), and
replace (z) by (q) in (Z).  This is a linkage to

\[
                         X\cup(Z-z+q)
\]

of the same order and strictly smaller total length, a contradiction.
Thus every portal path is clean.  Discarding all but two portal paths gives
the final assertion. (square)

### Remark 3.2 (what has actually been cleaned)

Theorem 3.1 cleans a carrier in the sense needed for branch-set surgery:
the path contains no old branch-bag vertex before its named endpoint and
is disjoint from every root-to-(X) path.  It does not claim that an
unrelated bichromatic Kempe carrier is clean.  If a Kempe carrier first
hits a different portal, its endpoint can be changed only when the
corresponding endpoint exchange remains independent in (M_U/X).

### Corollary 3.3 (capacity--colour collision alignment)

Assume (k\ge r+1), and let (c) be any (r)-colour boundary state in
which

\[
                         \{v\}\cup X
\]

is rainbow.  The clean portal basis (Z) in Theorem 3.1 may be used as a
collision carrier endpoint set.  More precisely, either

1. some (z\in Z) has the colour of a unique vertex of
   ({v}\cup X); or
2. two distinct (p,q\in Z) have the same colour, namely the unique
   colour missing on ({v}\cup X).

In both cases all displayed portal endpoints have mutually disjoint clean
root carriers, simultaneously disjoint from the complete (X)-linkage.

#### Proof

The rainbow core has order (r-1), so exactly one of the (r) colours is
missing on it.  If a member of (Z) uses a core colour, outcome 1 holds.
Otherwise every member of (Z) uses the single missing colour.  Theorem
3.1 gives

\[
                         |Z|\ge k-r+1\ge2,
\]

so outcome 2 holds.  The carrier assertion is part of Theorem 3.1.
(square)

Thus in the co-rank-one cell the colour collision is aligned not only with
the unique multiply hit model bag, as in the anti-diamond theorem, but also
with a root-side linkage basis.  No further pigeonhole or choice of Kempe
trace is needed for that alignment.

## 4. Exact split-or-labelled-lock consequence

For (i\in I), let the far side Hall certificate omitting (i) be fixed.
It consists of pairwise disjoint suffixes from (X) to the bags

\[
                         B_j\qquad(j\in I-\{i\}).           \tag{4.1}
\]

Adjoin each suffix to its terminal bag.  The resulting sets are pairwise
adjacent because the old bags form a clique model.

### Theorem 4.1 (two-foot split or a two-label lock)

Assume (k\ge r+1), and choose (p,q) and the common linkage from
Theorem 3.1.  Let

\[
                         B=Y_p\mathbin{\dot\cup}Y_q        \tag{4.2}
\]

be any partition into nonempty connected sets with (p\in Y_p),
(q\in Y_q), and with an edge between the two sets.  If some (i\in I)
satisfies

\[
 E(Y_p,B_j)\ne\varnothing\ne E(Y_q,B_j)
 \qquad\text{for every }j\in I-\{i\},                    \tag{4.3}
\]

then (G) contains a (K_{r+1})-minor.

Consequently, in a (K_{r+1})-minor-free graph, every connected
(p)-(q) split (4.2) has at least two retained-label defects.  More
precisely, put

\[
 D_p=\{j\in I:E(Y_p,B_j)=\varnothing\},\qquad
 D_q=\{j\in I:E(Y_q,B_j)=\varnothing\}.                  \tag{4.4}
\]

Then (D_p\cap D_q=\varnothing) and

\[
                         |D_p\cup D_q|\ge2.                \tag{4.5}
\]

#### Proof

Use the root-side linkage from Theorem 3.1, retaining its paths to all of
(X) and to (p,q).  Concatenate the (X)-paths with the far suffixes
in (4.1).  This gives (r-2) pairwise disjoint connected branch sets,
one for each (j\in I-\{i\}), and each contains a distinct vertex of
(N_G(v)).  The two unused portal paths are absorbed respectively into
(Y_p) and (Y_q).  They are disjoint from one another and from all
(X)-paths by Theorem 3.1, so the resulting (r) branch sets are
pairwise disjoint.

The (r-2) far branch sets are pairwise adjacent.  Condition (4.3) makes
each of (Y_p,Y_q) adjacent to every one of them, and the last two sets
are adjacent to each other by (4.2).  Thus they form a (K_r)-model all
of whose bags meet (N_G(v)).  The singleton ({v}) completes a
(K_{r+1})-model.

Every old (B_j) has an edge to (B), so a label cannot lie in both
(D_p) and (D_q).  If their union had order at most one, omit that one
label (or any label if the union is empty); then (4.3) would hold.  This
proves (4.5). (square)

### Corollary 4.2 (the geometric part of the double-foot problem is gone)

For any two distinct vertices (p,q) in a connected graph (B), a split
(4.2) exists: take a spanning tree, delete an edge of its (p)-(q)
path, and assign the remaining tree branches to their components.
Therefore the co-rank-one residue is not failure to obtain two connected,
adjacent rooted pieces.  It is exactly the two-label lock (4.5): every
such split loses retained model adjacency on at least two labels.

## 5. First-hit peel and strict Hall descent

Fix (i\in I).  Since (B_i) and (B) are adjacent connected branch
bags, there is a path in (L[B_i\cup B]) from (B_i) to (P).  Choose
one and orient it from (B_i).  Stop at its first vertex (q\in P), and
let (C) be the nonempty final segment lying in (B).  Then

\[
 C\text{ is connected},\quad C\cap P=\{q\},\quad
 E(C,B_i)\ne\varnothing.                                \tag{5.1}
\]

Thus taking the first extra portal is a literal carrier cleaning: any
later portal endpoint gives a strictly longer carrier than (5.1).

Call (C) a **safe (i)-peel** if

\[
\begin{array}{ll}
\text{(a)}&a\notin C;\\
\text{(b)}&B-C\text{ is nonempty and connected};\\
\text{(c)}&E(B-C,B_j)\ne\varnothing
             \quad(j\in I-\{i\}).
\end{array}                                               \tag{5.2}
\]

### Theorem 5.1 (safe peel gives contact increase or a smaller circuit)

If the first-hit carrier has a safe (i)-peel, then there is a labelled
(K_r)-model with two contacted bags.  Relative to that model, either all
remaining bags (B_j), (j\in I-\{i\}), are simultaneously linkable, or
there is a Hall circuit of order at most (r-2), strictly smaller than
the original circuit (I).

In particular, a contact-maximal co-rank-one model has no safe first-hit
peel.

#### Proof

The portal (q) has a neighbour in a component of (U) containing an
unused root (z\in R).  Choose a (z)-to-(q) path (R_q) whose internal
vertices lie in (U).  Define new branch sets

\[
 B'=B-C,\qquad B_i'=B_i\cup C\cup R_q,\qquad
 B_j'=B_j\quad(j\ne i).                                  \tag{5.3}
\]

They are disjoint: (R_q-q) lies outside the old model, and (C) has
been removed from (B) before being added to (B_i).  The sets (B')
and (B_i') are connected by (5.2)(b), (5.1), and the definition of
(R_q).  Since (B) was connected and (C,B-C) are both nonempty, an
edge joins (C) to (B-C); hence (B') is adjacent to (B_i').

For (j\ne i), the new (B_i') remains adjacent to (B_j) through the
old bag (B_i).  Condition (5.2)(c) retains every adjacency from (B')
to (B_j), (j\ne i).  All other old adjacencies are unchanged.  Thus
(5.3) is a (K_r)-model.

The bag (B') still contains the old root (a), while (B_i') contains
the distinct unused root (z).  Contact has increased from one bag to
two.  The only uncontacted bags of the new model are indexed by
(I-\{i\}).  If they are linkable, absorb a corresponding linkage.  If
they are not, choose an inclusion-minimal nonlinkable subset (J).  It is
a Hall circuit and

\[
                         |J|\le |I|-1=r-2.                 \tag{5.4}
\]

This proves the dichotomy.  A contact-maximal model forbids (5.3)
already at the contact-increase step. (square)

### Corollary 5.2 (exact first-hit blockers)

If no contact increase and no smaller Hall circuit is possible, every
first-hit (i)-carrier is blocked by at least one of the following, and
there is no fourth geometric failure:

1. its (B)-segment contains the protected root (a);
2. deleting that segment empties or disconnects (B);
3. for some (j\in I-\{i\}), that segment contains every attachment of
   (B) to (B_j).

This follows simply by negating (5.2).  The list is useful because every
blocker has a named object: a protected root, a cut-lobe, or a retained
bag label.

### Corollary 5.3 (cleaning a core-colour collision carrier)

Use Corollary 3.3, and suppose (z\in Z) has the colour of some
(x\in X).  In the far Hall certificate omitting an index (i), let the
(x)-rooted branch set contain the original deficient bag (B_j), where
(j\ne i).  The connected carrier in (B\cup A_x) may be chosen to run
inside (A_x) to (B_j), cross one old (B_j)-(B) edge, and then run
inside (B) toward (z).  Stop this carrier at the first portal
(q\in P) encountered after entering (B), and call its (B)-segment
(C).

Then (C) is a first-hit (j)-carrier satisfying (5.1).  Consequently
either

1. (C) is safe and Theorem 5.1 strictly increases contact or replaces
   (I) by a smaller Hall circuit; or
2. (C) has one of the three exact blockers in Corollary 5.2.

#### Proof

The original bags (B_j) and (B) are connected and adjacent.  The
(x)-branch contains (B_j), so choose the carrier with the prescribed
old interbag edge.  Its first (P)-vertex gives a connected (B)-segment
which meets (P) only at its endpoint and is adjacent to (B_j).  This
is precisely (5.1), after which Theorem 5.1 and Corollary 5.2 apply.
(square)

Thus a core-colour collision carrier never remains merely “dirty.”  Its
first dirt is either absorbed with strict Hall descent or is certified by
a protected root, a cut-lobe, or a named unique-attachment label.  The
same conclusion applies when the first dirt is an additional portal rather
than the originally selected endpoint (z).

## 6. Faithful-operation audit

Put

\[
                         S=\{v\}\cup X\cup P.              \tag{6.1}
\]

This is the genuine promoted adhesion.  A minimum linkage in Theorem 3.1
has a portal path (R_z) meeting (S) exactly in its endpoint (z).
Contracting (R_z) onto (z) is therefore a boundary-anchored root-shore
operation: it is faithful to the closed far shore.

Likewise a first-hit segment (C) from (5.1) meets (S) exactly in
(q).  If (|C|\ge2), contracting (C) onto (q) is a
boundary-anchored far-shore operation faithful to the closed root shore.
No two vertices of (S) are identified in either operation.

Consequently Theorem 2.1 of
`hadwiger_crossed_arbitrary_minor_operations.md` applies literally:
colourings of these two opposite proper minors cannot induce the same
equality partition on (S).  If such compatible states are ever obtained,
their cross-pullbacks colour (G).

This is an exact audit, not an existence assertion.  Neither gammoid
exchange nor first-hit truncation forces the two boundary partitions to
agree.  The surviving blockers in Corollary 5.2 still require a dynamic
state argument or a label-preserving lobe exchange.

## 7. Why the old bag-label gammoid cannot do this job

### Proposition 7.1 (same-sink portal blindness)

For every (h\ge2) there is a strict gammoid on elements

\[
                         I\mathbin{\dot\cup}\{b\},
 \qquad |I|=h,                                           \tag{7.1}
\]

such that

1. (I) is a circuit;
2. (b) belongs to no circuit; and
3. the terminal (b) can be given arbitrarily many different incoming
   portal routes without changing either conclusion.

Thus circuit elimination on bag labels cannot turn a first extra portal
of one accessible bag into a smaller circuit.

#### Proof

Take (h) sources and an intermediate set
(X_0=\{x_1,\ldots,x_{h-1}\}).  Join every source to every (x_j), and
join every (x_j) to every terminal in (I).  Any (h-1) members of
(I) are linkable, while all (h) are not, so (I) is a circuit.

Add a terminal (b).  From each source give a private two-edge route to
(b); subdividing or duplicating these routes gives arbitrarily many
portal realizations of the same terminal.  The set consisting of (b)
and any (h-1) elements of (I) is linkable: use one source on a private
(b)-route and the remaining (h-1) sources through the distinct
vertices of (X_0).  Hence (b) is a coloop in the restriction to
(I\cup\{b\}), and the only circuit there is (I).  Extra incoming
routes to the same sink do not create a new ground element and cannot
alter circuit elimination. (square)

Theorem 3.1 avoids this blindness by putting the **individual portal
vertices** in a second, root-shore gammoid.  The two gammoids have different
ground sets and different jobs:

* the old bag-label gammoid gives the exact far-side circuit and its
  (X)-rooted clique model;
* the root-shore portal gammoid gives clean, simultaneous carriers to
  (X) and to individual portal vertices.

Theorem 4.1 composes the two certificates.  What remains after the
composition is the two-label split lock (4.5), not an unexamined path
intersection or a fictitious application of circuit elimination.

## 8. Exact remaining co-rank-one residue

The co-rank-one carrier problem has therefore descended to the following
audited object.

* There are two portal vertices (p,q) with clean mutually disjoint root
  carriers, simultaneously disjoint from the complete (X)-linkage.
* The accessible bag always has a connected adjacent (p)-(q) split.
* Every such split has at least two named retained-label defects.
* Every first-hit transfer toward a deficient bag is locked by a protected
  root, a cut-lobe, or a unique retained-label attachment; otherwise the
  Hall circuit strictly shrinks.
* Clean opposite contractions are boundary-faithful, but equality of their
  full (S)-states is not automatic.

This is a genuine uniform rooted-model reduction: it removes all carrier
intersection ambiguity in the co-rank-one cell and proves strict descent
whenever a first-hit lobe is geometrically movable.  The unresolved step is
now specifically to show that the two-label lock and all first-hit blockers
cannot coexist with the proper-minor transition states.
