# Response propagation across the two cutvertex lobes

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_cutvertex_lobe_response_propagation_audit.md`](hc7_order8_cutvertex_lobe_response_propagation_audit.md).  This is a conditional
result inside the connected order-eight opposite-response branch.  It
assumes the exact two-lobe cutvertex structure stated below; it does not
prove that every surviving order-eight interface has that structure, and it
does not prove `HC_7`.

## 1. Setting

Let `G` be a graph with

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le 6\quad\hbox{for every proper minor }M\hbox{ of }G.
 \tag{1.1}
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \tag{1.2}
\]

where

\[
 S=\{d,e\}\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
 \qquad |X|=|Y|=3.
 \tag{1.3}
\]

Assume that `X,Y` are independent and that there are proper six-colourings
with the following boundary equality partitions:

* a colouring `c_L` of `G[L union S]` induces

  \[
                    X\mid Y\mid\{d,e\};
  \tag{1.4}
  \]

* a colouring `c_R` of `G[R union S]` induces

  \[
                    X\mid Y\mid\{d\}\mid\{e\}.
  \tag{1.5}
  \]

Thus each displayed block is monochromatic and different displayed blocks
have different colours.  Assume moreover that every six-colouring of
`G[R union S]` in which `X,Y` are distinct monochromatic blocks and `d,e`
avoid both block colours has `c(d) != c(e)`.  This is the assertion that the
closed `R`-shore has only the split response.

Assume also, as in the live connected-shore normalization, that `R`
contains vertex-disjoint connected subgraphs `P_0,P_1`, each adjacent to
every literal vertex of `S`, and that there is a `P_0`--`P_1` edge.  These
named subgraphs are retained because a terminal `K_7`-minor construction
must preserve their literal labels; the response propagation below does not
infer those labels from colours.

Let `z in L`.  Assume that `G[L]-z` has exactly two components `C_d,C_e`,
and that their full neighbourhoods in `G` are

\[
 \begin{split}
 N_G(C_d)&=\{z\}\mathbin{\dot\cup}(S-\{e\}),\\
 N_G(C_e)&=\{z\}\mathbin{\dot\cup}(S-\{d\}).
 \end{split}
 \tag{1.6}
\]

Finally assume that `c_L(z)=c_L(d)=c_L(e)`.  Properness of `c_L` gives the
three facts which will be used repeatedly:

\[
                    zd,ze,de\notin E(G).
\tag{1.7}
\]

The two exact order-eight boundaries exposed by the lobes are

\[
 B_d=\{z\}\mathbin{\dot\cup}(S-\{e\}),
 \qquad
 B_e=\{z\}\mathbin{\dot\cup}(S-\{d\}).
 \tag{1.8}
\]

For `r in {d,e}`, call a six-colouring of a closed side of `B_r`
**admissible** if `X,Y` are distinct monochromatic blocks and `z,r` avoid
both block colours.  Its equality type records whether `z` and `r` have the
same colour.

## 2. The two boundaries have opposite singleton responses

### Theorem 2.1

For the boundary `B_d`:

1. the closed lobe `G[C_d union B_d]` has equality response and no
   inequality response;
2. the complementary closed side `G-C_d` has inequality response and no
   equality response; and
3. in every admissible colouring of `G-C_d`,

   \[
                         c(z)=c(e)\ne c(d).
   \tag{2.1}
   \]

Symmetrically, for `B_e`, the closed `C_e`-side has only equality response,
the complementary side `G-C_e` has only inequality response, and every
admissible colouring of `G-C_e` satisfies

\[
                         c(z)=c(d)\ne c(e).
\tag{2.2}
\]

#### Proof

Restrict `c_L` to `G[C_d union B_d]`.  This is admissible and has
`c_L(z)=c_L(d)`, so the equality response on the lobe side is nonempty.

We next construct an inequality response on `G-C_d`, checking explicitly
that the recolouring is proper.  Write the four colours used by `c_R` on
the blocks in (1.5) as

\[
                  \xi_X,\xi_Y,\delta,\varepsilon,
\tag{2.3}
\]

respectively.  They are pairwise distinct.  Permute the six colour names
in `c_L` so that its colours on `X,Y,\{d,e,z\}` become

\[
                  \xi_X,\xi_Y,\varepsilon.
\tag{2.4}
\]

Restrict this permuted colouring to

\[
                     G[C_e\cup\{z\}\cup S]
\tag{2.5}
\]

and change the colour of `d` from `\varepsilon` to `\delta`.  By (1.6), no
vertex of `C_e` is adjacent to `d`.  By (1.7), `d` is adjacent to neither
`z` nor `e`.  All remaining possible neighbours of `d` in (2.5) lie in
`X union Y`, whose colours are `\xi_X,\xi_Y`.  Since `\delta` differs from
both, the recolouring is proper.

The recoloured graph (2.5) and `c_R` now agree on every literal vertex of
`S`.  There are no edges from `C_e union {z}` to `R`, by (1.2).  They
therefore glue to a proper six-colouring of `G-C_d`.  On `B_d` it induces

\[
X\mid Y\mid\{z\}\mid\{d\},
\qquad c(z)=c(e)=\varepsilon,\quad c(d)=\delta.
\tag{2.6}
\]

Thus the complementary inequality response is nonempty.

If either closed side of `B_d` admitted the other equality type, the two
closed sides would have a common admissible type.  Permuting colour names
on one side would align the three blocks in the equality case or the four
blocks in the inequality case.  The two open sides are anticomplete, so the
aligned colourings would glue across the literal boundary `B_d` to a proper
six-colouring of `G`, contrary to (1.1).  Hence the two response sets are
the claimed opposite singletons.

It remains to prove that (2.1) holds in *every* complementary admissible
colouring, not only in (2.6).  Let `c` be such a colouring and let
`\alpha=c(z)`, `\beta=c(d)`.  They are distinct.  If `z,d` lay in different
components of the subgraph induced by colours `\alpha,\beta`, swapping these
two colours on the component containing `z` would make `z,d` equal.  The
vertices of `X union Y` use neither `\alpha` nor `\beta`, so the swap would
remain admissible.  This contradicts the singleton response just proved.
Consequently there is an `alpha`--`beta` path from `z` to `d` whose
internal vertices avoid `B_d`.

Every such path contains `e`.  Indeed, after deleting
`B_d-\{z,d\}`, its internal vertices lie in

\[
                         C_e\mathbin{\dot\cup}\{e\}
                         \mathbin{\dot\cup}R.
\tag{2.7}
\]

There are no `C_e`--`R` edges by (1.2), `C_e` has no neighbour at `d` by
(1.6), and `z` has no edge to `e` or `d` by (1.7).  Thus the path must run
from `z` into `C_e`, pass through `e`, enter `R`, and end at `d`.

In particular `c(e)` is one of `\alpha,\beta`, and hence avoids the two block
colours.  Restricting `c` to `G[R union S]` gives an admissible response on
that shore.  Its response is split by hypothesis, so
`c(e) != c(d)=\beta`.  It follows that `c(e)=\alpha=c(z)`, proving (2.1).

The proof for `B_e` is obtained by interchanging `d,C_d,\delta` with
`e,C_e,\varepsilon`.  In the construction, map the merged root colour to
`\delta`, restrict to `C_d union {z} union S`, and recolour `e` to
`\varepsilon`.  Equations (1.6) and (1.7) give the same properness check.
The Kempe path from `z` to `e` must pass through `d`, and the split response
on `R` gives (2.2).  This completes the proof.  \(\square\)

### Corollary 2.2

Both `G[C_d]` and `G[C_e]` are nonbipartite.  Consequently each contains a
`K_3` minor.

#### Proof

If, for example, `G[C_d]` were bipartite, colour the four independent
blocks

\[
                       X,\quad Y,\quad\{z\},\quad\{d\}
\]

with four distinct colours and colour `C_d` with the other two colours.
This is a proper colouring of `G[C_d union B_d]` with the inequality
response, contrary to Theorem 2.1.  The argument for `C_e` is symmetric.
A connected nonbipartite graph contains an odd cycle, which contracts to a
`K_3` minor. \(\square\)

## 3. The crossed six-colouring of `G-z`

### Theorem 3.1

There is a proper six-colouring `psi` of `G-z` which induces the split
partition (1.5) on `S` and has the following crossed-neighbour property.
Put

\[
                         \delta=\psi(d),
 \qquad                  \varepsilon=\psi(e).
\tag{3.1}
\]

Then

\[
 \begin{array}{ll}
 N_G(z)\cap C_d\text{ contains no vertex of colour }\delta,
 &N_G(z)\cap C_d\text{ contains a vertex of colour }\varepsilon,\\[2mm]
 N_G(z)\cap C_e\text{ contains no vertex of colour }\varepsilon,
 &N_G(z)\cap C_e\text{ contains a vertex of colour }\delta.
 \end{array}
\tag{3.2}
\]

#### Proof

Choose one complementary colouring from each part of Theorem 2.1.  Permute
the colour names of the `G-C_e` colouring so that the two colourings induce
the same four literal blocks, with the same four colours, on `S`.

Use the `G-C_d` colouring on `C_e union R union S`, and use the aligned
`G-C_e` colouring on `C_d`.  Delete `z`.  The two lobe colourings agree
with the chosen colouring on every vertex of `S`; there are no
`C_d`--`C_e` edges and no edges from either lobe to `R`.  This defines a
proper six-colouring `psi` of `G-z`.

In the `G-C_e` colouring, `z` had colour `\delta` by (2.2).  Therefore none
of its neighbours in `C_d` has colour `\delta`.  Similarly, in the
`G-C_d` colouring, `z` had colour `\varepsilon` by (2.1), so none of its
neighbours in `C_e` has colour `\varepsilon`.  This proves the two
nonoccurrence assertions in (3.2).

Every one of the six colours occurs in `N_G(z)` under `psi`: otherwise a
missing colour could be assigned to `z`, producing a proper six-colouring
of `G`, contrary to (1.1).  The vertex `z` has no neighbour in `R`, and by
(1.7) it has no neighbour at `d` or `e`.  Its neighbours in `S` lie in
`X union Y`, whose two colours are different from `\delta,\varepsilon`.
Since colour `\delta` is absent from `N_G(z) cap C_d`, it must occur in
`N_G(z) cap C_e`.  Symmetrically colour `\varepsilon` must occur in
`N_G(z) cap C_d`.  This proves the two occurrence assertions. \(\square\)

Define the two nonempty literal sets

\[
 \begin{split}
 Z_d&=N_G(z)\cap C_e\cap\psi^{-1}(\delta),\\
 Z_e&=N_G(z)\cap C_d\cap\psi^{-1}(\varepsilon).
 \end{split}
\tag{3.3}
\]

Deleting all edges from `z` to `Z_d` makes `psi` extend to `z` with colour
`\delta`; deleting all edges from `z` to `Z_e` makes it extend with colour
`\varepsilon`.  Thus (3.3) also gives two explicit, operation-supported
proper-minor colourings.  If one of these sets is a singleton, the
corresponding operation is a single edge deletion.

### Lemma 3.2 (operation-specific saturation at every crossed edge)

For every `u in Z_d` and `v in Z_e`, every proper six-colouring of
`G-zu` gives `z,u` the same colour, and every proper six-colouring of
`G-zv` gives `z,v` the same colour.  In any such colouring, each endpoint
of the deleted edge has a neighbour in every one of the other five colour
classes.

#### Proof

The edge-deleted graph is a proper minor and hence has a proper
six-colouring by (1.1).  If the ends of the deleted edge received different
colours, restoring the edge would give a proper six-colouring of `G`.
Therefore the ends have one common colour.

If one endpoint had no neighbour in some other colour, recolour that
endpoint with the missing colour.  Its colour would then differ from the
colour of the other endpoint, so the deleted edge could again be restored.
This would six-colour `G`, a contradiction.  The argument applies at both
ends and to either family of edges. \(\square\)

### Proposition 3.3 (the named full subgraphs cannot both descend)

Relative to the boundary `B_d`, at most one of two vertex-disjoint
connected subgraphs in the complementary open side can both meet `R` and
be adjacent to `z`.  Consequently the two literal subgraphs `P_0,P_1`
cannot both be extended, disjointly, to connected `B_d`-full subgraphs.
The symmetric statement holds for `B_e`.

#### Proof

The complementary open side of `B_d` is

\[
                         C_e\mathbin{\dot\cup}\{e\}
                         \mathbin{\dot\cup}R.
\tag{3.4}
\]

There are no `C_e`--`R` edges.  Within (3.4), every path from `C_e` to
`R` contains `e`: all other vertices of `S` belong to the boundary `B_d`,
and hence do not belong to the open side.  Moreover a subgraph of (3.4)
which is adjacent to `z` must meet `C_e`, because `z` has no neighbour in
`R` by (1.2) and no edge to `e` by (1.7).

It follows that every connected subgraph of (3.4) which meets `R` and is
adjacent to `z` contains the literal vertex `e`.  Two such subgraphs cannot
be vertex-disjoint.  Any connected extension of `P_i` which is full to
`B_d` must meet `R` and must be adjacent to `z`, so this applies to
`P_0,P_1`.  Interchanging `d,C_d` with `e,C_e` proves the statement for
`B_e`; there the unique internal joining vertex is `d`. \(\square\)

## 4. Exact gain and remaining label-preserving obstruction

Theorem 2.1 transfers the omitted root through each exact order-eight
boundary: on the complementary side of `B_d`, the cutvertex `z` is forced
to share the colour of `e`, and on the complementary side of `B_e` it is
forced to share the colour of `d`.  Theorem 3.1 combines the two transfers
without identifying a palette colour with a branch-set label.

The conclusion is not yet one of the terminal outcomes of the active
order-eight programme.  Membership of a vertex in `Z_d` says only that it
has the same **colour** as the literal boundary vertex `d`; structurally it
lies in `C_e`, whose full neighbourhood omits `d`.  Likewise `Z_e` lies in
`C_d`, whose full neighbourhood omits `e`.  Colour equality supplies no
edge, connected subgraph, or first-hit assignment to a named minor-model
branch set.  In particular, because there are no `L`--`R` edges, neither
crossed neighbour set meets the named boundary-full subgraphs `P_0,P_1`; their
existence does not assign either palette contact to one of those literal
labels.  Permuting the colours unused on the four boundary blocks can
also change the remaining neighbour-colour allocation without changing any
literal branch-set incidence.

After the colours are forgotten, the nonemptiness of `Z_d,Z_e` adds no new
host edge at all: (1.6) already says that `z` has a neighbour in each lobe.
The new assertion is solely which boundary colour occurs on such a
neighbour.  Therefore a branch-set conclusion cannot follow from the
uncoloured incidence of (3.3); it must use a further Kempe component or a
specific deletion/contraction response that carries literal first-hit data.

Consequently the inherited data prove precisely the crossed nonempty sets
(3.3), not a labelled split of either lobe.  A further theorem must use an
operation-specific colouring after deleting or contracting an edge in
`zZ_d` or `zZ_e` to obtain one of:

1. a connected subgraph with the required literal contacts to the named
   branch sets, and hence an explicit `K_7`-minor model;
2. an actual order-seven separation carrying one complete common boundary
   equality partition; or
3. a strict host-level descent preserving the selected response and all
   named branch sets.

Inferring any of these outcomes directly from `c(u)=c(d)` or
`c(v)=c(e)` would be exactly the forbidden palette-to-label identification.
The present theorem deliberately makes no such inference.
