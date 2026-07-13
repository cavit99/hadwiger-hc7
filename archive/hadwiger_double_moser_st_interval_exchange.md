# The (st)-interval exchange in the 2-connected double-Moser body

## 1. Purpose and hypotheses

Use the double-Moser notation

\[
 H_1=\{x_1,x_2\},\qquad H_2=\{x_3,x_4\},
\]

with old outer edge (ab), new outer edge (pq), and centres (u,v).
The vertex (a) sees (H_1), (b) sees (H_2), (q) sees
(H_1), and (p) sees (H_2).

The cutvertex theorem in
`hadwiger_double_moser_cutvertex_exchange.md` reduces the live branch to
a 2-connected body.  The small outer-portal lemma discussed in Section 7
below upgrades this to a 2-connected common exterior

\[
                         C=\{a,b\}\cup R.                       \tag{1.1}
\]

This note extracts the exact interval invariant of an (ab)
(st)-numbering.  It proves the following substantive fact.

> While both (p) and (q) have contacts on both sides, a transition
> between two quotient-negative rank-two split states changes exactly one
> held root label for one missing root label.  Any larger transition is a
> root-rich third carrier and gives a (K_7)-minor.

The conclusion converts the six maximal negative rows into the bases of
(U_{2,4}).  It does not eliminate the final low-rank gap or the final
two-exchange web.

## 2. Connected prefix and suffix carriers

Fix an (st)-numbering

\[
                  z_1=b,z_2,\ldots,z_{n-1},z_n=a                \tag{2.1}
\]

of (C) with respect to the edge (ba).  Thus every internal vertex has
both an earlier and a later neighbour.  Put

\[
 L_i=C[\{z_1,\ldots,z_i\}],\qquad
 U_i=C[\{z_{i+1},\ldots,z_n\}]                  \tag{2.2}
\]

for (1\le i<n).

### Lemma 2.1

Every (L_i) and (U_i) is connected.

#### Proof

Starting from an internal vertex and repeatedly taking an earlier
neighbour eventually reaches (b), without leaving its prefix.  Repeated
later neighbours similarly reach (a) inside the suffix.  \(\square\)

Consequently every cut in (2.2) is a covering connected split of the
common exterior, with (b) on the lower side and (a) on the upper side.

## 3. Four monotone root intervals

Define the reverse-root state at cut (i) by

\[
\begin{aligned}
 B_i={}&\{j\in\{1,2\}:N_{L_i}(x_j)\ne\varnothing\}\\
 &\cup\{j\in\{3,4\}:N_{U_i}(x_j)\ne\varnothing\}.
                                                               \tag{3.1}
\end{aligned}
\]

The first two coordinates are nondecreasing in (i), and the last two
are nonincreasing.  Fullness of (R) to (X), together with the fixed
outer contacts, gives

\[
                         B_1=\{3,4\},\qquad
                         B_{n-1}=\{1,2\}.                       \tag{3.2}
\]

For (j\in\{1,2\}), let (f_j) be the first index of an (x_j)-portal
in the order.  For (j\in\{3,4\}), let (ell_j) be the last such index.
Then coordinate (j\le2) enters immediately after (f_j), while
coordinate (j\ge3) leaves immediately after (ell_j).

The same notation for (s\in\{p,q\}) gives its first and last portal
indices (f_s,ell_s).  Both sides of cut (i) meet (s) exactly when

\[
                         f_s\le i<\ell_s.                       \tag{3.3}
\]

Call

\[
 J_P=\{i:\max(f_p,f_q)\le i<\min(\ell_p,\ell_q)\}             \tag{3.4}
\]

the **two-sided (P)-corridor**.  An event vertex (z_k) is strictly
inside this corridor when both cuts (k-1,k) belong to (J_P).

## 4. The ten-row atlas becomes rank two

The exact connected-split atlas has ten maximal negative states.  Four of
them have (p,q) both exclusively on one side:

\[
 0111\mid22,\quad1011\mid22,\quad
 1101\mid11,\quad1110\mid11.                    \tag{4.1}
\]

They cannot contain a cut in (J_P).  The remaining six are

\[
\begin{array}{ccc}
0011\mid33,&0101\mid33,&0110\mid33,\\
1001\mid33,&1010\mid33,&1100\mid33.
\end{array}                                                     \tag{4.2}
\]

### Lemma 4.1 (rank-two form)

For (i\in J_P), the split quotient has a (K_7)-minor whenever

\[
                             |B_i|\ge3.                          \tag{4.3}
\]

If it is negative, its state is contained in one of the six rows (4.2),
so (|B_i|\le2).  A maximal negative state with two reverse-root
contacts is therefore precisely a basis of (U_{2,4}).

#### Proof

The (P)-coordinates of a cut in (J_P) are (33).  Hence no state in
(4.1) can dominate it.  Every maximal negative state still available is
one of (4.2), and each has exactly two root bits.  Conversely the explicit
three-cross certificate in
`hadwiger_double_moser_edge_exchange.md`, Theorem 5.1, gives a hand
(K_7)-model for (4.3).  \(\square\)

## 5. A transition is atomic or root-rich

For an event vertex (z_k), define

\[
 G_k=B_k-B_{k-1}\subseteq\{1,2\},\qquad
 D_k=B_{k-1}-B_k\subseteq\{3,4\}.                \tag{5.1}
\]

Every label in (G_k\cup D_k) is genuinely adjacent to (z_k): a gained
label has its first lower-side portal there, and a dropped label has its
last upper-side portal there.

### Theorem 5.1 (atomic basis exchange)

Suppose (z_k) is strictly inside the two-sided (P)-corridor, and both
(B_{k-1},B_k) are quotient-negative bases of order two.  Then exactly
one of the following holds.

1. (G) contains a (K_7)-minor.
2. The transition is a one-for-one exchange:

   \[
                         |G_k|=|D_k|=1.                          \tag{5.2}
   \]

#### Proof

Since the two states both have order two,

\[
                         |G_k|=|D_k|.                            \tag{5.3}
\]

If their common value is at least two, (z_k) is adjacent to all four
roots of (X), and in particular to at least three.  The sets

\[
                         L_{k-1},\qquad U_k,qquad\{z_k\}        \tag{5.4}
\]

are pairwise disjoint and connected.  Strict membership in the corridor
says that each of the first two has neighbours to both (p) and (q).
Thus orient them so that the (a)-side meets (p) and the (b)-side
meets (q).  Lemma 2.1 of
`hadwiger_double_moser_three_carrier_completion.md`, with
(Z=\{z_k\}), gives a (K_7)-minor.

The only remaining nontrivial transition has common value one, which is
(5.2).  A zero value means that no state change occurred and may simply
be suppressed.  \(\square\)

The proof is the promised exchange axiom.  It uses the geometry only once:
a vertex trying to exchange two labels at once is itself the third
root-rich carrier.

### Corollary 5.2 (two atomic exchange vertices)

Assume every root event from (3.2) occurs strictly inside (J_P), every
intermediate cut is negative, and no intermediate state has order below
two.  Then there are exactly two state-changing vertices (r,s), in that
order.  Each is adjacent to one root of (H_1) and one root of (H_2),
and these two pairs form a perfect matching between (H_1) and (H_2).

#### Proof

There are exactly two gains and two losses between the endpoint states in
(3.2).  Theorem 5.1 pairs each gain with exactly one simultaneous loss.
Hence there are exactly two nonsilent events, and their label pairs use
all four labels once.  \(\square\)

This is the label-level crossed four-cycle.  Turning it into a graph-level
crossed frame requires information about how the two event vertices are
joined through the middle of the (st)-order.

## 6. The two exact residual geometries

The interval argument leaves only the following alternatives.

### 6.1 A laminar low-rank gap

If some intermediate state has order below two, then in the chronological
word of the two losses (D) and two gains (G), a loss occurs without a
simultaneous gain.  Ignoring ties, the only words which never create a
three-contact positive state are

\[
                         DDGG\quad\hbox{or}\quad DGDG.           \tag{6.1}
\]

The first has a rank-zero gap; the second has a rank-one gap.  At a cut in
that gap, the lower side sees at most one of (H_1), while the upper side
sees at most one of (H_2).  This is the laminar portal order which must
be converted into a two-cut/exact seven-adhesion or a two-apex web.

### 6.2 A two-event crossed frame

If rank never drops, Corollary 5.2 gives two event vertices carrying the
two edges of a perfect matching between (H_1,H_2).  If a connected set
(Z), disjoint from a lower (b)-to-(P) carrier and an upper
(a)-to-(P) carrier, contains both event vertices, then

\[
                             |N_X(Z)|=4,
\]

and the root-rich third-carrier lemma gives (K_7).  Therefore a surviving
two-event state must separate the two event vertices in every such middle
carrier.  That is precisely a two-demand web obstruction, rather than an
unclassified contact state.

### 6.3 A (P)-interval barrier

If a root event is not strictly inside (J_P), then at the relevant cut
one of (p,q) has no contact on one side.  The four unbalanced maximal
rows (4.1) are exactly these endpoint locks.  Thus failure of the atomic
exchange theorem is recorded by a nonoverlapping (P)-portal interval,
the second boundary datum needed by the web/adhesion argument.

No assertion in this section identifies a web with a planar embedding;
that is the remaining topological theorem.

## 7. The small 2-connectivity prerequisite

The (st)-order assumes that (C) is 2-connected.  Once (R) is
2-connected, a cutvertex of (C) can only be a vertex (z\in R) which is
the unique (R)-portal of both (a) and (b).  The remaining contacts of
(a,b) to (p,q) have only nine patterns.  The conservative quotient
calculation gives the following dichotomy:

* one (P)-contact exposes an exact seven-cut; or
* the three minimal two-(P)-contact patterns
  ((ap,aq),(ap,bq),(aq,bp)) have explicit (K_7)-models after
  contracting the full remainder of (R).

This finite prerequisite should be cited only with its displayed models or
its dependency-free verifier.  It is logically separate from the interval
exchange proved above.

## 8. Net advance

After cutvertex closure and the small prerequisite, the unbounded
2-connected body has been reduced without enumerating its order:

\[
\boxed{
\begin{array}{c}
\text{three-contact split}\Rightarrow K_7,\\
\text{multi-label event}\Rightarrow\text{root-rich third carrier}
   \Rightarrow K_7,\\
\text{otherwise: a rank-0/1 laminar gap, a two-event crossed web,}
   \text{ or a }P\text{-interval barrier.}
\end{array}}
\]

The remaining theorem must turn those three interval obstructions into an
exact seven-adhesion or a planar graph after deleting the two centres
(u,v).  In the latter outcome the Four Colour Theorem would six-colour
(G).  This is now a topological two-apex/web problem, not a further
finite contact atlas.
