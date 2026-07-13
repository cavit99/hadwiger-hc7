# The central exact two-shore funnel

## 1. Geometry before using colour

Let $G$ be seven-connected and $K_7$-minor-free, and let

\[
 S=\{h,1,2,5,6,y,z\}
\]

be the full exact adhesion from the central-edge outcome of
`hadwiger_four_connected_rooted_diamond.md`.  Assume $G-S$ has exactly
two components.  In the old degree-seven frame,

\[
 N(v)=\{h,1,2,3,4,5,6\},
\]

$v$ is adjacent to all seven members of its neighbourhood, $34$ is an
edge, and each of $3,4$ is adjacent to $h$ and $5$.

If $v\in\{y,z\}$, the boundary itself contains the literal $K_4$ on
$\{v,h,1,2\}$.  Theorem 2.2 below gives the corresponding fan
certificate.  Until then assume $v\notin\{y,z\}$.

If $\{y,z\}=\{3,4\}$, then $S=N(v)$ and the two-shore cut consists of
the singleton $\{v\}$ and the sole exterior component of $G-N[v]$.
That is exactly the already isolated sole-exterior pure-Moser problem.
This note treats the other placement.

Let $C_v$ be the shore containing $v$ and a member
$\ell\in\{3,4\}-S$, and let $D$ be the opposite full shore.  Let $R$
be the component of $C_v-v$ containing $\ell$.  Then

\[
 R\sim v,\qquad N(R)\subseteq S\cup\{v\}.          \tag{1.1}
\]

The untouched shore $D$ is on the far side of $N(R)$.  Therefore
seven-connectivity gives

\[
 |N_S(R)|\ge6.                                    \tag{1.2}
\]

Moreover $R$ meets both $h$ and $5$, through the literal $\ell$.
Consequently precisely one of the following holds.

1. $R$ meets all five labels
   \[
                    K=\{h,1,2,5,6\};              \tag{1.3}
   \]
2. $R$ has a unique defect $d\in\{1,2,6\}$, and
   \[
                    T_d=(S-\{d\})\cup\{v\}        \tag{1.4}
   \]
   is another exact seven-cut, with $R$ a full component behind it.

Indeed, the only possible defect outside $K$ is $y$ or $z$, while a
defect in $K$ cannot be $h$ or $5$.  In the latter case (1.1)--(1.2)
give $N(R)=T_d$ exactly.  Thus failure of (1.3) is not a vague portal
deficiency: it is a specified nested exact adhesion.

## 2. The separated five-arm certificate

The following positive object is weaker than a covering bipartition of
the opposite shore.

### Theorem 2.1 (separated central fan)

Assume (1.3).  Suppose there are disjoint sets $X,Y\subseteq D$ such
that

\[
\begin{aligned}
 &G[X\cup\{5\}]\text{ is connected and }
   N_{\{h,1,2\}}(X) = \{h,1,2\},\\
 &G[Y\cup\{6\}]\text{ is connected and }h\in N(Y).
                                                        \tag{2.1}
\end{aligned}
\]

Then $G$ contains a $K_7$-minor.

#### Proof

Use the seven bags

\[
 \{h\},\quad\{1\},\quad\{2\},\quad
 \{v\},\quad R,\quad X\cup\{5\},\quad Y\cup\{6\}. \tag{2.2}
\]

They are disjoint and connected.  The first three form a triangle.
Each of the last four sees that triangle: use the old star at $v$,
(1.3), the three contacts of $X$, and the $h$-contact of $Y$ together
with $16,26$.

The last four are pairwise adjacent through, respectively,

\[
 vR,\quad v5,\quad v6,\quad R5,\quad R6,\quad56.   \tag{2.3}
\]

These are all twenty-one adjacencies, so (2.2) is a $K_7$-model.
\(\square\)

No edge between $X$ and $Y$ is required.  Nor must either set cover a
side of $D$.  This is important: the exact geometric demand is a
reserved $6$-to-$h$ arm disjoint from a $5$-rooted three-arm fan, not
a spanning shore split.

The placement $v\in\{y,z\}$ has an even simpler version.

### Theorem 2.2 (the literal-$K_4$ fan)

Suppose $v\in S$, let $C,D$ be the two full shores, and suppose one
shore, say $C$, contains disjoint sets $X,Y$ satisfying (2.1).  Then
$G$ contains a $K_7$-minor.

#### Proof

The seven bags are

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 D,\quad X\cup\{5\},\quad Y\cup\{6\}.             \tag{2.4}
\]

The first four form a $K_4$.  The full shore $D$ sees every singleton
and both anchored fan bags through $5,6$.  Each fan bag sees the $K_4$
by (2.1), using $v5,v6,16,26$ where appropriate, and the two fan bags
meet through $56$.  Thus all seven bags are pairwise adjacent.
\(\square\)

The literal-$K_4$ placement also permits an unbounded cutvertex
closure.

### Theorem 2.3 (cutvertex closure in the literal-$K_4$ placement)

Assume $v\in S$, and let $C,D$ be the two full shores.  If $C$ has a
cutvertex, then either $G$ contains a $K_7$-minor, or $C$ has a
connected adjacent split

\[
                         C=X\mathbin{\dot\cup}Y               \tag{2.5}
\]

such that, up to interchanging $X,Y$,

\[
              N_S(X)=S-\{1\},\qquad N_S(Y)=S-\{2\},          \tag{2.6}
\]

and $z1,z2\notin E(G)$.  Thus every cutvertex shore outside this one
antipodal capacity state is eliminated, independently of its order.
In the residual, the chosen cutvertex has exactly two lobes; after
orienting them as $L_1,L_2$,

\[
 N_S(L_1)=S-\{1\},\quad N_S(L_2)=S-\{2\},\quad
 q1,q2\notin E(G).                                  \tag{2.6a}
\]

#### Proof

Let $q$ be a cutvertex and let $X$ be one component of $C-q$; put
$Y=C-X$.  Both sets are connected and adjacent.  For $X$,

\[
                         N(X)\subseteq S\cup\{q\}.
\]

The opposite shore is on the far side, so seven-connectivity makes
$X$ adjacent to at least six vertices of $S$.  A second component of
$C-q$, contained in $Y$, gives the same lower bound for $Y$.  Since
$C$ is full, the two possible one-element defect sets are distinct.

There are two literal boundary cliques

\[
 Q_h=\{v,h,1,2\},\qquad Q_6=\{v,6,1,2\}.                    \tag{2.7}
\]

Choose one of them and distinct anchors $a_X,a_Y\in S-Q$.  An anchor
is assigned only to a piece which contacts it; if that piece misses a
member $d$ of $Q$, additionally require $a_Xd$ (or $a_Yd$) to be a
boundary edge.  Whenever this assignment exists, the seven bags

\[
       \{q:q\in Q\},\qquad D,\qquad
       X\cup\{a_X\},\qquad Y\cup\{a_Y\}             \tag{2.8}
\]

form a $K_7$-model.  The four singleton bags form a clique.  Fullness
joins $D$ to them and to both anchored bags.  The two anchored bags are
adjacent through the $X$--$Y$ edge and see every singleton; their only
possible missing singleton is repaired by their anchor.

It remains only to choose the anchors.  With no optional edge incident
with $z$, the available repair incidences are

\[
\begin{array}{c|c|c}
Q&S-Q&\text{repairs forced by the old frame}\\ \hline
Q_h&\{5,6,z\}&v\!:\{5,6\},\quad1\!:6,\quad2\!:6,\\
Q_6&\{h,5,z\}&v\!:\{h,5\},\quad1\!:h,\quad2\!:h,
                         \quad6\!:5.
\end{array}                                                   \tag{2.9}
\]

Defects not belonging to the selected clique need no repair.  Use
$Q_6$ when one defect is $h$, use $Q_h$ when one defect is $6$, and
otherwise use $Q_h$.  The spare third anchor makes the two choices
distinct.  The only failure is when the two defects are $1$ and $2$:
both require $6$ for $Q_h$, and both require $h$ for $Q_6$.  If either
$z1$ or $z2$ is present, $z$ supplies a second repair anchor, so even
that row closes.  This proves (2.6). \(\square\)

The two-row obstruction (2.6) is sharp for this branch-set mechanism;
it is the exact place where the $56$ transition must provide an
interface exchange rather than another static anchor.

To prove the final assertion in (2.6a), let
$L_1,\ldots,L_k$ be the components of $C-q$.  If the split
$L_1\mid(C-L_1)$ survives, orient it so that $L_1$ misses $1$ and
the other side misses $2$.  Hence $q,L_2,\ldots,L_k$ have no contact
to $2$.  If $k\ge3$, the complementary side of the split at $L_2$
contains both $L_1$ (which contacts $2$) and $L_3$ (which contacts
$1$), so it is full to $S$.  That defect pair is not the exceptional
$1\mid2$ row and has already been closed.  Thus $k=2$.

Now apply the anchor argument to the split
$L_2\mid(C-L_2)$.  The second side contains $L_1$ and therefore
contacts $2$.  To remain exceptional it must miss $1$, so the
cutvertex $q$ has no $1$-contact.  The first orientation already says
that $q$ has no $2$-contact.  This proves (2.6a).

Combining Sections 1--2 gives a rigorous two-shore dichotomy:

\[
 \boxed{K_7\text{ from a separated fan}}
 \quad\text{or}\quad
 \boxed{T_d\text{ for }d\in\{1,2,6\}}
 \quad\text{or}\quad
 \boxed{\text{a fan-interlacing obstruction in }D}.           \tag{2.10}
\]

The middle outcome is an actual exact cut, not an order-six cut and
not a quotient defect.

## 3. What the critical edge supplies

Now assume $G$ is seven-contraction-critical.  Let $p$ be the image of
$56$ in $L=G/56$, let $c$ be a six-colouring of $L$, and put
$\alpha=c(p)$.  The split-cycle theorem gives, for every
$\beta\ne\alpha$, a simple $\alpha/\beta$ path $P_\beta$ from $5$
to $6$ in $G-56$, or equivalently a side-labelled cycle through $p$
in $L$.

Put

\[
 S'=(S-\{5,6\})\cup\{p\}.
\]

### Lemma 3.1 (two-shore itinerary normal form)

If the six vertices of $S'$ receive six distinct colours, let
$q_\beta$ be the unique member of $S'-\{p\}$ of colour $\beta$.
Then a shortest $P_\beta$ has exactly one of the following forms.

1. Its interior lies in one shore of $G-S$.
2. It contains $q_\beta$, and its two subpaths from $5$ to
   $q_\beta$ and from $q_\beta$ to $6$ have interiors contained in
   single shores (not necessarily the same shore).

More generally, if a colour $\beta$ is absent from $S'$ and $p$ is
the only $\alpha$-coloured vertex of $S'$, then $P_\beta$ has outcome
1.

#### Proof

In the rainbow case the only boundary vertices whose colours belong to
$\{\alpha,\beta\}$ are $5,6,q_\beta$.  A simple path uses
$q_\beta$ at most once.  After deleting these boundary vertices, each
remaining path segment lies in one component of $G-S$, since distinct
shores are anticomplete.  If $q_\beta$ is absent from the path there is
only one segment, proving outcome 1; otherwise there are the two stated
segments.  In the final stated case, no boundary vertex other than the
split copies $5,6$ has either colour $\alpha$ or $\beta$, so the same
argument forces the whole interior into one shore. \(\square\)

For $q_\beta=1$ or $2$, the second subpath may be replaced by the
literal edge $q_\beta6$.  Hence each of the colours of $1,2$ supplies
either a shore-confined $5$--$6$ path or a $5$--$q_\beta$ arm whose
interior lies in one shore.

### Corollary 3.2 (clean critical fan closes)

Assume the boundary trace is rainbow.  Suppose either $v\in S$, or
$v\notin S$ and the near-full lobe is in row (1.3).  Suppose the
$h$-cycle uses two segments in a shore to which Theorem 2.1 or 2.2
applies (the opposite shore $D$ in the first case), one from $5$ to
$h$ and one from $h$ to $6$, and the $1$- and $2$-cycles supply arms
in that same shore from $5$ to $1,2$.
If the interior of the $h$--$6$ segment is disjoint from the union of
the interiors of the other three arms, then $G$ has a $K_7$-minor.

#### Proof

Let $Y$ be the interior of the $h$--$6$ segment and let $X$ be the
union of the interiors of the three $5$-rooted arms.  The set
$X\cup\{5\}$ is connected even if the three interiors meet only at
their common boundary end $5$; it sees $h,1,2$.  Similarly
$Y\cup\{6\}$ is connected and $Y$ sees $h$.  The disjointness
hypothesis gives (2.1).  If $v\notin S$ and this shore is the opposite
shore $D$, Theorem 2.1 applies (provided the near-full lobe is in the
non-descent row (1.3)); if $v\in S$, Theorem 2.2 applies. \(\square\)

Paths belonging to different nonzero colours can intersect only in
$\alpha$-coloured vertices.  Therefore the residual in this normalized
Kempe state is now exact: either a required arm is diverted into the
distinguished shore $C_v$, or every choice of the $h$--$6$ return has
an unavoidable, ordered first hit at an $\alpha$-vertex of one of the
three $5$-rooted arms.  This is the two-shore ordered web/portal state;
contracting the arms to unlabelled edges would erase its only remaining
information.

## 4. Scope and remaining gap

Theorem 2.1 eliminates an unbounded family and Lemma 3.1 converts every
critical-edge witness into a two-shore itinerary without enumerating
optional $y,z$ edges.  What remains is to prove that the unavoidable
first-hit state either can be uncrossed to the separated fan, or exposes
one of the exact cuts $T_d$ in a form compatible with the allocated
peel.  No such final uncrossing is claimed here.

The branch sets in Theorem 2.1 and all possible harmless defects
$\varnothing,y,z$ of $R$ are replayed by
`degree9_exact7_two_shore_fan_verify.py`.
