# Singleton-thin reduction and the `M+13` packet-escape theorem

**Status:** proved and independently audited.  The identification of the two
boundary types is conditional on the frozen, audited 129-boundary census.

## 1. Setting

Let

\[
 V(G)=\{q\}\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `q` is anticomplete to `R` and `N(q)=S`.  Assume that `G` is not
six-colourable and every proper minor of `G` is six-colourable.  Put
`H=G[S]`.  In the exact `(1,2)` application, `R` contains two disjoint
connected `S`-full packets `P_1,P_2`.

## 2. The singleton-thin boundary collapse

Since `d(q)=7`, Dirac's neighbourhood inequality for a
7-contraction-critical graph gives

\[
                         \alpha(H)\le 7-7+2=2.       \tag{2.1}
\]

Among the 129 boundary graphs left by the already-audited adaptive `(1,2)`
census, exactly two have independence number at most two.  A targeted
isomorphism extraction from that frozen census identifies them as

\[
                         M\quad\hbox{and}\quad M+13, \tag{2.2}
\]

where

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Thus (2.2) is a conditional consequence of membership in the frozen
129-graph residual, not a classification of all seven-vertex graphs with
independence number two.

## 3. The unique safe state of `M+13`

Assume henceforth that `H=M+13`.  Its unique proper equality partition of
packet demand at most two is

\[
 \Pi^*=\{0\}\mid\{1\}\mid\{3\}\mid\{2,5\}\mid\{4,6\}. \tag{3.1}
\]

Indeed `0,1,3` form a triangle and `25,46` are nonedges, so the demand of
(3.1) is `5-3=2`.  Uniqueness is a finite boundary fact checked by the
existing exhaustive partition enumeration.

## 4. Exact trace and Kempe escape

Contract the connected star `q union {2,5}`.  Six-colour the resulting
proper minor and expand the independent literal block `25` only on
`G[R union S]=G-q`.  Fullness of `q` makes `25` an exact boundary block.

All six colours must occur on `S`: otherwise a colour absent from `S` can
be assigned to `q`, six-colouring `G`.  Hence the five remaining vertices
`0,1,3,4,6` are singleton blocks of five distinct colours.  Apply the exact
singleton-block Kempe exchange to the nonedge `46`.  Either

1. a swap merges exactly `4,6`, producing (3.1), after which the sixth
   colour absent from `S` again colours `q`; or
2. there is a literal `4-6` bichromatic path whose internal vertices lie
   in `R`.

The first outcome contradicts the choice of `G`.  Thus every exact `25`
trace returns the path outcome.

Symmetrically, contracting `q union {4,6}` forces an exact `46` block and
returns a literal `2-5` bichromatic path with interior in `R`.

## 5. Packet escape gives a literal `K_7`

Let `X` be the internal vertex set of a returned `4-6` path.  If

\[
                         X\cap(P_1\cup P_2)=\varnothing,
\]

then the following are seven literal clique branch sets:

\[
 \{1\},\ \{2\},\ \{6\},\ \{3,q\},\
 \{5\}\cup P_1,\ P_2,\ \{0,4\}\cup X.             \tag{5.1}
\]

The first three form the triangle `126`.  The last branch set is connected
through `04` and the `4-6` path, and its final path edge meets `{6}`.
Fullness of `q,P_1,P_2`, together with the displayed boundary anchors,
supplies every remaining adjacency.  In particular no edge between
`P_1,P_2` is assumed: `P_2` sees the literal `5` in the other packet bag.

For a returned `2-5` path with internal set `Y` disjoint from both packets,
the symmetric seven bags are

\[
 \{3\},\ \{4\},\ \{5\},\ \{1,q\},\
 \{6\}\cup P_1,\ P_2,\ \{0,2\}\cup Y.             \tag{5.2}
\]

Here `345` is the singleton triangle and the final path edge meets `{5}`.
Thus either escape produces a literal `K_7` model.

## 6. Exact residue

In a `K_7`-minor-free survivor:

* every `4-6` path returned from an exact `25` trace meets
  `P_1 union P_2`; and
* every `2-5` path returned from an exact `46` trace meets
  `P_1 union P_2`.

The paths arise from possibly different six-colourings.  Nothing here makes
them simultaneous, disjoint from one another, incident with both packets,
or confined to the same packet.  The remaining packet-escape theorem must
use a proper-minor transition or internal packet geometry.
