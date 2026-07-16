# Component exchange in the mixed-shore support-six model

**Status:** written proof with a separate GREEN internal audit in
[`hc7_mixed_shore_two_component_exchange_audit.md`](hc7_mixed_shore_two_component_exchange_audit.md).
The first theorem eliminates every component whose sole missing boundary
contact is the boundary endpoint of the two-vertex branch set.  The second
theorem shows, when three singleton branch sets lie in the other open shore,
that all surviving components have the same missing boundary contact.
Neither theorem proves `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph.  Let `S` be an eight-vertex separator
such that `G-S` has exactly two components `U,V`, and suppose every vertex
of `S` has a neighbour in each component.  Let `s\in S` be adjacent to
every vertex of `S-\{s\}`, and let `x\in S-\{s\}`.

Suppose `G-\{s,x\}` has a support-six `K_5`-minor model with branch sets

\[
       \{u_1\},\ldots,\{u_h\},
       \quad\{w_1\},\ldots,\{w_{4-h}\},
       \quad\{v,t\},                                   \tag{1.1}
\]

where

\[
       h\in\{2,3\},\quad u_i\in U,\quad v\in V,\quad
       t,w_j\in S-\{s,x\}.                             \tag{1.2}
\]

Thus the four vertices

\[
                         u_1,\ldots,u_h,w_1,\ldots,w_{4-h}       \tag{1.3}
\]

form a clique, and `t` is adjacent to every `u_i`.

Every component of `V-v` has a neighbour at `v`, because `V` is connected.

## 2. A component cannot miss only the edge endpoint

### Theorem 2.1

If a component `C` of `V-v` is adjacent to every vertex of `S-\{t\}`,
then `G` contains a `K_7` minor.

### Proof

Put

\[
        A=\{u_1,\ldots,u_h\},\qquad
        F_0=\{s,t,w_1,\ldots,w_{4-h}\},\qquad
        T=S-F_0.                                      \tag{2.1}
\]

The set `F_0` has order `6-h`, and hence

\[
                              |T|=h+2.                 \tag{2.2}
\]

Delete

\[
        Z=\{w_1,\ldots,w_{4-h},v,t,s\}.               \tag{2.3}
\]

Thus `|Z|=7-h`.  There are `h` pairwise vertex-disjoint `A`--`T`
paths in `G-Z`.  Otherwise, by Menger's theorem, a set `X` of order at
most `h-1` separates `A` from `T` in `G-Z`.  Since `|A|=h` and
`|T|=h+2`, both `A-X` and `T-X` are nonempty.  Then `Z\cup X` is a
separator of `G` of order at most

\[
                         (7-h)+(h-1)=6,
\]

contrary to seven-connectivity.

Stop the paths on their first visits to `T`.  Before those visits they do
not enter `C`: a path starting in `U` can enter `C` only through `v` or
through `S`; the vertex `v` and all boundary vertices outside `T` are in
`Z`.  The stopped paths are pairwise disjoint, avoid all five old branch
sets except at their respective initial vertices, and end at distinct
vertices of `T`.

Enlarge each branch set `\{u_i\}` along its corresponding path.  Together
with the unchanged sets `\{w_j\}`, denote the resulting four branch sets
by

\[
                              R_1,R_2,R_3,R_4.          \tag{2.4}
\]

They remain connected, pairwise disjoint, and pairwise adjacent.  The
following seven sets are branch sets of a `K_7`-minor model:

\[
              R_1,R_2,R_3,R_4,
              \quad \{v,t\},
              \quad C,
              \quad \{s\}.                            \tag{2.5}
\]

Indeed:

- `\{v,t\}` is adjacent to every `R_i` by the original `K_5` model;
- `C` is adjacent to every unchanged `w_j` and to the terminal in `T`
  added to every enlarged `U`-branch set;
- `C` is adjacent to `\{v,t\}` through an edge from `C` to `v`;
- `s` is adjacent to every `R_i` through the boundary vertex in that
  branch set;
- `s` is adjacent to `\{v,t\}` through `st`; and
- `s` is adjacent to `C`, since `s\ne t`.

All seven sets are connected and pairwise disjoint.  This verifies every
adjacency in (2.5) and proves the theorem. \(\square\)

### Corollary 2.2

Assume additionally that `G` is `K_7`-minor-free and has no actual
order-seven separation.  The component-contact theorem in
[`hc7_mixed_shore_component_contacts.md`](hc7_mixed_shore_component_contacts.md)
then implies that every component of `V-v` has exactly one missing boundary
contact, and that this contact belongs to

\[
                    \{s,t,w_1,\ldots,w_{4-h}\}.
\]

Theorem 2.1 eliminates `t`.  Hence every surviving component of `V-v`
misses `s` or one of the vertices `w_j`.

## 3. Alignment when three singleton branch sets lie in `U`

### Theorem 3.1

Assume `h=3`, and write `w=w_1`.  If `V-v` has components `C_s,C_w` such
that

\[
             N_S(C_s)=S-\{s\},\qquad
             N_S(C_w)=S-\{w\},                         \tag{3.1}
\]

then `G` contains a `K_7` minor.

### Proof

Put

\[
       A=\{u_1,u_2,u_3\},\qquad
       Z=\{w,v,t,s\},\qquad
       T=S-\{s,w,t\}.                                 \tag{3.2}
\]

Here `|Z|=4` and `|T|=5`.  There are three pairwise vertex-disjoint
`A`--`T` paths in `G-Z`.  Otherwise Menger's theorem gives an
`A`--`T` separator `X` in `G-Z` with `|X|\le2`; the sets `A-X` and
`T-X` are both nonempty, while

\[
                              |Z\cup X|\le6,
\]

contradicting seven-connectivity.

Stop the paths on their first visits to `T`.  As in Theorem 2.1, they
cannot enter `V-v` before those visits: the only other entrance from `U`
is through the deleted vertex `v`, and every boundary vertex outside `T`
is deleted.  Enlarge `\{u_i\}` along the three stopped paths and call the
resulting branch sets `R_i`.  Their distinct boundary terminals lie in
`T`, so they are all adjacent to both `C_s` and `C_w`.

Now take the following seven connected sets:

\[
       R_1,R_2,R_3,
       \quad C_s\cup\{w\},
       \quad\{t\},
       \quad C_w\cup\{v\},
       \quad\{s\}.                                    \tag{3.3}
\]

They are pairwise disjoint.  We check the adjacencies not inherited
immediately from the original model.

- Each `R_i` is adjacent to `C_s\cup\{w\}` through the original edge
  `u_iw`, to `\{t\}` through `u_it`, to `C_w\cup\{v\}` through its
  terminal in `T`, and to `\{s\}` through that same terminal.
- The sets `C_s\cup\{w\}` and `\{t\}` are adjacent because `C_s` is
  adjacent to `t`.
- The sets `C_s\cup\{w\}` and `C_w\cup\{v\}` are adjacent through an
  edge from `C_s` to `v`.
- The set `C_s\cup\{w\}` is adjacent to `\{s\}` through `ws`.
- The vertex `t` is adjacent to `C_w\cup\{v\}` through `tv`, and to
  `s` through `ts`.
- Finally, `C_w\cup\{v\}` is adjacent to `s` because `C_w` is adjacent
  to `s`.

Together with the retained clique adjacencies among `R_1,R_2,R_3`, these
are all pairs in (3.3).  Thus (3.3) is an explicit `K_7`-minor model.
\(\square\)

### Corollary 3.2

Under the hypotheses of Corollary 2.2 with `h=3`, all components of
`V-v` have the same missing boundary contact.  That common missed vertex
is either `s` or `w_1`.

### Proof

Corollary 2.2 leaves only the labels `s,w_1`.  If both labels occurred,
two components would satisfy (3.1), and Theorem 3.1 would give a `K_7`
minor. \(\square\)

## 4. Exact remaining cases

Together with the common-neighbour completion theorem, these results leave
only nonsingleton opposite shores.  Every component of `V-v` misses `s` or
one of the boundary singleton-model vertices `w_j`; when `h=3`, the missed
vertex is common to all components.  For `h=2`, the unresolved possibility
is that different components miss different vertices among
`s,w_1,w_2`.  Closing that case requires an additional label-preserving
composition, not merely another boundary-contact count.
