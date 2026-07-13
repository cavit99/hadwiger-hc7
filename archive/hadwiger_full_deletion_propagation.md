# Full-deletion vertices propagate through a minimum fragment

## 1. General theorem

Let `G` be `k`-connected, let `S` be a `k`-cut, and let `D` be a
component of `G-S` of minimum order among all components behind all
`k`-cuts.  Say that `u in D` is a **full-deletion vertex** when

\[
                         N_S(D-u)=S.                 \tag{1.1}
\]

The original component is full to `S`: otherwise its proper boundary in
`S` would be a cut of order below `k`.

Write

\[
                 \mathcal H=\{u\in D:N_S(D-u)=S\}.  \tag{1.2}
\]

### Theorem 1.1 (full-deletion propagation)

If `mathcal H` is nonempty, then

\[
                         \mathcal H=V(D).            \tag{1.3}
\]

Equivalently, in a minimum fragment the existence of one vertex whose
deletion preserves every boundary contact forces every boundary portal
class to have order at least two.

### Proof

We first record the one-sided form of atomic surplus.  If `A` is any
nonempty connected proper subset of `D`, then

\[
 |N_S(A)|+|N_D(A)-A|=|N_G(A)|\ge k+1.              \tag{1.4}
\]

Indeed, `N_G(A)` separates `A` from a component of `G-S` different from
`D`.  Its order is at least `k` by connectivity.  Equality would make
`N_G(A)` a `k`-cut with `A` as a component behind it, contradicting the
minimum choice of `D`.  Notice that `D-A` need not be connected.

Now take a component `C` of the induced graph `D[mathcal H]`, and put

\[
                         X=N_D(C)-C.                \tag{1.5}
\]

Every `x in X` lies outside `mathcal H`; otherwise it would be joined to
`C` in `D[mathcal H]`.  Since `x` is not a full-deletion vertex, some
boundary label `s_x in S` has no portal in `D-x`.  Fullness of the
original shore `D` therefore gives the exact private-portal identity

\[
                         N_D(s_x)=\{x\}.            \tag{1.6}
\]

The labels `s_x` are distinct for distinct `x`.  None is contacted by
`C`, and hence

\[
                         |N_S(C)|\le k-|X|.          \tag{1.7}
\]

If `C` were a proper subset of `D`, equations (1.5)--(1.7) would give

\[
 |N_S(C)|+|N_D(C)-C|\le k,
\]

contrary to (1.4).  Thus `C=D`.  Since `C subseteq mathcal H`, this is
exactly (1.3).  QED.

## 2. The `C6+K1` minimum atom

Use the notation of
`hadwiger_c6_specified_side_warehouse_exchange.md`: `G` is a
proper-minor-minimal hypothetical counterexample to `HC_7`, `S` is the
exact seven-boundary with

\[
                       \overline{G[S]}=C_6\dot\cup K_1,
\]

and `D` is the chosen minimum full shore.  Hub promotion already supplies
one vertex `h` for which `D-h` is full.  Theorem 1.1 therefore gives the
following much stronger conclusion.

### Corollary 2.1 (the whole atom is the hub core)

Every vertex of `D` is a full-deletion vertex.  In particular:

1. every boundary label has at least two distinct portals in `D`;
2. for every `u in D`, the singleton/full-body atlas applies to
   `{u}|(D-u)`, so
   \[
        |N_S(u)|\le4,\qquad d_D(u)\ge8-|N_S(u)|;    \tag{2.1}
   \]
3. for every edge `uv in E(D)`, both `D-u` and `D-v` are full, the body
   `D-{u,v}` is connected and misses at most one boundary label, and a
   possible missed label is adjacent to both `u,v`;
4. every internal edge carries the joint-edge palette warehouse: in every
   six-colouring of `G-uv`, the ends have one colour and lie together in
   every endpoint bichromatic component, with all five non-endpoint
   palettes represented at both ends inside `D union S`.

### Proof

The first assertion is Theorem 1.1.  Item 1 is its portal-class
reformulation.  Item 2 is the singleton/full-body atlas followed by
one-sided atomic surplus at `{u}`.  The minimum fragment is
three-connected, so `D-{u,v}` is connected; applying one-sided atomic
surplus to this body gives items 3 exactly as in Theorem 3.1 of the
specified-side warehouse note.  Item 4 is Theorem 4.1 of that note,
which now applies to every edge rather than only to promoted hub edges.
QED.

## 3. Consequences for the former cycle branch

The graph `D[mathcal H]` is not merely leafless and does not merely contain
a cycle: it is the entire three-connected shore `D`.  Thus there is no
separate hub-cycle holonomy problem and no tight-leaf alternative.  The
transported degree-eight leaf closure remains a valid independent theorem,
but it is not needed inside this minimum atom.

The remaining exchange problem is correspondingly more uniform:

> **All-edge rooted exchange.**  A three-connected minimum fragment over
> a fixed boundary has every boundary portal class of order at least two,
> every vertex deletion full, and the endpoint-complete palette warehouse
> on every internal edge.  Prove that it contains the target rooted model,
> or that one faithful operation state occurs on the opposite shore.

This is strictly stronger input than a single cyclic list of operation
states.  In particular, any proposed odd-cycle selector must extend from
the cycle edges to **every chord, bridge edge, and off-cycle edge** of the
three-connected shore while preserving the same full-deletion property.
The low-connectivity equality-gadget and wheel selectors do not meet this
all-edge condition.

## 4. A five-carrier rooted completion and the first size consequence

Let `z` denote the isolated vertex of the missing graph
`C6 dotcup K1`.  Thus `z` is adjacent in `G[S]` to every other boundary
vertex.

### Lemma 4.1 (five-carrier completion)

Suppose `Q_1,...,Q_5` are pairwise disjoint, pairwise adjacent connected
subgraphs of `D` such that

\[
 |N_S(Q_i)|\ge4\quad(i\in[5]),                    \tag{4.1}
\]

and every boundary label is contacted by at least two **different**
`Q_i`.  Then `G` contains a `K_7` minor.

### Proof

Put `R_i=N_S(Q_i)-{z}`.  We claim that the five sets `R_i` have distinct
representatives.  Hall's condition is immediate for a subfamily of order
at most three, since every `R_i` has order at least three.

If four sets had union of order at most three, all four would equal one
three-set `A` and all four original rows would be `A union {z}`.  Each of
the other three cycle labels would then be contacted by at most the fifth
carrier, contrary to the assumed two-carrier multiplicity.  If all five
sets had union of order at most four, at least two of the six cycle labels
would be contacted by none of the carriers, again a contradiction.  Hall's
theorem now gives distinct

\[
                    x_i\in N_S(Q_i)-\{z\}.          \tag{4.2}
\]

Use the seven branch bags

\[
 Q_i\cup\{x_i\}\ (i\in[5]),\qquad \{z\},\qquad H, \tag{4.3}
\]

where `H` is the opposite full shore.  The first five bags are connected
and pairwise adjacent through the `Q_i`; each sees `{z}` because `z` is
adjacent to `x_i`; and each sees `H` because `H` is full to `S`.  The last
two bags are adjacent through any boundary edge from `H` to `z`.  Thus
(4.3) is a `K_7` model.  QED.

### Corollary 4.2 (the minimum atom has at least six vertices)

In the `C6+K1` setting, `|D|>=6`.

### Proof

For every `u in D`, Corollary 2.1 gives

\[
             |N_S(u)|+d_D(u)\ge8,
             \qquad |N_S(u)|\le4.                 \tag{4.4}
\]

Thus `|D|<=4` is impossible.  If `|D|=5`, equality holds throughout:
`D=K_5` and every vertex of `D` contacts exactly four boundary labels.
Take its five singleton vertices as the carriers in Lemma 4.1.  Every
boundary label contacts at least two distinct vertices by Corollary 2.1,
so the lemma gives `K_7`, a contradiction.  QED.

The dependency-free/z3 cross-check
`c6_allhub_portal_pair_probe.py` encodes the Hall certificate as all 5,040
possible choices of the universal singleton and five representatives; it
reports the residual formula unsatisfiable.  The proof above does not rely
on that computation.

### Corollary 4.3 (a six-vertex atom is not complete)

If `|D|=6`, then `D ne K_6`.

### Proof

Suppose `D=K_6`, with vertices `d_0,...,d_5`.  Equation (2.1) says that
each `d_i` contacts three or four boundary labels.  Every label has at
least two portals by Corollary 2.1.

If the six contact rows have distinct representatives in `S`, the six
bags `{d_i,x_i}` together with the opposite full shore `H` form a
`K_7` model.  Suppose no such representatives exist.  Hall's theorem and
the row lower bound three show that a deficient subfamily has order at
least four.  A deficient family of order five would leave at least three
labels to be represented twice by the sole remaining row, and a deficient
family of order six would leave an uncontacted label.  Hence exactly four
rows have union a three-set `A`.  Those four rows equal `A`; two-portal
multiplicity forces both remaining rows to equal `S-A`, a four-set.

It remains only the finite boundary symmetry of
`K_7-(C_6 dotcup K_1)`.  Label its two prism triangles

\[
 \{0,1,2\},\qquad\{3,4,5\},
\]

its matching edges `03,14,25`, and its universal vertex `z=6`.  Up to the
dihedral automorphism group of the missing six-cycle, a three-set `A` has
one of the following six forms.  In the table, `d_0,...,d_3` have row `A`
and `d_4,d_5` have row `S-A`; the four singleton bags are always
`{0},{1},{2},{z}`, and the final displayed two bags are added to those
four and `H`.

\[
\begin{array}{c|cc}
A& B_1&B_2\\ \hline
012&\{3,d_0,d_4\}&\{4,d_1,d_5\}\\
013&\{3,5,d_0\}&\{4,d_1,d_4\}\\
015&\{5,d_0\}&\{3,4,d_4\}\\
01z&\{3,4,d_4\}&\{5,d_0,d_5\}\\
03z&\{3,4,d_4\}&\{5,d_0,d_5\}\\
04z&\{3,d_4\}&\{4,5,d_0\}.
\end{array}                                             \tag{4.5}
\]

In every row the two displayed bags are disjoint, connected, adjacent,
and adjacent to all four singleton bags; this follows directly from the
two prism triangles, the matching `03,14,25`, and the indicated contact
rows.  The opposite full shore is adjacent to them through their boundary
vertices and to the four singletons.  Thus each row of (4.5) is an
explicit `K_7` model, a contradiction.  QED.

The script `c6_allhub_order6_probe.py` independently checks all 35 labelled
choices of `A` and prints a seven-bag certificate for each.

### Lemma 4.4 (the six-carrier repaired-SDR lemma)

Let `F=K_6-M`, where `M` is a matching of order two or three.  Give every
endpoint of `M` a contact row in `S` of order four, and every other vertex
a row of order three or four.  Suppose every label of `S` belongs to at
least two rows.  Then there are six distinct representatives `x_i`, one
from each row, such that for every `d_i d_j in M` at least one of

\[
 x_ix_j\in E(G[S]),\qquad x_j\in N_S(d_i),\qquad
 x_i\in N_S(d_j)                                    \tag{4.6}
\]

holds.

For a matching of order one the same conclusion holds unless, after
naming its ends `d_4,d_5`, the other four vertices have one common
three-row `A` and both ends have row `S-A`.

### Certified finite proof

There are only `7P6=5,040` injective representative maps.  The verifier
`c6_allhub_order6_residual_classify.py` uses Boolean variables `x_{i,s}`
and imposes exactly

\[
 3\le |R_i|\le4,quad |R_i|=4\ (d_i\in V(M)),quad
 |\{i:s\in R_i\}|\ge2.                              \tag{4.7}
\]

For every injective map `f`, it forbids the conjunction

\[
 \bigwedge_i (f(i)\in R_i)\quad\wedge\quad
 \bigwedge_{d_id_j\in M,\ f(i)f(j)\notin E(G[S])}
       (f(j)\in R_i\ \vee\ f(i)\in R_j).            \tag{4.8}
\]

Thus a satisfying assignment is exactly a row system with no repaired
SDR; all missing pairs are tested simultaneously.  For `|M|=2,3` the
formulas are unsatisfiable.  For `|M|=1`, adding the negation of the 35
displayed `A^4|(S-A)^2` profiles is unsatisfiable.  The output is

```text
q=1 outside exact 2+4 profiles unsat
q=2 repaired-SDR residual unsat
q=3 repaired-SDR residual unsat
```

The trust boundary is the displayed short standalone encoding,
Z3's finite Boolean kernel, and the host Python runtime.  No graph-minor
search is used in this lemma.

### Corollary 4.5 (the minimum atom has at least seven vertices)

In fact

\[
                              |D|\ge7.              \tag{4.9}
\]

### Proof

Corollary 4.2 gives `|D|>=6`.  Suppose `|D|=6`.  Equation (2.1) gives
`delta(D)>=4`, so the complement of `D` is a matching `M`.

The case `M=emptyset` is Corollary 4.3.  If `|M|=2` or `3`, apply Lemma
4.4.  The six bags `{d_i,x_i}` are connected.  Every ordinary pair is
adjacent through its edge in `D`, and (4.6) repairs every pair in `M`.
Together with the opposite full shore they form a `K_7` model.

If `|M|=1`, the same conclusion holds unless the exact residual profile
in Lemma 4.4 occurs.  Relabel its four `A`-row vertices as
`d_0,...,d_3` and its two `(S-A)`-row vertices as `d_4,d_5`.  The only
missing edge of `D` is `d_4d_5`.  The six explicit certificates in
(4.5) never use that edge: every internal or interbag `D` edge displayed
there has at least one end among `d_0,...,d_3`.  Hence the same table gives
a `K_7` in the residual case.  All matchings are excluded.  QED.

The order-six octahedral core is therefore not a genuine coherent-web
residue once the all-vertex full-deletion multiplicity is retained.  Any
remaining web or two-apex obstruction has order at least seven and must
realize the endpoint-complete operation warehouse on every internal edge.

## 5. Connectivity gives seven distinct literal portals

The size bound (4.9) unlocks a standard Hall argument in its sharp rooted
form.

### Lemma 5.1 (full-boundary portal matching)

Let `G` be `k`-connected, let `S` be a `k`-cut, and let `D` be a component
of `G-S` with `|D|>=k`.  Then the portal classes

\[
                         P_s=N_D(s)\quad(s\in S)     \tag{5.1}
\]

have distinct representatives in `D`.

### Proof

If Hall fails, choose `A subseteq S` and put

\[
                         X=\bigcup_{s\in A}P_s,
                         \qquad |X|<|A|.             \tag{5.2}
\]

Since `|X|<=k-1<|D|`, take a component `C` of `D-X`.  It has no contact
with any label in `A`, and every internal neighbour outside `C` lies in
`X`.  Therefore

\[
                         N_G(C)\subseteq X\cup(S-A),
\]

so

\[
                         |N_G(C)|\le |X|+k-|A|<k,    \tag{5.3}
\]

contrary to `k`-connectivity.  QED.

### Corollary 5.2 (literal seven-root normal form)

There are distinct vertices

\[
                         p_s\in N_D(s)\quad(s\in S). \tag{5.4}
\]

Moreover every portal class has another member besides its selected
representative, by full-deletion propagation.

Thus the minimum atom has a simultaneous system of seven literal roots,
each class having an additional reserve portal (not necessarily distinct
across classes).  This is stronger than choosing a new
SDR separately for each operation state.

### Lemma 5.3 (nonseparating portal sparsity)

For a nonempty set `X subset D` such that `D-X` is nonempty and connected,
let

\[
                  A_X=\{s\in S:N_D(s)\subseteq X\}. \tag{5.5}
\]

Then

\[
                              |A_X|\le |X|-1.        \tag{5.6}
\]

### Proof

Put `Y=D-X`.  The connected proper set `Y` has

\[
                         N_G(Y)\subseteq X\cup(S-A_X).
\]

One-sided atomic surplus gives `|N_G(Y)|>=8`, and hence

\[
             8\le |X|+7-|A_X|,
\]

which is (5.6).  QED.

Since `D` is three-connected, deletion of any two vertices leaves it
connected.  Therefore no boundary class has a unique portal, and at most
one boundary class can have all its portals in any prescribed vertex pair.
If such a class exists, its portal set is exactly that pair.  More
generally, (5.6) is the exact capacity inequality that any
label-preserving branch-set split must preserve; it rules out parallel
two-portal labels without appealing to colour states.

### Lemma 5.4 (strict Hall surplus and occurrence usability)

For every nonempty proper set `A subset S`,

\[
          \left|\bigcup_{s\in A}N_D(s)\right|\ge |A|+1.       \tag{5.7}
\]

Consequently every actual portal occurrence `x in N_D(s)` belongs to a
full system of distinct representatives of the seven portal classes.

#### Proof

Put `U=union_{s in A}N_D(s)`.  If `U=D`, then
`|U|=|D|>=7>=|A|+1`.  Otherwise take a component `C` of `D-U`.  It misses
every boundary label in `A`, and every internal neighbour outside `C`
lies in `U`.  Strict atomic surplus gives

\[
        8\le |N_G(C)|\le |U|+7-|A|,
\]

which is (5.7).

Now fix `x in N_D(s)` and match `s` to `x`.  For a set
`A subseteq S-{s}`, (5.7) says that its portal union has order at least
`|A|+1`; after deleting the one forbidden representative `x`, at least
`|A|` choices remain.  Hall's theorem therefore matches the other six
labels to distinct vertices outside `x`, extending the prescribed
occurrence to a full SDR.  QED.

Thus the simultaneous root system in Corollary 5.2 may be chosen through
any prescribed literal occurrence.  Any remaining rooted-model failure
is geometric; it cannot be blamed on an unusable portal occurrence.

### Theorem 5.5 (two prescribed roots or an exact order-eight gate)

Let `s,t in S` be distinct and let

\[
                         x\in N_D(s),\qquad y\in N_D(t),
                         \qquad x\ne y.                \tag{5.8}
\]

Then either the seven portal classes have an SDR which assigns `s` to
`x` and `t` to `y`, or there are a nonempty set
`A subseteq S-{s,t}` and a component `C` of `D-U`, where

\[
                         U=\bigcup_{a\in A}N_D(a),       \tag{5.9}
\]

such that

\[
 |U|=|A|+1,\qquad \{x,y\}\subseteq U,\qquad
 N_G(C)=U\mathbin{\dot\cup}(S-A).                    \tag{5.10}
\]

In particular `N_G(C)` is an actual separator of order eight.

#### Proof

Assign `s` to `x` and `t` to `y`, and apply Hall to the other five
portal classes after deleting the forbidden vertices `x,y`.  If Hall
holds, it gives the required extension.

Otherwise some nonempty `A subseteq S-{s,t}` satisfies

\[
 \left|\left(\bigcup_{a\in A}N_D(a)\right)-\{x,y\}\right|
       <|A|.                                           \tag{5.11}
\]

Lemma 5.4 gives `|U|>=|A|+1`.  Removing two vertices from `U` leaves at
most `|A|-1` vertices by (5.11), so equality is forced, both `x,y` lie
in `U`, and `|U|=|A|+1`.  Since `|A|<=5`, we have
`|U|<=6<|D|`; hence `D-U` has a component `C`.

The component `C` misses every boundary label in `A` and has no internal
neighbour outside `U`.  Therefore

\[
                         N_G(C)\subseteq U\cup(S-A),
\]

whose right side has order `|A|+1+7-|A|=8`.  Strict atomic surplus gives
`|N_G(C)|>=8`, so equality holds throughout and proves (5.10).  QED.

The proof is parameter-uniform: in a minimum `k`-fragment with strict
surplus `k+1`, failure to extend two prescribed distinct occurrences to
a full `k`-class SDR exposes an exact boundary of order `k+1`.  Thus the
simultaneous loss of two literal root coordinates is not an arbitrary
capacity failure; it is precisely the next separator layer.

## 6. Exact reduction to three rooted-`K_4` views

Label the missing cycle by `c_0,...,c_5` and its isolated vertex by `z`.
Choose the simultaneous roots in (5.4).

### Theorem 6.1 (antipodal rooted-`K_4` completion)

Let `c_j,c_{j+3}` be an antipodal pair on the missing six-cycle.  If `D`
has a rooted `K_4` model at the four selected roots

\[
       \{p_{c_i}:i\notin\{j,j+3\}\},              \tag{6.1}
\]

then `G` contains a `K_7` minor.

### Proof

Append the corresponding four boundary labels to their rooted bags.  Add
the three bags

\[
                  \{z\},\qquad \{c_j,c_{j+3}\},
                  \qquad H.                       \tag{6.2}
\]

The antipodal pair is an edge of `G[S]`, and it collectively sees every
other cycle label: their two pairs of missing-cycle neighbours are
disjoint.  The vertex `z` is universal on the cycle labels, and the
opposite shore `H` is full.  Hence the four rooted bags and the three bags
in (6.2) are pairwise adjacent connected branch sets.  QED.

Thus a target-free atom has **three simultaneous rooted-`K_4` failures**,
one on the complement of each antipodal pair.  This is already sufficient
for the planar/web mechanism; the following five-root completion is a
secondary, stronger-model alternative.

### Theorem 6.2 (five cycle roots complete to `K_7`)

If, for some `j`, the graph `D` has a rooted `K_5` model at

\[
                 \{p_{c_i}:i\in\mathbb Z_6-\{j\}\}, \tag{6.3}
\]

then `G` contains a `K_7` minor.

### Proof

Append the boundary vertex `c_i` to the rooted bag containing `p_{c_i}`.
The five bags remain disjoint and connected and still form a `K_5`.
Add the connected bag

\[
                              \{z,c_j\}             \tag{6.4}
\]

and the opposite full shore `H`.  The bag (6.4) sees every one of the five
rooted bags because `z` is adjacent to every cycle label; `H` sees them
through their appended labels and sees (6.4) through `z`.  These are seven
pairwise adjacent connected bags.  QED.

Consequently a target-free minimum atom also satisfies the simultaneous
six-fold obstruction

\[
 \text{for every }j\in\mathbb Z_6,\quad
 D\text{ has no rooted }K_5\text{ at }
 \{p_{c_i}:i\ne j\}.                               \tag{6.5}
\]

This is the correct replacement for hub-cycle holonomy.  The roots in all
tests are one common SDR with reserve portals, the host is one
three-connected minimum fragment, and every internal edge has the faithful
endpoint-complete operation state.  A coherent two-apex/web theorem need
only classify the simultaneous rooted failures in (6.1) and (6.5); it need not
track an arbitrary sequence of promoted hubs.

### Lemma 6.3 (synchronization of the three planar failures)

Suppose the three antipodal-complement quadruples from Theorem 6.1 lie in
one three-connected planar torso, and each quadruple is cofacial in the
torso's fixed embedding.  Then exactly one of the following holds.

1. all six selected cycle roots lie on one face; or
2. the three quadruples use three distinct faces, and each antipodal root
   pair is an edge common to the two faces whose quadruples contain it.

### Proof

Whitney uniqueness lets us use one embedding.  Any two quadruples share
the two roots of the third antipodal pair.  If their faces are distinct,
two distinct faces of a three-connected plane graph can meet in at most
one edge; hence the shared roots are the ends of their common edge.  If
two of the three faces coincide, their two quadruples together contain all
six roots, giving outcome 1.  Otherwise all three faces are distinct and
the preceding argument applied cyclically gives outcome 2.  QED.

Outcome 2 is not an unstructured residue: it is the exact three-face
coherent web, with the three antipodal pairs as its shared facial edges.
Thus, once the rooted-`K_4` obstruction is placed in one planar torso, the
entire infinite hub core has only a common-face society or this fixed
three-face society.  What remains is the faithful treatment of pieces
behind the torso's triangle adhesions.

### Corollary 6.3.1 (the three-face society is impossible)

In the minimum all-full-deletion atom, outcome 2 of Lemma 6.3 cannot
occur.

### Proof

Let `B={p_0,...,p_5}` be the six selected cycle roots.  Strict Hall surplus
for the proper six-label set `\{c_0,...,c_5\}` gives

\[
                 \left|\bigcup_{i=0}^5N_D(c_i)\right|\ge7.  \tag{6.6}
\]

Choose an occurrence `x in N_D(c_i)-B`.  Replacing only `p_i` by `x`
keeps the other five selected cycle roots fixed and gives another six-row
SDR.  The antipodal-complement view which omits `c_i` is unchanged.  Each
of the other two new views shares three vertices with its corresponding
old view.  Since a rooted `K_4` in any new view gives `K_7` by Theorem 6.1,
all three new views are cofacial.  Face intersections in the fixed
three-connected plane embedding force the two changed views to use the
same two old faces as before.  Hence `x` lies in their intersection.

Those two distinct faces meet exactly in the shared antipodal root edge
`p_i p_{i+3}`.  A vertex in their intersection is one of its ends, both of
which belong to `B`.  This contradicts `x notin B`.  Therefore no such
`x` exists and the six portal classes have union contained in `B`, of
order at most six, contradicting (6.6).  QED.

Thus a simultaneous planar failure of all three rooted views has only the
common-face outcome.  The former three-edge-bond operation analysis remains
a valid conditional theorem, but the literal occurrence surplus eliminates
that bond before colour holonomy is needed.

### Lemma 6.3.2 (the common-face society violates atomic degree sum)

Suppose `D` itself is planar and all six cycle portal classes lie on one
face `F`.  Then the minimum atom contains a `K_7` minor.

### Proof

Assume it is target-free.  Let `n=|D|`, let `m=|E(D)|`, and let `ell` be
the length of the facial cycle `F`.  Every vertex `u` satisfies

\[
                 d_D(u)+p_u\ge8,
                 \qquad p_u=|N_S(u)|\le4.           \tag{6.6a}
\]

All occurrences of the six cycle labels lie on `F`.  Hence an interior
vertex can contact at most the remaining universal label `z`, while a
facial vertex has load at most four.  Therefore

\[
                         \sum_{u\in D}p_u
                         \le4\ell+(n-\ell)=n+3\ell. \tag{6.6b}
\]

Planarity with a face of length `ell` gives

\[
                         m\le3n-3-\ell.             \tag{6.6c}
\]

Summing (6.7) and using (6.9) gives

\[
 \sum p_u\ge8n-2m\ge2n+6+2\ell.                  \tag{6.6d}
\]

Equations (6.8)--(6.10) imply `ell>=n+6`, contrary to `ell<=n`.  QED.

### Theorem 6.3.3 (uniform three-separator theorem)

The minimum `C6+K1` atom is not four-connected.  Since it is already
three-connected, it has a vertex cut of order exactly three.

### Proof

Suppose `D` were four-connected.  If an antipodal-complement view had a
rooted `K_4`, Theorem 6.1 would give `K_7`.  Otherwise the four-connected
rooted-`K_4` theorem makes `D` planar and makes all three views cofacial in
its unique embedding.  Lemma 6.3 and Corollary 6.3.1 eliminate the
three-face outcome, leaving one common face for the six selected roots.

The one-coordinate replacement argument of Lemma 1.1 in
`hadwiger_c6_common_face_order_exchange.md` puts every occurrence of all
six cycle portal classes on that face.  Lemma 6.3.2 is now a contradiction.
Thus `D` is not four-connected.  QED.

This is the first order-independent contact-or-separator theorem for the
minimum atom.  The remaining obstruction is forced behind a literal
three-cut of `D`; a four-connected planar web cannot realize the atomic
degree and portal loads.

### Corollary 6.3.4 (exact-seven atom descends to exact eight)

If `G` has no `K_7` minor, the minimum `C6+K1` exact-seven atom exposes
an actual separator of order exactly eight.

#### Proof

Let `T` be the three-cut supplied by Theorem 6.3.3 and let
`C_1,...,C_m` be the components of `D-T`.  Three-connectivity makes each
vertex of `T` adjacent to every `C_i`.  Put

\[
                         A_i=S-N_S(C_i).
\]

Strict atomic surplus applied to the connected proper set `C_i` gives

\[
          8\le |N_G(C_i)|=3+|N_S(C_i)|,
\]

so every `|A_i|<=2`.  Suppose all defects had order at most one.  Fix
distinct `i,j`.  Both sides of the split `C_i | (D-C_i)` are connected
and adjacent.  The first side misses at most one label of `S`; the second
side misses a set contained in `A_j`, hence also at most one.  The exact
two-piece `C6+K1` atlas then completes this split, together with the
opposite full shore, to a `K_7` model, a contradiction.

Thus some `|A_i|=2`, and its literal ambient neighbourhood is

\[
               N_G(C_i)=T\mathbin{\dot\cup}N_S(C_i),
               \qquad |N_G(C_i)|=3+5=8.
\]

This is the claimed exact-eight separator.  QED.

The argument is order-independent and leaves no owner-exchange residue at
the exact-seven layer: the only target-free outcome is the next separator
layer.  A standalone formulation and its hypotheses are recorded in
`hadwiger_c6_threecut_lobe_exchange.md`.

### Lemma 6.4 (the seven-vertex internal cut is universally rooted)

Let `J` be a three-connected graph on seven vertices with minimum degree
at least four.  If `J` is not four-connected, then every four distinct
vertices of `J` root a `K_4` minor.

#### Proof

Let `T` be a three-cut.  Every component `C` of `J-T` has order at least
two, since a singleton vertex would have degree at most three.  The four
vertices outside `T` therefore form exactly two components

\[
                         A=\{a_1,a_2\},\qquad
                         B=\{b_1,b_2\}.              \tag{6.6}
\]

Each pair is an edge.  A vertex in either pair has at most its pair mate
and the three vertices of `T` as neighbours; minimum degree four forces
it to be adjacent to all of `T`.  Thus `J` contains the spanning graph

\[
                         \overline{K_3}\vee(2K_2),     \tag{6.7}
\]

with arbitrary additional edges inside `T`.

Let `R` be any four roots and put `r=|R cap T|`.  The following branch
bags in (6.7) give a rooted `K_4`; unused vertices are simply deleted.

* If `r=0`, all of `A union B` are roots.  Adjoin two distinct vertices
  of `T` to the two `A`-root bags.  Those two bags see both singleton
  `B` bags, while the edges inside `A` and `B` supply the remaining
  adjacencies.
* If `r=1`, one of `A,B`, say `A`, contributes both roots and the other
  contributes one.  Adjoin the two nonroot vertices of `T` separately to
  the two `A`-root bags.
* If `r=2` and the two off-`T` roots lie in one pair, adjoin the two
  vertices of the other pair separately to the two `T`-root bags.  If
  the off-`T` roots lie in different pairs, adjoin the two unused pair
  mates separately to the two `T`-root bags and adjoin the unused vertex
  of `T` to either off-`T` root bag; this last addition repairs the sole
  missing adjacency between the two off-`T` roots.
* If `r=3`, the fourth root lies in one pair.  Adjoin the two vertices of
  the other pair separately to two of the `T`-root bags.  Their mutual
  edge joins those two bags, while the third `T` root itself sees both;
  all three see the off-`T` root.

Every displayed enlargement is connected, the four bags are disjoint,
and the preceding adjacency checks use only (6.7).  QED.

### Corollary 6.5 (the minimum atom has order at least eight)

In the minimum `C_6 dotunion K_1` atom,

\[
                              |D|\ge8.               \tag{6.8}
\]

#### Proof

Corollary 4.5 gives `|D|>=7`.  Suppose `|D|=7`.  The singleton atlas and
strict surplus give `delta(D)>=4`, and the minimum-fragment theorem gives
three-connectivity.  Corollary 5.2 supplies one simultaneous seven-root
SDR; since the shore has seven vertices, the selected roots exhaust it.

If `D` is not four-connected, Lemma 6.4 gives a rooted `K_4` for every
four-root view, contradicting Theorem 6.1.  Hence `D` is
four-connected.  If all three antipodal-complement views failed, the
four-connected rooted-`K_4` theorem would make `D` planar and make each
view cofacial in its unique embedding.  Lemma 6.3 leaves two cases.

In the common-face case, one face contains the six cycle roots.  A simple
plane graph on `n=7` vertices with a face of length at least six has

\[
                         |E(D)|\le3n-3-6=12,
\]

whereas `delta(D)>=4` gives `|E(D)|>=14`, a contradiction.  In the
three-face case, the three shared antipodal root edges form a triangle in
the plane dual.  The corresponding three primal edges form an edge cut.
But four-connectivity implies edge-connectivity at least four.  This is
again impossible.  Therefore one view has a rooted `K_4`, and Theorem 6.1
gives `K_7`.  QED.

The separate Boolean verifier `c6_allhub_order7_two_carrier_verify.py`
also returns UNSAT for a larger static template family, but Corollary 6.5
is a hand proof and does not depend on it.

### Lemma 6.6 (one common root face contains every cycle portal)

Suppose `D` is planar and three-connected, and for one selected system of
six distinct cycle roots the common-face outcome of Lemma 6.3 holds on a
face `F`.  Then

\[
                         N_D(c_i)\subseteq V(F)
                         \qquad(i\in\mathbb Z_6).      \tag{6.9}
\]

#### Proof

Fix `x in N_D(c_i)`.  If `x` is one of the other five selected cycle
roots, it already lies on `F`.  Otherwise replace only the selected root
`p_{c_i}` by `x`; the six cycle representatives remain distinct.

The antipodal-complement view which omits `c_i` and its mate is unchanged,
so its four roots lie on `F`.  Each of the other two views has three
unchanged roots on `F`.  Since `G` is target-free, Theorem 6.1 says none
of the three new views has a rooted `K_4`.  The planar rooted-`K_4`
theorem puts each view on a face.  Two distinct faces of a
three-connected plane graph share at most two vertices; hence every one
of these faces is `F`.  In particular the two views containing `x` put
`x` on `F`.  QED.

Thus the common-face residue is a full portal-set society, not merely a
fortunate six-root transversal.  The common-face circular-order theorem
may therefore be applied without separately transporting duplicate cycle
occurrences.

The remaining uniform target can now be stated without the Moser labels:

> **Three-view rooted exchange.**  Let a three-connected minimum fragment
> carry six labelled portal classes, with distinct selected roots and a
> reserve in every class,
> and suppose every vertex deletion preserves all classes and every
> internal edge carries the endpoint-complete critical palette state.  If
> the three antipodal-complement views fail their rooted `K_4`, then the fragment has a common
> rural two-apex embedding, or one internal faithful state is accepted by
> the opposite shore.

Unlike a single nonseparating rooted-`K_5` assertion, this target uses three
overlapping rooted-`K_4` views and the all-edge minor-transition network.  It is
also the precise place where a web theorem could eliminate an infinite
family at once.

## 7. Certified closure of the saturated order-seven atom

The finite exception in the common-row duplication theorem has `|D|=7`.
In the present all-deletion atom it is completely eliminable using two
uniform branch templates.

### Lemma 7.1 (order-seven two-carrier completion)

Let `D` be a graph on seven vertices satisfying

\[
 d_D(u)+|N_S(u)|\ge8,qquad |N_S(u)|\le4            \tag{7.1}
\]

for every vertex, and suppose every label of `S` has at least two portals
in `D`.  Then the graph consisting of `D`, the `C6+K1` boundary, and one
opposite full shore contains a `K_7` minor.

### Certified finite proof

Put `F=overline D`.  Equation (7.1) gives

\[
             d_F(u)\le2,qquad |N_S(u)|\ge2+d_F(u). \tag{7.2}
\]

The verifier `c6_allhub_order7_two_carrier_verify.py` uses one Boolean
variable for each edge of `F` and each vertex-label contact.  It imposes
exactly (7.2), the row upper bound four, and column sum at least two.  It
then forbids the following exhaustive positive templates.

1. **Six repaired representatives.**  Omit one vertex of `D`, assign the
   other six distinct boundary representatives which they contact, and
   repair every missing `D` edge either by an edge between representatives
   or by one cross contact.  The six two-vertex bags and the full opposite
   shore form `K_7`.  There are
   \[
                         7\cdot 7P6=35,280
   \]
   labelled templates.
2. **Two connected carriers.**  Keep the boundary `K_4`
   `\{0,1,2,z\}` and the opposite full shore.  Choose distinct
   `r_A,r_B in \{3,4,5\}` and disjoint nonempty connected sets
   `A,B subseteq D`.  Append `r_A` to `A` and `r_B` to `B`.  For
   `r=3,4,5`, respectively, require the carrier to contact
   \[
        \{1,2\},\qquad\{0,2\},\qquad\{0,1\}.       \tag{7.3}
   \]
   These are precisely the two members of `\{0,1,2\}` not adjacent to
   `r`.  The appended labels make the two carrier bags adjacent, while
   (7.3) makes both bags adjacent to the fixed boundary `K_4`.  Together
   with that `K_4` and the full shore they form `K_7`.  There are 11,592
   labelled support templates.

Connectivity of a proposed support is encoded exactly by requiring an
edge across every nontrivial bipartition of that support.  Every missing
`D` edge in the first template is checked simultaneously.  Negating all
46,872 templates gives

```text
type-A 35280 type-B 11592 residual unsat
```

Thus one of the displayed literal branch models exists.  The verifier is
a short standalone finite Boolean encoding; the trust boundary is Z3 and
the host Python runtime.  It uses no graph-minor oracle and does not assume
three-connectivity, so its hypotheses are weaker than those of the minimum
atom.  QED.

### Corollary 7.2 (new fragment-size bound)

The minimum `C6+K1` atom satisfies

\[
                              |D|\ge8.              \tag{7.4}
\]

### Proof

Corollary 4.5 gives `|D|>=7`.  At order seven, (7.1) is atomic surplus at
singletons and the singleton/full-body row bound.  Two-portal column
multiplicity is Corollary 2.1.  Lemma 7.1 gives `K_7`, a contradiction.
QED.

This closes the only bounded saturated exception in duplicating one common
literal row.  Any remaining common-row failure therefore exposes the exact
order-eight gate of that theorem; it cannot hide in a seven-vertex atom.
