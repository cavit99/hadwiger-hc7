# Exact interface exchange at a covering bad split

## 1. Setting

Let (G) be (r)-minor-critical: (G) is not (r)-colourable and
every proper minor is (r)-colourable.  Let (S) be the boundary of a
side (D), so

\[
 N_G(D)\subseteq D\cup S.
\]

Suppose

\[
 D=X\mathbin{\dot\cup}Y
\]

is a partition into nonempty connected sets.  This includes the
connected full splits obtained by extending the two carriers of a web
crossing.  Write

\[
 \partial(X,Y)=E_G(X,Y).
\]

For a colouring (c) and colours \(\alpha,\gamma\), a component of
the \(\alpha/\gamma\)-subgraph of (G[D]) is **boundary-anchored** if
it has a neighbour in (S) whose colour is \(\alpha\) or \(\gamma\).

## 2. The interface exchange lemma

### Theorem 2.1 (internal ear or two boundary anchors)

Fix an edge (e=xy\in\partial(X,Y)), with (x\in X) and (y\in Y),
and let (c) be any (r)-colouring of (G-e).  Put
\(\alpha=c(x)=c(y)\).  For every colour \(\gamma\ne\alpha\), precisely
one of the following two alternatives is forced:

1. the \(\alpha/\gamma\)-subgraph of (G[D]-e) contains an
   (x)-(y) path; or
2. the components of that subgraph containing (x) and (y) are
   distinct and each is boundary-anchored.

Consequently, if (q) colours satisfy alternative 1, then

\[
 |\partial(X,Y)|\ge q+1.                         \tag{2.1}
\]

Equivalently, at least

\[
 r-|\partial(X,Y)|                              \tag{2.2}
\]

of the colours different from \(\alpha\) satisfy the two-anchor
alternative (when the right side is positive).

#### Proof

Restoring (e) would colour (G) unless (c(x)=c(y)), proving the
definition of \(\alpha\).

Fix \(\gamma\ne\alpha\), and let (K_x,K_y) be the components
containing (x,y), respectively, in the \(\alpha/\gamma\)-subgraph of
(G[D]-e).  If they coincide, alternative 1 holds.  Suppose they are
distinct.  If, say, (K_x) were not boundary-anchored, interchange
\(\alpha\) and \(\gamma\) on (K_x), leaving (S) and the rest of
the graph fixed.  No edge internal to (D) becomes monochromatic,
because (K_x) is an entire bichromatic component.  No edge from
(K_x) to (S) becomes monochromatic: a boundary neighbour with a
colour outside \(\{\alpha,\gamma\}\) is unaffected, while by
assumption there is no boundary neighbour using either colour.
The switch gives (x) colour \(\gamma\), leaves (y) colour
\(\alpha\), and therefore permits restoration of (e).  This is an
(r)-colouring of (G), a contradiction.  Thus (K_x) is anchored;
the symmetric switch at (K_y) proves that (K_y) is anchored too.

For every colour satisfying alternative 1, choose an (x)-(y) path
inside (D-e) and one edge on that path crossing from (X) to (Y).
It is different from (e), and its endpoint colours are
\(\alpha,\gamma\).  Edges chosen for distinct values of \(\gamma\)
are distinct.  This proves (2.1), and (2.2) follows because there are
(r-1) colours other than \(\alpha\).  \(\square\)

## 3. Exact state carried by the exchange

Let (D') denote the unchanged complement of the open side (D), and
let \(\Pi_e\) be the equality partition induced by (c) on (S).
Then

\[
 \Pi_e\in \mathcal E_r(D-e,S)\cap\mathcal E_r(D',S),
 \qquad
 \Pi_e\notin\mathcal E_r(D,S).                    \tag{3.1}
\]

The first two memberships are restrictions of (c).  If the last one
failed, an extension over the original (D) could be aligned label by
label with (c) on the complement and would colour (G).

Thus Theorem 2.1 decorates every edge-deletion transition with concrete
geometry: for each other colour it supplies either an internal
bichromatic ear across the split or boundary anchors on both sides.

### Corollary 3.1 (geometry-preserving deletion)

Suppose the split (X\mid Y) extends two disjoint crossing carriers,
one contained in each side.  If

\[
 |\partial(X,Y)|\ge2,
\]

then deletion of any one interface edge preserves all of the following:

* both connected crossing carriers;
* the two contact rows (N_S(X),N_S(Y));
* the covering property (N_S(X)\cup N_S(Y)=S); and
* adjacency of the two pieces.

It nevertheless creates the strict state (3.1).  Hence a covering bad
split with at least two interface edges is not structurally edge-minimal;
it is **state-critical inside a fixed split geometry**.

#### Proof

The deleted edge has one end in each side, so it changes neither induced
side nor either carrier or contact row.  A second interface edge retains
adjacency.  Equation (3.1) is the minor-critical transition. \(\square\)

## 4. Relation with tight cuts

Put

\[
 P_X=N_S(X),\qquad T_X=N_Y(X).
\]

Ambient (k)-connectivity gives

\[
 |P_X|+|T_X|\ge k.                                \tag{4.1}
\]

Equality exposes the nested minimum cut (P_X\cup T_X).  If equality
does not hold, Theorem 2.1 identifies the exact missing exchange:
internal ears retain the crossing geometry, while every colour without
such an ear is pinned to (S) on both sides.  A complete
ear-peel-or-tight-cut theorem must therefore prove that the simultaneous
two-sided boundary anchoring can be rerouted through a positive boundary
state or forces equality in (4.1).

This last inference is not a consequence of minor-criticality alone.
For example, an odd cycle with empty boundary is edge-critical for two
colouring, and the same boundary state is created by deleting many
different edges.  Thus pigeonholing the finite state set across distinct
edge deletions does not reconstruct a colouring of the original graph.
The clique-minor exclusion and the actual portal rows of the covering bad
split must enter the final exchange.
