# The terminal degree-nine lobe: a two-root swap and its exact obstruction

## 1. Terminal state

Continue with outcome 2 of Theorem 5.1 in
`hadwiger_degree9_two_carrier_capacity_exchange.md`.  Thus the connected
sets are

\[
                         Z,D,Q,R_5,R_0,
\]

where (Z) contains the root (e_6) of (L_6), (D) contains (6),
and (Q) contains the root (e_0) of (L_0).  The set (Z) has no
contact to (R_5,R_0,3,4), while (D) and (Q) retain their two
right target classes.

There are a vertex (s\in Q) and a component (J) of (Q-s) such
that

\[
 e_0\in J,qquad N_Q(Z)\subseteq J\cup\{s\},qquad
 N_Q(Z)\cap J\ne\varnothing,                              \tag{1.1}
\]

and (J) has no contact to either right bag.  Put

\[
                              S=Q-J.                        \tag{1.2}
\]

Then (S) is connected, (J\sim S), and (S) contains every
(Q)-portal to (R_5\cup R_0).  This is the sole terminal state of
the alternating exchange.

For a set (X) outside (Z), write

\[
                P_X=\{z\in Z:z\text{ has a neighbour in }X\}.
                                                               \tag{1.3}
\]

## 2. A two-root swap closes

### Theorem 2.1 (terminal two-root swap)

Suppose (Z) has a connected bipartition

\[
                            Z=E\mathbin{\dot\cup}T           \tag{2.1}
\]

such that

\[
 e_6\in E,qquad
 E\cap P_D\ne\varnothing,quad E\cap P_S\ne\varnothing,
 \qquad
 T\cap P_D\ne\varnothing,quad T\cap P_J\ne\varnothing.
                                                               \tag{2.2}
\]

Then (G) contains a (K_7)-minor.

#### Proof

Use the seven branch sets

\[
 \{h\},\quad \{1\},\quad \{2\},\quad
 E,\quad T\cup J,\quad D\cup R_5,
 \quad \{v,3\}\cup S\cup R_0.                             \tag{2.3}
\]

They are disjoint.  The fifth set is connected through the
(T)-(J) contact.  The sixth is connected through (65), and the
last is connected through an (S)-(R_0) portal, the right-root--(3)
edge, and (3v).

The last four sets form a clique.  The six witnesses, in their displayed
order, are

\[
 ET,quad E D,quad E S,quad T D,quad J S,quad v6.       \tag{2.4}
\]

Here the first witness exists because a connected graph partitioned into
two nonempty connected sets has an edge between the sides.  Finally,
(E) sees (h,1,2) through (e_6), (T\cup J) through (e_0),
(D\cup R_5) through (6) and the right root in (R_5), and the last
set through (v) and the right root in (R_0).  Together with (12),
this audits all twenty-one adjacencies.  Thus (2.3) is a (K_7)-model.
\(□\)

The operation really swaps the spare roots: (T) is joined to the
ordinary root side (J), while the outer root side (E) is joined across
the bottleneck to the target side (S).

Two simpler cross patterns close before the internal split is needed.

### Lemma 2.2 (direct terminal crosses)

If (Z\sim S) and either

\[
                         J\sim D                              \tag{2.5}
\]

or

\[
                         J\sim\{3,4\},                       \tag{2.6}
\]

then (G) contains a (K_7)-minor.

#### Proof

Under (2.5), use

\[
 \{h\},\{1\},\{2\},Z,J,
 D\cup R_5,\ \{v,3\}\cup S\cup R_0.                       \tag{2.7}
\]

The last four sets form a clique through
(ZJ,ZD,ZS,JD,JS,v6), respectively.

For (2.6), suppose (J\sim3); the other case is symmetric.  Use

\[
 \{h\},\{1\},\{2\},Z,J\cup\{3\},
 D\cup R_5,\ \{v,4\}\cup S\cup R_0.                       \tag{2.8}
\]

The last four sets meet through
(ZJ,ZD,ZS,3R_5,34,v6).  Connectivity and the contacts to
(h,1,2) follow from the two left roots, (6), (v), and the two
right roots exactly as in (2.3).  \(□\)

Thus, in a minor-free terminal state with (Z\sim S),

\[
                          J\not\sim D,3,4.                   \tag{2.9}
\]

Since (J) is a component of (Q-s), is target-free, and contains
the ordinary-left root, (2.9) gives the exact neighbourhood

\[
             N_G(J)=\{h,1,2,s\}\mathbin{\dot\cup}P_J.       \tag{2.10}
\]

Seven-connectivity therefore forces

\[
                              |P_J|\ge3.                     \tag{2.11}
\]

Equality in (2.11) is another exact seven-interface.  Thus, once even
one (Z)-(S) contact exists, the surviving root lobe has at least three
*distinct vertices of (Z)* on its portal side.

In fact the entire (Z)-(S) branch is impossible.

### Theorem 2.3 (the target-side contact is excluded)

In a seven-connected (K_7)-minor-free terminal state,

\[
                              Z\not\sim S.                   \tag{2.12}
\]

Hence every (Z)-(Q) portal lies strictly in the root-bearing lobe
(J), not at (s) or on the target side.

#### Proof

Suppose (Z\sim S).  Lemma 2.2 gives (K_7) unless
(J\not\sim D,3,4), so assume these noncontacts.  Put
(U=Z\cup J).  The set (U) is connected because (J) contains a
(Z)-portal.  Its only neighbours are

\[
          N_G(U)=\{h,1,2,s\}\mathbin{\dot\cup}N_D(Z).       \tag{2.13}
\]

Indeed, (J) leaves (Q) only through (s), is target-free, and has no
(D,3,4)-contact; (Z) has no right or (3,4)-contact and all its
(Q)-contacts lie in (J\cup\{s\}).  The active-carrier invariant says

\[
              N_D(Z)=\{6\}\quad\hbox{or}\quad\{6,c\}.      \tag{2.14}
\]

Thus (|N_G(U)|\le6).  This is a genuine separator from (v) and the
right bags, contradicting seven-connectivity.  \(□\)

There is no hidden double count in (2.13): because (J) is a component
of (Q-s), every (J)-(Q-J) edge is incident with the single vertex
(s); and because (N_Q(Z)\subseteq J\cup\{s\}), a (Z)-(S)
edge is also incident with that same (s).  The old inactive carrier is
(D), so its complete contact set with (Z) is exactly one of the two
sets in (2.14).

The exact capacity left by (2.12) is worth recording.  Put

\[
 P_D(U)=N_D(Z\cup J),\qquad
 C_{34}(J)=N_{\{3,4\}}(J).                                  \tag{2.15}
\]

Then

\[
 N_G(Z\cup J)=\{h,1,2,s\}\mathbin{\dot\cup}P_D(U)
                    \mathbin{\dot\cup}C_{34}(J),            \tag{2.16}
\]

and seven-connectivity gives

\[
                         |P_D(U)|+|C_{34}(J)|\ge3.           \tag{2.17}
\]

Thus the sole terminal residue is a **fully nested root lobe**: all
active portals enter (J), while (J) must send at least three total
exits toward the inactive carrier and the two cross literals.

## 3. Exact two-linkage formulation

The hypothesis of Theorem 2.1 is equivalent to the following finite
two-linkage condition inside (Z).

Theorem 2.3 subsequently shows that the actual terminal state has
(P_S=\varnothing), so this two-linkage is not the final mechanism.  We
retain the formulation and web audit because they rigorously eliminate
the tempting target-side branch and identify why it cannot be the
surviving obstruction.

### Lemma 3.1 (two disjoint Steiner connectors)

There is a bipartition (2.1)--(2.2) if and only if (Z) contains two
vertex-disjoint connected subgraphs (K_E,K_T) such that

\[
 \begin{array}{c|ccc}
       &\text{root}&D\text{-portal}&\text{opposite carrier portal}\\ \hline
 K_E&e_6&P_D&P_S\\
 K_T&-&P_D&P_J.
 \end{array}                                                \tag{3.1}
\]

In the table, an entry means that the connected subgraph contains a
vertex of the indicated set.

#### Proof

Given (E,T), take in each side a minimal tree joining the displayed
vertices.  Conversely, contract the two disjoint connected subgraphs,
take a spanning tree of (Z), and delete an edge on the path between the
two contracted vertices.  Undoing the contractions gives a connected
bipartition with the two prescribed subgraphs on opposite sides.
\(□\)

Consequently, in a (K_7)-minor-free host the terminal lobe satisfies
the exact obstruction

> there are no two disjoint connected subgraphs in (Z), one joining
> (e_6) to a (D)-portal and an (S)-portal, and the other joining a
> second (D)-portal to a (J)-portal.                         \(\tag{3.2}\)

This is the genuine next theorem-strength input.  It is narrower than an
arbitrary rooted (K_5) or web statement: it is a two-tree packing in one
specified carrier, with four labelled portal classes and one protected
root.

## 4. Two Paths reduction and the forced web order

The obstruction (3.2) has a canonical standard two-paths shadow.  Fix a
path (R\subseteq Z) from (e_6) to (P_D), chosen shortest, and
contract (R) to a vertex (a).  Let (\pi) be the contraction map.
Form (H_R) from (Z/R) by adding three new vertices (b,c,d) with

\[
 N(b)=\pi(P_S),\qquad N(c)=\pi(P_J),\qquad
 N(d)=\pi(P_D).                                           \tag{4.1}
\]

The four new frame vertices are taken in the cyclic order

\[
                              (a,c,b,d).                    \tag{4.2}
\]

### Theorem 4.1 (clean crossing or ordered web)

For every such protected root--(D) path (R), exactly one of the
following holds.

1. (H_R) has disjoint paths from (a) to (b) and from (c) to
   (d).  Then (G) has a (K_7)-minor.
2. (H_R) is a subgraph of a four-web whose frame, in cyclic order, is
   (a,c,b,d).

#### Proof

In outcome 1, delete the three added terminal vertices and undo the
contraction of (R).  The first path together with (R) is a connected
subgraph meeting (e_6,P_D,P_S); the second is a disjoint connected
subgraph meeting (P_J,P_D).  Lemma 3.1 and Theorem 2.1 give the
(K_7)-minor.

If the two paths do not exist, the tuple (a,c,b,d) is crossless.
The generalized Two Paths Theorem says precisely that every crossless
tuple embeds in a web with that tuple as its frame.  The crossing pairs
for the order (4.2) are (a,b) and (c,d), so this is outcome 2.
\(□\)

The invoked result is Theorem 1.5 of Humeau--Pous, *On the Two Paths
Theorem and the Two Disjoint Paths Problem* (2025), equivalently the
classical Robertson--Seymour/Thomassen Two Paths Theorem in its web
form.  Thus, in a minor-free terminal state, **every** choice of the
protected path (R) produces this same alternating frame order.

Seven-connectivity already removes every underloaded piece of the web.

### Lemma 4.2 (web-cell load)

Let (X) be a nonempty proper subset of (Z-R), and suppose

\[
                              |N_Z(X)|\le3.                  \tag{4.3}
\]

Then

\[
                         |N_G(X)-Z|\ge 7-|N_Z(X)|.           \tag{4.4}
\]

In particular, a piece separated from the rest of (Z) by a facial
triangle of the web has at least four external neighbours.  It must meet
at least one of the nonfixed carrier portal classes (C\cup A) in the
capacity invariant (5.4b) of the preceding note.

#### Proof

The set (N_Z(X)\cup(N_G(X)-Z)) is a genuine separator of (G), so
seven-connectivity gives (4.4).  The only (h)-neighbour in (Z) is
(e_6\in R).  Hence a set (X\subseteq Z-R) has no (h)-contact, and

\[
        N_G(X)-Z\subseteq\{1,2,6\}\cup C\cup A.             \tag{4.5}
\]

For a three-vertex internal boundary, (4.4) requires four external
vertices, while (\{1,2,6\}) supplies only three.  Thus (X) meets
(C\cup A).  Smaller internal boundaries give the same conclusion a
fortiori.  \(□\)

Consequently the surviving web is not arbitrary: it is
**portal-saturated**.  Every nontrivial triangle-separated cell away
from the protected root path carries a (D)-, (J)-, or (S)-portal.
This is the precise point at which a portal-order or minor-transition
argument must enter; an underloaded cell would expose a separator of
order at most six immediately.

Combining the preceding results completely disposes of the proposed
four-web branch.

### Corollary 4.3 (no portal-saturated web survives)

In a minor-free terminal state, (P_S=\varnothing).  In particular no
portal-saturated web with nonempty (S)-side occurs.

#### Proof

This is Theorem 2.3.  Alternatively, before invoking that theorem, a
crossing in any (H_R) gives (K_7) by Theorem 4.1, while a crossless
instance gives the ordered web and Lemma 4.2 portal-loads its cells.
Lemma 2.2 and the separator (2.13) then exclude that web globally.
\(□\)

This tests the limit of saturation: saturation by itself does not
force a crossing.  A four-web may have a facial clique attached through
a triangle and carrying only portal classes on one side of the cyclic
order; it remains a web and hence crossless.  What kills the branch here
is the extra labelled carrier geometry: after the two direct-cross
closures, the union (Z\cup J) exposes the six-cut (2.13).  No
minor-critical colouring transition is needed for this elimination.

## 5. Static data do not force the swap

The obstruction (3.2) is real if one retains only the spanning model,
portal counts, and bottleneck order.  Contract (Z,D,J,S,R_5,R_0) to
their essential pieces, keep two distinct (Z)-to-(J) portal vertices
(p_1,p_2), and arrange the ordinary carrier as

\[
                    J-p_1,quad J-p_2,quad J-s-S,           \tag{5.1}
\]

with (Zp_1,Zp_2).  Give (D) both right contacts, give (S) both
right contacts, and retain every pure-Moser and rooted-model edge.
Then (s) separates the root-bearing lobe
(J\cup\{p_1,p_2\}) from both right target classes, and the two active
portals are distinct.  The set (Z) is a singleton, so (3.1) fails.

Nevertheless this graph has treewidth at most five.  One width-five
elimination order is

\[
 p_1,p_2,s,S,3,4,Z,1,2,D,J,R_0,R_5,h,v.         \tag{5.2}
\]

`degree9_terminal_root_swap_counterarchitecture_verify.py` checks the
terminal-lobe conditions, all six old model adjacencies, the two distinct
active portals, and the width-five certificate.  Hence neither
seven-connectivity nor contraction-critical transition data may be
discarded in an attempt to prove (3.1).

For diagnostic purposes, there is also a fourteen-vertex graph satisfying
all of the following:

* it is exactly seven-connected;
* (N[v]) is the pure Moser spindle and (d(h)=9);
* the four rooted bags and all six old model adjacencies are present;
* the terminal lobe has the exact boundary count
  (N(Z)=\{h,1,2,6,J,p_1,s\}); and
* (Z) is a singleton, so the two-root split is impossible.

`degree9_terminal_root_swap_7connected_verify.py` exhaustively checks
all vertex deletions of order at most six and the displayed local data.
The graph does contain a (K_7)-minor.  In fact it has (Z\sim S),
(J\sim D), and a cross-literal (J)-(3) contact, so Lemma 2.2
explains it immediately.  It is therefore only a diagnostic that the
raw split need not exist; it is **not** a survivor after the direct-cross
closures (2.9) are imposed.

Fourteen is the smallest order compatible with these raw contracted roles:
the eight vertices of (N[v]), four distinct exterior roots, the
bottleneck (s), and one further portal are all forced.  The last portal
is needed because an inactive carrier with only the fixed (6)-contact
forces three active portals by (5.4c).  A genuinely relevant
connectivity test must also enforce (2.9), the non-flexibility of all
four roots, and the cyclic web order.  The fourteen-vertex graph does
not do so.

## 6. Remaining task

The alternating exchange has therefore reduced the same-bag degree-nine
lock to the fully nested double-root shore

\[
                             U=Z\cup J,                      \tag{6.1}
\]

with boundary (2.16), capacity (2.17), and no (Z)-(S) contact.  The
two-Steiner condition (3.1) is no longer the live question because its
(P_S)-class is empty.

The next exact exchange target is the following **nested two-root
splitter**.  Put

\[
       P_s=N_J(s),\qquad P_D=N_U(D).                         \tag{6.2}
\]

Prove that either (G) already has a (K_7)-minor, or (U) has a
connected bipartition

\[
                         U=E\mathbin{\dot\cup}T              \tag{6.3}
\]

such that

\[
 e_6\in E,quad e_0\in T,qquad
 E\cap P_s,E\cap P_D,T\cap P_s,T\cap P_D\ne\varnothing.    \tag{6.4}
\]

Indeed, (6.3)--(6.4) immediately gives the seven branch sets

\[
 \{h\},\{1\},\{2\},E,T,
 D\cup R_5,\ \{v,3\}\cup S\cup R_0.                       \tag{6.5}
\]

The last four form a clique through (ET,ED,Es,TD,Ts,v6), and
the two protected roots supply their (h,1,2)-contacts.  Thus failure
of (6.3)--(6.4), not a four-web in (Z), is the exact remaining
routing obstruction.

A useful closure theorem would therefore say:

> a seven-connected contraction-critical nested double-root shore with
> (|P_D|+|C_{34}|\ge3) either has the split (6.3)--(6.4), uses a
> cross-literal exit to build (K_7), or exposes an adhesion of order at
> most six.

This target preserves both roots and all carrier labels, and applies to
bags of arbitrary order.  It is the well-founded continuation of the
capacity exchange: a successful peel moves a proper root-free piece of
(J) into (Z), while a failed peel must account for all three exits in
(2.17).
