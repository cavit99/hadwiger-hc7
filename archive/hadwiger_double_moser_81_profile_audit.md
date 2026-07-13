# Independent audit of the double-Moser outer-portal profiles

## Verdict

**GREEN for the (9\times9=81) two-component claim.**  The current
`double_moser_outer_portal_peel_verify.cpp` checks only the 36 profiles in
which both components meet both old outer vertices and each misses one
new-boundary label.  That is not enough, by itself, for components of type
(a/\mathrm{full}) or (b/\mathrm{full}).  The larger claim is nevertheless
true.  It is independently exhaustively verified by
`double_moser_81_profile_audit.cpp` and admits the short hand proof below.

The three-component “representatives plus an unused literal edge” proof is
also valid.  It works for all (6^3) maximal defect triples; the apparent
12-profile residue in `double_moser_outer_portal_profiles.py` comes from
requiring the third unused boundary vertex to be put into one of the two
leftover bags.  A minor model may delete that vertex.

## 1. Quotient and the nine row types

Write

\[
 L=\{x_1,x_2\},\qquad R=\{x_3,x_4\}.
\]

The graph on

\[
 W=L\mathbin{\dot\cup}R\mathbin{\dot\cup}\{p,q\}
\]

consists of the triangles (L\cup\{q\}) and (R\cup\{p\}), joined
by (pq).  For a component (D) of (C-\{a,b\}), seven-connectivity
gives exactly one of the following nine maximal profiles:

\[
 a/\mathrm{full},\quad b/\mathrm{full},\quad
 ab/\mathrm{full},\quad ab/\mathrm{miss}(d)quad(d\in W).
\tag{1.1}
\]

The notation before the slash records (N_{\{a,b\}}(D)); after the
slash it records the contacts with (W).

## 2. The uniform two-component template

Let (D_1,D_2) be two distinct components, and let (d_i\in
W\cup\{\varnothing\}) be their possible defects.  Each (D_i) meets
at least one of (a,b).

### Lemma 2.1 (two-wing representative lemma)

Unless (d_1=d_2\in\{p,q\}), there are

* one literal edge (H=\{y,z\}\in\{L,R\});
* an ordering ((r,s)) of the opposite literal edge; and
* a bijection ({\rho_1,\rho_2\}=\{p,q\})

such that

\[
 \rho_i\ne d_i,
 \qquad
 d_i\in\{y,z,r\}\Longrightarrow d_i\rho_i\in E(G[W]).
\tag{2.1}
\]

#### Proof

Define the preferred repair representative of a nonempty defect by

\[
 h(d)=
 \begin{cases}
 q,&d\in L\cup\{p\},\\
 p,&d\in R\cup\{q\}.
 \end{cases}                                             \tag{2.2}
\]

Thus (h(d)\ne d) and (h(d)d\in E(G[W])).  If the two preferred
representatives differ, assign them to the corresponding components;
then any choice of (H,r,s) satisfies (2.1).  If at least one defect is
empty, give every nonempty defect its preferred representative and give
the empty-defect component the unused representative; this has the same
conclusion.

Suppose both preferred representatives are (q); the other case is
symmetric.  Hence the nonempty defects lie in (L\cup\{p\}).

* If exactly one defect is (p), give that component (q).  Give the
  other component (p), choose (H=R), and choose (r\in L) different
  from the latter component's defect.  That defect is then the unused
  root (s), so it needs no repair.
* If neither defect is (p), give one component (q) and the other
  (p).  Again take (H=R), choosing (r\in L) different from the
  defect of the component represented by (p).

The sole excluded possibility is (d_1=d_2=p).  Symmetrically, the sole
excluded possibility in the other half is (d_1=d_2=q). (square)

### Lemma 2.2 (ordinary profile certificate)

Under the conclusion of Lemma 2.1, the seven sets

\[
 \{u\},\quad \{y\},\quad\{z\},\quad\{v,r\},\quad
 \{s,a,b\},\quad D_1\cup\{\rho_1\},\quad
 D_2\cup\{\rho_2\}                              \tag{2.3}
\]

form a (K_7)-model.

#### Proof

The component bags are connected because (ho_i\ne d_i).  They are
adjacent to each other: unless one component misses the other
representative, it supplies the required edge directly; if it does, the
other component sees the first representative.  A simultaneous failure
would force the two defects to be the transposed representatives, and
then the literal edge (pq) joins the bags.

Each component bag sees (y,z) and ({v,r}) directly through its full
row, except when the relevant root is its defect; (2.1) repairs exactly
that incidence.  It sees ({s,a,b}) through its nonempty old-outer
contact and sees ({u}) through its representative.

The five boundary bags are mutually adjacent: (yz) is a literal edge,
(v) sees all four roots, (s) is joined to the appropriate one of
(a,b), and (u) sees (v,W).  Thus all seven bags in (2.3) are
pairwise adjacent. (square)

### Lemma 2.3 (equal outer-defect certificate)

If (d_1=d_2\in\{p,q\}), then both components have the (ab)-profile,
and

\[
 \{v\},\quad\{x_1\},\quad\{x_2\},\quad\{u,x_3\},
 \quad D_1\cup\{a\},\quad D_2\cup\{b\},
 \quad\{x_4,p,q\}                                  \tag{2.4}
\]

are a (K_7)-model.

#### Proof

The two component bags are connected and adjacent through (ab).  Since
their common defect is only (p) or only (q), each still meets
(x_1,x_2,x_3,x_4) and at least one of (p,q).  These contacts give
all adjacencies to the other five displayed bags.  The remaining
adjacencies are the two Moser stars, (x_1x_2), and the connected path
(x_4-p-q) or triangle incidences already present in the frame.
\(square\)

Lemmas 2.1--2.3 prove all 81 ordered row pairs.  Notice that the
(a/\mathrm{full}) and (b/\mathrm{full}) profiles cause no difficulty:
the ordinary template uses only that every component meets at least one
of (a,b).  The stronger (ab)-contact is needed only in the equal
outer-defect certificate, where it is automatically present by (1.1).

## 3. Exact independent replay

`double_moser_81_profile_audit.cpp` constructs the conservative
12-vertex quotient for every ordered pair of the nine profiles.  It
enumerates all connected vertex subsets and searches exhaustively for
seven disjoint pairwise adjacent branch sets.  It finds a model in all
81 cases and prints one witness for each unordered profile pair.

This replay is independent of the representative lemmas: it searches all
minor models, rather than only the displayed templates.

## 4. Three components: a genuine unused-edge proof

Let (D_1,D_2,D_3) have defects (d_1,d_2,d_3\in
W\cup\{\varnothing\}).  At least one literal edge (H=\{y,z\}) contains
defects of at most one of the three components.  Let (tin\{p,q\}) be
the triangle vertex adjacent to both ends of (H), and let (T) be the
opposite boundary triangle.

If one component has its defect in (H), represent that component by
(t).  The other two components can be assigned distinct representatives
from the three vertices of (T), each avoiding its own defect.  If no
component has a defect in (H), assign the three representatives from
(T).  A system of distinct representatives exists because each row
forbids at most one vertex.  The only apparent Hall failure is when all
three defects equal one vertex of (T); in that case replace that vertex
in the representative set by (t).  Every component then sees every
representative directly.

Thus there are distinct representatives (ho_1,ho_2,ho_3\in W-H)
such that every (D_i\cup\{\rho_i\}) is connected, the three bags are
pairwise adjacent, and each sees both (y,z).  Consequently

\[
 \{u\},\quad\{v,a,b\},\quad\{y\},\quad\{z\},
 \quad D_i\cup\{\rho_i\}\ (i=1,2,3)              \tag{4.1}
\]

is a (K_7)-model.  The third vertex of (W-H-\{\rho_1,\rho_2,
\rho_3\}) is simply deleted.  This deletion is why the more restrictive
Python partition experiment reports twelve false residues while the
actual minor certificate has none.

## 5. Consequence for the outer peel

The claim that two components of (C-\{a,b\}) force a (K_7)-minor is
correct for every portal profile allowed by seven-connectivity.  The
current hand proof can therefore be compressed to the two-wing
representative lemma plus the single equal-outer-defect template, rather
than a 9-by-9 case enumeration.
