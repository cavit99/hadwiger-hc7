# Opposite colouring responses at an independent two-vertex odd-cycle transversal

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_independent_oct_opposite_response_audit.md`](hc7_order8_independent_oct_opposite_response_audit.md).
This is an unbounded colouring reduction.  It does not prove `HC_7`.

This note treats the static geometry left by the honest strict-reversal
quotient.  Its boundary has two nonadjacent vertices `d,e` whose deletion
leaves a bipartite graph.  Two one-defect connected subgraphs on one shore
and two boundary-full connected subgraphs on the other shore each produce a
six-colouring with one of exactly two boundary equality patterns.  A
counterexample can survive only when the two shores permit opposite patterns.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing,
 \qquad |S|=8.                                      \tag{1.1}
\]

Assume that every proper minor of `G` is six-colourable.  Let `d,e` be
distinct nonadjacent vertices of `G[S]`, and let

\[
                         S-\{d,e\}=X\mathbin{\dot\cup}Y              \tag{1.2}
\]

be a bipartition.  Assume that `X,Y` are nonempty and that each of `d,e`
has a neighbour in each of `X,Y`.

Suppose `L` contains disjoint connected subgraphs `A_d,A_e` such that

\[
 N_G(A_d)\cap S=S-\{d\},
 \qquad
 N_G(A_e)\cap S=S-\{e\},                            \tag{1.3}
\]

and `R` contains disjoint connected subgraphs `Q_1,Q_2`, each adjacent to
every literal vertex of `S`.

## 2. The two response sets

Contract a spanning tree of each of

\[
                         A_d\cup X,
                         \qquad A_e\cup Y.             \tag{2.1}
\]

These are disjoint connected sets.  Their two contraction images are
adjacent, and each of `d,e` is adjacent to both images.  Thus they induce a
`K_4` minus the edge `de`.  The contraction gives a proper minor.  Every
six-colouring of that minor restricts and expands to a proper colouring of
`G[R\cup S]` in which `X` and `Y` are two distinct monochromatic blocks,
while `d,e` use colours different from both block colours.  The vertices
`d,e` may have equal or distinct colours.

Let

\[
                         \mathcal R\subseteq\{=,\ne\}                 \tag{2.2}
\]

be the set of equality types induced by **all** proper six-colourings of
`G[R\cup S]` in which `X,Y` are distinct monochromatic blocks and `d,e`
avoid both block colours.  The contraction above proves that
\(\mathcal R\ne\varnothing\).

Similarly, contract spanning trees of

\[
                         Q_1\cup X,
                         \qquad Q_2\cup Y.             \tag{2.3}
\]

The two images are adjacent, and boundary-fullness makes each image
adjacent to both `d,e`.  These contractions therefore give the same
`K_4-de` boundary pattern in a proper minor.  Let

\[
                         \mathcal L\subseteq\{=,\ne\}                 \tag{2.4}
\]

be the set of equality types induced by all proper six-colourings of
`G[L\cup S]` with the same two prescribed monochromatic blocks and colour
avoidance.  The contractions in (2.3) prove that
\(\mathcal L\ne\varnothing\).

## 3. Opposite-response theorem

### Theorem 3.1

Under the hypotheses above, at least one of the following holds:

1. `G` is six-colourable; or
2. the two response sets are opposite singletons; that is, either

   \[
                        \mathcal L=\{=\},
                        \qquad \mathcal R=\{\ne\},      \tag{3.1}
   \]

   or the same display holds with \(\mathcal L,\mathcal R\) interchanged.

   Moreover, on the closed shore whose response set is \(\{\ne\}\), every
   colouring contributing that type has a two-colour `d`--`e` path whose
   internal vertices lie in its open shore.

#### Proof

If \(\mathcal L\) and \(\mathcal R\) contain a common type, choose one colouring
of each closed shore with that type.  In type `=`, both colourings induce
the same three-block partition

\[
                         X\mid Y\mid\{d,e\};            \tag{3.2}
\]

in type \(\ne\), they induce the same four-block partition

\[
                         X\mid Y\mid\{d\}\mid\{e\}.    \tag{3.3}
\]

Permute colour names on one shore to align the blocks.  Since there is no
edge between `L` and `R`, the two colourings glue to a proper six-colouring
of `G`.

Hence, if `G` is not six-colourable, the two nonempty subsets
`\mathcal L` and `\mathcal R` of the two-element set `\{=,\ne\}` are
disjoint.  They are therefore the two opposite singleton sets.

Suppose, without loss of notation, that \(\mathcal R=\{\ne\}\).  Take a
colouring contributing that type on the `R`-shore.  Let \(\alpha,\beta\)
be the two distinct colours on `d,e`.  If `d,e` lie in different components
of the subgraph induced by colours `alpha,beta`, interchange those two
colours on the component containing `d`.  This gives another proper
colouring, and it makes `d,e` equal.

No vertex of `X\cup Y` changes colour in that interchange: both `d,e` are
adjacent to each of the monochromatic blocks `X,Y`, so the two block colours
are different from \(\alpha,\beta\).  Thus the new colouring still satisfies
the defining boundary conditions and contributes type `=` to \(\mathcal R\), contradicting
\(\mathcal R=\{\ne\}\).  Therefore `d,e` lie in one two-colour component.  Its
`d`--`e` path contains no other boundary vertex, again because all vertices
of `X\cup Y` use the two block colours.  The internal vertices of the path
therefore lie in `R`. \(\square\)

## 4. Localization at the two full connected subgraphs

### Theorem 4.1

Assume that `G` is not six-colourable and orient Theorem 3.1 so that

\[
                         \mathcal L=\{=\},
                         \qquad \mathcal R=\{\ne\}.     \tag{4.1}
\]

Then every `d`--`e` path in `G[R\cup\{d,e\}]` has an internal vertex in
`Q_1\cup Q_2`.

#### Proof

Suppose that `P` is a `d`--`e` path whose internal vertices avoid
`Q_1\cup Q_2`.  The edge `de` is absent, so `P` has an internal vertex.
Contract edges of `P` until its image is one edge with distinct ends `d,e`.
At the same time contract spanning trees of the two disjoint connected sets

\[
                         Q_1\cup X,
                         \qquad Q_2\cup Y.              \tag{4.2}
\]

The three contractions have disjoint interiors.  The two images in (4.2)
are adjacent, each is adjacent to both `d,e`, and the contracted path
supplies the edge `de`.  These four objects therefore form a `K_4` in a
proper minor of `G`.

Six-colour that minor and restrict the colouring to `G[L\cup S]`.  Expanding
the two contractions in (4.2) makes `X,Y` distinct monochromatic blocks,
while the `K_4` forces `d,e` to have distinct colours different from both
block colours.  This contributes type `\ne` to `\mathcal L`, contrary to
(4.1). \(\square\)

### Corollary 4.2

In the orientation (4.1), every forced bichromatic path supplied by Theorem
3.1 meets `Q_1\cup Q_2` internally.

This is a literal host localization: the obstruction is no longer the
existence of a `d`--`e` path, but its unavoidable first intersections with
the two named full connected subgraphs.

## 5. Relation to the induced-path branch

The exact three-component induced-path branch has a stronger direct
colour-gluing argument: the path itself is three-colourable, so the common
partition `X | Y | {d,e}` can be realized on that closed side without first
passing through the response dichotomy above.  The present theorem is kept
for more general two-shore configurations in which the side containing
`A_d,A_e` is not known to be three-colourable.  No finite boundary
classification is a hypothesis of Theorems 3.1 or 4.1.

## 6. Trust boundary

Theorems 3.1 and 4.1 prove a common colouring or an exact opposite-response
normal form in which every `d`--`e` path on the proper-response shore must
meet `Q_1\cup Q_2`.  They do not split either full connected subgraph,
decode the first intersections into an explicit `K_7` minor, or return an
order-seven separation.  Those are the remaining label-preserving host
obligations.

The theorem uses no identification of a palette colour with a named
branch-set label.  It also makes no assertion when `G[S-\{d,e\}]` is
nonbipartite.

## 7. Dependencies

- the proper-minor six-colourability assumption from minor minimality.
