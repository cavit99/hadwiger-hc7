# Reserved connector or full adhesion

## 1. A uniform rooted-model principle

### Theorem 1.1 (reserved connector or full adhesion)

Let `H` be a `k`-connected graph.  Let

\[
                 \mathcal M=(B_1,\ldots,B_m)
\]

be a rooted `K_m`-model with roots `u_i in B_i`, and put
`W=union_i B_i`.  Let `a,b` be distinct vertices outside `W`.  Assume
that for every `i`, at least one of `a u_i` and `b u_i` is an edge.

Then exactly one of the following useful outcomes occurs.

1. **Reserved connector.**  There is an `a`--`b` path `P` in `H-W`.
   Then

   \[
                         V(P),B_1,\ldots,B_m
   \]

   are the branch sets of a `K_{m+1}`-model.
2. **Full adhesion.**  There is an inclusion-minimal `a`--`b` separator
   `Z subseteq W`, with `|Z|>=k`, such that the components `C_a,C_b` of
   `H-Z` containing `a,b`, respectively, satisfy

   \[
                    N_H(C_a)=Z=N_H(C_b).                 \tag{1.1}
   \]

   More precisely, every vertex of `Z` has a neighbor in each of
   `C_a,C_b`; equality in (1.1) holds because distinct components of
   `H-Z` have no edge.

If `k>m`, the second outcome multiply hits a model bag:

\[
                  |Z\cap B_i|\ge2
\]

for some `i`.

#### Proof

If `a,b` lie in the same component of `H-W`, that component contains an
`a`--`b` path `P`.  It is disjoint from every model bag.  The path bag is
adjacent to `B_i`, because it contains both `a,b` and one of these is
adjacent to the root `u_i`.  It is connected; the old bags are connected
and pairwise adjacent.  This proves outcome 1.

Otherwise `W` separates `a` from `b`.  Choose an inclusion-minimal subset
`Z subseteq W` which still separates them.  Since `H` is `k`-connected,
`|Z|>=k`.  For every `z in Z`, minimality gives an `a`--`b` path whose
only vertex in `Z` is `z`; the two edges of that path incident with the
separator show that `z` has a neighbor in both `C_a` and `C_b`.
Conversely, every neighbor outside one of these components lies in `Z`,
because `C_a,C_b` are components of `H-Z`.  This proves (1.1).

Finally, `Z` is distributed among the `m` disjoint bags.  If `|Z|>=k>m`,
the pigeonhole principle gives a bag containing at least two vertices of
`Z`.  QED.

This theorem is label-free and uniform in `k,m`.  It deliberately says
nothing about how to split the multiply hit bag; that is the dynamic
portal-order problem.

## 2. Degree-seven `HC_7` corollary

### Theorem 2.1 (double-root trace dichotomy)

Let `G` be a seven-contraction-critical, `K_7`-minor-free graph and let
`v` be a vertex of degree seven.  Put `H=G-v` and `N=N_G(v)`.  For every
nonedge `ab` of `G[N]`, one of the following holds.

1. `G` contains a `K_7` minor; or
2. `H` has a rooted `K_5`-model `B_1,...,B_5`, rooted at the five
   vertices `U=N-{a,b}`, and there is an inclusion-minimal `a`--`b`
   separator

   \[
                         Z\subseteq\bigcup_{i=1}^5B_i,
                         \qquad |Z|\ge6,                 \tag{2.1}
   \]

   whose two distinguished shores are full to `Z`.  In particular,
   some `B_i` contains at least two vertices of `Z`.

If equality holds in (2.1), then

\[
                            S=Z\cup\{v\}                 \tag{2.2}
\]

is an exact seven-vertex adhesion in `G`, and the components containing
`a` and `b` are both full to `S`.

The theorem is stated with outcome 1 although the ambient hypotheses say
that it cannot occur.  Consequently every hypothetical counterexample
with a degree-seven vertex is forced into outcome 2 for every nonedge
`ab` selected for the exact trace.

#### Proof

Dirac's neighborhood inequality at `v` gives

\[
                         \alpha(G[N])\le2.               \tag{2.3}
\]

Fix a nonedge `ab` in `G[N]`.  Contract the connected star on
`{v,a,b}` to one vertex.  A six-coloring of this proper minor expands to
a proper six-coloring `c` of `H` in which `a,b` have one color, say
color 0, and no other vertex of `N` has color 0.  The graph `H` is not
five-colorable, for otherwise `G` would be six-colorable.  Moreover every
color of `c` occurs on `N`, for a missing color could be given to `v`.
It follows that the five vertices

\[
                            U=N-\{a,b\}=\{u_1,\ldots,u_5\}
\]

have five distinct nonzero colors.

If two vertices `u_i,u_j` are nonadjacent, they belong to the same
two-color Kempe component.  Indeed, otherwise interchange their two
colors on the component containing `u_i`.  Since each of these colors
occurs exactly once on `N`, the old color of `u_i` disappears from `N`
and can be assigned to `v`, producing a six-coloring of `G`.

Let

\[
                     F=\overline{G[U]}.
\]

By (2.3), `F` is triangle-free.  Mantel's theorem gives `|E(F)|<=6`.
Kriesell--Mohr's theorem that every graph on five vertices with at most
six edges has property (*) therefore supplies an `F`-certificate rooted
at `U`, using only the five nonzero color classes.  Call its bags
`B_1,...,B_5`.  Whenever `u_i u_j` is not an edge of `F`, the two roots
are adjacent in `G`; their root edge makes `B_i,B_j` adjacent.  Thus the
same five bags are a rooted `K_5`-model in `H`.  They avoid `a,b`, because
the construction was performed in the union of the five nonzero color
classes.

For every `u_i`, at least one of `a u_i,b u_i` is an edge: otherwise
`{a,b,u_i}` would contradict (2.3).  Apply Theorem 1.1 to `H`, this
rooted `K_5`-model, and `a,b`.  The graph `G` is seven-connected by
Mader's theorem, hence `H` is six-connected.  A reserved connector gives
six pairwise adjacent branch sets in `H`, all meeting `N`; adjoining the
singleton bag `{v}` gives a `K_7`-minor.  Otherwise Theorem 1.1 gives
(2.1), full shores, and a multiply hit bag.

If `|Z|=6`, remove `S=Z union {v}` from `G`.  The `a`- and `b`-components
remain distinct.  Each is adjacent to every vertex of `Z`, and they are
also adjacent to `v` through `a` and `b`, respectively.  Hence both are
full to the exact seven-adhesion `S`.  QED.

### Theorem 2.2 (the residue is exactly a two-shore `P_4` support lock)

Retain the rooted `K_5`-model from Theorem 2.1 and write
`W=union_i B_i`.  If there is no `K_7` minor, let `A` and `D` be the
distinct components of `H-W` containing `a` and `b`.  Define their bag
contact sets

\[
 I_A=\{i:E(A,B_i)\ne\varnothing\},\qquad
 I_D=\{i:E(D,B_i)\ne\varnothing\}.
\]

Then

\[
 I_A\cup I_D=[5],\qquad I_A\ne[5]\ne I_D.       \tag{2.3}
\]

Consequently there are indices

\[
       x\in I_A-I_D,\qquad y\in I_D-I_A,          \tag{2.4}
\]

and the complement of the support graph of the seven disjoint rooted
pieces

\[
                   A,D,B_1,\ldots,B_5
\]

contains the missing-edge path

\[
                         B_x-D-A-B_y.             \tag{2.5}
\]

Thus every degree-seven residue is the `P_4` atomic motif of the uniform
one-surplus theorem; the `K_3` and `3K_2` motifs do not arise at this
stage.  Moreover,

\[
 |N_H(A)|\ge6,quad N_H(A)\subseteq\bigcup_{i\in I_A}B_i,
\]

and symmetrically for `D`.  Since both contact sets have order at most
four, each shore has portal surplus at least two inside its contacted
model bags.

#### Proof

For each `i`, at least one of `a,b` is adjacent to `u_i`.  Since
`a in A`, `b in D`, this proves `I_A union I_D=[5]`.  If, say,
`I_A=[5]`, then

\[
                         A,B_1,\ldots,B_5
\]

are six disjoint connected pairwise adjacent branch sets, all meeting
`N`; with `{v}` they give `K_7`.  Thus neither contact set is all of
`[5]`.  Choosing a label missed by each shore and using their union
property gives (2.4).  The shores are distinct components of `H-W` and
are anticomplete.  They also have exactly the missing incidences in
(2.5), proving the support-path assertion.

Finally, `N_H(A)` separates the nonempty component `A` from `D`, so
six-connectivity gives `|N_H(A)|>=6`.  Every such neighbor lies in a bag
contacted by `A`; there are at most four of those bags.  The excess over
one portal per contacted bag is therefore at least two.  The same proof
applies to `D`.  QED.

### Lemma 2.3 (a label-preserving private-bag split closes the `P_4`)

Choose `x,y` as in (2.4).  Suppose `B_x` has a partition into nonempty
connected sets `X,Y` such that

1. `u_x in Y`;
2. `X` and `Y` are adjacent;
3. `A` is adjacent to `X`; and
4. both `X` and `Y` are adjacent to every old bag `B_j` with `j != x`.

Then `G` has a `K_7` minor.

#### Proof

Use the following six branch sets in `H`:

\[
 A\cup X,\qquad D\cup B_y,\qquad Y,
 \qquad B_j\ (j\notin\{x,y\}).                   \tag{2.6}
\]

    The first two are connected because there is an `A`--`X` edge and a
    `D`--`B_y` edge.  They are adjacent through the edge between `X` and
    `B_y`.
The first and third are adjacent through `X-Y`; the second and third are
adjacent through `B_y-Y`.  Conditions 3--4 and the old clique-model
adjacencies give all remaining pairs.  The first set contains `a`, the
second contains `b`, the third contains `u_x`, and every singleton old
bag retains its root.  Thus all six sets meet `N`; adjoining `{v}` gives
`K_7`.  QED.

The symmetric statement holds with `A,D` and `x,y` exchanged.  This is
the exact dynamic target left by Theorem 2.2: portal surplus is already
proved, so a counterexample must arrange every private-bag portal behind
a one-sided loss of a named old-bag adjacency.

### Lemma 2.4 (weaker exact arm condition)

The conclusion of Lemma 2.3 still holds if condition 4 is replaced by
the following asymmetric conditions:

- the rooted remainder `Y` is adjacent to every `B_j`, `j != x`; and
- the detached `A`-arm `X` is adjacent to `B_y` and to every `B_j` with
  `j notin I_A`.

#### Proof

Use the same six sets (2.6).  The rooted remainder `Y` sees every old
bag by the first condition.  The branch `A union X` sees `B_j` directly
through `A` when `j in I_A`, and through `X` otherwise.  In particular
it sees `D union B_y` through the required `X-B_y` edge.  All other
adjacencies are supplied exactly as in Lemma 2.3.  QED.

In the sharp `|I_A|=4` cell, the detached arm needs to retain only the
single missing label `B_y`; all four other named clique adjacencies may
remain concentrated in the rooted remainder.  This is the weakest clean
private-bag peel presently extracted from the support geometry.

## 3. Consequences and precise remaining gap

This proves, without Moser labels or a bound on bag/shore order, the
promised dichotomy

\[
 \boxed{\text{rooted }K_5+\text{reserved connector}}
 \quad\text{or}\quad
 \boxed{\text{full adhesion with a multiply hit named bag}}.
\]

It closes the first outcome completely.  In the second outcome:

- equality `|Z|=6` feeds directly into the exact order-seven full-shore
  machinery, including the audited `C_6 disjoint-union K_1` closure;
- strict surplus `|Z|>6` supplies more portal capacity inside the five
  named bags;
- before taking a minimal separator, the two root shores form exactly the
  atomic missing-`P_4` support motif and each has portal surplus at least
  two;
- what remains is the dynamic theorem that opens the multiply hit bag, or
  converts its failed split into compatible proper-minor coloring states.

Lemma 2.3 shows exactly what “opens” means without Moser labels: detach an
`A`-portal side of a private bag while its rooted remainder and the
detached side both preserve the four old clique labels.  A proof that
minor-critical operation states force this split, or else a color-gluable
adhesion, would close the entire degree-seven residue at once.

The result does not prove `HC_7`: it does not eliminate all possible
boundary graphs at equality, nor the strict-surplus portal-order lock, and
it presupposes the existence of a degree-seven vertex.
