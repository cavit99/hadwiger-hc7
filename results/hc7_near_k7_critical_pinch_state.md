# A critical shared pinch produces an actual-adhesion state

## Status

This is the safe dynamic conclusion at the degenerate canonical gate in
which the `X`-attachment and the `W`-attachment of the rotation connector
are the same vertex `s`.  Edge criticality does **not** split `s` into two
labelled carriers.  It does, however, put a deletion/contraction state on
the literal adhesion `N(W)`, together with five colour-distinguished
entrances into the `W`-shore.

The result is uniform in the near-clique labels.  In the rotation datum of
`../results/hc7_near_k7_rotation_edge.md`, the nonempty new defect set
ensures that `N(W)` really has a far side.  A collision with a state
produced by an operation in that far side six-colours the whole graph.

## 1. Setting and equality states

Let `G` be a graph which is not six-colourable but every proper minor and
every proper edge-deleted subgraph of `G` is six-colourable.  Let `W` be a
nonempty connected vertex set and put

\[
                         S=N_G(W),\qquad
 C=G[W\cup S],\qquad O=G-W.                       \tag{1.1}
\]

Assume that `V(G)-(W union S)` is nonempty, so `(C,O)` is an actual
two-shore separation.  Fix `s in S`, `w in W`, and a literal edge `sw`.

For a graph `J` containing the labelled set `S`, write `Ext(J,S)` for the
equality partitions of `S` induced by proper six-colourings of `J`.

## Theorem 1 (critical-pinch state and five entrances)

Every six-colouring `c` of `G-sw` has the following properties.  Put
`0=c(s)=c(w)` and name the other five colours `1,...,5`.

1. For every `i in {1,...,5}`, the vertices `s,w` lie in the same
   component of the subgraph induced by colours `{0,i}`.  Hence there is
   an `s-w` path `Q_i` in `G-sw` using only those two colours.
2. Traverse `Q_i` from `w`, and let `t_i` be its first vertex outside
   `W`.  Then `t_i in S`, the `w-t_i` prefix has all its internal vertices
   in `W`, and `c(t_i) in {0,i}`.  If `t_i=t_j` for distinct `i,j`, then
   `c(t_i)=0`.
3. If `t_i=s`, the predecessor of `s` on `Q_i` is a vertex
   `u_i in W` of colour `i`, joined literally to `s`.  Thus the indices
   whose entrances collapse at `s` give pairwise distinct direct
   `s-W` neighbours.
4. If `Pi` is the equality partition induced by `c` on `S`, then

   \[
        \Pi\in Ext(C-sw,S)\cap Ext(O,S)
        \quad\hbox{but}\quad
        \Pi\notin Ext(C,S).                         \tag{1.2}
   \]

   The same assertion holds for every six-colouring of `G/sw`, after
   retaining the contracted image of `s,w` as the boundary vertex `s`.

### Proof

If `c(s)` and `c(w)` were different, restoring `sw` would leave a proper
six-colouring of `G`.  Hence they have a common colour, called `0`.

Fix another colour `i`.  If `s` and `w` belonged to different
`{0,i}`-components, interchange `0` and `i` on the component containing
`s`.  The colouring remains proper on `G-sw`, and the ends of `sw` now
have different colours.  Restoring the edge would six-colour `G`, a
contradiction.  This proves item 1.

The path begins in `W` and ends at `s notin W`.  Its first vertex outside
`W` is therefore in `N_G(W)=S`, and its prefix has the asserted form.
The colour assertion follows because the whole path is bichromatic.  A
vertex occurring on both an `{0,i}`-path and an `{0,j}`-path has colour in
`{0,i} cap {0,j}={0}` when `i!=j`, proving item 2.  If the first boundary
vertex is `s`, the preceding vertex is in `W`; alternation gives it colour
`i`.  Different colours give different predecessors, proving item 3.

The restrictions of `c` to `C-sw` and `O` plainly induce the same
labelled partition `Pi`, giving the intersection in (1.2).  If `Pi`
extended to a six-colouring of `C`, permute its six colour names so that
its labelled blocks on `S` agree with the restriction of `c` to `O`.
The two colourings then glue across the separation and colour `G`, which
is impossible.  Thus `Pi` does not extend to `C`.

A colouring of `G/sw` is the same as a colouring of `G-sw` in which
`s,w` have one colour.  Its contracted image can be used as the copy of
the boundary vertex `s`, so the identical proof applies.  QED.

## Corollary 2 (opposite-operation collision)

Let `nu` be a deletion or contraction supported wholly in the open far
shore `V(G)-(W union S)`.  If a six-colouring of `G/nu` induces on `S`
the partition `Pi` from Theorem 1, then `G` is six-colourable.

### Proof

The operation leaves the closed side `C` unchanged.  Its colouring
therefore restricts to a colouring of `C` inducing `Pi`, contrary to the
last part of (1.2).  Equivalently, glue that restriction to the colouring
of `O` supplied by `G-sw`.  QED.

Thus, in a hypothetical counterexample, the state produced by the literal
pinch edge is excluded from every state family produced by an operation
strictly across the actual adhesion.  This is the precise state collision
which a global rotation composition has to force.

## Corollary 3 (the exact-seven one-pair trace)

Assume additionally that `|S|=7`, that `s` is the only boundary vertex of
colour `0`, and that `sw` is the only edge from `s` to `W`.  Then the five
vertices `t_1,...,t_5` are distinct and have colours `1,...,5`,
respectively.  The seventh boundary vertex repeats exactly one of those
five colours.  Consequently `Pi` consists of one two-vertex nonzero block
and five singleton blocks.

### Proof

The uniqueness of the edge `sw`, which is absent in `G-sw`, prevents an
entrance `t_i` from being `s`.  Since `s` is the only zero-coloured
boundary vertex, item 2 of Theorem 1 gives `c(t_i)=i`; hence the five
entrances are distinct.  Together with `s` they already use all six
colours.  The one remaining member of the seven-vertex boundary is not
zero-coloured by hypothesis and therefore repeats one of colours
`1,...,5`.  QED.

## 2. Application to an exact deficiency rotation

Use the notation of the rotation datum in
`../results/hc7_near_k7_rotation_edge.md`.  Suppose the fixed
`X-Z` attachment and the selected `Z-W` attachment coincide at
`s in Z`, and choose a neighbour `w in W`.  Since the new defect set
`E` is nonempty, `W` is anticomplete to the nonempty fixed bag `F_e` for
every `e in E`.  Therefore `F_e` lies outside

\[
                         W\cup N_G(W),
\]

and `S=N_G(W)` is an actual adhesion with nonempty shores.  Theorem 1
applies to the literal edge `sw`.

There are now exactly two safe positive uses of this datum.

* If the connector (possibly augmented by a protected bypass) has the
  two disjoint labelled rooted carriers from the rotation theorem, those
  carriers give a literal `K_7` model.
* Otherwise the edge `sw` supplies the actual-adhesion state `Pi` in
  (1.2).  Finding the same labelled partition from any proper-minor
  operation in the far shore invokes Corollary 2 and six-colours `G`.

The five entrance paths do not by themselves identify palette colours
with the five fixed row labels.  They record literal shore entrances and
the exact equality state, and nothing stronger is used here.

## Trust boundary

This theorem discharges the construction of the dynamic state at a
shared canonical pinch.  It does **not** prove that an opposite operation
produces the same state, and it does not turn the five Kempe paths into
five disjoint labelled carriers.  The accompanying critical-pinch barrier
shows that even seven-connectivity plus ordinary seven-criticality does
not justify that stronger inference.
