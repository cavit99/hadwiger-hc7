# A cross-pair perfect matching at the balanced order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_balanced_cross_matching_normalization_audit.md`](hc7_balanced_cross_matching_normalization_audit.md).
This theorem is a label-preserving normalization inside the balanced
order-eight branch.  It does not align the two closed-shore colouring
extensions and does not prove `HC_7`.

## 1. Boundary matching lemma

### Lemma 1.1

Let

\[
 S=R\mathbin{\dot\cup}A\mathbin{\dot\cup}B
       \mathbin{\dot\cup}\{x\},
 \qquad |R|=3,\quad |A|=|B|=2,
\]

and let `J` be a graph on `S`.  Assume that

1. `R` is a clique in `J`;
2. `J[A]` and `J[B]` are edges;
3. `A` is anticomplete to `B` in `J`;
4. for each of `A` and `B`, the two endpoint nonneighbour sets in `R`
   are nonempty and disjoint; and
5. `I_2 vee J` has no `K_7` minor.

Put `F=overline J`, and suppose that `F` has a perfect matching.  If no
perfect matching of `F` contains an edge with one end in `A` and the other
in `B`, then

\[
       N_F(x)=A\cup B,
\]

relative to the seven other boundary vertices.  Equivalently, in `J` the
vertex `x` is complete to `R` and anticomplete to `A union B`.

### Proof

Because `R` is independent in `F`, every perfect matching matches each of
its three vertices outside `R`.  If a perfect matching matches `x` to a
vertex of `R`, its remaining three edges use the four vertices of
`A union B` and the other two vertices of `R`.  Exactly one of those
three edges therefore has both ends in `A union B`.  The only edges of
`F[A union B]` are the four edges between `A` and `B`, so that edge is an
`A`--`B` edge.  By hypothesis this never happens.  Hence every perfect
matching matches `x` to a vertex of `A union B` and matches the three
vertices of `R` bijectively to the other three endpoints.

Fix one perfect matching.  By symmetry, write

\[
  A=\{a,b\},\quad B=\{c,d\},
\]

and relabel `R={r_1,r_2,r_3}` so that the matching is

\[
             xa,\quad r_1b,\quad r_2c,\quad r_3d.       \tag{1.1}
\]

The nonempty `F`-neighbour set of `a` in `R` is disjoint from that of
`b`.  Since `br_1` is an edge of `F`, the vertex `a` has an `F`-neighbour
in `{r_2,r_3}`.

We show first that `x` has no `F`-neighbour in `R`.  If `xr_2` is an edge,
then

\[
             xr_2,\quad ac,\quad br_1,\quad dr_3
\]

is a perfect matching containing the cross edge `ac`; if `xr_3` is an
edge, use

\[
             xr_3,\quad ad,\quad br_1,\quad cr_2.
\]

Finally suppose `xr_1` is an edge.  If `ar_2` is an edge, then

\[
             xr_1,\quad bc,\quad ar_2,\quad dr_3
\]

is the forbidden matching.  Otherwise the preceding paragraph forces
`ar_3` to be an edge, and

\[
             xr_1,\quad bd,\quad ar_3,\quad cr_2
\]

is the forbidden matching.  Thus `x` is anticomplete to `R` in `F`, or
equivalently complete to `R` in `J`.

It remains to show that `x` is complete to `A union B` in `F`.  We already
have `xa in E(F)` from (1.1).  If `xb` were an edge of `J`, then the five
sets

\[
             \{r\}\ (r\in R),\qquad \{x\},\qquad A
                                                               \tag{1.2}
\]

would be a `K_5`-minor model in `J` supported on six vertices.  The set
`A` is connected, is adjacent to every vertex of `R` by collective
adjacency, and meets `{x}` through `xb`; while `R union {x}` is a clique.
If `p,q` denote the two nonadjacent universal vertices in `I_2 vee J`,
choose an unused boundary vertex `w`.  Then the five sets in (1.2),
together with `{p,w}` and `{q}`, form a `K_7`-minor model, contrary to
hypothesis 5.  Therefore `xb in E(F)`.

The same argument with the connected edge `B` shows that neither `xc` nor
`xd` can be an edge of `J`: either one would make `B`, the three singleton
vertices of `R`, and `{x}` a six-vertex `K_5` model in `J`, and hence give
a `K_7` minor in `I_2 vee J`.  Thus all four edges from `x` to
`A union B` belong to `F`, completing the proof. \(\square\)

## 2. Host-level completion

### Theorem 2.1

Let `G` contain an eight-vertex separator

\[
       S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
              \mathbin{\dot\cup}\{x\},\qquad |R|=3,
\]

and suppose:

1. `R` is a clique;
2. `e,f` are disjoint anticomplete edges, each collectively adjacent to
   every vertex of `R`;
3. `G-S` has two connected components `C,D`, each adjacent to every
   vertex of `S`;
4. `C` contains adjacent vertices `ell_e,ell_f`, each adjacent to every
   vertex of `R`;
5. `e` is anticomplete to `ell_e` and has a neighbour at `ell_f`, while
   `f` is anticomplete to `ell_f` and has a neighbour at `ell_e`; and
6. the graph

   \[
                   H=C-\{ell_e,ell_f\}
   \]

   is connected, is met by each of `ell_e,ell_f,x`, and has a neighbour
   in each of `V(e),V(f)`.

Put `J=G[S]`.  Assume the endpoint nonneighbour sets in `R` satisfy
Lemma 1.1(4), that `I_2 vee J` has no `K_7` minor, and that
`overline J` has a perfect matching.  Then either `G` has a `K_7` minor,
or `overline J` has a perfect matching containing an edge between
`V(e)` and `V(f)`.

### Proof

Suppose no such cross-pair perfect matching exists.  Lemma 1.1 says that
`x` is complete in `J` to `R` and anticomplete to
`V(e) union V(f)`.  Consider the seven sets

\[
 \{r\}\ (r\in R),\qquad
 V(e)\cup\{ell_f\},\qquad
 V(f)\cup\{ell_e\},\qquad
 V(H)\cup\{x\},\qquad
 V(D).                                                 \tag{2.1}
\]

They are pairwise disjoint.  They are connected: the second and third
sets use the cross-index contacts in hypothesis 5, `H union {x}` is
connected by hypothesis 6, and `D` is connected.

We check all adjacencies.  The three singleton sets form a clique.  Each
is adjacent to the two leaf-and-edge sets through the corresponding leaf,
to `H union {x}` through `x`, and to `D` by boundary fullness.  The two
leaf-and-edge sets are adjacent through `ell_e ell_f`.  Each is adjacent
to `H union {x}` through its leaf (and also through the relevant boundary
contact from `H`), and to `D` through an endpoint of its boundary edge.
Finally `H union {x}` is adjacent to `D` through the boundary vertex `x`.
Thus the seven sets in (2.1) are pairwise adjacent connected branch sets,
and form a `K_7`-minor model in `G`. \(\square\)

### Corollary 2.2 (a shared missing clique contact)

Under hypotheses 1--6 of Theorem 2.1, if `G` has no `K_7` minor, then
there is a vertex `r in R` such that

\[
        xr\notin E(G)
        \quad\text{and}\quad
        N_G(r)\cap V(H)=\varnothing.                  \tag{2.2}
\]

### Proof

If no such vertex existed, use the seven branch sets in (2.1).  The
connectivity and every adjacency not involving an `R` singleton are
verified exactly as in Theorem 2.1.  For each `r in R`, either `xr` is an
edge or `H` has a neighbour at `r`; hence the branch set
`H union {x}` is adjacent to `{r}`.  The other three nonsingleton branch
sets are adjacent to every vertex of `R` through the two clique leaves and
boundary fullness.  Thus (2.1) would again be an explicit `K_7`-minor
model. \(\square\)

## 3. Consequence for the balanced branch

In the active balanced order-eight configuration, hypotheses 1--5 of
Theorem 2.1 are part of the exact star boundary.  Hypothesis 6 is the
independently audited conclusion of the disconnected-leaf-side completion
after excluding a `K_7` minor and an actual order-seven separation.  The
join-minor exclusion follows by contracting the two boundary-full open
components.  Therefore every surviving balanced host admits a perfect
matching of `overline{G[S]}` whose unique edge internal to
`V(e) union V(f) union {x}` joins an endpoint of `e` to an endpoint of
`f`; the other three matching edges pair `x` and the two remaining defect
endpoints with the three vertices of `R`.

This normalization is host-level and label-preserving.  It is stronger
than merely knowing that the boundary has a four-pair colouring.  It does
not show that this four-pair partition extends through either closed shore.
Corollary 2.2 supplies one further host constraint: the connected
leaf-side interior and `x` have a common missed vertex in `R`.  A later
matching exchange must preserve this literal label rather than only the
abstract four-pair partition.
