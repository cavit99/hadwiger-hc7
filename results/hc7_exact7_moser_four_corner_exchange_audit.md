# Independent audit: pure-Moser four-corner exchange

Audited file: `hc7_exact7_moser_four_corner_exchange.md`.

**Verdict:** **GREEN.**

Under its stated exact two-component hypotheses, the note proves that every
two-connected exterior component of order at least three is impossible.  A
single application of the already-audited four-port theorem supplies one of
the two complementary corner matchings, and the proper-minor colourings
produce and reproduce the same exact boundary state.  No favourable
five-root crossing or compatibility of separately chosen rural embeddings
is assumed.

## 1. Hypotheses

The file now states all hypotheses used by the proof: `G` is
seven-connected, strongly seven-contraction-critical, and `K7`-minor-free;
`N(v)=S` is the literal Moser spindle; and

\[
                         G-N[v]=C\mathbin{\dot\cup}D
\]

has exactly two nonempty connected components.  Thus `C,D` are
anticomplete and `S`-full, and the two closed shores cover all of `G-v`.

## 2. Exact carrier exchange

For orientations `{a,x}={1,2}` and `{b,y}={3,4}`, put

\[
                         r=\{a,y\},\qquad e=\{x,b\}.
\]

Both are independent left-right pairs.  The simultaneous contraction of
`{v} union r` and `C union e` is a proper minor: the sets are disjoint,
connected, and adjacent.  On restriction to the closed `D`-shore, only the
independent literal blocks `r,e` are expanded.

Both contracted representatives see every one of `0,5,6` and see one
another.  Since the only edge on `{0,5,6}` is `56`, the exact boundary
partition is one of

```text
R0 = r | e | 0  | 5 | 6
R5 = r | e | 05 | 6
R6 = r | e | 06 | 5.
```

Suppose disjoint adjacent connected carriers `X,Y` contact respectively
the two vertices of `r,e`.  Contract `X union r`, `Y union e`, and the star
on `v union I_q`, where `I_0={0}`, `I_5={0,5}`, and `I_6={0,6}`.  Every
carrier contains one left corner, which sees `6`, and one right corner,
which sees `5`.  The displayed block representatives consequently form a
literal `K5` for `q=0` and a literal `K4` for `q=5,6`.  Their colours are
pairwise distinct, so restriction to the closed `C`-shore induces exactly
`R_q`, not a coarsening.

Choosing the returned `q`, a palette permutation aligns the two shore
colourings on every literal of `S`.  They glue because `C,D` are
anticomplete.  At most five colours occur on `S`, leaving a sixth colour
for `v`.  Every pullback expands only an independent literal block; there
is no colour-to-branch-set identification.

## 3. Two-connected rural carrier lemma

Let `D` be two-connected with `|D|>=3`, and suppose its literal four-root
closure has a disk embedding with boundary order `a,x,b,y`.

For either same-side pair `T={a,x}` or `T={b,y}`, the inequality

\[
                         |N_D(T)|\ge2
\]

is forced by seven-connectivity: otherwise
`N_D(T) union (S-T)` is an at-most-six cut, and `D-N_D(T)` is nonempty.
Since each individual portal set is nonempty, distinct representatives can
be chosen for each pair.  The literal edges `ax=12` and `by=34` then add two
ears with distinct ends to the two-connected graph `D`; the whole
four-root closure is two-connected.

Its outer-face boundary is therefore a cycle.  In order `a,x,b,y`, the
consecutive pairs `a-y` and `x-b` are Moser nonedges.  Their open facial arcs
have disjoint, nonempty, connected interiors in `D`.  A shortest path in
connected `D` enlarges one interior until the two carriers are adjacent,
while preserving disjointness and all endpoint contacts.  This proof is
valid for `D=K3`; no three-connectivity assumption remains.

## 4. Single four-port application

Apply the GREEN seven-boundary four-port linkage-or-disk theorem to the
ordered roots `(1,2,3,4)` in `D`.  Its far side contains `C` and `v`, and
fullness supplies every root portal.

* In the linkage outcome, disjoint paths join `1-3` and `2-4`.  Their
  interiors are nonempty because `13,24` are absent, and adjacent
  enlargement supplies carriers for `13|24`.
* In the rural outcome, one literal disk embedding has boundary order
  `(1,2,3,4)`.  Section 3 supplies carriers for `14|23`.

Both matchings consist of independent left-right pairs and feed the exact
exchange in Section 2.  The outcomes are exhaustive, proving Theorem 4.1.

The only external mathematical dependency specific to this theorem is the
already-audited four-port linkage-or-disk result in
`results/hc7_moser_crossing_carrier.md`; adjacent enlargement and the
two-ear step are elementary.  No computation is used here.
