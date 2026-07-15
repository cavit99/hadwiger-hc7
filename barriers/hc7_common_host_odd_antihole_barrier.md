# Common-host odd-antihole barrier

**Status:** proved mechanism barrier, with a deterministic certificate probe for
the `HC_7` instance.  This construction is not a counterexample to
Hadwiger's Conjecture: it already contains the target clique minor.  Its role
is to show exactly which hypotheses cannot, by themselves, close the
common-edge-deletion route.

## 1. The uniform construction

Fix an integer `q>=3`, put `n=2q+1`, and write the vertices of a cycle in
cyclic order as

\[
                         0,1,\ldots,2q.
\]

Let

\[
 G_q=\overline{C_{2q+1}},\qquad
 e=1(2q),\qquad f=0(2q-1),\qquad
 H_q=G_q-\{e,f\}.                                      \tag{1.1}
\]

Both named pairs are edges of `G_q`: each joins the ends of a length-two
arc of the cycle.  They are vertex-disjoint.  Several cross-edges between
their endpoint pairs are absent; for example, `01`, `0(2q)`, and
`(2q-1)(2q)` are cycle edges and hence nonedges of `G_q`.

### Proposition 1.1 (chromatic and state properties)

For every `q>=3`:

1. `chi(G_q)=q+1`, and `G_q` is `(q+1)`-vertex-critical;
2. `chi(H_q)=chi(H_q+e)=chi(H_q+f)=q`;
3. every `q`-colouring of `H_q+e` makes the ends of `f` equal, and every
   `q`-colouring of `H_q+f` makes the ends of `e` equal;
4. no `q`-colouring of `H_q` makes both named endpoint pairs equal;
5. the simultaneous named contraction `G_q/e/f` is not `q`-colourable.

#### Proof

An independent set of `G_q` is a clique of `C_{2q+1}`, so it has order at
most two.  Consequently `chi(G_q)>=q+1`.  Pairing consecutive cycle
vertices and leaving one singleton gives a `(q+1)`-colouring.  Deleting
one vertex leaves the complement of `P_{2q}`; its consecutive pairs give
a `q`-colouring, while its independence number is still two.  This proves
the first assertion.

Deleting `e` permits the colour classes

\[
 \{2q,0,1\},\ \{2,3\},\ \{4,5\},\ldots,
 \{2q-2,2q-1\},                                      \tag{1.2}
\]

and deleting `f` permits

\[
 \{2q-1,2q,0\},\ \{1,2\},\ \{3,4\},\ldots,
 \{2q-3,2q-2\}.                                      \tag{1.3}
\]

Thus `H_q`, `H_q+e`, and `H_q+f` are all `q`-colourable.

The nonedge graph of `H_q` is `C_{2q+1}+e+f`.  Its only triangles are

\[
              T_e=\{2q,0,1\},\qquad
              T_f=\{2q-1,2q,0\}.                     \tag{1.4}
\]

Indeed, a triangle must use one of the two added chords.  The endpoints
of `e` have only `0` as a common neighbour in the nonedge graph, and the
endpoints of `f` have only `2q` as a common neighbour.  Hence the only
independent triples of `H_q` are the two triples in (1.4), and they
intersect.  A `(q-1)`-colouring of `2q+1` vertices, when every colour
class has order at most three, would require at least three disjoint
classes of order three.  This is impossible.  Therefore `chi(H_q)=q`.

In a `q`-colouring of `H_q+e`, the edge `e` is proper.  If `f` were also
proper, the same colouring would colour `G_q`, contradicting
`chi(G_q)=q+1`.  The symmetric argument applies to `H_q+f`, proving the
opposite response signatures.

Finally suppose a `q`-colouring of `H_q` made both named pairs equal.  A
colour class containing the ends of `e` could acquire a third vertex only
by becoming `T_e`, but `0` already belongs to the colour class containing
the ends of `f`.  Symmetrically, the `f`-class cannot acquire `2q`.
After these two pair classes are removed, `2q-3` vertices remain, and the
remaining graph has independence number at most two by (1.4).  The other
`q-2` colours cover at most `2q-4` vertices, a contradiction.

A `q`-colouring of `G_q/e/f` expands to a `q`-colouring of `H_q` in
which both named endpoint pairs are equal.  Conversely, such an
equal/equal colouring of `H_q` descends through the two contractions.
Thus the fourth and fifth assertions are equivalent.  In particular,
the construction supplies both one-edge deletion responses but fails the
simultaneous **named** double-contraction response.  \(\square\)

### Proposition 1.2 (high connectivity and model properties)

For every `q>=3`:

1. `kappa(G_q)=2q-2`;
2. `H_q` has a spanning `K_q` model;
3. `H_q` already contains a `K_{q+1}` minor;
4. after deleting any two vertices from `G_q`, a literal `K_q` remains;
5. `G_q` is not contraction-critical: contracting the edge `03` produces
   a graph containing a literal `K_{q+1}`.

#### Proof

Every vertex of `G_q` has degree `2q-2`, so its connectivity is at most
`2q-2`.  Remove at most `2q-3` vertices and let `W` be the remaining set,
so `|W|>=4`.  If `G_q[W]` were disconnected with sides `A,B`, every
`A`--`B` pair would be an edge of the original cycle.  Since cycle degree
is two, both sides would have order at most two.  Equality would force a
`K_{2,2}` subgraph of the cycle, impossible in a cycle of order at least
seven.  Hence `G_q[W]` is connected and `kappa(G_q)=2q-2`.

For a spanning `K_q` model in `H_q`, take the `q-1` singleton bags

\[
                      \{2\},\{4\},\ldots,\{2q-2\}
\]

and one bag containing all remaining vertices.  The singleton vertices
are pairwise adjacent.  The large bag is connected (vertex `3` is
adjacent inside `H_q` to every other member of that bag), and it meets
every singleton bag.

For a `K_{q+1}` model already in `H_q`, take the `q` singleton bags

\[
                    \{0\},\{2\},\ldots,\{2q-2\}       \tag{1.5}
\]

and the remaining bag

\[
                    \{1,3,5,\ldots,2q-1,2q\}.         \tag{1.6}
\]

The vertices in (1.5) form a clique.  The bag (1.6) is connected and has
an edge to every singleton bag.  Deleting `e` and `f` does not destroy
these properties.

Deleting two vertices from the original cycle leaves one or two paths on
`2q-1` vertices in total.  Their independence numbers sum to at least
`q`.  Those independent cycle vertices induce a literal `K_q` in
`G_q` minus the selected pair.

Lastly contract the edge `03` of `G_q`.  The cycle-nonneighbour sets of
`0` and `3` are respectively `\{1,2q\}` and `\{2,4\}`, which are
disjoint.  The contracted vertex is therefore universal.  The set

\[
                      \{1,4,6,\ldots,2q\}
\]

has order `q` and contains no consecutive cycle vertices, so it is a
literal `K_q`.  Together with the contracted vertex it gives a literal
`K_{q+1}`.  \(\square\)

## 2. Fully labelled `HC_7` certificate (`q=6`)

Set `q=6`, so `G=overline(C_13)`, `e=1 12`, `f=0 11`, and
`H=G-{e,f}`.

The two opposite six-colourings are

\[
 \begin{aligned}
 G-e:&\quad  \{0,1,12\}\mid\{2,3\}\mid\{4,5\}
              \mid\{6,7\}\mid\{8,9\}\mid\{10,11\},\\
 G-f:&\quad  \{0,11,12\}\mid\{1,2\}\mid\{3,4\}
              \mid\{5,6\}\mid\{7,8\}\mid\{9,10\}.
 \end{aligned}                                                   \tag{2.1}
\]

A spanning `K_6` model of the common host `H`, with the four endpoints in
four different rows, is

\[
 \{1,2,9\},\ \{8,12\},\ \{0\},\ \{6,11\},\
 \{3,10\},\ \{4,5,7\}.                                  \tag{2.2}
\]

Thus an arbitrary common spanning model need not have a multiply-hit
named row.  This does not rule out reselecting or extremizing the model.

An explicit `K_7` model already in `H` is

\[
 \{0\},\ \{2\},\ \{4\},\ \{6\},\ \{8\},\ \{10\},\
 \{1,3,5,7,9,11,12\}.                                  \tag{2.3}
\]

Contracting `03` makes the contracted vertex universal to the `K_6`

\[
                         \{1,4,6,8,10,12\}.             \tag{2.4}
\]

The accompanying deterministic probe checks (2.1)--(2.4), exact
six-chromaticity of `H`, absence of the simultaneous equal/equal state,
non-six-colourability of `G/e/f`, 10-connectivity, and the absence of any
two-vertex `K_5` transversal.

## 3. Exact barrier scope

The construction proves that none of the following, even in combination,
forces a common named equality state or a fixed two-vertex terminal:

- connectivity well above seven;
- vertex-criticality;
- two vertex-disjoint named edge deletions with universal opposite
  colouring signatures;
- a connected, exactly six-chromatic common host;
- a spanning common-host `K_6` model.

It also disproves any claim that **every** spanning common-host model must
place two named endpoints in one row.  It does not disprove an existential
row-splitting theorem after model reselection, because (2.3) explicitly
closes to `K_7`.  For the same reason it cannot disprove the desired
literal `K_7` outcome.

The first actual minimal-`HC_7` ingredients that exclude this entire
family are `K_7`-minor-freeness and strong contraction-criticality.  More
sharply, strong contraction-criticality already excludes it at the named
double contraction: `G_q/e/f` is a proper minor and would have to be
`q`-colourable, contrary to Proposition 1.1.  This is exactly why a
double-contraction lock theorem contains information absent from the two
opposite deletion responses.  The nonnamed edge `03` supplies a second,
independent failure, since `G_q/03` already contains `K_{q+1}`.

Consequently the odd-antihole family does not refute an exchange theorem
that explicitly uses the named double-contraction response.  It does
refute any attempt to derive that response from high connectivity,
vertex-criticality, the two one-edge deletion states, and a common
spanning model alone.  Further carrier-edge contraction responses remain
available as an additional source of global information.
