# Regeneration at the shifted order-eight separation

**Status:** written proof, independent audit pending.  This note proves a
model-regeneration dichotomy inside the current endpoint-rigid frontier.  It
does not prove `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph.  Let `S` be an eight-vertex separator
such that `G-S` has exactly two connected components `U,V`, and assume that
every vertex of `S` has a neighbour in each component.  Let `s in S` be
adjacent to every vertex of `S-{s}`.

Fix `v in V` and `y in S`, and put

\[
                         X=V-\{v\}.
\]

Assume that `X` is nonempty and

\[
                N_G(X)=\{v\}\mathbin{\dot\cup}(S-\{y\}),            \tag{1.1}
\]

and, more strongly, that every component of `X` is adjacent to every
vertex of the eight-set on the right side of (1.1).  These are exactly the
shifted-separation conclusions in the current frontier.

For a two-set `P`, let `mu_G(P)` be the minimum support order of a `K_5`
minor model in `G-P`.  The application below assumes

\[
                   \max_{|P|=2}\mu_G(P)\le 6.                         \tag{1.2}
\]

An **actual order-seven separation** means a separation of order seven
with both open sides nonempty.

## 2. Shifted-pair regeneration theorem

### Theorem 2.1

Assume (1.1), and suppose that `G` has neither a `K_7` minor nor an actual
order-seven separation.  Let `mathcal N` be a `K_5` minor model in
`G-{s,v}` supported on at most six vertices.  Then exactly one of the
following two structural outcomes is necessary.

1. **Strict full-separation descent.**  The support of `mathcal N` is
   contained in `U union (S-{s})`.  There is an eight-set `K` and a
   nonempty union `L` of components of `G-K` such that

   \[
        L\subsetneq U,\qquad \{s,v\}\subseteq K,qquad
        V(\mathcal N)\subseteq L\cup K.                             \tag{2.1}
   \]

   Every component of `G-K` is adjacent to every vertex of `K`.  Thus
   `(L,K,V(G)-(L union K))` is another full order-eight separation, the
   same avoided pair and the complete regenerated model lie on its closed
   `L`-side, and the source-side order has strictly decreased from `|U|`
   to `|L|`.

2. **Straddling normal form.**  The model has support order six.  After
   interchanging `U` and `X` only in the description of the model, its
   branch sets are

   \[
        \{q_1\},\ldots,\{q_h\},\quad
        \{r_1\},\ldots,\{r_{4-h}\},\quad \{z,t\},                   \tag{2.2}
   \]

   where

   \[
   \begin{aligned}
      &1\le h\le3,\qquad q_i\in W,\qquad r_j,t\in S-\{s\},\\
      &z\in W',
   \end{aligned}                                                     \tag{2.3}
   \]

   and `{W,W'}={U,X}`.  In particular, all open-side singleton branch
   sets lie on one side, while the opposite side occurs only in the
   two-vertex branch set through its vertex `z`.

Consequently, under (1.2), applying the theorem to a minimum model in
`G-{s,v}` either gives the strict descent in outcome 1 or reduces every
remaining regenerated model to the single straddling form (2.2).

### Proof

Put

\[
                            T=S-\{s\}.                               \tag{2.4}
\]

In `G-{s,v}`, the sets `U` and `X` are anticomplete.  We first eliminate
models supported on only one closed side.

#### A model supported on the `X`-side

Suppose

\[
                       V(\mathcal N)\cap U=\varnothing.              \tag{2.5}
\]

Write the branch sets of `mathcal N` as `N_1,...,N_5`, put
`m=|V(mathcal N)|<=6`, and let `I` be the indices of branch sets disjoint
from `T`.  Set `h=|I|`.  If `h=0`, skip directly to the branch-set
construction below.  Otherwise choose one vertex `a_i in N_i` for each
`i in I`, and put

\[
 \begin{aligned}
     A&=\{a_i:i\in I\},\\
     Z&=(V(\mathcal N)-A)\cup\{s,v\},\\
     B&=T-V(\mathcal N).
 \end{aligned}                                                       \tag{2.6}
\]

If `b=|T cap V(mathcal N)|`, then `b<=m-h`, and hence

\[
                           |B|=7-b\ge7-m+h\ge h+1.                  \tag{2.7}
\]

There are `h` pairwise vertex-disjoint `A`--`B` paths in `G-Z`.
Otherwise set-Menger gives an `A`--`B` separator `D` in `G-Z` with
`|D|<=h-1`.  At least one vertex of each of `A` and `B` remains, while

\[
                         |Z\cup D|\le(m-h+2)+(h-1)=m+1\le7.         \tag{2.8}
\]

This contradicts seven-connectivity when the last order is at most six,
and gives an actual order-seven separation when it is seven.

Stop the paths on their first visits to `T`.  Before those visits they
cannot enter `U`: they start in `X`, the vertices `s,v` are deleted, and
every remaining passage from `X` to the rest of the graph meets `T`.
Enlarge the corresponding branch sets along these stopped paths.  All five
branch sets now meet `T`, remain pairwise disjoint, and preserve all their
old adjacencies.

The seven sets

\[
                 N_1,\ldots,N_5,\quad U,\quad\{s\},                 \tag{2.9}
\]

with the indicated enlargements, form a `K_7` minor: `U` and `s` are
adjacent, `U` is adjacent to every model row through its terminal in `T`,
and `s` is adjacent to every such terminal.  This contradicts the
hypothesis.  Therefore (2.5) is impossible.

#### A model supported on the `U`-side

Suppose next that

\[
                       V(\mathcal N)\cap X=\varnothing.              \tag{2.10}
\]

We define a six-vertex target set `B_0` and one exceptional boundary
vertex to be avoided.

If `y ne s`, put

\[
                         B_0=S-\{s,y\}.                              \tag{2.11}
\]

If `y=s`, choose

\[
                         z_0\in S-(\{s\}\cup V(\mathcal N)),        \tag{2.12}
\]

which is possible because `|S-{s}|=7` and the model has support at most
six, and put

\[
                         B_0=S-\{s,z_0\}.                            \tag{2.13}
\]

Let `I` now index the branch sets disjoint from `B_0`, and put `h=|I|`.
Choose one representative `a_i` from each such branch set.  When `y ne s`
and one of these branch sets contains `y`, choose `y` itself as its
representative.  Put `A={a_i:i in I}` and

\[
 Z=
 \begin{cases}
  (V(\mathcal N)-A)\cup\{s,v\}\cup(\{y\}-A),&y\ne s,\\
  (V(\mathcal N)-A)\cup\{s,v,z_0\},&y=s,
 \end{cases}                                                        \tag{2.14}
\]

and let

\[
                         B=B_0-V(\mathcal N).                         \tag{2.15}
\]

As before, every branch set meeting `B_0` accounts for a model vertex
outside the `h` unanchored branch sets.  Therefore

\[
                         |B|\ge6-m+h\ge h.                           \tag{2.16}
\]

If there are `h` disjoint `A`--`B` paths in `G-Z`, stop them on their
first visits to `B_0` and enlarge the corresponding model rows.  No
stopped path enters `X`.  For `y ne s`, every entrance to `X` uses `v` or
`S-{y}`; the vertices `s,v` are deleted and the path stops at its first
visit to `B_0`.  If a path starts at `y`, equation (1.1) says that it has
no edge into `X`.  For `y=s`, the only boundary vertex outside `B_0` is
the deleted vertex `z_0`, in addition to the deleted `s,v`.

All five enlarged rows consequently meet `B_0` and remain disjoint from
`X`.  Choose a component `C` of `X`.  If `y ne s`, then

\[
                    N_1,\ldots,N_5,\quad C,\quad\{s\}               \tag{2.17}
\]

is a `K_7` model: `C` and `s` are adjacent because `C` misses only `y`,
and both are adjacent to every model row through its terminal in `B_0`.
If `y=s`, replace the last two sets in (2.17) by

\[
                            C,\quad\{s,z_0\}.                       \tag{2.18}
\]

The second set is connected, it is adjacent to `C` through `z_0`, and
both sets are adjacent to every model row through `B_0`.  Again this is a
`K_7` model.  Hence the asserted linkage cannot exist.

Set-Menger therefore gives an `A`--`B` separator `D` in `G-Z` with
`|D|<=h-1`.  Both sides are nonempty by (2.16), and

\[
                              |Z\cup D|\le m+2\le8.                  \tag{2.19}
\]

Orders at most six contradict seven-connectivity, and order seven is an
actual order-seven separation.  Thus equality holds throughout (2.19):

\[
                      m=6,\qquad |D|=h-1,qquad |Z\cup D|=8.         \tag{2.20}
\]

When `y ne s`, equality also shows that `y` is outside the model support;
if it belonged to the support, the union in (2.14) would have one fewer
vertex and (2.19) would be at most seven.

Put `K=Z union D`, and let `L` be the union of the components of `G-K`
which contain a surviving member of `A-D`.  Then `L` is nonempty and the
whole support of `mathcal N` lies in `L union K`: every representative is
in `L union D`, while every other model vertex belongs to `Z`.

Moreover `L subsetneq U`.  Every vertex of `S` lies either in `K` or in
`B-D`; every component of `X` has a neighbour in `B-D` and therefore lies
on the opposite side of the separation.  The containment in `U` is
strict.  Indeed, if `L=U`, then `K` contains no vertex of `U`;
connectedness of `U` and the surviving source in `A-D` put all of `U` in
one component of `G-K`.  But a vertex of the nonempty set `B-D` has a
neighbour in `U` by boundary fullness, joining that target to the source
component and contradicting the separating property of `D`.  This proves
`L subsetneq U`.

Finally every component `C'` of `G-K` is adjacent to all eight vertices
of `K`.  Its neighbourhood is a subset of `K`; seven-connectivity gives
`|N(C')|>=7`, while equality would make `N(C')` an actual order-seven
separator because `G-K` has another nonempty side.  Therefore
`N(C')=K`.  This proves outcome 1.

#### Models meeting both open sides

The only remaining case is that `mathcal N` meets both `U` and `X`.
Its support cannot have order five, since five singleton branch sets form
a literal `K_5` and no singleton in `U` is adjacent to a singleton in
`X`.  Thus its support has order six, with four singleton branch sets and
one two-vertex branch set.

No singleton branch set in `U` can coexist with a singleton branch set in
`X`.  Hence all open-side singleton rows lie on one side `W`, and the
opposite side `W'` occurs in the two-vertex row.  Connectivity and the
absence of `U`--`X` edges force that row to have the form `{z,t}` with
`z in W'` and `t in T`.  This gives (2.2)--(2.3) with `1<=h<=4`.

If `h=4`, the vertex `t` must be adjacent to all four `q_i`, because `z`
has no neighbour in `W`.  Thus `t,q_1,q_2,q_3,q_4` form a support-five
`K_5` on one closed side.  The two one-side arguments above apply with
`m=5`; in the `U`-side argument (2.19) is then at most seven.  Hence that
literal `K_5` gives a `K_7` minor or an actual order-seven separation, both
excluded.  Therefore `h<=3`, proving outcome 2.  \(\square\)

## 3. Exact contribution and remaining obstruction

The shifted pair `{s,v}` is useful because it deletes the universal
boundary vertex and the old mixed-model endpoint simultaneously.  Global
support height at most six then regenerates a model, but Theorem 2.1 shows
that the model is not arbitrary:

- the shifted-shore-only orientation is impossible;
- the old-shore-only orientation carries the same pair and model into a
  strictly smaller full order-eight separation; and
- every nondecreasing return is an exact support-six mixed-shore model
  with at most three singleton rows on either open side.

The theorem does not yet compare the labels of the straddling model with
the four singleton rows of the original model.  That label-preserving
comparison is the remaining exchange problem.  Nor does the separation
descent decrease the original shifted-shore order `|X|`: it decreases the
opposite, regenerated-model shore.  It becomes a recursive induction only
after the proof spine allows full order-eight states ranked by the size of
the closed shore carrying the pair and model; the universal-boundary
property need not survive on the new eight-set.
