# Independent audit: exact-seven nested cutvertex exchange

## Verdict

**GREEN.**  Under the hypotheses written in
`../results/hc7_exact7_nested_cutvertex_exchange.md`, Lemma 2.1,
Theorem 3.1, and Corollary 3.2 are correct.  The gate assignment is
exhaustive, all carrier sets are disjoint and connected, the four
carrier--carrier adjacencies are literal, the two uses of
7-connectivity give the stated boundary-contact bounds, the boundary
representatives have an SDR, and the final seven bags have all 21
required adjacencies.

The conclusion is local.  It rules out a vertex whose deletion produces
three components inside one of the two named lobes; it does not show
that the entire block--cutvertex tree is a path, and it does not produce
an apex set or an equality state.

## 1. Scope and separation facts

The audited setting is the actual separation

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no `LR` edges, three disjoint connected `S`-full packets in `R`,
and `G[L]` three-connected.  A 3-cut `T={t_1,t_2,t_3}` of `G[L]` has
exactly the two named components `J,K` after deletion.

Three-connectivity implies that each of `J,K` has a neighbour at every
literal gate in `T`: otherwise its neighbourhood in `G[L]` would have
order at most two.  If `z in J` and `A` is a component of `J-z`, then

\[
 N_{G[L]}(A)\subseteq \{z\}\cup N_T(A).
\]

If `|N_T(A)|<=1`, the set on the right has order at most two and
separates `A` from the nonempty lobe `K`, contrary to
three-connectivity.  Thus every gate set

\[
                         U_A=N_T(A)
\]

has order two or three, exactly as used in Lemma 2.1.

Every component of `J-z` has a neighbour at `z`, since `J` is connected.
This supplies the `A-z`, `B-z`, and `C-z` edges later used in the
carrier construction.

## 2. Audit of the gate-assignment lemma

There are only four possible gate sets: the three 2-subsets of `T` and
`T` itself.

### A full gate set

If `U_C=T`, any two other gate sets `U_A,U_B` intersect because both
have order at least two in a 3-set.  If their intersection has order at
least two, choose distinct `u,v` in it.  If it has order one, choose the
common gate for one of `u,v` and a different permitted gate for the
other.  In either event

\[
 u\in U_A,\qquad v\in U_B,
 \qquad v\in U_A\ \hbox{or}\ u\in U_B.
\]

The unused gate `w` belongs to `U_C`.

### Three gate 2-sets

Write `m_X` for the unique gate missed by a component `X`.

* If `m_A,m_B,m_C` are all distinct, the choices in the note are valid:
  with missed gates `a,b,c`, respectively, take
  `u=c`, `v=a`, `w=b`.  Then `u` also belongs to `U_B`.
* If exactly two missed gates occur, relabel so that
  `m_A=m_C=a`, `m_B=c`, and let `d` be the third gate.  The choices
  `u=d`, `v=a`, `w=c` work, and `u` also belongs to `U_B`.
* If every component misses the same gate `w`, both remaining gates
  `u,v` belong to every component gate set.  Since `J` has a neighbour
  at `w` but no component of `J-z` does, the edge `zw` is literal.

If the family has more than three components and not all missed gates
are equal, two components with different missed gates and any third
component give a triple whose missed gates are not all equal.  Hence the
case selection is exhaustive for the full statement, not only for a
preselected triple.

As a finite guardrail, all `4^3=64` ordered triples of allowed gate sets
were enumerated.  Allowing permutation of the three components, every
triple has choices of distinct `u,v,w` satisfying (2.1)--(2.2), where
the `zw` alternative is used precisely when all three sets miss `w`.
There were zero uncovered patterns.

## 3. The four literal carriers

The proposed sets are

\[
 W_1=A\cup\{u\},\qquad
 W_2=B\cup\{v\},\qquad
 W_3=C\cup\{z,w\},\qquad K.
\]

They are pairwise disjoint: `A,B,C` are distinct components of `J-z`;
`z` belongs to none of them; `u,v,w` are distinct vertices of `T`; and
`K` is the other component of `G[L]-T`.

Connectivity is literal:

* `A-u` and `B-v` edges exist by the definitions of `U_A,U_B`;
* `C` has a neighbour at `z`, and either `C-w` exists or the edge `zw`
  exists; and
* `K` is a component and hence connected.

The six adjacencies among these four carriers are:

| Pair | Literal witness |
|---|---|
| `W_1W_2` | `A-v` if `v in U_A`, or `B-u` if `u in U_B` |
| `W_1W_3` | an `A-z` edge |
| `W_2W_3` | a `B-z` edge |
| `KW_1` | a `K-u` edge |
| `KW_2` | a `K-v` edge |
| `KW_3` | a `K-w` edge |

The final three exist because `K` meets all three gate vertices.

## 4. Boundary contact counts and representatives

For `X in {A,B,C}`, all neighbours outside `X` lie in

\[
                    \{z\}\cup U_X\cup N_S(X).
\]

This set separates `X` from both the other lobe `K` and the nonempty
opposite open shore.  Its three parts are disjoint, so seven-connectivity
gives

\[
 1+|U_X|+|N_S(X)|\ge7,
 \qquad |N_S(X)|\ge6-|U_X|\ge3.
\]

For three subsets of a seven-element set, each of order at least three,
Hall's condition is automatic: unions of one, two, and three members
have order at least three, hence at least the size of the subfamily.
Thus distinct representatives

\[
 s_1\in N_S(A),\quad s_2\in N_S(B),\quad s_3\in N_S(C)
\]

exist.

Similarly, every neighbour of `K` outside `K` lies in
`T union N_S(K)`.  This set separates `K` from `J` and from the open
opposite shore, so

\[
                       3+|N_S(K)|\ge7.
\]

Therefore `|N_S(K)|>=4`, and a fourth representative

\[
                    s_0\in N_S(K)-\{s_1,s_2,s_3\}
\]

exists.  Adding `s_i` to its corresponding carrier preserves
disjointness and makes that carrier connected to its representative.

## 5. Complete `K_7` adjacency audit

Let the four enlarged carriers be

\[
 D_0=K\cup\{s_0\},\quad
 D_1=W_1\cup\{s_1\},\quad
 D_2=W_2\cup\{s_2\},\quad
 D_3=W_3\cup\{s_3\}.
\]

Let `r_1,r_2,r_3` be the three vertices of
`S-\{s_0,s_1,s_2,s_3\}` and let

\[
                         E_i=P_i\cup\{r_i\}
\]

for the three disjoint `S`-full packets in `R`.  All seven bags are
pairwise disjoint and connected.  Their 21 adjacencies are:

| Bag pairs | Number | Literal witness |
|---|---:|---|
| among the four `D_j` | 6 | the six carrier edges audited in Section 3 |
| `E_iD_j` | 12 | `P_i-s_j`, by `S`-fullness |
| among the three `E_i` | 3 | `P_i-r_j`, by `S`-fullness |

The total is `6+12+3=21`.  Thus the seven bags form a literal `K_7`
model, with no contraction lifting, palette identification, or hidden
planarity assumption.

## 6. Corollary and trust boundary

Theorem 3.1 applies symmetrically with `J,K` interchanged.  Hence, in a
`K_7`-minor-free survivor, deletion of any vertex inside either named
lobe leaves at most two components in that lobe.  This is exactly the
local block--cutvertex-degree statement of Corollary 3.2.

The proof essentially uses:

* three-connectivity of `G[L]`, both for the two-gate condition and for
  every lobe meeting all three gates;
* an actual 3-cut with the two named nonempty lobes;
* seven-connectivity of the whole graph for the literal boundary-contact
  counts; and
* three disjoint `S`-full packets in the opposite shore.

It does not show that a block node meets at most two cutvertices, that
the entire block tree is linear, or that a local gate order is coherent
across different 3-cuts.  Those remain outside the theorem's scope.

