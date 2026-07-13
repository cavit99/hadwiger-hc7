# Off-face transfer descends every four-connected locked carrier

## Status

This is a label-preserving exchange theorem on the one-missing branch of
the coherent transported `K_7^vee` model.  It combines the audited locked
two-row face theorem with planar degree escape.  A four-connected marked
carrier either has the protected fixed linkage or transfers an off-face
vertex into a common row and becomes a strictly smaller marked carrier.
Iterating terminates at the linkage or at a non-four-connected carrier.

## 1. Coherent one-missing setting

Let

\[
                  A,D,E,U_1,U_2,U_3,U_4
\]

be a spanning labelled near-`K_7` model.  The six foreign bags are
connected, pairwise disjoint and pairwise adjacent.  The deficient bag
`A` is anticomplete to the fixed missed twin `D`, is adjacent to `E`, and
contains the normalized path core `P`.  The path endpoints give literal
`A-U_i` edges for all four neutral rows, independently of every added
piece.

Assume `A` is the union of `P` and pairwise disjoint connected pieces,
each attached to `P`, with no edges between distinct pieces.

Fix a path cut `P=L dotunion R`.  Let `K` be one connected crossing piece
and let `H,Q` be two distinct retained rows from
`{E,U_1,U_2,U_3,U_4}`.  Put

\[
 A_L=N_K(L),\quad A_R=N_K(R),\quad
 P_H=N_K(H),\quad P_Q=N_K(Q).                              \tag{1.1}
\]

Assume these four families have an SDR.  Include in the certificate any
already selected helper pieces for the other row duties, all disjoint from
`K`.

## Lemma 1 (one off-face vertex transfers safely)

Suppose `K` has a plane embedding with facial cycle `F` containing

\[
                  A_L\cup A_R\cup P_H\cup P_Q,             \tag{1.2}
\]

and let `w in K-F`.  Assume `K-w` is connected and `w` has a neighbour
outside `K`.  Then `w` can be transferred from `A` into one of the three
common foreign rows

\[
             \mathcal R=\{E,U_1,U_2,U_3,U_4\}-\{H,Q\},     \tag{1.3}
\]

producing a spanning labelled near-`K_7` model with the same path core,
the same fixed missed twin and helpers, and the smaller marked carrier
`K-w`.

### Proof

Distinct old exterior pieces are anticomplete, so every neighbour of `w`
outside `K` lies in `P` or a foreign bag.  It does not lie in `P`: every
path vertex belongs to exactly one of `L,R`, and such an edge would put
`w` in `A_L union A_R`, contrary to (1.2).  It does not lie in `H` or
`Q` for the same reason, and it does not lie in `D` because `AD` is the
fixed missing pair.  Hence `w` has a neighbour in a row of `mathcal R`.

Choose the target row `T` as follows.  If `E in mathcal R` and `w` has a
neighbour in `E`, put `T=E`; otherwise choose any row of `mathcal R` met
by `w`.  Replace

\[
                         A\longmapsto A'=A-\{w\},
             \qquad     T\longmapsto T'=T\cup\{w\}.       \tag{1.4}
\]

The bag `T'` is connected through a literal `w-T` edge.  The graph
`K-w` is connected and retains all four portal families in (1.1), hence
it still attaches to `P`; consequently `A'` is connected.  Since `K` is
connected and `K-w` is nonempty, an edge from `w` to `K-w` makes `A'`
adjacent to `T'`.

All old adjacencies of `T` to the other foreign bags survive.  The four
`A'-U_i` adjacencies survive at the fixed path endpoints.  If `T=E`, the
edge from `w` to `K-w` restores `A'E`.  If `E in mathcal R` and `T!=E`,
then `w` had no neighbour in `E` by the choice rule.  If `E` is one of
`H,Q`, all its `K`-portals lie on `F`, so again `w` had no neighbour in
`E`.  Thus deleting `w` never removes the old `AE` adjacency.  Finally
`A'D` remains absent because `A' subset A`,
and enlarging `T` does not affect that named pair.

All vertices remain in exactly one bag, so the model is spanning.  The
marked piece `K-w` retains every portal family and the same SDR, remains
crossing, and is disjoint from all fixed helpers.  Its order is `|K|-1`,
as required.
\(\square\)

## Theorem 2 (four-connected linkage-or-descent)

In the setting above, assume `G` has minimum degree at least six and
`G[K]` is four-connected.  Then either

1. `K` contains disjoint paths, one joining `A_L` to `P_H` and the other
   joining `A_R` to `P_Q`; or
2. there is a spanning labelled model with the same certified duties and
   helpers whose marked crossing carrier is `K-w` for some vertex `w`,
   and therefore has order `|K|-1`.

### Proof

If the paths do not exist, the audited locked two-row theorem gives a
plane embedding of `G[K]` with one face `F` containing every portal
vertex which occurs in a full SDR.  Every element of the union of the
four portal families occurs in a full SDR: start with any SDR and, for a
specified unused element of one family, replace only that family's
representative.  Thus (1.2) holds.

The planar carrier degree-escape theorem gives a vertex `w in K-F` with
a neighbour outside `K`.  Four-connectivity makes `K-w` connected.
Lemma 1 gives outcome 2.  \(\square\)

## Corollary 3 (finite descent of a rank-four Hall collision)

Suppose a minimal Hall-deficient row set exposes one carrier `K` with the
two opposed duties `H,Q`, while every other required row has its distinct
matched carrier/helper outside `K`, and suppose the four families (1.1)
have an SDR.  Repeatedly apply Theorem 2 whenever the current marked
carrier is four-connected.  Since its order strictly decreases in the
descent outcome, after finitely many steps either the literal linkage and
shore completion give `K_7`, or the marked carrier is not
four-connected.

## Exact residual

The theorem removes four-connected rural geometry by a strict exchange;
it does **not** eliminate the Hall collision.  The surviving one-missing
collision has one of three precise defects:

1. the two-row carrier is not four-connected;
2. the four portal families have transversal rank at most three; or
3. some other Hall duties cannot be assigned disjoint helpers outside the
   carrier.

These are the next bounded-adhesion/state cases.  A four-connected rural
carrier is never terminal, but its non-four-connected descendant remains
to be closed.
