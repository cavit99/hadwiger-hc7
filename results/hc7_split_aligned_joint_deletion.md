# A branch-set split aligned with a common two-edge deletion

**Status:** written proof; separate internal audit GREEN in
[`hc7_split_aligned_joint_deletion_audit.md`](hc7_split_aligned_joint_deletion_audit.md).

This note combines two independently useful facts about a spanning labelled
`K_7`-minus-one-edge model.  At the singleton end of the missing adjacency,
there is enough incident-edge deletion capacity to preserve the same model
after deleting two edges.  Independently, a common branch set with two
neighbours of the singleton can be split to give a `K_7`-minor model or an
actual full-neighbourhood separation.  The choices can be made together:
one deleted edge enters the connected side returned by the split and the
other has its outer end outside that side.

When the second outer end is not itself on the new boundary, the two
one-edge colouring responses lie on opposite closed shores.  The
nonadjacent-leaf and critical-triangle alternatives then have literal
first-entry interpretations on the same separation.  The theorem does not
force the resulting boundary to have order seven or synchronize its two
shore colourings.

## 1. Setting

Let `G` be a seven-connected graph with no `K_7` minor.  Suppose that its
vertex set is partitioned into seven nonempty connected branch sets

\[
                       \{x\},D,U_1,U_2,U_3,U_4,U_5             \tag{1.1}
\]

which form a spanning labelled `K_7`-minus-one-edge model whose unique
missing adjacency is `xD`.  Thus the five sets `U_i` are pairwise adjacent,
each is adjacent to `D`, and `x` is adjacent to every `U_i` and anticomplete
to `D`.

Put

\[
             M_i=N_G(x)\cap U_i,\qquad n_i=|M_i|.              \tag{1.2}
\]

Every `n_i` is positive and, because the model is spanning,

\[
                         d_G(x)=\sum_{i=1}^5n_i\ge7.           \tag{1.3}
\]

An edge set incident with `x` is called **model-preserving** when deleting
it leaves the seven sets in (1.1) as the same labelled near-complete minor
model.

## 2. Split-aligned joint deletion

### Theorem 2.1

At least one of the following holds.

1. `G` contains a `K_7` minor, with branch sets obtained explicitly from
   (1.1).
2. There are an index `i`, a nonempty proper connected set
   `L subset U_i`, and vertices `a,b` such that, with

   \[
                  S=N_G(L),\qquad e=xa,\qquad f=xb,            \tag{2.1}
   \]

   all of the following are true:

   - `S` is the boundary of an actual separation with two nonempty open
     sides;
   - `a in L`, `b notin L`, and `x in S`;
   - the two-edge set `{e,f}` is model-preserving for (1.1); and
   - one of the following two precise capacity patterns holds:

     (a) `n_i>=3`, the vertex `b` also belongs to `U_i`, and at least one
         edge from `x` to `U_i` remains after deleting `e,f`; or

     (b) `n_i=2`, the vertex `b` belongs to some `U_j`, `j!=i`, with
         `n_j>=2`, and one edge from `x` to each of `U_i,U_j` remains
         after deleting `e,f`.

In outcome 2, `G-{e,f}` is therefore one graph in which the same labelled
model and a common six-colouring coexist whenever every proper subgraph of
`G` is six-colourable.

#### Proof

Equation (1.3) and the five positive integers `n_i` give an index `i` with
`n_i>=2`.  Choose `rho in M_i`, choose a spanning tree `T` of `G[U_i]`,
and let `T_0` be the minimal subtree of `T` containing

\[
                              M_i\cup\{\rho\}=M_i.              \tag{2.2}
\]

Every leaf of the minimal terminal subtree `T_0` belongs to `M_i`, and a
nontrivial tree has at least two leaves.  Since at most one of them is
`rho`, the tree `T_0` has a leaf `m in M_i-{rho}`.  Delete from the full spanning
tree `T` the edge of `T_0` incident with `m`.  Let `Z,W` be the vertex sets
of the two resulting components, named so that `m in Z` and `rho in W`.
Then `Z,W` are nonempty connected adjacent sets which partition `U_i`.
Moreover,

\[
                       M_i\cap Z=\{m\},\qquad
                       M_i-\{m\}\subseteq W.                   \tag{2.3}
\]

Indeed, every member of `M_i` lies in `T_0`, and the component cut off at
the leaf `m` contains no other vertex of `T_0`; branches of `T-T_0`
attached on that side contain no member of `M_i`.

Rename the four common branch sets other than `U_i` as
`V_1,V_2,V_3,V_4`.  If `Z` is adjacent to `D` and `W` is adjacent to every
`V_k`, then

\[
                \{x\},\quad D\cup Z,\quad W,\quad
                V_1,V_2,V_3,V_4                               \tag{2.4}
\]

are seven branch sets of a `K_7` model.  The set `D union Z` is connected;
the cut tree edge joins it to `W`; the two sets `Z,W` are both adjacent to
`x` by (2.3); `D` supplies all adjacencies from `D union Z` to the four
sets `V_k`; and every remaining adjacency is inherited from (1.1).  This
is outcome 1.

Suppose (2.4) is unavailable.  If `Z` is anticomplete to `D`, put `L=Z`.
Then `N_G(L)` separates the nonempty connected set `L` from the nonempty
set `D`.  Otherwise `Z` is adjacent to `D`, so some `V_k` is anticomplete
to `W`; put `L=W`.  Now `N_G(L)` separates `L` from that nonempty `V_k`.
In either case `S=N_G(L)` is the boundary of an actual separation.

It remains to choose the two edges.  First suppose `n_i>=3`.  If `L=Z`,
put `a=m` and choose `b in M_i cap W`, leaving a second vertex of
`M_i cap W` unchosen.  If `L=W`, choose `a in M_i cap W`, put `b=m`, and
again leave another vertex of `M_i cap W` unchosen.  Thus `a in L`,
`b notin L`, and deleting `xa,xb` leaves an `x-U_i` edge.  All other
required model adjacencies are untouched, proving pattern (a).

Suppose instead that `n_i=2`.  Equation (1.3) gives

\[
                         \sum_{j\ne i}n_j\ge5,                  \tag{2.5}
\]

so some `j!=i` satisfies `n_j>=2`.  The two members of `M_i` lie on
opposite sides by (2.3).  Let `a` be the member in `L`, and choose any
`b in M_j`, retaining another member of `M_j`.  The other member of `M_i`
also remains.  Hence deletion of `xa,xb` retains the required adjacencies
from `x` to both `U_i` and `U_j`, proving pattern (b).

In both patterns `a in L` makes `x in N_G(L)=S`; the construction gives
`b notin L`; and deletion of the two selected edges changes neither the
connectivity of a branch set nor any other model adjacency.  Seven-
connectivity gives `|S|>=7`, although no upper bound has yet been proved.
This completes outcome 2.  \(\square\)

### Corollary 2.2 (parameter-uniform form)

Let `t>=4`.  Suppose a `t`-connected, `K_t`-minor-free graph has a
spanning labelled `K_t`-minus-one-edge model

\[
                       \{x\},D,U_1,\ldots,U_{t-2}
\]

whose missing adjacency is `xD`.  Then either `G` has a `K_t` minor, or
there are a connected proper set `L subset U_i` and two edges `xa,xb`,
with `a in L` and `b notin L`, such that `N_G(L)` is the boundary of an
actual separation and deleting both edges preserves the same labelled
model.  If `|N(x) cap U_i|>=3`, both outer ends may be chosen in `U_i`
while retaining an `x-U_i` edge.  If `|N(x) cap U_i|=2`, the second outer
end may be chosen in another `U_j` having at least two neighbours of `x`,
while retaining an edge from `x` to each of `U_i,U_j`.  The returned
separator has order at least `t`.

#### Proof

Put `n_i=|N(x) cap U_i|`.  There are `t-2` positive integers `n_i` and

\[
                         \sum_i n_i=d_G(x)>=t.
\]

Thus some `n_i>=2`.  Apply the same minimal-terminal-subtree split in
`U_i`.  The displayed construction (2.4), with the other `t-3` common
branch sets in place of `V_1,...,V_4`, is a `K_t` model whenever the split
does not return a full-neighbourhood separation.  If `n_i>=3`, the
same-bag edge choice is unchanged.  If `n_i=2`, then

\[
                     \sum_{j\ne i}n_j>=t-2
\]

over `t-3` positive summands, so some `n_j>=2`; the second-bag choice is
again valid.  Finally `t`-connectivity gives the separator-order bound.
\(\square\)

## 3. Exact response orientation

Assume from now on that `G` is not six-colourable and every proper minor
of `G` is six-colourable.  Retain outcome 2 of Theorem 2.1 and put

\[
                      C=G[L\cup S],\qquad O=G-L.                \tag{3.1}
\]

For an edge `h`, let `Resp(h,S)` be the equality partitions of the literal
set `S` induced by proper six-colourings of `G-h`.  Let `Ext(Q,S)` be the
partitions induced by proper six-colourings of a graph `Q` containing `S`.

### Proposition 3.1 (clean separation or boundary pinch)

Exactly one of the following placement alternatives holds.

1. **Clean separation:** `b notin S`.  Then

   \[
   \begin{aligned}
      Resp(e,S)&\subseteq Ext(O,S)\setminus Ext(C,S),\\
      Resp(f,S)&\subseteq Ext(C,S)\setminus Ext(O,S).
   \end{aligned}                                               \tag{3.2}
   \]

   In particular the two response languages are disjoint.
2. **Boundary pinch:** `b in S`.  Then `f=xb` is an edge of the literal
   boundary graph `G[S]`.  Its deletion changes both closed sides at their
   common boundary, so the opposite-shore inclusions (3.2) are not valid
   for `f`.

#### Proof

The alternatives merely distinguish whether the vertex `b notin L`
belongs to the boundary or the opposite open side.  The edge `e=xa` has
one end in `L` and one end in `S`, so it belongs to `C` but not to `O`.
In the clean case, `f=xb` belongs to `O` but not to `C`.

A six-colouring of `G-e` therefore restricts to a proper colouring of the
unchanged graph `O`.  If its boundary partition also extended through
`C`, the two closed-shore colourings could be aligned by a permutation of
the six colours and glued to colour `G`.  This is impossible, proving the
first inclusion in (3.2).  The argument with `C,O` and `e,f` interchanged
proves the second.  Their two set differences are disjoint.

If `b in S`, both ends of `f` lie in `S`, which is exactly the asserted
boundary placement and explains why the preceding unchanged-shore
argument is unavailable.  \(\square\)

### Proposition 3.2 (response-preserving nested descent)

Assume the clean alternative of Proposition 3.1.  Let `R_b` be the
component of `G-S` containing `b`, and put

\[
                         S_b=N_G(R_b).                         \tag{3.3}
\]

Then `S_b subseteq S`, `x in S_b`, and exactly one of the following holds.

1. `S_b` is a proper subset of `S`.  It is the boundary of an actual
   separation of strictly smaller order, and, for

   \[
             C_b=G[R_b\cup S_b],\qquad O_b=G-R_b,
   \]

   the same named responses satisfy

   \[
   \begin{aligned}
      Resp(f,S_b)&\subseteq Ext(O_b,S_b)\setminus Ext(C_b,S_b),\\
      Resp(e,S_b)&\subseteq Ext(C_b,S_b)\setminus Ext(O_b,S_b).
   \end{aligned}                                               \tag{3.4}
   \]

2. `S_b=S`.  Thus both `L` and `R_b` are connected subgraphs adjacent to
   every literal vertex of the same boundary `S`.

In the first outcome seven-connectivity gives `|S_b|>=7`.  The descent
preserves the two named deleted edges, their opposite response
orientations, and the same global labelled near-complete model in
`G-{e,f}`.

#### Proof

Every neighbour of the component `R_b` outside `R_b` belongs to `S`, so
`S_b subseteq S`.  The edge `f=xb`, with `b in R_b`, gives `x in S_b`.
The nonempty set `L` lies in a different component of `G-S`, so `S_b` is
the boundary of an actual separation.  Either it is all of `S` or it has
strictly smaller order.

The edge `f` belongs to `C_b` but not to `O_b`, while `e=xa` belongs to
`O_b` but not to `C_b`: here `a in L` and `x in S_b`.  A colouring of
`G-f` therefore restricts to the unchanged graph `O_b`.  If its boundary
partition extended through the original graph `C_b`, gluing would
six-colour `G`.  This proves the first inclusion in (3.4).  Interchanging
the two closed sides and the two edges proves the second.  The remaining
claims follow from seven-connectivity and from Theorem 2.1.  \(\square\)

### Proposition 3.3 (minimum oriented interface)

Still in the clean alternative, call a vertex set `T` **oriented for
`(e,f)`** when `x in T` and `a,b` lie in distinct components `A_T,B_T` of
`G-T`, respectively.  Such sets exist because `S` is one.  Choose an
oriented set `T` of minimum order.  Then

\[
                         N_G(A_T)=T=N_G(B_T).                    \tag{3.5}
\]

Thus the two components containing the named outer endpoints are both
full to one common boundary.  Moreover the two edge responses have the
opposite orientations

\[
\begin{aligned}
 Resp(e,T)&\subseteq
   Ext(G-A_T,T)\setminus Ext(G[A_T\cup T],T),\\
 Resp(f,T)&\subseteq
   Ext(G-B_T,T)\setminus Ext(G[B_T\cup T],T).
\end{aligned}                                                  \tag{3.6}
\]

The interface has order at least seven.  If the initial boundary `S` is
not already minimum, replacing it by `T` is a strict host-level decrease
which preserves `x,a,b`, the two response orientations, and the global
labelled near-complete model after deleting `e,f`.

#### Proof

Because `A_T` is a component of `G-T`, its full neighbourhood is a subset
of `T`.  The edge `e=xa` gives `x in N_G(A_T)`.  If
`N_G(A_T) subsetneq T`, then `N_G(A_T)` is itself oriented for `(e,f)`:
the connected set `A_T` is one component after its full neighbourhood is
deleted, while `b` lies outside that neighbourhood and cannot enter
`A_T`.  This contradicts the minimum order of `T`.  Hence
`N_G(A_T)=T`; the same argument with `B_T` and `f` proves (3.5).

For the first line of (3.6), the edge `e` belongs only to the closed
`A_T`-side and `f` belongs only to the opposite closed side.  A colouring
of `G-e` restricts to the unchanged opposite side, but its partition on
`T` cannot extend through the original `A_T`-side, since gluing would
colour `G`.  The second line is symmetric.  Seven-connectivity gives the
order bound, and all preserved labels are literal in the definition of
an oriented set.  \(\square\)

## 4. Literal first entries in the clean case

Continue in the clean alternative, put

\[
                             H=G-\{e,f\},                       \tag{4.1}
\]

and note that `H` retains the same spanning labelled model.  The colouring
fork for jointly persistent incident edges now has the following literal
interpretation on the separation `(C,O)`.

### Corollary 4.1 (nonadjacent outer ends)

Suppose `ab` is not an edge.  There is a proper six-colouring `kappa` of
`H`, with

\[
       \kappa(x)=\kappa(a)=\kappa(b)=\alpha,
       \qquad N_G(x)\cap\kappa^{-1}(\alpha)=\{a,b\}.             \tag{4.2}
\]

At least one of the following descriptions applies.

1. The pair `xa` is bichromatically connected in `H` for all five colours
   other than `alpha`.  For each such colour choose an `a-x` path and stop
   at its first vertex `y` outside `L`.  Then `y in S`, the preceding
   path segment has all internal vertices in `L`, and entrances belonging
   to two distinct alternate colours can coincide only at an
   `alpha`-coloured boundary vertex.
2. There is an `a-b` path in `H-x` which is the union of two named
   bichromatic components and at most one edge between them.  Its first
   vertex after leaving `L` belongs to `S-{x}`.  Switching the component
   containing `a` gives a colouring of `G-f`, while switching the component
   containing `b` gives a colouring of `G-e`; by (3.2), their complete
   labelled equality partitions on `S` are distinct.
3. The pair `xb` is bichromatically connected in `H` for all five colours
   other than `alpha`.  Let `R_b` be the component of `G-S` containing
   `b`.  Orient the five paths from `b` to `x` and stop each at its first
   vertex outside `R_b`.  The resulting vertices lie in `S`, the preceding
   segments have all internal vertices in `R_b`, and the same collision
   rule as in description 1 holds.

#### Proof

The exact trace and the saturation-or-bypass alternative are Proposition
2.1 of the jointly persistent incident-edge colouring theorem, with its
central vertex `v` renamed `x` and its leaves renamed `a,b`.

In the first description, orient each path from `a in L` to `x in S` and
take its first vertex outside `L`.  Full-neighbourhood equality gives that
this vertex lies in `S`.  A common vertex of paths using palettes
`{alpha,i}` and `{alpha,j}`, with `i!=j`, has colour in their intersection
`{alpha}`, proving the repetition assertion.

In the bypass description, the path begins at `a in L`, ends at
`b notin L union S`, and avoids `x`; hence its first exit lies in
`S-{x}`.  The two component switches are the one-edge responses stated by
the saturation-or-bypass theorem.  Proposition 3.1 puts their boundary
partitions in the two disjoint set differences in (3.2), so they cannot be
equal.  If the theorem returns an all-colour saturated edge and it is not
`xa`, it is `xb`.  In the clean case `b` belongs to an open component
`R_b` of `G-S`, while `x` belongs to `S`.  Taking the first exit of each
`b-x` path from `R_b` proves description 3, including its collision rule.
\(\square\)

### Corollary 4.2 (adjacent outer ends)

Suppose `ab` is an edge.  Let `X` be the six-colourings of `H` in which
`e` has equal ends and `f` has proper ends, and let `Y` be those with the
opposite signature.  Write `Part_S(c)` for the equality partition induced
on `S` by a colouring `c`.  Then

\[
 \{Part_S(c):c\in X\}\subseteq Ext(O,S)\setminus Ext(C,S),
 \qquad
 \{Part_S(c):c\in Y\}\subseteq Ext(C,S)\setminus Ext(O,S).    \tag{4.3}
\]

Both sets are nonempty and are disjoint.  They are either unions of
different Kempe components of the colouring reconfiguration graph, or a
first transition between them interchanges two colours on one connected
bichromatic subgraph `D`.  In the latter case

\[
                             D\cap S\ne\varnothing,              \tag{4.4}
\]

and the interchange changes the complete labelled equality partition on
`S`; it is not merely a permutation of colour names on the boundary.
The two possible placements and the saturation conclusions inside `D`
are exactly those in the critical-triangle transition theorem.  If `D`
does not dominate `G`, its full neighbourhood is an actual commonly
coloured separator; if it dominates, `G-D` is five-chromatic and has no
`K_6` minor.

#### Proof

A colouring in `X` restores `f` and is therefore a colouring of `G-e`;
a colouring in `Y` restores `e` and is a colouring of `G-f`.  Equation
(4.3) is Proposition 3.1.  Nonemptiness, the Kempe-component alternative,
the placements of `D`, and its saturation properties are Theorem 3.1 and
Corollary 3.2 of the jointly persistent incident-edge colouring theorem.

If `D` avoided `S`, the two consecutive colourings would agree on every
literal boundary vertex and would induce the same equality partition,
contrary to the disjointness in (4.3).  The same disjointness rules out a
boundary interchange which merely permutes two whole colour blocks and
leaves the equality partition unchanged.  This proves (4.4) and the
stronger partition statement.  \(\square\)

## 5. Exact gain and remaining obstruction

Theorem 2.1 is a host-level, label-preserving alignment theorem.  It
eliminates the possibility that branch-set splitting and common
model-preserving deletion have to be selected independently.  In the
clean case, the colouring fork is now attached to one actual separation:
the nonadjacent bypass has a literal first exit, and every adjacent-case
transition changes a literal labelled boundary partition.  Proposition
3.2 additionally gives a strict response-preserving full-neighbourhood
descent unless the opposite component is full to the original boundary.
Proposition 3.3 makes this well founded: minimizing the boundary order
produces two endpoint components full to one common interface.

Three obstructions remain, and none is silently treated as terminal.

1. The second deleted edge can be a boundary edge (`b in S`).
2. In the adjacent case, the two response families can remain in different
   Kempe components.
3. A boundary-crossing component, saturated path family, or bypass need
   not assign its first hits injectively to the five named common branch
   sets.

In the clean branch, the last obstruction may therefore be studied on the
minimum interface (3.5), rather than along an unranked sequence of local
splits.  The remaining issue there is allocation of the literal first
hits to the fixed branch-set labels, not existence of a decreasing host
parameter.

The separator `S` is only lower-bounded by seven.  Even when it has order
seven, the theorem does not produce one full equality partition extending
through both original closed shores.  A separator from the transition
component carries a common assignment of two opposite one-edge responses,
not automatically a proper colouring of both original closed shores.  The
strict descent in Proposition 3.2 preserves the named response edges and
the global labelled model, but its new boundary can cut through old branch
sets; it is not yet the stronger branch-set-preserving descent needed for
induction.  Thus the result narrows the palette-to-label problem without
proving `HC_7`.

## 6. Dependencies

- [joint deletion capacity at the deficient singleton](../results/hc7_deficient_singleton_joint_persistence.md)
- [two-mark branch-set split](../results/hc7_two_mark_branch_set_split.md)
- [colouring fork for jointly persistent incident edges](../results/hc7_joint_persistent_incident_colour_fork.md)
