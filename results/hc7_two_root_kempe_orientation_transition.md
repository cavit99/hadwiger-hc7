# A Kempe transition between two colour-dominating roots

**Status:** written proof; independently audited in
[`hc7_two_root_kempe_orientation_transition_audit.md`](hc7_two_root_kempe_orientation_transition_audit.md).

This note identifies the exact geometry of a single Kempe interchange
which transfers colour domination from one of two nonadjacent external
vertices to the other.  Its main reusable conclusion is that the
interchanged component is one open side of an actual separation, and that
specified sides of its bipartition have neighbours in every untouched
colour class.  The conclusion is independent of any preselected minor
model.

## 1. Exact transition theorem

Let `J` be a graph, let `a,b` be two new nonadjacent vertices with specified
neighbourhoods in `J`, and put

\[
                         G=J+\{a,b\}.
\]

For a proper colouring `d` of `J`, say that a root `r in {a,b}` is
**colour-dominating in `d`** if `N_J(r)` meets every colour class of `d`.

### Theorem 1.1 (orientation-changing Kempe component)

Let `c` be a proper colouring of `J` with a palette of `q>=2` colours.
Assume that every proper `q`-colouring of `J` makes at least one of `a,b`
colour-dominating.  Let `alpha,beta` be two colours, let `K` be a component
of

\[
                 J[c^{-1}(\{\alpha,\beta\})],
\]

and let `c'` be obtained by interchanging `alpha,beta` on `K`.  Suppose
that

* `a` is colour-dominating in `c` and `b` is not; and
* `b` is colour-dominating in `c'` and `a` is not.

Then there are uniquely determined colours

\[
             \lambda,\gamma\in\{\alpha,\beta\},
\]

where `lambda` is lost by `a` and `gamma` is gained by `b`.  If
`bar(lambda)` and `bar(gamma)` denote the other colours of the pair, then
the following assertions hold.

1. The contacts of `a` satisfy

   \[
   \begin{aligned}
    &N_J(a)\cap c^{-1}(\lambda)\ne\varnothing,
      &&N_J(a)\cap c^{-1}(\lambda)\subseteq V(K),\\
    &N_J(a)\cap V(K)\cap c^{-1}(\bar\lambda)=\varnothing,
      &&N_J(a)\cap(c^{-1}(\bar\lambda)-V(K))\ne\varnothing.
   \end{aligned}                                           \tag{1.1}
   \]

2. The contacts of `b` satisfy

   \[
   \begin{aligned}
    &N_J(b)\cap c^{-1}(\gamma)=\varnothing,\\
    &N_J(b)\cap V(K)\cap c^{-1}(\bar\gamma)\ne\varnothing,
      &&N_J(b)\cap(c^{-1}(\bar\gamma)-V(K))\ne\varnothing.
   \end{aligned}                                           \tag{1.2}
   \]

3. For every colour `theta` outside `{alpha,beta}`, the set

   \[
                V(K)\cap c^{-1}(\lambda)                 \tag{1.3}
   \]

   has a neighbour of colour `theta` in `J-K`.  The set

   \[
                V(K)\cap c^{-1}(\bar\gamma)              \tag{1.4}
   \]

   also has a neighbour of colour `theta` in `J-K`.

4. The graph `G[V(K) union {a,b}]` is connected and contains an
   `a-b` path whose internal vertices lie in `K` and have only colours
   `alpha,beta`.

5. The open neighbourhood `N_G(K)` is an actual separator of `G`, with

   \[
        \{a,b\}\subseteq N_G(K),\qquad
        N_G(K)-\{a,b\}\subseteq
        \bigcup_{\theta\notin\{\alpha,\beta\}}c^{-1}(\theta).
                                                               \tag{1.5}
   \]

If `G` is `k`-connected, then

\[
                    |N_J(K)|\ge k-2.                         \tag{1.6}
\]

In particular, when `q=6` and `G` is seven-connected, `N_J(K)` has at
least five vertices and meets each of the four untouched colour classes.
If `|N_J(K)|=5`, then `N_G(K)` is an actual order-seven separator.

#### Proof

Only the incidence of the two colours `alpha,beta` with a root's
neighbourhood can change under the interchange.  Since `a` sees both
colours before the interchange but is not colour-dominating afterwards,
it loses at least one of them.  It cannot lose both: losing `alpha` would
require every `alpha`-neighbour of `a` to lie in `K` and no
`beta`-neighbour of `a` to lie in `K`, while losing `beta` would require
the two opposite conditions.  Thus it loses a unique colour `lambda`.
Writing out what it means for that colour to disappear, while the other
one remains, gives exactly (1.1).

The root `b` can gain only one of `alpha,beta`.  It cannot have missed
both before the interchange, because an interchange creates no contact
when neither colour occurred on its neighbourhood.  Thus it missed a
unique colour `gamma`.  No `gamma`-neighbour existed before the
interchange.  To create one, `b` must have a
`bar(gamma)`-neighbour in `K`; to retain the other colour after the
interchange, it must also have a `bar(gamma)`-neighbour outside `K`.
This proves (1.2).

Fix a colour `theta` outside `{alpha,beta}`.  Suppose that no vertex of
`K` having colour `lambda` has a neighbour of colour `theta`.  Recolour
every `lambda`-coloured vertex of `K` with `theta`.  This is proper:
vertices of one colour are independent, all vertices of `K` have colours
`alpha,beta`, and the assumed absence of a `theta`-coloured neighbour
removes the only possible new conflict.  By (1.1), `a` now misses
`lambda`.  By (1.2), `b` still misses `gamma`: if `gamma=lambda`, no
`gamma` contact is created, and if `gamma` is the other switched colour,
that colour was not changed.  This gives a proper `q`-colouring in which
neither root is colour-dominating, contrary to the hypothesis.  Hence
(1.3) has a neighbour of every untouched colour.

Apply the same argument to `c'` and the inverse interchange.  In `c'`,
the root `b` loses `gamma` on returning to `c`.  The vertices of `K`
having colour `gamma` in `c'` are precisely those having colour
`bar(gamma)` in `c`.  Recolouring that side to `theta`, if it had no
`theta`-neighbour, would leave `a` missing `lambda` and make `b` miss
`gamma`.  This proves the assertion for (1.4).

By (1.1), `a` has a neighbour in `K`, and by (1.2), so does `b`.  Since
`K` is connected, a path in `K` between two such neighbours extends to
the path in item 4.  The two contacts may be the same vertex; this occurs
when `lambda=bar(gamma)` and is not excluded by the hypotheses.

Every vertex of `J-K` having colour `alpha` or `beta` is anticomplete to
`K`; otherwise it would belong to the same two-colour component.  Thus
the last inclusion in (1.5) holds.  The two roots belong to `N_G(K)` by
the preceding paragraph.  Finally, (1.1) supplies a
`bar(lambda)`-coloured neighbour of `a` outside `K`.  That vertex is
anticomplete to `K`, so it survives outside `K union N_G(K)`.  Deleting
`N_G(K)` consequently leaves both the nonempty component `K` and a
vertex outside it.  Hence `N_G(K)` is an actual separator.

If `G` is `k`-connected, every actual separator has order at least `k`.
Since its two root vertices are distinct from `J`, (1.6) follows.  For
`q=6,k=7`, item 3 gives all four untouched colours and (1.6) gives at
least five vertices.  Equality makes the full separator have order
seven.  \(\square\)

### Corollary 1.2 (two-sided and one-sided forms)

Under Theorem 1.1 there are two genuinely different geometries.

1. If `lambda=gamma`, the two sets in (1.3) and (1.4) are the opposite
   colour sides of `K`.  Each side has a neighbour in every untouched
   colour class, and the two root contacts on `K` have different colours.
2. If `lambda!=gamma`, the sets in (1.3) and (1.4) are the same colour
   side of `K`.  That side has neighbours in every untouched colour
   class, and both roots may meet `K` at the same vertex.

Thus an orientation-changing interchange does not always give two
distinct root portals or two separately saturated sides.

## 2. Application to a spanning `K_7`-minus-one-edge model

Suppose now that `q=6`, `G` is seven-connected, and `J=G-{a,b}` has five
pairwise disjoint connected branch sets

\[
                         B_1,\ldots,B_5
\]

which partition `V(J)`, are pairwise adjacent, and are each adjacent to
both `a` and `b`.  Thus these five sets and the singleton roots form a
spanning `K_7`-minus-one-edge model, with `ab` its only absent
branch-set adjacency.

Theorem 1.1 gives the strict separation

\[
 \bigl(V(K)\cup N_G(K),\;V(G)-V(K)\bigr),                \tag{2.1}
\]

whose open `K`-side is nonempty and whose other open side contains an
`alpha`- or `beta`-coloured vertex.  Consequently:

* if `|N_J(K)|=5`, (2.1) is an actual order-seven separation;
* otherwise the adhesion has order at least eight and `K` is a strict
  connected-side reduction.

There is one immediate label-preserving completion.  If, for some `i`,
`K subseteq B_i` and `B_i-K` contains a connected nonempty subgraph `W`
which is adjacent to `K`, to every `B_j` with `j!=i`, and to at least one
of `a,b`, then `G` contains a `K_7` minor.  Indeed, retain as a singleton
the root adjacent to `W`, absorb `K` into the other root, and use `W` and
the four sets `B_j`, `j!=i`, as the other five branch sets.

The transition theorem does not force this completion.  The component
`K` may cross several of the five preselected branch sets, and removing
its vertices may disconnect those sets or destroy their named
adjacencies.  Likewise, the four untouched palette colours in item 3 are
not labels of four branch sets.  Therefore (2.1) is a genuine strict
separation, but an adhesion of order at least eight is not yet a
label-preserving branch-set split.  Turning that separation into either
such a split or a fixed two-vertex obstruction is the exact remaining
composition problem.

## 3. Trust boundary

The theorem proves more than the existence of a bichromatic path: it
forces a colour-saturated side (or two sides) of the component and an
actual separator.  It does not identify colours with branch-set labels,
preserve connectivity of the five branch sets after deleting `K`, or
reduce an adhesion of order greater than seven to order seven.
