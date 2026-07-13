# Complementary-block exchange in a 3-connected Moser rural shore

**Status:** proved and independently audited.

## 1. Setting and result

Let `G` be a seven-connected graph which is proper-minor-minimal subject to
not being six-colourable.  Let `v` have neighbourhood

\[
 S=\{0,1,2,3,4,5,6\},
 \qquad
 E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.       \tag{1.1}
\]

Assume `G-N[v]` has two components `C,D`, both `S`-full.  Suppose `C`
contains two vertex-disjoint paths, with interiors outside `N[v]`, joining
`0` to `5` and `2` to `4`.  This is the favourable pure-Moser crossing.
Assume `D` has order at least four and is three-connected.

### Theorem 1 (3-connected rural closure)

Under these hypotheses, `G` contains a `K_7` minor or is six-colourable.
In particular, these hypotheses cannot occur in a hypothetical minimal
`HC_7` counterexample.

The new mechanism is an exact alternative:

* a crossing linkage in `D` gives the already-audited literal two-row
  `K_7` completion; or
* the rural disk supplies the *noncrossing* complementary carriers `13`
  and `24`, and those carriers reflect every state returned by contracting
  the opposite full shore.

Thus the rural order is used positively.  No global planarity conclusion is
inferred from one page.

## 2. Two elementary interface lemmas

### Lemma 2.1 (two added root edges make a two-connected closure)

Let `K` be three-connected.  Add four new vertices `a,b,c,d`, the two edges
`ab,cd`, and arbitrary nonempty edges from each new vertex to `K`.  If

\[
 |N_K(\{a,b\})|\ge2,
 \qquad |N_K(\{c,d\})|\ge2,                              \tag{2.1}
\]

then the resulting graph is two-connected.

#### Proof

The two nonempty portal sets of `a,b` have distinct representatives unless
both are the same singleton.  The first inequality excludes precisely that
exception.  Choose distinct `x in N_K(a)` and `y in N_K(b)`.  Then

\[
                         x-a-b-y                         \tag{2.2}
\]

is an ear with distinct ends on the two-connected graph `K`.  Adding an ear
to a two-connected graph preserves two-connectivity.  Apply the same
argument to `c,d`, whose two distinct representatives lie in the original
`K`, and then add all unused portal edges.  Adding edges cannot create a
cutvertex.  \(\square\)

### Lemma 2.2 (consecutive facial carriers)

Let `K` be connected and let `Q=K\cup\{a,b,c,d\}` be two-connected with a
disk embedding in which the four displayed vertices occur on the disk
boundary in cyclic order

\[
                         a,b,c,d.                         \tag{2.3}
\]

Suppose `ab,cd` are absent.  Then `K` contains disjoint nonempty connected
sets `X,Y` such that

* `X` has neighbours at both `a,b`;
* `Y` has neighbours at both `c,d`; and
* after enlarging one set inside `K`, `X,Y` are adjacent.

#### Proof

Because `Q` is two-connected, the boundary of its outer face is a cycle.
Take the boundary arc from `a` to `b` containing neither `c` nor `d`, and the
disjoint boundary arc from `c` to `d` containing neither `a` nor `b`.  Since
`ab,cd` are absent, each arc has a nonempty connected interior.  No other
one of the four added vertices lies on either open arc, so both interiors
lie in `K`.  Call them `X_0,Y_0`; they are disjoint and have the stated
literal endpoint contacts.

Choose a shortest `X_0-Y_0` path in connected `K`, truncated so that its
internal vertices avoid both end sets.  Add all internal vertices to `X_0`.
The resulting `X` and `Y=Y_0` remain disjoint and connected, retain all four
endpoint contacts, and the last path edge joins them.  \(\square\)

## 3. Linkage or a rural complementary pair

Use the favourable crossed `0-5` and `2-4` paths in `C` as in
`../results/hc7_moser_crossing_carrier.md`.  Assign the omitted frame vertex
`6` to the branch bag rooted at `5`.  The four crossed-page bags have exactly
one row-`1` duty, at `4`, and one row-`3` duty, at `2`.

The audited four-port theorem applied to `D` and the ordered roots

\[
                         1,3,4,2                          \tag{3.1}
\]

has two outcomes.  In its linkage outcome, disjoint `1-4` and `3-2` paths
inside `D`, followed by the audited adjacent-enlargement lemma, are the two
literal row carriers.  The audited two-row carrier theorem then gives a
literal `K_7` model.  We may therefore assume the other outcome:

\[
        G[D\cup\{1,2,3,4\}]
        \text{ has a disk embedding with boundary order }1,3,4,2.       \tag{3.2}
\]

Put

\[
                         Q=G[D\cup\{1,2,3,4\}].          \tag{3.3}
\]

We verify the two-connectivity needed to use the literal facial arcs.  If
`|N_D(\{1,2\})|<=1`, then

\[
             N_D(\{1,2\})\cup(S-\{1,2\})                \tag{3.4}
\]

has order at most six and separates the nonempty graph
`D-N_D(\{1,2\})` from `v` and the opposite component `C`.  Here `|D|>=4`
ensures the first side is nonempty.  This contradicts seven-connectivity.
Thus `|N_D(\{1,2\})|>=2`; identically,
`|N_D(\{3,4\})|>=2`.  The only edges induced by these four roots which are
needed are the literal Moser edges `12,34`.  Lemma 2.1, with `K=D`, proves
that `Q` is two-connected.

Apply Lemma 2.2 to (3.2), with

\[
                         (a,b,c,d)=(1,3,4,2).             \tag{3.5}
\]

The Moser nonedges `13,24` make the lemma applicable.  We obtain disjoint
adjacent connected sets `X,Y subseteq D` such that

\[
 X\text{ contacts }1,3,
 \qquad
 Y\text{ contacts }2,4.                                 \tag{3.6}
\]

These are not the crossing row carriers.  They are carriers for the two
independent complementary boundary blocks

\[
                         r=\{1,3\},\qquad e=\{2,4\}.     \tag{3.7}
\]

## 4. Exact state returned from the crossed shore

Contract the two disjoint connected sets

\[
                         \{v\}\cup r,
                 \qquad C\cup e.                        \tag{4.1}
\]

They are adjacent through the edges from `v` to `e`.  The resulting graph
is a proper minor and has a six-colouring.  Restrict it to the unchanged
closed `D`-shore and expand only the two independent literal blocks `r,e`.

The two contracted representatives are adjacent and each is adjacent to
all of `0,5,6`: the first through `v`, the second through the `S`-full
component `C`.  Since `56` is an edge while `05,06` are not, the exact
equality partition induced on the literal set `S` is one of

\[
\begin{aligned}
 R_0&=\{r,e,\{0\},\{5\},\{6\}\},\\
 R_5&=\{r,e,\{0,5\},\{6\}\},\\
 R_6&=\{r,e,\{0,6\},\{5\}\}.                            \tag{4.2}
\end{aligned}
\]

No palette label has been attached to a pre-existing branch bag: (4.2) is
only the literal equality partition returned by the minor colouring.

## 5. Every returned state is reflected through the rural carriers

For `q in \{0,5,6\}`, put

\[
                 I_0=\{0\},\qquad I_5=\{0,5\},
                 \qquad I_6=\{0,6\}.                    \tag{5.1}
\]

The sets `I_q` are independent.  Contract in one proper minor

\[
                         X\cup r,
                 \qquad Y\cup e,
                 \qquad \{v\}\cup I_q.                 \tag{5.2}
\]

All three sets are disjoint and connected.  The first two are adjacent by
the `X-Y` edge, and the star representative is adjacent to both through
`v-r` and `v-e` edges.

For `q=0`, the three representatives together with literal `5,6` form a
`K_5`.  Besides the adjacencies just listed, the exact witnesses are

\[
 35,16 \quad\text{from }X\cup r,
 \qquad
 45,26 \quad\text{from }Y\cup e,                         \tag{5.3}
\]

and the star representative sees `5,6` through `v`, while `56` is literal.

For `q=5`, the three representatives and literal `6` form a `K_4`: use
`16` from the first block, `26` from the second, and either `v6` or `56`
from the star block.  For `q=6`, they and literal `5` form a `K_4`: use
`35`, `45`, and either `v5` or `65`.

Thus every proper minor in (5.2) has a six-colouring which, after restriction
to the unchanged closed `C`-shore and expansion of the independent literal
blocks, induces **exactly** `R_q` on `S`.  The clique just verified forces
different colours on all displayed blocks.

Choose the value of `q` actually returned in (4.2).  Permute the six colours
on one closed-shore colouring so the two colourings agree on every literal
vertex of `S`.  The open components `C,D` are anticomplete, so the colourings
glue to a six-colouring of `G-v`.  Every partition in (4.2) has at most five
blocks.  After the palette alignment, one colour is absent from `S`; assign
it to `v`.  This gives a six-colouring of `G`, a contradiction.

Sections 3--5 prove Theorem 1. \(\square\)

## 6. Exact contribution and trust boundary

This theorem closes an unbounded family: every order-at-least-four,
three-connected rural component opposite the favourable crossed Moser page.
Together with the audited thin-rural exchange (which closes singleton,
bridge, cutvertex, cycle, and cactus shores), the separately certified
triangle-shore theorem, and the low-cut theorem, it removes every internal
geometry **conditional on that favourable crossing**.

It does not prove that an arbitrary crossing of the five-root frame can be
relabelled as the favourable disjoint `0-5`, `2-4` pair.  Different induced
five-cycles or multiple crossing witnesses must be composed without assuming
their paths are mutually disjoint.  This is the remaining multi-frame step,
not a residual 3-connected web inside `D`.

The result uses no computation.  Its dependencies are the GREEN four-port
linkage-or-disk theorem and literal two-row carrier theorem in
`../results/hc7_moser_crossing_carrier.md` and the standard fact that adding
an ear to a two-connected graph preserves twoconnectivity.
