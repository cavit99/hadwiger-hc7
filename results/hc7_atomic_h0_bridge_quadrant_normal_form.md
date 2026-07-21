# Bridge normal form for the atomic `H_0` subdivision

**Status:** written proof and computer-assisted finite result; separate
internal audit GREEN.

The hard disjoint-demand atomic collision contains a subdivision of

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}.                 \tag{1.1}
\]

This note determines exactly what one path through an `H_0`-bridge can do,
confines every bridge in a `K_7`-minor-free host to one of four attachment
regions, and closes two sparse but unbounded augmentation cases.  It does
not yet combine an arbitrary family of confined bridges while preserving
the three connected support subgraphs of the atomic common frame.

## 1. Attachment supports

Let `T` be a subdivision of `H_0`, with the eight branch vertices retaining
their labels.  Write `T_uv` for the segment that replaces the edge `uv` of
`H_0`.  For \(z\in V(T)\), define its **endpoint support** by

\[
 \sigma_T(z)=
 \begin{cases}
  \{v\},&z\text{ is the branch vertex }v,\\
  \{u,v\},&z\in\operatorname{int}(T_{uv}).
 \end{cases}                                             \tag{1.2}
\]

A `T`-path is a path with distinct ends in `T` and no internal vertex in
`T`.  A `T`-bridge is either an edge outside `T` with both ends in `T`, or a
component of `G-V(T)` together with all of its incident edges to `T`.  Its
vertices in `T` are its attachments.

## 2. A path crossing a missing pair is terminal

### Theorem 2.1 (cross-pair path closure)

Suppose a `T`-path `Q` has ends `p,q`.  If

\[
 a\in\sigma_T(p)\quad\text{and}\quad b\in\sigma_T(q),   \tag{2.1}
\]

then \(T\cup Q\) contains an explicit `K_7`-minor model.  The same holds
with `a,b` replaced by `c,d`.

#### Proof

Assume (2.1).  Let `A_0` be the subpath from `a` to `p` on the segment
incident with `a`, with `A_0={a}` when `p=a`.  Define `B_0` symmetrically.
The sets `A_0,B_0` are disjoint.  Indeed, `ab` is not an edge of `H_0`,
distinct segment interiors are disjoint, and a branch vertex other than
`a` cannot have `a` in its endpoint support.

Choose an edge of `Q`.  Put the part of `Q` before that edge together with
`A_0` into `A`, and put the part after it together with `B_0` into `B`.
Then `A,B` are disjoint connected sets, and the chosen edge joins them.
Put

\[
 C_x=V(T_{cx})\cup\bigl(V(T_{xd})-\{d\}\bigr),          \tag{2.2}
\]

and start the four other branch sets at the literal vertices `d,e,f,g`.

Allocate the unused internal vertices of every segment of `T` to a branch
set containing one of its ends.  On a segment cut at `p` or `q`, allocate
the unused far suffix to the branch set at its far end.  Every branch set
remains connected, the cut edge retains the corresponding adjacency, and
all seven branch sets are disjoint.  The chosen edge of `Q` supplies the
formerly absent `ab` adjacency.  The last edge of `T_xd` supplies the
formerly absent `cd` adjacency between `C_x` and the set containing `d`.
Every other pair is joined along a segment of `T`.  Thus

\[
                      A,B,C_x,D,E,F,G                   \tag{2.3}
\]

is a `K_7`-minor model.

For a `c`--`d` crossing, interchange the two missing pairs.  Merge `a`
with `x` along `T_ax`, and use the `x`-side of `T_xb` to repair the absent
`ab` adjacency.  The same allocation proves the claim.  \(\square\)

The theorem deliberately says nothing about the absent common-frame pair
`xe`.  The subdivision `T` has no `xf` or `xg` segment; those two contacts
belong to separately owned connected support subgraphs.

## 3. Four attachment regions

For \(r\in\{a,b\}\) and \(s\in\{c,d\}\), let

\[
 T^{r,s}=\bigl(V(H_0)-\{r,s\}\bigr)
 \ \cup\!\!\bigcup_{\substack{uv\in E(H_0)\\
                         \{u,v\}\cap\{r,s\}=\varnothing}}
                         \operatorname{int}(T_{uv}).     \tag{3.1}
\]

Thus a point lies in `T^{r,s}` precisely when its endpoint support omits
both `r` and `s`.

### Theorem 3.1 (quadrant confinement)

If `G` has no `K_7` minor, every `T`-bridge `B` has some
\(r\in\{a,b\}\) and \(s\in\{c,d\}\) such that all attachments of `B` lie in
`T^{r,s}`.

If `B` is the bridge arising from a component `K` of `G-V(T)`, then

\[
 |\operatorname{Att}(B)|=|N_G(K)|\ge7                 \tag{3.2}
\]

when `G` is seven-connected, and the lower bound is eight when `G` is
eight-connected.  The numerical bound does not apply to an edge bridge,
which has two attachments.

#### Proof

Put

\[
 \Sigma(B)=\bigcup_{z\in\operatorname{Att}(B)}\sigma_T(z).
\]

If both `a,b` belonged to \(\Sigma(B)\), they would occur at distinct
attachments because no point of `T` has endpoint support containing the
nonedge `ab`.  A path through `B` between those attachments would contradict
Theorem 2.1.  Hence \(\Sigma(B)\) omits `a` or `b`.  It similarly omits `c` or
`d`, proving the first assertion.

For a nontrivial bridge, its attachment set is exactly `N_G(K)`.  If this
set is a proper subset of `V(T)`, deleting it separates `K` from a remaining
vertex of `T`, so connectivity gives the required bound.  If it equals
`V(T)`, it has at least the eight branch vertices, which is enough for both
displayed cases.  \(\square\)

Let `W` be the subdivided wheel in `T` with rim order

\[
                         a,c,b,d,a
\]

and hub `x`.  Intersecting (3.1) with `W` shows more concretely that every
bridge has all of its wheel attachments in one of the four closed
subdivided triangles

\[
 W[a,c,x],\quad W[c,b,x],\quad W[b,d,x],\quad W[d,a,x]. \tag{3.3}
\]

The many attachments guaranteed by (3.2) may still lie on only a few long
segment intervals; (3.2) is not a count of distinct endpoint labels.

## 4. Exact finite classification of one bridge path

The retained checker is
[`../active/hc7_atomic_h0_single_bridge_falsifier.py`](../active/hc7_atomic_h0_single_bridge_falsifier.py).
Run it from the repository root with

```text
.venv/bin/python -B active/hc7_atomic_h0_single_bridge_falsifier.py
```

### Theorem 4.1 (one-path classification)

Up to suppressing degree-two vertices, there are 488 placements of one
`T`-path according to whether each end is a branch vertex or lies in the
interior of one of the 23 segments of `T`.  Exactly 96 placements contain a
`K_7` minor.  They are precisely the placements for which the two endpoint
supports contain `ab` or `cd` across them.  Each of the other 392 placements
becomes planar after deleting one of

\[
                         \{e,f\},\quad\{e,g\},\quad\{f,g\}. \tag{4.1}
\]

Consequently the converse to Theorem 2.1 is exact for one added `T`-path:
if it does not cross a missing pair at the level of endpoint supports, its
union with `T` is two-apex and has no `K_7` minor.

#### Finite proof and certificates

There are eight branch attachment classes and 23 segment-interior classes.
Two distinct classes give `binom(31,2)=465` unordered placements.  Two
distinct points on the same segment give 23 further placements.  Reversing
their order is an isomorphism, so these 488 cases are exhaustive.  An
arbitrary bridge-path length and unused segment intervals only subdivide a
canonical case.  A path parallel to an existing segment is accommodated by
the explicit nonempty interval in the canonical graph and does not change
the conclusion.

For every canonical graph, the checker enumerates every spanning partition
into seven nonempty sets, tests the connectedness of all seven sets, and
tests all 21 required quotient adjacencies.  This is an exact clique-minor
oracle: in a connected graph every minor model can be made spanning by
absorbing components outside its branch sets.  It returns models in exactly
the 96 cases predicted by Theorem 2.1.

In each of the 392 negative cases, the checker independently deletes a pair
in (4.1), obtains a planar rotation system from `networkx`, and validates
that rotation system with `check_structure()`.  A `K_7` model in a graph
made planar by two vertex deletions would leave a `K_5` model in the planar
remainder after discarding at most two apex-containing branch sets, which
is impossible.

The detailed counts are

| endpoint types | terminal | two-apex |
|---|---:|---:|
| branch--branch | 2 | 26 |
| branch--segment | 24 | 160 |
| segment--segment | 70 | 206 |
| **total** | **96** | **392** |

The selected planarizing certificates, in the checker's fixed order, are
`ef` for 361 cases, `eg` for 26 cases, and `fg` for 5 cases.  A case may
have more than one planarizing pair.

## 5. Seven-connectivity closes a one-interior-vertex residue

Put

\[
 Z_{ab}=\{c,d,e,f,g,x\},\qquad H_{ab}=G-Z_{ab}.         \tag{5.1}
\]

### Theorem 5.1 (clean path, exact separator, or two paths)

Let `G` be seven-connected and contain `T`.  At least one of the following
holds:

1. `G` contains a `K_7` minor;
2. some vertex `v in V(H_ab)-{a,b}` makes
   \(Z_{ab}\cup\{v\}\) an exact order-seven separator between `a` and `b`; or
3. `H_ab` contains two internally vertex-disjoint `a`--`b` paths, and the
   interior of each path meets `V(T)`.

The same trichotomy holds after interchanging `ab` and `cd` and deleting
the other six branch vertices.

#### Proof

Seven-connectivity makes `H_ab` connected.  If it contains an `a`--`b`
path whose internal vertices avoid `V(T)`, Theorem 2.1, or equivalently the
clean-path construction recorded in the preceding atomic-frame result,
gives outcome 1.

Otherwise apply the vertex form of Menger's theorem to `a,b` in `H_ab`.
Either a single vertex `v` separates them, or there are two internally
disjoint `a`--`b` paths.  In the first case
\(Z_{ab}\cup\{v\}\) is a seven-vertex cut in `G`, giving outcome 2.  In the
second case neither path can be clean, so both meet `V(T)` internally,
giving outcome 3.  The `cd` statement is symmetric.  \(\square\)

If `G` is strongly seven-contraction-critical, outcome 2 has the exact
proper-minor responses required by the bounded-interface programme.  Every
component of the complement of the seven-set is adjacent to every boundary
vertex; otherwise its neighbourhood would be a cut of order at most six.
For a nonempty independent boundary set `I`, contract one full component
together with `I`, six-colour the proper minor, expand `I`, and restrict to
the opposite closed shore.  Contracting the opposite component gives the
reverse response.  In both colourings, `I` is one exact boundary colour
class because the contracted full component is adjacent to every boundary
vertex outside `I`.

### Corollary 5.2

If `T` has at most one internal vertex, then a seven-connected host
containing `T` has a `K_7` minor or the exact order-seven separator in
Theorem 5.1.

#### Proof

In outcome 3 the two paths meet distinct internal vertices of `T`, which is
impossible under the hypothesis.  \(\square\)

This closes every seven-connected augmentation of the smallest incompatible
two-bridge example recorded in the adjacent barrier note: its underlying
`H_0` subdivision has only the one internal vertex on `T_ef`.

## 6. Breaking a saturated subcritical separator

The next lemma is useful beyond the atomic frame.

### Lemma 6.1 (critical component-joining path)

Let `H` be a subgraph of a `k`-connected graph `G`, let
\(S\subseteq V(H)\) have order less than `k`, and suppose that whenever `u,v`
belong to distinct components of `H-S`, the graph `H+uv` has a `K_7`
minor.  If `H-S` is disconnected, then `G` has a `K_7` minor.

#### Proof

The graph `G-S` is connected.  Take a path in `G-S` meeting two components
of `H-S`, and then take a subpath `P` between consecutive visits to
distinct components.  Its ends `u,v` lie in distinct components of `H-S`
and its internal vertices avoid `V(H)`.  Contracting `P` to the edge `uv`
while retaining `H` shows that `H+uv` is a minor of `G`.  The hypothesis
now gives a `K_7` minor in `G`.  \(\square\)

### Corollary 6.2 (the multipartite saturation cannot persist)

Every seven-connected graph containing `K_{3,2,2,2}` as a subgraph has a
`K_7` minor.

#### Proof

Let `U` be the part of order three and put
`S=V(K_{3,2,2,2})-U`, so `|S|=6`.  The three vertices of `U` are the
components after deleting `S`.  Adding an edge within `U` creates a
`K_7` minor.  Explicitly, for

\[
 U=\{u,v,w\},\quad A=\{a,a'\},\quad
 B=\{b,b'\},\quad C=\{c,c'\},
\]

and added edge `uv`, use

\[
 \{u\},\ \{v\},\ \{w,a\},\ \{a'\},\
 \{b,c\},\ \{b'\},\ \{c'\}.                           \tag{6.1}
\]

These seven connected sets are pairwise adjacent.  Lemma 6.1 with `k=7`
therefore applies.  \(\square\)

The graph `K_{3,2,2,2}` is the natural six-connected saturation of the
small triangle-ear obstruction.  Corollary 6.2 is unbounded: the ambient
seven-connected graph may have arbitrarily many additional vertices.

## 7. Exact remaining implication

One bridge path is now completely understood, the one-internal-vertex
residue returns an exact response-bearing separator, and the maximal
six-connected multipartite saturation cannot survive in a seven-connected
host.  In the remaining `K_7`-minor-free case:

- every nontrivial `T`-bridge has at least seven attachments in one of the
  four regions (3.1);
- both missing-pair deletion residues which avoid an exact separator have
  two internally disjoint paths meeting distinct internal segment vertices;
  and
- different individually two-apex bridges need not share a planarizing
  pair.

The missing theorem must use interactions among these high-attachment
bridges to create an `ab`, `cd`, or ownership-preserving `xe` augmentation,
or identify a smaller full component with its proper-minor response.  A
common planarizing pair cannot be inferred by intersecting the certificates
of individual bridge paths.
