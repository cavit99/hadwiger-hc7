# The 13-vertex cofacial-neighbour barrier to rooted Jorgensen

## Status

This is a verified counterexample to

\[
\begin{split}
 &H\text{ six-connected},\quad
  \text{every component of }H-S\text{ meets }X\ (|S|\le6)\\
 &\hspace{25mm}\Longrightarrow
 H\text{ apex or }H\text{ has an }X\text{-meeting }K_6\text{ model}.
\end{split}
\]

The example is nonapex and has no `X`-meeting `K6`.  Its unique
planarizing pair is explicit, and deleting it leaves `X` cofacial.  Thus
the example does **not** refute the corrected conclusion

\[
 X\text{-meeting }K_6\quad\text{or one coherent cofacial two-apex pair}.
\]

The exact certificate is
`hc7_rooted_jorgensen_apex_barrier_verify.py`.

## Construction

Let `T` be the icosahedron and fix a vertex `z`.  Put

\[
 R=T-z,qquad H=K_2\vee R,qquad
 X=N_T(z)\cup V(K_2).
\]

Write `a,b` for the two universal vertices.  The set `N_T(z)` has five
vertices, so `|X|=7`.  In the explicit NetworkX labelling used by the
verifier,

\[
 z=0,quad N_T(z)=\{1,5,7,8,11\},\quad a=12,\quad b=13,
\]

and `H` has graph6 string

```text
LhcEJKtFNo^~~~
```

## Proposition 1 (connectivity and robust contact)

The graph `H` is six-connected.  For every `S` with `|S|<=6`, every
component of `H-S` meets `X`.

### Proof

The icosahedron is five-connected, so `R=T-z` is four-connected.  Hence

\[
                   \kappa(K_2\vee R)=2+\kappa(R)=6.
\]

If at least one of `a,b` survives deletion of `S`, that universal vertex
makes `H-S` connected.  Since `|X|=7>|S|`, its component contains a
surviving member of `X`.

Suppose `a,b` both lie in `S` and put `S_R=S-{a,b}`.  Then `|S_R|<=4`.
If a component `C` of `R-S_R` missed `N_T(z)`, then `z` would have no
neighbour in `C`; consequently `C` would remain separated from the rest
of `T-S_R`, contradicting five-connectivity of `T`.  Thus every component
meets `N_T(z) subseteq X`.  \(\square\)

## Proposition 2 (no `X`-meeting `K6`)

The graph `H` has no `K6` model all of whose bags meet `X`.

### Proof

Assume such a model exists.  Since the planar graph `R` has no `K5`
minor, `a` and `b` must lie in two distinct branch bags: if at most one
bag met `{a,b}`, at least five bags would lie wholly in `R`; if one bag
contained both, the same would be true.

Delete the two bags containing `a,b`.  The other four bags lie wholly in
`R`, are pairwise adjacent, and meet `X`.  They cannot meet `a` or `b`, so
each meets `N_T(z)`.  Choosing one such vertex from each bag produces four
distinct roots and a `K4` model rooted at them.

But deleting `z` puts all five vertices of `N_T(z)` on the boundary of one
face of `R`.  Four cofacial vertices of a plane graph cannot root a `K4`
minor: contracting four disjoint rooted bags would give a plane drawing of
`K4` with all four vertices on the outer face, contradicting that `K4` is
not outerplanar.  \(\square\)

The exclusion is genuinely rooted, not an absence of an ordinary clique
minor.  The four bags

\[
                  \{1\},\ \{2\},\ \{8\},\ \{9,3,6\}
\]

form a `K4` model in `R`; together with `{a},{b}` they form an unrooted
`K6` model in `H`.

## Proposition 3 (exact rural alternative)

The graph `H` is nonapex and `{a,b}` is its unique planarizing pair.
Moreover `H-{a,b}=R` is planar with `N_T(z)` on the facial walk

\[
                         1,8,7,11,5.
\]

The verifier checks all thirteen one-vertex deletions and all 78
two-vertex deletions.  Structurally, deleting only one of `a,b` leaves a
cone over the nonouterplanar four-connected graph `R`; deleting neither
leaves such a cone as a subgraph.  Deleting both leaves the planar graph
`R`.

## HC7 lift

Add a vertex `v` with `N(v)=X`.  The robust-contact condition makes the
new graph seven-connected.  Deleting `a,b` leaves precisely the original
plane icosahedron: place `v` in the face of `R` formerly occupied by `z`.
In fact the lift is exactly `K2 join T`.  It is `K7`-minor-free, while the
seven bags

\[
 \{a\},\{b\},\{0\},\{1\},\{5\},\{8,2,6\},\{4\}
\]

form `K7^vee`: the first six bags form the `K6` rim and the last bag meets
`{a},{b},{5},{8,2,6}`.  Thus this counterexample explains why the surviving alternative must be a
**cofacial** two-apex structure, not merely the assertion that `H` is
two-apex.

For completeness, `K7` exclusion is literal: in any putative seven-bag
model, discard the at most two bags containing `a,b`.  At least five
pairwise adjacent connected bags remain wholly in the planar icosahedron,
giving a forbidden `K5` minor there.
