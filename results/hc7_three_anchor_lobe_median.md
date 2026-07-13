# The lobe-median exchange at a three-anchor obstruction

## Status

This is a proved local exchange theorem for the sharp three-anchor branch.
It does not infer an actual cut from row-label ownership.  Instead it
compares two literal reassignments of one detachable row lobe.  Every
ownership pattern gives a `K_7`, a `K_7^-`, or a missing-star model with
at most two holes, except for one exact pattern.  In that sole pattern the
same vertices form `K_7` minus two independent edges, so two disjoint
repair packets give a literal `K_7` and failure is an exact four-terminal
two-path/web input.

The theorem is insensitive to the order or size of the lobe and of all
seven bags.  It is therefore suitable after a three-point sector
transversal has exposed a detachable nonsingleton row lobe.

## 1. Literal setting and minimality

Let

\[
                     A,D,F,R_1,R_2,R_3,R_4                 \tag{1.1}
\]

be pairwise disjoint connected bags.  Every pair is adjacent except
possibly `AD`, and assume `AD` is genuinely absent.  Thus (1.1) is a
labelled one-hole near-`K_7` model with centre `A` and missed twin `D`.

Let `L` be a nonempty proper subset of `F` for which both `G[L]` and
`G[F-L]` are connected.  Write `F_0=F-L`.  Assume

\[
              L\sim A,\qquad L\sim D,\qquad F_0\sim A.     \tag{1.2}
\]

For `Q in {D,R_1,R_2,R_3,R_4}`, say that `L` **owns** `Q` if every
actual edge of `G` between `F` and `Q` has its `F`-end in `L`.  Put

\[
 \Omega(L)=\{Q:L\text{ owns }Q\},\quad
 d={\bf1}_{D\in\Omega(L)},                               \tag{1.3}
\]

and

\[
 o=|\Omega(L)\cap\{R_1,R_2,R_3,R_4\}|,
 \qquad
 k=|\{i:L\sim R_i\}|.                                   \tag{1.4}
\]

Every owned neutral row is met by `L`, so `o<=k`.

The only minimality hypothesis used below is the standard detachable-part
condition

\[
                         |\Omega(L)|=d+o\ge2.             \tag{1.5}
\]

For completeness, (1.5) follows in the no-`K_7` branch if `F` is
minimal in a comparison class which permits every nonmissed row `R_i`
to be enlarged by a detachable part of `F`.  If `L` owns no row, delete
it from `F`.  If its sole owner is `R_i`, move it into `R_i`; an actual
`L-R_i` edge connects the enlarged row, an edge across `L|F_0` restores
`F_0-R_i`, and all other required model edges survive.  If its sole owner
is `D`, moving it into `D` uses `L-D`, repairs `AD` through `L-A`, and
restores `D-F_0` across the cut, giving a literal `K_7`.  Thus no
target-free member of this permitted-transfer comparison class has at
most one owner.  Alternatively, (1.5) may simply be retained as an
explicit hypothesis.
Either operation strictly decreases `F`.

## 2. The two complementary models

### Lemma 1 (rotation model)

The seven bags

\[
                A,\quad D\cup L,\quad F_0,
                \quad R_1,R_2,R_3,R_4                    \tag{2.1}
\]

are connected and pairwise adjacent except exactly for

\[
                 \{F_0R_i:R_i\in\Omega(L)\}.             \tag{2.2}
\]

In particular (2.1) has exactly `o` missing pairs, all incident with the
single centre `F_0`.

#### Proof

The enlarged bag `D union L` is connected through `L-D`, and `F_0` is
connected by hypothesis.  An edge across `L|F_0` gives
`(D union L)-F_0`; an `A-L` edge repairs the old missing pair `AD`;
and `F_0-A` is retained by (1.2).  Every adjacency not incident with
`F` survives.  For a neutral row `R_i`, the residual bag `F_0` loses
its old edge to `R_i` precisely when all old `F-R_i` edges had their
`F`-ends in `L`, which is exactly ownership.  No other pair can be
missing.  \(\square\)

### Lemma 2 (median model)

Put `X=A union F_0` and `Y=L`.  The seven bags

\[
                    X,\quad Y,\quad D,
                    \quad R_1,R_2,R_3,R_4                \tag{2.3}
\]

are connected and pairwise adjacent except exactly for

\[
       \{XD:D\in\Omega(L)\}
       \ \cup\
       \{YR_i:L\not\sim R_i\}.                           \tag{2.4}
\]

Consequently (2.3) has at most `d+4-k` missing pairs.

#### Proof

The bag `X` is connected through the retained edge `A-F_0`; `Y` is
connected by hypothesis; and the edge across `L|F_0` gives `XY`.
The pairs `YD` and `XR_i` exist through `L-D` and the old `A-R_i`
edges.  The bags `D,R_1,...,R_4` retain their old clique adjacencies.

Because `A-D` is absent, `XD` exists exactly when `F_0-D` exists.  The
latter fails exactly when `D` is owned by `L`.  Finally `YR_i` exists
exactly when `L` meets `R_i`.  These are all pairs, proving (2.4).
\(\square\)

## 3. Exact amplification

### Theorem 3 (lobe-median defect dichotomy)

Under (1.1)--(1.5), one of the following holds.

1. The rotation model (2.1) is a literal missing-star near-`K_7` model
   with at most two missing spokes.
2. The median model (2.3) is a literal `K_7` or `K_7^-` model.
3. After relabelling the neutral rows, the exact exceptional state is

   \[
     D,R_1,R_2,R_3\in\Omega(L),\qquad
     L\sim R_1,R_2,R_3,\qquad L\not\sim R_4,             \tag{3.1}
   \]

   and (2.3) is `K_7` minus the two independent edges

   \[
                              XD,\qquad YR_4.             \tag{3.2}
   \]

There is no other multi-row residue.

#### Proof

If `o<=2`, Lemma 1 gives outcome 1.  Suppose `o>=3`.  Then `k>=o>=3`.
If `d=0`, Lemma 2 has at most `4-k<=1` missing pairs, giving outcome 2.
If `d=1` and `k=4`, Lemma 2 has at most one missing pair, again giving
outcome 2.

The only remaining numerical possibility is `d=1` and `k=3`.  Since
`3<=o<=k`, we have `o=k=3`.  Relabel the met neutral rows as
`R_1,R_2,R_3`.  Lemma 2 then says that the only missing pairs are
`XD` and `YR_4`.  They are independent because the seven bags in (2.3)
are disjoint.  This is precisely (3.1)--(3.2).  \(\square\)

The complementarity is the point of the theorem.  Many owned neutral
rows make the rotation model poor but force `L` to meet many rows, which
makes the median model good.  Only `3+1` ownership/contact balance leaves
two defects, and those defects have fixed independent endpoints.

### Corollary 3.1 (the exact `K_3 join C_4` carrier)

In outcome 3, the common rows `R_1,R_2,R_3` form the `K_3` side and

\[
                            X-Y-D-R_4-X                   \tag{3.3}
\]

is the literal `C_4` side of a `K_3 join C_4` minor model.  Its two
missing diagonals are exactly (3.2).

#### Proof

The three common rows are pairwise adjacent and, by Lemma 2, each is
adjacent to all four bags in (3.3).  The four displayed cycle edges are
respectively the `X-Y` cut edge, the assumed `Y-D` edge, the old
`D-R_4` row edge, and the old `R_4-A` edge contained in `R_4-X`.
Lemma 2 says that the only absent pairs among the four cycle bags are its
two diagonals.  \(\square\)

Thus the sole residue is not another arbitrary portal pattern.  It is
the precise expanded `K_3 join C_4` carrier for which two disjoint
repair packets close both diagonals.  If those packets fail, it is ready
for a set-root web or guarded-cycle analysis once the required fixed
connector or actual adhesion is supplied; the carrier alone is not yet a
rural or two-apex conclusion.

## 4. The exceptional state is an exact packet/linkage input

### Lemma 4 (two-packet promotion)

In outcome 3, suppose there are disjoint connected sets `K_1,K_2`, each
disjoint from the seven bags in (2.3), such that

\[
           K_1\sim X,D,
           \qquad
           K_2\sim Y,R_4.                                \tag{4.1}
\]

Then `G` has a literal `K_7` minor.

#### Proof

Replace `X` by `X union K_1` and `Y` by `Y union K_2`.  The two enlarged
bags are connected, remain disjoint from each other and from the other
five bags, and (4.1) repairs exactly the two absent pairs in (3.2).
Every old adjacency survives.  The seven resulting bags are therefore a
literal `K_7` model.  \(\square\)

Equivalently, two vertex-disjoint paths joining the bag pairs `X-D` and
`Y-R_4`, with interiors outside the seven displayed bags, supply the two
packets.  If such paths do not exist, the obstruction is no longer an
unbounded row-support pattern: it is the exact four-terminal two-path
problem

\[
                         (X,D;Y,R_4).                    \tag{4.2}
\]

This is a literal set-to-set two-linkage input.  Once a fixed connector
or actual adhesion containing its four portal sets is supplied, a
set-root or guarded-cycle web analysis may be applied.  In an actual
adhesion, a web-side failure must be used to construct the three boundary
blocks of the opposite partition-carrier splice; agreement only on the
four row labels is insufficient.

## 5. Three-anchor use

Suppose a sharp packing/transversal argument has exposed a detachable
row lobe `L` whose skeleton neighbourhood is a three-point set.  If the
two internal gates to `F-L` and the actual foreign contact vertices give
`|N_G(L)|<=6`, they are already an actual forbidden separator in a
seven-connected host.  Otherwise contact counting alone is exhausted.

When the rich-contact lobe meets the currently missed twin and `F-L`
retains its centre contact, Theorem 3 is the correct amplification:
arbitrarily many contacts inside nonsingleton rows collapse either to a
missing-star near model with at most two spokes, to `K_7^-`, or to the
single protected two-path state (4.2).  Thus no further enumeration of
row support patterns is needed at this lobe.

The theorem does not claim that seven-connectivity alone supplies the
two packets in Lemma 4, or that the displayed carrier itself supplies a
web.  A two-linkage failure inside a produced connector can be a web
rather than a small cut.  The remaining HC7 input must first produce that
connector or actual adhesion and then use its proper-minor state, exactly
as in the guarded cyclic-shore partition-carrier theorem.
