# Removable fans give state-aligned covering splits

## 1. The distinction which the local list calculation must retain

Let \(G\) have an exact adhesion \(L\), and let \(D\) and \(D^*\) be
two connected shores of \(G-L\), each full to \(L\).  Suppose that
\(D\) contains a removable outer fan

\[
 F=x_1\cdots x_m
\]

with common neighbour \(h\in D-F\).  Here "removable" means the usual
triangulated-disk configuration: \(D-F\) is connected, every \(x_i\)
is adjacent to \(h\), consecutive fan vertices are adjacent, and the
only shore neighbours of an interval of \(F\), apart from \(h\), are
its two possible outer-path neighbours.

Fix an \(r\)-colouring \(c\) of \(G-F\).  Its extension over \(F\) is
the path-list problem

\[
 A_i=\Omega-c(N_G(x_i)-F),\qquad |\Omega|=r.
 \tag{1.1}
\]

Put

\[
 R_1=A_1,\qquad
 R_i=\{\gamma\in A_i:R_{i-1}\not\subseteq\{\gamma\}\}.
 \tag{1.2}
\]

The complete recurrence has up to \(2^r\) subset states, including the
empty failure state.
Only after a reachable set becomes a singleton does a non-resetting
suffix run through the \(r\) forced-colour states.  Thus, for \(r=6\),
the phrase "six-state automaton" is correct only for that deterministic
suffix, not for the extension relation of the shore and not even for the
whole path recurrence.

There is a second, more important distinction.  Failure to extend this
particular colouring \(c\) does not say that the equality state induced
by \(c|_L\) is absent from the shore's extension family: another colouring
of \(G-F\), inducing the same state on \(L\), may use a different colour
on \(h\) and extend.  Section 4 gives the smallest such Moser example.

## 2. The fan-interval split lemma

### Lemma 2.1 (connected interval split)

For every nonempty interval

\[
 I=\{x_p,x_{p+1},\ldots,x_q\}\subseteq F,
\]

the partition

\[
 D=I\mathbin{\dot\cup}(D-I)
 \tag{2.1}
\]

has two connected, adjacent parts.  Moreover

\[
 |N_D(I)-I|\le 3.
 \tag{2.2}
\]

#### Proof

The interval is connected along the outer path.  The graph \(D-F\) is
connected and contains \(h\).  Every vertex of \(F-I\) is adjacent to
\(h\), so \(D-I\) is connected.  The edge from any vertex of \(I\) to
\(h\) makes the two parts adjacent.  Finally, the shore neighbours of
\(I\) outside \(I\) are contained in \(\{h,x_{p-1},x_{q+1}\}\), with a
missing symbol at an end of the fan interpreted as the corresponding
outer corner.  This proves (2.2). \(\square\)

### Lemma 2.2 (covering quotient)

Let \(J=G[L]\), and contract \(D^*\) to \(z\), \(I\) to \(x\), and
\(D-I\) to \(y\).  There is a partition \(P\dot\cup(L-P)=L\) such that
the resulting minor contains the quotient consisting of

* \(J\) on \(L\);
* \(z\) complete to \(L\);
* the edge \(xy\);
* \(x\) adjacent to every label in \(P\); and
* \(y\) adjacent to every label in \(L-P\).

In particular, if \(G\) is \(K_t\)-minor-free, this is a covering
\(K_t\)-negative split of \(J\).

#### Proof

Fullness of \(D\) gives

\[
 N_L(I)\cup N_L(D-I)=L.
\]

Assign every label met by only one part to that part and assign a label
met by both parts arbitrarily.  This gives \(P\subseteq N_L(I)\) and
\(L-P\subseteq N_L(D-I)\).  Lemma 2.1 supplies connected branch sets and
the edge between them; fullness of \(D^*\) supplies the complete vertex
\(z\).  Delete surplus incidences after the three contractions.  The
quotient is a minor of \(G\), so it cannot contain a \(K_t\)-minor when
\(G\) does not. \(\square\)

### Lemma 2.3 (tight interval or surplus)

If \(G\) is \(k\)-connected, then

\[
 |N_L(I)|+|N_D(I)-I|=|N_G(I)|\ge k.
 \tag{2.3}
\]

If equality holds, \(N_G(I)\) is an exact \(k\)-cut.  Every component
behind it is full to that cut.  If the inequality is strict, the interval
split has genuine portal/interface surplus.

#### Proof

The opposite shore lies outside \(I\cup N_G(I)\), so \(N_G(I)\)
separates the nonempty interval \(I\) from a nonempty set.  Connectivity
gives (2.3).  Equality makes it a minimum cut.  A component behind a
minimum \(k\)-cut must meet every cut vertex, since otherwise the other
\(k-1\) cut vertices still separate it. \(\square\)

## 3. Exact state-aligned conversion

### Theorem 3.1 (forced chain to split or tight adhesion)

In the setting of Section 1, exactly one of the following happens for the
fixed colouring \(c\) of \(G-F\).

1. The recurrence (1.2) ends nonempty, and \(c\) extends over \(F\).
2. The recurrence fails, and there is a canonical nonempty fan interval
   \(I\) for which Lemma 2.2 gives a covering split.  If \(G\) is
   \(K_t\)-minor-free, that split is \(K_t\)-negative.  It either exposes
   the exact \(k\)-cut in Lemma 2.3 or has strict interface surplus.

#### Proof

The first alternative is the exact path recurrence.  Otherwise let \(j\)
be the first index with \(R_j=\varnothing\).  If \(j=1\) or
\(A_j=\varnothing\), take \(I=\{x_j\}\).  Lemmas 2.1--2.3 apply directly.

It remains that \(j>1\) and \(A_j\ne\varnothing\).  Then, for a unique
colour \(\alpha\),

\[
 R_{j-1}=A_j=\{\alpha\}.
 \tag{3.1}
\]

Trace backwards to the last reset, and let \(p\le j-1\) be the first
index of the resulting singleton run.  Take

\[
 I=\{x_p,\ldots,x_j\}.
\]

It is a nonempty interval canonically selected by the failed colouring.
Lemmas 2.1--2.3 give all assertions in the second alternative. \(\square\)

### Corollary 3.2 (minor-critical form)

Suppose \(G\) is non-\(r\)-colourable but every proper minor is
\(r\)-colourable.  Deleting \(F\) gives an \(r\)-colouring \(c\) of
\(G-F\), and it cannot extend.  Hence every removable outer fan in an
exact full-shore adhesion supplies a state-aligned covering split,
together with the tight-cut/surplus alternative of Lemma 2.3.  If \(G\)
is also \(K_t\)-minor-free, the split is a covering bad split; if its
quotient were positive instead, it would lift a \(K_t\)-minor.

This closes the *mixed deterministic-chain conversion*: a mixed chain is
not required to contain a repeated portal profile.  Its contiguous
support itself is the first branch set of the covering split.  What remains
is the already isolated covering-bad-split exchange problem; no additional
unbounded fan word remains.

## 4. An atomic warning: fixed-colouring failure is not state failure

Use the reserved Moser labels

\[
 U=\{0,2,4,5,6\},\qquad a=1,\qquad w=7,
\]

and the equality state

\[
 \{0,5\}\mid\{1,3\}\mid\{2,w\}\mid\{4\}\mid\{6\}.
 \tag{4.1}
\]

On a wheel \(W_5\), put the five ordinary rim profiles, in cyclic order,

\[
 02,03,13,14,24
 \tag{4.2}
\]

in the abstract missing-cycle coordinates used by the Moser scripts; the
hub sees \(a,w\).  Give the hub colour \(4\) and delete the two consecutive
rim vertices with profiles \(03,13\).  The other three rim vertices can be
coloured \(3,3,0\).  Both deleted vertices then have the singleton list
\(\{5\}\), so this fixed colouring does not extend.

Nevertheless the same boundary state extends over the whole wheel.  In
rim order a valid colouring is

\[
 (3,4,5,3,5),\qquad c(h)=0.
 \tag{4.3}
\]

Thus the failed local colouring cannot be promoted to a missing boundary
state.  The verifier `moser_fan_mixed_state_audit.py` checks (4.1)--(4.3)
and also finds all seven distinct-profile singleton collisions in the
thirty residual Moser trace families.

## 5. Scope

The theorem is label-free and does not use the special Moser profiles.
It converts every removable-fan failure into the same finite covering
split object already produced by the cyclic-hull theorem.  It does not by
itself eliminate a covering bad split with surplus interface.  That is the
next global exchange lemma, and confusing a fixed minor colouring with a
whole-shore extension state cannot be used to bypass it.

## 6. Exact Moser refinement of two and three fan vertices

The warning in Section 4 is also sufficiently rigid to obtain a sharper
Moser-specific conversion.  Across the thirty residual trace families,
there are exactly seven unordered pairs of *distinct* ordinary profiles
which can have the same singleton list:

\[
\begin{split}
 &(02,03),(02,14),(02,24),(03,13),\\
 &(03,24),(13,14),(14,24).
\end{split}
\tag{6.1}
\]

Combine two adjacent fan vertices carrying one of these pairs with a
covering full split of a crossed frame in the opposite shore.  There are

\[
 7\cdot5\cdot2^3=280
\tag{6.2}
\]

conservative quotients.  The exact connected-branch-set search in
`moser_mixed_fan_crossing_verify.cpp` gives the following complete atlas.

### Theorem 6.1 (atomic mixed-pair atlas)

Of the 280 quotients in (6.2), 272 contain a \(K_7\)-minor.  The eight
negative quotients all have the fan pair

\[
 (P_{02},P_{14}).
\tag{6.3}
\]

In every negative quotient, one crossing carrier contains the opposite
terminal \(b=3\) as a non-demanded contact.  If that contact can instead
be put on a third connected piece adjacent to both crossing carriers,
while the original carrier retains its demanded crossing pair, the
enlarged quotient contains a \(K_7\)-minor.

#### Verification

The program constructs the pure Moser boundary and apex, the two adjacent
fan vertices and their common connected body, and every covering split of
each opposite frame.  Its minor routine enumerates every nonempty connected
vertex set and then every disjoint pairwise-touching seven-tuple, so both
positive and negative answers are exhaustive.  It asserts exactly eight
negative cells.  For each of them it adds the third piece, moves only the
free \(b\)-contact, and verifies a \(K_7\)-model.  Its output ends with

```text
checked 280 mixed-fan/opposite-crossing quotients; negative 8
```

The eight sparse exceptions are in fact impossible in the critical graph.
The \(P_{14}\)-vertex has degree seven and has

\[
 \{a,5,6,w\}\subseteq N(x).
\]

Inside \(\{a,5,6\}\), the only missing edge is \(a5\).  If neither
\(aw\) nor \(5w\) were present, \(\{a,5,w\}\) would be an independent
triple in \(N(x)\), contrary to Dirac's
\(\alpha(N(x))\le2\).  Thus \(aw\) or \(5w\) is present.  The verifier
adds each of these edges separately and finds all eight quotients
\(K_7\)-positive.  Hence all seven atomic mixed collision pairs close.

The two outer-corner colours of a removable fan were not included in the
first ordinary-row atlas.  They can shrink an endpoint list, so a complete
two-vertex argument must check the three remaining unordered profile
pairs as well.  There are \(3\cdot5\cdot2^3=120\) quotients.  Exactly 32
sparse quotients are negative, all of profile type

\[
 (P_{02},P_{13})\quad\hbox{or}\quad(P_{13},P_{24}).
\tag{6.4}
\]

For a \(P_{13}\)-vertex the relevant boundary neighbours are
\(\{a,4,5,w\}\), and \(45\) is the only edge among \(\{a,4,5\}\).
Dirac therefore forces

\[
 aw\in E(G)\quad\hbox{or}\quad
 \{4w,5w\}\subseteq E(G).
\tag{6.5}
\]

Indeed, without \(aw\), the independent triples \(\{a,4,w\}\) and
\(\{a,5,w\}\) force \(4w\) and \(5w\), respectively.  The exact replay
adds the first alternative and the two edges of the second alternative;
both repairs are \(K_7\)-positive in every one of the 32 cells.  The third
remaining pair \((P_{03},P_{14})\) is positive without repair.

Together with the 200 same-profile certificates in
`fan_crossing_fullsplit_verify.py`, this proves:

### Theorem 6.2 (all ordinary two-fan profiles)

Two adjacent ordinary fan vertices, their common connected remainder, and
any covering split of an opposite crossed Moser frame contain a
\(K_7\)-minor in a 7-contraction-critical graph.

There is an even simpler stabilization at length three.  The same verifier
checks all

\[
 5^3\cdot5\cdot2^3=5000
\tag{6.6}
\]

ordered triples of ordinary profiles and opposite covering crossings.
Every sparse quotient is already \(K_7\)-positive; Dirac repair is not
needed.

### Theorem 6.3 (three-fan stabilization)

Three consecutive ordinary fan vertices, their common connected
remainder, and any covering split of an opposite crossed Moser frame
contain a \(K_7\)-minor.

The quotient uses the three fan vertices separately, the contracted
remainder adjacent to all three through the common fan neighbour, and the
two adjacent crossing pieces.  Thus every certificate lifts to the
original shore.

## 7. Complete removable-fan conversion in the Moser web cell

Assume now the full reserved Moser two-shore setting: the current shore
\(D\) is three-connected, full and relatively seven-connected; all five
of its frames are crossless; and the opposite shore is subject to the same
five-frame system.

### Lemma 7.1 (a triple lock is an exact seven-cut)

If \(x\in D\) has a triple-lock profile with shield label \(s\), so that
\(N_D(s)=\{x\}\), then

\[
 N_G(D-x)=\{x\}\cup(L-\{s\}).
\tag{7.1}
\]

In particular this is an exact seven-cut.

#### Proof

Three-connectivity makes \(D-x\) nonempty and connected.  Its shore
boundary inside \(D\) is exactly \(\{x\}\).  It misses the shield label
\(s\), while relative seven-connectivity gives

\[
 1+|N_L(D-x)|\ge7.
\]

Since \(|L|=7\), all other six labels occur, proving (7.1).  The opposite
shore lies beyond the displayed neighbourhood, so it is a seven-cut.
\(\square\)

### Theorem 7.2 (removable-fan closure)

Let \(F\) be a removable outer fan in \(D\).  Then one of the following
holds:

1. \(G\) contains a \(K_7\)-minor;
2. \(G\) is six-colourable; or
3. \(F\) exposes an exact seven-cut.

#### Proof

If a fan vertex is a triple lock, Lemma 7.1 gives outcome 3.  Hence assume
every fan vertex is ordinary.  Such a vertex has three shore neighbours
and exactly four boundary neighbours.

If \(|F|=1\), its seven neighbours form a seven-cut isolating it from the
opposite shore, giving outcome 3.  Suppose \(|F|\ge2\), and choose two
consecutive fan vertices.  Their complement in \(D\) is connected and is
adjacent to both through the common fan neighbour.

If the opposite five-frame society is crossless, the bilateral
all-crossless web-gluing theorem six-colours \(G\), giving outcome 2.
Otherwise it has a crossed frame.  Extend its two carriers to a covering
connected split.  Theorem 6.2 applied to the chosen adjacent fan pair gives
outcome 1. \(\square\)

This theorem is stronger than the proposed forced-chain conversion.  Once
the geometric fan is present, the colouring automaton is unnecessary:
two ordinary fan vertices close against a crossing, bilateral
crosslessness closes by web gluing, and every remaining one-vertex or
triple-lock case is a tight adhesion.  The non-wheel planar-core route is
therefore reduced from arbitrary deterministic words to the *removable
singleton* alternative of the canonical disk reduction and to recursion
across the exact seven-cuts in outcome 3.
