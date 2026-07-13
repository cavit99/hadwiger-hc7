# Audit of reserved-path/rooted-model surgery: the one-bag normal form is insufficient

## 1. The proposed splitter axiom

The five-connected route naturally suggests the following implication.

> Let (H) be five-connected and nonplanar, let
> (X=\{x_1,x_2,x_3,x_4\}), and let (T) be an induced path disjoint
> from (X).  If (H-T) has no (X)-rooted (K_4), choose an
> (X)-rooted (K_4)-model in (H) minimizing its intersection with
> (T).  Once that intersection lies in one interval and one branch
> bag, it can be removed or rerouted, freeing (T).

The last sentence is false, even after adding the exact four-colour
saturation forced along a planar blocker.  The obstruction is a unique
**model-adjacency portal**: the sole path vertex in the model may be the
only edge from its rooted bag to another rooted bag.

## 2. A five-connected counterarchitecture

Let (L) be the square antiprism.  Its top square is

\[
                         x_1x_2x_3x_4x_1,
\]

and its bottom square is (y_1y_2y_3y_4y_1).  In addition to the two
square cycles, join

\[
                         x_i y_i,qquad x_i y_{i-1}
\]

with indices modulo four.  This is a four-connected plane graph and the
four roots are incident with its top face.  Hence (L) has no
(X)-rooted (K_4)-model.

Add the induced even path

\[
                         T=a t p                             \tag{2.1}
\]

and give its vertices the following neighbourhoods in (L):

\[
\begin{aligned}
 N_L(a)&=\{x_1,x_2,y_1,y_2,y_3,y_4\},\\
 N_L(p)&=\{x_3,x_4,y_1,y_2,y_3,y_4\},\\
 N_L(t)&=\{x_1,x_2,x_3,y_1,y_2\}.                \tag{2.2}
\end{aligned}
\]

Call the resulting eleven-vertex graph (H^star).

### Lemma 2.1 (audited properties)

The graph (H^star) has all of the following properties.

1. (H^star) is five-connected and nonplanar.
2. (T) is an induced even path, and its ends have the required typed
   root contacts:

   \[
                         a\sim\{x_1,x_2\},\qquad
                         p\sim\{x_3,x_4\}.
   \]

3. For every proper four-colouring of (L), all four colours occur on
   each of (N_L(a),N_L(t),N_L(p)).
4. (L=H^star-T) has no (X)-rooted (K_4)-model.
5. Among all (X)-rooted (K_4)-models in (H^star), the minimum
   number of (T)-meeting bags is one and the minimum number of used
   path vertices is one.

#### Certificate

The dependency-free verifier
`reserved_path_model_normalization_probe.py` checks vertex-connectivity
by deleting every set of at most four vertices, enumerates all 168
proper four-colourings of (L), and exhausts every rooted branch-set
model.  It prints

```text
five_connected=True edges=35 nonplanar_by_euler=True
four_colourings=168 all_path_rows_saturating=True
rooted_K4_after_deleting_path=False
minimum_path_intersection=(1, 1)
model=('x1',) | ('x2',) | ('x3', 'y1', 'y2') | ('x4', 'y3', 'a')
```

Nonplanarity also follows immediately from

\[
                         |E(H^star)|=35>3\cdot11-6.
\]

The displayed four bags give a readable rooted model.  They meet (T)
in the singleton interval \(\{a\}\), contained in exactly one bag.
Deleting (a) from that bag destroys its adjacency to the bag
\(\{x_2\}\): neither (x_4) nor (y_3) is adjacent to (x_2), while
(ax_2\) is an edge.  Thus (a) is an irreplaceable model-adjacency
portal.  No alternative model avoids (T), by item 4.  \(\square\)

## 3. Verdict on interval normalization

The counterarchitecture does not disprove the purely formal assertion
that some minimum model can be normalized to interval intersections and
one path bag.  It proves something sharper for the intended argument:
even the strongest possible such normalization—one vertex, one interval,
one bag—does **not** imply that the path can be freed.

Consequently, a path/model surgery proof needs an extra splitter axiom.
One sufficient form would be:

> **Portal-redundant one-bag splitter.**  If a minimum rooted model meets
> (T) in one bag (B), then every adjacency from (B) to the other
> three bags has a witness in the root component of (B-T), or has a
> detour through (H-T) which avoids the other bags.

Five-connectivity, nonplanarity, an induced even path, typed endpoint
contacts, and four-saturation of every path neighbourhood do not imply
this axiom: (H^star) satisfies all five conditions.

## 4. Corrected route

The failure identifies exactly why the second-detour theorem in
`hadwiger_double_moser_reserved_connector_linkage.md` is indispensable.
One cannot free (T) by looking at a single minimum rooted model.  One
must use an independent path (Q) to replace an essential model
adjacency, or turn the failure into the loaded two-path three-adhesion
already proved there.

Thus the correct structural target is not an unqualified interval
normalization.  It is:

> **Portal exchange with a second shore.**  At every path vertex which
> is the unique witness for a rooted-model adjacency, the second detour
> (Q), a Kempe carrier, or a one-step minor-transition state supplies
> an avoiding replacement; otherwise the essential portal and the
> three-adhesion form an exact seven-cut.

This is strictly stronger than bridge stability for one path and is the
precise missing splitter axiom exposed by the counterarchitecture.

