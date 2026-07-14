# Three-cuts force a labelled near model or a strict seven-descent

**Status:** proved and independently audited.

This note continues the connected-rich width-two spine after binary
two-gates have been eliminated.  It closes every literal three-cut by one
uniform lobe partition.  No virtual edge of a web completion is used.

## 1. Setup

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

be an actual separation in a seven-connected graph.  Thus `L,R` are
nonempty and anticomplete.  Assume:

1. `G[L]` is three-connected;
2. `P,Q subseteq R` are disjoint connected `S`-full packets joined by a
   literal edge; and
3. the paired boundary `H=G[S]` either contains a spanning non-path tree,
   or is `K_{1,3} dotcup K_3`.

These are exactly the connected-rich width-two frontier inputs.  In its
connected boundary cases, the three literal neighbours of the distinguished
singleton `c` already form a three-edge star and hence extend to the
required spanning non-path tree.

Seven-connectivity also makes `L` literally `S`-full.  Indeed
`N_G(L) subseteq S`; if one boundary literal were absent, at most six
vertices would separate the nonempty shores `L` and `R`.

## 2. A lobe has four boundary labels

Let `T={t_1,t_2,t_3}` be a three-vertex cut of `G[L]`, and call the
components of `G[L]-T` the **lobes**.

### Lemma 2.1 (literal lobe boundary)

Every lobe `D` satisfies

\[
                         N_L(D)=T,
             \qquad |N_S(D)|\ge4.                       \tag{2.1}
\]

If equality holds in the second inequality, then

\[
                         \Omega_D=T\cup N_S(D)           \tag{2.2}
\]

is a literal separator of order seven, and

\[
 V(G)=D\mathbin{\dot\cup}\Omega_D
       \mathbin{\dot\cup}\bigl(V(G)-(D\cup\Omega_D)\bigr) \tag{2.3}
\]

is an actual seven-separation whose `D`-side is nonempty, full to
`Omega_D`, and strictly smaller than `L`.

#### Proof

Every lobe meets all three members of `T`.  Otherwise at most two gate
vertices separate it from another lobe, contrary to three-connectivity.
All neighbours of `D` outside it therefore lie in

\[
                         T\cup N_S(D).                   \tag{2.4}
\]

Another lobe and the original nonempty shore `R` lie outside this set, so
it is a genuine separator.  Seven-connectivity gives

\[
                         3+|N_S(D)|\ge7.                 \tag{2.5}
\]

If equality holds, (2.4) is exactly the order-seven set `Omega_D`:
every gate vertex and every displayed boundary literal has a neighbour in
`D`.  Thus `N_G(D)=Omega_D`, proving fullness and (2.3).  Since another
lobe is nonempty, `D` is a proper subset of `L`.  \(\square\)

## 3. Partitioning all lobes into two near-full carriers

### Lemma 3.1 (two-carrier partition at a three-gate)

Suppose every `T`-lobe `D` satisfies `|N_S(D)|>=5`.  Then `L` has a
partition

\[
                         L=X\mathbin{\dot\cup}Y          \tag{3.1}
\]

such that:

1. `G[X]` and `G[Y]` are connected;
2. there is a literal `X-Y` edge;
3. `|N_S(X)|,|N_S(Y)|>=5`; and
4. `N_S(X) union N_S(Y)=S`.

#### Proof

Partition the nonempty family of lobes into two nonempty subfamilies
`mathcal D_X,mathcal D_Y`.  Put

\[
 X=\{t_1\}\cup\bigcup_{D in\mathcal D_X}D,
 \qquad
 Y=\{t_2,t_3\}\cup\bigcup_{D in\mathcal D_Y}D.          \tag{3.2}
\]

Every lobe meets every gate vertex.  Hence `X` is connected through
`t_1`.  The nonempty family `mathcal D_Y` joins both `t_2` and `t_3`, so
`Y` is connected even when `t_2t_3` is not an edge.  The vertex `t_1` has
a neighbour in every member of `mathcal D_Y`, giving a literal `X-Y`
edge.

Each side contains a lobe with at least five boundary labels, and so each
side has boundary support at least five.  Finally (3.2) partitions all of
`L`; since `L` is `S`-full, the two supports cover `S`.  \(\square\)

No gate edge is assumed in this construction.

## 4. The three-cut dichotomy

### Theorem 4.1 (three-cut closure or strict descent)

Under the setup of Section 1, if `G[L]` has a three-vertex cut, then at
least one of the following holds.

1. `G` contains a literal labelled `K_7^vee` minor.
2. There is a strict actual order-seven adhesion whose connected side is
   one `T`-lobe, is full to its new literal boundary, and has fewer
   vertices than `L`.

#### Proof

Fix a three-cut `T`.  If some lobe has exactly four boundary labels,
Lemma 2.1 gives outcome 2.  Otherwise every lobe has at least five labels,
and Lemma 3.1 gives disjoint adjacent connected carriers `X,Y` satisfying

\[
 |N_S(X)|,|N_S(Y)|\ge5,
 \qquad N_S(X)\cup N_S(Y)=S.                            \tag{4.1}
\]

The four sets `X,Y,P,Q` are pairwise disjoint.  The pairs `X-Y` and
`P-Q` are literal edges, and `P,Q` are `S`-full.  The two-defect anchored
near-model theorem in
`../results/hc7_exact7_binary_gate_near_model.md`, Theorem 2.1, now
applies to `H=G[S]`.  It produces a literal labelled `K_7^vee` model,
which is outcome 1.  \(\square\)

### Corollary 4.2 (the minimum-shore residue is four-connected)

Assume additionally that `|L|>=5`.  If the labelled near-model handoff and
every strict exact-seven descent are excluded—for example, after choosing
the active open shore minimal by order among the relevant actual
seven-adhesions—then `G[L]` is four-connected.  In the live width-two
frontier, `|L|>=5` follows from the already proved bound
`delta(G[L])>=4`.

Together with the four-connected portal theorem, the entire
three-connected width-two frontier then leaves through a labelled
`K_7^vee` handoff or through a strictly smaller actual seven-adhesion.

## 5. Scope

The strict descent does not by itself pull the old paired equality state to
the new boundary.  Its strength is literal: the new boundary is exactly

\[
                         T\cup N_S(D),                  \tag{5.1}
\]

and every one of its seven vertices has a neighbour in the smaller lobe.
Thus the theorem eliminates an infinite family without a lobe census, but
state transfer at the descended adhesion remains a separate global
composition obligation.
