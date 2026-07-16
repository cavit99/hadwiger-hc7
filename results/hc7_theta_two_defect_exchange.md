# Two-defect exchange in the mixed-shore support-six model

**Status:** written proof with a separate GREEN internal audit in
[`hc7_theta_two_defect_exchange_audit.md`](hc7_theta_two_defect_exchange_audit.md).
The theorem closes the remaining different-contact case when two singleton
branch sets lie in one open component.  Although it arose from the
endpoint-rigid theta boundary, the proof uses only the named boundary clique
and is therefore strictly more general than the finite theta calculation.
It does not prove `HC_7`.

## 1. The exchange theorem

### Theorem 1.1

Let `G` be a seven-connected graph.  Let `S` be an eight-vertex separator
such that `G-S` has exactly two components `U,V`, and suppose every vertex
of `S` has a neighbour in each component.  Let `s\in S` be adjacent to
every vertex of `S-\{s\}`, and let `x\in S-\{s\}`.

Suppose `G-\{s,x\}` has a support-six `K_5`-minor model with branch sets

\[
              \{u_1\},\ \{u_2\},\ \{w_1\},\ \{w_2\},\ \{v,t\},       \tag{1.1}
\]

where

\[
       u_1,u_2\in U,\qquad v\in V,\qquad
       t,w_1,w_2\in S-\{s,x\}.                         \tag{1.2}
\]

Assume additionally that `t` is nonadjacent to at least one of
`w_1,w_2`.

Let `C,D` be distinct components of `V-v`.  Assume that for distinct
vertices

\[
                         y,z\in\{s,w_1,w_2\},          \tag{1.3}
\]

their boundary neighbourhoods are

\[
                         N_S(C)=S-\{y\},\qquad
                         N_S(D)=S-\{z\}.               \tag{1.4}
\]

Then `G` contains a `K_7` minor.

### Proof

The four singleton branch sets in (1.1) form a clique.  In particular,

\[
        u_1u_2,\ u_iw_1,\ u_iw_2,\ w_1w_2\in E(G)
        \quad(i=1,2),                                  \tag{1.5}
\]

and adjacency of `\{v,t\}` to `\{u_i\}` is necessarily supplied by
`tu_i`, because there is no edge between `U` and `V`.  Thus

\[
                              tu_1,tu_2\in E(G).        \tag{1.6}
\]

The mixed-shore normalization also says that `t` is nonadjacent to at
least one of `w_1,w_2`.

#### Anchoring the two `U`-branch sets

Put

\[
       A=\{u_1,u_2\},\qquad
       Z=\{s,t,w_1,w_2,v\},\qquad
       T=S-\{s,t,w_1,w_2\}.                            \tag{1.7}
\]

We have `|Z|=5` and `|T|=4`.  There are two pairwise vertex-disjoint
`A`--`T` paths in `G-Z`.  Otherwise set-Menger supplies an `A`--`T`
separator `X` in `G-Z` with `|X|\le1`.  Both `A-X` and `T-X` are
nonempty, so `Z\cup X` is a separator of `G` of order at most six,
contrary to seven-connectivity.

Stop both paths on their first visits to `T`.  Before those visits neither
path enters `V-v`: a path from `U` can do so only through the deleted
vertex `v` or through `S`, and every boundary vertex outside `T` is also
deleted.  Enlarge `\{u_1\},\{u_2\}` along the stopped paths and call the
resulting branch sets `R_1,R_2`.  Their distinct terminal vertices
`p,q\in T` satisfy

\[
           R_i\text{ is adjacent to }C,D,\text{ and }\{s\}
           \quad(i=1,2),                               \tag{1.8}
\]

because neither component misses a vertex of `T`, and `s` is complete to
`S-\{s\}`.  The old edges in (1.5)--(1.6) also give

\[
           R_i\text{ adjacent to }\{w_1\},\{w_2\},\{t\}
           \quad(i=1,2).                               \tag{1.9}
\]

Choose a vertex

\[
                              r\in T-\{p,q\}.          \tag{1.10}
\]

There are at least two choices, but only one is needed.  Each stopped path
contains no vertex of `T` other than its endpoint, so `r` lies in neither
`R_1` nor `R_2`.

#### The endpoint matching

For `b\in\{s,w_1,w_2\}`, define

\[
                 L(b)=\{e\in\{v,t\}:eb\in E(G)\}.     \tag{1.11}
\]

Every `L(b)` is nonempty.  This is clear for `b=s`, because `ts` is an
edge.  For `b=w_j`, it follows because the old branch set `\{v,t\}` is
adjacent to the singleton branch set `\{w_j\}`.

Suppose first that the two sets `L(y),L(z)` have distinct representatives.
After interchanging `C,D` if necessary, choose distinct

\[
                         e_C\in L(y),\qquad e_D\in L(z),
                         \qquad \{e_C,e_D\}=\{v,t\}.    \tag{1.12}
\]

The following seven sets form a `K_7`-minor model:

\[
       R_1,R_2,
       \quad C\cup\{e_C\},
       \quad D\cup\{e_D\},
       \quad\{s\},\quad\{w_1\},\quad\{w_2\}.         \tag{1.13}
\]

Both enlarged component sets are connected: every component of `V-v` has
a neighbour at `v`, and each is adjacent to `t` because its sole missing
boundary contact belongs to `\{s,w_1,w_2\}`.  Each enlarged component set
is adjacent to all three boundary singleton sets.  Its component supplies
the two contacts it does not miss, while its assigned endpoint supplies
the missed one.  The two enlarged component sets are adjacent through an
edge from the component containing `v` to `v` in the other set, or through
`vt`.  The three boundary vertices `s,w_1,w_2` form a clique, and
(1.8)--(1.9) give all their adjacencies to `R_1,R_2`.  Thus all 21 pairs
in (1.13) are adjacent.

It remains that `L(y),L(z)` have no distinct representatives.  Since they
are nonempty subsets of the two-element set `\{v,t\}`, Hall's condition
gives

\[
                              L(y)=L(z)=\{e\}           \tag{1.14}
\]

for one endpoint `e`.  There are exactly two forms.

#### Form A: both missed contacts are seen only by `v`

If `e=v`, neither `y` nor `z` is `s`, because `ts` is an edge.  Relabeling
`w_1,w_2` and `C,D` if necessary, we have

\[
        y=w_1,\quad z=w_2,\quad
        tw_1,tw_2\notin E(G),\quad vw_1,vw_2\in E(G).  \tag{1.15}
\]

Now use the seven branch sets

\[
       R_1,R_2,
       \quad C,
       \quad\{t\},
       \quad\{s\},
       \quad D\cup\{r\},
       \quad\{v,w_2\}.                                \tag{1.16}
\]

The last two nonsingleton sets are connected: `D` is adjacent to `r`, and
`vw_2` is an edge.  Each is adjacent to both `R_i`: the component `D`
sees `p,q`, while `w_2` is adjacent to the original vertices `u_i`.
The component `C` sees `p,q`, so it too is adjacent to both `R_i`.

Among the last five sets, `C,\{t\},\{s\}` form a triangle: `C` misses
only `w_1`.  The set `D\cup\{r\}` is adjacent to them respectively
through `Cr`, `Dt`, and `Ds`; the set `\{v,w_2\}` is adjacent to them
through `Cv`, `tv`, and `sw_2`.  Finally `D\cup\{r\}` is adjacent to
`\{v,w_2\}` through an edge from `D` to `v`.  These observations verify
all adjacencies in (1.16), giving a `K_7` minor.

#### Form B: both missed contacts are seen only by `t`

If `e=t`, the pair `\{y,z\}` cannot equal `\{w_1,w_2\}`, since `t` is
nonadjacent to at least one `w_j`.  Relabeling `w_1,w_2` and `C,D` if
necessary, we therefore have

\[
       y=s,\quad z=w_2,\quad
       tw_1\notin E(G),\quad tw_2\in E(G),
       \quad vs,vw_2\notin E(G).                       \tag{1.17}
\]

Use the seven branch sets

\[
       R_1,R_2,
       \quad C,
       \quad\{w_1\},
       \quad\{w_2\},
       \quad D\cup\{t\},
       \quad\{s,r\}.                                  \tag{1.18}
\]

The last two sets are connected because `D` sees `t` and `sr` is an
edge.  They are adjacent to both `R_i` through `t` and `s`, respectively.
The component `C` sees `p,q`, while `w_1,w_2` have their original edges
to `u_1,u_2`; hence the first five sets in (1.18) also have all required
adjacencies to `R_1,R_2`.

Among the last five sets, `C,\{w_1\},\{w_2\}` form a triangle because
`C` misses only `s` and `w_1w_2` is an edge.  The set `D\cup\{t\}` is
adjacent to them through `Ct`, `Dw_1`, and `tw_2`; the set `\{s,r\}` is
adjacent to them through `Cr`, `sw_1`, and `sw_2`.  Finally
`D\cup\{t\}` is adjacent to `\{s,r\}` through `ts` (and also through
`Ds`).  Thus (1.18) is a `K_7`-minor model.

The endpoint-matching case and Forms A and B exhaust all possibilities,
so the theorem follows. \(\square\)

## 2. Consequence for component contacts

### Corollary 2.1

Assume the endpoint-rigid mixed-shore setup, that `G` is `K_7`-minor-free,
and that `G` has no actual order-seven separation.  Then all components of
`V-v` have the same missing boundary contact.

### Proof

The separately audited component-contact and component-exchange theorems
show that every component has exactly one missing boundary contact, that
the missed vertex is `s` or one of the `w_j`, and that the conclusion
already holds when `h=3`.  When `h=2`, two distinct missing contacts would
satisfy Theorem 1.1 and give a `K_7` minor.  Thus they cannot occur.
\(\square\)

### Corollary 2.2 (shifted order-eight separation)

Under the hypotheses of Corollary 2.1, suppose `V-v` is nonempty and let
`y\in S` be the common missed boundary vertex.  Then

\[
                         N_G(V-v)=\{v\}\cup(S-\{y\}),  \tag{2.1}
\]

so `\{v\}\cup(S-\{y\})` is an actual separator of order eight.

### Proof

Every component of `V-v` is adjacent to `v` because `V` is connected, is
adjacent to every vertex of `S-\{y\}`, and has no neighbour at `y`.
There is no edge from `V-v` to `U`.  This proves (2.1).  Deleting the
displayed eight-set leaves the nonempty set `V-v` on one side and the
nonempty component `U` on another. \(\square\)

## 3. Exact remaining problem

The finite theta placement problem is therefore no longer open: all
components behind the two-vertex branch set have one common missed boundary
vertex, for both `h=2` and `h=3`.  The residue is an exact shifted
order-eight separation, not a list of local theta placements.

The next step must use contraction-criticality across that separation.  A
valid continuation must either synchronize a proper-minor colouring on its
two closed sides, regenerate a labelled model with a strict host-measured
decrease, or construct a `K_7` minor.  Contact counting alone has now been
exhausted.
