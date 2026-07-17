# Audit of the terminal-contraction three-root reduction

**Verdict:** **GREEN.**  Proposition 2.1 and its stated terminal-pair
consequence are valid.  The promoted planar support-five exclusion theorem
does logically use this reduction only for Corollary 3.2; its independent
Theorems 2.1 and 3.1 do not depend on it.

**Current source SHA-256:**
`b43c38b125e6d22c4f7d7ecb3b3dda7741518c0c0516a5b03bb5d2b0663dc59e`

**Audited mathematical revision SHA-256:**
`3e65bf8e0525679d54198f9826ae888d9d1d1500642ce478b0e9f8247ca87b2f`

The current source differs from the audited mathematical revision only in
its status paragraph and in the relative path of the now-promoted planar
support-five exclusion theorem.  No setup, proposition, proof, or scope
claim changed.  This audit therefore binds its verdict to the current hash.

## 1. Connectivity, planarity, and the external triangle

Let `H=G/xy`, with contracted vertex `z`, and put

\[
                       J=H-\{z,r\}=G-\{x,y,r\}.
\]

Deleting `z,r` from the seven-connected graph `H` leaves `J`
five-connected.  By hypothesis `J` is `K_5`-minor-free.  The standard
four-connected form of Wagner's theorem therefore makes `J` planar.

A literal `K_4` cannot occur in `J`: in any plane drawing its four facial
triangles separate any outside vertex from the opposite clique vertex.
Since a five-connected graph has at least six vertices, such an outside
vertex exists, contradicting five-connectivity.

The proof that `x,y,r` form a triangle is also correct.  The edge `xy` is
part of the setup.  Four-colour `J`.  If `xr` were absent, `x,r` could use
one fresh colour and `y` a second fresh colour, producing a six-colouring
of all of `G`; this contradicts the assumed non-six-colourability.  Hence
`xr` is present, and the symmetric argument gives `yr`.

## 2. Exact equivalence with a rooted support-five model

Fix `q` in `\{x,y,r\}` and delete the other two vertices.  The remaining
graph is exactly `J+q`.

If `J` has a `q`-rooted `K_4` model of total support at most five, adding
the singleton branch set `\{q\}` gives a `K_5` model of support at most
six which avoids the deleted pair.  Thus that pair is not a transversal.

Conversely, let a support-at-most-six `K_5` model survive in `J+q`.  It
must use `q`, because `J` is `K_5`-minor-free.  If the branch set containing
`q` is the singleton `\{q\}`, deleting it leaves a `q`-rooted `K_4` model
in `J` on at most five support vertices: adjacency to the singleton branch
set gives the required literal `q`-contact to every remaining branch set.

If the `q`-branch set is not a singleton, five nonempty branch sets on at
most six vertices force bag sizes `(2,1,1,1,1)`.  The four other branch
sets are singleton vertices of `J` and form a literal `K_4`, which was
excluded above.  Hence this alternative is impossible.  This proves both
directions of Proposition 2.1(3), with no omitted bag-size case.

## 3. Dependency on the planar support-five exclusion

The terminal-contraction reduction establishes the precise rooted-model
equivalence.  To close the branch, one then needs to exclude every
support-at-most-five `K_4` model in the five-connected planar graph `J`.
That is exactly Theorem 2.1 of
[`hc7_five_connected_planar_support_five_exclusion.md`](hc7_five_connected_planar_support_five_exclusion.md).
Its proof is independent of this reduction.  Its Corollary 3.2 invokes
Proposition 2.1 here to translate the exclusion back to the three displayed
two-vertex transversals.  Thus the dependency is one-way and noncircular.

## 4. Trust boundary

The result closes only the standardized branch in which the contracted
graph is seven-connected and deleting the contracted vertex together with
`r` leaves a `K_5`-minor-free graph.  It does not handle a quotient of lower
connectivity, a rooted `K_4` model with support at least six, a nonterminal
proper-minor response, or the general support-six transversal problem.
