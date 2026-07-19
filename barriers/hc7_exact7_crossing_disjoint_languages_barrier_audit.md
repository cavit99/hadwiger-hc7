# Independent internal audit: exact-seven disjoint-language barrier

**Verdict:** GREEN for the exact revisions

```text
barriers/hc7_exact7_crossing_disjoint_languages_barrier.md
SHA-256 5698af94146e423bb62945ed2aec904cbff4f15f8eac4ba23811c2c02a51e3ad

barriers/hc7_exact7_crossing_disjoint_languages_barrier_verify.py
SHA-256 2641e614f0c443fdd98e2ed01492ef24fc938d9e1ae3255cd742b004c456fd64
```

This is a separate internal mathematical audit, not external peer review.
It checked the literal graph and separation, connectivity, both intact
closed-shore colouring languages, the three proper-minor responses, the
forced boundary partition, packing and demand, the explicit minor model,
and the stated trust boundary.

## 1. Host, separation, and connectivity

The construction has the claimed 22 vertices and 124 edges.  The displayed
sets `A,S,B` partition the vertex set, `|S|=7`, there are no `A`--`B`
edges, both open shores are connected, and each open shore is adjacent to
every literal boundary vertex.  The two designated independent edges have
their interior ends in `A` and their other ends in `S`.

The verifier exhausts every deletion of at most six vertices and confirms
that the remainder is connected; deleting `S` leaves exactly the two
nonempty components `A` and `B`.  The written connectivity proof is also
valid.  The join `J\vee K_{2,3}` is seven-connected because `J` and
`K_{2,3}` are both two-connected.  For every nonempty subset of `B`, the
verifier independently checks at least seven neighbours outside the set.
Consequently no component lying wholly in `B` can be separated from the
surviving join by deleting at most six vertices.

## 2. The two intact closed-shore languages

On the `A`-side, `G[A\cup S]=J\vee K_{2,3}`.  The diamond equalities make
`J` four-chromatic, while the connected bipartite factor has chromatic
number two.  Hence this closed shore is exactly six-chromatic.  Every
six-colouring uses disjoint palettes of orders four and two on the two join
factors, and the unique bipartition colouring of the connected
`K_{2,3}` forces

\[
                              c(y_1)=c(y_2).
\]

On the `B`-side, `Q\cup\{r,s\}` is a literal `K_6`.  The vertices `y_1`
and `y_2` are complete to `Q` and adjacent respectively to `r` and `s`.
They are therefore forced to use the colours of `s` and `r`, respectively,
so

\[
                              c(y_1)\ne c(y_2).
\]

The explicit response rows restrict to a proper six-colouring of this
closed shore.  Thus both intact closed shores are exactly six-chromatic,
but their boundary extension languages are disjoint.  This proves that
the full host is not six-colourable.  A seven-colouring follows from a
six-colouring of `G-e` by giving one endpoint of the restored edge a new
colour, so `chi(G)=7`.

## 3. Response profile and forced partition

The common deletion has exactly the endpoint signatures `EE`, `EP`, and
`PE`.  The absent `PP` signature is the ordinary three-colour obstruction
of `K_4-\{ab,cd\}` after the two diamond equalities are imposed.  The
three displayed rows were checked edge by edge.  The `EP` and `PE` rows
colour `G-e` and `G-f`, while equality of the appropriate endpoints lets
the same rows descend to `G/e` and `G/f`; the `EE` row descends to
`G/e/f`.  The literal `K_6=Q\cup\{r,s\}` survives every named operation,
so these graphs are exactly, rather than merely at most, six-chromatic.

The verifier enumerates all 48 normalized common-deletion six-colourings.
They all induce precisely

\[
 \Pi=\{\{b\},\{d\},\{x_1,x_2\},\{y_1,y_3\},\{y_2\}\}.
\]

The written forcing argument is sound.  The `K_6` fixes six distinct
colours on `Q,r,s`; the complete join and the triangle in `J_0` force
three disjoint colours on each of `J_0` and `K_{2,3}`.  Consequently
`x_1=x_2`.  Adjacency of `y_3` to `Q\cup\{r\}` forces `y_3=y_1`, and the
second diamond together with the edge from `d` to `bp` forces `b\ne d`.

## 4. Packing, demand, and terminal minor

The two displayed connected subsets of `A` are boundary-full.  Every
boundary-full connected subset of `A` must join a `b`-portal to a
`d`-portal, and every such path meets `\{ap,bp\}`.  Thus at most two are
disjoint, proving `nu_A=2`.  The vertex `ell` is boundary-full and is the
unique `B`-neighbour of `x_1`, so every boundary-full connected subset of
`B` contains `ell`; hence `nu_B=1`.

The boundary is `I_2\vee K_{2,3}` and has chromatic number three.  The
singleton vertices of `Pi` are `b,d,y_2`, inducing the path
`b-y_2-d`; their clique number is two.  Therefore the asserted demand is
`5-2=3>nu_B`.

The seven displayed branch sets form an explicit `K_7`-minor model.  In
particular, the last set `\{s,y_2,x_2\}` is connected, is adjacent to all
four `Q` singletons, to `y_1` through `x_2`, and to `r` through `s`.
All other required adjacencies are literal clique or displayed table
edges.  Finally, deleting `y_3` leaves the incompatible equations
`y_1=y_2` and `y_1\ne y_2`, so the resulting proper subgraph is still not
six-colourable; the restricted `EP` response gives the stated upper bound
of seven.

## 5. Scope

The barrier is correctly scoped.  It contains a `K_7` minor and is not
minor-minimal subject to being non-six-colourable.  It therefore does not
refute a terminal theorem for a hypothetical minor-minimal,
`K_7`-minor-free counterexample.  It proves only that exact boundary order,
seven-connectivity, two six-colourable intact shores, the `(2,1)` packing
vector, excessive demand, and the complete `EE/EP/PE` response profile do
not by themselves synchronize the intact boundary languages.  Any
positive theorem must use at least one of the deliberately omitted global
hypotheses, such as `K_7`-minor exclusion or further proper-minor
colourings.
