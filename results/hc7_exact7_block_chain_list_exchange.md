# Exact-seven block-chain list exchange

## 1. Frozen setting

Assume the audited exact-seven `(1,3)` two-lobe setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `G` is seven-connected and strongly seven-contraction-critical,
there are no `LR` edges, and `R` contains three pairwise disjoint connected
`S`-full packets.  Assume explicitly that `G[L]` is three-connected.  Let
`T={t_i,t_j,t_k}` be a three-cut of `G[L]`, and let `J,K` be the two
components of `G[L]-T`.

Fix a spanning `T`-rooted triangle

\[
                  (B_i,B_j,B_k)
\]

in `G[K union T]`.  Suppose its literal portal matching rank is two, and
choose distinct representatives

\[
        p_j\in N_S(B_j),\qquad p_k\in N_S(B_k).          \tag{1.1}
\]

Thus `B_i` is the unmatched rooted bag for this chosen matching; put
`F={p_j,p_k}`.  The audited block-chain theorem says that, in a
`K_7`-minor-free survivor, the block--cutvertex tree of `J` is a path.

This note proves a uniform exchange along that path.  Every noncrossed
cut closes by a literal `K_7`.  If the path has any cutvertex at all,
all surviving cuts have one common orientation

\[
                 \{i,j\}\mid\{i,k\},                   \tag{1.2}
\]

the common gate `t_i` has no literal boundary portal, and the whole path
induces a monotone sequence of uncolourable exact proper-minor list states.
This is an infinite-family reduction to one ordered state sweep, not a
finite list of labelled cases.

## 2. Fresh labels across a lobe cut

We first isolate the small Hall calculation which makes the exchange
literal.

### Lemma 2.1 (two fresh representatives)

Let `X,Y subseteq S` satisfy

\[
       |X|\ge3,\qquad |Y|\ge3,\qquad |X\cup Y|\ge4.
\]

For every two-set `F subseteq S`, there are distinct

\[
                     x\in X-F,\qquad y\in Y-F.          \tag{2.1}
\]

#### Proof

Neither `X-F` nor `Y-F` is empty.  If the two sets did not have an SDR,
Hall's theorem for a two-set family would give
`|(X union Y)-F|<=1`.  Then `|X union Y|<=3`, a contradiction. `square`

Let `z` be a cutvertex of `J`, and let `A,D` be the two components of
`J-z`.  There are exactly two by the audited nested-cutvertex exchange.
Put

\[
                     U_A=N_T(A),\qquad U_D=N_T(D).       \tag{2.2}
\]

Three-connectivity of `G[L]` gives

\[
                         |U_A|,|U_D|\ge2.                \tag{2.3}
\]

Moreover, every exit from `A` in `G` lies in
`{z} union U_A union N_S(A)`.  Deleting this set separates `A` from the
opposite lobe and the nonempty opposite open shore.  Hence

\[
             |N_S(A)|\ge 6-|U_A|\ge3,                  \tag{2.4}
\]

and the same estimate holds for `D`.  Finally,
`|N_S(J)|>=4`, since `T union N_S(J)` separates `J`.  Consequently the
two connected sides in either partition

\[
                 A\mid(D\cup\{z\}),\qquad
                 (A\cup\{z\})\mid D                    \tag{2.5}
\]

have contact sets satisfying Lemma 2.1: each has order at least three,
and their union is `N_S(J)`, of order at least four.

## 3. Every noncrossed cut closes

### Theorem 3.1 (cut-duty exchange)

If, after possibly interchanging `A,D`,

\[
                       i\in U_A,
             \qquad \{j,k\}\subseteq U_D,              \tag{3.1}
\]

then `G` contains a literal `K_7` minor.

#### Proof

Use the connected partition

\[
                         X=A,\qquad Y=D\cup\{z\}.
\]

It has an `XY` edge, `X` has a neighbour at `t_i`, and `Y` has neighbours
at both `t_j,t_k`.  By Lemma 2.1 and (2.5), choose distinct labels

\[
          a\in N_S(X)-F,\qquad b\in N_S(Y)-F.            \tag{3.2}
\]

The four sets

\[
             B_i\cup X,\qquad B_j,\qquad B_k,\qquad Y  \tag{3.3}
\]

are disjoint connected pairwise adjacent carriers.  The first three retain
the old rooted-triangle adjacencies.  The last carrier is adjacent to
`B_i union X` through the `XY` edge, to `B_j` through a `Yt_j` edge, and
to `B_k` through a `Yt_k` edge.  They have the four distinct literal
representatives `a,p_j,p_k,b`.

Enlarge these four carriers by their representatives, and anchor the three
disjoint `S`-full packets in `R` at the remaining three vertices of `S`.
Packet fullness supplies all packet--carrier and packet--packet edges, so
the seven bags form a literal `K_7` model. `square`

### Corollary 3.2 (only crossed cut signatures survive)

At a cutvertex of a `K_7`-minor-free survivor, both `U_A,U_D` have order
exactly two, and their ordered pair is one of

\[
\begin{split}
 & (\{i,j\},\{i,k\}),\quad
   (\{i,k\},\{i,j\}).                                  \tag{3.4}
\end{split}
\]

#### Proof

If one support is all of `T`, then the other support, which has order at
least two, either contains `i` or equals `{j,k}`.  In the first case use
the other side for `X` in Theorem 3.1; in the second use the `T`-side.
Thus neither support is `T`.

There are three two-subsets of `T`.  Theorem 3.1 excludes a pair in which
one side contains `i` and the other is `{j,k}`.

It remains to exclude equal supports.  Suppose

\[
                         U_A=U_D=T-\{g\}.
\]

The lobe `J` meets every literal gate.  Since neither open component meets
`t_g`, the edge `zt_g` is literal.  If `g=i`, use the connected partition

\[
                      X=A\cup\{z\},\qquad Y=D;
\]

then `X` meets `t_i` and `Y` meets both `t_j,t_k`.  If `g=j` or `g=k`,
use `X=A`, `Y=D union {z}`; the latter side meets the omitted gate through
`z` and the other required gate through `D`.  In every case the two parts
have contact sets of order at least three whose union is `N_S(J)`, of
order at least four.  Lemma 2.1 supplies two fresh representatives avoiding
`F`, and the four-carrier construction in Theorem 3.1 gives a literal
`K_7`.  Thus equal supports are impossible, leaving exactly (3.4).
`square`

This is the point where the unmatched root matters.  The statement does
not assert the same signature for three different choices of unmatched
bag.

## 4. Nested supports force one global crossed order

List the cutvertices of the block-chain `J` in their linear order as

\[
                         z_1,\ldots,z_r.
\]

For each `h`, let `A_h` be the component of `J-z_h` on the left and `D_h`
the component on the right.  If `h<ell`, then

\[
                  U_{A_h}\subseteq U_{A_ell},
          \qquad U_{D_ell}\subseteq U_{D_h}.             \tag{4.1}
\]

Indeed, the earlier left component is contained in the later one, and the
later right component is contained in the earlier one.

### Theorem 4.1 (canonical crossed-chain theorem)

If `r>=1`, then, after possibly reversing the block-chain and interchanging
`j,k`,

\[
                U_{A_h}=\{i,j\},\qquad
                U_{D_h}=\{i,k\}qquad(1\le h\le r).     \tag{4.2}
\]

In particular,

\[
\begin{aligned}
 N_J(t_j)&\subseteq A_1\cup\{z_1\},\\
 N_J(t_k)&\subseteq D_r\cup\{z_r\},                    \tag{4.3}
\end{aligned}
\]

while both open tails at every cut contain a neighbour of `t_i`.

#### Proof

All supports in (4.1) have order two by Corollary 3.2.  The inclusions
therefore force all left supports to equal one fixed two-set `P`, and all
right supports to equal one fixed two-set `Q`.  Corollary 3.2 says directly
that `P,Q` are the two distinct sets `{i,j}`, `{i,k}`.  Reverse the chain
or interchange `j,k` if necessary to obtain (4.2).  Formula
(4.3) follows at the first and last cuts, and the last assertion is part
of (4.2). `square`

Thus an arbitrarily long block chain has no drifting gate pattern.  Its
two outer gate classes have one fixed order, and the unmatched class
crosses every actual articulation.

## 5. The common gate is literally unlabelled

The crossed order yields four clique carriers without using the rooted
triangle.

### Theorem 5.1 (labelled common-gate closure)

Suppose one cut has the crossed signature

\[
                         U_A=\{i,j\},\qquad
                         U_D=\{i,k\}.                    \tag{5.1}
\]

If `N_S(t_i)` is nonempty, then `G` contains a literal `K_7` minor.

#### Proof

The four sets

\[
 A\cup\{z,t_j\},\qquad D\cup\{t_k\},
             \qquad K,\qquad\{t_i\}                    \tag{5.2}
\]

are disjoint and connected.  Their six pairwise adjacencies have literal
witnesses:

* the first two meet through an edge from `z` to `D`;
* the first and third meet through the contact of `K` with `t_j`;
* the second and third meet through the contact of `K` with `t_k`;
* the first and fourth meet through an `At_i` edge;
* the second and fourth meet through a `Dt_i` edge; and
* the third and fourth meet through a `Kt_i` edge.

The first two carriers each contact at least three boundary vertices by
(2.4), and `K` contacts at least four.  The last carrier has a boundary
contact by hypothesis.  Four sets of respective lower bounds
`3,3,4,1` have an SDR: every subfamily not using the singleton set has
union of order at least its size, adjoining the singleton preserves the
same inequalities, and the full union has order at least four because of
`N_S(K)`.  Therefore the four carriers have four distinct literal
representatives.  The usual three-packet lift gives a literal `K_7`.
`square`

### Corollary 5.2

In a surviving crossed chain,

\[
                             N_S(t_i)=\varnothing.       \tag{5.3}
\]

This is a literal conclusion about the common gate vertex, not a statement
that some palette colour is absent from a model bag.

## 6. The exact monotone list-state sweep

For every cut `z_h`, define a spanning three-carrier partition of the thin
shore by

\[
\begin{aligned}
 C_j^h&=A_h\cup\{z_h,t_j\},\\
 C_k^h&=D_h\cup\{t_k\},\\
 C_i  &=K\cup\{t_i\}.                                  \tag{6.1}
\end{aligned}
\]

Connectivity follows from (4.2).  The first two carriers are adjacent
through a `z_hD_h` edge; their adjacencies to `C_i` are witnessed through
the literal gates `t_j,t_k`.  Thus (6.1) is a spanning partition of `L`
into three connected pairwise adjacent carriers.

Let

\[
 \Lambda_h(s)=\{q\in\{i,j,k\}:N_G(s)\cap C_q^h\ne\varnothing\}.
                                                               \tag{6.2}
\]

Each list is nonempty because the connected thin shore `L` is `S`-full.
Moreover every palette colour occurs in at least four lists: (2.4) gives
the bound four for each tail because its gate support has order two, and
`|N_S(K)|>=4` gives it for colour `i`.

### Theorem 6.1 (monotone exact-state dichotomy)

For every `h`, either

1. `G` is six-colourable; or
2. `(G[S],Lambda_h)` is an uncolourable nonempty three-palette list
   instance.

In a hypothetical counterexample only outcome 2 occurs.  As `h` increases,
the support of colour `j` is monotone nondecreasing, the support of colour
`k` is monotone nonincreasing, and the support of colour `i` is fixed.

#### Proof

If `G[S]` has a proper colouring `phi(s) in Lambda_h(s)`, apply the audited
spanning-triangle list-state theorem to the three carriers in (6.1).  It
contracts each independent colour block into its selected carrier on one
side and into distinct full packets on the other, producing the same exact
boundary equality partition from two proper minors.  After a palette
permutation the two six-colourings glue, so `G` is six-colourable.

For monotonicity, `A_h union {z_h}` is nested increasingly along the
block-chain, while `D_h` is nested decreasingly.  The carrier `C_i` does
not change.  Literal contact with a nested carrier has the same
monotonicity, proving the last assertion. `square`

One may also allocate `z_h` to the right carrier instead.  This gives the
second exact state

\[
 A_h\cup\{t_j\},\qquad D_h\cup\{z_h,t_k\},\qquad C_i,   \tag{6.3}
\]

which differs only by transferring the literal contact set `N_S(z_h)`
between colours `j,k`; it too must be uncolourable in a survivor.

## 7. What this discharges and what remains

The theorem closes, by explicit bags, every rank-two block-chain cut whose
gate duties are not crossed.  It also proves that crossed signatures cannot
drift along an arbitrarily long chain and closes the entire subfamily in
which the common gate has a literal boundary portal.  The residual is one
canonical object:

* one fixed unmatched gate `t_i`, with no `S`-neighbour;
* one left class `{i,j}` and one right class `{i,k}` at every articulation;
  and
* a monotone family of exact uncolourable list states (6.2), including both
  allocations (6.1) and (6.3) at every cut.

This is the promised block-terminal order at literal carrier level.  The
remaining operation-state theorem must show that such a monotone sweep
cannot stay uncolourable, or that its persistent implication conflict is
carried by one globally coherent two-vertex endgame.  This note does not
infer that endgame merely from the crossed order, and it makes no claim for
a maximum rooted-triangle portal rank below two.
