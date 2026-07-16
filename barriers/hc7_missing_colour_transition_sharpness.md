# Sharp limits of the missing-colour transition

**Status:** explicit constructions; independently replayable by the
displayed colourings.

The exact transition theorem in
`../results/hc7_missing_colour_matching_transition.md` cannot be sharpened
to a singleton-output theorem or equipped with a rank depending only on
the matching signature.  Both failures persist under high connectivity
and three pairwise disjoint labelled split supports.  The examples below
contain `K_7` minors and are not hypothetical `HC_7` counterexamples.

## 1. One singleton state can branch to both other rows

Let `P=K_{3,3,3,3}`.  Let `H` consist of the edge `xy` and the two
internally disjoint length-four `x-y` paths

\[
 x-u_2-v_2-w_2-y,
 \qquad
 x-u_3-v_3-w_3-y.
\]

Put

\[
 G=P\vee H,qquad
 e_1=xy,quad e_2=u_2v_2,quad e_3=u_3v_3,qquad
 F=\{e_1,e_2,e_3\}.
\]

The join has chromatic number `4+3=7`.  Choose three disjoint transversal
four-cliques `Q_1,Q_2,Q_3` in the four parts of `P`.  Then
`Q_i union V(e_i)` are pairwise disjoint support-six `K_5` models.

On `K=G-F`, colour the four parts of `P` with four private colours and
colour

\[
 x,y,v_2,v_3\text{ with }\alpha,qquad
 u_2,u_3,w_2,w_3\text{ with }\gamma.
\]

This is a proper six-colouring of `K` with exact signature `{e_1}`.  The
`alpha,gamma` component of `x` in `K` is

\[
                         C=\{x,u_2,u_3\}.
\]

Swapping it makes `e_1` proper and makes both `e_2,e_3` equal.  Thus the
exact transition is

\[
                         \{e_1\}\longrightarrow\{e_2,e_3\}.
\]

In particular, neither high connectivity nor disjoint support labels
forces a singleton output.  The missing additional hypotheses are
`K_7`-freeness and the full contraction-critical composition data.

## 2. Singleton transitions can form a directed cycle

Again let `P=K_{3,3,3,3}`, but now put

\[
 G=P\vee C_7,qquad
 F=\{01,23,45\}
\]

for the cyclic order `0,1,...,6,0`.  The graph `C_7-F` has components
`1-2`, `3-4`, and `5-6-0`.  Give them the two-colour patterns

\[
 (a,1-a),\qquad (b,1-b),\qquad(c,1-c,c).
\]

The three deleted rows are equal exactly under the conditions

\[
                         c=a,qquad b=1-a,qquad c=1-b.
\]

As `(a,b,c)` varies, the only signatures are the three singletons and the
all-equal state.  Swapping the component containing the first endpoint of
the unique equal row gives, after a cyclic relabelling,

\[
          \{e_1\}\longrightarrow\{e_3\}
          \longrightarrow\{e_2\}\longrightarrow\{e_1\}.
\]

The three disjoint transversal four-cliques of `P` again give disjoint
labelled supports, and the join is highly connected and seven-chromatic.
This example does **not** realize the three doubleton signatures, so it
does not refute an argument using the full punctured cube.  It does prove
that the local missing-colour move, viewed only through its current and
next signatures, has no well-founded rank.

## Consequence for the active proof

The productive data are the literal two-colour component, the named
four-clique it avoids, the full family of exact contraction states, and
the weighted separator rank.  Iterating the seven abstract signature
labels alone is a terminated route.
