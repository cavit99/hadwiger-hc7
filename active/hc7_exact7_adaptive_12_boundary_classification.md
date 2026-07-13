# Boundary classification for adaptive exact-seven `(1,2)` reflection

## Status and scope

This is a **boundary-only theorem and falsification package**.  It classifies
the packet demand of every proper equality partition containing a prescribed
exact independent block.  It does not say that an arbitrary enumerated
partition is realizable by a proper-minor colouring of either shore.

Let `H=G[S]`, where `|S|=7`.  In the actual packet vector `(1,2)` there are
three disjoint `S`-full packets in total.  If `H` contains a `K_4`, assigning
the other three literal boundary vertices to the packets gives a literal
`K_7` model.  Thus the only live boundary case has

\[
                              \omega(H)\le 3.             \tag{1.1}
\]

For an independent nonempty set `I`, let `P_I` be the family of partitions
`Pi` of `S` into at most six nonempty independent blocks such that `I` is one
exact block.  Put

\[
 d_H(\Pi)=|\Pi|-\omega\bigl(H[\operatorname{sing}(\Pi)]\bigr).
\]

The two packets on the rich shore reflect every returned state with
`d_H(Pi)<=2`.

## 1. Exact classification for a non-singleton forced block

### Theorem 1.1 (split-remainder criterion)

Let `|I|>=2`, put `R=S-I`, and write `F=H[R]`.  Then:

1. some partition in `P_I` has packet demand at most two if and only if `F`
   is a split graph;
2. the maximum packet demand over `P_I` is

   \[
             \max_{\Pi\in P_I}d_H(\Pi)
                =1+|R|-\omega(F);                         \tag{1.2}
   \]

3. consequently every partition in `P_I` has demand at most two if and only
   if

   \[
                          \omega(F)\ge |R|-1.              \tag{1.3}
   \]

Under (1.1), if `F` is not split, the minimum demand is exactly three.  The
minimal induced demand-three certificates are precisely

\[
                         2K_2,\qquad C_4,\qquad C_5.       \tag{1.4}
\]

#### Proof

Suppose `Pi in P_I` has demand at most two.  Let `C` be a maximum clique
among its singleton blocks.  The block `I` lies outside `C`.  Since at most
two blocks lie outside `C`, all of `R-C` lies in at most one further
independent block.  Hence `F` is the union of the clique `C` and an
independent set.

Conversely, if `R=C dotcup B`, where `C` is a clique and `B` is independent,
use the blocks `I`, `B` when nonempty, and the singleton blocks `{c}` for
`c in C`.  Its demand is at most two.  This proves assertion 1.

For assertion 2, start from any state in `P_I` and refine every non-singleton
block other than `I` into singleton blocks.  Refining an independent block
of order `r>=2` increases the number of blocks by `r-1`, while adding that
independent set to the singleton graph increases its clique number by at
most one.  Demand therefore does not decrease.  The terminal refinement is

\[
                       I\mid\{r_1\}\mid\cdots\mid\{r_{|R|}\},
\]

whose demand is the right-hand side of (1.2).  Assertion 3 follows.

The forbidden induced subgraphs for split graphs are exactly
`2K_2,C_4,C_5`.  Here `|R|<=5`.  If `F` is nonsplit, assertion 1 gives
minimum demand at least three.  It is at most three: a `K_4`-free graph on
at most five vertices is three-colourable, and a three-colouring of five
vertices has a singleton colour class; adjoining the block `I` therefore
has demand at most three.  Thus the minimum is exactly three. `square`

### Corollary 1.2 (the robust choice criterion)

In a `K_4`-free seven-vertex boundary, a non-singleton independent set `I`
forces **every** returned partition to have demand at most two exactly in
one of the following cases:

* `|I|>=5`;
* `|I|=4` and `H[S-I]` contains an edge;
* `|I|=3` and `H[S-I]` contains a triangle.

No independent pair is robust, because its five-vertex remainder would
need a `K_4`.

Consequently, if an actual `(1,2)` exact-seven adhesion has such a boundary
set `I`, contract the thin packet with `I`.  Fullness makes `I` an exact
returned block, every possible returned partition has demand at most two,
and the two rich packets reflect it exactly.  Palette alignment then
six-colours `G`.  Thus this entire boundary family is closed without any
internal shore analysis.

## 2. Singleton forced blocks

For completeness, let `I={i}`.  Some member of `P_I` has demand at most two
if and only if at least one of the following holds:

1. there is a clique `C subseteq S-{i}` such that
   `S-({i} union C)` is independent; or
2. there is a clique `C subseteq N_H(i)` such that
   `H[S-({i} union C)]` is bipartite.

Indeed, take a maximum clique `C` among the singleton blocks of a safe
partition.  If `i notin C`, the singleton `{i}` consumes one of the at most
two blocks outside `C`, so all other vertices outside `C` form one
independent block.  If `i in C`, the remaining vertices occupy at most two
independent blocks.  Both constructions reverse directly.

No singleton is robust under (1.1).  Refine a state to six blocks while
keeping `{i}` exact.  The unique nonsingleton block is then an independent
pair `B subseteq S-{i}`, and the demand is

\[
                         6-\omega(H[S-B])\ge3.            \tag{2.1}
\]

Thus singleton forcing alone can never make the `(1,2)` reflection
automatic.

## 3. Exhaustive census

The deterministic verifier enumerates all 685 unlabeled `K_4`-free graphs
on seven vertices, all 18,264 independent-set/boundary pairs, and all 876
partitions with at most six blocks.  It checks Theorem 1.1, the singleton
criterion, and the following census.

| `alpha(H)` | boundary graphs | admit a robust `I` | residue | residue with some safe `I` | residue with no safe `I` |
|---:|---:|---:|---:|---:|---:|
| 2 | 9 | 0 | 9 | 4 | 5 |
| 3 | 353 | 154 | 199 | 167 | 32 |
| 4 | 265 | 234 | 31 | 31 | 0 |
| 5 | 51 | 51 | 0 | 0 | 0 |
| 6 | 6 | 6 | 0 | 0 | 0 |
| 7 | 1 | 1 | 0 | 0 | 0 |
| **total** | **685** | **446** | **239** | **202** | **37** |

The 239-boundary residue has an exact structural description:

* all nine boundaries with independence number two;
* the 199 independence-number-three boundaries for which the complement of
  every independent triple is triangle-free; and
* the 31 independence-number-four boundaries for which the complement of
  every independent four-set is edgeless.

The last class is equivalently the bipartite order-seven graphs with
`alpha=4` in which every minimum vertex cover is independent.  The first
two descriptions are the safer invariant formulations; no unlabeled case
list is needed.

## 4. The independent two-anchor lift

If distinct `x,y in S` satisfy

\[
                        H-\{x,y\}\succeq K_4,             \tag{4.1}
\]

then the three full packets and this literal boundary model give a `K_7`
minor.  Namely, take the four branch sets of the `K_4` model together with

\[
            V(Q)\cup\{x\},\qquad
            V(P_1)\cup\{y\},\qquad
            V(P_2).
\]

Fullness supplies all packet-to-model and packet-to-packet adjacencies.
This is independent of state reflection.

There is a useful label-free form of (4.1).  Since `H` is `K_4`-free, a
`K_4` model on five boundary vertices must have branch-set orders
`2,1,1,1`.  Hence the two-anchor lift exists if and only if `H` contains a
triangle `T` and a disjoint edge `uv` such that

\[
                         T\subseteq N_H(u)\cup N_H(v).    \tag{4.2}
\]

The edge `uv` is the two-vertex branch bag and `T` supplies the three
singleton bags.  Thus surviving the lift means that every disjoint
triangle-edge pair has a literal missed triangle vertex.  This
triangle-edge coverage condition is the compact structural invariant; it
replaces a search through twenty-one labelled anchor pairs.

Of the 239 graphs surviving robust reflection, 110 have this two-anchor
lift.  The exact residual therefore has 129 unlabelled boundaries:

| `alpha(H)` | some safe state | no safe state | total |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 2 |
| 3 | 87 | 9 | 96 |
| 4 | 31 | 0 | 31 |
| **total** | **119** | **10** | **129** |

This residue has the invariant definition

\[
\begin{split}
 &\text{no independent `I` has }\omega(H-I)\ge |S-I|-1,\\
 &H-\{x,y\}\text{ is `K_4`-minor-free for every pair `x,y`.}
\end{split}                                                   \tag{4.3}
\]

The two independence-number-two orbits are the Moser spindle and its
surviving one-edge extension.  The former has no safe state; the extension
has one but does not force it.  The 31 independence-number-four graphs are
exactly the bipartite residue already described in Section 3; a bipartite
graph on five vertices cannot contain a `K_4` minor, because a five-vertex
`K_4` model would have three literal singleton bags forming a triangle.

### The ten absolute-demand-three orbits

All ten, **including the Moser spindle**, contain two vertex-disjoint
triangles.  They admit the following label-free construction.  Let `A,B`
be disjoint triangles and let `z` be the seventh vertex.  Up to interchanging
`A,B` and permuting vertices inside them, precisely these patterns occur:

1. there is no `A-B` edge and the unordered pair
   \((|N(z)\cap A|,|N(z)\cap B|)\) is one of

   \[
          (0,0),(0,1),(0,2),(1,1),(1,2),(2,2);           \tag{4.4}
   \]

2. there is one `A-B` edge, `z` avoids both endpoints, and its support
   sizes are `(1,2)` or `(2,2)`; the `(2,2)` graph is the Moser spindle;
3. the `A-B` edges form a matching of order two, and `z` sees either
   exactly the two unmatched triangle vertices, or those two vertices plus
   one matched endpoint on one side.

These are ten graph orbits, not ten arbitrary labelled cases.  The
canonical-marking verifier minimizes over the `2(3!)^2` symmetries of the
two triangles and checks exactly these ten signatures.  This classification
corrects a tempting but false distinction: the Moser spindle is not the
exception to the disjoint-triangle pattern.

The minimum-demand witnesses also have a uniform form.  In each of the nine
independence-number-three orbits, take a maximum independent triple `I`.
Its four-vertex complement is nonsplit and hence is `2K_2` or `C_4`; its
two bipartition classes `X,Y` give

\[
                               I\mid X\mid Y,             \tag{4.5}
\]

with demand three and no singleton blocks.  In the standard Moser labeling

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\},
\]

one explicit minimum state is

\[
                 \{1,3\}\mid\{0,6\}\mid\{2,5\}\mid\{4\},
                                                               \tag{4.6}
\]

whose unique singleton clique has order one, again giving demand three.

## 5. Explicit guardrails

### 5.1 No static safe choice: `2K_3 dotcup K_1`

Let the triangles be `012` and `345`, with vertex `6` isolated.  The graph
is `K_4`-free and has independence number three.  For the maximum
independent set

\[
                              I=\{0,3,6\},
\]

the remainder is `2K_2`, and

\[
                       \{0,3,6\}\mid\{1,4\}\mid\{2,5\}
\]

has demand three.  In fact **every** independent `I` has minimum demand at
least three.  This falsifies both “choose a maximum independent set” and
“independence number at least three suffices.”  Among unlabeled boundaries
with no safe choice, this is an edge-minimal representative (six edges).

### 5.2 Safe is not robust: `3K_2 dotcup K_1`

Let the edges be `01,23,45`, with `6` isolated, and take

\[
                              I=\{0,2,4,6\}.
\]

The two-block partition `I | {1,3,5}` has demand two, but the equally legal
returned partition

\[
                          I\mid\{1\}\mid\{3\}\mid\{5\}
\]

has demand three.  Thus `alpha(H)>=4` guarantees a combinatorially safe
partition but does not guarantee a robust forced block.  Existence of a
safe abstract partition cannot be substituted for realizability by a
proper-minor colouring.

### 5.3 Uniform demand three: `complement(C_7)`

Label the underlying cycle cyclically.  Independent blocks in
`H=overline{C_7}` are singletons or cycle edges, so a proper equality
partition is a matching `M` of the cycle plus its unmatched singleton
vertices.  If `m=|M|`, the unmatched cycle graph has independence number
`4-m`.  Therefore

\[
                         d_H(\Pi)=(7-m)-(4-m)=3
\]

for every proper partition containing any prescribed independent block.
This is a compact adversarial boundary on which no adaptive choice of `I`
changes the demand.

## 6. Strategic consequence

The robust criterion closes 446 of the 685 unlabeled `K_4`-free boundary
types in an actual `(1,2)` adhesion, and the two-anchor lift closes 110 more
outside that class.  It cannot close the remaining 129 by these two
mechanisms.  Ten of those do not even admit an abstract safe choice; the
other 119 show that existence of a favourable state is not a state-transfer
theorem.

Accordingly the next theorem must use information absent from `H`:

* which equality states are actually returned by proper-minor colourings;
* a demand-three-to-`K_7` carrier construction; or
* a coherent fixed-pair endgame.

The split obstruction (1.4), the invariant residue (4.3), and the ten
double-triangle orbits are the compact certificates to carry into that
geometry.

## Verification

Run:

```bash
PYTHONPATH=active/runtime/deps python3 \
  active/hc7_exact7_adaptive_12_boundary_verify.py
```
