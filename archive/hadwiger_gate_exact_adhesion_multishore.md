# The antipodal gate exact adhesion has exactly two shores

## 1. A label-free neighbour-allocation lemma

### Lemma 1.1 (full components consume distinct outside neighbours)

Let (G) be (k)-connected, let (S) be a (k)-cut, and let
(z\in S).  Every component of (G-S) contains a neighbour of (z).
Consequently, if distinct components (D_1,\ldots,D_r) satisfy

\[
                     N_G(z)-S\subseteq D_1\cup\cdots\cup D_r,       \tag{1.1}
\]

then (D_1,\ldots,D_r) are all the components of (G-S).

More generally,

\[
                 c(G-S)\le |N_G(z)-S|.                              \tag{1.2}
\]

#### Proof

Let (C) be a component of (G-S).  If (z) had no neighbour in
(C), then

\[
                         N_G(C)\subseteq S-\{z\}.
\]

The set on the right has order (k-1), and it separates the nonempty
set (C) from any other component of (G-S), contrary to
(k)-connectivity.  Thus (N_C(z)\ne\varnothing).

Different components are disjoint, so choosing one (z)-neighbour in
each gives the injection behind (1.2).  Under (1.1), any additional
component would need a (z)-neighbour outside the displayed union, which
does not exist.  \(\square\)

The conclusion uses actual neighbour placement, not merely the induced
graph (G[S]).  It is therefore stronger than a boundary-state count in
the situation below.

## 2. The exact antipodal gate

Use the audited notation from
`hadwiger_palette_deletion_rooted_core.md` and
`hadwiger_bichromatic_gate_peel_or_adhesion.md`.  Thus:

* (G) is seven-connected;
* (v) has degree seven and
  (N_G(v)=\{0,1,2,3,4,5,6\});
* (X=\{1,2,3,4\});
* (K_0) is the gate component containing (0);
* (K_{56}) is the other gate component and contains (5,6); and
* a two-separator (\{p,q\}) in (H-X), where (H=G-v), separates
  (K_0) from (K_{56}).

Put

\[
                         L=\{v\}\cup X\cup\{p,q\}.                  \tag{2.1}
\]

The Menger construction gives

\[
 p,q\notin K_0\cup K_{56}\cup X.
\]

All seven neighbours of (v) have already been accounted for by
(X\cup\{0,5,6\}).  Hence

\[
 vp,vq\notin E(G),\qquad
 N_G(v)\cap L=X,qquad
 N_G(v)-L=\{0,5,6\}.                              \tag{2.2}
\]

No assertion about (pq) is made or needed: it may be an edge or a
nonedge.  Likewise the arbitrary (pX)- and (qX)-edges play no role.

The set (L) separates (K_0) from (K_{56}) in (G).  Indeed,
(X\cup\{p,q\}) separates them in (H), and the only new vertex when
passing from (H) to (G) is (v\in L).  Its order is seven, so
seven-connectivity makes (L) an exact seven-cut.

Let (D_0,D_{56}) be the components of (G-L) containing (K_0) and
(K_{56}), respectively.  They are distinct.  Moreover,

\[
                         0\in D_0,qquad \{5,6\}\subseteq D_{56}.   \tag{2.3}
\]

### Theorem 2.1 (no multishore antipodal gate)

In the preceding setting,

\[
                              G-L=D_0\mathbin{\dot\cup}D_{56};      \tag{2.4}
\]

in particular (G-L) has exactly two components.  Therefore the exact
adhesion branch created by the antipodal gate can never enter a
three-or-more-shore state.

#### Proof

Equations (2.2)--(2.3) give

\[
 N_G(v)-L=\{0,5,6\}\subseteq D_0\cup D_{56}.
\]

Apply Lemma 1.1 to the seven-cut (L), with (z=v).  Every component
of (G-L) must contain a neighbour of (v), while the two displayed
components already contain all three such neighbours.  Hence there is
no third component.  Since (L) separates the two gate sets, both
displayed components exist and are distinct, proving (2.4).  \(\square\)

## 3. Why no boundary-state cube is required

The general exact-cut results still provide useful checks:

1. Seven-connectivity makes every component behind (L) full to all
   seven boundary vertices.
2. Four or more full shores would already be excluded by the elementary
   minor packings and full-shore block gluing in
   `hadwiger_exact7_multicomponent_closure.md`.
3. For an arbitrary three-shore seven-cut, those theorems leave a real
   residue: the three-colour ((3,2,2)) state is eliminated, but the
   four-chromatic pure-Moser boundary requires additional portal/state
   information.

The gate adhesion has precisely the extra information missing from an
arbitrary cut: the two prescribed sides cover every neighbour of the
degree-seven boundary vertex (v) outside (L).  Theorem 2.1 therefore
closes the multishore branch before any colour gluing is attempted.

In particular, it would be incorrect and unnecessary to assume that the
equality blocks of a six-colouring form a clique.  The boundary graph on
(L) is only partially fixed:

* (v) is adjacent to all four vertices of (X);
* (X) contains the two matching edges (12,34);
* (vp,vq) are nonedges;
* (pq), the (pX)-edges, and the (qX)-edges are unrestricted.

These unknown edges can obstruct a proposed contraction-and-gluing
argument.  They do not affect the neighbour-allocation proof.

## 4. Exact scope and remaining branch

Theorem 2.1 is label-free in its operative form: a (k)-cut cannot have
an additional component once specified components already cover all
outside neighbours of one boundary vertex.  The antipodal labels merely
verify that cover through (0\mid56).

Thus there is no missing transfer condition for the
three-or-more-component gate state: that state is empty.  The surviving
exact-adhesion problem is necessarily the two-shore problem

\[
                         D_0\mid L\mid D_{56},
\]

where the cyclic-hull, relative-capacity, or minor-transition machinery
must still repair the deficient gate adjacency.  Nothing proved here
closes that two-shore exchange.

