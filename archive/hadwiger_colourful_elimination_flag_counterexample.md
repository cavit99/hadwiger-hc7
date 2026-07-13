# A full colourful elimination flag with no prescribed rooted clique model

## Status

The flag-packaging principle proposed in
`hadwiger_colourful_elimination_flag.md` is false, already in order four.
The counterexample below is entirely explicit.  It preserves every level of
the private-colour descent: all four boundary sets are inclusion-minimal
colourful, every deleted layer is a whole private colour class, and the four
distinguished roots are nevertheless not the roots of a `K_4`-model.

This is not a counterexample to Strong Hadwiger.  The failure is caused by
prescribing the particular root selected at each level of the flag.

## 1. The graph

Let `G` have vertex set

\[
                         \{0,1,2,3,4,5,6\}
\]

and edge set

\[
\begin{split}
 E(G)=\{&03,04,05,06,\ 12,14,15,\ 23,24,\\
        &34,36,56\}.
                                                        \tag{1.1}
\end{split}
\]

Equivalently, its edges are the union of the five triangles

\[
                 034,\quad 036,\quad 056,\quad 124,\quad 234
                                                        \tag{1.2}
\]

and the additional edge `15`.

### Lemma 1.1

The graph `G` is four-chromatic, and `X_4=V(G)` is inclusion-minimal
four-colourful.

#### Proof

Suppose first that `G` had a three-colouring.  The triangle `034` uses
all three colours.  The triangles in (1.2), read successively, force

\[
 c(2)=c(0),\qquad c(1)=c(3),\qquad
 c(6)=c(4),\qquad c(5)=c(3).
                                                        \tag{1.3}
\]

The edge `15` now has equally coloured ends, a contradiction.  On the
other hand,

\[
          \{0,2\}\mid\{3,5\}\mid\{4,6\}\mid\{1\}
                                                        \tag{1.4}
\]

is a proper four-colouring.  Hence `chi(G)=4`, so every proper
four-colouring uses all four colours on `V(G)`.

For completeness, the following table gives a proper three-colouring of
`G-v` for every vertex `v`; each row lists its three independent colour
classes.

\[
\begin{array}{c|c}
v&\text{colour classes of }G-v\\ \hline
0&\{1,3\}\mid\{4,5\}\mid\{2,6\}\\
1&\{0,2\}\mid\{3,5\}\mid\{4,6\}\\
2&\{0,1\}\mid\{3,5\}\mid\{4,6\}\\
3&\{0,1\}\mid\{4,5\}\mid\{2,6\}\\
4&\{0,1\}\mid\{3,5\}\mid\{2,6\}\\
5&\{0,2\}\mid\{1,3\}\mid\{4,6\}\\
6&\{0,2\}\mid\{1,3\}\mid\{4,5\}.
\end{array}                                             \tag{1.5}
\]

Extend the row for `v` by giving `v` a fourth colour.  This produces a
four-colouring in which that fourth colour occurs on `V(G)` exactly at
`v`.  Thus `V(G)-{v}` is not four-colourful for every `v`, proving
inclusion-minimality.  \(\square\)

### Lemma 1.2 (the counterexample has every independent trace)

For every nonempty independent set \(S\subseteq V(G)\), there is a proper
four-colouring of `G` having one colour class exactly `S`.

#### Proof

Choose `v in S`.  By (1.5), `G-v` is three-colourable, and hence so is
the induced subgraph `G-S`.  Colour `G-S` with three colours and give
every vertex of the independent set `S` a fourth colour.  This is proper
and the fourth colour has trace exactly `S`.  Since `chi(G)=4`, the
resulting colouring necessarily uses all four colours.  \(\square\)

Thus the failure below persists under the full independent-trace
hypothesis furnished by star contractions in a minor-critical graph.

## 2. The complete private-colour flag

Use the four-colouring (1.4), choose

\[
                 x_4=1,\qquad A_4=\{1\},
\]

and put `H_3=G-A_4`.  In `H_3`, set

\[
             X_3=\{0,4,5\},\qquad
             c_3:\ \{0,2\}\mid\{3,5\}\mid\{4,6\}.
                                                        \tag{2.1}
\]

The same triangle propagation as in (1.3), now without the triangle
`124`, shows that every three-colouring of `H_3` satisfies

\[
                 c(2)=c(0),\quad c(6)=c(4),\quad
                 c(5)=c(3),                              \tag{2.2}
\]

while `034` uses all three colours.  Hence `X_3={0,4,5}` uses all three
colours in every three-colouring.  It is inclusion-minimal because it has
three vertices, and no set of at most two vertices can use all three
colours in a colouring.  Choose

\[
                 x_3=0,\qquad A_3=\{0,2\}.
\]

Then `A_3` is a colour class of (2.1) and
`A_3\cap X_3=\{0\}`.

The graph

\[
 H_2=H_3-A_3=G[\{3,4,5,6\}]
\]

is the path

\[
                         4-3-6-5.                       \tag{2.3}
\]

Its endpoints `4,5` receive opposite colours in every two-colouring.
Consequently

\[
 X_2=\{4,5\},\qquad
 c_2:\ \{3,5\}\mid\{4,6\}
                                                        \tag{2.4}
\]

is an inclusion-minimal two-colourful state.  Choose

\[
                 x_2=4,\qquad A_2=\{4,6\}.
\]

Finally, `H_1=H_2-A_2` is the edgeless graph on `{3,5}`; the singleton

\[
                         X_1=\{5\},\qquad x_1=5          \tag{2.5}
\]

is inclusion-minimal one-colourful.

Thus (1.4), (2.1), (2.4), and (2.5) give a colourful elimination flag
of order four with distinguished roots

\[
                         (x_1,x_2,x_3,x_4)=(5,4,0,1).
                                                        \tag{2.6}
\]

Every clause of Theorem 2.1 in the original flag note is visible here;
in particular, this is not merely one collection of pairwise Kempe
paths.

## 3. The prescribed rooted `K_4` does not exist

### Lemma 3.1

There is no `K_4`-model in `G` having four bags which contain,
respectively, `5,4,0,1`.

#### Proof

Suppose such a model exists, and denote its bags by

\[
                         B_5,B_4,B_0,B_1.
\]

The adjacent connected bags `B_0` and `B_1` have connected union.  That
union contains `0,1` and, by disjointness from the other two rooted bags,
avoids `4,5`.  It therefore contains a `0`--`1` path in
`G-{4,5}`.

But in `G-{3,4,5}` the vertices `0,1` lie in different components:
the only remaining nontrivial pieces relevant to them are the edges
`06` and `12`.  Hence every `0`--`1` path in `G-{4,5}` contains `3`,
so

\[
                         3\in B_0\cup B_1.              \tag{3.1}
\]

Similarly, `B_4\cup B_5` contains a `4`--`5` path avoiding `0,1`.
After also deleting `3`, the remaining vertices split into the two edges
`24` and `56`.  Thus every such path contains `3`, and

\[
                         3\in B_4\cup B_5.              \tag{3.2}
\]

Equations (3.1) and (3.2) contradict the pairwise disjointness of model
bags.  \(\square\)

## 4. Consequences for the uniform programme

The counterexample identifies the precise failure of reserved-connector
induction.  The full nested private-colour data do not guarantee even
the two-linkage forced by a prescribed rooted clique: here every
`0`--`1` connector avoiding the other roots and every `4`--`5`
connector avoiding the other roots use the same bottleneck vertex `3`.

Therefore none of the following is a valid uniform principle:

1. every colourful elimination flag packages its distinguished roots;
2. nested private-colour descent alone supplies the reserved connectors
   needed by induction;
3. the exact Kempe information at every level can be combined without an
   additional disjoint-linkage or separator hypothesis.

A repaired theorem must permit reselecting roots after seeing the
separator, or must have a genuine model-or-capacity-cut alternative.  In
particular, the nesting itself cannot replace the separator side of the
uniform portal-capacity dichotomy.

### The exact missing compatibility

Call distinct terminals `(r_1,...,r_k)` **matching-linked** if, for every
matching `M` on a subset of `[k]`, there are pairwise vertex-disjoint
paths, one joining `r_i` to `r_j` for each `ij in M`, and every path
avoids all terminals not equal to its own ends.

This condition is necessary for a prescribed rooted `K_k`-model.  Indeed,
for an edge `ij` of `M`, the union of the adjacent bags rooted at
`r_i,r_j` contains an `r_i`--`r_j` path; paths chosen for distinct edges
of the matching lie in disjoint pairs of bags.

The roots (2.6) are not matching-linked for the matching

\[
                          \{01,45\}:                    \tag{4.1}
\]

the proof of Lemma 3.1 shows that both required paths must contain `3`.
Thus the exact missing compatibility in private-colour descent is not
another pairwise Kempe statement.  It is simultaneous **root-matching
linkage**, or else a separator certificate explaining its failure.

At the top step of this particular flag, the same obstruction says that
no lower-order `K_3`-model rooted at `5,4,0` can coexist with a disjoint
connected carrier rooted at `1` and adjacent to all three bags.  Such a
carrier and the three old bags would themselves be the forbidden rooted
`K_4`-model.

The example refutes packaging an arbitrary selected flag.  It does not
refute the different existential assertion that one can always *reselect*
all private roots and layers so as to obtain a packageable flag.  That
adaptive assertion would still imply Strong Hadwiger and remains
theorem-strength; the distinction between these quantifiers must not be
blurred.

Indeed adaptive choice repairs this particular graph.  One valid flag has
roots

\[
                          (1,5,6,0),                    \tag{4.2}
\]

obtained successively from the colour classes

\[
\begin{array}{c|c|c}
i&X_i&A_i\\ \hline
4&V(G)&\{0\}\\
3&\{1,5,6\}&\{2,6\}\\
2&\{1,5\}&\{4,5\}\\
1&\{1\}&\text{--}.
\end{array}                                             \tag{4.3}
\]

The required colourings have classes

\[
 \{0\}\mid\{1,3\}\mid\{4,5\}\mid\{2,6\},
 \qquad
 \{1,3\}\mid\{4,5\}\mid\{2,6\},
 \qquad
 \{1,3\}\mid\{4,5\}.
\]

To verify the only non-immediate state, the triangles `124,234` force
`1,3` to have the same colour in every three-colouring of `G-0`; the
path `1-5-6-3` then forces `1,5,6` to use all three colours.  After
deleting `{2,6}`, the remaining graph is the path `5-1-4-3`, so
`{1,5}` is inclusion-minimal two-colourful.  Thus (4.3) is a genuine
flag, not merely a root list.

The four bags

\[
                         \{1,2,3\},\quad\{5\},\quad
                         \{6\},\quad\{0\}             \tag{4.4}
\]

form a `K_4`-model rooted in the order (4.2).  This explicitly confirms
that the open adaptive statement is not being declared false by the bad
flag (2.6).

## 5. Uniform lift to every order

The failure is not confined to order four.

### Theorem 5.1

For every `k>=4` there is a colourful elimination flag of order `k`
whose distinguished roots do not root a `K_k`-model.

#### Proof

Put `s=k-4`, let `Q` be a clique of order `s`, and form the join

\[
                              G_k=G\vee Q.              \tag{5.1}
\]

The graph `G` is four-vertex-critical by Lemma 1.1 and (1.5).  Therefore
`G_k` is `k`-vertex-critical: deleting a vertex of `G` leaves a graph
colourable with `3+s=k-1` colours, while deleting a vertex of `Q` leaves
a graph colourable with `4+(s-1)=k-1` colours.  Consequently `V(G_k)` is
inclusion-minimal `k`-colourful.

More generally, every vertex-critical graph has the full independent-
trace property on its whole vertex set: for nonempty independent `S`,
delete one vertex of `S`, colour the remaining induced graph with one
fewer colour, and restore `S` as a new colour class.  Hence every `G_k`
also has every independent exact trace.

Order the vertices of `Q` arbitrarily.  In a `k`-colouring of the join,
each vertex of `Q` is a singleton colour class and its colour is absent
from `G`.  Delete these singleton private classes one at a time, always
taking the whole current vertex set as the next minimal colourful set.
After the `s` deletions the remaining state is precisely `(G,V(G))`.
Continue with the complete order-four flag in Sections 1--2.  This is a
valid order-`k` elimination flag.  Its roots consist of all vertices of
`Q` together with `5,4,0,1`.

Suppose these roots admitted a rooted `K_k`-model.  The `s` vertices of
`Q` lie in `s` distinct bags, so none of the four bags rooted at
`5,4,0,1` contains a vertex of `Q`.  Those four bags therefore lie
entirely in `G`; their connectedness and every adjacency between them are
also witnessed inside `G`.  They would form a `K_4`-model rooted at
`5,4,0,1`, contrary to Lemma 3.1.  \(\square\)

Thus no induction may treat the nested private-colour flag as a uniformly
packageable object, even asymptotically.  The same crossed linkage defect
survives after arbitrarily many perfectly behaved singleton layers are
placed above it.
