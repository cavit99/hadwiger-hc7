# A connected deficient-branch-set trichotomy

**Status:** written proof; separate internal audit GREEN.

This note gives a standard-language extension of the audited singleton
deficient-branch-set trichotomy.  The deficient branch set may now be an
arbitrary connected subgraph, provided that its whole open neighbourhood is
contained in the five branch sets which it meets.

The theorem applies to the five-branch-set-supported separation obtained
from a rainbow diamond in the conditional defect-one two-tree.  Its third
outcome is a genuine labelled near-`K_7` model with a proper connected
subbag as its new deficient centre.  It is **not** a descent to another
valid defect-one component-contact configuration: the protected labels,
the colour-matched path, and its admissible cut need not survive.

## 1. Two elementary connected-subgraph lemmas

Let `U` be a connected vertex set and let

\[
                         R_1,\ldots,R_h                       \tag{1.1}
\]

be pairwise disjoint connected vertex sets outside `U`, each adjacent to
`U`.  Put

\[
                         P_j=N_U(R_j)\ne\varnothing.          \tag{1.2}
\]

Fix distinct vertices `r,s in U`.  An **`r`-retaining connector** is a
connected set `T subseteq U` which contains `r` and meets every `P_j`.
Such a connector always exists: join `r` and one selected vertex of every
`P_j` by paths in `G[U]`.

### Lemma 1.1 (a vertex outside a retaining connector)

Suppose an `r`-retaining connector `T` avoids `s`, and let `Y` be the
component of `G[U-T]` containing `s`.  Then

1. `Y` and `U-Y` are nonempty and connected;
2. `Y` is adjacent to `U-Y`; and
3. `U-Y` remains adjacent to every set in (1.1).

#### Proof

The set `Y` is connected by definition.  Every component of `G[U-T]` has
an edge to the connected set `T`, since `G[U]` is connected.  Consequently
`U-Y`, consisting of `T` and all the other components attached to it, is
connected and adjacent to `Y`.  Finally, `T` meets every portal set `P_j`,
so `U-Y` retains an edge to every `R_j`.  \(\square\)

Call `s` **unavoidable from `r`** if every `r`-retaining connector contains
`s`.

### Lemma 1.2 (the connected side forced by an unavoidable vertex)

Suppose `s` is unavoidable from `r`.  Let `W_s` be the component of
`G[U-s]` containing `r`, and put

\[
                             Z_s=U-W_s.                    \tag{1.3}
\]

Then `Z_s,W_s` are nonempty connected adjacent sets, `s in Z_s`, and at
least one of the portal sets in (1.2) is contained in `Z_s`.

#### Proof

Every component of `G[U-s]` other than `W_s` has an edge to `s`.
Therefore their union with `s`, which is `Z_s`, is connected.  The set
`W_s` is connected and contains `r`, so both sides are nonempty; an edge
between them exists because `G[U]` is connected.

If `W_s` met every `P_j`, a connected subgraph of `G[W_s]` containing `r`
and one selected vertex of every `P_j` would be an `r`-retaining connector
which avoids `s`.  Hence some `P_j` is disjoint from `W_s`, and therefore
is contained in `Z_s`.  \(\square\)

For a set `Z subseteq U`, define its set of lost foreign adjacencies by

\[
 \Omega_U(Z)=\{j:P_j\subseteq Z\}.                      \tag{1.4}
\]

Thus `U-Z` is anticomplete to `R_j` exactly when
`j in Omega_U(Z)`.

### Lemma 1.3 (opposite unavoidable sides)

If `s` is unavoidable from `r` and `r` is unavoidable from `s`, then the
two sets `Z_s,Z_r` defined by (1.3) in the two orientations are disjoint.
Consequently

\[
             \Omega_U(Z_s)\cap\Omega_U(Z_r)=\varnothing. \tag{1.5}
\]

#### Proof

If a vertex `v` belonged to both sets, then every `r-v` path in `G[U]`
would use `s`, while every `s-v` path would use `r`.  Take a simple
`r-v` path.  Its suffix from `s` to `v` avoids `r`, a contradiction.
Thus `Z_s` and `Z_r` are disjoint.

Every `P_j` is nonempty.  It cannot be contained in two disjoint vertex
sets, which proves (1.5).  \(\square\)

## 2. The connected deficient-branch-set theorem

### Theorem 2.1 (connected one-missing-adjacency trichotomy)

Let `G` be seven-connected.  Let

\[
                       A,R,F_1,F_2,F_3,F_4,F_5             \tag{2.1}
\]

be pairwise disjoint nonempty connected vertex sets satisfying:

1. `R,F_1,...,F_5` are pairwise adjacent, and hence form a `K_6`-minor
   model;
2. `A` is anticomplete to `R` and is adjacent to every `F_i`; and
3. every vertex outside `A` which has a neighbour in `A` belongs to
   `F_1 union ... union F_5`.

Then at least one of the following holds.

1. `G` contains a `K_7` minor.
2. For some `i`, there is a nonempty proper connected set
   `Y subset F_i` such that `F_i-Y` is connected and `N_G(Y)` is the
   boundary of an actual separation with two nonempty open sides.  In
   particular,

   \[
                              |N_G(Y)|\ge7.                \tag{2.2}
   \]

   If equality holds, every component of `G-N_G(Y)` is adjacent to every
   vertex of `N_G(Y)`.
3. For some `i`, there is a partition

   \[
                          F_i=Z\mathbin{\dot\cup}W         \tag{2.3}
   \]

   into nonempty connected adjacent sets such that the six sets

   \[
                   A\cup Z,\quad R,\quad F_j\ (j\ne i)    \tag{2.4}
   \]

   form a `K_6`-minor model, and the connected set `W` is adjacent to all
   but exactly one or exactly two of those six sets.  Thus `G` contains a
   labelled `K_7^-`- or `K_7^\vee`-minor model whose deficient centre `W`
   is a proper connected subset of the old branch set `F_i`.

Here `K_7^\vee` denotes the graph obtained from `K_7` by deleting two
edges incident with one vertex.

#### Proof

Put `S=N_G(A)`.  Hypotheses 2 and 3 imply

\[
                 S\subseteq F_1\cup\cdots\cup F_5.       \tag{2.5}
\]

The connected set `R` is disjoint from `A union S`, so `S` separates the
nonempty connected sets `A` and `R`.  Seven-connectivity gives
`|S|>=7`.  Choose seven distinct vertices of `S`, including at least one
from every `F_i`.  Some donor branch set, say `U=F_i`, contains two of the
chosen vertices; call them `r,s`.

Use as the five foreign sets for `U`

\[
                    R\quad\hbox{and}\quad F_j\ (j\ne i). \tag{2.6}
\]

Their portal sets in `U` are all nonempty because the six sets
`R,F_1,...,F_5` form a clique minor model.

Suppose first that `s` is not unavoidable from `r`.  Choose an
`r`-retaining connector which avoids `s`, and let `Y` be the component
outside it containing `s`.  Lemma 1.1 says that `Y` and `U-Y` are
nonempty connected adjacent sets and that `U-Y` retains every adjacency
to the five sets in (2.6).

If `Y` is anticomplete to `R`, then `R` lies outside
`Y union N_G(Y)`.  Hence

\[
                     (Y\cup N_G(Y),\;V(G)-Y)             \tag{2.7}
\]

is an actual separation with two nonempty open sides.  Seven-connectivity
gives (2.2), so outcome 2 holds.

If `Y` is adjacent to `R`, put

\[
                         R'=R\cup Y,\qquad U'=U-Y.        \tag{2.8}
\]

The seven branch sets

\[
                       A,\quad R',\quad U',\quad
                       F_j\ (j\ne i)                     \tag{2.9}
\]

are connected and disjoint.  The selected vertex `s` supplies the
`A-R'` adjacency, while `r in U'` supplies `A-U'`.  The edge across
`Y|(U-Y)` supplies `R'-U'`.  The retained portal contacts from Lemma 1.1
and the old foreign clique supply every remaining adjacency.  Thus (2.9)
is an explicit `K_7`-minor model, giving outcome 1.

The same argument, with the names `r,s` reversed, applies if `r` is not
unavoidable from `s`.  We may therefore assume that each selected vertex
is unavoidable from the other.

Apply Lemmas 1.2 and 1.3.  They give two disjoint connected detachable
sides `Z_s,Z_r`, each containing one selected neighbour of `A`, and each
with a nonempty set of lost foreign adjacencies.  Those two sets of lost
adjacencies are disjoint subsets of the five labels in (2.6).  One of the
two sides, call it `Z`, therefore satisfies

\[
                         1\le |\Omega_U(Z)|\le2.           \tag{2.10}
\]

Put `W=U-Z`.  Lemma 1.2 makes `Z,W` nonempty connected adjacent sets.

If `Z` is anticomplete to `R`, the separation (2.7), with `Z` in place of
`Y`, gives outcome 2.  Suppose then that `Z` is adjacent to `R`, and put

\[
                              A'=A\cup Z.                 \tag{2.11}
\]

The set `A'` is connected because `Z` contains a selected neighbour of
`A`.  The six sets

\[
                         A',\quad R,\quad F_j\ (j\ne i)   \tag{2.12}
\]

are pairwise adjacent: `Z` supplies `A'R`, `A` supplies every
`A'F_j` edge, and all the other adjacencies are old edges of the foreign
`K_6` model.

The cut edge between `Z` and `W` makes `W` adjacent to `A'`.  For a set
in (2.6), the residual `W` loses its old adjacency precisely when its
portal set is contained in `Z`, namely precisely for the labels in
`Omega_U(Z)`.  Equation (2.10) therefore says that the seven sets

\[
                         W,\quad A',\quad R,\quad
                         F_j\ (j\ne i)                   \tag{2.13}
\]

form a labelled `K_7^-`- or `K_7^\vee`-minor model with deficient centre
`W`.  This is outcome 3.

It remains only to verify the fullness assertion in outcome 2.  Let
`T=N_G(Y)` have order seven and let `C` be a component of `G-T`.  If some
`t in T` had no neighbour in `C`, then `N_G(C) subseteq T-{t}` would
separate `C` from another component of `G-T` using at most six vertices,
contrary to seven-connectivity.  Thus every component is `T`-full.
\(\square\)

## 3. The labelled colouring information at a separator

The theorem does not force the separator in outcome 2 to have order seven,
and it does not force matching boundary colourings.  The following is the
exact colouring information that minor-criticality supplies without any
additional claim.

### Proposition 3.1 (one-sided boundary partitions)

Assume in addition that `G` is not six-colourable and every proper minor
of `G` is six-colourable.  Let `Y` be returned by outcome 2 and put

\[
                    T=N_G(Y),\quad G_L=G[Y\cup T],
                    \quad G_R=G-Y.                       \tag{3.1}
\]

Every deletion or contraction supported strictly inside `Y` produces a
six-colouring whose equality partition on the literal boundary `T`
extends to `G_R` but does not extend to the unmodified graph `G_L`.
If the same equality partition is produced by a proper operation in the
opposite open shore, then the two closed-shore colourings can be aligned by
a permutation of the six colours and glued to a six-colouring of `G`.

#### Proof

The operation gives a proper minor, hence a six-colouring.  Its restriction
to the unchanged graph `G_R` gives the asserted extension.  If the same
boundary equality partition extended to `G_L`, permuting colour names on
one side would make the two restrictions agree on every vertex of `T`;
their union would six-colour `G`, a contradiction.  The final statement is
the same gluing argument using proper operations in opposite shores.
\(\square\)

Thus a returned separator is a labelled colouring interface, but a common
boundary partition is still an additional theorem-strength requirement.

## 4. Parameter-uniform form

The argument is not specific to seven branch sets.

### Corollary 4.1 (uniform connected deficient-branch-set trichotomy)

Let `m>=3`, let `G` be `(m+1)`-connected, and let

\[
                         A,R,F_1,\ldots,F_{m-1}             \tag{4.1}
\]

be pairwise disjoint nonempty connected sets.  Suppose that

1. `R,F_1,...,F_{m-1}` form a `K_m`-minor model;
2. `A` is anticomplete to `R` and adjacent to every `F_i`; and
3. `N_G(A) subseteq F_1 union ... union F_{m-1}`.

Then `G` contains a `K_{m+1}` minor, or there is a nonempty proper
connected set `Y` in one `F_i`, with connected complement in `F_i`, whose
open neighbourhood is an actual separator of order at least `m+1`, or
there is a labelled near-`K_{m+1}` model whose deficient centre is a proper
connected subset of one `F_i` and whose only missing model adjacencies are
`q` edges incident with that centre, where

\[
                         1\le q\le\left\lfloor
                              \frac{m-1}{2}\right\rfloor. \tag{4.2}
\]

At separator order exactly `m+1`, every component of its deletion is
adjacent to every boundary vertex.

#### Proof

The set `N_G(A)` separates `A` from `R`, so it has at least `m+1`
vertices.  Choose `m+1` of them, including one in every one of the `m-1`
sets `F_i`.  Some donor `U=F_i` contains two selected vertices.

Repeat the proof of Theorem 2.1 with the `m-1` foreign sets

\[
                            R\quad\hbox{and}\quad F_j\ (j\ne i). \tag{4.3}
\]

An avoidable selected vertex gives either the explicit transfer into `R`,
and hence a `K_{m+1}` model, or an actual separator.  If the two selected
vertices are mutually unavoidable, Lemmas 1.2 and 1.3 give two disjoint
connected sides with disjoint nonempty sets of lost foreign adjacencies.
One of those two sets has order at most `floor((m-1)/2)`.  If its side
misses `R`, its open neighbourhood is an actual separator.  Otherwise
adjoin that side to `A`; its connected donor complement becomes the
deficient centre and misses precisely that set of foreign adjacencies.
The equality-order fullness proof is unchanged.  \(\square\)

## 5. Application to the rainbow-diamond separation

Use the notation of
[`hc7_defect_one_rainbow_diamond_separator.md`](../results/hc7_defect_one_rainbow_diamond_separator.md).
The five sets

\[
                         A_1,A_2,A_3,V_m,V_n              \tag{5.1}
\]

are connected and pairwise adjacent.  The connected set `X` is adjacent
to all five, the connected set `V_r` is adjacent to all five, and `X` is
anticomplete to `V_r`.  The five-branch-set-supported separation gives

\[
             N_G(X)\subseteq A_1\cup A_2\cup A_3\cup V_m\cup V_n. \tag{5.2}
\]

Therefore Theorem 2.1 applies with

\[
 A=X,\qquad R=V_r,\qquad
 \{F_1,\ldots,F_5\}=\{A_1,A_2,A_3,V_m,V_n\}.             \tag{5.3}
\]

In a `K_7`-minor-free host it yields either an actual separator as in
outcome 2 or a labelled one-/two-missing-spoke near-`K_7` model whose new
deficient centre is a proper connected subbag of one set in (5.1).

This is a strict connected-subbag move, but it is not a valid descent for
the active defect-one induction.  If the donor is one of `A_1,A_2,A_3`,
the new centre is not even a component of one of the four protected branch
sets.  If the donor is `V_m` or `V_n`, moving `Z` into `X` need not preserve
the old protected label, the colour-matched path, the admissible cut, or
eligibility at that cut.  Moreover a single connected-subbag deficiency
rotation has a label-preserving inverse, so proper containment in the
current donor is not by itself a well-founded global rank.

The exact remaining step is therefore a **label-preserving re-entry or
colour-gluing theorem**: it must turn outcome 3 into another complete valid
defect-one configuration with a smaller eligible lifted component, or turn
outcome 2 into an exact order-seven interface with a boundary partition
attained from both shores.  Neither conclusion follows from the
connected-subgraph geometry proved here.

## 6. Dependencies

- [rainbow-diamond separation in the conditional defect-one two-tree](../results/hc7_defect_one_rainbow_diamond_separator.md)
- [single connected-subbag rotations are exact involutions](../results/hc7_near_k7_rotation_edge.md)
