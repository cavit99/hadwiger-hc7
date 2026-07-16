# Bridge augmentation in the exceptional six-path configuration

**Status:** written proof; independently audited in
[`hc7_disjoint_k6minus_support6_bridge_augmentation_audit.md`](hc7_disjoint_k6minus_support6_bridge_augmentation_audit.md).
The proved statements below isolate the exact consequence of seven-connectivity in the
quotient survivor from
[`hc7_disjoint_k6minus_support6_six_link_barrier.md`](../barriers/hc7_disjoint_k6minus_support6_six_link_barrier.md).
They do not close this configuration or prove `HC_7`.  The remaining problem
is to compose two labelled four-terminal web certificates that share one
of the six linkage paths.

## 1. Normalized configuration

Let `G` be a seven-connected graph.  Suppose that `G` contains the following
two disjoint six-vertex subgraphs.

- On
  \[
     A=\{a_0,a_1,a_2,a_3,x,y\},
  \]
  the set `Q={a_0,a_1,a_2,a_3}` is a clique, `xy` is an edge,
  `x` is adjacent to `a_0,a_1,a_2`, and `y` is adjacent to `a_3`.
  Thus the four singleton branch sets indexed by `Q`, together with
  `\{x,y\}`, form a `K_5`-minor model.
- On
  \[
     B=\{b_0,b_1,b_2,r,p,q\},
  \]
  every pair is adjacent except possibly `p,q`; in particular, `G[B]`
  contains the displayed `K_6^-`.

Suppose further that there are six pairwise vertex-disjoint paths, internally
disjoint from `A` and `B`, with the following ends:

\[
\begin{array}{lll}
 P_0:a_0\mathbin{-}b_0,&
 P_1:a_1\mathbin{-}b_1,&
 P_2:a_2\mathbin{-}b_2,\\
 P_3:a_3\mathbin{-}p,&
 P_4:x\mathbin{-}q,&
 P_5:y\mathbin{-}r.
\end{array}                                                    \tag{1.1}
\]

The paths are oriented from their first displayed end to their second.  For
an oriented path `P` with ends `s,t`, the notation `P-t` means the path after
deleting its end `t`.

This is precisely the labelled quotient configuration not settled by the
mere existence of the six paths.  No edge not explicitly listed above is
assumed absent from `G`.

## 2. A path avoiding the two exceptional rails gives a `K_7` minor

### Theorem 2.1 (clean augmenting path)

Fix \(i\in\{0,1,2\}\).  Suppose there is a path `R` with one end

\[
             u\in V(P_5-y)
\]

and the other end

\[
             v\in V(P_i-b_i),
\]

such that the interior of `R` is disjoint from

\[
            A\cup B\cup\bigcup_{h=0}^5V(P_h).
\]

Then `G` has a `K_7` minor.

#### Proof

Let `u^-` be the neighbour of `u` on `P_5` toward `y`; it exists because
`u\ne y`.  Let `v^+` be the neighbour of `v` on `P_i` toward `b_i`; it
exists because `v\ne b_i`.  Define

\[
\begin{aligned}
 L_5&=P_5[y,u^-],&
 R_5&=P_5[u,r]\cup (R-v),\\
 L_i&=P_i[a_i,v],&
 R_i&=P_i[v^+,b_i].
\end{aligned}                                                \tag{2.1}
\]

Here `R-v` is the subpath obtained by deleting the end `v`.  It meets
`P_5[u,r]` at `u`, so `R_5` is connected.  If
`{i,j,k}={0,1,2}`, consider the seven vertex sets

\[
 \boxed{
  P_j,\quad P_k,\quad P_3,\quad
  P_4\cup L_5,\quad R_5,\quad L_i,\quad R_i.}
                                                               \tag{2.2}
\]

They are pairwise disjoint.  Each is connected: the only non-immediate case
is `P_4\cup L_5`, and it is connected by the edge `xy`.

For completeness, all adjacencies among the five branch sets after
`P_j,P_k` are witnessed as follows:

\[
\begin{array}{c|cccc}
 &P_4\cup L_5&R_5&L_i&R_i\\ \hline
P_3&a_3y&pr&a_3a_i&pb_i\\
P_4\cup L_5&&u^-u&xa_i&qb_i\\
R_5&&&\text{the last edge of }R\text{ at }v&rb_i\\
L_i&&&&vv^+
\end{array}                                                    \tag{2.3}
\]

Both `P_j` and `P_k` are adjacent to every other branch set in (2.2):
use the clique edges in `Q` for adjacency to `P_3` and `L_i`, the edges
`a_jx,a_kx` for adjacency to `P_4\cup L_5`, and the clique edges in
`B` for adjacency to `R_5` and `R_i`.  The two paths `P_j,P_k` are
adjacent to each other at either end.  Thus (2.2) is an explicit
`K_7`-minor model.  \(\square\)

### Remark 2.2 (why the labels matter)

The theorem uses an augmenting path from the `r`-rail `P_5` to one of the
three rails `P_0,P_1,P_2`.  The analogous construction need not work when
the second end lies on `P_3` or `P_4`.  The adjacent finite barrier verifies
that those two alternatives are genuine at the contracted-quotient level.

## 3. Seven-connectivity forces a two-path separator relation

Put

\[
 Z=\{b_0,b_1,b_2,p,q,y\},\qquad H=G-Z,                    \tag{3.1}
\]

and define the following three disjoint vertex sets in `H`:

\[
\begin{aligned}
 U&=V(P_5-y),\\
 T&=\bigcup_{i=0}^{2}V(P_i-b_i),\\
 X&=V(P_3-p)\cup V(P_4-q).
\end{aligned}                                                \tag{3.2}
\]

The two constituent paths displayed in the definition of `X` are the two
exceptional rails; extra host edges may of course join them.

### Theorem 3.1 (forced return and separator)

In the normalized configuration, at least one of the following holds.

1. `G` has a `K_7` minor.
2. In `H`, the set `X` separates `U` from `T`; equivalently,

   \[
                    \text{Every }U\text{--}T\text{ path in }H
                    \text{ meets }X.                    \tag{3.3}
   \]

More explicitly, seven-connectivity always supplies a path whose interior
is disjoint from all six paths in (1.1), from `A`, and from `B`, and whose
ends lie respectively in `U` and one of

\[
 V(P_0-b_0),\ldots,V(P_4-q).                              \tag{3.4}
\]

If `G` is `K_7`-minor-free, the second end of every such path lies on
`P_3-p` or `P_4-q`.

#### Proof

Since `G` is seven-connected and `|Z|=6`, the graph `H=G-Z` is connected.
The set `U=P_5-y` is nonempty and connected.  The vertex set

\[
 L=\bigcup_{h=0}^{4}V(P_h-\text{its end in }B)             \tag{3.5}
\]

is also connected: `A-y` is connected, and each truncated path in (3.5)
has its first end in `A-y`.  The sets `U` and `L` are disjoint.  Choose a
shortest `U`--`L` path in `H`.  Its interior misses both `U` and `L`.
All vertices of the six displayed paths outside `U\cup L` belong to
`Z`, and all vertices of `A\cup B` outside `U\cup L` also belong to
`Z`.  Hence this shortest path has exactly the disjointness asserted after
(3.4).

If its end in `L` belongs to `P_i-b_i` for some \(i\in\{0,1,2\}\), Theorem
2.1 gives a `K_7` minor.  Therefore, in a `K_7`-minor-free graph, its end
in `L` must lie on `P_3-p` or `P_4-q`.  This proves the explicit forced
return statement.

It remains to prove the separator assertion.  Suppose that `H-X` contains
a `U`--`T` path.  Choose one of minimum length.  By shortening it at its
first and last contacts, its interior avoids `U\cup T`; it avoids `X`
by construction.  The six paths in (1.1), and all vertices of `A\cup B`,
are contained in

\[
            U\cup T\cup X\cup Z.
\]

Thus the chosen path satisfies the hypotheses of Theorem 2.1 for whichever
one of `P_0,P_1,P_2` contains its end in `T`.  This gives a `K_7` minor,
a contradiction.  Hence `X` separates `U` from `T` in `H`.  \(\square\)

### Corollary 3.2 (the exact unresolved branch)

Assume that `G` is `K_7`-minor-free.  Let `W` be a minimum `U`--`T`
separator in `H`, where by definition `W` is disjoint from `U\cup T`.

- If `|W|=1`, then `Z\cup W` is the boundary of an actual separation of
  `G` of order seven, with nonempty open sides containing vertices of `U`
  and `T`.
- If `|W|>=2`, Menger's theorem supplies two pairwise vertex-disjoint
  `U`--`T` paths in `H`.  Every such path meets `X`, by Theorem 3.1.

The second outcome is the remaining composition problem.  The theorem does
not show that the two paths meet different components `P_3-p,P_4-q`, does
not control their order of intersection with those paths, and does not
turn `X` into a separator of bounded order.  In particular, this is not yet
an order-at-most-six separator contradiction.

#### Proof

The first assertion follows because deleting `Z\cup W` separates the
nonempty sets `U` and `T`.  The second is exactly
the vertex form of Menger's theorem, followed by (3.3).  \(\square\)

## 4. Crossed bridges transpose the exceptional endpoint assignment

For \(h\in\{3,4\}\), write

\[
 (s_3,t_3)=(a_3,p),\qquad (s_4,t_4)=(x,q).
\]

The union of `P_5`, `P_h`, and the two edges

\[
 ys_h,\qquad rt_h                                      \tag{4.1}
\]

is a cycle `C_h`.  Thus the two exceptional return classes from Theorem
3.1 have a common cycle formulation.

### Theorem 4.1 (crossed cycle bridges)

Fix \(h\in\{3,4\}\).  Suppose there are two pairwise vertex-disjoint paths
`R_1,R_2`, each joining `P_5` to `P_h`, whose interiors avoid `A`, `B`,
and all six paths in (1.1).  Suppose their four ends are distinct.  Write
these ends as

\[
 u_1,u_2\in V(P_5),\qquad v_1,v_2\in V(P_h),
\]

where `R_i` joins `u_i` to `v_i`.  If `u_1,u_2` occur in this order from
`y` to `r` on `P_5`, while `v_2,v_1` occur in this order from `s_h` to
`t_h` on `P_h`, then `G` has a `K_7` minor.

#### Proof

The two paths

\[
\begin{aligned}
 Q_5&=P_5[y,u_1]\cup R_1\cup P_h[v_1,t_h],\\
 Q_h&=P_h[s_h,v_2]\cup R_2\cup P_5[u_2,r]
\end{aligned}                                                \tag{4.2}
\]

are vertex-disjoint and are disjoint from every `P_l` with
\(l\notin\{5,h\}\).  They transpose the two right ends: if `h=3`, then
`Q_5` joins `y` to `p` and `Q_3` joins `a_3` to `r`; if `h=4`, then
`Q_5` joins `y` to `q` and `Q_4` joins `x` to `r`.

When `h=3`, the following are seven branch sets:

\[
 \boxed{
 (P_0-b_0)\cup(Q_3-r),\quad P_1,\quad P_2,\quad P_4,
 \quad Q_5,\quad\{b_0\},\quad\{r\}.}                    \tag{4.3}
\]

The first set is connected by the edge `a_0a_3`.  It is adjacent to the
last two singleton sets along the final edges of `P_0` and `Q_3`, and to
`P_1,P_2,P_4,Q_5` by `a_0a_1,a_0a_2,a_0x,a_3y`, respectively.  The four
middle paths have right ends `b_1,b_2,q,p`; all corresponding right-side
edges exist except `pq`, and that last adjacency is supplied by `xy`.
Finally `b_0,r` are adjacent to each other and to all four middle right
ends.  Hence (4.3) is a `K_7`-minor model.

When `h=4`, the seven branch sets are

\[
 \boxed{
 (P_0-b_0)\cup(Q_4-r),\quad P_1,\quad P_2,\quad P_3,
 \quad Q_5,\quad\{b_0\},\quad\{r\}.}                    \tag{4.4}
\]

Now the first set is connected by `a_0x` and is adjacent to the four
middle paths by `a_0a_1,a_0a_2,a_0a_3,xy`.  Their right ends are
`b_1,b_2,p,q`; the sole missing right-side adjacency `pq` is supplied by
`a_3y`.  The adjacencies involving `b_0,r` are as before.  Thus (4.4) is
a `K_7`-minor model.  \(\square\)

### Theorem 4.2 (two explicit web certificates)

For \(h\in\{3,4\}\), put

\[
 D_h=\left((A\cup B)\cup
       \bigcup_{\ell\notin\{5,h\}}V(P_\ell)\right)
       \setminus\bigl(V(P_5)\cup V(P_h)\bigr),
 \qquad H_h=G-D_h,                                      \tag{4.5}
\]

and give the four terminals the cyclic order

\[
                         \mathcal T_h=(y,r,t_h,s_h).     \tag{4.6}
\]

Then at least one of the following holds:

1. `G` has a `K_7` minor; or
2. for each \(h\in\{3,4\}\), the graph `H_h` embeds as a spanning subgraph
   of a `4`-web whose frame, in cyclic order, is `\mathcal T_h`.

Equivalently, in outcome 2 there is a set `F_h` of edges on `V(H_h)` such
that `H_h+F_h` is a web with frame `\mathcal T_h`.

#### Proof

Fix `h`.  A crossing of the ordered tuple `\mathcal T_h` consists of two
vertex-disjoint paths, one from `y` to `t_h` and one from `r` to `s_h`.
The definition of `H_h` ensures that their interiors avoid the other four
linkage paths and all vertices of `A\cup B` except their four prescribed
ends.  Reverse the second path and call the two paths `Q_5,Q_h`.  They are
exactly the transposed paths used in (4.3) when `h=3` and in (4.4) when
`h=4`.  The seven branch sets displayed there therefore give a `K_7`
minor.

Consequently, if outcome 1 fails, `\mathcal T_h` is crossless in `H_h`.
The Generalised Two Paths Theorem of Humeau--Pous says that a graph with a
given ordered tuple either has a crossing or embeds in a web with that
tuple as its frame.  It therefore supplies the required edge set `F_h`.
Apply this independently for `h=3` and `h=4`.  \(\square\)

The completion edges in `F_h` are not asserted to be edges of `G` and may
not be used as branch-set adjacencies.  Moreover, the two web completions
need not agree on the vertices common to `H_3` and `H_4`.  The exact
remaining problem is therefore no longer an arbitrary noncrossing path
system: it is to exploit seven-connectivity and the common path `P_5` to
show that two such independently obtained `4`-web certificates either
admit a genuine crossing in one host graph or expose a labelled separation
usable by the support-six argument.

## 5. What Perfect's augmentation theorem does and does not add

Delete only

\[
                      Z'=\{b_0,b_1,b_2,y\}.             \tag{5.1}
\]

The graph `G-Z'` is three-connected.  Let

\[
                      S=\{p,q\}\cup T.
\]

The Fan Lemma supplies a three-fan from `r` to `S`.  Perfect's augmentation
theorem, applied to the two-edge fan `rp,rq`, allows the three-fan to be
chosen with `p,q` among its feet.  Its third foot therefore lies in `T`.
Although Perfect's theorem preserves the two feet rather than the two
original arms, the `p`- and `q`-arms can then be replaced by the literal
edges `rp,rq`: the third arm avoids `p,q`.

Take the last contact of the third arm with `U` and its first subsequent
contact with `T`.  If the resulting subpath avoids `X`, Theorem 2.1 gives a
`K_7` minor.  Hence in a `K_7`-minor-free graph every such Perfect-augmented
third arm meets `P_3-p` or `P_4-q`.

This identifies the precise limitation of the standard augmentation
theorems here.  Perfect's theorem preserves prescribed feet, and Pym's
linkage theorem preserves prescribed subsets of the two endpoint sets;
neither theorem preserves a prescribed permutation of a full six-linkage
or forces the new arm to avoid the two named exceptional paths.  Additional
label-sensitive composition is required after Theorem 3.1.

## 6. Relation to the classical two-clique argument

The deletion of the six vertices in (3.1) is adapted from the proof of
Rolek--Song, Lemma 1.9, where two disjoint `K_6` subgraphs in a
seven-connected graph yield a `K_8^-` minor.  In that argument any extra
path can be split profitably because both six-sets are cliques.  Here the
left set is only the six-vertex support of a `K_5` model and the right set
has the missing edge `pq`; exactly two endpoint classes cease to be
profitable, producing the separator `X`.

References:

- M. Rolek and Z.-X. Song, *Coloring graphs with forbidden minors*,
  Journal of Combinatorial Theory, Series B 127 (2017), 14--31,
  [arXiv:1606.05507](https://arxiv.org/abs/1606.05507), Lemma 1.9.
- H. Perfect, *Applications of Menger's graph theorem*, Journal of
  Mathematical Analysis and Applications 22 (1968), 96--111,
  [doi:10.1016/0022-247X(68)90163-7](https://doi.org/10.1016/0022-247X(68)90163-7).
- J. S. Pym, *The Linking of Sets in Graphs*, Journal of the London
  Mathematical Society s1-44 (1969), 542--550,
  [doi:10.1112/jlms/s1-44.1.542](https://doi.org/10.1112/jlms/s1-44.1.542).
- S. Humeau and D. Pous, *On the Two Paths Theorem and the Two Disjoint
  Paths Problem*, [arXiv:2505.16431](https://arxiv.org/abs/2505.16431),
  Theorem 1.3 and the web-completion equivalence in Section 5.

## 7. Trust boundary

The following are proved here without computation:

- the explicit seven branch sets in Theorem 2.1;
- the forced-return alternative from seven-connectivity;
- the two-path separator relation in Theorem 3.1;
- the endpoint transposition and explicit branch sets in Theorem 4.1; and
- the two web-completion certificates in Theorem 4.2, conditional only on
  the cited Generalised Two Paths Theorem.

The adjacent quotient computation is used only to explain why the two
exceptional paths are the correct residual labels.  It is not used in the
proofs.  The still-open step is to compose the two independently obtained
web certificates along their common path `P_5`, or else to derive a useful
order-seven separation while preserving the labelled minor model.
