# Independent audit: exact-seven three-gate resource exchange

## Verdict

**GREEN.**  Under the hypotheses stated in
`hc7_exact7_three_gate_resource_exchange.md`, the claimed conclusion is
valid:

\[
 |\pi_0(G[L]-T)|\ge 3\quad\Longrightarrow\quad K_7\preccurlyeq G.
\]

In particular, every surviving actual three-cut of the three-connected
thin shore has exactly two lobes.  The proof uses no edge of a virtual
web triangle and does **not** use the false assertion that deleting a
lobe leaves a `T`-rooted `K_3`.

The theorem is actually independent of contraction-criticality and of
the condition `nu_L=1`.  Its literal inputs are precisely:

1. the displayed actual order-seven separation with nonempty shores;
2. seven-connectivity of the host;
3. three pairwise disjoint `S`-full packets in the opposite shore; and
4. three-connectivity of `G[L]`.

## 1. Scope and lobe neighbourhoods

The partition

\[
V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
\qquad |S|=7,
\]

with no `LR` edge is an actual separation.  If `T` is an actual
three-cut of the three-connected graph `G[L]`, every component `C` of
`L-T` has a neighbour at each of the three literal vertices of `T`.
Indeed, `N_L(C)` is contained in `T`; if it had order at most two, it
would separate `C` from another component of `L-T`, contrary to
three-connectivity.  Thus

\[
N_L(C)=T.
\]

No virtual completion edge is used here.

## 2. Audit of Lemma 2.1

Let `B_1,...,B_4` be the four disjoint connected clique carriers in
`L`, and let distinct `s_i in S` represent their portal sets.  The bags

\[
B_i\cup\{s_i\}\quad(1\le i\le4)
\]

are disjoint, connected and pairwise adjacent.  If
`S-{s_1,...,s_4}={r_1,r_2,r_3}`, the other three bags

\[
P_j\cup\{r_j\}\quad(1\le j\le3)
\]

are disjoint and connected.  Two such packet bags are adjacent because
each `S`-full packet contacts the other bag's literal anchor.  Every
packet bag is adjacent to every carrier bag because it contacts that
carrier's literal anchor.  This is a literal seven-bag clique model.

The proof neither identifies a colour class with a branch bag nor
expands a contracted boundary label.

## 3. Audit of Lemma 2.2

For a lobe `C`, all exits in the whole graph lie in

\[
T\cup A(C),\qquad A(C)=N_S(C).
\]

Another lobe and the nonempty opposite shore survive outside this set,
so seven-connectivity gives `3+|A(C)|>=7`, hence `|A(C)|>=4`.

For the localized portal matching, let `m` be the maximum matching
order in the bipartite incidence graph `S--V(C)`.  The deficiency form
of Hall gives `U subseteq S` with

\[
m=7-|U|+|N_C(U)|.
\]

If `m<min{4,|C|}`, then `C-N_C(U)` is nonempty: otherwise the displayed
identity would give `m>=|C|`.  Deleting

\[
T\cup(S-U)\cup N_C(U)
\]

removes exactly `3+m<=6` vertices.  The remaining part of `C` has no
edge to `U`, no undeleted internal exit, and no edge to `R`; meanwhile
`R` remains nonempty.  This is a separator of order below seven.  The
matching bound `min{4,|C|}` is therefore correct.

## 4. Audit of Lemma 2.3: the delicate linkage step

When `|C|>=2`, Lemma 2.2 supplies distinct portal vertices `x,y in C`
matched to distinct literal labels `a,b in S`.

There are two vertex-disjoint paths from `{x,y}` to two distinct
vertices of `T`.  Here is a complete justification of the Menger step.
If no such linkage existed, the set-to-set form of Menger would give a
set `Z` of order at most one meeting every `{x,y}`--`T` path.  The empty
set is impossible.  If its sole vertex `z` lies outside
`{x,y} union T`, then `G[L]-z` separates both starts from `T`.  If
`z=x` (respectively `z=y`), then `G[L]-z` separates the other start from
`T`.  If `z in T`, then `G[L]-z` separates a start from the two
remaining members of `T`.  Each alternative contradicts
three-connectivity.  Since the two paths are vertex-disjoint, they use
different starts and different ends.

Stopping them at their first vertices of `T` leaves disjoint connected
initial segments wholly inside `C`, one containing `x` and one
containing `y`.  Their union can be joined by a shortest connector in
`C`, producing a tree, and that tree extends to a spanning tree of
`G[C]`.  Deleting one edge on the connector partitions `C` into
nonempty connected sets `X,Y`; the deleted tree edge is a literal
`XY` edge.  The two sets retain their distinct portal labels and their
contacts with two distinct gate vertices.  Thus every item asserted in
Lemma 2.3 follows.

## 5. Four-or-more-lobe case

For distinct lobes `C_0,C_1,C_2,C_3` and
`T={t_1,t_2,t_3}`, the four carriers

\[
C_0,\quad C_1\cup\{t_1\},\quad
C_2\cup\{t_2\},\quad C_3\cup\{t_3\}
\]

are connected and disjoint.  The central lobe contacts all three gate
vertices.  For `i ne j`, lobe `C_i` contacts gate vertex `t_j`, so every
pair of enlarged gate carriers is adjacent as well.  Each carrier has
at least four boundary labels.  Four subsets of a seven-set, each of
order at least four, satisfy Hall: the union of every nonempty
subfamily has order at least four, hence at least the size of that
subfamily.  Lemma 2.1 applies.

Unused lobes cause no interference.

## 6. Exactly three lobes with a nontrivial lobe

Apply Lemma 2.3 to the nontrivial lobe `C_1`, obtaining
`C_1=X dotcup Y`, distinct gate contacts `t_1,t_2`, and a literal
`XY` edge.  With `C_2,C_3` the other lobes, define

\[
B_1=X\cup\{t_1\},\quad
B_2=Y\cup\{t_2\},\quad
B_3=C_2\cup\{t_3\},\quad
B_4=C_3.
\]

All six carrier adjacencies are literal:

| pair | literal witness |
|---|---|
| `B_1B_2` | the `XY` edge |
| `B_1B_3` | an edge from `C_2` to `t_1` |
| `B_2B_3` | an edge from `C_2` to `t_2` |
| `B_1B_4` | an edge from `C_3` to `t_1` |
| `B_2B_4` | an edge from `C_3` to `t_2` |
| `B_3B_4` | an edge from `C_3` to `t_3` |

The first two carriers have the distinct labels `a,b`.  Since each of
`A(C_2),A(C_3)` has order at least four, one may choose

\[
c in A(C_2)-\{a,b\},\qquad
d in A(C_3)-\{a,b,c\}.
\]

These are four distinct representatives.  Lemma 2.1 yields a literal
`K_7`.

## 7. Exactly three singleton lobes

Here `L` consists of the three gate vertices and three singleton lobes,
so `|L|=6`.  Since `G[L]` is connected and there are no `LR` edges, it
is a component of `G-S`.  The audited actual-adhesion portal matching
theorem therefore gives an `S--L` matching saturating all six vertices
of `L`.  In particular, every gate vertex has a literal boundary
portal; choosing one gate vertex `t_3` and one such label `a` is valid.

For singleton lobes `c_0,c_1,c_2`, the carriers

\[
\{c_0\},\quad \{c_1,t_1\},\quad
\{c_2,t_2\},\quad \{t_3\}
\]

are connected and pairwise adjacent.  The first lobe sees all three
gate vertices, `c_1` sees `t_2,t_3`, and `c_2` sees `t_1,t_3`; these
give all six pairs.  Represent the last carrier by `a`.  Each singleton
lobe has at least four labels, so the other three carriers can be
represented greedily after excluding respectively at most one, two and
three already used labels.  The four representatives are distinct, and
Lemma 2.1 applies.

This case uses only the proved global portal matching theorem.  It does
not infer a rooted triangle in the complement of a lobe.

## 8. Two-lobe literal-edge proposition

For two lobes `C,D`, literal gate edge `uv`, and third gate vertex `w`,
the four carriers

\[
C,\quad D\cup\{w\},\quad \{u\},\quad \{v\}
\]

are disjoint, connected, and pairwise adjacent.  The two singleton gate
carriers are adjacent through `uv`; every other pair is witnessed by a
lobe-to-gate edge.  An SDR for the two gate portal sets supplies two
labels, and the two lobe label sets of order at least four supply two
further distinct labels.  The conclusion and the rank-one restriction
on every surviving literal gate edge are correct.

## 9. Exact promoted conclusion

Every actual three-cut has at least two lobes by definition.  Theorem
3.1 eliminates every cut with at least three lobes.  Hence the exact
remaining nonplanar gate cell has two lobes.  Each lobe meets every gate
vertex, has at least four literal boundary labels, and has localized
portal matching order `min{4,|C|}`.  Every literal gate edge has endpoint
portal rank at most one.

The note's final guardrail is consistent with, rather than used by, the
proof: the `K_{3,3}`-plus-one-edge example shows why no blanket
`T`-rooted-`K_3` assertion may be inserted into this argument.
