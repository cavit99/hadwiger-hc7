# Contact-transversal amplification at a lex-minimal row

## Status

This note tests the proposed sharp `nu=tau=3` amplification at the
literal near-`K_7` interface.  It proves two safe mechanisms:

1. an actual-neighbour count which really does turn a three-point
   skeleton transversal into an order-at-most-six separator; and
2. a two-owner lobe rotation which turns a detachable three-contact row
   lobe meeting the currently missed row into a new one- or two-hole
   near-`K_7` model.

It also identifies a sharp failure of the hoped-for automatic separator:
lex-minimal row ownership bounds the number of **row labels** owned by a
lobe, but not the number of actual vertices at the opposite ends of those
row edges.  Thus “three skeleton vertices plus two peer rows” is not a
five-vertex cut unless the peer contacts have separately been reduced to
actual singleton gates.

Sections 1--5 have passed the adjacent independent audit.  Section 6 was
added afterward to make the packet Hall deficiency and its
four-connected discharge explicit; it requires a short audit addendum
before being cited as audited.

## 1. Literal setting

Let

\[
                         A,D,F,R_1,R_2,R_3,R_4            \tag{1.1}
\]

be pairwise disjoint connected bags.  Every pair is adjacent except
possibly `AD`; all six bags other than `A` form a clique model, and `A`
is adjacent to `F,R_1,...,R_4`.  Assume `AD` is genuinely absent.

Let `L` be a nonempty proper subset of `F` such that `G[L]` and
`G[F-L]` are connected, and assume `F-L` still has an edge to `A`.  Put

\[
 Z=N_F(L)\subseteq F-L,
 \qquad T=N_A(L),
 \qquad W=N_G(L)-(A\cup F).                              \tag{1.2}
\]

The intended sharp span cell has

\[
                         |T|=3,\qquad |Z|\le2.            \tag{1.3}
\]

For a foreign row `Q in {D,R_1,...,R_4}`, say that `L` **owns** `Q`
when every actual edge between the two displayed bags `F,Q` has its
`F`-end in `L`.  Write `Omega(L)`
for the set of owned rows.

If `G` is `K_7`-minor-free, `F` is minimized lexicographically while all
earlier bags and the missing pair `AD` are fixed, and the comparison
class permits enlarging any nonmissed foreign row by a detachable part
of `F`, the standard detachable-part argument gives

\[
                              |\Omega(L)|\ge2.            \tag{1.4}
\]

Indeed, the retained `A-(F-L)` edge means that `A` is not an additional
owned requirement.  With no foreign owner delete `L`.  With sole owner
`Q != D`, move `L` into `Q`, using an `L-(F-L)` edge to restore their
mutual adjacency; this stays in the comparison class and shortens `F`.
If the sole owner is `D`, the same move repairs `AD` through the nonempty
set `T=N_A(L)` and restores `DF` through the cut edge; no required pair
is lost, so the seven bags form a literal `K_7` model.  This contradicts
`K_7`-minor-freeness.  All cases with at most one owner are excluded.

## 2. What seven-connectivity really gives

### Lemma 1 (actual contact-count amplification)

Assume the seven displayed bags span the host graph, `|T|=3`,
`|Z|<=2`, and the far side `V(G)-(L\cup N_G(L))` is nonempty.  Then

\[
                         |W|\ge4-|Z|.                    \tag{2.1}
\]

Equivalently, if `|W|<=3-|Z|`, then `G` has a separator of order at
most six.

#### Proof

Every neighbour of `L` belongs to the disjoint union `T union Z union W`.
Thus

\[
                |N_G(L)|=|T|+|Z|+|W|.
\]

If `|W|<=3-|Z|`, this order is at most six, and the set separates the
nonempty connected lobe `L` from the assumed nonempty far side.  This
contradicts seven-connectivity.  Rearranging gives (2.1). \(\square\)

The word “actual” is essential.  Formula (2.1) counts vertices in `W`,
not the number of model bags which contain them.

## 3. A detachable two-owner lobe rotates the missing hole

### Theorem 2 (two-owner missed-row rotation)

Retain (1.1)--(1.3).  Assume in addition that

1. `L` has an edge to `D`; and
2. `|Omega(L)|=2`.

Replace

\[
                         D\longmapsto D'=D\cup L,
                  \qquad F\longmapsto F'=F-L.            \tag{3.1}
\]

Then the seven bags remain connected and pairwise adjacent except for
the pairs

\[
                         F'Q\qquad
                  (Q\in\Omega(L)-\{D\}).                 \tag{3.2}
\]

Consequently:

* if `D in Omega(L)`, (3.1) is a one-hole `K_7^-` model;
* if `D notin Omega(L)`, (3.1) is a two-hole near-`K_7` model whose two
  missing pairs share the centre `F'`.

In both cases the old missing pair `AD` is literally repaired.

#### Proof

The new `D'` is connected through the assumed `D-L` edge, and `F'` is
connected by detachability.  The cut between `L` and `F-L` supplies an
edge `D'F'`.  The old absent pair is repaired because `T=N_A(L)` is
nonempty, so `A-D'` is an actual edge.  The bag `F'` retains its required edge to
`A` by the standing assumption in Section 1.

Every old adjacency not incident with `F` survives unchanged.  The
enlarged bag `D'` also retains every old adjacency of `D`.  For a foreign
row `Q`, the edge `F'Q` survives exactly unless all old `F-Q` edges had
their `F`-ends in `L`, i.e. unless `Q in Omega(L)`.  The special row
`D` is harmless even when owned, because `D'F'` is restored by the
`L-(F-L)` cut edge.  Hence precisely the pairs in (3.2) are absent.

There are two owners.  If one is `D`, (3.2) has one member.  If neither
is `D`, it has two members and both are incident with `F'`. \(\square\)

This is a literal model rotation, not a palette argument.  It is exactly
the detachable-packet output wanted from a sharp three-contact lobe: the
existing one-hole/two-hole height and rotation machinery may be applied
to the returned labelled model.

### Corollary 3 (support-two sharp cell)

If all foreign neighbours of `L` lie in at most two row bags and one of
them is `D`, then lex-minimality (1.4) makes those two bags exactly the
owner set.  Hence Theorem 2 applies whenever `F-L` retains an `A` portal.

#### Proof

Every owned row is among the rows actually met by `L`.  At most two are
met, while (1.4) gives at least two owners.  Thus both met rows are owned,
including `D`. \(\square\)

## 4. Falsification of the automatic small-cut step

The following family shows why lex-minimality alone cannot replace the
literal hypothesis in Lemma 1.

Take an `A`-path containing three vertices `t_1,t_2,t_3`.  Let `F` be
the edge `lf`, with

\[
                l\sim t_1,t_2,t_3,\qquad f\sim t_1.      \tag{4.1}
\]

Let `Q_1,Q_2` be disjoint connected row bags of arbitrary order `M`, and
join `l` to every vertex of both.  Put no `f-Q_i` edge; equivalently,
every actual `F-Q_i` edge has its `F`-end at `l`.  Attach every other
required foreign row only at `f`,
and add arbitrary foreign--foreign edges needed for the clique model.

Then `L={l}` is detachable, its full skeleton neighbourhood is the
three-point set `{t_1,t_2,t_3}`, and

\[
                         \Omega(L)=\{Q_1,Q_2\}.           \tag{4.2}
\]

Thus the exact two-owner conclusion forced by lex-minimality holds.  But

\[
 N_G(L)\supseteq
   \{t_1,t_2,t_3,f\}\cup V(Q_1)\cup V(Q_2),              \tag{4.3}
\]

whose order is unbounded.  Moving `L` into `Q_1` loses the only
`F-Q_2` adjacency, and conversely.  Hence neither owner is a faithful
one-row transfer.

This family is a falsifier of the *inference from ownership labels to an
actual separator*.  It is not asserted to be a seven-connected,
`K_7`-minor-free, contraction-critical host.  Those global hypotheses
must supply the missing mechanism; lex-minimality by itself does not.

## 5. Precise remaining amplification edge

In the sharp `nu=tau=3` cell, a valid terminating argument may now use
one of the following verified statements.

1. **Actual gate concentration.**  If the peer-side endpoints together
   with the two internal gates satisfy `|Z|+|W|<=3`, Lemma 1 contradicts
   seven-connectivity.
2. **Missed-row support.**  If a detachable two-owner lobe meets `D`
   and its residual row retains an `A` portal, Theorem 2 returns a one-
   or two-hole near model, rather than another portal case.
3. **Rural/state branch.**  If neither holds, the obstruction has at
   least `4-|Z|` literal peer-side contact vertices and either avoids the
   missed row or owns more than two rows.  These contacts cannot be
   contracted to row labels.  They must be used as disjoint repair
   packets, put into one common rural web, or organized into the opposite
   partition carriers of
   `hc7_guarded_cycle_web_exchange.md`, Theorem 5.

If `F-L` loses the last `A-F` portal, the standing hypothesis of this
note fails and that lost literal duty is a fourth output.  It must be
handled by the endpoint-owner/rotation theorem; it cannot be silently
included in item 3.

The unresolved statement is therefore narrower than the proposed
automatic amplification:

> **Live contact-transversal target.**  In a seven-connected,
> contraction-critical, `K_7`-minor-free host, the rich-peer branch in
> item 3 cannot persist simultaneously on the two open shores without
> producing four distributed sectors, two opposite partition carriers,
> or one common rural disk system.

No current lemma proves this last sentence.  The construction in Section
4 explains exactly why the proof must use seven-connectivity together
with the actual peer-side endpoints or the proper-minor states; counting
row owners is insufficient.

## 6. Exact packet deficiency and the four-connected discharge

The rich endpoints do have one immediate constructive use once their
literal carriers are retained.

### Lemma 4 (row-disjoint packet witnesses)

Let `Q_1,...,Q_4` be the rooted corner bags and `F_1,F_2,F_3` the fixed
row cores in Theorem 1.5 of `hc7_port_distributed_row_exchange.md`.
Let `mathcal K` be a family of pairwise disjoint connected off-skeleton
packets, disjoint from the seven cores.  For every missing duty `(i,j)`,
put

\[
 {\cal N}(i,j)=\{K\in{\cal K}:K\sim Q_i\text{ and }K\sim F_j\}. \tag{6.1}
\]

All missing duties can be repaired by assigning every used packet one
row label if and only if one can choose

\[
                 K_{ij}\in{\cal N}(i,j)                  \tag{6.2}
\]

for every missing duty so that

\[
              K_{ij}=K_{hk}\quad\Longrightarrow\quad j=k. \tag{6.3}
\]

The same packet may witness several corners of one row, but may not
witness duties belonging to two different rows.

#### Proof

Given (6.2)--(6.3), assign each selected packet its unique row index;
omit every unused packet.  Every duty is repaired, so the distributed-row
packet theorem applies.  Conversely, from any valid packet assignment
choose for each missing duty one assigned packet which repairs it.  A
packet has one row label, giving (6.3). \(\square\)

Thus the exact Hall-type failure is not “fewer than four endpoints”.  If
some `N(i,j)` is empty, that unsupported duty is one failure branch.  If
all the sets in (6.1) are nonempty, the remaining failure is exactly:

> for every choice of one literal supporting packet per duty, some one
> packet is forced to represent duties of two different rows.

This is the locked two-row collision, stated without palette labels.

### Lemma 5 (locked collision splits or is one rural page)

Let `L` be a connected set disjoint from the seven core bags.  Suppose
there is an already labelled family `K_0` of pairwise disjoint connected
packets, disjoint from `L` and from the cores, such that direct edges
together with `K_0` repair every duty other than two duties
`(i,j),(h,k)` with `j!=k`.  Inside
`G[L]` put

\[
 A=N_L(Q_i),\quad P=N_L(F_j),\quad
 B=N_L(Q_h),\quad R=N_L(F_k).                            \tag{6.4}
\]

Assume these four sets are nonempty and pairwise disjoint and `G[L]` is
four-connected.  Then exactly one of the following occurs.

1. `L` contains disjoint connected packets `K_j,K_k`, where `K_j`
   meets `A,P` and `K_k` meets `B,R`.  Adding these two packets to
   `K_0`, with row labels `j,k`, repairs all duties; the distributed-row
   packet theorem gives `K_7` (or `K_7^-` if the hypotheses explicitly
   retain one further unrepaired duty).
2. `G[L]` is planar and one facial cycle contains all four portal sets in
   the labelled alternating block order `A,R,P,B`, up to reversal.  Hence
   the obstruction is one literal local rural page, ready for the
   separate torso/adhesion composition branch, not another
   packet-incidence case.

#### Proof

Apply the audited four-set rural block theorem
`hc7_near_k7_set_root_rural_order.md`, Theorem 1, to the four sets
`A,B,P,R`.  Its linkage outcome gives disjoint `A-P` and `B-R` paths;
take their vertex sets for `K_j,K_k`.  They are eligible for the two
different row labels and satisfy (6.3).  Since both lie in `L`, they are
disjoint from the preassigned family `K_0`.  Its other outcome is exactly
the displayed facial block order `A,R,P,B`, up to reversal. \(\square\)

### Applicability consequence

This discharges the rich-peer subcase in which the distinct peer-side
endpoints can be placed into four disjoint portal classes inside one
four-connected lobe disjoint from the already assigned packets: it gives
the missing off-skeleton packets or one local rural page.  What remains is
now literal and smaller:

* overlapping portal classes, handled only when a common-portal
  promotion is available;
* a cutvertex or 2-adhesion inside `L`, which must be exposed as an
  actual boundary state; or
* more than one simultaneous cross-row collision in different lobes.

The inequality `|W|>=4-|Z|` alone does not ensure four disjoint portal
classes, so Lemma 5 is not asserted outside this exact scope.
