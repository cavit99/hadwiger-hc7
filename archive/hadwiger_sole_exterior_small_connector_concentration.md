# Small reserved connectors concentrate all surviving Moser supports

## 1. Setting

Let (G) be a hypothetical seven-connected counterexample-derived graph,
let (v) have degree seven, and suppose that

\[
 N_G(v)=I\mathbin{\dot\cup}U,
 \qquad I=\{a,b\},\quad |U|=5,
\]

where (I) is independent, (G[U]\cong C_5), and
(C=G-N[v]) is the sole exterior component.  The cut (N_G(v)) has
exactly the two full shores (C) and the singleton ({v}).

Write (F\cong C_5) for the missing-edge cycle on (U).  Its five
two-edge matchings are precisely the five perfect nonedge matchings

\[
                         I\mid J\mid K\mid\{r\}
\tag{1.1}
\]

of the pure Moser boundary, with (J,K\in E(F)) vertex-disjoint.

An **(I)-connector** is a connected set (X\subseteq C) which has
a neighbour at both (a,b).  For (e=xy\in E(F)), say that (e)
survives outside (X) if some component of (C-X) contains a connected
set meeting both portal rows (N_C(x),N_C(y)).

## 2. Protected-support concentration

### Theorem 2.1

Let (X\subsetneq C) be an (I)-connector of order at most two.  Then
one of the following holds.

1. (G) has a nested exact seven-cut.
2. At least three of the five edges of (F) survive outside (X), and
   the nonsurviving edges form either the empty set, one edge, or two
   incident edges of (F).

Thus, after the already proved elimination of nested three-shore Moser
cuts, every such connector either exports the desired exact two-shore
adhesion or destroys at most two adjacent Kempe supports.

### Proof

Fix a frame ({J,K}), that is, two vertex-disjoint edges of (F).
Apply Theorem 0.1 of `hadwiger_small_carrier_packet_or_cut.md` to the
three disjoint pair blocks (I,J,K), the exact cut (N_G(v)), the
shore (C), and the (I)-carrier (X).  If it exports an exact
seven-cut, outcome 1 holds.  Otherwise (X) is disjoint from a carrier
for (J) or from a carrier for (K), lying in one component of
(C-X).  In other words, at least one edge of every frame survives.

Let (R\subseteq E(F)) be the surviving edge set.  The graph whose
vertices are the five edges of (F), with adjacency meaning
vertex-disjointness in (F), is again a five-cycle.  The preceding
paragraph says that the complement (E(F)-R) is an independent set in
this disjointness cycle.  It consequently has order at most two.  If it
has order two, its two members are not vertex-disjoint in the original
cycle (F), and hence are incident.  This is outcome 2.  \(\square\)

## 3. Exact limit of the lemma

The theorem is stronger than merely finding one crossed frame: a small
reserved connector leaves a protected support set meeting every frame.
It still does not by itself give the nonseparating rooted (K_5).
Kriesell--Mohr packaging needs all five missing-cycle adjacencies.  If
one or two incident supports fail, absorbing the connector into the
shared deficient root can repair those adjacencies, but consumes the
sixth branch set.  Recovering that lost branch set, or proving that one
of the failed supports can be rerouted, is the remaining exchange step.

The result therefore isolates the first genuinely unbounded protected
case: every surviving (a)-(b) connector has at least three exterior
vertices, or the only obstruction is one/two adjacent support failures
behind a nested exact two-shore cut.

