# A full labelled shell for the locked two-row path

## Status

This graph realizes the exact Hall-deficient residue after rooted
triangle promotion.  It has a spanning coherent labelled `K_7^vee`
model, every row duty except two opposed duties is already duplicated,
and the two remaining rows have the same unique crossing carrier.  That
carrier is the alternating path

\[
                         l-q-r-h.
\]

The shell is `K_7`-minor-free.  A one-sum with `K_{3,3,3}` makes the
host non-two-apex while preserving both the model and `K_7` exclusion.
The resulting graph has connectivity one, so it does not refute a
seven-connected exchange theorem.  It proves that the proper-minor
states or global connectivity must break the ordered gate; all static
label and Hall data alone are insufficient.

The solver-free exhaustive certificate is
`hc7_near_k7_locked_two_row_full_shell_barrier_verify.py`.

## 1. Construction

Let

\[
                         D,E,U_1,U_2,U_3,U_4
\]

form a clique.  Add the path core edge `p_Lp_R`.  Give it the normalized
neutral contacts

\[
 p_L\sim U_1,U_2,
 \qquad
 p_R\sim U_3,U_4.                                  \tag{1.1}
\]

Join both `p_L,p_R` to `E`, so the active twin row is already available
on both path shores.

Add one crossing carrier

\[
                         K=l-q-r-h                              \tag{1.2}
\]

and edges

\[
                    p_Ll,\quad p_Rr,\quad qU_1,\quad hU_3.    \tag{1.3}
\]

Finally add two singleton crossing helpers.  The vertex `s_2` is
adjacent to `p_L,p_R,U_2`, and `s_4` is adjacent to
`p_L,p_R,U_4`.  There are no other edges.

Put

\[
       A=\{p_L,p_R,l,q,r,h,s_2,s_4\}.                         \tag{1.4}
\]

Then

\[
                  A,D,E,U_1,U_2,U_3,U_4                      \tag{1.5}
\]

is a spanning labelled `K_7^vee` model with the sole absent spoke
`AD`.  The three old exterior pieces relative to the path core are
`K,{s_2},{s_4}`; they are connected, pairwise anticomplete, and each
crosses the cut `p_L|p_R`.

## 2. Exact Hall deficiency

The active row `E` is adjacent to both path sides directly.  Promoting
`s_2` into `U_2` and `s_4` into `U_4` makes those two rows adjacent to
both sides.  The only remaining duties are

\[
          \text{right shore needs }U_1,
          \qquad
          \text{left shore needs }U_3.                       \tag{2.1}
\]

Both duties have the same unique crossing support `K`: its `U_1` portal
is `q`, and its `U_3` portal is `h`.  Thus the two-row incidence family
has neighbourhood `{K}` and Hall deficiency one.

Whole-piece promotion cannot close (2.1).  Promoting `K` into `U_1`
duplicates `U_1` but consumes the only `U_3` support; promoting it into
`U_3` has the symmetric failure.

Nor is there a protected fixed linkage inside `K`.  The desired paths
would join

\[
                         l\text{ to }h,
              \qquad    r\text{ to }q.                       \tag{2.2}
\]

The unique `l-h` path is all of (1.2), while the unique `r-q` path is
its middle edge.  They cannot be vertex-disjoint.  This is the alternating
terminal order from the locked two-row theorem with

\[
              A_L=\{l\},\quad P_{U_3}=\{h\},\quad
              A_R=\{r\},\quad P_{U_1}=\{q\}.                 \tag{2.3}
\]

## 3. Exact `K_7` exclusion

The shell has fourteen vertices.  The verifier enumerates every nonempty
connected vertex set of order at most eight and searches exhaustively for
seven pairwise disjoint, pairwise adjacent candidates.  This is complete:
in a seven-bag model on fourteen vertices no branch bag has more than
`14-6=8` vertices.  It finds 5,946 connected candidate bags and no
`K_7` model.

Thus the obstruction does not merely defeat the intended rooted
construction while hiding a different clique model; the labelled shell
itself is `K_7`-minor-free.

## 4. A non-two-apex host

Take a disjoint `K_{3,3,3}` and identify one of its vertices with `D`.
Absorb the tripartite summand into the model bag labelled `D`.  The model
(1.5) remains spanning and coherent: the enlarged `D` bag is connected,
retains all foreign-bag adjacencies through its old vertex, and is still
anticomplete to `A`.

The resulting graph is `K_7`-minor-free.  It is a one-sum at `D` of two
`K_7`-minor-free graphs.  In a clique model of order at least three,
all bags avoiding the cutvertex must lie on one side; pruning the possible
cutvertex bag puts the whole model in one summand.  The shell is
`K_7`-minor-free by Section 3, and `K_{3,3,3}` is `K_7`-minor-free by the
standard singleton count: seven bags on nine vertices force at least
five singleton bags, but at most one singleton can lie in each of its
three independent parts.

The host is not two-apex.  After any two vertex deletions, the
`K_{3,3,3}` summand loses at most two vertices and still contains a
`K_{3,3}` subgraph.  The verifier checks every deletion pair directly.

Its connectivity is exactly one: deleting the identified vertex `D`
separates the two summands.  This is the sole deliberately failed global
hypothesis.  Any positive theorem for (2.1) must use seven-connectivity
to turn the ordered gate's rich external contacts into a nonalternating
linkage, or use contraction-critical one-step states to splice across the
gate.  Neither conclusion is encoded in the Hall incidence relation.

## Trust boundary

The construction refutes

\[
 \text{coherent labelled model}+K_7\text{-free}+\text{non-two-apex}
 +\text{all other rows promoted}
 \Longrightarrow\text{two-row fixed linkage}.
\]

It does not refute the same statement with seven-connectivity or full
contraction-criticality.  Those are exactly the live axioms.
