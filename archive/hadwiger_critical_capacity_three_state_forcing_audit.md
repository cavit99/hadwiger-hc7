# Independent audit: critical capacity-three state forcing

## Verdict

**GREEN AS PATCHED.**  The four-set SDR consequence, the rooted `K_4`
model, the conditional state-forcing `K_7` completion, the atomic
three-pair linkage theorem, and the Mycielski warning are correct.

The source was patched in one place: four is the threshold at which the
**antichain property alone** guarantees an SDR.  The five-set example is
an abstract antichain without an SDR; it did not prove realization of
that family as outside neighbourhoods in a vertex-critical graph.  The
patched note no longer makes that stronger claim.

## 1. Critical SDR

If locally parallel nonadjacent vertices have common neighbourhood `U_0`
inside the selected module and outside profiles `A_i`, then
`A_i subseteq A_j` would give

\[
               N(x_i)=U_0 union A_i subseteq U_0 union A_j=N(x_j),
\]

contrary to critical anti-domination.  For at least two vertices the
outside sets are therefore nonempty and pairwise incomparable.

For any subfamily of at most four such sets, Hall's inequality follows
from the elementary maximum-antichain sizes on ground sets of order
zero, one, two and three.  In particular, three incomparable sets cannot
have union of order two, and four cannot have union of order three.
Hence four locally parallel vertices have distinct outside
representatives.  Five two-subsets of a four-set correctly show only
that this inference stops at five.

## 2. Rooted and labelled branch sets

In Lemma 2.1, every `L_i union R_i` is connected because the full
`K_{3,3}` contact includes `L_iR_i`.  Two different such bags are
adjacent through `L_iR_j`, and `Z` sees each through `L_i`.  The four
displayed bags are therefore a literal rooted `K_4` model.

Theorem 3.1 is a correct conditional lift.  Enlarging `B_i` by the
disjoint connected column `C_i` preserves all old clique-model
adjacencies, supplies connectivity through `B_iC_i`, and supplies the
three missing neutral contacts by hypothesis.  Together with the
`Q`-full bag `B_0` and the three singleton vertices of the triangle,
the displayed seven bags form a `K_7` model.  The theorem correctly does
not infer the state-forcing columns from unlabelled private neighbours.

## 3. Atomic three-pair theorem

Contract the three disjoint two-vertex connected sets to protected
sources.  If a three-linkage to `T` fails, set-Menger gives a separator
of order at most two in the contracted graph.

* With no contracted source in the separator, its inverse image has
  order at most two.
* With exactly one contracted source, replacing it by its two-vertex
  preimage gives a cut of order at most three.

Both contradict four-connectivity.  The only remaining certificate is
the two contracted sources themselves.  Their inverse image is the
four-vertex union of two protected pairs and separates the third pair
from `T`.  Four-connectivity makes this an exact order-four cut: no
proper subset can separate.  Adding the deleted neutral triangle gives
the claimed exact order-seven adhesion in the ambient graph.

This proof relies essentially on the protected carriers having order
two.  For larger carriers a contracted source can be a capacity-one
warehouse whose inverse image is larger than three, exactly as stated.

## 4. Mycielski warning

The Mycielskian of `K_3` is four-vertex-critical.  Its three clone
vertices have common internal neighbour `w` and outside profiles

\[
          {v_1,v_2},\quad {v_0,v_2},\quad {v_0,v_1}.
\]

These profiles form the asserted antichain and admit an SDR.  The four
sets

\[
 {w},\quad {u_0,v_1},\quad {u_1,v_2},\quad {u_2,v_0}
\]

are connected and pairwise adjacent, so the unlabelled rooted model is
valid.  A row concentrated at `w` remains confined to the first bag;
the model does not become state-forcing.  Thus the example genuinely
refutes a vertex-critical-only labelled completion, while leaving an
operation-sensitive contraction-critical theorem possible.

