# Exact-seven thin-shore exchange

## Status and scope

This proved and independently audited note attacks only the extremal actual-adhesion cell

\[
                 (\nu_L,\nu_R)=(1,3).                 \tag{0.1}
\]

Here `G` is a 7-connected, `K_7`-minor-free graph which is strongly
7-contraction-critical (`chi(G)=7` and every proper minor is
6-colourable), `S` is the literal boundary of an actual separation, `|S|=7`,
and both open shores are nonempty.  The open shore `L` is connected and
contains no two disjoint `S`-full packets, while the other shore `R`
contains three pairwise disjoint `S`-full packets.

The independently audited exact-seven full-packet theorem
(`results/hc7_exact_seven_packet_packing.md`) is used as an input.  In
particular, the input says that `G[S]`
is triangle-free and that no admissible one-block equality partition of
`S` exists.  An admissible partition is

\[
 S=I_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}I_m
     \mathbin{\dot\cup}Q,                              \tag{0.2}
\]

where each `I_i` is independent of order at least two and `Q` is a
clique whose vertices are singleton colour classes.  Each shore with
`m` disjoint full packets funds the exact state (0.2) by proper-minor
contraction and restriction to the untouched opposite shore.

The main result below eliminates an infinite family, rather than another
finite list:

> **A surviving thin shore is 2-connected.**

More generally, any two disjoint adjacent connected pieces in the thin
shore, each missing at most one literal boundary vertex,
already gives a literal `K_7` or an exact opposite-shore equality-state
splice.  The proof also identifies the only apparent exceptional
boundary pattern and closes it rather than naming it as a new gap.

The remaining cell is therefore a genuinely 2-connected labelled
society.  Section 4 gives an additional exact restriction at each of its
2-cuts.

## 1. The two-near-full-piece exchange

For a connected subgraph `X` of the open shore put

\[
 D(X)=S-N_G(X).
\]

### Theorem 1 (near-full split closes the `(1,3)` cell)

Assume (0.1).  Suppose `X,Y\subseteq L` are disjoint nonempty connected
vertex sets, there is an `XY` edge, and

\[
                     |D(X)|\le 1,\qquad |D(Y)|\le1.      \tag{1.1}
\]

Then `G` contains a `K_7` minor or `G` is 6-colourable.  In particular,
this configuration cannot occur in the counterexample-derived setting.

#### Proof

Let `P_1,P_2,P_3` be disjoint `S`-full packets in `R`, and put

\[
                     C=N_S(X)\cap N_S(Y).                \tag{1.3}
\]

By (1.1), `|C|\ge5`.

**Case 1: `G[C]` has an edge `qq'`.**

Choose distinct

\[
                     r_1,r_2,r_3\in C-\{q,q'\}.
\]

The following are seven literal branch sets:

\[
 P_1\cup\{r_1\},\quad P_2\cup\{r_2\},\quad
 P_3\cup\{r_3\},\quad X,\quad Y,\quad\{q\},\quad\{q'\}.
                                                               \tag{1.4}
\]

They are disjoint and connected.  The first three are pairwise adjacent
because every `P_i` contacts every literal vertex of `S`.  Each is
adjacent to `X` and `Y` through its anchor `r_i`, and to `q,q'` by
fullness.  The sets `X,Y` are adjacent by hypothesis and each contacts
both `q,q'`.  Finally `qq'` is an edge.  Thus (1.4) is a literal
`K_7` model.

We may consequently assume that `C` is independent.

**Case 2: one defect is empty, or the defects coincide.**

Then `S-\{d\}` is independent for some `d\in S` (with arbitrary `d`
if both defects are empty).  Hence

\[
                       I=S-\{d\},\qquad Q=\{d\}          \tag{1.5}
\]

is an admissible one-block partition.  One full packet on each shore
funds (1.5), and the two proper-minor colourings splice on the literal
boundary.  This 6-colours `G`, contrary to the setting.

We may therefore write

\[
                D(X)=\{a\},\qquad D(Y)=\{b\},\qquad a\ne b.  \tag{1.6}
\]

Now `C=S-\{a,b\}` is independent.  If `ab` is an edge, then

\[
                       I=C,\qquad Q=\{a,b\}              \tag{1.7}
\]

is again an admissible one-block partition, giving the same
contradiction.  Thus `ab` is not an edge.  It follows that every boundary
edge has one end in `\{a,b\}` and the other in `C`.

**Case 3: `a` and `b` have a common neighbour in `C`.**

If both have boundary degree one, with common neighbour `c`, then

\[
                     I=S-\{a,c\},\qquad Q=\{a,c\}        \tag{1.8}
\]

is an admissible one-block partition: `I` is independent because `C` is
independent, `ab` is absent, and the only boundary edge at `b` is `bc`,
whose other end was deleted.  This again splices to a 6-colouring.

Otherwise, by symmetry, `a` has two distinct neighbours `c,x\in C`.
Choose `c` for the boundary edge `ac` and use the other neighbour `x`
to enlarge `X`.  Let

\[
             \{r_1,r_2,r_3\}=S-\{a,b,c,x\}.              \tag{1.9}

These three vertices all belong to `C`, so `Y` contacts them.  The seven
branch sets

\[
 P_1\cup\{r_1\},\quad P_2\cup\{r_2\},\quad
 P_3\cup\{r_3\},\quad X\cup\{x\},\quad Y,
 \quad\{a\},\quad\{c\}                                  \tag{1.10}

form a literal `K_7` model.  Indeed, `X\cup\{x\}` is connected because
`x\in C\subseteq N_S(X)`; it sees `a` through the edge `xa` and sees
`c` directly from `X`.  The set `Y` contacts both `a` and `c`, since it
misses only `b`.  It contacts all three `r_i`.  Each full packet sees
`x,a,c` and every other anchor, so all remaining adjacencies in (1.10)
are immediate.  The singleton pair is adjacent through `ac`.

**Case 4: `a` and `b` have no common neighbour in `C`.**

Put

\[
 \begin{aligned}
 J_X&=\{b\}\cup N_S(a),\\
 J_Y&=\{a\}\cup N_S(b),
 \end{aligned}                                             \tag{1.11}
\]

and distribute the vertices of

\[
                  C-(N_S(a)\cup N_S(b))                    \tag{1.12}

arbitrarily between `J_X,J_Y`, subject to both sets having order at
least two.  Such a distribution exists unless one of the two initial
sets in (1.11) is a singleton and (1.12) is empty.  (If both initial
sets are singletons, then (1.12) has order five, so there is no
exception.)  In the exceptional event `S-\{b\}` or `S-\{a\}` is
independent, respectively, and an admissible one-block partition already
gives a 6-colouring.  Hence we may take both blocks nontrivial.

The two sets are independent: `C` is independent, `ab` is absent, and
the assumption `N_S(a)\cap N_S(b)=\varnothing` says that `b` has no
neighbour in `N_S(a)` and `a` has no neighbour in `N_S(b)`.  Moreover
`X` contacts every vertex of `J_X`, because the only boundary vertex it
misses is `a`; symmetrically `Y` contacts every vertex of `J_Y`.

Contract the two disjoint connected sets

\[
                       X\cup J_X,qquad Y\cup J_Y          \tag{1.13}

in a proper minor.  They are adjacent through the given `XY` edge, so
every 6-colouring of the minor restricts to a proper colouring of the
untouched `R` shore whose exact equality partition on literal `S` is

\[
                              S=J_X\dot\cup J_Y.            \tag{1.14}

Conversely, two of the three full packets in `R` fund exactly (1.14)
on the untouched `L` shore.  Permuting the two used colour names and
the unused palette colours makes the two colourings agree on every
literal boundary vertex.  They splice to a 6-colouring of `G`.

All cases close. \(\square\)

### Audit note on the state splice

The two sets in (1.13) include all seven literal boundary vertices, but
they need not include all of `L`.  No contracted carrier is expanded on
the side containing it: the colouring of that minor is restricted only
to `R` and to the equality classes represented by `J_X,J_Y`, so every
unused vertex of `L` is simply discarded from that restriction.  The
reverse operation lies entirely in `R` and its colouring is restricted
to all of `L` together with the literal boundary.  Thus there is no
palette-to-row identification and no illicit expansion of an internal
packet.

## 2. All non-2-connected thin shores close

### Corollary 2.1 (cutvertex closure)

Under (0.1), if `L` has a cutvertex, then the configuration closes by
Theorem 1.

#### Proof

Let `z` be a cutvertex and let `C_1,C_2` be two distinct components of
`L-z`.  For every component `C` of `L-z`,

\[
                         N_G(C)\subseteq S\cup\{z\}.
\]

Seven-connectivity therefore gives `|N_S(C)|\ge6`.

Take `X=C_1` and `Y=L-C_1`.  The set `Y` is connected, it contains
`C_2`, and it is adjacent to `X` through `z`.  Thus

\[
                         |N_S(X)|\ge6,qquad |N_S(Y)|\ge6.
\]

Theorem 1 applies. \(\square\)

### Corollary 2.2 (the singleton shore is impossible)

The open thin shore cannot consist of one vertex.

#### Proof

Suppose `L=\{x\}`.  Actual separation and `S`-fullness give
`N_G(x)=S`, so `d_G(x)=7`.  Dirac's neighbourhood inequality for a
7-contraction-critical graph gives

\[
                         \alpha(G[N(x)])\le2.               \tag{2.1}

But the packet theorem gives that `G[S]` is triangle-free.  By
`R(3,3)=6`, every triangle-free graph on seven vertices has an
independent set of order at least three, contradicting (2.1). \(\square\)

### Corollary 2.3 (structural residue)

Every surviving `(1,3)` thin shore is 2-connected and has at least three
vertices.

Indeed, Corollaries 2.1 and 2.2 leave only the possible two-vertex
connected shore.  If `L=xy`, then seven-connectivity gives
`d_G(x),d_G(y)\ge7`; since neither vertex has a neighbour in the opposite
open shore, each has at least six neighbours in `S`.  The split
`X=\{x\}`, `Y=\{y\}` therefore satisfies Theorem 1 and closes as well.

This eliminates every tree, every block chain with at least two blocks,
and every graph with a proper pendant block, irrespective of its order.

## 3. The exact two-carrier criterion in the 2-connected residue

The preceding proof also isolates the constructive target inside a
2-connected shore.

### Lemma 3.1 (block-terminal carriers give the matching state)

Let

\[
                         S=I_1\dot\cup I_2\dot\cup Q       \tag{3.1}

be an admissible partition with two nontrivial blocks.  Suppose `L`
contains disjoint connected subgraphs `T_1,T_2` such that `T_i` contacts
every literal vertex of `I_i`.  Assume also that

1. either `T_1,T_2` are adjacent or there is an `I_1I_2` edge in
   `G[S]`; and
2. for every `q in Q` and `i in {1,2}`, either `T_i` contacts `q` or
   `q` has a neighbour in `I_i`.

Then an operation in `L` funds the exact state (3.1) on `R`, and hence
`G` is 6-colourable.

#### Proof

Each `T_i\cup I_i` is connected, because every vertex of `I_i` has a
neighbour in `T_i`; the two sets are disjoint.  Contract both in a
proper minor.  The two contracted representatives are adjacent by
hypothesis 1.  Hypothesis 2 makes each representative adjacent to every
literal vertex of `Q`; and `Q` is a clique.  Hence the representatives
together with `Q` form a clique, so a six-colouring of this proper minor,
restricted to `R\cup S`, induces exactly the equality partition (3.1).
Conversely, two of the three disjoint full packets in `R` fund exactly
the same state on `L\cup S` by the packet-contraction lemma.  Align the
block colours by a palette permutation and glue the two closed-shore
colourings. \(\square\)

The final sentence records an essential guard: merely connecting the two
independent blocks is not enough when `Q` is nonempty.  The desired
block-terminal Two-Paths theorem must preserve contacts to every
singleton in `Q` as well as mutual carrier adjacency.  When `Q` is empty,
the lemma has no extra qualification.

## 4. What a 2-cut is allowed to look like

The next result does not close every 2-cut, but it removes all
high-multiplicity incoherent 2-cut families through the same reusable
exchange principle.

### Proposition 4.1 (coherent defect pairs at a many-lobe 2-cut)

Let `L` be a surviving 2-connected thin shore, let `\{p,q\}` be a
2-cut, and let `C_1,\ldots,C_k` be the components of
`L-\{p,q\}`.  Put

\[
                           D_i=S-N_S(C_i).                  \tag{4.1}

Then `|D_i|\le2` for every `i`.  Moreover:

* if `k\ge4`, some two-group division closes by Theorem 1 unless one
  2-set `D` occurs as `D_i` for at least `k-1` indices;
* for `k=2`, the displayed lobe-intersection certificate guarantees
  closure when both defects have order at most one;
* for `k=3`, that certificate guarantees closure unless either all three
  defects have order two, or the unique defect of order at most one is
  accompanied by two equal defect 2-sets.

Thus an unbounded family of lobes behind one 2-cut can survive only by
carrying one coherent missing boundary pair on all but at most one lobe.

#### Proof

Because `L` is 2-connected, every `C_i` has a neighbour at each of
`p,q`.  Since

\[
                          N_G(C_i)\subseteq S\cup\{p,q\},
\]

seven-connectivity gives `|N_S(C_i)|\ge5`, proving `|D_i|\le2`.

For a nonempty index set `A`, the union of the lobes indexed by `A`
has boundary defect

\[
                 S-N_S\!\left(\bigcup_{i\in A}C_i\right)
                       =\bigcap_{i\in A}D_i.               \tag{4.2}

Partition `\{1,\ldots,k\}` into nonempty sets `A,B`, and define

\[
 X=\{p\}\cup\bigcup_{i\in A}C_i,qquad
 Y=\{q\}\cup\bigcup_{i\in B}C_i.                          \tag{4.3}

Both sets are connected; they cover `L`, and they are adjacent because
each lobe has neighbours at both cut vertices.  If

\[
                        \left|\bigcap_{i\in A}D_i\right|\le1,
 \qquad
                        \left|\bigcap_{i\in B}D_i\right|\le1,             \tag{4.4}

then Theorem 1 closes the configuration.

It remains only a finite set-family observation.  Call a nonempty group
bad when its defect intersection has order two.  Since every `D_i` has
order at most two, a group is bad **exactly** when all its members are
copies of one fixed 2-set.

Assume `k\ge4` and no 2-set occurs `k-1` times.  If at least two of the
`D_i` have order at most one, put one in each group.  If exactly one does,
put it alone in the first group; the remaining 2-sets are not all equal,
so the second group is not bad.  If all `D_i` are 2-sets, choose a most
frequent value `D` and a distinct value `E`, and put one copy of each in
the first group.  The complement still contains two distinct values:
this is immediate unless `D` occurred `k-2` times, and in that extremal
case the complement contains the remaining `k-3` copies of `D` and the
second non-`D` member.  Thus neither group is bad and (4.4) holds.

Conversely, if one 2-set occurs at least `k-1` times, every division
leaves some group consisting only of copies of that 2-set; the proposition
asserts only necessity, not that every such concentrated family really
survives.  For `k=2`, both groups are singletons, so the raw
lobe-intersection test certifies (4.4) when both defects have order at
most one.  For `k=3`, one group is a singleton.  It is good only if its
defect has order at most one, and then the complementary pair is bad
exactly when its two defects are equal 2-sets.  This gives the stated
classification for the displayed certificate.  Contacts from `p` or
`q` to `S` can only shrink the actual defects of the sets in (4.3), so
they may close some of the listed exceptional raw patterns as well.
\(\square\)

### Proposition 4.2 (a repeated defect pair closes)

In the setting of Proposition 4.1, suppose `k\ge3` and two components,
say `C_1,C_2`, have the same defect 2-set

\[
                         D_1=D_2=\{a,b\}.                 \tag{4.5}
\]

Then the configuration closes by Theorem 1.

#### Proof

Let

\[
 H=L\left[\{p,q\}\cup\bigcup_{i=3}^k V(C_i)\right].     \tag{4.6}
\]

Every component `C_i` has a neighbour at each of `p,q`.  Consequently
`H+pq` is 2-connected.  For completeness, deletion of `p` or `q`
leaves the other cut vertex joined to every lobe.  If an internal vertex
`z` of one lobe is deleted, every component of that lobe minus `z` has
a neighbour at `p` or `q`; otherwise `z` would be a cutvertex of the
2-connected graph `L`.  The added edge `pq` then joins all remaining
pieces.

All neighbours in `L` of `a` and `b` lie in `H`, because `C_1,C_2`
miss both vertices.  The two portal sets

\[
                 A=N_L(a)\cap V(H),\qquad
                 B=N_L(b)\cap V(H)                       \tag{4.7}
\]

have distinct representatives.  Indeed, `L` is `S`-full, so both are
nonempty.  If they had no distinct representatives, then
`A=B=\{z\}` for one vertex `z`.  Deleting

\[
                         \{z\}\cup(S-\{a,b\})             \tag{4.8}
\]

would remove only six vertices.  The nonempty lobes `C_1,C_2` would
then have no route to the opposite open shore: there are no shore-crossing
edges, their boundary neighbours other than `a,b` were deleted, they
miss `a,b`, and `z` was the sole remaining `a`- or `b`-portal anywhere
in `L`.  This contradicts 7-connectivity.

Choose distinct `r\in A` and `s\in B`.  The set form of Menger's theorem
in the 2-connected graph `H+pq` gives two vertex-disjoint paths linking
the set `\{p,q\}` to the set `\{r,s\}`.  Equivalently, after possibly
interchanging `p,q`, there are disjoint paths

\[
                         P_a:p\longrightarrow r,
             \qquad     P_b:q\longrightarrow s.          \tag{4.9}
\]

Trivial paths are allowed when a portal is itself a cut vertex.  The
artificial edge `pq` is not used: a path using it would contain both
members of the source set, leaving no disjoint path from the other
source.

Now put

\[
 X=V(C_1)\cup\{p\}\cup V(P_a),\qquad
 Y=V(C_2)\cup\{q\}\cup V(P_b).                            \tag{4.10}
\]

The two sets are disjoint and connected.  They are adjacent because
`C_1` has a neighbour at `q\in Y`.  The lobe `C_1` contacts every
vertex of `S-\{a,b\}`, while the terminal `r` of `P_a` has a neighbour
at `a`; hence `X` misses at most `b`.  Symmetrically `Y` misses at most
`a`.  Theorem 1 closes the configuration. \(\square\)

### Corollary 4.3 (bounded 2-cut frontier)

Every 2-cut in a surviving thin shore has at most three lobes.  If it
has three lobes, then the three raw defect 2-sets that escape the
grouping certificate are pairwise distinct.

Indeed, Proposition 4.1 reduces every `k\ge4` residue to a defect 2-set
occurring at least `k-1` times, and Proposition 4.2 closes that residue.
For `k=3`, Proposition 4.2 closes every repeated defect pair, including
the exceptional pattern consisting of one small defect and two equal
2-sets.  Thus only the pairwise-distinct defect-two pattern can survive
the raw lobe test (with contacts at `p,q` possibly closing additional
instances).

The next literal construction supersedes this defect-pattern residue
entirely.

### Theorem 4.4 (three lobes give a literal `K_7`)

Let `\{p,q\}` be a 2-cut of the surviving 2-connected thin shore `L`.
If `L-\{p,q\}` has at least three components, then `G` contains a
literal `K_7` model.

#### Proof

Choose three components `C_1,C_2,C_3`.  As in Proposition 4.1, each
`C_i` has neighbours at both `p,q` and contacts at least five vertices
of `S`.  Put `D_i=S-N_S(C_i)`, so `|D_i|\le2`.  Since

\[
                      |D_1\cup D_2\cup D_3|\le6<|S|,
\]

there is a literal vertex

\[
                       t\in S-(D_1\cup D_2\cup D_3)       \tag{4.11}
\]

contacted by all three lobes.

For each `i`, the set `N_S(C_i)-\{t\}` has order at least four.  These
three subsets of the six-element set `S-\{t\}` have a system of distinct
representatives `x_1,x_2,x_3`: Hall's condition is immediate, since a
one-set union has order at least four, a two-set union has order at least
four, and a three-set union has order at least four.  Let

\[
                \{r_1,r_2,r_3\}=S-\{t,x_1,x_2,x_3\}.      \tag{4.12}
\]

Using three disjoint full packets `P_1,P_2,P_3` in `R`, define

\[
\begin{array}{lll}
 A_1=V(C_1)\cup\{p,x_1\},
 &A_2=V(C_2)\cup\{q,x_2\},
 &A_3=V(C_3)\cup\{x_3\},\\[2mm]
 B_i=V(P_i)\cup\{r_i\}\quad(i=1,2,3),
 &&T=\{t\}.
\end{array}                                                \tag{4.13}
\]

These seven sets are pairwise disjoint and connected.  The three
`A_i` are pairwise adjacent: `C_1` has a neighbour at `q\in A_2`, while
`C_3` has neighbours at `p\in A_1` and `q\in A_2`.  Every `A_i` is
adjacent to `T` because `C_i` contacts `t`.  The three `B_i` are pairwise
adjacent because each full packet contacts the other packets' distinct
anchors.  Every `B_i` is adjacent to every `A_j` through `x_j`, and to
`T` through `t`, by `S`-fullness.  Thus (4.13) is a literal `K_7`
model. \(\square\)

### Corollary 4.5 (exact 2-cut frontier)

Every 2-cut of a surviving thin shore has exactly two lobes.  It has at
least two by definition, and Theorem 4.4 excludes three or more.

## 5. Exact remaining sub-gap

The `(1,3)` actual-adhesion cell has not been completely closed.  What
remains after the results above is sharply geometric:

1. `L` is a 2-connected labelled society of order at least three;
2. no division into two adjacent connected shores lets both shores miss
   at most one literal vertex of `S`;
3. every 2-cut has exactly two lobes;
4. for a minimum admissible partition, a matching state would follow
   from two disjoint block-terminal carriers with the explicit singleton
   contacts stated in Lemma 3.1.

This is the correct entry point for a block-terminal Two-Paths/web
dichotomy.  The negative certificate must preserve literal first-hit
portal labels and the contacts to `Q`; an unlabelled rural embedding is
not enough.  The proposition shows why the certificate should have a
canonical width-two frontier: any genuinely branching 2-cut with
incoherent boundary defects has already closed by Theorem 1.
