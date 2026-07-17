# A rainbow-diamond separation in the defect-one two-tree

**Status:** written proof with a separate internal audit returning GREEN.

This note proves a structural consequence of the conditional defect-one
configuration.  It extracts a label-faithful `K_7^-`-minor model and an
actual host separation whose boundary is contained in five named branch
sets.  It does not bound that boundary from above, align colourings of its
two closed shores, or prove `HC_7`.

## 1. Fixed setup

Let `G` be a seven-connected graph with no `K_7` minor.  Let

\[
                         A_1,A_2,A_3                                      \tag{1.1}
\]

be pairwise disjoint, connected, pairwise adjacent vertex sets.  Let
`J` be a component-contact graph whose vertices represent pairwise
disjoint connected subgraphs of `G`, all disjoint from
`A_1\cup A_2\cup A_3`, and partitioned into four protected labels.
Two vertices of `J` are adjacent exactly when their represented
subgraphs are adjacent in `G`.  Assume that

1. every one of the four labels is represented, and vertices with the
   same label are nonadjacent;
2. `J` is a two-tree; and
3. every represented subgraph is adjacent to every set in (1.1).

Write `V_x` for the connected subgraph represented by $x\in V(J)$, and
put

\[
 \mathcal U=A_1\cup A_2\cup A_3\cup
             \bigcup_{x\in V(J)}V_x.                                \tag{1.2}
\]

Contracting the displayed sets gives the minor

\[
                              H=K_3\vee J.                            \tag{1.3}
\]

We also use the attachment-clique conclusion from the audited
defect-one normalization: for every component `W` of $G-\mathcal U$, the
vertices of `H` whose represented sets are adjacent to `W` induce a
clique in `H`.

In the defect-one application, the proper-label condition holds because
two components with the same protected label come from the same old
branch set and are therefore anticomplete.

## 2. A rainbow `K_4^-` in every four-labelled two-tree

### Lemma 2.1 (rainbow diamond)

The graph `J` has four vertices `l,r,m,n`, one of each protected label,
such that

\[
                J[\{l,r,m,n\}]=K_4-lr.                               \tag{2.1}
\]

In particular, `m,n` are the two common neighbours of the nonadjacent
poles `l,r` in this subgraph.

#### Proof

Fix a two-tree construction of `J`: start with a triangle and repeatedly
add one vertex adjacent to both ends of an existing edge.  The initial
triangle has three distinct labels.  Since all four labels occur, there
is a first added vertex `l` carrying the fourth label.  Let `mn` be the
edge on which `l` was added.

Every edge of a two-tree belongs to a triangle.  Hence, immediately
before `l` was added, there was a vertex `r` adjacent to both `m` and
`n`.  The vertices `m,n,r` have the three labels already present: their
labels are pairwise distinct because they form a triangle, and the label
of `r` is not the new fourth label by the choice of `l`.

At the moment `l` was added, its only neighbours among the old vertices
were `m,n`.  Later construction steps add no edge between two already
present vertices, so `lr` is absent in the final graph.  All five other
edges on `l,r,m,n` are present.  Thus (2.1) holds and the four vertices
have four distinct labels.  \(\square\)

### Corollary 2.2 (label-faithful near-complete minor)

The seven connected subgraphs

\[
                 A_1,A_2,A_3,V_l,V_r,V_m,V_n                         \tag{2.2}
\]

form a labelled `K_7^-`-minor model in `G`.  Its unique missing model
adjacency is `V_lV_r`, and the four protected labels occur exactly once.

#### Proof

The first three sets form a clique model and are adjacent to all four
selected component subgraphs.  Lemma 2.1 supplies every adjacency among
the latter four except `V_lV_r`.  By the definition of the
component-contact graph, the missing quotient edge means that `V_l` and
`V_r` are anticomplete in `G`.  \(\square\)

## 3. The shared edge separates the two poles

### Lemma 3.1

The vertices `l` and `r` lie in different components of

\[
                              J-\{m,n\}.                              \tag{3.1}
\]

#### Proof

If there were an `l-r` path in `J-{m,n}`, contract its internal part to
obtain the missing edge `lr`.  Together with the five edges in (2.1),
this would give a `K_4` minor in `J`.  A two-tree is `K_4`-minor-free, a
contradiction.  \(\square\)

Let `C` be the component of `J-{m,n}` containing `l`, and define

\[
                     X_0=\bigcup_{x\in V(C)}V_x.                     \tag{3.2}
\]

The set `X_0` is connected: a path in `C` lifts edge by edge to a
connected union of represented subgraphs.

Let $\mathcal A_C$ be the set of all components `W` of $G-\mathcal U$
which have an edge to `X_0`, and put

\[
                    X=X_0\cup\bigcup_{W\in\mathcal A_C}V(W).         \tag{3.3}
\]

### Theorem 3.2 (five-branch-set-supported separation)

The set `X` is connected, and

\[
          N_G(X)\subseteq A_1\cup A_2\cup A_3\cup V_m\cup V_n.      \tag{3.4}
\]

Moreover, `V_r` is contained in

\[
                         V(G)-(X\cup N_G(X)).                         \tag{3.5}
\]

Consequently

\[
             \bigl(X\cup N_G(X),\;V(G)-X\bigr)                      \tag{3.6}
\]

is an actual separation with two nonempty open sides, and

\[
                              |N_G(X)|\ge 7.                          \tag{3.7}
\]

#### Proof

Every component in $\mathcal A_C$ is connected and has an edge to the
connected set `X_0`; hence `X` is connected.

There is no edge of `J` between a vertex of `C` and a vertex outside
$C\cup\{m,n\}$, by the definition of `C`.  Now let `W` be a component
of $G-\mathcal U$ which touches `X_0`.  Its attachment vertices in `H`
induce a clique.  One of those attachment vertices belongs to `C`.  It
follows that every attachment vertex of `W` which belongs to `J` lies in
$C\cup\{m,n\}$: a vertex of `J` outside that set would be nonadjacent
to the attachment vertex in `C`, contradicting the attachment-clique
property.  Its remaining possible attachments are the three vertices of
the joined `K_3`, represented by `A_1,A_2,A_3`.

Distinct components of $G-\mathcal U$ are anticomplete.  Since (3.3)
absorbs every such component touching `X_0`, no omitted outside component
has an edge to `X`.  The preceding paragraph and the quotient separation
therefore give (3.4).

By Lemma 3.1, `r` is outside $C\cup\{m,n\}$.  Hence `V_r` is disjoint
from the five sets on the right of (3.4), and no quotient edge joins it
to a vertex of `C`.  Also no component absorbed into `X` can touch
`V_r`: its attachment clique would then contain a nonadjacent pair
consisting of a vertex of `C` and `r`.  Thus `V_r` is disjoint from `X`
and anticomplete to it, proving (3.5).

The first open side of (3.6) contains the nonempty set `X`; the second
contains the nonempty connected subgraph `V_r`.  Its intersection is
exactly `N_G(X)`.  Thus (3.6) is an actual separation, and
seven-connectivity gives (3.7).  \(\square\)

## 4. Exact trust boundary

The theorem above uses the whole two-tree only to find a label-rainbow
diamond and then a quotient edge separator.  It replaces the unbounded
two-tree by an actual host separation supported on five named branch
sets.  It does **not** prove any of the following.

1. The separator in (3.6) has order at most seven.  Its five supporting
   branch sets may each contain many literal boundary vertices.
2. If its order is seven, six-colourings of the two closed shores induce
   the same equality partition on the seven boundary vertices.
3. A proper-minor colouring preserves the four protected component
   labels, the selected path and cut, or the rainbow diamond.
4. The side `X` or one of its represented components is smaller than a
   globally chosen lifted simplicial component.
5. Every adjacent-pair configuration reaches the conditional defect-one
   hypotheses of Section 1.

Thus the remaining theorem in this branch is a host-level exchange on
the five-branch-set-supported separation: it must either reduce the
literal boundary excess, align the two boundary colouring partitions, or
reconstruct a valid defect-one configuration with a strictly smaller
lifted component.

## 5. Dependency

- [normal form around a simplicial component in the defect-one branch](../results/hc7_defect_one_simplicial_normalization.md)
- [component-contact defect and the two-tree equality case](../results/hc7_component_contact_defect_theorem.md)
