# Regeneration trichotomy at a normalized support-six model

**Status:** proved synthesis; independent audit pending.  The theorem closes
the non-seven-connected and two-apex quotient branches.  It also proves
that unrooted `K_6` regeneration in the remaining quotient branch is
canonical and therefore supplies no new model information by itself.

## 1. Setup

Let `G` be a seven-connected, strongly seven-contraction-critical,
`K_7`-minor-free graph.  Fix a two-set `P` meeting every literal `K_5` in
`G`, and suppose `G-P` has a support-six `K_5` model

\[
                         Q,\quad xy,                    \tag{1.1}
\]

where `Q={q_1,q_2,q_3,q_4}` is the singleton `K_4` core and `xy` is the
two-vertex edge bag.  Put

\[
 W=Q\cup\{x,y\},\qquad H=G/xy,
\]

and write `z` for the contracted image.  Then

\[
                         L=Q\cup\{z\}                  \tag{1.2}
\]

is a literal `K_5` in `H`.

The existence of `P` is the proved global literal-`K_5` transversal
theorem.  The result below starts after the support-six model has been
selected; it does not assert that `P` already meets every support-six
model.

## 2. The canonical quotient model

### Lemma 2.1 (canonical spanning `K_6` regeneration)

If `H` is seven-connected, then

\[
                         C=H-L=G-W                     \tag{2.1}
\]

is two-connected, every vertex of `L` has a neighbour in `C`, and

\[
             \{q_1\},\{q_2\},\{q_3\},\{q_4\},\{z\},C \tag{2.2}
\]

is a spanning `K_6` model in `H`.

#### Proof

For every set `X subseteq V(C)` of order at most one,

\[
                      C-X=H-(L\cup X)
\]

is connected because `|L\cup X|<=6` and `H` is seven-connected.  The
order convention for seven-connectivity gives `|H|>=8`, so `C` has at
least three vertices.  Hence `C` is two-connected.

Every `l in L` has degree at least seven in `H` and at most four neighbours
inside the five-set `L`, so it has a neighbour in `C`.  The five singleton
sets in (2.2) form a clique, the sixth set is connected, and it is adjacent
to every singleton.  These six bags cover `V(H)`.  \(\square\)

Thus the `K_6` minor whose existence follows from `chi(H)=6` and known
`HC_6` may be exactly (2.2).  Mere unrooted regeneration in `G/xy` gives
no second carrier and no new contact beyond seven-connectivity.

## 3. Exact critical colouring data

### Lemma 3.1 (quotient palette and locks)

The graph `H` has chromatic number six.  Fix a six-colouring `c` of `H`,
give `x,y` the colour of `z`, and view this as a colouring of `G-xy`.
Then:

1. each of `x,y` has a neighbour in every colour different from `c(z)`;
2. for every such colour `gamma`, the vertices `x,y` lie in one component
   of the subgraph of `G-xy` induced by colours `c(z),gamma`;
3. if `q_i` is nonadjacent to `x`, then `x` has a neighbour of colour
   `c(q_i)` in `C`; symmetrically for `y`; and
4. for the unique colour absent from the clique `L`, there is an `x-y`
   bichromatic path whose internal vertices all lie in `C`.

#### Proof

The contraction is a proper minor of `G`, so it is six-colourable.  A
five-colouring of `H` would pull back to `G-xy`; recolouring one of `x,y`
with a fresh sixth colour would six-colour `G`.  Thus `chi(H)=6`.

If, in a six-colouring, one endpoint missed a noncontraction colour, it
could be recoloured with that colour and the edge `xy` restored.  This
proves item 1.  If `x,y` lay in different components of one of the stated
bichromatic graphs, swapping the two colours on the component containing
`x` would again give the endpoints different colours and hence six-colour
`G`.  This proves item 2.

The clique `L` uses five distinct colours.  The only vertex of `L` with
colour `c(q_i)` is `q_i`; if it is not adjacent to an endpoint, the
neighbour supplied by item 1 lies outside `L`, namely in `C`.  This proves
item 3.  The sixth colour does not occur in `L`, so an `x-y` path supplied
by item 2 for that colour has all its internal vertices in `C`.  \(\square\)

Items 1--4 are colour-labelled contacts and paths.  They do not identify
palette colours with branch bags of an independently chosen `K_6` model.

## 4. Terminal branches and the exact regeneration obstruction

### Theorem 4.1 (regeneration trichotomy)

Under the setup of Section 1, at least one of the following applies.

1. `H` is not seven-connected.  Splitting `z` back into `x,y` gives an
   actual exact-seven separation whose boundary contains `x,y` and whose
   closed shore contains the selected support-six model.
2. `H` is seven-connected and two-apex.  Then `G` has a two-vertex set
   meeting every support-at-most-six `K_5` model.
3. `H` is seven-connected and non-two-apex.  Lemmas 2.1 and 3.1 hold, and
   the split edge has exactly one of the following two deletion responses:

   * `chi(G-\{x,y\})=5`; then every five-colouring of this deletion has,
     in each colour, a vertex adjacent to both `x` and `y`;
   * `chi(G-\{x,y\})=6`; then `G-\{x,y\}` contains a spanning `K_6`
     model.  For every such model, the union of the rows contacted by
     `x` or `y` has order at most five, unless `G` already has a `K_7`
     minor.

#### Proof

Outcome 1 is the proved support-six contraction dichotomy and canonical
component handoff: every separator of order at most six in `H` contains
`z`, and replacing `z` by `x,y` gives an actual seven-boundary preserving
the named model.

In outcome 2, apply the proved two-apex contraction-pullback theorem.  It
handles separately whether a planarizing pair contains `z` and always
returns a literal pair in `G` meeting every support-at-most-six model.

It remains that `H` is seven-connected and non-two-apex.  Lemmas 2.1 and
3.1 apply.  Vertex-criticality gives

\[
                  5\le\chi(G-\{x,y\})\le6.             \tag{4.1}
\]

If equality is five, the standard colourwise common-neighbour lemma for a
double-critical edge gives the first response: otherwise one colour class
can be recoloured with one fresh colour while assigning the old colour and
the fresh colour to `x,y`, producing a six-colouring of `G`.

If equality is six, known `HC_6` gives a `K_6` minor in the deletion.
The deletion is five-connected and hence connected, so the model can be
enlarged to a spanning model.  If the connected edge-bag `\{x,y\}` meets
all six rows, it and the six rows are a `K_7` model.  Therefore a
`K_7`-minor-free host has joint row-contact order at most five.  \(\square\)

## 5. Consequence for the proposed strategy

The nontrivial use of model regeneration is **not** the automatic model in
`G/xy`; Lemma 2.1 shows that model is already forced before criticality is
used.  The first genuinely new model is one avoiding the contracted vertex,
equivalently the six-residual branch `chi(G-\{x,y\})=6`.

The exact remaining obstruction is therefore graph-specific and
label-sensitive:

* in the double-critical branch, five colourwise common neighbours need
  not occupy five mutually adjacent carriers;
* in the six-residual branch, a spanning `K_6` exists, but all neighbours
  of the split edge can be concentrated in at most five rows; and
* Lemma 3.1 supplies palette-labelled paths, but does not assign those
  paths to the six regenerated rows.

Any further theorem must use the proper-minor response to split a named
row, produce a genuinely different near-full carrier, or identify the
same global terminal pair.  Reinvoking `HC_6` on `G/xy` cannot do this.
