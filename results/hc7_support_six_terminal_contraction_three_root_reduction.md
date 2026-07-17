# A terminal contraction pair reduces to three rooted `K_4` models

**Status:** proved and separately audited GREEN in
[`hc7_support_six_terminal_contraction_three_root_reduction_audit.md`](hc7_support_six_terminal_contraction_three_root_reduction_audit.md).
The putative three-root residue is closed by the support-five exclusion
theorem in
[`hc7_five_connected_planar_support_five_exclusion.md`](hc7_five_connected_planar_support_five_exclusion.md).
This closes only the terminal-pair branch and does not prove the full
support-six transversal theorem.

## 1. Setup

Let `G` be a seven-connected graph which is not six-colourable.  Let `xy`
be an edge, put `H=G/xy`, and denote the contracted vertex by `z`.  Assume
that `H` is seven-connected.  Suppose that, for some vertex `r` of `H-z`,

\[
                         H-\{z,r\}
       \quad\hbox{is `K_5`-minor-free}.                 \tag{1.1}
\]

Write

\[
                         J=G-\{x,y,r\}=H-\{z,r\}.      \tag{1.2}
\]

For a vertex `q` outside `J`, a **`q`-rooted `K_4` model of support at
most five in `J`** means four disjoint connected branch sets in `J`, of
total order at most five, which are pairwise adjacent and each have a
literal neighbour at `q`.

## 2. Exact reduction

### Proposition 2.1

Under the setup above:

1. `J` is five-connected and planar, and it contains no literal `K_4`;
2. `x,y,r` form a literal triangle in `G`; and
3. for each `q in {x,y,r}`, the pair

   \[
                       \{x,y,r\}-\{q\}                 \tag{2.1}
   \]

   meets every `K_5` model supported on at most six vertices if and only if
   `J` has no `q`-rooted `K_4` model supported on at most five vertices.

Consequently, all three canonical pullbacks of the terminal pair would fail
exactly when the one common five-connected planar graph `J` carried one
such rooted `K_4` model for each of the three vertices of the external
triangle `xyr`.  The cited support-five exclusion theorem proves that `J`
cannot carry even one of these models.

#### Proof

Deleting two vertices from the seven-connected graph `H` leaves a
five-connected graph.  Thus `J` is five-connected.  It is `K_5`-minor-free
by (1.1), so Wagner's four-connected theorem makes it planar.

The graph `J` has no literal `K_4`.  Indeed, in a planar drawing a literal
`K_4` divides the sphere into four triangular regions.  Since a
five-connected graph has more than four vertices, some component outside
that `K_4` lies in one of the regions.  The three vertices on the boundary
of that region separate the component from the rest of the `K_4`, contrary
to five-connectivity.

The edge `xy` is present by construction.  Four-colour `J`, which is
possible by planarity.  If `xr` were absent, assign one fresh colour to
`x,r` and a second fresh colour to `y`.  This would properly six-colour
`G`, contrary to the hypothesis.  Hence `xr` is an edge; interchanging
`x,y` gives `yr`.  Therefore `xyr` is a triangle.

Fix `q in {x,y,r}` and let `P={x,y,r}-{q}`.  If `J` has a `q`-rooted
`K_4` model on at most five vertices, adjoining the singleton branch set
`{q}` gives a `K_5` model in `G-P` supported on at most six vertices.
Thus `P` is not a transversal.

Conversely, suppose that a `K_5` model `M` of support at most six survives
in `G-P`.  It must contain `q`; otherwise it would lie in the
`K_5`-minor-free graph `J`.  The model cannot have support five.  Such a
model has five singleton bags, and deleting its singleton `q`-bag would
leave a literal `K_4` in `J`.

Hence `M` has support exactly six and bag-size multiset
`(2,1,1,1,1)`.  Its unique two-vertex bag cannot contain `q`, since the
other four singleton bags would again form a literal `K_4` in `J`.
Therefore `{q}` is a singleton bag.  Removing it leaves four pairwise
adjacent connected branch sets in `J` of total order five, and the
singleton-bag adjacencies say that `q` has a neighbour in every one of
them.  This is the required `q`-rooted `K_4` model.  The equivalence follows.
\(\square\)

## 3. Closure and trust boundary

The proposition converts the model-transversal pullback question into a
small-support minor question in one planar core.  No three-model composition
is needed.  A five-connected planar graph has no `K_4` model supported on
at most five vertices: after contracting the unique two-vertex bag, one
would obtain a literal `K_4` in a four-connected planar graph with an extra
vertex, exposing a separating triangle.  Therefore all three pairs among
`x,y,r` are support-at-most-six `K_5` transversals.

This argument does not address a four-connected planar core, a rooted model
on six or more vertices, a nonterminal response in the contracted graph, or
the non-seven-connected contraction branch.
