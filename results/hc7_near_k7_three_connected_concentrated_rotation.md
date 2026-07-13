# Three-connected donors eliminate the concentrated two-piece rotation

## Status

This closes an infinite family left outside the single-gate involution
theorem.  In the `4+1+1+1` seven-root distribution, the concentrated
rotation moves two disjoint pieces from one donor into the two missed twin
bags.  If the donor is three-connected, a rooted connected partition can
leave a singleton protected core.  The resulting `K_7^-`/`K_7^vee` model
has a singleton deficient centre and contradicts the original
deficient-first normalization.

Thus a surviving concentrated rotation is not a 3-connected portal
problem.  It is confined to a cutvertex, a 2-separation, or a cycle torso,
where adhesion states/web composition are the appropriate tools.

## Lemma 1 (two-sided neighbour partition)

Let `H` be a 2-connected graph, let `s,t` be distinct vertices, and let
`Q subseteq V(H)` contain at least two vertices.  There is a partition

\[
                         V(H)=L\mathbin{\dot\cup}R        \tag{1.1}
\]

such that:

1. `H[L]` and `H[R]` are connected;
2. `s in L` and `t in R`; and
3. both `L` and `R` meet `Q`.

### Proof

Add the edge `st` if it is absent.  The resulting graph remains
2-connected and has an `st`-numbering

\[
                         v_1=s,v_2,\ldots,v_n=t,          \tag{1.2}
\]

in which every internal vertex has a neighbour earlier and a neighbour
later in the order.  The standard inductive consequence is that every
prefix and every suffix is connected.  This connectivity uses only old
edges of `H`: the possibly added edge `st` has one end first and the other
last, so it lies in no proper prefix or suffix.

Let `p` and `q` be the least and greatest positions occupied by vertices
of `Q`.  Since `Q` has two distinct vertices, `p<q`.  Choose
`k` with `p<=k<q` and put

\[
                  L=\{v_1,\ldots,v_k\},\qquad
                  R=\{v_{k+1},\ldots,v_n\}.              \tag{1.3}
\]

The prefix/suffix property gives connectivity, their ends contain `s,t`,
and the choices of `p,q` put a member of `Q` on each side. \(\square\)

## Theorem 2 (3-connected concentrated donor closure)

Let `mu>=2` be the minimum deficient-centre order among all (not
necessarily spanning) labelled `K_7^vee` models in `G`.  Use any current
transported labelled model

\[
                     X,B,C,U,V_1,V_2,V_3,                \tag{2.1}
\]

where:

1. `B,C,U,V_1,V_2,V_3` form a `K_6` model;
2. `X` is connected, is anticomplete to `B,C`,
   and meets `U,V_1,V_2,V_3`;
3. four distinct selected vertices of `N(X)` lie in `U`; and
4. the displayed transported frame belongs to the same comparison class
   (so a new labelled near model may be compared with `mu`).

Suppose some selected root `r in U` satisfies

\[
              G[U-r]\text{ is 2-connected},\qquad
              |N_U(r)|\ge2.                              \tag{2.1a}
\]

Then at least one of the following occurs.

1. `G` contains a `K_7` minor.
2. There is a nonempty connected proper set `Y subset U` for which
   `N_G(Y)` is an actual separator of order at least seven (full at exact
   order seven).
3. There is a labelled `K_7^-` or `K_7^vee` model with a singleton
   deficient centre, contradicting `mu>=2`.

In particular (2.1a) holds for every selected root when `G[U]` is
3-connected.  Consequently, in a hypothetical minimal counterexample
after excluding the target and faithful adhesion outputs, the donor in
every concentrated two-piece rotation is not 3-connected.

### Proof

Protect a selected root `r` satisfying (2.1a), and call two of the other
selected roots `s,t`.  By hypothesis,

\[
                         H=G[U-r]                         \tag{2.2}
\]

is 2-connected, and

\[
                         Q=N_U(r)                         \tag{2.3}
\]

has at least two vertices.  Apply Lemma 1 to `H,s,t,Q`, obtaining
connected sets `L,R` which partition `U-r`, contain `s,t` respectively,
and each have an edge to `r`.  Thus

\[
                         U=\{r\}\mathbin{\dot\cup}L
                                   \mathbin{\dot\cup}R   \tag{2.4}
\]

is a three-part connected partition whose singleton core is adjacent to
both moved parts.  Each part contains a selected `X`-neighbour.

If `L` or `R` misses either twin `B` or `C`, its open neighbourhood is an
actual separator: the moved part is one nonempty side and the whole missed
connected twin bag is a far side.  Seven-connectivity gives order at least
seven, with the standard fullness conclusion at equality.  This is
outcome 2.

Otherwise both `L,R` meet both twins.  Assign `L` to `B` and `R` to `C`
and apply the audited one-donor deficiency-rotation theorem with

\[
                    U_0=\{r\},\qquad Z_B=L,\qquad Z_C=R. \tag{2.5}
\]

The enlarged twin bags are connected.  The two edges from `r` into
`L,R` restore the centre--twin spokes, and the selected root `r` supplies
the centre--`X` spoke.  The six foreign bags

\[
                    X,\ B\cup L,\ C\cup R,\ V_1,V_2,V_3 \tag{2.6}
\]

form a clique model.  The singleton centre `{r}` can miss only some of
the three untouched neutral rows.

If it misses none, the seven bags give `K_7`, outcome 1.  If it misses one
or two, they give a labelled `K_7^-` or `K_7^vee` model with deficient
   centre `{r}`, outcome 3.  Such a model is admissible in the comparison
   class and has centre order one, strictly below `mu>=2`.

If `{r}` misses all three untouched rows, `N_G(r)` is an actual separator:
any one of the connected `V_i` is a far side after deleting the open
neighbourhood of `r`.  This again gives outcome 2.  The cases exhaust the
rotation theorem. \(\square\)

## Corollary 3 (the directed residue is adhesion-two)

Apply a Tutte decomposition to a surviving concentrated donor `U`.
Theorem 2 eliminates every 3-connected realization in which the four
selected roots can be handled in the donor itself.  Hence all four-root
capacity must be concentrated through:

* a cutvertex gate;
* a 2-vertex adhesion into one 3-connected torso; or
* a cycle torso.

Virtual torso edges are not host edges, so this corollary is a localization,
not a completed split.  Its significance is that the only possibly
directed rotation left outside the involution theorem already has the
width-two web/adhesion form requested by the composition programme.

More sharply, at every surviving selected root `r`, either `d_U(r)<=1`
or `G[U-r]` is not 2-connected.  Thus even inside a non-3-connected donor,
the four roots must sit at literal leaf/gate positions of its
block--2-cut structure; a root in a locally 3-connected region would
trigger Theorem 2 directly.

## Uniform form

The proof uses only the following general mechanism.  A `k`-connected
rooted-model state has one donor containing a protected root and two
surplus roots.  If the donor is 3-connected, deleting the protected root
leaves a 2-connected graph; an `st`-numbering splits the remainder into
two rooted shores, each reattached to the singleton core.  Whenever the
two target transfers lose at most the allowed number of other rows, a
globally deficient-first model must therefore have singleton centre.
