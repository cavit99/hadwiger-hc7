# A one-missing-adjacency model yields a universally multicoloured separator

**Status:** written proof; separate internal audit GREEN.  This is a conditional
theorem for a spanning labelled `K_7`-minus-one-edge model.  It does not
prove `HC_7`.

## Theorem

Let `G` be seven-connected and not six-colourable, and suppose every proper
minor of `G` is six-colourable.  Suppose that `V(G)` is partitioned into
seven nonempty connected branch sets

\[
                    \{a\},D,U_1,U_2,U_3,U_4,U_5,
\]

which form a labelled `K_7`-minus-one-edge model whose unique missing
adjacency is `aD`.

Then either `G` contains a `K_7` minor, or there is a partition

\[
                    V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R
\]

with the following properties.

1. `L` is nonempty and connected, `T=N_G(L)`, `R` is nonempty, and there is
   no edge from `L` to `R`.
2. The vertex `a` belongs to `T`.
3. The graph `G[R\cup T]-a` contains five pairwise vertex-disjoint
   connected subgraphs `Q_0,Q_1,Q_2,Q_3,Q_4` which are pairwise adjacent,
   each is adjacent to `a`, and

   \[
                 T\subseteq\{a\}\cup\bigcup_{i=0}^4V(Q_i).
   \]

4. At least one of the five subgraphs is disjoint from `T`.
5. In every proper six-colouring of `G[R\cup T]`, at least one nonempty
   intersection `T\cap V(Q_i)` contains vertices of two different colours.

Thus the full-neighbourhood separation returned by the two-mark branch-set
split automatically has all the geometric hypotheses of the five-row
reflection theorem.  Failure of reflection is exactly the universal
multicolouring assertion in item 5.

## Proof

Seven-connectivity gives `d_G(a)>=7`.  Since the model is spanning and
`a` is anticomplete to `D`, all neighbours of `a` lie in the five branch
sets `U_1,...,U_5`.  Some one of them, say `U`, therefore contains two
distinct neighbours of `a`.

Apply the construction in the two-mark branch-set split theorem to `U`.
It gives a partition

\[
                         U=Z\mathbin{\dot\cup}W
\]

into nonempty connected adjacent sets, both adjacent to `a`.  Rename the
other four common branch sets as `V_1,...,V_4`.  If `Z` is adjacent to `D`
and `W` is adjacent to every `V_i`, the seven sets

\[
                    \{a\},\quad D\cup Z,\quad W,
                    \quad V_1,V_2,V_3,V_4
\]

form an explicit `K_7`-minor model.  It remains to treat the two separator
outcomes of that construction.

### Case 1: `Z` is anticomplete to `D`

Put

\[
                       L=Z,\qquad T=N_G(Z),
                       \qquad R=V(G)-(L\cup T).
\]

The set `R` is nonempty because it contains `D`.  Since `U` is adjacent to
`D` while `Z` is anticomplete to `D`, the sets `W` and `D` are adjacent.
Define

\[
                  Q_0=D\cup W,qquad Q_i=V_i\quad(1\le i\le4).
\]

These five sets are disjoint and connected.  They are pairwise adjacent:
`D` supplies every adjacency from `Q_0` to a set `V_i`, and the four
sets `V_i` were already pairwise adjacent.  The vertex `a` is adjacent to
`Q_0` through `W` and to every `V_i`.

Spanningness and `Z\perp D` give

\[
                    T\subseteq\{a\}\cup W\cup
                    V_1\cup V_2\cup V_3\cup V_4,
\]

so the five displayed connected subgraphs cover `T-{a}`.  If `Z` were
adjacent to every `V_i`, then

\[
                  \{a\},\quad D\cup W,\quad Z,
                  \quad V_1,V_2,V_3,V_4
\]

would form a `K_7`-minor model: the edge between `Z` and `W` supplies the
adjacency from `Z` to `D\cup W`.  Hence, in the non-`K_7` outcome, some
`V_j` is anticomplete to `Z`.  For that index,

\[
                            T\cap V(Q_j)=\varnothing.
\]

### Case 2: `Z` is adjacent to `D` and `W` is anticomplete to some `V_j`

Put

\[
                       L=W,\qquad T=N_G(W),
                       \qquad R=V(G)-(L\cup T),
\]

and define

\[
                  Q_0=D\cup Z,qquad Q_i=V_i\quad(1\le i\le4).
\]

Now `R` is nonempty because it contains `V_j`.  The set `Q_0` is connected
through an edge between `D` and `Z`.  As in Case 1, `D` supplies every
adjacency from `Q_0` to the four other connected subgraphs; those four are
pairwise adjacent; and `a` is adjacent to `Q_0` through `Z` and to every
`V_i`.  Spanningness gives

\[
                    T\subseteq\{a\}\cup D\cup Z\cup
                    V_1\cup V_2\cup V_3\cup V_4.
\]

Thus the five connected subgraphs again cover `T-{a}`.  The assumed
anticompleteness of `W` and `V_j` gives

\[
                            T\cap V(Q_j)=\varnothing.
\]

This proves items 1--4 in both separator orientations.  Notice in
particular that simultaneous losses on the two sides of the split cause no
new geometric case: merging `D` with the opposite side of `U` restores the
five pairwise adjacent connected subgraphs required for reflection.

It remains to prove item 5.  The closed far shore `G[R\cup T]=G-L` is a
proper minor of `G`, so it has a proper six-colouring.  Suppose that some
such colouring makes every nonempty set `T\cap V(Q_i)` monochromatic.
Items 2--4 then verify the hypotheses of the five-row reflection theorem;
the boundary-free subgraph `Q_j` supplies its second alternative.  That
theorem reflects the same boundary equality partition through
`G[L\cup T]` and glues the two colourings, producing a proper
six-colouring of `G`.  This contradicts the hypothesis on `G`.

Therefore every proper six-colouring of the far closed shore multicolours
at least one nonempty intersection `T\cap V(Q_i)`, proving item 5.  \(\square\)

## Consequence for the degree-seven one-spoke case

The audited aligned degree-seven theorem gives a labelled
`K_7`-minus-one-edge model whenever the relevant vertex of the boundary
complement has degree two.  The spanning enhancement preserves its
singleton centre and its named boundary roots.  The present theorem then
reduces that entire one-spoke branch to the separator in the theorem.

Accordingly, donor splitting, simultaneous losses, and an unrestricted
centre-to-deficient-bag path are no longer separate open problems.  The
remaining implication is the following label-preserving colouring step:

> In the separator supplied above, use a proper-minor response on the
> `L` side to obtain either a far-shore six-colouring which is monochromatic
> on every named boundary intersection, an explicit `K_7`-minor model, or
> a strict host-level reduction preserving the five named connected
> subgraphs.

The exact degree-seven matching response gives monochromatic operation
endpoints and five bichromatic connections, but it does not currently
identify their first contacts with the five named connected subgraphs.

## Trust boundary

- The theorem does not bound `|T|` above by seven.  Seven-connectivity only
  gives `|T|>=7`; equality makes the separation full to every component.
- The multicoloured subgraph may depend on the selected far-shore
  colouring.  No fixed `Q_i` is asserted to be multicoloured in all
  colourings.
- A multicoloured boundary intersection need not admit a
  label-preserving split of its connected subgraph.
- The exact matching response on the original degree-seven boundary does
  not by itself name the five subgraphs `Q_i`.  Turning palette colours
  into these branch-set labels remains the open first-hit problem.
- The graph `K_2` joined with the icosahedral graph gives a
  seven-connected, `K_7`-minor-free static example with the same merged-row
  geometry and a necessarily multicoloured boundary intersection.  It is
  six-colourable and does not have the required contraction-critical
  response, so it is a sharpness example rather than a counterexample to
  the theorem.

## Dependencies

- [two-mark branch-set split](../results/hc7_two_mark_branch_set_split.md)
- [five-row reflection across a separation](../results/hc7_five_row_separator_reflection.md)
- [spanning degree-seven bridge corollaries](../results/hc7_degree7_one_spoke_bridge_corollaries.md)
- [exact degree-seven matching response](../results/hc7_degree7_matching_bridge_bundle.md)
- [boundary-labelled degree-seven near-`K_7` model](../results/hc7_degree7_aligned_near_k7_model.md)
