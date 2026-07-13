# A unique interface edge forces a tight cut or a portal-ear fan

## 1. Setting

Let `G` be a `k`-connected graph and let `S` be a set of order `k`.
Suppose `G-S` has two anticomplete connected shores `D,D'`, both full
to `S`.  Suppose further that

\[
 D=X\mathbin{\dot\cup}Y,
\]

where `X,Y` are nonempty and connected and

\[
 E_G(X,Y)=\{xy\},\qquad x\in X,\ y\in Y.          \tag{1.1}
\]

Put

\[
 P_X=N_S(X),\qquad P_Y=N_S(Y).                    \tag{1.2}
\]

Thus `P_X union P_Y=S`, but the two rows may overlap.  Contracting each
of `X,Y,D'` to one vertex gives the **actual-row quotient**: the first
two contracted vertices are adjacent and have boundary rows `P_X,P_Y`,
while the third is complete to `S`.

Fix a target order `q` (in the sharp application, `q=7`).

## 2. The label-free geometric trichotomy

### Theorem 2.1 (positive quotient, portal-ear fan, or tight cut)

In the setting above, at least one of the following holds.

1. The actual-row quotient contains a `K_q` minor (and hence
   so does `G`).
2. Both pieces are full to the boundary,

   \[
   P_X=P_Y=S,
   \]

   and `G-xy` contains `k-1` internally vertex-disjoint `x-y` paths.
   At least `k-2` of these paths meet `S` in exactly one vertex.  These
   `k-2` paths are mutually internally disjoint and their boundary
   vertices are distinct.  In particular, each is contained in

   \[
   X\cup Y\cup\{s\}
   \]

   for its unique boundary vertex `s`; they form a portal-preserving
   `x-y` ear fan.
3. One of

   \[
   P_X\cup\{y\},\qquad P_Y\cup\{x\}               \tag{2.1}
   \]

   is an exact `k`-vertex cut nested strictly inside the original
   `D`-side.

The quotient alternative can be tested before the other two; if it is
negative, alternatives 2 and 3 are exhaustive.

#### Proof

The external neighbourhood of `X` is exactly

\[
 N_G(X)=P_X\cup\{y\}.
\]

It separates `X` from the nonempty opposite shore `D'`.  Consequently
`k`-connectivity gives

\[
 |P_X|+1\ge k.                                    \tag{2.2}
\]

Similarly `|P_Y|+1\ge k`.  Since both rows are subsets of the
`k`-element set `S`, each row has order `k-1` or `k`.  A row of order
`k-1` makes the corresponding set in (2.1) an exact `k`-cut.  If no
such cut occurs, both rows equal `S`.

It remains to prove the ear assertion in this last case.  We first use
the standard inequality

\[
 \kappa(G-xy)\ge k-1.                             \tag{2.3}
\]

For completeness, suppose a set `Z` of order at most `k-2` disconnects
`G-xy`.  Since `G-Z` is connected, the deleted edge `xy` is the unique
edge between two components `A,B` of `(G-xy)-Z`, with `x in A` and
`y in B`.  Neither component is a singleton: if, for example,
`A={x}`, then `d_G(x)\le |Z|+1\le k-1`, contrary to the minimum-degree
consequence of `k`-connectivity.  But then `Z union {x}` has order at
most `k-1` and separates `A-{x}` from `B` in `G`, again a contradiction.
This proves (2.3).

Menger's theorem now supplies `k-1` internally disjoint `x-y` paths in
`G-xy`.  Every one meets `S`, because (1.1) is the only edge between
`X` and `Y` and neither shore has a neighbour outside its own vertices
and `S`.  Internal disjointness makes all boundary vertices occurring
on different paths distinct.  There are `k-1` paths and only `k`
vertices in `S`, so at most one path can use more than one boundary
vertex.  Hence at least `k-2` paths meet `S` exactly once.  A simple
`x-y` path with unique boundary vertex `s` cannot enter `D'`: entering
and leaving `D'` would require two boundary vertices.  It is therefore
contained in `X union Y union {s}`, as asserted.  Finally, if the
actual-row quotient is positive, its branch sets lift through the three
contractions, proving alternative 1.  This completes the proof. \(\square\)

For the sharp Hadwiger cell `k=7`, alternative 2 gives **five mutually
internally disjoint one-label ears**, not merely five unrelated portal
contacts.

## 3. Exact coloring rigidity at the unique edge

Now assume in addition that `G` is not `r`-colorable but every proper
minor is `r`-colorable.  Let `c` be an `r`-coloring of `G-xy`.  Necessarily

\[
 c(x)=c(y)=\alpha,                                \tag{3.1}
\]

since otherwise `c` colors `G`.  Write `phi=c|S`, with its color names
fixed (not merely up to a permutation).

For `Z in {X,Y}` and terminal `u in {x,y}`, let `L_Z(phi,u)` be the set
of colors which can occur at `u` in an `r`-coloring of `G[S union Z]`
whose restriction to `S` is exactly `phi`.

### Lemma 3.1 (terminal rigidity)

\[
 L_X(\phi,x)=L_Y(\phi,y)=\{\alpha\}.              \tag{3.2}
\]

#### Proof

Both sets are nonempty by restriction of `c`.  If
`a in L_X(phi,x)` and `b in L_Y(phi,y)` with `a!=b`, use the
corresponding two arm colorings and retain `c` on `S union D'`.  They
agree pointwise on `S`; there are no edges between `D'` and `D`, and
the only edge between `X` and `Y` is `xy`, whose ends now have distinct
colors.  The three colorings therefore glue to an `r`-coloring of `G`,
a contradiction.  Thus every pair in the Cartesian product of the two
nonempty sets has equal coordinates.  Both sets must be the same
singleton, and (3.1) identifies it as `{alpha}`. \(\square\)

### Corollary 3.2 (pinned-or-palette-tight transition)

Exactly one of the following applies to the deletion coloring.

1. The terminal color `alpha` occurs on `S` (the transition is
   **boundary-pinned**).
2. The color `alpha` is absent from `S`, and every one of the other
   `r-1` colors occurs on `S` (the transition is **palette-tight**).

In particular, when `r=6` and `|S|=7`, a palette-tight transition induces
an exact five-block equality partition on `S`.  Its block-size type is
either

\[
 3+1+1+1+1\quad\hbox{or}\quad2+2+1+1+1.           \tag{3.3}
\]

#### Proof

Suppose `alpha` is absent from `S` and another color `gamma` is also
absent.  Permuting `alpha` and `gamma` in the `X`-arm coloring fixes
`phi` pointwise and changes the color at `x`, contradicting (3.2).
Thus all other colors occur.  The last assertion just partitions seven
vertices into five nonempty color classes. \(\square\)

### Corollary 3.3 (simultaneous color-indexed anchoring)

For every `gamma != alpha`, the `alpha/gamma` component containing `x`
in `G[X]` has a neighbour in `S` colored `alpha` or `gamma`, and so does
the corresponding component at `y` in `G[Y]`.  In the palette-tight
case, the anchor color must be `gamma`.

#### Proof

If the component at `x` had no such boundary incidence, interchange
`alpha` and `gamma` on it.  This fixes `phi` pointwise and changes the
terminal color, contradicting Lemma 3.1.  The other arm is symmetric.
If `alpha` is absent from `S`, only a `gamma`-colored boundary incidence
is possible. \(\square\)

Thus, in the unique-interface HC7 cell, simultaneous two-sided anchoring
does not remain an amorphous Kempe obstruction.  Unless a nested exact
seven-cut is exposed, it comes with both:

* five disjoint one-label portal ears supplied by connectivity; and
* a rigid boundary-pinned or exact five-block coloring transition.

This is the appropriate input for the next portal-peel theorem.

## 4. Why the ear outcome is indispensable

It is false that full actual rows plus all five two-sided color anchors
force a `K_7` quotient or an exact seven-cut without using the placement
of the ears.

Let

\[
 S=\{z,c_0,\ldots,c_5\},\qquad G[S]=K_1\vee C_6,
\]

and add three vertices `h,x,y`, each complete to `S`, with the single
helper edge `xy`.  Regard `h` as the opposite full shore and
`X={x},Y={y}`.  Both actual rows equal `S`, and both external
neighbourhoods have order eight, so neither is an exact seven-cut.

This ten-vertex quotient has no `K_7` minor.  Indeed `z` is universal,
so a hypothetical `K_7` model can be chosen with `{z}` as one branch
set and would leave a `K_6` model in

\[
 F=C_6\vee(K_2\mathbin{\dot\cup}K_1).             \tag{4.1}
\]

To see that `eta(F)<=5`, classify branch sets of a clique model as
`C_6`-only, helper-only, or mixed, and let `m` be the number of mixed
sets.  The nonmixed sets on either side form clique minors after the
vertices used by the mixed sets are deleted.  If `m=0`, their total
number is at most `eta(C_6)+eta(K_2 dotcup K_1)=3+2=5`.  If `m=1`,
deleting at least one cycle vertex leaves a forest and deleting at least
one helper leaves Hadwiger number at most two, so the total is at most
`1+2+2=5`.  If `m=2`, at most one helper remains, giving
`2+2+1=5`.  If `m=3`, no helper remains and the bound is again at most
`3+2=5`.  No larger `m` is possible.  Hence (4.1) has no `K_6` minor.

Nevertheless, color `x,y,h` with color 6, color `z` with 1, and color

\[
 (c_0,c_1,c_2,c_3,c_4,c_5)=(2,3,4,2,3,5).
\]

This is a proper six-coloring after deleting `xy`.  Every color
`1,...,5` occurs on `S`, and since `x,y` are complete to `S`, all five
two-anchor alternatives hold on both sides.  The example also has the
full seven one-label ears `x-s-y` (`s in S`).  It therefore pinpoints
the missing information: anchoring alone is insufficient, while the
ear system retained in Theorem 2.1 is exactly the structural datum that
must be exploited.

The focused verifier `unique_interface_c6_counterexample_verify.py`
checks the coloring and performs an independent exhaustive connected
branch-set search.
