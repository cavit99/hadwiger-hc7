# Stateful pullback at global support six

**Status:** proved elementary pullback and separator lemmas.  The
seven-contractible branch still has two independent open residues: an
equal-support neutral response and a strict split-row/forced-pole response.
This note is a global reduction, not a proof of `HC_7`.

## 1. Setup

Let `G` be a seven-connected, `K_7`-minor-free, strongly
seven-contraction-critical graph.  Let `P` maximize, over all **two-vertex
sets**,

\[
 \mu_G(P)=\min\{|V(\mathcal M)|:\mathcal M\text{ is a }K_5
                  \text{-model in }G-P\},
\]

and suppose that the maximum is six.  Fix a minimum model in `G-P`.
By the audited support-six dichotomy it has four singleton bags

\[
                         Q=\{q_1,q_2,q_3,q_4\}
\]

and one edge-bag `xy`.  Put `W=Q union {x,y}`, let `H=G/xy`, and write
`z` for the image of `xy`.

The phrase **split-row model** means a `K_5` model in `G` in which `x`
and `y` belong to two distinct branch sets.

For any graph `J` and any vertex set `R subseteq V(J)`, not necessarily a
two-set, use the same notation

\[
 \mu_J(R)=\min\{|V(\mathcal N)|:\mathcal N\text{ is a }K_5
                   \text{-model in }J-R\},
\]

with value infinity when no such model exists.  All applications below use
two-sets.

## 2. Exact model pullback

### Lemma 2.1 (the only obstruction to contraction pullback)

Let `R subseteq V(H)-{z}` and let `s>=5`.  If

\[
                            \mu_H(R)>s,
\]

then every `K_5` model in `G-R` with support at most `s` is a split-row
model.

If instead `R={z,r}` and `mu_H(R)>s`, then

1. every `K_5` model of support at most `s` in `G-{x,r}` contains `y`;
2. every `K_5` model of support at most `s` in `G-{y,r}` contains `x`.

#### Proof

Consider a `K_5` model `N` in `G-R`, where `z notin R`.  If `N` uses at
most one of `x,y`, contracting `xy` maps `N` to a `K_5` model in `H-R`
without increasing its support.  If it uses both vertices in one branch
set, the same contraction is internal to that branch set and again gives a
`K_5` model, now with support smaller by one.  Thus the contraction can
fail to return five disjoint branch sets only when `x,y` occur in distinct
branch sets.  This proves the first assertion.

Now let `R={z,r}`.  A model in `G-{x,r}` which also avoids `y` survives
unchanged in `H-{z,r}`; the symmetric statement is identical.  The assumed
lower bound on `mu_H(R)` excludes such a model of support at most `s`.
\(\square\)

This lemma is sharp as a model-theoretic statement: contracting an edge
joining two different rows merges those rows and produces only four branch
sets.  Any stronger pullback theorem must use the counterexample colouring
response or produce a coherent terminal pair; contraction alone cannot
remove this alternative.

## 3. What a terminal pair in the contraction forces

### Lemma 3.1 (terminal-pair chromatic lock)

Assume that `R` is a two-vertex set for which `H-R` is `K_5`-minor-free.

1. If `z notin R`, write `R={r,s}`.  Then

   \[
        G-(R union {x})\quad\text{and}\quad G-(R union {y})
   \]

   are `K_5`-minor-free.  Moreover, `rs` is an edge and all four edges
   between `{x,y}` and `{r,s}` are present.  Thus `{x,y,r,s}` is a literal
   `K_4`.  In every proper four-colouring of `H-R`, each of `r,s` has a
   neighbour in every colour class.
2. If `R={z,r}`, then `G-{x,y,r}` is `K_5`-minor-free, both `xr` and `yr`
   are edges, and in every proper four-colouring of `H-{z,r}`, the vertex
   `r` has a neighbour in every colour class.

#### Proof

The minor-free assertions follow directly from Lemma 2.1, with no support
bound: a model avoiding `R` and one of `x,y` contracts to a model in
`H-R`; when `z in R`, a model avoiding `x,y,r` is already a model in
`H-{z,r}`.

Known `HC_5` gives a proper four-colouring of `H-R`.

First suppose `z notin R`.  Give `r,s` two fresh colours and pull the
four-colouring back through the split, initially giving `x,y` the colour
of `z`.  If, for example, `xr` were absent, keep `y` in the old colour and
give `x` the fresh colour used only on `r`.  This is a proper six-colouring
of `G`, a contradiction.  The other three adjacencies follow symmetrically.
If `rs` were absent, give both `r,s` one fresh colour, keep `y` in the old
colour of `z`, and give `x` the sixth colour.  This is again a proper
six-colouring, so `rs` is an edge.
If `r` missed one of the four old colour classes, recolour `r` with that
old colour and give one of `x,y` the now unused fresh colour of `r`; keep
the other split endpoint in the old colour of `z`.  This again six-colours
`G`.  The same argument applies to `s`.

Now suppose `R={z,r}`.  Four-colour `H-{z,r}`, give `z,r` two fresh
colours, and split `z`.  If one split endpoint were nonadjacent to `r`, it
could take the fresh colour of `r`, while the other retained the colour of
`z`.  Thus `xr,yr` are edges.  If `r` missed an old colour class, recolour
`r` with it and use the two fresh colours on `x,y`.  This also gives a
proper six-colouring.  Hence the stated saturation is compulsory.
\(\square\)

Lemma 3.1 identifies the exact chromatic residue of a terminal pair in
`H`: either it pulls back, or the split edge is joined completely to a
two-set (or to the retained vertex) and that set is saturated against
every four-colouring of the `K_5`-minor-free remainder.  No rooted-model
conclusion is asserted.

### Corollary 3.2 (planar split lock)

Under Lemma 3.1, the graph `H-R` is five-connected and planar.

* If `z notin R`, then `G-R` is obtained from this five-connected planar
  graph by splitting `z` into the adjacent vertices `x,y`.  Every `K_5`
  model in `G-R` uses `x,y` in distinct rows, while the literal `K_4`
  `{x,y,r,s}` and the four-colour saturation in Lemma 3.1 are compulsory.
* If `R={z,r}`, then `G-{x,y,r}=H-{z,r}` is five-connected and planar;
  every model avoiding one split endpoint and `r` contains the opposite
  endpoint, and the triangle `xyr` and four-colour saturation are
  compulsory.

#### Proof

Deleting two vertices from the seven-connected graph `H` leaves a
five-connected graph.  Lemma 3.1 assumes it is `K_5`-minor-free, so Wagner's
four-connected theorem makes it planar.  The model assertions are Lemma
2.1 with no finite support bound, and all remaining assertions were proved
in Lemma 3.1. \(\square\)

Thus a terminal in the contraction either pulls back literally or produces
one coherent planar vertex-split obstruction.  This is a structural
alternative, not yet a proof that the same pair is terminal in `G`.

## 4. The non-seven-connected contraction gives a model-preserving handoff

Use the audited exact-seven packet theorem and the audited elimination of
the `(1,3)` vector.

### Theorem 4.1 (canonical component handoff)

Suppose `H` is not seven-connected.  Then there is a six-separator `T` of
`H`, with `z in T`, such that for

\[
                       S=(T-{z}) union {x,y}
\]

the following hold.

1. Every component of `H-T` is also a component of `G-S` and is `S`-full.
2. All vertices of `Q-T` lie in at most one component `C_Q` of `H-T`.
   Consequently the complete support `W` of the selected model is contained
   in the closed shore `S union C_Q` (with `C_Q` omitted if `Q subseteq T`).
3. If `H-T` has at least three components, then for every component `C`
   the actual separation

   \[
               (C union S,\; V(G)-C)
   \]

   has packet vector `(1,2)`, with `C` the packet-one shore.  In particular
   one may choose `C ne C_Q`, so the entire selected `K_5` model remains
   intact in the opposite closed shore.
4. If `H-T` has exactly two components, their packet vector is `(1,1)` or
   `(1,2)`.  In the latter case the selected model is still contained in
   one of the two closed shores.

#### Proof

The support-six contraction dichotomy gives an order-six separator `T`
containing `z`, and splitting `z` produces the actual seven-boundary `S`.
The components on deleting the respective boundaries are identical.

For a component `C` of `G-S`, its neighbourhood is contained in `S`.
If it missed a literal member of `S`, its neighbourhood would have order
at most six, contradicting seven-connectivity.  Thus every component is
`S`-full.

The set `Q union {z}` is a clique in `H`.  Vertices of a clique which lie
outside a separator cannot occupy two different components.  Hence all of
`Q-T` lies in at most one component `C_Q`.  Since `x,y in S`, this also
proves the model-containment statement.

Assume there are at least three components and fix one of them, `C`.  The
opposite open shore contains two distinct components, each an `S`-full
packet, so its packet number is at least two.  The exact-seven packet
classification says that, up to orientation, only `(1,1),(1,2),(1,3)` can
occur, and the adaptive reflection theorem excludes `(1,3)` in the present
strongly contraction-critical graph.  It follows that `C` has packet
number one and its opposite shore has packet number exactly two.  This is
item 3.  Since at most one component is `C_Q`, a different component may
be chosen.

With exactly two components the same classification, together with the
elimination of `(1,3)`, leaves `(1,1)` and `(1,2)`.  The already proved
model-containment statement is independent of the orientation. \(\square\)

### Corollary 4.2 (entry into the genuinely ranked class)

Suppose at least one globally `mu`-maximal support-six certificate has a
non-seven-connected split contraction and yields a `(1,2)` separation in
Theorem 4.1.  Then the class of actual oriented `(1,2)` separations of `G`
is nonempty.  Choose from **all** members of that class one minimizing the
order of the packet-one shore.  This is the audited graph-global,
well-founded exact-seven rank.

Thus every later valid `(1,2)` receiver with a smaller packet-one shore is
a contradiction without any equality-state comparison.  The particular
cell produced by Theorem 4.1 preserves the selected support-six model in one
named closed shore.  The globally minimum reselected cell need not preserve
that model or the pair `P`.  Therefore using the model inside the ranked
cell still requires either a state-uniform exact-seven theorem or a proof
that the selected subclass is closed under the intended receiver.  This
corollary does not rank a `(1,1)` receiver and does not silently assume that
closure.

## 5. The seven-connected branch and the exact remaining obstruction

Suppose `H` is seven-connected.  The global literal-`K_5` transversal
theorem applied to `H` returns a two-set `R` with

\[
                              \mu_H(R)>=6.
\]

Since `Q union {z}` is a literal `K_5`, this `R` meets that five-set.
Lemma 2.1 gives the complete safe pullback statement.

* If `z notin R` and `mu_H(R)>=7`, then either `mu_G(R)>=7`, or every
  support-at-most-six response in `G-R` is a split-row model.
* If `R={z,r}` and `mu_H(R)>=7`, then either one lift pair has value at
  least seven, or every support-at-most-six response to `{x,r}` contains
  `y` and every such response to `{y,r}` contains `x`.
* If `mu_H(R)=6`, a nonsplit support-six response may survive contraction,
  so no strict support increase follows.

Because the chosen value six is globally maximal, neither the neutral
equal-support response nor the split-row/forced-pole alternatives can be
discarded by numerical maximization.  The missing theorem must first handle
the equality branch `mu_H(R)=6` by coupling a minimum model in `H-R` to the
original edge-bag model, or else handle the strict branch by coupling the
named split-row/forced-pole responses.  In either branch it must return a
literal `K_7`, one coherent terminal pair, or a model-preserving transition
into the globally ranked exact-seven class of Corollary 4.2.  Contraction
alone supplies none of these conclusions.

## 6. Exact strategic consequence

The noncontractible branch produces a model-preserving `(1,2)` cell and
separately proves that a globally minimum `(1,2)` class exists, except for a
normalized `(1,1)` residue.  It does **not** prove that the globally reselected
minimum cell preserves the model or pair.

The seven-contractible branch has two residues:

1. `mu_H(R)=6`, where a neutral nonsplit support-six model may survive and
   no row constraint is available; and
2. `mu_H(R)>=7`, where every small response has the split-row/forced-pole
   form of Lemma 2.1.

Further work must classify both branches in one closed transition system.
A theorem which merely reselects another support-six pair without excluding
the equal-support branch, preserving the named model data, or strictly
increasing a graph-global rank is a neutral transition rather than progress.
