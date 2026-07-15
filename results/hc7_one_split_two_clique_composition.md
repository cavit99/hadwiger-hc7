# One split model and two literal cliques

**Status:** proved and independently audited.

This is the first global composition rung obtained by combining the
support-at-most-six programme with the published three-clique theorem.  It
returns a trichotomy: a `K_7` minor, one common two-vertex transversal of
every small `K_5` model, or a canonical exact-seven separation carrying all
three named models.  The first two outcomes are terminal; the last is an
unranked model-preserving handoff.

## 1. Statement

Let `M` be a `K_5` model supported on six vertices.  Write its unique
two-vertex bag as the edge `e=xy` and its four singleton bags as the
literal clique `Q`.  Let `C_2,C_3` be two literal `K_5` cliques.  Contract
`e`, denote its image by `z`, and write `C_i^e` for the image of `C_i`.

### Theorem 1.1 (one-split composition trichotomy)

Let `G` be seven-connected.  Suppose that

1. neither `C_2` nor `C_3` contains both ends of `e`; and
2. the three literal cliques in `G/e` satisfy

   \[
   |(Q\cup\{z\})\cap C_i^e|\le3\quad(i=2,3),
   \qquad |C_2^e\cap C_3^e|\le3.                    \tag{1.1}
   \]

Then at least one of the following holds.

1. `G` contains a `K_7` minor.
2. Some two vertices of `G` meet every `K_5` model in `G` supported on at
   most six vertices.
3. There is an exact separation `(A,B)` of `G` of order seven such that
   `x,y in A cap B`, both open shores are nonempty, and each of

   \[
                         Q\cup\{x,y\},\qquad C_2,\qquad C_3
   \]

   is contained in one of the two closed shores.

The third outcome is canonical: it is the lift of a minimum separator of
`G/e`.  Thus it preserves the three named model carriers and puts the
entire split edge into the adhesion.

## 2. Proof

Contract `e` and call the resulting graph `H`.  The set

\[
                              L=Q\cup\{z\}
\]

is a literal `K_5` in `H`.  Each `C_i` has at most one end of `e`, so its
image `C_i^e` is again a literal `K_5`.  Moreover, by (1.1),

\[
 |L\cap C_i^e|\le3,
 \qquad |C_2^e\cap C_3^e|\le3.                    \tag{2.1}
\]

An edge contraction of a seven-connected graph is six-connected.  We
split according to whether `H` is seven-connected.

Suppose first that `H` is seven-connected.  If `H` is two-apex, choose a
two-set `R` such that `H-R` is planar.  The two-apex contraction-pullback
theorem in
[`hc7_five_connected_planar_support_five_exclusion.md`](hc7_five_connected_planar_support_five_exclusion.md)
returns a literal two-set in `G` meeting every support-at-most-six `K_5`
model.  This is outcome 2.

If `H` is not two-apex, apply Theorem 1.10 of Niu--Zhang, *Cliques, minors
and apex graphs*, Discrete Mathematics 309 (2009), 4095--4107.  By (2.1),
the seven-connected non-two-apex graph `H` contains a `K_7` minor.  Expanding
the contraction of `e` gives outcome 1 in `G`.

It remains that `H` is not seven-connected.  Since it is six-connected,
if `|V(H)|=7`, then `H` is a literal `K_7` and outcome 1 holds.  We may
therefore assume `|V(H)|>=8`.  Now `H` has a separator `T` of order six
with at least two nonempty components.  Necessarily `z in T`: otherwise
`T` itself would separate `G`, contrary to seven-connectivity.  Replace
`z` in `T` by `x,y` and put

\[
                       T^+=(T-\{z\})\cup\{x,y\}.       \tag{2.2}
\]

Then `|T^+|=7`, and distinct components of `H-T` lift to distinct
components of `G-T^+`.  Hence `T^+` is the boundary of an actual
exact-seven separation of `G` with both open shores nonempty.

Every clique of `H` lies in `T` together with at most one component of
`H-T`, since vertices in distinct components are nonadjacent.  Apply this
to `L,C_2^e,C_3^e`.  On expanding `z`, the clique `L` becomes the named
model support `Q union {x,y}`, while each `C_i^e` pulls back to the original
literal clique `C_i` (using at most one of `x,y`).
Consequently each of the three named carriers lies in a closed shore of
the lifted separation, and outcome 3 holds.  \(\square\)

## 3. Consequence for the support-six target

Let `S_{<=6}(G)` be the family of supports of all `K_5` models on at most
six vertices.  In a seven-connected `K_7`-minor-free graph with
`tau(S_{<=6}(G))>2`, Theorem 1.1 says that every triple satisfying its
row-compatibility hypotheses produces the exact-seven handoff in outcome
3.  The `K_7` and common-transversal outcomes contradict the assumptions.

There is also no obstruction consisting of three literal `K_5` cliques:
the separated-triple theorem makes their pairwise intersections at most
three; the graph cannot be two-apex (an apex pair would meet every `K_5`
model); and Niu--Zhang therefore gives a `K_7` minor directly.  Hence a
hypothetical counterexample to the support-six target must use at least
one genuine split model in every separated triple.

## 4. Trust boundary

The theorem does not assert that the split edge can always be selected
row-compatible with the other two supports.  Notice that literal privacy
is not required: one end of `e` may belong to either `C_i`, provided the
three quotient cliques still satisfy (1.1).  The affine pair-cover construction
in
[`../barriers/hc7_support_six_affine_alignment_barrier.md`](../barriers/hc7_support_six_affine_alignment_barrier.md)
shows that such literal privacy is false as a set-system conclusion.

The result also does not close outcome 3 by itself.  Its contribution is
that no unlabelled portal data are lost there: the split edge is in the
seven-adhesion and every selected model is assigned to a closed shore.
The remaining global extraction theorem must return either this
row-compatible configuration or a structured pair-cover design whose
genuine graph realization forces `K_7`.
