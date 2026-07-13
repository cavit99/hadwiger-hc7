# Adversarial audit of the new degree-seven round

## 0. Verdict

Under the standing hypotheses used in the four notes -- namely that (G)
is a proper-minor-minimal (K_7)-minor-free (7)-chromatic graph, that
(d_G(v)=7), and hence that

\[
 N=N_G(v),\qquad \kappa(G)\ge 7,\qquad \delta(G)\ge 7,
 \qquad \alpha(G[N])=2,
\]

all four audited claims survive.  More precisely:

1. every edge of (Q=\overline{G[N]}) really can be prescribed as the
   repeated pair of a six-colouring of (G-v);
2. the deletion dichotomy for (Q) is correct, with (K_{3,4}) the unique
   all-hard graph;
3. the double-contraction boundary-state Lemma 2.1 is correct;
4. the cutvertex Lemmas 5.3 and 5.4 are correct, including the construction
   which excludes three cut sides; and
5. the graph (K_2\vee\overline{C_8}), with the specified degree-seven
   apex added, is a valid counterexample to the proposed colour-preserving
   removable-path principle based only on the local package.

No branch-set intersection, improper colour expansion, or connectivity
failure was found.  There are two small exposition points worth repairing:

* the one-component conclusion in the (K_3\dot\cup K_4) neighbourhood
  should display the two helper bags explicitly; and
* in the double-contraction proof one should say "uncontract
  (\{v,x,y\}), give (x,y) the colour of (q), and delete (v)" rather
  than "delete the part of (q) coming from (v)."

Neither point changes a theorem.

## 1. Full accessibility and the seven-vertex dichotomy

### 1.1 Full accessibility is valid

Fix (xy\in E(Q)).  Thus (x,y\in N) and (xy\notin E(G)).  Contract
the connected branch set (\{x,v,y\}) to (q), obtaining (J).  It is a
proper (K_7)-minor-free minor, so minimality gives a six-colouring of
(J).

The lower bound (\chi(J)\ge6) is sound.  If (J) had a five-colouring,
uncontracting (q), assigning its colour to both (x) and (y), and
assigning a sixth, globally fresh colour to (v) would colour (G).
The expansion is proper because (xy\notin E(G)), and every old neighbour
of (x) or (y) is a neighbour of (q) in the quotient.

Now take any six-colouring of (J), and put
(U=N-\{x,y\}).  Every (u\in U) is adjacent to (q), using the old
edge (uv), so (U) avoids the colour of (q).  If one of the five other
colours were absent from (U), it could be assigned to (v) after the
same expansion, again producing a six-colouring of (G).  Thus the five
vertices of (U) use the other five colours bijectively.  This proves the
claimed prescribed repeated pair in full, not just its existence for some
colouring.

No assumption about edges from (v) outside (N) is hidden here:
(N=N_G(v)) by definition and (d(v)=7=|N|).

### 1.2 The pseudoforest dichotomy is valid

A triangle-free graph (R) on five vertices which is not a pseudoforest
has a connected component with cyclomatic number at least two.  If that
component has (s) vertices, it has at least (s+1) edges.  For
(s\le4) this contradicts the triangle-free extremal bound, and for
(s=5) it requires at least six edges.  Mantel's bound is six, with the
unique equality graph (K_{2,3}).  Hence (K_{2,3}) is indeed the only
five-vertex triangle-free non-pseudoforest.

Suppose now that (Q-\{x,y\}\cong K_{2,3}) for every edge (xy) of the
nonempty triangle-free seven-vertex graph (Q).  The connectivity argument
in the note is correct: if (xy) lies in one component, the other five
vertices must all lie in one component because their induced graph is
connected.  They induce (K_{2,3}), so they contain an edge (uv).
Deleting (u,v) then leaves the still-present edge (xy) in a component
separate from the other three vertices, contradicting the hypothesis for
(uv).

Writing (m=e(Q)), deletion of the ends of any edge gives

\[
 6=m-d(x)-d(y)+1,
 \qquad d(x)+d(y)=m-5.                         \tag{1.1}
\]

In a connected graph with constant degree sum on edges, degrees alternate
along paths.  An odd cycle forces regularity; otherwise the graph is
bipartite and semiregular.  The regular equations
(m=7r/2) and (2r=m-5) give (r=10/3), impossible.  In the bipartite
case, with side orders (p\le q), degrees (r,s), and (p+q=7), one has

\[
 pr=qs=m,\qquad r+s=m-5,
 \qquad r\le q,\quad s\le p.
\]

For (p=1,2,3), respectively, the divisibility and degree bounds give
((r,s)=(6,1),(5,2),(4,3)); only the last satisfies the second equation.
Thus (p=3,q=4,r=4,s=3), so every cross-edge is present and
(Q=K_{3,4}).  An exhaustive check of the unlabeled seven-vertex graph
atlas also finds exactly this one isomorphism class, but the preceding
proof is complete without computation.

### 1.3 The exceptional one-component conclusion is also valid

When (Q=K_{3,4}), write (G[N]=K_3\dot\cup K_4), with parts (A,B).
If (G-N[v]) had two distinct components (C_1,C_2), seven-connectivity
would give (N(C_i)=N).  Choose distinct (a_1,a_2\in A).  Then

\[
 C_1\cup\{a_1\},\quad C_2\cup\{a_2\},
 \quad \{b\}\ (b\in B)
\]

are six disjoint connected pairwise adjacent bags: the first two are
adjacent through (a_1a_2), and each meets every (B)-singleton through
its exterior component.  All six bags meet (N), so adding ({v})
gives a (K_7)-model.  Hence at most one exterior component exists.  At
least one exists, for example because every (a\in A) has only its two
neighbours in (A) and (v) before exterior neighbours are counted,
whereas (\delta(G)\ge7).  Thus the asserted unique exterior component is
correct.  The original note should include these explicit helper bags.

## 2. Audit of the double-contraction boundary-state lemma

Let (G-N[v]=C_1\dot\cup C_2), and let
(L_i=G[N\cup C_i]).  Seven-connectivity implies
(N_G(C_i)=N): otherwise (N_G(C_i)), of order at most six, separates
(C_i) from (v).

The three assertions of Lemma 2.1 are all correct.

### 2.1 Singleton states on both sides

For each (e=xy\in E(Q)), the full-accessibility colouring above restricts
to a colouring of each (L_i) whose boundary equality partition is exactly
({xy}).  Therefore
({e}\in\mathcal E_1\cap\mathcal E_2).

### 2.2 No common state of size at least two

Two side colourings with the same matching state induce the same equality
partition on (N).  A permutation of the six colour names makes them
identical on (N), including when the boundary uses only four or five of
the six colours.  Since there are no edges between (C_1) and (C_2),
they then glue to a colouring of (G-v).  A state of size at least two
uses at most five colours on (N), so an absent colour can be assigned to
(v).  This contradicts (\chi(G)=7).

### 2.3 Every edge belongs to a larger state on each side

Fix (e=xy) and (i), and put (j\ne i).  Contract the disjoint connected
sets (\{v,x,y\}) and (C_j) to (q,h).  The resulting graph is a proper
minor and hence is six-colourable.  The vertices (q,h) are adjacent
because both (x) and (y) have neighbours in (C_j).  Each of the five
vertices (U=N-\{x,y\}) is adjacent to both (q) and (h): to (q)
through its old edge to (v), and to (h) because (N(C_j)=N).
Consequently (q,h) have different colours and (U) uses at most the
other four.

Delete (h), uncontract the first branch set, assign the colour of (q)
to (x,y), and discard (v).  This is a proper colouring of (L_i).
The pair (xy) is a boundary equality class, and among the remaining five
vertices some second equality occurs.  Since
(\alpha(G[N])=2), every equality class has order at most two.  Therefore
the state is a matching containing (e), of size two or three.  The
branch sets used in the quotient are disjoint, and adjacency between them
does not invalidate simultaneous contraction.

This also confirms that the lemma gives coverage only.  It does not couple
the resulting larger-state colouring to the singleton-state colouring, so
the negative set-system examples in the boundary-state note are not
contradicted.

## 3. Audit of the cutvertex restrictions

Assume the exceptional cell

\[
 G[N]=K_3\dot\cup K_4,
 \qquad A=V(K_3),\quad B=V(K_4),
\]

and that (C=G-N[v]) is the unique exterior component.  Let (z) be a
cutvertex of (C), and let (D) be a component of (C-z).

### 3.1 Lemma 5.3

All neighbours of (D) outside (D) lie in
({z}\cup N).  If (D) met at most five vertices of (N), deleting
({z}\cup N_N(D)) would be a cut of order at most six separating (D)
from (v).  Thus every side meets at least six boundary vertices.

If two sides (D_1,D_2) meet all four vertices of (B), each meets at
least two vertices of (A).  Two subsets of a three-set, each of order at
least two, have distinct representatives; choose (a_i\in A) adjacent to
(D_i), with (a_1\ne a_2).  The bags

\[
 D_1\cup\{a_1\},\quad D_2\cup\{a_2\},
 \quad \{b\}\ (b\in B)
\]

form the claimed (N)-meeting (K_6)-model.  In particular, the first
two bags are disjoint and adjacent through (a_1a_2).

If (D_1,D_2) both have the unique defect (b\in B), they meet all of
(N-\{b}).  The degree count in the note is correct:
(b) has only its three neighbours in (B) and (v) outside (C), so
(d(b)\ge7) gives at least three neighbours in (C).  Neither deficient
side contains such a neighbour.  Choose a (b)-(z) path (R) starting
with any remaining (C)-neighbour of (b) and then staying in its
component of (C-z) until it reaches (z) (or use the edge (bz)).
The path avoids (D_1\cup D_2).  With distinct (a_1,a_2\in A), the six
bags

\[
 D_1\cup\{a_1\},\quad D_2\cup\{a_2\},\quad V(R),
 \quad \{b'\}\ (b'\in B-\{b})
\]

are disjoint.  The endpoint (z\in V(R)) sees both sides, repairing their
only missing (B)-adjacency.  All remaining adjacencies are supplied by
the cliques on (A,B) and by the boundary attachments.  This verifies the
second model without assigning (z) to two bags.

It follows correctly that there is at most one side meeting all of (B)
and at most one side for each of the four possible defects in (B), hence
at most five sides at this stage.

### 3.2 Lemma 5.4, including the three-side closure

A nongood side misses one vertex of (B) and therefore meets every vertex
of (A).  Two nongood sides with different defects can be consolidated
with any (a\in A):

\[
 X=D_i\cup D_j\cup\{a\}.
\]

The bag is connected because (a) has a neighbour in each side, and it
is adjacent to all of (B) because the two defects differ.

Four nongood sides can therefore be paired into two disjoint (B)-complete
helper bags using distinct vertices of (A); together with the four
(B)-singletons they form a (K_6)-model.  Likewise, one good side and
two nongood sides give two such helpers: the good side meets at least two
vertices of (A), so its chosen (A)-vertex can be made distinct from
the one used to consolidate the nongood pair.

It remains to check the genuinely new case of three nongood sides.  Their
defects (b_1,b_2,b_3\in B) are distinct by Lemma 5.3.  The sets
(B-\{b_i\}) have a system of distinct representatives
(c_1,c_2,c_3).  Put (X_i=D_i\cup\{c_i\}).  Then:

* each (X_i) is connected because (D_i) meets (c_i);
* the (X_i) are disjoint and pairwise adjacent through the clique edges
  (c_ic_j); and
* each (X_i) is adjacent to each singleton ({a}), (a\in A), because
  a nongood side meets all of (A).

The three (X_i) and the three (A)-singletons are therefore six disjoint
pairwise adjacent (N)-meeting bags.  Adding ({v}) gives a
(K_7)-model.  This proves that (C-z) has at most two components.  The
argument does not reuse (z), and no hidden linkage assumption is present.

## 4. Audit of the explicit CP--RP obstruction

Let

\[
 C=p,a,q,b,c,r,d,e,p,
 \qquad J=\overline{C_8},
 \qquad H=K_2\vee J,
\]

where the two universal adjacent vertices are (h_1,h_2).  Put
(N=\{h_1,h_2,a,b,c,d,e\}), and add (v) adjacent exactly to (N).

### 4.1 Chromatic and connectivity data

The independent sets of (J) have order at most two and its independent
pairs are precisely the cycle edges.  A four-colouring is therefore a
perfect matching of the cycle.  The cycle has exactly the two perfect
matchings

\[
 M_0=\{pa,qb,cr,de\},\qquad
 M_1=\{ep,aq,bc,rd\}.
\]

Thus (\chi(J)=4) and (\chi(H)=6).  Each matching has exactly one pair
wholly in (N), and every one of its other pairs meets (N); the two
universal singleton colours also meet (N).  Hence every six-colouring of
(H) uses all six colours on (N), so (\chi(G)=7).

The connectivity claims are correct.  The graph (J) is five-connected:
after deletion of at most four vertices, a disconnection would make every
cross-pair an edge of (C_8).  A singleton side can have at most two such
cross-neighbours, while two sides of order at least two would give a
(K_{2,2}) in (C_8), both impossible when at least four vertices remain.
Since (\delta(J)=5), equality follows.  Joining (K_2) gives
(\kappa(H)=7).  If at most six vertices are deleted from (G), then:

* when (v) remains, (H) minus those vertices is connected and at least
  one of the seven vertices of (N) remains to attach (v); and
* when (v) is deleted, at most five vertices were deleted from (H).

Therefore (\kappa(G)=7), the upper bound following from (d(v)=7).
The cycle vertices have degree seven in (H); (p,q,r) do not see (v),
and (v) has degree seven, so (\delta(G)=7).  Finally, the only cycle
edges with both ends in (N) are (bc,de), hence

\[
 \overline{G[N]}=\{bc,de\},\qquad \alpha(G[N])=2.
\]

These values were also checked directly by computer:

\[
 \kappa(J)=5,\qquad\kappa(H)=7,\qquad\kappa(G)=7.
\]

### 4.2 Genuine accessibility and failure of CP--RP

Under (M_0), the repeated boundary pair is (de), the unique roots are
(h_1,h_2,a,b,c), and their missing-edge graph is the single edge (bc).
The two relevant colour classes are (\{q,b\}) and (\{c,r\}).  Their
induced bichromatic graph has the unique (b)-(c) path

\[
 b-r-q-c.                                          \tag{4.1}
\]

On the other hand, after the unique roots are removed, deleting (q,r)
leaves the vertices (p,d,e), with (pd) the only edge.  Hence every
(d)-(e) path avoiding the roots contains (q) or (r), and deleting
either destroys (4.1).

Under (M_1), the repeated pair is (bc), the roots are
(h_1,h_2,a,d,e), and the only missing root edge is (de).  The relevant
classes are (\{r,d\}), (\{e,p\}), and their unique path is

\[
 d-p-r-e.                                          \tag{4.2}
\]

Deleting (p,r) from the root-avoiding graph leaves (q,b,c), with
(qc) its only edge.  Thus every root-avoiding (b)-(c) path contains
(p) or (r), and deletion destroys (4.2).

These are all accessible colourings up to colour permutation: every
six-colouring of (H) induces one of the two perfect matchings above.
Moreover, each colouring descends to the corresponding genuine
(\{v,x,y\})-contraction, and a five-colouring of that contraction would
expand to a six-colouring of (G).  Hence both contraction graphs really
have chromatic number six.

### 4.3 The example is correctly excluded by the global CE hypotheses

Inside (J), the bags

\[
 \{p\},\quad\{q\},\quad\{c\},\quad\{d\},\quad\{a,r\}
\]

form a (K_5)-model.  The last bag is connected; (r) supplies adjacency
to (p,q), and (a) supplies adjacency to (c,d).  The other four
singletons are pairwise adjacent.  Adding ({h_1},{h_2}) gives the
claimed (K_7)-model in (H).

The failure of edge-criticality is also valid.  Deleting the edge (pb)
from (J) replaces the complementary cycle by
(R=C_8+pb).  This graph is triangle-free, so independent sets of
(\overline R) have order at most two; (M_0) still gives a
four-colouring.  Every four-colouring of the eight-vertex graph therefore
consists of four pairs which are edges of (R).  Since
(R[\{p,q,r\}]) is edgeless, every pair meets (N).  Together with the
two universal singleton colours, every six-colouring of (H-pb) saturates
(N).  Hence (G-pb) remains seven-chromatic.

The example therefore refutes only the local CP--RP implication, exactly
as advertised.  It does not refute any statement using (K_7)-minor
exclusion or proper-minor/edge criticality.

## 5. Consequence for the search

The new positive reductions are safe to reuse.  What they do **not**
provide is equally important:

* full accessibility does not couple the colourings belonging to different
  contractions;
* the boundary-state cover lemma does not provide a Kempe transition
  between a singleton state and its larger state; and
* high connectivity, saturation, and even a one-edge forest do not imply
  a colour-preserving removable path without the global minor-critical
  hypotheses.

Thus the remaining proof mechanism must genuinely use either
(\eta(G)=6), criticality under edge deletion/contraction, or a global
rerouting theorem.  None of the four audited claims silently supplies that
missing mechanism.
