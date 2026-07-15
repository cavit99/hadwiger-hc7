# A parity barrier for four-colour boundary state transfer

**Status:** exact abstract extension-language barrier.  It is verified by
`hc7_four_colour_parity_language_barrier_verify.py`.

This example shows that four-colourability of the boundary, the join-minor
exclusion supplied by two full shores, and the exact-private-block response
for every independent boundary set do not force a common six-colour state.
It is not an actual contraction-critical host and is not a counterexample to
`HC_7`.

## 1. Boundary

Let

\[
 X=\{x_0,x_1,x_2,x_3\},\qquad
 Y=\{y_0,y_1,y_2,y_3\},
\]

and let the boundary graph be

\[
                              J=K_4[X]\mathbin{\dot\cup}K_4[Y]. \tag{1.1}
\]

Thus `chi(J)=4`.  Every independent set has order at most two and is
either a singleton or a cross-pair `{x_i,y_j}`.

The static two-shore quotient is also target-free:

\[
                              I_2\vee J\not\succcurlyeq K_7.    \tag{1.2}
\]

Indeed, it has a two-bag tree decomposition with bags `I_2 union X` and
`I_2 union Y`, each of order six.  Hence its treewidth is at most five.

## 2. Two disjoint exact-trace languages

For a matching `M` in the complete bipartite graph between `X` and `Y`,
let `Pi_M` be the boundary partition whose non-singleton blocks are the
two-sets in `M` and whose unmatched vertices are singleton blocks.  It is
a proper equality partition of `J`.

Use matchings of size three and four.  A perfect matching is a permutation
`sigma in S_4`; call its state even or odd according to the sign of
`sigma`.  A three-edge matching omits one `x_i` and one `y_j`; complete it
by `x_i y_j` and use the sign of the resulting perfect matching.

Let `E_+` be all even states and `E_-` all odd states.  They are disjoint,
and every state has four or five blocks, hence is a legal six-colour
boundary state.

Nevertheless each language separately has the full-shore exact-trace
property:

* Fix a cross-pair `{x_i,y_j}`.  The six perfect matchings containing it
  split equally into three even and three odd states, so that pair occurs
  as one exact block in both languages.
* Fix a singleton `x_i`.  Choose any omitted `y_j`.  The six size-three
  matchings omitting `x_i,y_j` again split equally by the parity of their
  completion, so `{x_i}` is an exact block in both languages.  The same
  argument applies to every `y_j`.

These are all nonempty independent subsets of `J`.  Thus both abstract
closed shores answer every legal star-contraction query, but

\[
                              E_+\cap E_-=\varnothing.          \tag{2.1}
\]

No palette permutation repairs (2.1), because states are equality
partitions rather than named colour functions.

## 3. Consequence

The exact-private-block theorem is a collection of existential responses,
one response for each independent set.  It does not couple those responses
across different contractions.  The parity languages demonstrate the
missing coupling exactly.

Dvořák--Swart's realization theorem confirms the general severity of this
barrier: arbitrary permutation-closed extension languages can be realized
by graphs while excluding an `X`-rooted `K_{k+1}` and an unrooted
`K_{k+2}` minor.  That theorem does not supply the seven-connectivity,
literal two-full-shore structure, or contraction-critical transitions of
the active `HC_7` setting, so it is used here only as a guardrail.

Accordingly, a valid four-colour two-shore theorem must use a transition
that couples two proper-minor responses (such as the leaf-rooted chromatic
drop), or ambient labelled routing.  Boundary four-colourability plus
independent-block probes alone cannot prove state transfer.
