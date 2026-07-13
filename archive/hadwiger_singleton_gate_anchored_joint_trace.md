# The singleton dirty gate has a root-anchored critical (56)-trace

## 1. Setting

Let (G) be non-six-colourable and suppose that every proper minor of
(G) is six-colourable.  Let (v) have degree seven and let its
neighbourhood be the labelled pure Moser spindle

\[
 N(v)=\{h,1,2,3,4,5,6\},
\]

\[
 E(G[N(v)])=
 \{h1,h2,h3,h4,12,16,26,34,35,45,56\}.        \tag{1.1}
\]

The edge (56) is critical: in every six-colouring of (G-56), its
ends have one colour, and for every other colour the two ends lie in the
same bichromatic component.

Call a vertex (s\notin N[v]) a **left root** when

\[
                       s\sim h,1,2,                         \tag{1.2}
\]

and a **right root** when

\[
                       s\sim h,3,4.                         \tag{1.3}
\]

The four exterior neighbours of the degree-nine Moser hub have one of
these two types.  The result below does not require (d(h)=9), however.

## 2. A joint trace forced by a proper minor

### Lemma 2.1 (the (h56)-trace)

There is a proper six-colouring (c) of (G-56) such that

\[
                         c(h)=c(5)=c(6)=\alpha.             \tag{2.1}
\]

Moreover, for any preselected vertex (s\notin N[v]) with (s\sim h), the colouring may
be chosen so that, if (\sigma=c(s)) is absent from
\(c(\{1,2,3,4\})\), then

\[
                              c(v)=\sigma.                  \tag{2.2}
\]

#### Proof

Delete (56) and contract the connected star on

\[
                            \{v,h,5,6\}
\]

to one vertex (z).  This is a proper minor of (G), hence has a
proper six-colouring.  Delete (v) before expanding the contracted
star, and give (h,5,6) the colour of (z).  This is a proper colouring
of (G-v-56): the three expanded leaves are pairwise nonadjacent there,
and every outside neighbour of one of them was adjacent to (z) in the
minor.

At most five colours occur on (N(v)): the three vertices (h,5,6)
have one colour and the other four neighbours contribute at most four
more.  Hence (v) has an available colour.  If (c(s)) is absent from
(c(\{1,2,3,4\})), it is also different from (\alpha) whenever
(s\sim h), and it is absent from all of (N(v)); in that case choose
it for (v).  Otherwise choose any available colour.  This proves the
lemma. \(\square\)

The deletion of (56) is essential.  In the original graph the three
leaves (h,5,6) are not independent.

## 3. Alignment with an actual exterior root

### Theorem 3.1 (root-anchored split-cycle member)

Let (s) be either a left root or a right root.  There is a proper
six-colouring (c_s) of (G-56) with the following properties.  Put

\[
 \alpha=c_s(h)=c_s(5)=c_s(6),\qquad \sigma=c_s(s).
                                                               \tag{3.1}
\]

Then the (\{\alpha,\sigma\})-component containing (5) contains all
four vertices

\[
                             h,s,5,6.                         \tag{3.2}
\]

If (s) is a left root, this component avoids (1,2).  If (s) is a
right root, it avoids (3,4).

After identifying (5,6), the (5)-(6) part of this component is
the side-labelled fan member of the critical-edge split-cycle theorem:
it is either a common (\sigma)-coloured neighbour of (5,6), or an
(\alpha\sigma)-cycle through the contracted vertex with one (5)-side
and one (6)-side incidence.

#### Proof

Apply Lemma 2.1 with the preselected vertex (s).  First suppose (s)
is a left root.  Since (s\sim h,1,2), its colour (\sigma) differs
from (\alpha,c(1),c(2)).  If (\sigma) occurs on
\(\{1,2,3,4\}\), it therefore occurs at some

\[
                              x\in\{3,4\}.                  \tag{3.3}
\]

If it does not occur there, choose (c(v)=\sigma) as in Lemma 2.1 and
put (x=v).  In the first case

\[
                         s-h-x-5                             \tag{3.4}
\]

is an (\alpha\sigma)-path.  In the second case (h,v,5,6) lie in one
(\alpha\sigma)-component because (v) is adjacent to all three
(\alpha)-coloured vertices, and (s\sim h) adds (s).

In either case (h,s,5) lie in one (\alpha\sigma)-component.  The
critical-edge Kempe argument for (56) says that (5) and (6) lie in
the same (\alpha\sigma)-component: otherwise swapping that component
at (5) would give (5,6) different colours and hence a six-colouring
of (G).  This proves (3.2).  The component avoids (1,2), since those
vertices have neither colour (\alpha) nor (\sigma).

For a right root, (\sigma) differs from
(\alpha,c(3),c(4)).  If it occurs on the four remaining boundary
vertices, it occurs at (x\in\{1,2\}), and now

\[
                         s-h-x-6                             \tag{3.5}
\]

is the required bichromatic path.  If it is absent, again choose
(c(v)=\sigma).  Criticality joins the other endpoint exactly as above,
and the component avoids (3,4).

The last assertion is precisely the split-cycle theorem applied to this
particular colouring and the particular colour (\sigma). \(\square\)

### Corollary 3.2 (all four hub roots can be anchored)

In the balanced degree-nine Moser state, for each of the four exterior
hub roots separately there is an (h56)-trace whose split-cycle fan has
a member in the colour of that root and whose corresponding bichromatic
component contains that actual root.

The colourings may be different for the four roots.  The conclusion is
therefore an operation-level family of aligned witnesses, not a claim
that four prescribed fan members coexist in one colouring.

This is stronger than the synchronization statement in Section 6 of
`hadwiger_dirty_connector_two_shore_dichotomy.md`: for the selected root
there is no remaining colour-to-bag alignment gap.

## 4. Consequence for the singleton dirty gate

Assume the terminal dirty state consists of the (K_7^-)-model

\[
              \{h\},\{1\},\{2\},\{r\},C,D_e,D_v,          \tag{4.1}
\]

where

* (r\in\{e_6,e_0\}) is a left root;
* (C) contains (5,6) and the right root (r_5);
* (D_e) contains the other left root (e);
* (D_v) contains (v);
* every displayed pair is adjacent except (D_eD_v), which is
  anticomplete in a (K_7)-minor-free graph.

Theorem 3.1 gives, in one colouring, an (\alpha c(r))-component
containing (h,r,5,6) and avoiding (1,2).  Applied in a possibly
different colouring to (e), it gives an (\alpha c(e))-component
containing (h,e,5,6) and avoiding (1,2).

There is also a useful exact reformulation.  Put (J=G-\{1,2\}).  The
graph (J) is five-connected, and the five bags

\[
                         \{h\},\{r\},C,D_e,D_v             \tag{4.2}
\]

are a rooted (K_5^-)-model at

\[
                             h,r,6,e,v,                     \tag{4.3}
\]

with only the (e v) pair deficient.  Every root in (4.3) is adjacent
to both (1) and (2).  Thus any label-preserving upgrade of (4.2) to
a rooted (K_5)-model immediately gives a (K_7)-model after adjoining
the singleton bags (1,2).

The vertex-rooted (K_4) theorem does not by itself perform this upgrade:
it packages only four roots.  Nor may one regard (4.2) as a static
connectivity theorem; the two-apex icosahedral architecture is the sharp
warning.  Theorem 3.1 supplies information absent from that architecture:
the fan member for the colour of either deficient root is forced to pass
through the critical (56) transition.

### Lemma 4.1 (the five-connected core is nonplanar)

The graph (J=G-\{1,2\}) is five-connected and nonplanar.  Consequently,
by the Kelmans--Seymour theorem, (J) contains a subdivision of (K_5).

#### Proof

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  If (J) were planar, the Four Colour Theorem would
colour (J) with four colours.  Give the adjacent vertices (1,2) two new
colours.  This is a proper six-colouring of all of (G), contrary to the
choice of (G).  Thus (J) is nonplanar.  The final assertion is the
Kelmans--Seymour theorem that every five-connected nonplanar graph
contains a topological (K_5). \(\square\)

This removes the static (K_2\vee I) obstruction at its source: after
deleting its two universal vertices, that example leaves the planar
icosahedron.  The remaining problem is now to align the unrooted
topological (K_5) in (J) with the five common neighbours
(h,r,6,e,v) of (1,2), or to combine it with the already rooted
(K_5^-)-model (4.2).

The two structures alone still do not force that alignment.

### Proposition 4.2 (TK5 plus a rooted near-model is insufficient)

There is a five-connected nonplanar graph \(J_0\), a five-set \(R_0\),
an \(R_0\)-rooted \(K_5^-\)-model, and an unrooted subdivision of
\(K_5\), but no \(R_0\)-rooted \(K_5\)-model.

#### Proof

Let \(A=C_8^2\), the square-antiprism graph, and take the four even
vertices \(0,2,4,6\) on one square face.  The graph \(A\) is
four-connected and planar.  By the rooted-\(K_4\) theorem it has a
rooted \(K_4^-\)-model at those vertices with an opposite pair
deficient, but it has no rooted \(K_4\)-model there: two opposite
linkages would cross in the common face.

Let \(J_0=K_1\vee A\), with universal vertex \(p\), and put
\(R_0=\{p,0,2,4,6\}\).  The graph \(J_0\) is five-connected.  It is
nonplanar (indeed \(A\) has a \(K_4\)-minor, so adjoining \(p\) gives a
\(K_5\)-minor), and hence the Kelmans--Seymour theorem supplies an
unrooted topological \(K_5\).  Adjoining the singleton bag \(\{p\}\) to
the rooted \(K_4^-\)-model in \(A\) gives the required rooted
\(K_5^-\)-model.

If an \(R_0\)-rooted \(K_5\)-model existed, delete its bag containing
\(p\).  The other four bags lie in \(A\), remain connected and pairwise
adjacent, and contain \(0,2,4,6\) separately.  They would be a rooted
\(K_4\)-model in \(A\), a contradiction. \(\square\)

Thus the root-anchored \(56\)-trace is not optional: five-connectivity,
the TK5, and the rooted near-model still admit a sharp planar-apex
counterarchitecture.

### Lemma 4.3 (the (v)-shore contains a literal right vertex)

In (4.1), at least one of (3,4) belongs to (D_v).

#### Proof

The singleton (r) is adjacent to (D_v), while (rv\notin E(G))
because (d(v)=7) and (r\notin N[v]).  Thus (D_v\ne\{v\}).  On a
path in (D_v) from (v) to an endpoint of an (rD_v)-edge, the first
vertex after (v) is a neighbour of (v) lying in (D_v).  The
vertices (h,1,2,r) are other displayed bags and (5,6\in C).  The
only remaining neighbours of (v) are (3,4). \(\square\)

This identifies (D_v) as the unique deficient shore with two literal
carrier contacts: the edges (v5,v6) give two distinct (C)-side
portals, while a vertex of (\{3,4\}) starts every internal route from
the root (v) to the singleton-gate portal.

## 5. The exact carrier peel which would close the singleton

The following elementary certificate is the precise output one wants
from the anchored split cycle.

### Lemma 5.1 (protected (5/6)-peel)

Retain (4.1).  Suppose (C=X\mathbin{\dot\cup}Y), where (X,Y) are
nonempty connected sets, and suppose, after possibly interchanging
(5,6), that

\[
 5\in X,\qquad X\sim D_e,                                  \tag{5.1}
\]

while (Y) retains every old adjacency from (C) to

\[
                         h,1,2,r,D_e,D_v.                   \tag{5.2}
\]

Then (G) has a (K_7)-minor.

#### Proof

Use the seven bags

\[
       \{h\},\quad\{1\},\quad\{2\},\quad\{r\},
       Y,\quad D_e\cup X,\quad D_v.                         \tag{5.3}
\]

The enlarged (D_e\cup X) is connected by (5.1), and it is adjacent
to (D_v) through the literal edge (5v).  Since (C) is connected
and (X,Y) are a nontrivial connected partition, (X\sim Y).  The
set (Y) retains all six contacts in (5.2); all other displayed
contacts are unchanged.  The four roots (r,e,v), together with the
retained carrier contacts, give every adjacency to the triangle
(h12).  Hence (5.3) is a (K_7)-model. \(\square\)

The same proof works with a connected (D_e)-to-(5) or
(D_e)-to-(6) corridor whose (C)-vertices form (X).

## 6. Exact remaining gap

Theorem 3.1 is a genuine use of contraction-criticality and closes the
previous colour-to-root alignment gap for one fan member.  It does **not**
yet imply Lemma 5.1.  A bichromatic component containing

\[
                             h,e,5,6
\]

may enter (D_v), may use the singleton (h) as its only attachment to
the (e)-side, and may meet the carrier through a portal whose deletion
separates one of the protected contacts in (5.2).  Connectedness of the
component gives no label-preserving allocation of its vertices between
(X) and (Y).

Thus the singleton is reduced to the following sharply operation-level
exchange, not to a static near-clique split:

> From the root-anchored (56)-component for the other left root (e),
> extract a protected (5/6)-peel as in Lemma 5.1, or show that every
> such extraction is blocked by one common portal set and use the
> deletion/contraction transition at an edge of that portal set.

The (K_2\vee\)icosahedron example still realizes the static rooted
(K_5^-) and portal-lock phenomena, but it does not satisfy the decisive
critical statement used in Theorem 3.1: a six-colouring of the edge-
deleted graph need not put the two edge ends in the same bichromatic
component for every other colour.  Hence the new theorem does not
silently rely on a connectivity-only assertion refuted by that example.
