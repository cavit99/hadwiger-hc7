# Minimum-cut reduction for the marked three-clique problem

**Status:** active proof reduction.  Lemmas 1--3 below are proved.  Section 4
is the first equality residue left by the six-connected `H`-Wege proof; it is
not claimed to be impossible here.

## 1. Fan plus two full components

### Lemma 1 (four-fan decoder)

Let `H` be six-connected, let `S` be a six-vertex separator, and let

\[
                         L=\{z\}\mathbin{\dot\cup}Q\cong K_5,
                         \qquad z\in S.
\]

Suppose that `Q-S` is nonempty and is contained in a component of `H-S`,
with at least two other components.  Then `H` has a `K_7` minor.

#### Proof

Every component `D` of `H-S` has `N(D)=S`: otherwise `N(D)` is a separator
of order at most five.  Thus each of the two components not containing
`Q-S` is a connected `S`-full packet; call them `P_1,P_2`.

The graph `H-z` is five-connected.  Put `I=Q cap (S-z)` and first take the
trivial path at every vertex of `I`.  The graph `(H-z)-I` is
`(5-|I|)`-connected, so the set form of Menger's theorem supplies
`4-|I|` further mutually disjoint paths from `Q-I` to `(S-z)-I`, with
distinct starts and ends.  Together these are four disjoint paths whose
initial vertices are the four distinct vertices of `Q` and whose ends in
`S-z` are distinct.  Shorten every nontrivial path at its first
vertex in `S`.  Its internal vertices then lie in the single component of
`H-S` containing `Q-S`.  Denote the four shortened paths by `R_q` and their
four ends by `t_q`.

There is a unique vertex

\[
                  r\in S-(\{z\}\cup\{t_q:q\in Q\}).
\]

The following seven sets are disjoint connected branch sets:

\[
     V(R_q)\quad(q\in Q),\qquad \{z\},\qquad V(P_1)\cup\{r\},
     \qquad V(P_2).
\]

The four path bags are pairwise adjacent through the clique `Q`.  The
singleton `z` is adjacent to every path bag through `zq`, and to both packet
bags because the packets are `S`-full.  Each packet bag is adjacent to every
path bag through the corresponding vertex `t_q`.  Finally `P_2` has a
neighbour at `r`, which lies in the other packet bag.  These seven bags are
a `K_7` model.  \(\square\)

### Corollary 2 (binary minimum cuts)

Let `H` be six-connected and `K_7`-minor-free, and suppose it contains
three pairwise disjoint `K_5` cliques `L_i` with marked vertices
`z_i in L_i`.  If a six-separator `S` contains all three marks, then
`H-S` has exactly two components.

#### Proof

It has at least two components.  Fix `i`.  The set `L_i-S` is nonempty,
because otherwise `S` would contain the five vertices of `L_i` and the two
other, disjoint marks.  Since `L_i-S` is a clique, it lies in one component
of `H-S`.  Three or more components would let Lemma 1 use two components
other than this one.  \(\square\)

This is stronger than the bare statement that a minimum cut is full on
both sides: it gives the exact binary-shore conclusion needed before any
state or portal language is introduced.

## 2. The `|W|=6` Mader cell is impossible

Apply the Robertson--Seymour--Thomas form of Mader's `H`-path theorem to
the three disjoint cliques, with packing target seven, and choose the
certificate `(W;(Y_j,X_j))` by maximizing `|W|` and then the number of
nonempty cells.  Use Niu's standard auxiliary graph obtained from `H-W`
by deleting every edge internal to a cell `Y_j`, and let `A_i` be the union
of its components meeting `L_i`.

### Lemma 3

Under the marked-separator hypothesis

\[
 T\text{ a six-separator}\quad\Longrightarrow\quad
 \{z_1,z_2,z_3\}\subseteq T,                         \tag{2.1}
\]

one has `|W|<=5`.

#### Proof

If `|W|=6`, the Mader budget makes every `X_j` have order at most one.
At least two of the sets `A_i` are nonempty because the cliques are disjoint.
If, say, `A_1` were empty, then `L_1 subseteq W`; the other two `A`-sets
would lie in distinct components of `H-W`, so `W` would be a six-separator.
Condition (2.1) would put `z_2,z_3` in `W`, impossible because the five
vertices of `L_1` already occupy five of its six positions.  Thus all three
`A_i` are nonempty.  In this equality cell the auxiliary components
meeting distinct cliques are also contained in distinct components of
`H-W`.  Indeed, the certificate condition gives
`N(Y_j-X_j) subseteq W union Y_j`.  A cell with `X_j=emptyset` therefore
has no attachment to another cell, while a cell with `|X_j|=1` has at most
one gateway to the rest of `H-W`.  Restoring the deleted edges internal to
such a cell can attach material to one auxiliary component, but cannot
merge two auxiliary components meeting different cliques.  Hence `H-W`
has at least three components.  This contradicts Corollary 2 (and (2.1)).
\(\square\)

Thus Lemma 3 replaces the first use of claw-freeness in Niu's
six-connected proof.  It uses the literal marked-cut hypothesis rather
than an unlabelled degree estimate.

## 3. A second replacement: the low-`W` balanced branch

Continue with Niu's notation.  The nonempty `X_j` are odd.  Let `m` be the
number with order at least three, and set

\[
 B_i=A_i\cap(X_1\cup\cdots\cup X_m),
 \qquad |B_1|\le |B_2|\le |B_3|.
\]

The connectivity/counting part of the published proof, which uses neither
claw-freeness nor minimum degree seven, gives

\[
 |B_i|\ge5-|W|,
 \qquad
 |B_1\cup B_2\cup B_3|\le18-3|W|.                  \tag{3.1}
\]

If the lower bound is missed by one in every row, namely

\[
 |B_1|=|B_2|=|B_3|=6-|W|,                         \tag{3.2}
\]

then equality holds throughout the Mader count: `m=6-|W|`, all the large
cells have order three, and they partition the three `B_i`.

For `|W|<=1`, (3.2) is impossible under (2.1) and `K_7`-minor exclusion.
Indeed, if `A_i-B_i` were nonempty, `W union B_i` would be a six-cut.  For
`|W|<=1` it cannot contain the two marks lying in the other two `A`-sets,
so `A_i=B_i` for every `i`.  Also `Y_j=X_j` for every cell: otherwise
`W union X_j` would be a separator of order at most four.  Moreover

\[
                         |B_i\cap X_j|=1             \tag{3.3}
\]

for every large cell.  If an intersection had order at least two, then
`W union (B_i triangle X_j)` would have order at most five.  It separates
the nonempty set `B_i cap X_j` from a vertex of another `B`-row outside
`X_j`, contradicting six-connectivity.

When `W` is empty, every terminal vertex `q in L_i` has all its neighbours
in `(B_i-q) union (X_j-B_i)`, where `X_j` is its cell, a set of order at
most seven.  If an unmarked `q` has degree six, its neighbourhood is a
six-cut and (2.1) forces the two other marks to be the two cross-cell
vertices.  The marked vertex `q=z_i` cannot have degree six, because the
six-cut `N(q)` omits the required mark `q`; it therefore has degree seven.
Every terminal vertex is consequently adjacent to both other vertices of
its cell.  Each `B_i` is connected: it contains the clique `L_i`, and its
possible sixth vertex is adjacent to `z_i`, which sees its entire
seven-vertex envelope.  The five vertices of `L_1` occupy five distinct
large cells, so one of these cells has an edge between, say, `B_1` and
`B_2`.  Then the five singleton vertices of `L_3`, together with the two
connected bags `B_1,B_2`, form a `K_7` model.

When `|W|=1`, the same construction absorbs the unique vertex of `W` into
the `B_i` belonging to its clique (if it belongs to one).  Every member of
`L_i-W` sees both cross-cell vertices by the preceding degree argument, so
choose a cross-cell edge incident with that `B_i` and use the third clique
as the five singleton core.  By (3.3), the members of the clique `L_i-W`
lie in distinct cells, so their clique edges survive in the auxiliary
graph.  Hence all components used in the definition of `A_i=B_i` coincide,
and `B_i` is connected; adding `W` preserves connectivity through
`L_i-W`.  The other external `B`-bag is a literal clique.  A core vertex
`q` has all neighbours in the seven-vertex set consisting of `W`, the
other four vertices of its own `B`-set, and the two cross-cell vertices.
If `d(q)>=7`, it sees the whole envelope.  If `d(q)=6`, its neighbourhood
is a six-cut and hence contains all three marks.  The mark in either
external label is therefore the corresponding cross-cell vertex, except
that the mark may itself be the vertex of `W` already absorbed in the
first external bag.  Thus `q` contacts both external bags in every case.
If `W` belongs to no clique, all three `B_i` are literal cliques; no
absorption is needed and any cross-cell edge chooses the two external bags.
Thus (3.2) again gives a literal `K_7`.

Consequently the marked-cut hypothesis replaces Niu's combined
claw/minimum-degree argument through the complete `|W|<=1` balanced
branch.

## 4. Exact live equality residue

What remains of (3.2) is sharply confined to

\[
 2\le |W|\le5,
 \quad m=6-|W|,
 \quad |X_1|=\cdots=|X_m|=3,
 \quad |B_i|=6-|W|.                                \tag{4.1}
\]

For every `i` with `A_i-B_i` nonempty, `W union B_i` is a six-cut.
Condition (2.1) therefore implies

\[
             \{z_1,z_2,z_3\}-W\subseteq B_i.       \tag{4.2}
\]

Since the `A_i`, and hence the `B_i`, are disjoint, (4.2) has two immediate
global consequences:

* one nonempty tail `A_i-B_i` forces `W` to contain the two marks with
  labels different from `i`;
* two tails with different labels force `W` to contain all three marks.

The equality residue therefore has only the following two unlabelled
forms.

* If `|W|=2`, exactly one tail is nonempty.  Indeed, no tail would require
  `W` to meet all three disjoint cliques, while two tails would force all
  three marks into `W`.  After relabelling,

  \[
       W=\{z_2,z_3\},\qquad A_2=B_2=L_2-z_2,
       \qquad A_3=B_3=L_3-z_3,                     \tag{4.3}
  \]

  while `A_1-B_1` is nonempty.
* If `3<=|W|<=5`, all three tails are nonempty and
  `\{z_1,z_2,z_3\} subseteq W`.  For if `A_i=B_i`, then
  `L_i-W subseteq B_i` and `|B_i|=6-|W|`, so
  `|W cap L_i|>=|W|-1`.  If the other two rows have tails, their cuts force
  all three marks into `W`; the tail-free row and the two marks outside its
  clique then occupy at least `(|W|-1)+2>|W|` distinct vertices.  If two
  rows are tail-free, their disjoint cliques alone require at least
  `2(|W|-1)>|W|` vertices of `W`.  Hence no row is tail-free, and two of
  the three tails force all three marks into `W`.

This is the first unresolved equality residue of the marked adaptation.
It is not the terminal `5+5+5` matrix cell (which is already audited and
excluded); it is a binary-shore, marked-six-cut composition problem.  A
proof must compose the crossing six-cuts in (4.2), or return the `K_7`
directly.  Replacing the resulting independent neighbours by a generic
"claw-free" contradiction is not available.

## 5. Trust boundary

Proved here:

* the four-fan/two-packet `K_7` decoder;
* every marked six-cut in a `K_7`-minor-free candidate is binary;
* elimination of the `|W|=6` Mader branch; and
* elimination of the balanced equality branch when `|W|<=1`.

Not proved here:

* the crossing-cut composition required by (4.1)--(4.2);
* the marked three-clique theorem; or
* the global support-six theorem.
