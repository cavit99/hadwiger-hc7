# Terminal-specific two-shore web gluing

## 1. Local-exposure theorem

Let a graph (G) have a vertex partition

\[
 V(G)=C\mathbin{\dot\cup}Z\mathbin{\dot\cup}D_1
       \mathbin{\dot\cup}D_2,
 \tag{1.1}
\]

where (D_1,D_2) are nonempty, connected and anticomplete. Give

\[
 C=(c_0,c_1,\ldots,c_{m-1}),\qquad m\ge4,
 \tag{1.2}
\]

a cyclic order and assume

\[
 E(G[C])\subseteq\{c_ic_{i+1}:i\in\mathbb Z_m\}.
 \tag{1.3}
\]

For each side (j\in\{1,2\}), let (Z_j\subseteq Z) satisfy

\[
 N_G(D_j)\subseteq D_j\cup C\cup Z_j,
 \tag{1.4}
\]

and assume every (c_i) has a neighbour in (D_j). Form (A_j) from
(G[D_j]) by adjoining independent terminals (t_i), with

\[
 N_{A_j}(t_i)=N_{D_j}(c_i),
 \tag{1.5}
\]

ordered as in (1.2).

### Theorem 1.1 (local-exposure web dichotomy)

If

\[
 \kappa(G)>3+\max\{|Z_1|,|Z_2|\},
 \tag{1.6}
\]

then either the terminal tuple is crossed in at least one of
(A_1,A_2), or (G-Z) is planar. Consequently,

\[
 \text{either a shore tuple is crossed, or }
 \chi(G)\le4+\chi(G[Z]).
 \tag{1.7}
\]

### Proof

Suppose both tuples are crossless. The generalized Two Paths Theorem
gives an edge-only completion of each (A_j), on the same vertex set,
to an (m)-web with the displayed frame.

If a nonempty set (X\subseteq D_j) is an inserted clique behind a rib
triangle (F), replace every artificial terminal of (F) by its label
in (C), and retain every shore vertex of (F). Call the resulting set
(\widehat F). It has order at most three and accounts for all neighbours
of (X) in (D_j\cup C). By (1.4),

\[
 N_G(X)\subseteq\widehat F\cup Z_j,
 \qquad |N_G(X)|\le3+|Z_j|<\kappa(G).
 \tag{1.8}
\]

This set separates (X) from the nonempty opposite shore, a
contradiction. Hence every actual shore vertex and edge belongs to the
planar rib.

Replace the terminals by their labels and draw the actual edges of
(G[C]) on the outer frame. Condition (1.3) is exactly what makes this
legal; absent frame edges are simply deleted. Thus each
(G[D_j\cup C]) has a disk embedding with the same labelled boundary.
Reflect one disk and glue them along (C). Anticompleteness of the shores
gives a plane embedding of (G-Z). Four-colour that graph and colour
(G[Z]) from a disjoint palette. This proves (1.7). \(\square\)

## 2. Terminal-aware crossing quotients

The minor half also has a local-exposure version. In addition to (1.4),
fix sets (B_j\subseteq C\cup Z_j) such that every label of (B_j)
has a neighbour in (D_j). Usually (C\subseteq B_j).

For a crossing on side (j), with alternating terminal pairs
((c_i,c_k)) and ((c_r,c_s)), define
(\Gamma_j(i,r,k,s)) by starting with (G[C\cup Z]) and adjoining
three vertices (x,y,h) such that

\[
 xy\in E,quad
 N(x)=\{y,c_i,c_k\},quad
 N(y)=\{x,c_r,c_s\},quad
 N(h)=B_{3-j}.
 \tag{2.1}
\]

Only the displayed new incidences are required; extra boundary edges are
those already in (G[C\cup Z]).

### Corollary 2.1 (terminal-aware finite certificate)

If every side and every alternating crossing satisfies

\[
 \eta(\Gamma_j(i,r,k,s))\ge t,
 \tag{2.2}
\]

then

\[
 G\text{ has a }K_t\text{ minor}
 \quad\text{or}\quad
 \chi(G)\le4+\chi(G[Z]).
 \tag{2.3}
\]

### Proof

Delete the artificial ends of a crossing. The two path interiors are
disjoint connected sets. If they are not adjacent, join them by a shortest
path in the connected shore and split the connector at an edge, obtaining
adjacent disjoint connected sets (X,Y) with the four prescribed portal
contacts. Contract (X,Y), delete the unused part of their shore, and
contract the opposite shore to (h). Every edge in (2.1) is present, so
(\Gamma_j) is a subgraph of a minor of (G). Thus (2.2) lifts. If no
tuple is crossed, Theorem 1.1 gives the colour alternative. \(\square\)

## 3. Strict strengthening of the previous theorem

Theorem 1.1 of `hadwiger_two_shore_web_gluing.md` is the special case

\[
 Z_1=Z_2=Z,qquad N(D_1)=N(D_2)=C\cup Z.
\]

Its connectivity condition is

\[
 \kappa(G)\ge |Z|+4.
\]

The present theorem only charges labels which can actually see the
particular inserted web piece. It permits different side-specific
exposure sets and requires

\[
 \kappa(G)\ge4+\max_j|Z_j|.
\]

This is a material improvement when the global palette set is larger than
either shore's local exposure.

## 4. Exact reserved-connector application

In the pure-Moser reserved connector take

\[
 C=U,\qquad Z=\{a,b,w,v\},
\]

where (C) is ordered as the present 5-cycle, and put

\[
 Z_a=\{a,w\},\qquad Z_b=\{b,w\}.
 \tag{4.1}
\]

The relative-shore theorem gives (1.4), with both shores full to (C).
Moreover

\[
 \chi(G[Z])\le2,
 \tag{4.2}
\]

because ({a,b\}) and ({v,w\}) are independent: (ab) is the
repeated nonedge and (w\notin N(v)). Seven-connectivity gives

\[
 7>3+2.
\]

The old common-boundary theorem does not apply: the shores are not both
full to the four-set (Z), and it would demand connectivity at least
eight. Theorem 1.1 does apply and says:

> either some Moser frame is crossed in a shore, or (G) is
> six-colourable.

Equivalently, the bilateral all-crossless cell is closed.

For the terminal-aware quotient take

\[
 B_a=C\cup\{a,w\},\qquad B_b=C\cup\{b,w\}.
 \tag{4.3}
\]

Here the label-free method reaches its exact limit. The dependency-free
program `reserved_terminal_specific_web_quotient_verify.py` checks all
five crossings on both sides. Every one of the ten conservative quotients
has

\[
 \eta(\Gamma_j)=6,
 \tag{4.4}
\]

not seven. Thus a crossing by itself does not yield (K_7) through the
finite quotient. The remaining information must come from the placement
of the crossing paths inside their shore: a contact with (w) or the
terminal, a split producing an additional adjacent bag, or a decorated
boundary-state transition. This is precisely the portal-distribution
information erased when a crossing is contracted to the two vertices
(x,y).

Hence the label-free theorem genuinely advances the reserved connector
(it forces a crossed frame at connectivity seven), but it cannot close
the one-crossed-side cell without a new portal-aware certificate.
