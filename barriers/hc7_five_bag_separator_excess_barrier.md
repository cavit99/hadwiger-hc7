# An infinite barrier to geometry-only five-branch-set separator bounds

**Status:** explicit infinite counterexample family to the false principle
stated below.  The construction is not a counterexample to `HC_7`.

This note records a sharp limitation of the five-branch-set-supported
separation obtained in the conditional defect-one branch.  Seven-connectivity,
`K_7`-minor exclusion, a label-faithful `K_7^-` model, and even
edge-maximal `K_7`-minor exclusion do not bound the order of that separation.
Contraction-critical colouring data, or a terminal two-vertex transversal,
is indispensable.

## 1. The false principle

The following statement is false.

> **False five-branch-set separator principle.**  Let `G` be a
> seven-connected graph with no `K_7` minor.  Suppose that
> `B_1,...,B_5,L,R` are pairwise disjoint connected subgraphs such that:
>
> 1. `B_1,...,B_5` are pairwise adjacent;
> 2. each of `L,R` is adjacent to every `B_i`;
> 3. `L` and `R` are anticomplete; and
> 4. there is a connected set `X` containing `L`, disjoint and
>    anticomplete from `R`, with
>    \[
>                 N_G(X)\subseteq\bigcup_{i=1}^5 B_i.
>    \]
>
> Then `|N_G(X)|<=7` (or the displayed separation can be trimmed to order
> seven while preserving `X`, `R`, and retaining each of the five named
> branch sets in its entirety in the separator).

The graphs below have `|N_G(X)|=n+2` for arbitrary odd `n>=7`.  They also
fit exactly the four-labelled diamond setup used to derive the
five-branch-set-supported separation.

## 2. The capped antiprism

Fix an odd integer `n>=7`, with subscripts taken modulo `n`.  Define `H_n`
on

\[
       \{p,q\}\cup\{a_i:0\le i<n\}\cup\{b_i:0\le i<n\}
\]

by the following edges:

\[
\begin{aligned}
 &a_i a_{i+1},\qquad b_i b_{i+1},\\
 &p a_i,\qquad q b_i,\\
 &a_i b_i,\qquad a_{i+1}b_i
 \qquad(0\le i<n).
\end{aligned}                                                   \tag{2.1}
\]

Thus `H_n` is the graph of a capped `n`-antiprism.  It has a planar
embedding with the `a`-cycle and `b`-cycle bounding a triangulated annulus,
and with `p` and `q` capping its two boundary cycles.  It has `2n+2`
vertices and `6n=3(2n+2)-6` edges, so this embedding is a planar
triangulation.

Let

\[
                         G_n=K_2\vee H_n,                           \tag{2.2}
\]

and call the two adjacent universal vertices in the `K_2` part `s,t`.

### Proposition 2.1

The graph `H_n` is five-connected.

#### Proof

Let `S` be a set of at most four vertices.  We prove that `H_n-S` is
connected.

First suppose that neither `p` nor `q` belongs to `S`.  Every surviving
`a_i` is joined to every other surviving `a`-vertex through `p`, and the
analogous statement holds for the surviving `b`-vertices through `q`.
The cross edges in (2.1) form the cycle

\[
 a_0b_0a_1b_1\cdots a_{n-1}b_{n-1}a_0.                            \tag{2.3}
\]

Meeting every edge of this even cycle requires at least `n` vertices.
Since `|S|<=4<n`, a cross edge survives.  It joins the `p`-component to
the `q`-component, so `H_n-S` is connected.

Next suppose, by symmetry, that `q` belongs to `S` and `p` does not.  Put
`S'=S-{q}`, so `|S'|<=3`.  All surviving `a`-vertices belong to the
component containing `p`.  If another component existed, it would contain
a maximal nonempty interval

\[
                       b_i,b_{i+1},\ldots,b_j                     \tag{2.4}
\]

of the surviving `b`-cycle and no `a`-vertex.  If
`1<=|I|<=n-2`,
its two boundary vertices `b_{i-1},b_{j+1}` must lie in `S'`, and all its
`|I|+1` distinct `a`-neighbours

\[
                       a_i,a_{i+1},\ldots,a_{j+1}                  \tag{2.5}
\]

must also lie in `S'`.  This requires at least `|I|+3>=4` vertices, a
contradiction.  If `|I|=n-1`, the two cyclic boundary positions coincide,
but the sole missing `b`-vertex and all `n` distinct `a`-neighbours must
lie in `S'`, requiring `n+1>3` deletions.  If the interval is the whole
`b`-cycle, avoiding all
`a`-neighbours requires all `n` `a`-vertices in `S'`, again impossible.

Finally suppose that both `p,q` belong to `S`.  At most two vertices have
then been deleted from the alternating cycle (2.3).  Deleting zero or one
vertex leaves it connected.  If two nonadjacent vertices are deleted, the
cycle leaves two paths; but the two neighbours of each deleted `a_i` on
(2.3) are `b_{i-1},b_i`, which are adjacent, and the two neighbours of
each deleted `b_i` are `a_i,a_{i+1}`, which are adjacent.  A surviving
same-cycle edge therefore bridges the two paths.  If the two deleted
vertices are adjacent on (2.3), what remains is already one path.  Hence
the ring is connected in all cases.

Thus no set of at most four vertices disconnects `H_n`.  (The ring
vertices have degree five, so its connectivity is exactly five.)
\(\square\)

### Corollary 2.2

The graph `G_n` is seven-connected.

#### Proof

Any separator between two vertices of `H_n` must contain both universal
vertices `s,t`; after deleting them it must still contain a separator of
`H_n`.  Conversely, `\{s,t\}` together with a five-cut of `H_n` is a
cut of `G_n`.  Proposition 2.1 therefore gives

\[
                          \kappa(G_n)=2+\kappa(H_n)=7.
\]

\(\square\)

## 3. Minor exclusion and chromatic number

### Proposition 3.1

The graph `G_n` has no `K_7` minor.

#### Proof

Suppose seven pairwise disjoint connected branch sets formed a `K_7`
minor model in `G_n`.  At most two of those branch sets can meet
`\{s,t\}`: disjointness assigns each of the two vertices to at most one
branch set.  Hence at least five branch sets lie wholly in `H_n`.  Their
pairwise model adjacencies are edges of `H_n`, because the only edges added
in (2.2) are incident with `s` or `t`.  Those five branch sets would form a
`K_5` minor in the planar graph `H_n`, impossible.  \(\square\)

### Proposition 3.2

The graph `G_n` is six-chromatic, not seven-chromatic.

#### Proof

The planar graph `H_n` is four-colourable.  It contains the odd wheel
formed by `p` and the odd `a`-cycle, so it is not three-colourable.  Thus
`chi(H_n)=4`.  Chromatic number is additive under join, and hence

\[
                          \chi(G_n)=2+\chi(H_n)=6.
\]

\(\square\)

There is also a useful saturation strengthening.  The graph `G_n` is
edge-maximal `K_7`-minor-free.  Indeed, `H_n` is a maximal planar graph.
For every nonedge `e` of `H_n`, the graph `H_n+e` remains five-connected
and is nonplanar.  Theorem 1.1 of He, Wang and Yu,
[The Kelmans--Seymour conjecture IV: a proof](https://arxiv.org/abs/1612.07189),
states that every five-connected nonplanar graph contains a subdivision of
`K_5`.  Thus `H_n+e` has a `K_5` minor.  Every nonedge of `G_n` lies in
`H_n`, because `s,t` are universal, and the resulting `K_5` minor together
with the singleton branch sets `\{s\},\{t\}` is a `K_7` minor of `G_n+e`.

## 4. The labelled near-complete model and large separation

Partition the `a`-cycle into three nonempty consecutive arcs

\[
                              P_1,P_2,P_3.                           \tag{4.1}
\]

Each `P_i` is connected, and the three arcs are pairwise adjacent: the
three cut edges of the cycle join each consecutive pair, including the
first and last arcs.  Put

\[
                         R=\{q\}\cup\{b_i:0\le i<n\}.              \tag{4.2}
\]

The seven connected subgraphs

\[
            \{s\},\ \{t\},\ P_1,\ P_2,\ P_3,\ \{p\},\ R           \tag{4.3}
\]

form a `K_7^-`-minor model whose unique missing adjacency is `\{p\}R`.
Indeed, the first five sets form a `K_5` model; `p` is adjacent to every
`a`-arc; and every `a`-arc has a cross edge to the connected set `R`.
The universal vertices supply the remaining adjacencies.  On the other
hand, `p` has no neighbour in `R`.

This model is exactly a four-labelled diamond of the kind used in the
defect-one separation theorem.  Take the three anchors to be

\[
                         \{s\},\ \{t\},\ P_1,
\]

and take the four properly and distinctly labelled two-tree vertices to
be represented by

\[
                l=\{p\},\qquad r=R,\qquad m=P_2,\qquad n=P_3.
\]

Their contact graph is `K_4-lr`, which is a two-tree.  All seven represented
sets cover `V(G_n)`, so any attachment-clique condition for components
outside their union holds vacuously.

Now take `X=\{p\}`.  Its full neighbourhood is

\[
                     N_{G_n}(X)=\{s,t\}\cup\{a_i:0\le i<n\}
                              =\{s\}\cup\{t\}\cup P_1\cup P_2\cup P_3.
                                                                    \tag{4.4}
\]

The graph outside `X\cup N(X)` is exactly the nonempty connected set `R`,
and it is anticomplete to `X`.  Thus (4.4) is precisely a
five-branch-set-supported separator, but

\[
                              |N_{G_n}(X)|=n+2.                     \tag{4.5}
\]

This order is unbounded.  Moreover, any separation whose open near side is
the singleton `X` must contain all of `N(X)`, so it cannot be trimmed to
order seven while retaining that side.  Retaining all five named common
branch sets in the separator likewise retains every vertex in (4.4).

The portal distribution inside the three nonsingleton common branch sets
is already maximally rich.  The pole `p` is adjacent to every vertex of
each `P_i`.  Every `a_j` also has a neighbour in `R` (indeed both
`b_{j-1}` and `b_j` lie in `R`).  Thus the two pole-attachment sets in each
`P_i` are both the whole branch set.  Multiple, coincident, or distributed
portal contacts alone still do not permit a split repairing the missing
`pR` adjacency.

There are also many equivalent labelled models in the same host.  Moving
the three cut edges that define the cyclic arcs in (4.1) transfers boundary
vertices between adjacent branch sets while preserving connectedness,
every model adjacency, the quotient `K_7^-`, and the separator (4.4).
The cyclic space of such arc partitions contains rotation cycles.  Hence a
quantity depending only on the quotient contact graph, the five labels, or
the separator order cannot be a strict rank for these model rotations.
This observation does not claim that the rotations are legal
contraction-critical state transitions.

## 5. Exact scope of the barrier

The family satisfies all of the following:

1. seven-connectivity;
2. `K_7`-minor exclusion, even edge-maximal `K_7`-minor exclusion;
3. a label-faithful `K_7^-` model with a named common `K_5`;
4. two anticomplete connected pole sides;
5. a separator supported on the five common branch sets, of arbitrarily
   large order; and
6. the attachment-clique conclusion used by the conditional two-tree
   argument (vacuously, because the model covers the host).

It does **not** satisfy the decisive counterexample hypotheses:

1. `G_n` is six-chromatic, not seven-chromatic;
2. it is not a seven-contraction-critical graph;
3. the labelled model is not supplied with the adjacent-pair proper-minor
   colouring provenance of the active `HC_7` programme; and
4. there is no obstruction to a global two-vertex terminal outcome:
   `\{s,t\}` meets every `K_5` minor model, because
   `G_n-\{s,t\}=H_n` is planar and hence has no `K_5` minor.

Consequently this family is not evidence against the conditional
exchange-or-gluing theorem with its full minor-critical hypotheses.  It
shows exactly what that theorem must use.  A valid next theorem must either

* allow the global two-vertex `K_5`-minor-transversal (or coherent
  two-apex) outcome; or
* use contraction-critical colourings and their literal attachment data to
  exclude the capped-antiprism geometry, reduce the separator excess, or
  align the two shore colourings.

Pure connectivity, edge-maximal `K_7`-minor-freeness, and branch-set
geometry cannot do this work.
