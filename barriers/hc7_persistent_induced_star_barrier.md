# Three persistent edges need not contain an induced two-leaf star

**Status:** explicit barrier with deterministic verifier; not an `HC_7`
counterexample.

The quantitative persistence theorem can give three deletion-persistent
edges at one vertex.  This example shows that their other endpoints may
form a triangle.  Thus persistence multiplicity alone does not force two
jointly persistent incident edges with nonadjacent leaves.

## Refuted intermediate claim

> In every seven-connected, `K_7`-minor-free graph with a spanning labelled
> `K_7`-minus-one-edge model, if three edges incident with a rooted vertex
> are deletion-persistent for that model, then two of them have nonadjacent
> other endpoints.

The example even has root degree eight and the three edges are jointly
persistent in every pair.

## Construction

Let `I` be the icosahedron.  Its triangular faces, in the deterministic
labelling used by the verifier, are

\[
\begin{array}{c|c@{\qquad}c|c}
0&081&10&289\\
1&078&11&346\\
2&0\,11\,7&12&3\,10\,4\\
3&0\,5\,11&13&3\,9\,10\\
4&0\,1\,5&14&4\,5\,6\\
5&1\,2\,6&15&4\,11\,5\\
6&1\,8\,2&16&4\,10\,11\\
7&1\,6\,5&17&7\,9\,8\\
8&2\,3\,6&18&7\,10\,9\\
9&2\,9\,3&19&7\,11\,10.
\end{array}
\]

Form a graph `H` with vertices `V_i` for the twelve vertices of `I` and
`F_j` for its twenty faces.  Join `V_i` to `F_j` when vertex `i` lies on
face `j`, and join `F_j` to `F_k` when the two faces share an edge.  This is
the planar dual of the truncated icosahedron.  It is five-connected, has
32 vertices, and every vertex has degree five or six.

Let

\[
                             G=K_2\vee H,
\]

where the two universal vertices are `alpha,beta`.  Then `G` is
seven-connected.  It has no `K_7` minor: a `K_7` model would have at least
five branch sets avoiding `alpha,beta`, and those branch sets would form a
`K_5` model in the planar graph `H`.

Use the following seven branch sets:

\[
\begin{array}{c|l}
R&\{F_0\}\\
S&\{\alpha,V_0,F_1\}\\
P&\{\beta\}\\
C_0&\{F_{17},F_{18},F_{19},F_2,V_7,V_8\}\\
C_1&\{F_5,V_1,V_6\}\\
C_2&\{F_{10},F_6,F_8,F_9,V_2,V_3,V_9\}\\
C_3&\{F_{11},F_{12},F_{13},F_{14},F_{15},F_{16},F_3,F_4,F_7,
       V_{10},V_{11},V_4,V_5\}.
\end{array}
\]

They partition `V(G)`, are connected, and form a spanning labelled
`K_7`-minus-one-edge model whose only missing adjacency is `C_0C_1`.
The root `F_0` has eight neighbours:

\[
       \alpha,\beta,V_0,V_8,V_1,F_1,F_6,F_4.
\]

Exactly three root edges enter `S`, namely

\[
                         F_0\alpha,\qquad F_0V_0,\qquad F_0F_1.
\]

Deleting any one or any two of them leaves another `R-S` edge, so the
three are pairwise jointly deletion-persistent.  Their other endpoints
induce a triangle: `alpha` is universal and `V_0F_1` is an incidence edge.
Every other root edge is the sole edge from `R` to its foreign branch set,
so these are exactly the persistent incident edges.

The deterministic verifier checks the construction, connectivity,
planarity of `H`, the branch sets, the missing model adjacency, and the
persistence statement:

```text
PYTHONPATH=active/runtime/deps python3 barriers/hc7_persistent_induced_star_barrier_verify.py
```

Expected output:

```text
verified persistent induced-star barrier
```

## Exact scope

This graph has actual order-seven separations.  For example, the two
universal vertices together with the five neighbours in `H` of any
degree-five vertex separate that vertex.  The construction therefore does
not refute the stronger conjectural statement which additionally assumes
that no actual order-seven separation exists.  It refutes only the attempt
to deduce the induced star from persistence multiplicity, degree eight,
seven-connectivity, `K_7`-minor exclusion, and the spanning labelled model
alone.
