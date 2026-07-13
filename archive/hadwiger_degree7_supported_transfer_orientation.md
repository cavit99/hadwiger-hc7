# A trace-independent support-orientation theorem at degree seven

## 1. General exact-trace setup

Let $G$ be a proper-minor-minimal counterexample to
$\mathrm{HC}_7$, let $d(v)=7$, and suppose $G-N[v]$ has two
components $C_1,C_2$. Let $r\subseteq N(v)$ be any independent
pair. Contracting the star $\{v\}\cup r$ gives an exact six-colouring
whose other five boundary vertices $U$ have distinct colours.

Let $F_r$ be the graph of missing edges of $G[U]$, and let $P_r$
be its disjointness graph: the vertices of $P_r$ are the edges of
$F_r$, and two are adjacent when their four ends are distinct. For
$e\in E(F_r)$, put $D_e=\{r,e\}$; for $ef\in E(P_r)$, put
$T_{ef}=\{r,e,f\}$. These symbols denote exact equality states on the
seven boundary vertices.

Every edge of $F_r$ is supported by at least one exterior component.
Label it $1$, $2$, or $B$ according as it is supported by $C_1$, by
$C_2$, or by both.

## 2. Transfer works for every degree-seven trace

### Lemma 2.1

If $e,f$ are adjacent in $P_r$ and both are supported by $C_s$, then

$$
T_{ef}\in\mathcal E_{3-s},
$$

where $\mathcal E_i$ is the exact boundary-state family extending to
$G[N\cup C_i]$.

### Proof

The supported bichromatic paths for $e,f$ are vertex-disjoint because
their four terminal colours are distinct. Join their nonempty interiors
by a shortest path in $C_s$, split the connector at an edge, and
contract the two resulting adjacent connected terminal blocks together
with the star $\{v\}\cup r$.

Let $w$ be the seventh boundary vertex, outside $r\cup e\cup f$.
Since $\alpha(G[N])\le2$, $w$ has a neighbour in each of the two
nonedges $e,f$: otherwise $w$ and the two ends of one of them would
be an independent triple. Hence the star image, the two path-block
images, and $w$ form a $K_4$. A six-colouring of the proper minor,
expanded on the retained boundary and opposite exterior component, has
the exact state $T_{ef}$. This is precisely the proof of the
pure-Moser transfer lemma, and it uses no special feature of the
$13$-trace. $\square$

## 3. The cross-support orientation obstruction

### Theorem 3.1

Let $K$ be the spanning subgraph of $P_r$ whose edges join a
$1$-labelled vertex to a $2$-labelled vertex; vertices labelled $B$
are isolated in $K$. In a counterexample, every connected component
of $K$ containing a $1$- or $2$-labelled vertex contains a cycle.
Moreover, no edge of $P_r$ has both ends labelled $B$.

### Proof

If a missing edge $e$ has label $1$, the one-swap state gives
$D_e\in\mathcal E_2$. Any edge $ef$ of $P_r$ for which $f$ has
label $1$ or $B$ is supported by $C_1$, so Lemma 2.1 gives
$T_{ef}\in\mathcal E_2$. Exact-state exclusivity therefore prevents
all those states from extending to side $1$. Two-anchor coverage of
$D_e$ on side $1$ must use a state $T_{ef}\in\mathcal E_1$ with
$f$ labelled $2$. Thus every $1$-vertex selects an incident edge
of $K$, owned by side $1$. Symmetrically, every $2$-vertex selects
an incident edge of $K$, owned by side $2$.

One edge of $K$ cannot be selected by both ends: its $1$-end would
require its triple state in $\mathcal E_1$, while its $2$-end would
require the same state in $\mathcal E_2$, contrary to exclusivity.
Consequently each component of $K$ has at least as many edges as
vertices, and hence contains a cycle.

Finally, a $BB$-edge of $P_r$ is supported on both sides. Lemma 2.1
would put its triple state in both extension families, again violating
exclusivity. $\square$

### Corollary 3.2

Suppose $P_r$ is connected and has maximum degree at most two.

1. If $P_r$ is a path or an odd cycle, no genuinely mixed support word
   exists; one exterior component supports every edge of $F_r$.
2. If $P_r$ is an even cycle, the only genuinely mixed words not
   excluded by these state axioms are the two alternating binary words.

### Proof

A path has no cyclic subgraph, so Theorem 3.1 permits no $1$- or
$2$-vertex. That is incompatible with a genuinely mixed word. If
$P_r$ is a cycle, the only subgraph containing a cycle is the whole
cycle. Hence a mixed survivor has no $B$-vertex and every edge joins
labels $1$ and $2$. Such a labelling exists exactly for an even
cycle, and then it is alternating. $\square$

## 4. Application to all ten pure-Moser traces

For the pure Moser spindle the ten traces split into three exact types:

$$
\begin{array}{c|c|c|c}
r&\text{number of traces}&F_r&P_r\\ \hline
05,06&2&K_{2,3}&C_6,\\
13,14,23,24&4&C_5&C_5,\\
15,25,36,46&4&\text{a }C_4\text{ with one pendant edge}&P_5.
\end{array}
$$

Thus every one of the eight $C_5/P_5$ traces is forced to be confined
to one exterior component. For the two $C_6$ traces, the only mixed
state patterns are alternating binary supports; every pattern containing
a bi-supported edge is eliminated.

The script `moser_all_trace_transfer_verify.py` reconstructs $F_r$ and
$P_r$ from the labelled Moser spindle, checks the $2+4+4$ type table,
and independently solves the finite exact-state system for all ten
repeated pairs. It reports no mixed survivor in the eight $C_5/P_5$
disjointness traces and exactly the two side-swapped alternating words
in each $C_6$ trace.

This theorem explains why supported-pair transfer closes the
two-component cell but not the sole-exterior cell. With one exterior
component all missing-edge paths are already confined; the unresolved
requirement is a connected sixth branch set joining the repeated pair
while avoiding the rooted $K_5$-model. State transfer alone does not
reserve that connector.
