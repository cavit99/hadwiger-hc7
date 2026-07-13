# Induced-core crossing at every minimum full-shore adhesion

## 1. Statement

Let (G) be a (k)-connected graph which is not (r)-colourable.  Let (S)
be a (k)-vertex cut such that (G-S) has exactly
two nonempty connected components (D_1,D_2), and suppose both are full:

\[
 N_G(D_1)=N_G(D_2)=S.                              \tag{1.1}
\]

Put (J=G[S]) and (Q=\overline J).  For a cyclically ordered
(C\subseteq S), form the usual terminal society on either shore by giving
each (c\in C) an artificial terminal adjacent to its full portal set in
that shore.

### Theorem 1.1 (minimum-adhesion core crossing)

If (Q) is nonsplit, then (Q) has an induced subgraph

\[
 F\in\{2K_2,C_4,C_5\}                              \tag{1.2}
\]

on a set (C).  For every such induced core satisfying

\[
 \chi(G[S-C])\le r-4,                              \tag{1.3}
\]

(with the cyclic order specified below), the terminal tuple is crossed in
at least one of the two shores.  In particular, if (k\le r), condition
(1.3) holds for every induced core in (1.2).

The orders are chosen so that (J[C]) is a subgraph of the frame cycle:

* if (F=2K_2), then (J[C]=C_4);
* if (F=C_4), then (J[C]=2K_2), placed as two opposite frame edges of
  a four-cycle; and
* if (F=C_5), then (J[C]=C_5), in its complementary cyclic order.

### Proof

The Földes--Hammer characterization of split graphs says that a graph is
split exactly when it has no induced (2K_2,C_4,C_5).  Hence (1.2)
exists.  The three displayed descriptions of (J[C]=\overline{F}) are
immediate (the complement of a five-cycle is another five-cycle).

Put (Z=S-C).  Suppose both shore tuples are crossless.  Apply the
terminal-specific two-shore web theorem with common side-exposure set
(Z_1=Z_2=Z).  Its connectivity inequality holds automatically.  If
(|C|=4), then

\[
 3+|Z|=3+(k-4)=k-1<k=\kappa(G),
\]

while for (|C|=5),

\[
 3+|Z|=k-2<k.
\]

The crossless conclusion therefore makes (G-Z) planar and gives

\[
 \chi(G)\le4+\chi(G[Z])\le r,
\]

contrary to the hypothesis.  If (k\le r), then a four-vertex core has
(|Z|=k-4\le r-4), while a five-vertex core has an even smaller omitted
set.  Hence (1.3) is automatic in that range.  The argument applies
independently to every eligible induced core.  \(□\)

## 2. Counterexample-derived corollary

In an (r)-minor-critical graph, the exact-block hypergraph theorem makes
the missing graph (Q=\overline{G[S]}) nonsplit at every two-full-shore
adhesion in its range.  Whenever an induced obstruction core satisfies
(1.3), Theorem 1.1 supplies two disjoint connected carriers for an
alternating pair of core demands in one shore.  This is automatic when
(k\le r).  At the sharp HC7 cut (k=7,r=6), it applies to every five-core
and to a four-core whose omitted triple is bipartite in (G[S]).

After a shortest connector is split at an edge, the crossed shore has a
connected bipartition (X\dot\cup Y) with (XY\in E) and prescribed
contacts to four boundary labels.  Consequently the exact remaining test
at a minimum adhesion is no longer

\[
 \text{``does any routing exist?''}
\]

but

\[
 \text{``is the crossed contact pair positive in the boundary's
 bad-split relation?''}                             \tag{2.1}
\]

If it is positive, contracting (X,Y) and the opposite full shore gives
the target clique minor.  If it is negative, (2.1) is a balanced bad-split
transition to which the defect-atlas connectivity, star, and uncrossing
machinery applies.

## 3. Significance and exact limit

The theorem is uniform in (k,r) and uses only a constant-size induced
core.  It closes the routing half of the desired contact-or-separator
dichotomy at every minimum full-shore cut: a colour-gluable planar web is
the only alternative to a crossed portal split, and minor-critical
noncolourability excludes that alternative.

It does not assert that the crossed split itself has a positive clique
quotient.  The reserved Moser audit shows this limitation is real: all ten
conservative crossed-frame quotients have Hadwiger number six.  Portal
placement, a further split, or the exact one-step colouring transition is
still needed to turn a negative crossed pair into a positive model.
