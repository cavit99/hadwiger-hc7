# A uniform coloured-model-haven dichotomy

## 1. Setup

Let $r\ge2$.  Let $G$ be a graph which is not $r$-colourable, let
$v\in V(G)$, and suppose

\[
                         H=G-v
\]

has a proper $r$-colouring $c$.  Put $N=N_G(v)$.  Every colour occurs
on $N$, since otherwise the missing colour could be assigned to $v$.

Let

\[
                         \mathcal B=(B_1,\ldots,B_r)             \tag{1.1}
\]

be a $K_r$-model in $H$.

## 2. A whole free palette lives in one component

### Lemma 2.1 (component palette concentration)

For every $X\subseteq V(H)$ with $H-X\ne\varnothing$, some component
$K$ of $H-X$ satisfies

\[
                         [r]-c(X)\subseteq c(N\cap K).          \tag{2.1}
\]

#### Proof

Let $K_1,\ldots,K_m$ be the components of $H-X$, put
$F=[r]-c(X)$, and let

\[
                         P_i=c(N\cap K_i)\cap F.
\]

Independently permute the colours in $F$ on each $K_i$, fixing every
colour in $c(X)$.  This preserves properness: different components are
anticomplete, and a palette permutation fixing the boundary colours
preserves every $K_i$--$X$ edge.

Let $a=\max_i|P_i|$, choose an $a$-element set $Q\subseteq F$, and on
each component choose a permutation sending $P_i$ into $Q$.  The
resulting proper colouring of $H$ uses at most

\[
                              |c(X)|+a
\]

colours on $N$.  Since $G$ is not $r$-colourable, this number is at
least $r$.  As $a\le|F|=r-|c(X)|$, equality holds and some
$P_i=F$.  That component is $K$.  \(\square\)

For $|X|<r$, define the **model component** $M(X)$ to be the component
of $H-X$ containing all branch bags disjoint from $X$.  It is
well-defined: at most $|X|$ bags meet $X$, and every two untouched bags
retain their model edge.

## 3. Rooting, a double foot, or a coloured adhesion

### Theorem 3.1 (coloured-model-haven dichotomy)

At least one of the following holds.

1. **Palette-polarized adhesion.**  There is $X\subseteq V(H)$ with
   $|X|<r$ and a component $K\ne M(X)$ of $H-X$ such that

   \[
   [r]-c(X)\subseteq c(N\cap K),                              \tag{3.1}
   \]

   while $M(X)$ omits some colour in $[r]-c(X)$ on its
   $N$-vertices.  The two components contain at least
   $r-|c(X)|$ distinctly coloured neighbours of $v$ and
   $r-|X|$ untouched model bags, respectively.

2. **Rooted contact.**  The model can be augmented to an
   $N$-meeting $K_r$-model.

3. **Double foot.**  The model can be augmented so that one bag
   contains two distinct vertices of $N$, reached by two disjoint
   prefixes whose internal vertices avoid every old model bag.

#### Proof

Assume outcome 1 fails.  Lemma 2.1 then says that, for every
$X\subseteq V(H)$ of order below $r$, the model component $M(X)$
contains an $N$-vertex of every colour outside $c(X)$.

Form a directed graph by replacing every edge of $H$ with its two
orientations.  For every colour $\gamma\in[r]$, add an artificial
source $s_\gamma$, with arcs from $s_\gamma$ to all vertices of $N$
coloured $\gamma$ and no arcs into $s_\gamma$.  Let
$S=\{s_\gamma:\gamma\in[r]\}$.

For every $J\subseteq[r]$, $|J|=j$, there are $j$ vertex-disjoint
directed paths from $S$ to $\bigcup_{i\in J}B_i$.  Otherwise directed
set-Menger gives a hitting set $Z$ of order $p<j$.  Put

\[
 C=\{\gamma:s_\gamma\in Z\},\qquad X=Z\cap V(H).
\]

Then $|C|+|X|=p<j\le r$.  Some bag $B_i$, $i\in J$, is disjoint
from $X$ and lies in $M(X)$.  Moreover

\[
                         |C\cup c(X)|\le p<r,
\]

so choose $\gamma\notin C\cup c(X)$.  By the assumed alignment,
$M(X)$ contains a vertex $n_\gamma\in N$ of colour $\gamma$.
Neither $s_\gamma$ nor $n_\gamma$ lies in $Z$, and the arc
$s_\gamma n_\gamma$ followed by a path inside $M(X)$ to $B_i$ avoids
$Z$, a contradiction.

Thus the strict gammoid from $S$ has rank at least $|J|$ on every
union of a subfamily of the bags.  Rado's matroidal transversal theorem
supplies one representative from each of the $r$ bags linked by $r$
vertex-disjoint paths from $S$.  All $r$ sources are used.  Deleting
their first arcs gives disjoint paths starting at distinct vertices of
$N$, one of each colour, and ending in a transversal of all bags.

Truncate every path at its first old model vertex.  If the $r$
first-hit bag labels are distinct, they exhaust all $r$ bags.  Adjoining
the model-free prefixes gives outcome 2.  Otherwise two paths first hit
one bag at distinct vertices; adjoining those prefixes gives outcome 3.
In both cases the enlarged bags remain disjoint and connected and every
old interbag edge survives.  \(\square\)

### Lemma 3.2 (minimum polarization is a rainbow gate)

Suppose outcome 1 holds, and choose $X$ of minimum order for which the
model component $M=M(X)$ omits a free colour.  Put

\[
 L=[r]-\bigl(c(X)\cup c(N\cap M)\bigr).                       \tag{3.2}
\]

Then $L\ne\varnothing$.  For every $x\in X$ and every
$\gamma\in L$, the graph $H-(X-\{x\})$ contains an
$M$--$N_\gamma$ path through $x$, where
$N_\gamma=\{u\in N:c(u)=\gamma\}$.  Hence every adhesion vertex
meets $M$ and, for each missing colour, a component containing a
neighbour of $v$ of that colour.

#### Proof

By minimality, $M(X-\{x\})$ contains an $N$-vertex of every colour
outside $c(X-\{x\})$.  It contains $M$ by model-haven nesting.  A
colour $\gamma\in L$ is absent from $c(X-\{x\})$ and from $N\cap M$.
Thus a path in $M(X-\{x\})$ from $M$ to an $N_\gamma$ vertex must use
the only restored vertex $x$.  A shortest such path gives the two
claimed portal incidences.  \(\square\)

## 4. Consequence for (HC_7)

### Corollary 4.1

Let $G$ be a hypothetical minimal counterexample to $HC_7$, fix
$v\in V(G)$, and let $mathcal B$ be any $K_6$-model in $G-v$.
Then either $G$ has a $K_7$-minor or $mathcal B$ can be augmented to
have a double-foot bag as in outcome 3 of Theorem 3.1.

#### Proof

Known $HC_6$ supplies the $K_6$-model, while audited
seven-connectivity gives

\[
                         \kappa(G-v)\ge6.
\]

The palette-polarized alternative would delete fewer than six vertices
and leave two components, impossible.  The rooted-contact alternative,
together with the singleton bag $\{v\}$, gives a $K_7$-model.  The only
remaining outcome is the double foot.  \(\square\)

This conclusion has no degree assumption and eliminates an infinite
family of contact-deficient models at once.  It does not yet split the
double-foot bag while retaining all five labelled interbag adjacencies.

## 5. Exact boundary of the theorem

The path transversal alone cannot be cleaned in general, even when all
$r$ roots link disjointly to all $r$ old bags.  The end-locked comb in
`hadwiger_linkage_model_cleaning_counterexample.md` is an explicit
infinite counterexample.  It fails the palette/model alignment through
a one-vertex cut, so it does not refute Theorem 3.1.

Contracting every old bag to a unit-capacity sink would force distinct
first-hit labels, but a cut in that quotient charges an arbitrarily
large bag as one unit and need not lift to an ordinary separator of
$H$.  The remaining uniform step is therefore exact: use the rainbow
gate structure of Lemma 3.2 (or the stronger minor-transition data) to
split a double-foot transit bag without destroying a labelled model
adjacency.
