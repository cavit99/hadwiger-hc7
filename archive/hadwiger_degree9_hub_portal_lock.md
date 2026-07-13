# The degree-nine Moser hub: portal completeness and the exact outer lock

## 1. Setting

Let \(G\) be non-six-colourable while every proper minor is
six-colourable.  Let \(v\) have degree seven and suppose its neighbourhood
is the pure Moser spindle on \(h,1,2,3,4,5,6\), with

\[
 E(G[N(v)])=
 \{h1,h2,h3,h4,12,16,26,34,35,45,56\}.          \tag{1.1}
\]

Assume \(d(h)=9\), and put

\[
 H_1=\{1,2\},\qquad H_2=\{3,4\},\qquad
 E=N(h)-\{v,1,2,3,4\}.                            \tag{1.2}
\]

Thus \(|E|=4\), and every member of \(E\) lies outside \(N[v]\).
Theorem 4.1 of `hadwiger_degree9_hub_rainbow_rooted_k4.md` supplies an
\(E\)-rooted \(K_4\)-model

\[
                         \mathcal B=(B_e:e\in E)                \tag{1.3}
\]

in \(G-\{v,h,1,2,3,4\}\).  Since the four bags are disjoint and each
meets the four-element set \(E\), every bag contains exactly one root
\(e\), and every root occurs.

This note proves two structural advances.

1. Every exterior root is complete to one of the two literal edges
   \(H_1,H_2\).
2. The rooted model already gives \(K_7\), except for one balanced
   outer-vertex lock.  A detachable arm in either locked bag then gives
   \(K_7\) explicitly.

## 2. A third simultaneous-star leaf forces portal completeness

### Theorem 2.1 (literal-edge portal theorem)

For every \(e\in E\),

\[
       H_1\subseteq N(e)\qquad\hbox{or}\qquad H_2\subseteq N(e).
\tag{2.1}
\]

#### Proof

Suppose that (2.1) fails.  Then \(e\) misses some \(i\in H_1\) and
some \(j\in H_2\).  Put

\[
 J=\{i,j\},\qquad J'=\{1,2,3,4\}-J.              \tag{2.2}
\]

Both \(J,J'\) are independent: each contains one vertex from each of
the two literal edges.  Moreover \(J\cup\{e\}\) is independent.

Simultaneously contract the disjoint stars

\[
          \{v\}\cup J',\qquad \{h\}\cup J\cup\{e\}             \tag{2.3}
\]

to adjacent vertices, and six-colour the resulting proper minor.  Let
their colours be \(\alpha\ne\beta\).  Delete \(v,h\) and expand only
the independent leaf sets.  The four vertices of \(W=H_1\cup H_2\)
then use \(\alpha,\beta\), one vertex of each literal edge in each
colour.

The vertices \(5,6\) each see one \(\alpha\)-leaf and one
\(\beta\)-leaf: vertex \(5\) sees \(3,4\), while \(6\) sees
\(1,2\).  Hence they avoid \(\alpha,\beta\); the edge \(56\) makes
their colours distinct.  Therefore at most four colours occur on

\[
                         N(v)-\{h\}=W\cup\{5,6\},               \tag{2.4}
\]

so the residual list \(L_v\) has order at least two.

On the other hand, \(W\) uses \(\alpha,\beta\), the selected vertex
\(e\) also has colour \(\beta\), and the other three vertices of
\(E\) contribute at most three further colours.  Thus at most five
colours occur on

\[
                         N(h)-\{v\}=W\cup E,                    \tag{2.5}
\]

and the residual list \(L_h\) is nonempty.  A set of order at least two
and a nonempty set have distinct representatives.  Assigning them to
the adjacent vertices \(v,h\) extends the colouring to \(G\), a
contradiction.  This proves (2.1). \(\square\)

The argument is an unbounded simultaneous-star lemma, not a finite
neighbourhood enumeration.  Equivalently, the set of vertices of
\(W\) missed by one exterior hub neighbour is contained in one literal
edge.

## 3. Combining the portal theorem with the rooted \(K_4\)

Call a rooted bag \(B_e\) **left** if \(e\) is complete to \(H_1\),
and **right** if \(e\) is complete to \(H_2\).  A bag whose root is
complete to both may be assigned either type.

### Theorem 3.1 (rooted core or balanced outer lock)

At least one of the following holds.

1. \(G\) contains a \(K_7\)-minor.
2. The four bags in (1.3) can be labelled

   \[
               L_6,L_0,R_5,R_0                              \tag{3.1}
   \]

   so that exactly two are left and exactly two are right,

   \[
                         6\in L_6,qquad 5\in R_5.             \tag{3.2}
   \]

In particular, in outcome 2 neither outer vertex lies outside the rooted
model, neither lies in a bag of the opposite type, and no root is complete
to both literal edges.

#### Proof

The four rooted bags are pairwise adjacent, and every one is adjacent to
\(\{h\}\) through its root.

If all four bags are left, then

\[
                   \{h\},\{1\},\{2\},B_1,B_2,B_3,B_4          \tag{3.3}
\]

are seven pairwise adjacent bags.  If exactly three are left, let \(R\)
be the remaining right bag.  Then

\[
          \{h\},\{1\},\{2\},B_{L,1},B_{L,2},B_{L,3},
          R\cup\{3,v\}                                        \tag{3.4}
\]

are a \(K_7\)-model: the last bag is connected through the edge from
the root of \(R\) to \(3\), and it sees \(1,2\) through \(v\).
The symmetric statements hold for four or three right bags.  Therefore
a minor-free residue has exactly two bags of each type.  If a root were
complete to both halves, assign its bag to whichever type creates a
three-to-one split and use (3.4).  Hence no such flexible root survives.

Write the balanced bags as \(L_1,L_2,R_1,R_2\).  We next record three
explicit augmentations.

* If \(6\) belongs to a right bag, say \(R_1\), use

  \[
  \{h\},\{1\},\{2\},L_1,L_2,R_1,R_2\cup\{3,v\}.               \tag{3.5}
  \]

  The bag \(R_1\) sees \(1,2\) through the vertex \(6\).

* If \(6\) is outside all four bags and \(5\) belongs to a left bag,
  the symmetric version of (3.5), based on the literal edge \(34\),
  gives \(K_7\).

* Suppose \(6\) is outside all four bags and \(5\) is outside or lies
  in a right bag.  Choose that right bag as \(R_1\) when applicable.
  Then

  \[
  \{h\},\{1\},\{2\},L_1,L_2,
  R_2\cup\{3,v\},
  R_1\cup\{4,5,6\}                                  \tag{3.6}
  \]

  is a \(K_7\)-model.  The last bag is connected through
  \(R_1-4-5-6\), and it sees \(1,2\) through \(6\).

It remains that \(6\) lies in a left bag.  If \(5\) lies in a left
bag, use the symmetric version of (3.5).  If \(5\) is outside the
model, absorb it into the left bag containing \(6\); the edge \(56\)
makes that bag connected and gives it contact to \(3,4\), after which
the same symmetric model applies.  The only case not covered is exactly
(3.2).  This proves the theorem. \(\square\)

All displayed augmentations are safe even if a bag already contains the
displayed outer vertex: the vertex is then retained in that same bag,
not counted twice.  The vertices \(v,1,2,3,4\) never lie in a rooted bag,
by the location of the model in Section 1.

## 4. Detaching one locked outer arm

Retain outcome 2 of Theorem 3.1.  Let \(e_6\in E\cap L_6\) be its
unique root.

### Theorem 4.1 (outer-arm splitter)

Suppose \(L_6\) contains disjoint connected sets \(U,D\) such that

\[
 e_6\in U,qquad 6\in D,qquad E(U,D)\ne\varnothing,           \tag{4.1}
\]

and \(U\) is adjacent to both \(L_0\) and \(R_0\).  Then \(G\)
contains a \(K_7\)-minor.

#### Proof

Use the seven bags

\[
 \{h\},\quad\{1\},\quad\{2\},\quad U,\quad L_0,
 \quad R_0\cup\{3,v\},
 \quad R_5\cup\{4\}\cup D.                                \tag{4.2}
\]

The sixth bag is connected through the root of \(R_0\), which is
adjacent to \(3\), and through \(3v\).  The last bag is connected:
the root of \(R_5\) is adjacent to \(4\), while \(5\in R_5\),
\(6\in D\), and \(56\) joins \(R_5\) to \(D\).

The first five bags form a clique: the roots of \(U,L_0\) see
\(1,2,h\), and \(U,L_0\) are adjacent by hypothesis.  The sixth bag
sees \(1,2\) through \(v\), sees \(U\) by the second protected
adjacency in the hypothesis, and sees \(L_0\) through the old
\(K_4\)-model.  The last bag sees \(1,2\) through \(6\), sees \(U\)
through the edge between \(U,D\), and sees \(L_0\) and the sixth bag
through the old adjacencies from \(R_5\).  Every bag also sees
\(\{h\}\) through its exterior root (or directly through the displayed
Moser edges).  Thus (4.2) is a \(K_7\)-model. \(\square\)

The symmetric statement holds with \(R_5,5,H_2\) in place of
\(L_6,6,H_1\).

### Corollary 4.2 (exact internal gate)

In a \(K_7\)-minor-free residue, let \(K\) be the component of
\(L_6-6\) containing \(e_6\).  Then \(K\) fails to be adjacent to at
least one of \(L_0,R_0\).  Symmetrically, the root component of
\(R_5-5\) misses at least one of \(R_0,L_0\).

#### Proof

If \(K\) met both protected bags, take \(U=K\) and let \(D\) be a
shortest \(6\)-to-\(K\) path in \(L_6\), with its endpoint in \(K\)
deleted.  Then (4.1) holds and Theorem 4.1 applies. \(\square\)

The covering version gives the exact attachment classes.

### Lemma 4.3 (covering split classification)

Suppose

\[
                         L_6=U\mathbin{\dot\cup}D               \tag{4.3}
\]

is a partition into connected adjacent sets, with \(e_6\in U\) and
\(6\in D\).  If \(U\) is adjacent to \(L_0\) and to at least one of
\(R_5,R_0\), then \(G\) contains a \(K_7\)-minor.

#### Proof

If \(U\) sees \(R_0\), Theorem 4.1 applies.  Otherwise \(U\) sees
\(R_5\) but not \(R_0\).  The original bags \(L_6,R_0\) were
adjacent, and (4.3) covers \(L_6\), so \(D\) is adjacent to
\(R_0\).  Use the seven bags

\[
 \{h,3,4\},\quad \{v\}\cup R_5,
 \quad\{1\},\quad\{2\},\quad U,
 \quad D\cup R_0,\quad L_0.                                \tag{4.4}
\]

They are connected: \(h34\) is a triangle; \(v\) sees the vertex
\(5\in R_5\); and \(D\) is adjacent to \(R_0\).  The first two bags
are adjacent through \(h\) and the exterior root of \(R_5\).  Each
sees the singletons \(1,2\): the first through \(h\), the second
through \(v\).  Both see \(U,D\cup R_0,L_0\): use the exterior roots
for the first bag, the old rooted-\(K_4\) adjacencies for the second,
and the assumed \(U\)-\(R_5\) edge where needed.  Finally
\(\{1\},\{2\},U,D\cup R_0,L_0\) form a clique through \(12\),
the left-root contacts, the edge \(U D\), and the old bag
adjacencies.  Hence (4.4) is a \(K_7\)-model. \(\square\)

### Corollary 4.4 (two attachment classes)

Let \(K\) be the component of \(L_6-6\) containing \(e_6\).  In a
\(K_7\)-minor-free residue, one of the following holds:

\[
 K\not\sim L_0,
 \qquad\hbox{or}\qquad
 K\not\sim R_5\text{ and }K\not\sim R_0.                    \tag{4.5}
\]

#### Proof

Put \(U=K\) and \(D=L_6-K\).  Every component of \(L_6-6\) other
than \(K\) has an edge to \(6\), because \(L_6\) is connected.
Consequently \(D\) is connected, contains \(6\), and is adjacent to
\(U\).  Lemma 4.3 now gives (4.5). \(\square\)

Thus the equality cell is no longer an arbitrary rooted \(K_4\).  Its
only surviving geometry consists of two balanced portal types and two
outer vertices which are internally essential one-vertex gates in their
respective branch bags.

## 5. Spanning the host and the exact adhesion equality

The ambient seven-connectivity can now be used without assuming that an
arbitrary rooted model is spanning.

### Lemma 5.1 (spanning rooted model)

The rooted \(K_4\)-model may be chosen so that

\[
              B_{e_1}\mathbin{\dot\cup}\cdots
              \mathbin{\dot\cup}B_{e_4}
              =G-\{v,h,1,2,3,4\}.                            \tag{5.1}
\]

#### Proof

Deleting the six displayed vertices leaves a connected graph, by
seven-connectivity.  The union of the four pairwise adjacent model bags
is connected.  Every component outside that union has an edge to at
least one bag; absorb the whole component into one such bag.  This
preserves connectedness, disjointness, all old bag adjacencies, and the
four roots.  Absorbing every outside component gives (5.1). \(\square\)

Fix such a spanning model in the balanced lock.  For the root component
\(K\) of \(L_6-6\), put

\[
                         S_6=\{h,1,2,3,4,6\}.                  \tag{5.2}
\]

### Theorem 5.2 (portal surplus or exact seven-adhesion)

At least one of the following holds.

1. \(G\) has a \(K_7\)-minor.
2. \(N_G(K)\) is an exact seven-cut.
3. One of the following strict-surplus alternatives holds:

   \[
   \begin{array}{ll}
   K\not\sim L_0,&
   |N(K)\cap(R_5\cup R_0)|\ge2,\\[1mm]
   K\not\sim R_5,R_0,&
   |N(K)\cap L_0|\ge2.
   \end{array}                                                \tag{5.3}
   \]

#### Proof

Assume there is no \(K_7\)-minor.  Corollary 4.4 gives the two cases
in (5.3).  In the first case put

\[
                         P=N(K)\cap(R_5\cup R_0).
\]

The spanning property and the fact that \(K\) is a component of
\(L_6-6\) give

\[
                         N_G(K)\subseteq S_6\cup P.             \tag{5.4}
\]

Indeed, every vertex outside the six displayed boundary vertices lies
in one of the four spanning bags; within \(L_6\), the component \(K\)
can leave only through \(6\); and \(v\) has no neighbour in \(K\),
because \(K\) contains none of the seven vertices of \(N(v)\).
The same inclusion holds in the second case with
\(P=N(K)\cap L_0\).

The set \(N_G(K)\) is a genuine separator: \(K\) is nonempty, while
the other rooted bags lie on the far side.  Seven-connectivity and
(5.4) imply \(|P|\ge1\).  If \(|P|=1\), the right side of (5.4) has
order seven, so seven-connectivity forces equality throughout;
\(N_G(K)\) is an exact seven-cut.  Otherwise \(|P|\ge2\), which is
outcome 3. \(\square\)

The symmetric theorem holds at \(R_5\), with \(5\) in place of
\(6\).  Thus the only non-adhesion residue has two actual protected
portals on each surviving side of an internal outer gate.

## 6. Sharpness of the quotient and the remaining global input

The outer lock is a real obstruction to any theorem using only the
contracted rooted model.  Contract the four rooted bags to vertices
\(L_6,L_0,R_5,R_0\), retain \(v,h,1,2,3,4\), and retain only these
edges:

* the four bag vertices form a clique and all see \(h\);
* \(L_6,L_0\) see \(1,2\), while \(R_5,R_0\) see \(3,4\);
* \(L_6\) also carries the contacts of \(6\), and \(R_5\) those of
  \(5\);
* the remaining edges are the displayed pure-Moser edges.

This ten-vertex quotient has treewidth at most five.  A width-five tree
decomposition is the three-bag path

\[
\begin{aligned}
 A&=\{v,h,L_6,L_0,1,2\},\\
 C&=\{v,h,L_6,L_0,R_5,R_0\},\\
 B&=\{v,h,R_5,R_0,3,4\},
\end{aligned}                                                   \tag{6.1}
\]

with edges \(A-C-B\).  Hence it has no \(K_7\)-minor.  This is an
explicit counterarchitecture to the overstrong assertion

\[
  \text{``an exterior-rooted }K_4\text{ plus the degree-nine hub
  always gives }K_7\text{.''}
\]

What is missing from the quotient is precisely the internal structure
of \(L_6,R_5\) and ambient seven-connectivity.  The next uniform target
is therefore a **locked-outer-gate-to-adhesion lemma**: in a
seven-connected contraction-critical host, the two internal gates in
Corollary 4.4 either fall into the exact-adhesion equality of Theorem 5.2,
or one of the five edge-critical Kempe detours uses the strict two-portal
surplus to create the splitter in Lemma 4.3.

The dependency-free probe
`pure_moser_degree9_model_occupancy_probe.py` exhausts the conservative
type/occupancy quotients and independently returns exactly the balanced
locks described in (3.1)--(3.2).  The hand proofs above, rather than the
probe, establish the positive cases.
