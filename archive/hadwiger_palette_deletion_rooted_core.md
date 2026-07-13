# Palette deletion produces rooted four-colour cores

## 1. A boundary-saturation theorem

Let (H) be a graph, let (S\subseteq V(H)), and let

\[
        c:V(H)\longrightarrow [k]
\]

be a proper (k)-colouring.  Say that (S) is **(k)-saturating**
when every proper (k)-colouring of (H) uses all (k) colours on
(S).  Empty colour classes are allowed in the phrase “(k)-colouring”,
so saturation says equivalently that no colouring with palette ([k])
uses at most (k-1) colours on (S).

### Theorem 1.1 (palette-deletion rooted core)

Assume (k\ge4), (S) is (k)-saturating, and choose any four colour
classes of (c).  Let (J) be the subgraph induced by their union and
put (X=S\cap V(J)).  Then every proper four-colouring of (J) uses all
four colours on (X).

Consequently, by the proved four-colour case of Holroyd's Strong
Hadwiger Conjecture, (J) contains an (X)-rooted (K_4)-minor.

#### Proof

The restriction of (c) makes (J) four-colourable.  Suppose that a
proper four-colouring (\varphi) of (J) used at most three colours on
(X).  Give each of the other (k-4) original colour classes of (c)
one distinct fresh colour.  Each such class is independent, different
deleted classes receive different colours, and their fresh palette is
disjoint from the palette of (\varphi).  Hence this extends (\varphi)
to a proper (k)-colouring of (H).

On (S), this extension uses at most

\[
                  3+(k-4)=k-1
\]

colours, contrary to saturation.  Thus (X) is four-colour-saturating
in (J).  The Strong-(HC_4) theorem gives the asserted rooted minor.
(\square)

The theorem is independent of the Moser spindle and of minor-criticality.
Its input is exactly the colour-saturation forced at the neighbourhood of
an uncoloured apex.

## 2. Counterexample specialization

Let (G) be a non-six-colourable graph, let (v\in V(G)), put
(H=G-v) and (S=N_G(v)), and suppose (H) has a proper six-colouring.
Then (S) is six-saturating in (H): if one of the six colours were
absent from (S), it could be assigned to (v).

### Corollary 2.1

For every proper six-colouring of (H), the union of any four colour
classes contains an (X)-rooted (K_4)-minor, where (X) is the set of
vertices of (S) in those four classes.

In particular, suppose the trace on (S) consists of one two-vertex
class (I) and five singleton classes.  Delete the colour class of
(I) and the class of any singleton (r\in S-I).  The remaining four
boundary vertices

\[
                         X=S-(I\cup\{r\})
\]

are the four roots of a rooted (K_4)-model lying entirely outside the
two deleted colour classes.  Since there are exactly four roots and four
disjoint rooted bags, every bag contains exactly one member of (X).

### Lemma 2.2 (unique-root colour fans)

Let (x\in S) be the unique vertex of (S) having colour (c(x)).  Then
(x) has a neighbour in every other colour class of (c).

#### Proof

If (x) had no neighbour of another colour (\gamma), recolouring (x)
with (\gamma) would remain proper.  The old colour (c(x)) would then be
absent from (S), contrary to saturation. \(\square\)

Thus, in an exact (2+1+1+1+1+1) trace, each singleton root has a direct
neighbour in every other colour class.  This is stronger than pairwise
Kempe connectivity at the roots and supplies a canonical five-colour fan
at every singleton root.

## 3. The antipodal Moser gate

Now assume that (G) is a **minor-minimal** (K_7)-minor-free
non-six-colourable graph, that (d_G(v)=7), and that (G[S]) is the pure
Moser spindle with

\[
 E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

The required exact trace exists, rather than being an additional
assumption.  Contract the connected star on (\{v,0,5\}) to one vertex
(z).  This is a proper minor; moreover, (05) is a nonedge.  By
minor-minimality the resulting graph is six-colourable.  Expanding the
colouring to (H=G-v), giving both (0) and (5) the colour of (z), gives
a proper six-colouring (c).  Every vertex of (S-\{0,5\}) is adjacent
to (z) in the contracted graph through its original edge to (v), so no
other boundary vertex has that colour.  The saturation observation in
Section 2 forces all six colours to occur on (S); hence the other five
boundary vertices have the five remaining colours, one each.  Thus (c)
has exact repeated pair (05).  Write

\[
 A=c^{-1}(c(0))=c^{-1}(c(5)),\qquad
 B=c^{-1}(c(6)),\qquad
 J=H-(A\cup B).
\]

Thus the four boundary vertices in (J) are

\[
                         X=\{1,2,3,4\}.
\]

Let (K_0) be the component of (H[A\cup B]) containing (0), and
let (K_{56}) be the component containing the boundary edge (56).

### Theorem 3.1 (rooted-core gate dichotomy)

The graph (J) contains an (X)-rooted (K_4)-model.  Moreover, either

1. (G) contains a (K_7)-minor; or
2. (K_0) and (K_{56}) are distinct, anticomplete components of
   (H[A\cup B]).

In outcome 2, switching the two colours on (K_0) turns the same
colouring into an exact-trace colouring whose repeated boundary pair is
(06) and whose singleton of the other gate colour is (5).  The
four-colour core (J) and its rooted (K_4) are unchanged.

#### Proof

Corollary 2.1 gives an (X)-rooted (K_4)-model

\[
                         R_1,R_2,R_3,R_4
\]

in (J), indexed so that (i\in R_i).  Suppose first that
(K_0=K_{56}).  Let (Q=x_0x_1\ldots x_\ell) be a shortest path in
this component from (x_0=0) to the set (\{5,6\}).  No internal vertex
of (Q) lies in (\{5,6\}).  Put

\[
 P_0=\{x_0,\ldots,x_{\ell-1}\},\qquad P_{56}=\{5,6\}.
\]

The edge (x_{\ell-1}x_\ell) and the boundary edge (56) show that
these are disjoint, adjacent connected sets in (A\cup B) such that

\[
                         0\in P_0,qquad
                         \{5,6\}\subseteq P_{56}.
\]

The vertex (0) is adjacent in the Moser spindle to every member of
(X).  The pair ({5,6}) collectively dominates (X): vertex (5)
sees (3,4), while vertex (6) sees (1,2).  Hence each of
(P_0,P_{56}) is adjacent to every rooted bag (R_i).  The six sets

\[
                  P_0, P_{56}, R_1,R_2,R_3,R_4
\]

are pairwise adjacent connected branch sets in (H).  Each contains a
vertex of (S), so the singleton branch set ({v}) is adjacent to all
six.  They form a (K_7)-model in (G).

Therefore (K_7)-minor-freeness forces (K_0\ne K_{56}).  Distinct
components of the induced bichromatic graph are anticomplete.  Its only
boundary vertices are (0,5,6), so (K_0) contains (0) and neither
(5) nor (6).  Interchanging the two colours on (K_0) preserves
properness and changes the boundary classes from

\[
                         05\mid 6
             \quad\hbox{to}\quad
                         5\mid 06.
\]

All other four colour classes, and hence (J), are untouched.  This
proves the theorem. (\square)

### Corollary 3.2 (a canonical (K_7^-)-model)

In the (K_7)-minor-free outcome, contracting (K_0,K_{56}) and the
four rooted bags gives a (K_6^-)-model in (H), whose only deficient
pair is (K_0K_{56}).  Adding ({v}) gives a (K_7^-)-model.  The
deficient bags are not arbitrary: they are two components of one
bichromatic graph, the first contains a boundary vertex complete to
(X), the second contains the boundary edge (56) collectively complete
to (X), and the Kempe switch across the first exchanges the exact traces
(05) and (06) without altering the rooted four-colour core.

This replaces the five-root reserved-(K_5) synchronization problem, for
this antipodal trace pair, by a four-root problem with one exact
bichromatic gate.  The remaining operation is label-free: either find a
connector between the two gate components disjoint from a rooted
(K_4), or turn every failed connector into a colour-state adhesion.
