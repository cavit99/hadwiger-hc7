# A persistent edge need not have a tight endpoint after deletion

**Status:** written proof and explicit counterexample; separate audit pending.

This note determines the conclusion supplied by abstract list-criticality
when both `H` and `H-e` are vertex-minimal for the same list assignment.
The ends of `e` have positive excess in `H`, and tight vertices of `H`
have the usual Gallai-forest structure.  However, neither end of `e` need
be tight even in `H-e`.  An explicit eleven-vertex constant-list example
shows that a tighter conclusion must use the seven-connected host,
boundary contacts, or labelled minor-model data.

## 1. The exact general endpoint lemma

Let `H` be vertex-minimal subject to not being colourable from a list
assignment `L`.  Call an edge `e` **deletion-persistent** if `H-e` is also
not `L`-colourable.  A vertex `w` is **tight in a graph J** when

\[
                              d_J(w)=|L(w)|.             \tag{1.1}
\]

### Proposition 1.1

Let `e=uv` be deletion-persistent.  Then:

1. `H-e` is vertex-minimal subject to not being `L`-colourable;
2. every vertex `w` satisfies

   \[
                        d_{H-e}(w)\ge |L(w)|;            \tag{1.2}
   \]

   in particular

   \[
       d_H(u)\ge |L(u)|+1,
       \qquad d_H(v)\ge |L(v)|+1;                       \tag{1.3}
   \]
3. every edge incident with a vertex tight in `H` is
   deletion-essential: deleting that edge makes `H` `L`-colourable;
4. if `F_e` is a spanning edge-minimal non-`L`-colourable subgraph of
   `H-e`, then every edge of `H` incident with an `H`-tight vertex belongs
   to `F_e`, and the subgraph induced by the `H`-tight vertices is a Gallai
   forest;
5. if one endpoint, say `u`, is tight in `H-e`, then

   \[
                             d_H(u)=|L(u)|+1.            \tag{1.4}
   \]

#### Proof

Every proper induced subgraph of `H-e` is contained in a proper induced
subgraph of `H` and is therefore `L`-colourable.  Persistence of `e` proves
assertion 1.  Colouring `(H-e)-w` and greedily extending to `w` proves
(1.2); applying it to the ends of the removed edge proves (1.3).

If an edge `g` incident with an `H`-tight vertex were deletion-persistent,
then (1.3), applied to `g`, would contradict tightness.  This proves
assertion 3.

Choose `F_e` by deleting edges from `H-e` while retaining
non-`L`-colourability.  It is still vertex-minimal, and hence

\[
                            d_{F_e}(w)\ge |L(w)|         \tag{1.5}
\]

for every vertex.  If `w` is tight in `H`, then `w` is not an endpoint of
`e` by (1.3), and

\[
 |L(w)|\le d_{F_e}(w)\le d_{H-e}(w)=d_H(w)=|L(w)|.
\]

Thus every edge incident with `w` is retained in `F_e`, and `w` is tight
there.  The degree-choosability theorem applied to the tight-vertex
subgraph of the vertex-minimal graph `F_e` says that each of its blocks is
complete or an odd cycle.  Since all edges among the `H`-tight vertices
are retained, the same holds in `H`.  This proves assertion 4.

Finally, if `u` is tight in `H-e`, restoring its one incident deleted edge
increases its degree by exactly one, which is (1.4). \(\square\)

### Corollary 1.2 (the boundary consequence of endpoint tightness)

Consider the shore-filling setting of the fixed-boundary list-critical
reduction with six colours.  Thus `H=G[D]`,

\[
 L_c(w)=[6]-c(N_G(w)\cap X),
\]

and define

\[
 \rho(w)=|N_G(w)\cap X|-|c(N_G(w)\cap X)|.              \tag{1.6}
\]

If an endpoint `w` of a deletion-persistent edge is tight in `H-e`, then
either `rho(w)>=1`, so two literal boundary neighbours of `w` receive the
same colour, or `N_G(w)` is an actual order-seven separator.

#### Proof

There are no vertices of the shore outside the shore-filling critical
subgraph.  The fixed-boundary degree identity and Proposition 1.1 give

\[
 d_G(w)=6+\bigl(d_H(w)-|L_c(w)|\bigr)+\rho(w)
       =7+\rho(w).                                      \tag{1.7}
\]

If `rho(w)>=1`, the first conclusion is its definition.  If `rho(w)=0`,
then `d_G(w)=7`.  The set `N_G(w)` separates `w` from the nonempty opposite
shore, so it is an actual order-seven separator. \(\square\)

Corollary 1.2 is the useful tight-endpoint outcome.  The next section shows
that abstract list-criticality cannot guarantee that outcome.

## 2. The Grötzsch-graph counterexample

Let indices be read modulo five.  Define the Grötzsch graph `F`, the
Mycielskian of the five-cycle, on

\[
                 \{x_0,\ldots,x_4,y_0,\ldots,y_4,z\}.   \tag{2.1}
\]

Its edges are

\[
 x_ix_{i+1},\qquad x_i y_{i+1},\qquad x_{i+1}y_i,
 \qquad zy_i\quad (i\in\mathbb Z_5).                   \tag{2.2}
\]

Put

\[
                         H=F+x_0x_2                    \tag{2.3}
\]

and give every vertex the constant list

\[
                              L(w)=\{1,2,3\}.           \tag{2.4}
\]

### Proposition 2.1

Both `H` and `H-x_0x_2=F` are vertex-minimal non-`L`-colourable, but

\[
                       d_F(x_0)=d_F(x_2)=4>|L(x_0)|.    \tag{2.5}
\]

Thus the deletion-persistent edge `x_0x_2` has no tight endpoint even
after it is deleted.

#### Proof

First, `F` is not three-colourable.  If it had a three-colouring, rename
the colour of `z` as colour 3.  Every `y_i` then has colour 1 or 2.  For
each original vertex `x_i` of colour 3, recolour `x_i` with the colour of
`y_i`.  Adjacent original vertices cannot both initially have colour 3;
and if only `x_i` is recoloured across an edge `x_ix_j`, then `y_i` is
adjacent to `x_j`.  The recolouring therefore gives a proper two-colouring
of the original five-cycle, a contradiction.  Hence neither `F` nor its
supergraph `H` is `L`-colourable.

The following colour classes give a proper four-colouring of `H`:

\[
 \{x_0,x_3,z\},\quad
 \{x_2,x_4,y_2,y_4\},\quad
 \{x_1,y_1,y_3\},\quad
 \{y_0\}.                                               \tag{2.6}
\]

It remains to verify vertex minimality.  The reflection

\[
 x_0\leftrightarrow x_2,quad x_3\leftrightarrow x_4,quad
 y_0\leftrightarrow y_2,quad y_3\leftrightarrow y_4              \tag{2.7}
\]

fixing `x_1,y_1,z` is an automorphism of `H`.  It therefore suffices to
give three-colourings after deleting one representative of each of its
seven vertex orbits.  The three entries in each row below are the colour
classes.

| deleted vertex | colour 1 | colour 2 | colour 3 |
|---|---|---|---|
| `x_0` | `x_2,x_4,z` | `x_1,x_3,y_1,y_3` | `y_0,y_2,y_4` |
| `x_1` | `x_0,x_3,z` | `x_2,x_4,y_2,y_4` | `y_0,y_1,y_3` |
| `x_3` | `x_0,y_0,y_2,y_3` | `x_2,x_4,z` | `x_1,y_1,y_4` |
| `y_0` | `x_0,x_3,z` | `x_2,x_4,y_2,y_4` | `x_1,y_1,y_3` |
| `y_1` | `x_0,x_3,y_0,y_3` | `x_1,x_4,z` | `x_2,y_2,y_4` |
| `y_3` | `x_0,x_3,z` | `x_1,x_4,y_1,y_4` | `x_2,y_0,y_2` |
| `z` | `x_0,x_3,y_0,y_3` | `x_2,x_4,y_2,y_4` | `x_1,y_1` |

Each row is checked directly from (2.2)--(2.3).  It colours `H-w`, and
therefore also its subgraph `F-w`.  Thus both `H` and `F` are
vertex-minimal non-`L`-colourable.  Finally, in `F` each original
five-cycle vertex has its two cycle neighbours and two clone neighbours,
which proves (2.5). \(\square\)

### Corollary 2.2 (a six-chromatic constant-list instance)

For every `r>=0`, put

\[
             F_r=K_r\vee F,
 \qquad      H_r=K_r\vee H,                              \tag{2.8}
\]

and give every vertex the constant list `[r+3]`.  Then `F_r` and `H_r`
are both vertex-minimal non-list-colourable, `H_r-x_0x_2=F_r`, and

\[
 d_{F_r}(x_0)=d_{F_r}(x_2)=r+4>r+3.                     \tag{2.9}
\]

In particular, `r=2` gives a six-chromatic pair with constant
five-element lists and a deletion-persistent edge whose two endpoints are
already non-tight after deletion.

#### Proof

Chromatic number is additive under a complete join.  Propositions 2.1 and
its displayed deletion colourings give

\[
 \chi(F_r)=\chi(H_r)=r+4.
\]

Deleting a vertex of the `K_r` factor lowers its contribution by one;
deleting a vertex of `F` or `H` lowers the other factor to a
three-colourable graph.  Thus both joins are vertex-minimal
`(r+4)`-chromatic graphs, equivalently vertex-minimal obstructions to their
constant `(r+3)`-element lists.  The edge identity is immediate from the
join construction, and every old vertex gains exactly `r` neighbours,
which proves (2.9). \(\square\)

## 3. Exact scope of the barrier

Proposition 2.1 refutes each abstract assertion that

* a deletion-persistent edge in a vertex-minimal list obstruction must
  have an endpoint tight after deletion;
* positive endpoint excess must be concentrated solely in the restored
  edge; or
* the two paired vertex-minimal obstructions alone yield a smaller
  list-critical kernel.

Corollary 2.2 shows that the failure persists at the six-chromatic scale
and is not an artefact of three-element lists.

The example is not asserted to be a hypothetical `HC_7` counterexample,
an asymmetric order-eight shore, seven-connected as a host, or equipped
with the labelled spanning near-`K_7` model.  In particular, it does not
refute a theorem which uses literal boundary repetitions, a prescribed
donor branch set, global `K_7`-minor exclusion, or proper-minor colouring
responses in the full host.

Consequently the high-after-deletion branch

\[
        d_{H-e}(u)>|L(u)|,qquad d_{H-e}(v)>|L(v)|        \tag{3.1}
\]

cannot be closed by the standard Gallai-forest or degree-choosability
theorems alone.  A valid continuation must couple the endpoint excess to
literal boundary contacts or to the five named branch sets of the
deletion-persistent near-complete minor model.

## 4. Reference

The degree-choosability characterization used in Proposition 1.1 is the
Borodin--Erdős--Rubin--Taylor theorem; see P. Erdős, A. L. Rubin and
H. Taylor, *Choosability in graphs*, Congressus Numerantium 26 (1979),
125--157.
