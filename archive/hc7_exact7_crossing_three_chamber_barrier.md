# Three proper-minor response types do not synchronize an exact-seven interface

**Status:** written finite counterarchitecture; deterministic verifier in
[`hc7_exact7_crossing_three_chamber_barrier_verify.py`](hc7_exact7_crossing_three_chamber_barrier_verify.py);
separate independent audit in
[`hc7_exact7_crossing_three_chamber_barrier_audit.md`](hc7_exact7_crossing_three_chamber_barrier_audit.md).
This graph is not a counterexample to `HC_7`: it contains a `K_7` minor and
is not minor-minimal subject to being non-six-colourable.

## 1. Statement

There is a seven-connected, seven-chromatic graph `G` with an actual
order-seven separation

\[
        V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B
\]

having all of the following properties.

1. Both open shores are connected and adjacent to every literal vertex of
   `S`, and their maximum boundary-full connected-subgraph packing numbers
   are

   \[
                         (\nu_A,\nu_B)=(2,1).
   \]

2. The boundary graph is four-colourable.
3. Two vertex-disjoint edges

   \[
                         e=ab,\qquad f=cd
   \]

   cross from the same connected open shore `A` to `S`.
4. The common deletion `G-{e,f}` has six-colourings of exactly the three
   endpoint-equality types

   \[
     (\mathsf{equal},\mathsf{equal}),\quad
     (\mathsf{equal},\mathsf{proper}),\quad
     (\mathsf{proper},\mathsf{equal});
   \]

   the fourth type is absent.  The two single-edge deletions and
   contractions, and the double contraction, are all exactly
   six-chromatic.
5. Every colouring in all three response types induces the same equality
   partition `Pi` on `S`.  The singleton shore `B` realizes `Pi`, while
   the intact `A`-closed shore rejects it.
6. The full-subgraph demand of `Pi` is two, strictly greater than
   `nu_B=1`.  Thus the selected response has the same Hall-demand
   obstruction as the active exact-seven branch.
7. The common response host contains a `K_6` subgraph.

Consequently the exact boundary order, the packing vector, four-colourable
boundary, excessive demand, two correctly placed crossing edges, and all
three proper-minor response types do not by themselves give a common
partition of the two intact closed shores.  Any positive theorem needs
additional global information excluding this construction.  In the active
`HC_7` setting, the available inputs are `K_7`-minor exclusion and the
six-colourability of every proper minor.

## 2. The four-colour core

Start with vertices

```text
a b ap bp pa qa pb qb c d.
```

On `a,ap,pa,qa`, put a diamond whose missing edge is `a ap`; explicitly,

```text
pa qa,  a pa, a qa,  ap pa, ap qa.
```

Put the analogous diamond on `b,bp,pb,qb`, with missing edge `b bp`.
Join each of `c,d` to both `ap,bp`, and add

\[
                         e=ab,\qquad f=cd.             \tag{2.1}
\]

Call this graph `J`, and put `J_0=J-{e,f}`.

In every proper three-colouring of a diamond, the ends of its missing edge
have the same colour.  Hence the colouring constraints of `J` on the four
effective vertices `a,b,c,d` are those of `K_4`, with `e,f` as a matching.
It follows that

* `chi(J)=4`;
* `J-e` and `J-f` are three-colourable;
* `J_0` realizes exactly `EE`, `EP`, and `PE`; and
* `PP` is impossible.

Moreover, `b` and `d` have different colours in every three-colouring of
`J_0`: the edge `bp d`, together with the forced equality `b=bp`, proves
this literally.

## 3. The exact-seven lift

Add a triangle

\[
                         T=\{t_0,t_1,t_2\}
\]

complete to `J`.  Add two nonadjacent vertices `w_0,w_1`, each complete to
`J` and adjacent to `t_1,t_2` but not to `t_0`.  Finally add a vertex
`ell` adjacent precisely to

\[
              S=\{b,d,t_0,t_1,t_2,w_0,w_1\}.          \tag{3.1}
\]

Take

\[
\begin{aligned}
 A&=\{a,ap,bp,pa,qa,pb,qb,c\},\\
 B&=\{ell\}.
\end{aligned}                                         \tag{3.2}
\]

There is no `A-B` edge.  Both open shores are connected and each is
adjacent to every vertex of `S`.  The two distinguished edges have the
required placement

\[
                         a,c\in A,\qquad b,d\in S.     \tag{3.3}
\]

### 3.1 Connectivity

The graph induced by `J union T union {w_0,w_1}` is seven-connected.  If
at most six vertices are deleted and both `J` and
`T union {w_0,w_1}` survive, their complete join connects the remainder.
All ten vertices of `J` cannot be deleted; if all five vertices outside
`J` are deleted, at most one vertex is additionally deleted from the
two-connected graph `J`.

If `ell` survives a deletion of at most six vertices, at least one of its
seven neighbours survives and joins it to that connected core.  Thus `G`
is seven-connected.  Deleting the displayed set `S` isolates `ell` from
the nonempty connected set `A`, so (3.1)--(3.2) are an actual order-seven
separation.

### 3.2 Chromatic number

The subgraph `T vee J` has chromatic number `3+4=7`.  Conversely, in a
seven-colouring use four colours on `J`, three new colours on `T`, and the
colour of `t_0` on `w_0,w_1`.  At most two of the four core colours occur
on `b,d`, so one of the other core colours is available for `ell`.
Therefore

\[
                              \chi(G)=7.               \tag{3.4}
\]

This already exposes one omitted global hypothesis: deleting `ell` leaves
the seven-chromatic subgraph `T vee J`.  Thus `G` is not minor-minimal.

## 4. Packing and boundary demand

Every vertex of `A` is adjacent to all five vertices
`T union {w_0,w_1}`.  Its neighbours at the two remaining boundary
vertices are

\[
\begin{aligned}
 N_A(b)&=\{a,pb,qb\},\\
 N_A(d)&=\{c,ap,bp\}.
\end{aligned}                                         \tag{4.1}
\]

The connected sets

\[
                       \{a,pa,ap\},\qquad \{pb,bp\}   \tag{4.2}
\]

are disjoint and `S`-full.  Conversely, every connected `S`-full subset
of `A` contains a path from the first set of portals in (4.1) to the
second.  Every such path meets `\{ap,bp\}`.  Hence no three such subsets
are disjoint, proving `nu_A=2`.  The singleton `ell` is `S`-full, so
`nu_B=1`.

The boundary contains the `K_4` on `b,t_0,t_1,t_2`, and it has the proper
four-colouring in which `b,d` share one colour, `T` uses three colours,
and `w_0,w_1` use the colour of `t_0`.  Thus `chi(G[S])=4`.

Every response colouring induces

\[
 \Pi=
 \bigl\{
   \{t_0,w_0,w_1\},\{t_1\},\{t_2\},\{b\},\{d\}
 \bigr\}.                                             \tag{4.3}
\]

The singleton vertices of this partition induce `K_4-bd`, whose clique
number is three.  Therefore

\[
 d_{G[S]}(\Pi)=|\Pi|-3=5-3=2>\nu_B.                   \tag{4.4}
\]

## 5. The three response types have one boundary partition

Take any three-colouring of `J_0`, give `t_0,t_1,t_2` three new colours,
and give `w_0,w_1` the colour of `t_0`.  The vertices `b,d` use two
different core colours, so the third core colour is absent from `S`; give
that colour to `ell`.  This is a proper six-colouring of `G-{e,f}`, and
its boundary partition is exactly (4.3).

The core analysis supplies all three endpoint signatures.  Restricting to
`J-e` gives `EP`, restricting to `J-f` gives `PE`, and identifying both
equal endpoint pairs gives the `EE` double-contraction response.  The
triangle `T` together with `a,pa,qa` is a `K_6` in every common response
host.  Hence each named deletion and contraction is exactly
six-chromatic, not merely at most six-chromatic.

The opposite singleton shore realizes (4.3): its vertex receives the
sixth colour absent from the boundary.  The intact `A`-closed shore rejects
every six-colouring, since it contains `T vee J`.  Thus the three chambers
agree perfectly on one high-demand boundary partition and still do not
synchronize the two intact closed shores.

## 6. Exact trust boundary

The following seven connected branch sets form an explicit `K_7`-minor
model:

\[
 \{t_0\},\ \{t_1\},\ \{t_2\},\
 \{a,pa,ap\},\ \{b,pb,bp\},\ \{c\},\ \{d\}.          \tag{6.1}
\]

Thus the construction has both terminal defects deliberately excluded in
the active branch:

1. `K_7 \preccurlyeq G`; and
2. the proper minor `G-ell` is still seven-chromatic.

It therefore does not refute a terminal-disjunctive theorem for a
hypothetical minor-minimal `HC_7` counterexample.  It does prove a precise
dependency statement:

> Even when all three available response types induce the **same**
> excessive-demand partition at the correct literal order-seven boundary,
> common-partition closure does not follow from the response lattice,
> packing vector, boundary chromatic number, or crossing-edge placement.
> Any positive theorem needs additional global information excluding this
> construction.  In the active `HC_7` setting, the available inputs are
> `K_7`-minor exclusion and further proper-minor colourings; these are the
> natural sources of a labelled branch-set allocation, a common boundary
> partition, or a strict response-preserving descent.

## 7. Verification

Run from the repository root:

```text
python3 archive/hc7_exact7_crossing_three_chamber_barrier_verify.py
```

Expected output:

```text
GREEN exact-seven crossing three-chamber barrier
kappa=7 boundary=7 chi_boundary=4 packing=(2,1)
two vertex-disjoint boundary-to-shore edges; chambers=EE,EP,PE; PP absent
all chambers induce one five-block boundary partition of demand=2>1
opposite singleton shore accepts the partition; intact operated shore rejects it
common response host contains K6; full host contains K7 minor
```
