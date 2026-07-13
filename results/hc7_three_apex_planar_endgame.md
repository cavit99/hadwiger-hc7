# The three-apex planar endgame closes by palette recycling

## Status

The uniform lifting lemma below is the constructive rooted-model principle
behind a complete closure of every planar remainder returned after deleting
at most three vertices.  It does not use
seven-connectivity, contraction-criticality, a selected near-`K_7` model,
or any portal labels.  Its only non-elementary input is the proved Strong
Hadwiger theorem for four colours (Martinsson--Steiner).

## Lemma 0 (uniform clique-apex lifting from Strong Hadwiger)

Fix positive integers `r,s`, and suppose Strong Hadwiger is true for `r`
colours: every colourful set in an `r`-chromatic graph roots a `K_r`
minor.  Let `G` satisfy `chi(G)>=r+s`, and suppose there is a set `A` of
at most `s` vertices for which `chi(G-A)<=r`.  Then `G` contains a
`K_(r+s)` minor.

### Proof

Pass to a subgraph minimal subject to having chromatic number at least
`r+s`.  It has chromatic number exactly `r+s`: deleting one edge lowers
chromatic number by at most one, while minimality makes every edge
deletion `(r+s-1)`-colourable.  Replace `A` by its intersection with
this subgraph and rename the subgraph `G`.  If `|A|<s`, then `r` colours on `G-A`
and one fresh colour per vertex of `A` use at most `r+s-1` colours, a
contradiction.  Hence `|A|=s`.

Put `H=G-A`.  We must have `chi(H)=r`, since otherwise an `(r-1)`-
colouring of `H` and `s` fresh colours on `A` colour `G` with at most
`r+s-1` colours.  Likewise `G[A]=K_s`: if `G[A]` were not complete,
then `chi(G[A])<=s-1`, and disjoint palettes on `H` and `A` would again
use at most `r+s-1` colours.

Write `A={a_1,...,a_s}` and put

\[
                        X=\bigcap_{a\in A}N_H(a).       \tag{0.1}
\]

We claim that `X` is colourful in `H`.  Otherwise, after permuting an
`r`-colouring of `H`, its independent colour-1 class `Z` misses `X`.
For every `z in Z cap N_H(a_1)`, choose an index
`j(z) in {2,...,s}` for which `z a_(j(z))` is not an edge; such an index
exists because `z` is not in `X`.  Recolour `z` with a fresh colour
`f_(j(z))`.  The recoloured vertices remain proper because `Z` is
independent and no fresh colour was used on `H`.  Finally colour `a_1`
with 1 and each `a_j`, `j>=2`, with its own fresh colour `f_j`.
The clique `A` is proper; every old colour-1 neighbour of `a_1` was
recoloured; and a vertex recoloured `f_j` was chosen nonadjacent to
`a_j`.  This is an `(r+s-1)`-colouring of `G`, a contradiction.

Thus `X` is colourful.  Strong Hadwiger for `r` supplies an `X`-rooted
`K_r` model in `H`.  Every one of its branch sets contains a vertex
adjacent to every member of the clique `A`.  The `r` rooted bags together
with the `s` singleton bags `{a}`, `a in A`, form a literal
`K_(r+s)` model. \(\square\)

## Theorem 1 (three-apex `HC_7` theorem)

Let `G` be a graph with `chi(G)>=7`.  If there is a set `A` of at most
three vertices such that `P=G-A` is planar, then `G` contains a `K_7`
minor.

Equivalently, every `K_7`-minor-free graph which becomes planar after
deleting at most three vertices is six-colourable.

### Proof

The theorem follows immediately from Lemma 0 with `(r,s)=(4,3)`, the
Four Colour Theorem, and the Strong Hadwiger theorem for four colours.
For completeness, here is the specialized recolouring and branch-set
construction.

It is enough to consider `chi(G)=7`, by passing to a subgraph minimal
subject to having chromatic number at least seven.  If `|A|<=2`, the Four Colour Theorem colours `P` with four
colours and two fresh colours suffice for `A`, contrary to `chi(G)=7`.
Thus `|A|=3`; write

\[
                         A=\{a_1,a_2,a_3\}.
\]

If `G[A]` is not a triangle, it is two-colourable.  Four colours on `P`
and two disjoint fresh colours on `A` again give a six-colouring of `G`.
Consequently `A` induces a triangle.

If `P` were three-colourable, three colours on `P` and three disjoint
fresh colours on the triangle `A` would also six-colour `G`.  Hence

\[
                              \chi(P)=4.                 \tag{1}
\]

Put

\[
       T=N_P(a_1)\cap N_P(a_2)\cap N_P(a_3).             \tag{2}
\]

We claim that `T` is **colourful** in `P`: every proper four-colouring of
`P` uses all four colours on `T`.

Suppose not.  After permuting colours, there is a proper colouring

\[
          c:V(P)\longrightarrow\{1,2,3,4\}
\]

such that no vertex of `T` has colour 1.  The colour class

\[
                         Z=c^{-1}(1)
\]

is independent.  Recolour each vertex `z in Z cap N_P(a_1)` by the
following rule:

\[
 c'(z)=
 \begin{cases}
 5,&z\notin N_P(a_2),\\
 6,&z\in N_P(a_2).
 \end{cases}                                             \tag{3}
\]

The second line is safe: such a vertex is adjacent to `a_1` and `a_2`,
but it is not in `T` (colour 1 is absent from `T`), and therefore it is
not adjacent to `a_3`.  Recolouring creates no edge conflict inside `P`:
the recoloured vertices belonged to the independent set `Z`, and colours
5 and 6 were not previously used on `P`.

Now give

\[
             a_1,a_2,a_3\quad\hbox{colours}\quad 1,5,6,
                                                               \tag{4}
\]

respectively.  These colours are distinct on the triangle.  Every old
colour-1 neighbour of `a_1` was recoloured.  A vertex recoloured 5 was
chosen not adjacent to `a_2`, and a vertex recoloured 6 was proved not
adjacent to `a_3`.  Hence (3)--(4), together with the unchanged colouring
of the other vertices of `P`, is a proper six-colouring of `G`.  This
contradicts `chi(G)=7` and proves the claim.

The Strong Hadwiger theorem for four colours states that, if `H` is a
four-chromatic graph and `S` is colourful in `H`, then `H` has an
`S`-rooted `K_4` minor.  Apply it to `(P,T)`.  There are four pairwise
disjoint, connected, pairwise adjacent branch sets

\[
                         B_1,B_2,B_3,B_4
\]

such that `B_i cap T` is nonempty for every `i`.  Choose
`t_i in B_i cap T`.  By (2), `t_i` is adjacent to each of
`a_1,a_2,a_3`.  Therefore

\[
       \{a_1\},\ \{a_2\},\ \{a_3\},\ B_1,B_2,B_3,B_4     \tag{5}
\]

are seven pairwise disjoint connected branch sets, and every two are
adjacent: the first three form a triangle, the last four form a `K_4`
model, and every cross-adjacency is witnessed by one of the edges
`a_jt_i`.  Thus (5) is a literal `K_7` model in `G`.  This proves the
theorem. \(\square\)

## Corollary 2 (guarded cyclic-shore planar outcome)

In a hypothetical `HC_7` counterexample, any structural theorem returning
a set `A` of at most three vertices with `G-A` planar terminates
immediately: Theorem 1 gives a literal `K_7` minor.  No further reduction
from three apex vertices to a prescribed two-apex pair is needed.

In particular, the three-guard planar outcome in
`../results/hc7_guarded_cycle_web_exchange.md` is as terminal as its
two-guard outcome.

## Corollary 3 (the exact rooted principle used)

For a triangle `A={a_1,a_2,a_3}` over a four-colourable graph `P`, failure
of six-colourability forces the triple common-neighbour set

\[
                  N_P(a_1)\cap N_P(a_2)\cap N_P(a_3)
\]

to be colourful in `P`.  When `chi(P)=4`, Strong Hadwiger for four
colours converts exactly this set into four labelled carriers, each
adjacent to all three apex vertices.

This is the palette-to-labelled-carrier bridge: it uses one common root
set rather than trying to synchronize three independently saturated
neighbourhoods.

## Dependency and audit checklist

1. Four Colour Theorem: `chi(P)<=4` for planar `P`.
2. A. Martinsson and R. Steiner, *Strengthening Hadwiger's conjecture for
   4- and 5-chromatic graphs*, JCTB 164 (2024), Theorem 1.3: every
   colourful set in a four-chromatic graph roots a `K_4` minor.
3. The recolouring uses colours 5 and 6 only on an independent old colour
   class, so no hidden edge conflict is possible.
4. Every rooted branch bag contains its own vertex of the *triple*
   common neighbourhood, so all twelve apex-to-bag adjacencies in (5) are
   literal edges; no collective-contact or palette-to-label inference is
   used.
5. Disconnected planar cores cause no issue.  Equation (1) and the Strong
   Hadwiger theorem apply to the whole graph `P`; colourfulness forces the
   rooted model into an appropriate four-chromatic component.
