# Uniform inequalities at a full minimum cut

## 1. Setting

Let `k>=3`, and let `G` be `k`-contraction-critical in the strong
minor-minimal sense:

\[
             \chi(G)=k,qquad
             \chi(H)\le k-1\quad\text{for every proper minor }H<G.
\tag{1.1}
\]

Let `S` be a minimum vertex cut of order `c=kappa(G)`, and write

\[
                         G-S=D_1\dot\cup\cdots\dot\cup D_m,
                         \qquad m\ge2.                       \tag{1.2}
\]

The graph `G` is connected: otherwise every component would be a proper
minor and hence `(k-1)`-colourable, contrary to `chi(G)=k`.  Thus the
displayed minimum cut and its components have their usual literal meaning.
Every `D_i` is full to `S`.  Indeed, `N(D_i)` is a cut contained in
`S`, so minimum-cardinality of `S` forces `N(D_i)=S`.

Put

\[
                              p=\chi(G[S]).                    \tag{1.3}
\]

Since `G[S]` is a proper minor obtained by deleting the nonempty
components of `G-S`,

\[
                              p\le k-1.                       \tag{1.4}
\]

## 2. Exact partial-trace saturation

For a side `i`, let `E_i` be the family of equality partitions of `S`
induced by `(k-1)`-colourings of `G[S union D_i]`.

### Theorem 2.1 (multi-block exact traces)

Fix `i`, let `0<=ell<=m-1`, and let

\[
                         A_1,\ldots,A_\ell\subseteq S          \tag{2.1}
\]

be pairwise disjoint nonempty independent sets.  There is a partition
`Pi in E_i` in which the `A_j` are `ell` distinct exact colour classes.
Equivalently, every side-extension family is `(m-1)`-block
trace-saturated.

### Proof

Choose distinct components `D_{h_1},...,D_{h_ell}` different from
`D_i`.  Contract each connected set

\[
                              D_{h_j}\cup A_j                  \tag{2.2}
\]

to a vertex `a_j`, and delete all other components except `D_i`.
Fullness makes the `a_j` a clique.  It also makes every
`x in S-union_j A_j` adjacent to every `a_j`.  The resulting graph is a
proper minor and hence has a `(k-1)`-colouring.  The `a_j` receive
distinct colours, and none of those colours occurs on any other boundary
vertex.  Expand only the boundary vertices of (2.2), retain the colours
on `D_i`, and discard the contracted opposite shores.  This colours the
closed side and gives exactly the asserted traces.  QED.

Despite this simultaneous saturation,

\[
                              \bigcap_{i=1}^m E_i=\varnothing. \tag{2.3}
\]

Indeed a common equality partition can be aligned by a permutation of
the colour names on every side and then glued, contrary to (1.1).
Thus the obstruction is not lack of any prescribed `m-1` independent
blocks; it is incompatibility among their completion states.

## 3. The sharp cut--component--chromatic inequality

### Theorem 3.1

Under (1.1)--(1.3),

\[
                         \boxed{\quad m\le p\le c-m\quad}.     \tag{3.1}
\]

In particular

\[
                         \boxed{\quad c\ge2m\quad}.           \tag{3.2}
\]

### Proof

For the lower bound, if `p<=m-1`, apply Theorem 2.1 to all the colour
classes of an optimal colouring of `G[S]`.  Its equality partition then
belongs to every `E_i`, contradicting (2.3).  Hence `p>=m`.

Take an optimal `p`-colouring of `G[S]`.  Any two singleton colour
classes are adjacent: otherwise their two vertices can be merged into
one colour class, contradicting optimality.  Hence all singleton colour
classes induce a clique.

Let `a` be the number of nonsingleton colour classes.  Suppose
`a<=m-1`.  Put all nonsingleton classes, together with enough singleton
classes to make `m-1` classes, first.  Connect those `m-1` classes
through the `m-1` opposite full shores.  Leave the remaining classes as
singleton boundary vertices.  They form a clique, and fullness makes
them adjacent to all the contracted class vertices.  Thus this exact
`p`-block partition extends over every closed side, exactly as in the
clique-residual block-gluing theorem.  This contradicts (2.3).

Therefore every optimal colouring has at least `m` nonsingleton classes.
Counting vertices gives

\[
                  c=|S|\ge 2a+(p-a)=p+a\ge p+m,               \tag{3.3}
\]

which is the upper bound in (3.1).  Combining it with `p>=m` proves
(3.2).  QED.

This improves the earlier singleton-class bound: a full minimum cut with
`m` components never has order below `2m`, regardless of the chromatic
number of its boundary.

### Corollary 3.2 (the first two equality layers)

1. If `c=2m`, then `p=m`, and every optimal colouring of `S` consists
   of `m` classes of order exactly two.
2. If `c=2m+1`, then `p in {m,m+1}`.  For `p=m`, every optimal colouring
   has class sizes `3,2,...,2`; for `p=m+1`, it has `m` classes of order
   two and one singleton class.

### Proof

Use `m<=p<=c-m` and the fact proved above that at least `m` optimal
classes are nonsingleton.  Equality in the vertex count leaves exactly
the displayed possibilities.  QED.

More generally, writing `c=2m+s` gives

\[
                              m\le p\le m+s,                  \tag{3.4}
\]

and at least `m` nonsingleton classes in every optimal boundary
colouring.  Thus Theorem 3.1 eliminates the infinite parameter range

\[
                              m>\lfloor c/2\rfloor            \tag{3.5}
\]

without any boundary enumeration.

## 4. Reserve inequalities in a least counterexample to Hadwiger

Now also suppose `G` has no `K_k` minor.  The full-shore reserve lift
gives, for every `Z subseteq S` with `|Z|=m-1`,

\[
                         \eta(G[S-Z])\le k-m-1.                \tag{4.1}
\]

Notice that `m<=p<=k-1` by Theorem 3.1 and (1.4), so `k-m>=1`; all
Hadwiger parameters in this paragraph are therefore defined, including
the endpoint `HC_1`.

Equivalently, if a `K_{k-m}` model exists in `G[S]`, every such model
uses at least

\[
                              c-m+2                            \tag{4.2}
\]

boundary vertices.  To see the equivalence, a model using at most
`c-m+1` vertices leaves `m-1` reserves outside its support; conversely a
model surviving one `(m-1)`-set deletion has support of at most
`c-m+1`.

Assume further that `k` is the least failing Hadwiger parameter, so
`HC_{k-m}` is available.  Equation (4.1) gives

\[
                         \chi(G[S-Z])\le k-m-1.                \tag{4.3}
\]

Adding back the `m-1` vertices of `Z` yields

\[
                              p\le k-2.                        \tag{4.4}
\]

Consequently every full minimum cut in a least counterexample satisfies

\[
              \boxed{\quad
                 m\le p\le\min\{c-m,k-2\},\qquad c\ge2m.
              \quad}                                         \tag{4.5}
\]

These bounds eliminate every pair `(c,m)` with `2m>c`, uniformly in
`k`, and also every `m>k-2`.

At equality `p=k-2`, (4.3) is tight for every reserve set:

\[
                         \chi(G[S-Z])=p-(m-1)                 \tag{4.6}
\]

because adding `Z` back gives the reverse inequality
`chi(G[S-Z])>=p-|Z|`.  Promoting this
row to a clique conclusion is not elementary: already the two-vertex
versions are close to double-critical colouring phenomena.  Thus
(4.5), rather than an unproved critical-to-clique assertion, is the safe
uniform endpoint of the purely chromatic argument.

## 5. Exact remaining uniform obstruction

The combination of Theorems 2.1 and 3.1 identifies the state gap
precisely:

* each side realizes an exact trace for every collection of at most
  `m-1` prescribed independent blocks;
* no equality partition is common to all sides; and
* every optimal boundary partition contains at least `m` nonsingleton
  blocks.

Thus any further uniform contradiction must synchronize the **completion
states of `m` nonsingleton blocks**.  Saturation of fewer blocks is
already automatic and cannot be the missing theorem.  Geometrically,
one needs either an `m`-th disjoint block carrier inside a shore, or a
separator exposing why that carrier cannot coexist with the first
`m-1`.  This is the exact contact-or-colour-gluing interface left after
the parameter range (3.5) is removed.

At the first equality layer `c=2m`, this interface is analysed exactly
in `hadwiger_uniform_equality_state_barrier.md`.  The boundary has an
optimal partition into `m` independent pairs.  Every side accepts either
the all-pair state or each prescribed one-pair split state.  A
minimal-empty-intersection family of such states is nevertheless
consistent, graph-realizable, and separately compatible with full
`2m`-connectivity and crossed internal one-step criticality.  Hence the
last-pair carrier/separator exchange is genuinely geometric; state
algebra alone cannot close even the equality layer.
