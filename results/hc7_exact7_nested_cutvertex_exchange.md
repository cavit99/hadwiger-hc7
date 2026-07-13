# Exact-seven nested cutvertex exchange

## 1. Scope

Assume the audited exact-seven `(1,3)` two-lobe setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `G` is seven-connected, there are no `LR` edges, `R` contains
three pairwise disjoint connected `S`-full packets, and `G[L]` is
three-connected.  Let `T={t_1,t_2,t_3}` be a three-cut of `G[L]`, and
let `J,K` be the two components of `G[L]-T`.

The crossed-arm lemma says that, for `z in J`, every component of `J-z`
meets at least two gate vertices.  The theorem below converts three such
crossed arms directly into the four literal labelled carriers required
for `K_7`.

## 2. A three-set gate assignment

For a component `A` of `J-z`, put

\[
                         U_A=N_T(A).
\]

Three-connectivity of `G[L]` gives `|U_A|>=2`: otherwise `{z}` together
with the at most one member of `U_A` separates `A` from `K`.

### Lemma 2.1 (two leaves and a gated centre)

Suppose `J-z` has at least three components.  There are distinct
components `A,B,C`, a permutation `(u,v,w)` of `T`, and one of the two
literal incidences

\[
                         v\in U_A\quad\hbox{or}\quad u\in U_B,
                                                               \tag{2.1}
\]

such that

\[
 u\in U_A,\qquad v\in U_B,
 \qquad\text{and}\qquad w\in U_C\text{ or }zw\in E(G).       \tag{2.2}
\]

#### Proof

Every `U_A` is a two- or three-element subset of the three-set `T`.

If some component `C` has `U_C=T`, use it as the third component.  For
any two other components `A,B`, their two-or-more-element gate sets
intersect.  Choose distinct `u in U_A`, `v in U_B` so that one of `u,v`
lies in both sets: if the intersection has two elements, choose two of
them; if it has one element, use that common element for one choice and
any different permitted element for the other.  Then (2.1) holds, and
the unused gate `w` belongs to `U_C`.

It remains that every selected gate set has order two.  Write `m_A` for
the unique gate missed by `A`.  If not all components of `J-z` have the
same missed gate, choose three whose missed gates are not all equal and
permute their names as follows.

* If the three missed gates are all distinct, write them `a,b,c` for
  `A,B,C`.  Take `u=c in U_A`, `v=a in U_B`, and `w=b in U_C`.
  Moreover `c in U_B`, so the second alternative in (2.1) holds.
* If exactly two missed gates occur, name the components so that
  `m_A=m_C=a` and `m_B=c ne a`.  Let `d` be the third gate, and take
  `u=d in U_A`, `v=a in U_B`, and `w=c in U_C`.  Here
  `d in U_B`, again giving (2.1).

Finally suppose every component misses the same gate `w`.  Choose any
three components, let `{u,v}=T-{w}`, and assign `u` and `v` to the first
two.  Both belong to both gate sets, so (2.1) holds.  Since `J` itself
meets every gate vertex and no component of `J-z` meets `w`, the literal
edge `zw` exists.  This proves (2.2). `square`

## 3. Literal carrier construction

### Theorem 3.1 (nested three-component closure)

If some vertex `z` of either lobe has at least three components after its
deletion, then `G` contains a literal `K_7` minor.

#### Proof

Apply Lemma 2.1 inside that lobe `J`, and define

\[
 W_1=A\cup\{u\},\qquad
 W_2=B\cup\{v\},\qquad
 W_3=C\cup\{z,w\}.                                      \tag{3.1}
\]

These three sets are pairwise disjoint and connected.  For `W_3`, the
component `C` has a neighbour at `z`, and either it has a neighbour at
`w` or the edge `zw` is literal.  Their pairwise adjacencies are also
literal:

* `W_1W_2` follows from (2.1);
* `W_1W_3` follows from an `A-z` edge; and
* `W_2W_3` follows from a `B-z` edge.

The opposite lobe `K` is connected and adjacent to every `W_i`, since
it meets each of the three literal gate vertices `u,v,w`.  Thus

\[
                           W_1,W_2,W_3,K                    \tag{3.2}
\]

are four disjoint connected clique carriers.

It remains to give them four distinct literal boundary representatives.
For `X in {A,B,C}`, every neighbour of `X` outside itself lies in

\[
                         \{z\}\cup U_X\cup N_S(X).          \tag{3.3}
\]

The other lobe and the nonempty opposite open shore remain after deleting
this set.  Seven-connectivity therefore gives

\[
             1+|U_X|+|N_S(X)|\ge7,
             \qquad |N_S(X)|\ge6-|U_X|\ge3.                \tag{3.4}
\]

Three subsets of a seven-set, each of order at least three, have an SDR:
every one-set subfamily has union at least three, every two-set subfamily
has union at least three, and the full three-set family has union at least
three.  Choose distinct

\[
              s_1\in N_S(A),\quad s_2\in N_S(B),
              \quad s_3\in N_S(C).                         \tag{3.5}
\]

Also `|N_S(K)|>=4`, since `T union N_S(K)` separates `K`; choose

\[
                       s_0\in N_S(K)-\{s_1,s_2,s_3\}.       \tag{3.6}

Adjoin these four representatives to the carriers in (3.2).  Anchor the
three disjoint `S`-full packets in `R` at the remaining three vertices of
`S`.  Packet fullness supplies every packet--packet and packet--carrier
adjacency.  The resulting seven disjoint connected bags are pairwise
adjacent and form a literal `K_7` model. `square`

### Corollary 3.2 (nested block-chain restriction)

In a `K_7`-minor-free survivor, for every lobe `J` and every `z in J`,
the graph `J-z` has at most two components.

This conclusion is intentionally local.  It bounds the degree of every
cutvertex node in the block--cutvertex tree; it does not say that the
whole block tree is a path, because a block node may still meet several
distinct cutvertices.

## 4. Use in the portal-rank exchange

The theorem eliminates the entire branching-cutvertex family in either
lobe, with no Moser labels and no bound on lobe order.  Consequently a
portal-rank monopoly which is supported behind cutvertices can only drift
through a sequence of two-sided cuts or around one two-connected block.
Those are precisely the two places where a block-terminal Two-Paths/web
dichotomy is meaningful.  No bounded portal transversal or equality state
is inferred here.
