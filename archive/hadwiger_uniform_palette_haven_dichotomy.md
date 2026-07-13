# Exact traces produce a colour haven: a uniform root-or-separator theorem

## 1. Setting

Let (r\ge 2), let (G) be a graph which is not (r)-colourable, and
let (v\in V(G)) be such that

\[
                         H:=G-v
\]

has a proper (r)-colouring (c).  Write (N=N_G(v)).  Necessarily
every colour occurs on (N), since a colour absent from (N) could be
assigned to (v).

The first result below uses no minor theory.  The minor-critical input
enters in Section 3, where a star contraction supplies an exact one-block
trace on (N).

## 2. Palette support across an arbitrary separator

### Theorem 2.1 (palette-support dichotomy)

Let ((A,B)) be a separation of (H), put

\[
 X=A\cap B,\qquad D=A-B,\qquad E=B-A,
\]

and let

\[
 C_X=c(X),\qquad F=[r]-C_X.
\]

Then one of the two open shores sees every colour not used on the
adhesion:

\[
 F\subseteq c(N\cap D)
 \quad\hbox{or}\quad
 F\subseteq c(N\cap E).                         \tag{2.1}
\]

#### Proof

Put

\[
 P=c(N\cap D)-C_X,\qquad Q=c(N\cap E)-C_X.
\]

Permuting the colours in (F) on all vertices of (D), while fixing
every colour in (C_X), preserves properness.  Indeed it plainly
preserves edges inside (D); and on an edge (xy) with (x\in D),
(y\in X), the colour (c(y)) is fixed, so no other colour can be
mapped to it by the permutation.  There are no edges from (D) to
(E).

For two subsets (P,Q\subseteq F), a permutation \(\pi\) of (F) can
be chosen so that

\[
                    |\pi(P)\cup Q|=\max\{|P|,|Q|\}.       \tag{2.2}
\]

If (|P|\le |Q|), map (P) injectively into (Q) and extend that
injection to a permutation of (F); the other case is symmetric.

After this shore permutation, the colours appearing on (N) are
contained in

\[
                 C_X\cup\pi(P)\cup Q.
\]

If neither set in (2.1) contained (F), then

\[
 |C_X|+\max\{|P|,|Q|\}<|C_X|+|F|=r.
\]

The resulting proper colouring of (H) would omit a colour on (N),
and that colour could be assigned to (v), contrary to the hypothesis
on (G).  Hence (2.1) holds.  \(\square\)

### Theorem 2.2 (one component carries the whole free palette)

For every (X\subseteq V(H)) with (H-X\ne\varnothing), some component (K) of (H-X)
satisfies

\[
                         [r]-c(X)\subseteq c(N\cap K).          \tag{2.3}
\]

#### Proof

Let (K_1,\ldots,K_m) be the components of (H-X), put
(F=[r]-c(X)), and define (P_i=c(N\cap K_i)\cap F).  Independently
permute the colours of (F) on each component (K_i), fixing every
colour in (c(X)).  These permutations preserve properness because
different components are anticomplete and all boundary colours are
fixed.

Let (a=\max_i|P_i|), choose an (a)-set (Q\subseteq F), and for
each (i) map (P_i) into (Q), extending the injection to a
permutation of (F).  The resulting colouring uses at most

\[
                              |c(X)|+a
\]

colours on (N).  Since (G) is not (r)-colourable, this number is
at least (r).  But (a\le|F|=r-|c(X)|), so equality holds and some
(P_i=F).  Its component is the required (K).  \(\square\)

The assertion is stronger than a two-shore orientation: the whole free
palette occurs in one actual component, even when individual colours
have many occurrences on (N).

### Corollary 2.3 (all free unique roots lie in one component)

Suppose a set (U\subseteq N) has the property that every colour used
on (U) occurs exactly once on all of (N).  For every
(X\subseteq V(H)), all vertices

\[
 U_X:=\{u\in U:c(u)\notin c(X)\}                 \tag{2.4}
\]

lie in one component of (H-X), provided (U_X\ne\varnothing).

#### Proof

If two vertices of (U_X) lay in different components, take one
component (K) containing some but not all of (U_X), and apply
Theorem 2.1 to the separation with open shores (K) and the union of
the other components of (H-X).  The first shore misses the unique
colour of a vertex of (U_X-K), while the second shore misses the
unique colour of a vertex of (U_X\cap K).  Thus neither shore sees
every colour outside (c(X)), contradicting (2.1).  \(\square\)

This is stronger than the usual numerical well-linkedness conclusion.
It remembers the actual equality state of the contracted colouring.

### Theorem 2.4 (private-colour haven, without an equality-cell hypothesis)

Let

\[
 U_c=\{u\in N: c(u)\text{ occurs exactly once on }N\},
 \qquad h=|U_c|.                                  \tag{2.5}
\]

If (h>0), then (H) has a canonical haven of order (h): for every
(X\subseteq V(H)), (|X|<h), let \(\beta_c(X)\) be the component of
(H-X) containing all vertices

\[
              \{u\in U_c:c(u)\notin c(X)\}.       \tag{2.6}
\]

This set is nonempty, the component exists and is unique, and

\[
 |U_c\cap V(\beta_c(X))|\ge h-|c(X)|\ge h-|X|.    \tag{2.7}
\]

If (X\subseteq Y) and (|Y|<h), then

\[
                         \beta_c(Y)\subseteq\beta_c(X).        \tag{2.8}
\]

#### Proof

Fewer than (h) colours occur on (X), so the colour of at least one
private root is absent.  Corollary 2.3 puts all such roots in one
component and gives (2.7).  If (X\subseteq Y), choose a private-root
colour absent from (c(Y)).  Its unique root lies in both haven
components; a component of (H-Y) is contained in a component of
(H-X), proving (2.8).  \(\square\)

### Corollary 2.5 (degree controls haven order)

If (d=|N|), then every proper (r)-colouring of (H) has at least

\[
                              2r-d                              \tag{2.9}


private colours on (N) (with the lower bound read as zero when
negative).  Consequently it supplies a colour haven of order at least
(2r-d).

#### Proof

All (r) colours occur on (N).  If (h) colour classes are
singletons, every other class has order at least two, so

\[
                         d\ge h+2(r-h)=2r-h.
\]

Now apply Theorem 2.4.  \(\square\)

For (HC_7), where (r=6), this produces haven orders at least five,
four and three at vertices of degrees seven, eight and nine,
respectively.  Thus the same separator invariant extends beyond the
degree-seven Moser laboratory without a new neighbourhood
classification.

## 3. Exact one-block traces from a critical apex

Now assume that every proper minor of (G) is (r)-colourable.  Let
(I\subseteq N) be an independent set satisfying

\[
                         |N-I|=r-1.                \tag{3.1}
\]

The set (I) is nonempty: otherwise (|N|=r-1), and any
(r)-colouring of (G-v) would leave a colour available for (v).

Contract the connected star (G[\{v\}\cup I]) to a vertex (z) and
colour the resulting proper minor with (r) colours.  Expanding away
from (v) gives a colouring (c) of (H).

### Lemma 3.1 (exact trace)

In this colouring,

* every vertex of (I) has the colour of (z);
* no vertex of (N-I) has that colour; and
* the (r-1) vertices in

\[
                              U:=N-I               \tag{3.2}
\]

have pairwise distinct colours, each of which occurs exactly once on
(N).

#### Proof

Every vertex of (N-I) is adjacent to (z) in the contracted minor,
so it avoids (c(z)).  If the (r-1) vertices of (N-I) did not use
all other (r-1) colours, then fewer than (r) colours would occur on
(N), and the missing colour could be assigned to (v).  Thus they use
the other colours bijectively.  The only remaining vertices of (N)
are those of (I), all coloured (c(z)), proving uniqueness on all of
(N).  \(\square\)

For a least-parameter Hadwiger counterexample, (3.1) is exactly the
Dirac equality cell

\[
 d(v)=t+s,\qquad r=t-1,\qquad |I|=s+2.
\]

### Theorem 3.2 (the colour haven)

For every (X\subseteq V(H)) with (|X|<r-1), there is a unique
component

\[
                         \beta_c(X)\text{ of }H-X             \tag{3.3}


containing every (u\in U) whose colour is absent from (c(X)).  The
assignment (X\mapsto\beta_c(X)) is a haven of order (r-1): whenever

\[
                         X\subseteq Y,qquad |Y|<r-1,
\]

one has

\[
                         \beta_c(Y)\subseteq\beta_c(X).       \tag{3.4}

Moreover

\[
 |U\cap V(\beta_c(X))|\ge r-1-|c(X)|\ge r-1-|X|. \tag{3.5}
\]

#### Proof

Since (|c(X)|\le |X|\le r-2), at least two palette colours are absent
from (c(X)).  At most one of these is the repeated colour on (I), so
at least one is the unique colour of a vertex of (U).  Corollary 2.3
therefore gives the unique component in (3.3), and the same corollary
puts all (r-1-|c(X)|) unique-colour roots outside (c(X)) in it.

If (X\subseteq Y), choose a unique-colour root (u\in U) whose colour
is absent from (c(Y)); such a root exists by the preceding count.  It
lies in both \(\beta_c(Y)\) and \(\beta_c(X)\).  A component of (H-Y)
is contained in a component of (H-X), so (3.4) follows.  \(\square\)

### Corollary 3.3 (separator capacity inequality)

For every separation ((A,B)) of (H), with (X=A\cap B),

\[
 \min\{|U\cap(A-B)|,|U\cap(B-A)|\}\le |c(X)|\le |X|. \tag{3.6}
\]

Thus the (r-1) uniquely coloured neighbours are node-well-linked in
the exact cut sense: deleting (p) vertices leaves a component
containing at least (r-1-p) of them.

## 4. Comparison with the haven carried by a clique model

Let

\[
                         \mathcal B=(B_1,\ldots,B_r)            \tag{4.1}


be a (K_r)-model in (H).  For (|X|<r), at least one branch bag is
disjoint from (X); all bags disjoint from (X) lie in one component
of (H-X), since every two such bags retain an edge between them.  Let

\[
                         \beta_M(X)                              \tag{4.2}


be that component.  These components form the standard model haven of
order (r).

### Theorem 4.0 (full-palette model alignment or a coloured adhesion)

At least one of the following holds.

1. **Palette-polarized adhesion.**  There is a set
   (X\subseteq V(H)), (|X|<r), and two distinct components
   (K,M) of (H-X) such that

   \[
   [r]-c(X)\subseteq c(N\cap K),qquad M=\beta_M(X),          \tag{4.2a}
   \]

   while (M) omits at least one colour in ([r]-c(X)) on its
   (N)-vertices.  The component (K) contains at least
   (r-|c(X)|) distinct neighbourhood vertices, and (M) contains
   all (r-|X|) model bags disjoint from (X).

2. **Coloured gammoid alignment.**  There are (r) pairwise
   vertex-disjoint paths, starting at (r) vertices of (N) having
   pairwise distinct colours and ending at a transversal containing
   one vertex of every model bag.  Truncating at first model hits either
   gives an (N)-meeting (K_r)-model or gives one bag two distinct
   (N)-roots through disjoint model-free prefixes.

#### Proof

Suppose outcome 1 fails.  By Theorem 2.2, this means that for every
(X\subseteq V(H)), (|X|<r), the model-haven component itself
contains an (N)-vertex of every colour outside (c(X)).

Form a directed auxiliary graph by replacing every edge of (H) with
its two orientations.  Add an artificial source vertex (s_\gamma)
for every colour (gamma\in[r]), with arcs from (s_\gamma) to all
vertices of (N) having colour (gamma), and no arcs into
(s_\gamma).  Let (S=\{s_\gamma:\gamma\in[r]\}).  We claim that for
every (J\subseteq[r]), (|J|=j), there are (j) vertex-disjoint
paths from (S) to \(\bigcup_{i\in J}B_i\).

Otherwise directed set-Menger gives a hitting set (Z) of order (p<j).  Put

\[
 C=\{\gamma:s_\gamma\in Z\},\qquad X=Z\cap V(H).
\]

Then (|C|+|X|=p<j\le r).  Some bag (B_i), (i\in J), is disjoint
from (X), and hence lies in \(\beta_M(X)\).  Since

\[
 |C\cup c(X)|\le |C|+|X|=p<r,
\]

choose a colour (gamma\notin C\cup c(X)).  Full-palette alignment
puts a vertex (n_\gamma\in N\cap\beta_M(X)) of colour (gamma).
Neither (s_\gamma) nor (n_\gamma) lies in (Z), and their edge
followed by a path inside \(\beta_M(X)\) to (B_i) avoids (Z), a
contradiction.

Thus the strict gammoid from the source set (S) in this directed graph
has rank at least (|J|) on
every union of a subfamily of the bags.  Rado's transversal theorem
gives one representative of each of the (r) bags linked by (r)
disjoint paths from (S).  All (r) artificial sources are used.
Delete their first edges: the resulting paths start at distinct
(N)-vertices, one of each colour.

Truncate these paths at their first model vertices.  If the (r)
first-hit bag labels are distinct, they exhaust all (r) bags; adjoining
the prefixes gives an (N)-meeting model.  Otherwise two paths first hit
one bag at distinct vertices, and adjoining those two prefixes gives the
stated multiply rooted bag.  In either case connectedness, disjointness,
and every old interbag edge are preserved.  \(\square\)

The artificial colour sources are essential.  They make the Menger cut
pay one unit for suppressing an entire neighbourhood colour.  Contracting
old model bags to unit sink vertices would additionally forbid transit
through them, but a cut of such a quotient charges a whole bag as one
unit and need not lift to an ordinary vertex separator.  The theorem
therefore stops honestly at the multiply rooted bag outcome.

### Corollary 4.0a (six-connectivity forces a double foot in (HC_7))

If (H) is (r)-connected, outcome 1 of Theorem 4.0 is impossible.
Consequently every (K_r)-model in (H) can either be made
(N(v))-meeting or can be augmented so that one bag contains two
distinct neighbours of (v), reached by disjoint model-free prefixes.

For a hypothetical minimal counterexample to (HC_7), the graph
(H=G-v) is six-connected and contains a (K_6)-model by (HC_6).
An (N(v))-meeting model would give a (K_7)-minor after adding the
singleton bag ({v}).  Hence every surviving model has the explicit
double-foot outcome.  This conclusion has no degree assumption on
(v); the degree-seven, eight and nine private-root counts refine it
through Theorem 4.1.

#### Proof

The polarized alternative deletes fewer than (r) vertices and leaves
two distinct components, contrary to (r)-connectivity.  Apply outcome
2 and its first-hit conclusion.  The (HC_7) specialization uses the
audited inequality (kappa(G-v)\ge6).  \(\square\)

### Lemma 4.0b (a minimum palette polarization is a rainbow gate)

Assume the palette-polarized outcome of Theorem 4.0 and choose (X)
of minimum order for which the model-haven component
(M=\beta_M(X)) omits a colour outside (c(X)).  Put

\[
 L=[r]-\bigl(c(X)\cup c(N\cap M)\bigr).                       \tag{4.2b}
\]

Then (L\ne\varnothing), and for every (x\in X) and every
(gamma\in L), the graph (H-(X-\{x\})) contains an
(M)-to-(N_\gamma) path through (x), where
(N_\gamma=\{u\in N:c(u)=\gamma\}).  In particular, every (x)
has a neighbour in (M), and for each (gamma\in L) it has a
neighbour in a component of (H-X) containing an (N_\gamma)-vertex.

#### Proof

Fix (x\in X).  By minimality of (X), the model-haven component
(\beta_M(X-\{x\})) contains an (N)-vertex of every colour outside
(c(X-\{x\})).  It contains (M) by haven nesting.  For
(gamma\in L), we have (gamma\notin c(X-\{x\})), so this larger
component contains a vertex of (N_\gamma).

No such vertex lies in (M) by the definition of (L).  Therefore a
path in \(\beta_M(X-\{x\})\) from (M) to (N_\gamma) must use the
only restored vertex (x).  Taking a shortest such path shows that
(x) has a neighbour on the (M)-side and a neighbour in the
(H-X) component containing its (N_\gamma) end.  This holds for
every (gamma\in L).  \(\square\)

Thus failure of coloured rooting is not an unstructured separator: at
a minimum failure every adhesion vertex is simultaneously a portal from
the model core toward every missing neighbourhood colour.  The remaining
issue is whether these colour gates can be assigned to distinct branch
bags without consuming a uniquely necessary model portal.

### Theorem 4.1 (uniform root-or-polarized-adhesion dichotomy)

Let $U_c$ be the set of private-colour roots from (2.5), and put
$h=|U_c|>0$.  Exactly one of the following alternatives occurs.

1. **Polarized adhesion.**  For some $X\subseteq V(H)$ with
   $|X|\le h-1$, the components $\beta_c(X)$ and $\beta_M(X)$ are
   distinct.  They are separated by $X$, and respectively contain

   \[
   h-|X|\quad\hbox{private-colour roots, and}\quad r-|X|
   \quad\hbox{untouched model bags}                 \tag{4.3}
   \]

   (with the first lower bound sharpened to $h-|c(X)|$).

2. **Full gammoid rank up to $h$.**  The two havens agree on every
   set of order below $h$.  Then, for every $J\subseteq[r]$ with
   $|J|\le h$, there are $|J|$ pairwise vertex-disjoint paths from
   $U_c$ to

   \[
                           \bigcup_{j\in J}B_j.       \tag{4.4}
   \]

   Consequently, for every prescribed $h$ branch bags there is a
   transversal, one vertex in each prescribed bag, which is linked to
   all of $U_c$ by $h$ pairwise vertex-disjoint paths.

#### Proof

If the havens differ, (4.3) follows from (2.7) and from the fact that
at most $|X|$ disjoint bags can meet $X$.

Assume they agree.  Fix $J$ of order $j\le h$.  If fewer than $j$
disjoint $U_c$-to-$\bigcup_{j\in J}B_j$ paths existed, the set form of
Menger's theorem would give a hitting set $X$ of order $p<j\le h$.
At most $p$ of the disjoint bags indexed by $J$ meet $X$, so some
$B_i$, $i\in J$, is disjoint from $X$ and lies in $\beta_M(X)$.  On
the other hand, $\beta_c(X)$ contains a root of $U_c-X$.  Equality of
the two haven components gives a path in $H-X$ from that root to
$B_i$, contradicting that $X$ hits every path from $U_c$ to the target
union.  This proves the rank inequality in (4.4).

Let $M_U$ be the gammoid on $V(H)$ in which a set is independent when
it is linkable from $U_c$.  The rank inequalities just proved say

\[
 \operatorname{rk}_{M_U}\!\left(\bigcup_{j\in J}B_j\right)\ge |J|
                                                               \tag{4.5}
\]

for every subfamily of any prescribed $h$ bags.  Rado's matroidal
transversal theorem supplies one representative from each bag whose
set is independent in $M_U$.  Since it has order $|U_c|=h$, the
linkage uses all roots of $U_c$.  \(\square\)

### Corollary 4.2 (exact equality-cell form)

Under Lemma 3.1, $h=r-1$ and $U_c=U$.  Thus the polarized adhesion has
order at most $r-2$ and the two shores in (4.3) contain at least
$r-1-|X|$ unique roots and $r-|X|$ untouched model bags.  In the
nonpolarized outcome, all $r-1$ unique roots link into a transversal
of any prescribed $r-1$ model bags.

### Lemma 4.3 (a minimum polarized adhesion has two full shores)

Assume outcome 1 of Theorem 4.1, and choose (X) of minimum order for
which the colour and model haven components differ.  Put

\[
                         C=\beta_c(X),\qquad M=\beta_M(X).
\]

Then

\[
                         N_H(C)=X=N_H(M).                       \tag{4.6}
\]

Thus the polarized outcome can be chosen as an exact two-full-shore
adhesion, not merely an arbitrary separator.  It retains the capacity
bounds (h-|c(X)|) private roots in (C) and (r-|X|) untouched
model bags in (M).

#### Proof

The inclusions (N_H(C),N_H(M)\subseteq X) hold because (C,M) are
components of (H-X).  Suppose some (x\in X) has no neighbour in
(C).  On restoring (x), the component (C) does not merge with any
other component.  The colour haven for (X-\{x\}) still contains the
private roots already in (C); any additional private root whose colour
is freed by removing (x) must lie in that same component by Theorem
2.4.  Hence \(\beta_c(X-\{x\})=C\).

The model-haven component for (X-\{x\}) contains (M).  It cannot
merge with (C) through (x), since (x) has no neighbour in (C).
Thus the two havens already differ at (X-\{x\}), contrary to the
minimum choice of (X).  Therefore every (x\in X) has a neighbour in
(C).  The symmetric argument, interchanging the two havens, shows that
every (x\in X) has a neighbour in (M), proving (4.6).  \(\square\)

### Corollary 4.4 (connectivity kills the polarized branch)

If (H) is (h)-connected, only outcome 2 of Theorem 4.1 can occur.
Hence all (h) private-colour roots have a disjoint-path transversal
into any prescribed (h) bags of the (K_r)-model.

In particular, let (G) be a hypothetical minimal counterexample to
(HC_7).  The audited seven-connectivity of (G) gives
(kappa(G-v)ge6).  With (r=6), Corollary 2.5 and Theorem 4.1 give:

Here the (K_6)-model in (G-v) is supplied by the already established
(HC_6).

\[
\begin{array}{c|c|c}
d_G(v)&\text{private roots in every six-colouring of }G-v
      &\text{bags met by a disjoint-path transversal}\\ \hline
7&\ge5&\text{any prescribed }5\text{ of the }6\text{ bags},\\
8&\ge4&\text{any prescribed }4\text{ of the }6\text{ bags},\\
9&\ge3&\text{any prescribed }3\text{ of the }6\text{ bags}.
\end{array}                                                    \tag{4.7}
\]

These are path-transversal statements in the full graph (G-v), not
yet clean branch-set contacts; paths which transit another model bag
lead to the first-hit alternatives below.

### Corollary 4.5 (first-hit contact or split certificate)

Assume the second outcome of Theorem 4.1.

Fix $J\subseteq[r]$, $|J|=j\le h$, and take the $j$ disjoint
paths supplied by (4.4).  Truncate every path at its first vertex in
the union of the model bags.  The truncated paths have pairwise
disjoint, model-free interiors.  At least one of the following holds.

1. Their first-hit bags are precisely the $j$ distinct bags indexed
   by $J$; this is a clean $U_c$-to-$J$ contact linkage.
2. Some first-hit bag is indexed outside $J$; this is an exchange
   contact into a previously untargeted bag.
3. Two paths first hit the same bag at distinct vertices; this is a
   double-hit portal certificate in that bag.  This includes the case
   in which two private roots already lie in the same old bag.

#### Proof

The first-hit label map from the $j$ paths to $[r]$ is either
injective or not.  If it is not, outcome 3 holds.  If it is injective,
its image has order $j$; that image is either $J$, giving outcome
1, or contains an index outside (J), giving outcome 2.  Truncation
preserves path disjointness.  A path which begins in a model bag simply
has a trivial first-hit prefix.  \(\square\)

For a contact-maximal model, an exchange hit on a noncontact bag raises
the number of contacted bags, while a hit on a bag already containing a
neighbour of (v) is a multiply rooted bag.  Thus a relative Hall deficit
cannot remain a purely abstract path failure: either the colour and model
havens are separated by the
polarized adhesion of Theorem 4.1, or the deficit is witnessed inside a
specific transit bag by an exchange/double-hit state.

### Corollary 4.6 (private-root contact or a multiply rooted bag)

Assume outcome 2 of Theorem 4.1.

Then the old (K_r)-model can be augmented so that either

1. (h) distinct bags contain (h) distinct roots of (U_c); or
2. one bag contains two distinct roots of (U_c), reached by two
   disjoint prefixes whose interiors avoid every old model bag (a prefix
   may be trivial when its root already lies in that bag).

#### Proof

Apply Theorem 4.1 to any (h) target bags, and truncate the resulting
paths at their first model hits.  If the first-hit labels are distinct,
adjoin each prefix to its first-hit bag.  The prefixes are disjoint and
model-free internally, so all bags remain disjoint and connected and all
old clique-model adjacencies survive.  This gives outcome 1.

If two first-hit labels coincide, adjoin both corresponding prefixes to
that bag.  Their roots and their first-hit vertices are distinct by path
disjointness.  This gives outcome 2, again without changing any old
interbag adjacency.  \(\square\)

For (HC_7), Corollary 4.4 therefore yields the following label-free
normal forms:
degree seven gives five distinctly contacted bags or a multiply rooted
bag; degrees eight and nine give the analogous numbers four and three.
This is a contact/split theorem for an infinite family of model
placements, not a finite neighbourhood enumeration.

## 5. Two-state orientation coherence and colour gluing

For an (r)-colouring (c) of (H), let

\[
 \mu(c)=\bigl|\{\gamma\in[r]:
        \gamma\text{ occurs at least twice on }N(v)\}\bigr|  \tag{5.1}
\]

be the number of nonprivate neighbourhood colours.

### Theorem 5.1 (opposite orientations glue)

Let ((A,B)) be a separation of (H), with open shores
(D=A-B), (E=B-A), and adhesion (X=A\cap B).  Let (c,d) be
proper (r)-colourings of (H) which induce the same equality
partition on (X).  Suppose the private-colour haven of (c) points
into (D), while the private-colour haven of (d) points into (E):

\[
             \beta_c(X)\subseteq D,qquad
             \beta_d(X)\subseteq E.                         \tag{5.2}
\]

(Both havens are assumed defined at (X).)  Then necessarily

\[
                         |c(X)|+\mu(c)+\mu(d)\ge r.           \tag{5.3}
\]

#### Proof

Because the two restrictions have the same equality partition, permute
the palette of (d) so that (d(x)=c(x)) for every (x\in X).
This preserves (mu(d)), private colours, and the component in (5.2).
Put (C_X=c(X)=d(X)).

Use (d) on (D\cup X) and (c) on (E\cup X).  These colourings
agree on (X), and no edge joins (D) to (E), so their union is a
proper (r)-colouring of (H).

Every private (d)-colour outside (C_X) has its unique
neighbourhood occurrence in \(\beta_d(X)\subseteq E\), and hence is
absent from (N\cap D).  Thus the (d)-colours on (N\cap D) which
are outside (C_X) belong to the at most (mu(d)) nonprivate
colours.  Symmetrically, the (c)-colours on (N\cap E) outside
(C_X) belong to the at most (mu(c)) nonprivate colours.
Consequently the hybrid colouring uses at most

\[
                         |C_X|+\mu(c)+\mu(d)
\]

colours on (N).  If this number were below (r), a missing colour
could be assigned to (v), contradicting the non-(r)-colourability
of (G).  This proves (5.3).  \(\square\)

### Corollary 5.2 (exact traces have coherent orientation)

Let (c,d) be two exact one-block traces from Lemma 3.1.  Then
$\mu(c),\mu(d)\le1$, with equality for a trace exactly when its repeated
block has at least two vertices.  If they induce the same equality partition on an
adhesion (X) with

\[
                              |c(X)|\le r-3,                  \tag{5.4}
\]

their colour havens cannot point to opposite open shores.

In particular, on an adhesion of order at most (r-3), every repeated
boundary state among exact star-contraction traces has a coherent
orientation.  This is an exact colour-gluing restriction on separator
states; it does not assume that either side contains a rooted clique
model.

## 6. What this does and does not close

Theorem 4.1 is an actual uniform root-or-separator theorem, not a
restatement of the desired (N(v))-meeting clique model:

* the separator alternative gives a labelled adhesion of order below
  $h$ with quantitative capacity on both shores;
* the other alternative proves all Hall rank inequalities through order
  $h$ and an $h$-path transversal into any $h$ model bags.

In the exact equality cell, $h=r-1$, giving the sharper values stated
in Corollary 4.2.

The remaining branch-set issue is sharply smaller but genuine.  A
linkage path to its prescribed bag may run through another model bag.
Absorbing all paths into the old model can therefore split a bag or
destroy one of its labelled adjacencies.  The theorem deliberately does
not call the resulting path system a rooted (K_{r-1})-model.  A
label-preserving model-cleaning lemma, or a proof that a transit bag
creates a splittable capacity packet, is still required.

In the polarized branch, the audited nested-cut transport theorem applies
once the adhesion is chosen inside a nested contact shore: the colour
roots and all but (|X|) clique bags now lie on prescribed opposite
sides, rather than merely being separated by an unlabelled minimum cut.
The new input is the palette permutation invariant (2.1), which forces
all uniquely coloured roots through a single component and cannot be
obtained from connectivity alone.
