# A rooted reduction for the split-planar residue

**Status:** written proof; internal audit pending.  This note gives an
unbounded structural reduction for the five-chromatic contracted-boundary
case.  It does not prove `HC_7`.

## 1. Setting

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  Retain
the notation of the audited
[five-chromatic contracted-boundary theorem](../results/hc7_contracted_five_chromatic_boundary.md).
Thus `pv` is an edge, `H=G/pv`, the contraction image `x` lies on the
five-cycle `C` of

\[
                         H[S]\cong K_2\vee C_5,
\]

and `U={a,b}` is the universal pair of this boundary.  Put

\[
                    J=G-U,\qquad P=H-U=J/pv,
\]

and

\[
                    T=\{p,v\}\cup(V(C)-\{x\}).          \tag{1.1}
\]

The earlier theorem gives the following facts.

1. `J` is five-connected and `P` is four-connected and planar.
2. `J` is nonplanar and is obtained from `P` by splitting `x` into the
   adjacent vertices `p,v`.
3. Both `a` and `b` are adjacent to every vertex of `T`.
4. Every `K_5`-minor model in `J` contains `p` and `v` in two distinct
   branch sets.

The fourth assertion is much stronger than merely saying that the pair
`{p,v}` meets every `K_5` model: each of the two vertices separately meets
every such model.

## 2. The split theorem

Let `Q=\overline{P_7}`.  Label its vertices `0,1,...,6` in the order of the
complemented path, so

\[
               ij\in E(Q)\quad\Longleftrightarrow\quad |i-j|\ge2.  \tag{2.1}
\]

We use Theorem 2.5 of Guoli Ding, Chanun Lewchalermvongs and John Maharry,
*Graphs with no* `\overline{P_7}`-*minor*, Electronic Journal of
Combinatorics 23(2) (2016), #P2.16,
<https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i2p16/pdf/>:

> If a nonplanar graph is obtained from a four-connected planar graph by
> splitting one vertex, then it contains `\overline{P_7}` as a minor.

Their vertex split replaces one vertex by adjacent vertices whose old
neighbour sets have order at least four.  This hypothesis is automatic
here: five-connectivity of `J` gives degree at least five at each of `p,v`,
so each has at least four neighbours other than the other split vertex.

### Lemma 2.1 (spanning `Q` model)

The graph `J` has a spanning `Q`-minor model

\[
                         \mathcal B=(B_0,\ldots,B_6).    \tag{2.2}
\]

#### Proof

The split theorem gives a `Q` model.  Since `J` is connected, every
component outside the union of its branch sets has a neighbour in that
union.  Add each such component to one adjacent branch set, one component
at a time.  Connectivity and all old branch-set adjacencies are preserved,
and eventually the model is spanning. \(\square\)

The split theorem itself does **not** say which branch sets contain `p`
and `v`.  The next lemma records the restriction forced by item 4 of
Section 1.

## 3. The two split vertices have restricted positions

### Lemma 3.1 (necessary positions)

Let `p` belong to `B_i` and `v` belong to `B_j`, interchanging `p,v` if
necessary.  Then `i\ne j`, and

\[
\begin{split}
 \{i,j\}\in\mathcal A:=\{&01,02,05,06,12,16,24,45,46,56\}. \tag{3.1}
\end{split}
\]

Here, for example, `24` denotes the pair `{2,4}`.  The list is invariant
under reversing the path labels `k\mapsto 6-k`.

#### Proof

Any `K_5` model in the quotient `Q` lifts, by taking unions of the
corresponding `B_k`, to a `K_5` model in `J`.  Every lifted model must
contain `p,v` in distinct branch sets.

The following five displayed partitions are `K_5`-minor models in `Q`:

\[
\begin{array}{c|ccccc}
 M_0&0&15&2&4&6\\
 M_1&04&1&25&3&6\\
 M_2&0&14&25&3&6\\
 M_3&03&1&25&4&6\\
 M_4&04&1&26&3&5.
\end{array}                                               \tag{3.2}
\]

A string such as `15` means the connected two-vertex branch set
`{1,5}`.  Directly from (2.1), every row consists of five connected,
pairwise adjacent sets.

The model `M_0` omits vertex `3` and combines `1,5`.  Therefore neither
split vertex lies in `B_3`, and they cannot lie one in `B_1` and the other
in `B_5`.  The remaining four rows respectively exclude the pairs

\[
                 04,\qquad14,\qquad25,\qquad26          \tag{3.3}
\]

from being the positions of `p,v`.  Removing these pairs and every pair
incident with `3` from the twenty-one pairs gives exactly the ten pairs in
(3.1).  The same argument excludes `i=j`, because any quotient model using
that vertex would put `p,v` in one lifted branch set. \(\square\)

The pair `24` is the position occupied by the split vertices in the
minimal graph `Q` itself: contracting the edge `24` in `Q` gives the
octahedron.  Lemma 3.1 shows that the published unrooted theorem permits
nine additional positions after lifting to a general host; one cannot
silently assume the minimal `24` placement.

## 4. Six common roots force a `K_7` model

For a spanning model (2.2), define its common-root contact set

\[
                   I(\mathcal B)=\{i:B_i\cap T\ne\varnothing\}.       \tag{4.1}
\]

### Lemma 4.1 (six contacted `Q` bags)

If `|I(\mathcal B)|\ge6`, then `G` contains a `K_7` minor.

#### Proof

First consider the finite quotient statement.  If at least six vertices
of `Q` are marked, then `Q` has a `K_5` model in which every branch set
contains a marked vertex.  It is enough to consider exactly one unmarked
vertex `r`.  The following rows give the required model:

\[
\begin{array}{c|ccccc}
 r\in\{0,1,3,5\}&03&15&2&4&6\\
 r=2              &03&1 &25&4&6\\
 r=4              &04&1 &25&3&6\\
 r=6              &04&1 &26&3&5.
\end{array}                                               \tag{4.2}
\]

Again every row is checked immediately from (2.1).  In the row selected
for `r`, each of the five sets contains a vertex different from `r`.

Apply (4.2) to the marked quotient vertices `I(\mathcal B)` and replace
each quotient vertex `i` by `B_i`.  This gives a `K_5` model
`N_1,...,N_5` in `J`, every branch set of which meets `T`.  Choose
`t_k\in N_k\cap T`.  By Section 1, both `a` and `b` are adjacent to
`t_k`.  Hence

\[
                         \{a\},\ \{b\},\ N_1,\ldots,N_5               \tag{4.3}
\]

are seven disjoint connected pairwise adjacent branch sets in `G`.  They
form a `K_7`-minor model. \(\square\)

### Corollary 4.2 (the exact surviving concentration)

In the `K_7`-minor-free residue, every spanning `Q` model satisfies

\[
                       2\le |I(\mathcal B)|\le5.         \tag{4.4}
\]

Consequently:

1. at least two of the seven `Q` branch sets avoid `T` entirely;
2. at least one `Q` branch set contains two vertices of `T`; and
3. the two branch sets containing `p,v` have distinct indices forming one
   of the ten pairs in (3.1).

#### Proof

The lower bound and item 3 follow from Lemma 3.1.  Lemma 4.1 gives the
upper bound.  Since the six literal vertices of `T` occupy at most five
branch sets, one branch set contains at least two; since there are seven
branch sets, at least two contain none. \(\square\)

## 5. A fixed five-separation and a four-root alternative

There is a second, complementary way to use the split-planar structure.
Put

\[
                    R=T-\{p\}=\{v\}\cup(V(C)-\{x\}).               \tag{5.1}
\]

Thus `R=Y-{a,b}` in the notation of the augmented full-component
reduction.  Define the two closed sides

\[
       K_A=J[A\cup R],\qquad K_D=J[D\cup\{p\}\cup R].              \tag{5.2}
\]

Their vertex sets define a five-separation of `J` with common vertex set
`R`.  When edge-disjoint closed sides are required, assign every edge of
`J[R]` to `K_A` and omit its duplicate copy from `K_D`.  Deleting only
edges internal to `R` does not affect the relative-connectivity argument
below.

### Lemma 5.1 (fixed planar side)

The graph `K_A` has a plane embedding in a closed disc with the five
vertices of `R` on its boundary in cyclic order.  Moreover, both
`K_A` and `K_D` are `(5,R)`-connected: after deleting fewer than five
vertices, every remaining component contains a vertex of `R`.

#### Proof

The contracted shore `H[A\cup V(C)]` has a disc embedding with `C` on
its boundary, by the proof of the audited contracted two-apex theorem.
Map `v` to the contraction image `x`.  Every edge of `K_A` then maps to
an edge of that contracted shore: `A` has no neighbour at `p`, so no
edge incident with `A` is lost under this identification.  Hence `K_A`
is isomorphic to a spanning subgraph of the contracted shore with `x`
renamed `v`.  Restricting the disc embedding proves the first assertion.

Let `Z` have order at most four, and suppose that a component `L` of
`K_A-Z` avoids `R`.  Then `L` lies in `A`.  Since `N_J(A)=R`, it
has no neighbour in `J-(V(K_A)\cup Z)`, so `Z` separates `L` in `J`.
This contradicts five-connectivity of `J`.  The same proof applies to
`K_D`, because `D\cup\{p\}` is connected and its only neighbours outside
it in `J` lie in `R`. \(\square\)

We use two standard results from Jie Ma and Xingxing Yu,
*Independent paths and* `K_5`-*subdivisions*, Journal of Combinatorial
Theory, Series B 100 (2010), 600--616,
<https://yu.math.gatech.edu/Papers/k5-1.pdf/>.  Their Theorem 4.3 gives a
four-arm wheel inside a `(5,R)`-connected plane graph with five boundary
vertices.  Seymour's Two Paths Theorem, quoted there as Theorem 2.2,
gives either two prescribed disjoint paths or a disc embedding with the
four terminals in crossing order.

### Theorem 5.2 (four-root model or one-apex planarity)

Assume `|A|>=2`.  There is a vertex `r in R` for which at least one of
the following holds:

1. `J` has a `K_5`-minor model with four distinct branch sets containing
   the four distinct vertices of `R-{r}`; or
2. `J-r` is planar.

#### Proof

By Lemma 5.1, `K_A` is `(5,R)`-connected, plane with `R` on the boundary,
and has at least seven vertices.  Ma--Yu Theorem 4.3 supplies a vertex
`w in A`, a cycle `W` in `A-w`, and four paths from `w` to four distinct
vertices of `R`.  The paths meet pairwise only at `w`, and each meets
`W` in exactly one vertex.  Let their boundary ends, in cyclic order, be
`r_1,r_2,r_3,r_4`, and let `r` be the fifth member of `R`.

The graph `K_D-r` is `(4,R-{r})`-connected.  Indeed, a separator of
order at most three isolating a component from `R-{r}` would, together
with `r`, give a separator of order at most four in `J`.  Apply Seymour's
Two Paths Theorem to the pairs

\[
                         (r_1,r_3),\qquad(r_2,r_4).                 \tag{5.3}
\]

If the two disjoint paths exist, combine them with `W` and the four arms.
This is the standard Ma--Yu construction of a subdivision of `K_5`.
For the corresponding minor model, absorb the arm ending at `r_i` into
the branch set at its point of intersection with `W`, and split each of
the two paths in (5.3) once between its endpoint branch sets.  Four
distinct branch sets then contain `r_1,r_2,r_3,r_4`, proving outcome 1.

Otherwise, the Two Paths Theorem gives a disc embedding of `K_D-r` in
which `r_1,r_2,r_3,r_4` occur on the boundary in this cyclic order.
The restriction of the embedding in Lemma 5.1 gives the same for
`K_A-r`.  Reflect one disc and identify the four boundary vertices.
The two sides share no other vertex and have no edge between their open
sides, so the result is a plane embedding of `J-r`.  This proves outcome
2. \(\square\)

Theorem 5.2 is deliberately stated for minor branch sets, not for the
branch vertices of the subdivision.  Ma--Yu Theorem 1.2 alone only
asserts an unrooted `TK_5`; its proof first replaces the given separation
by one with a maximal planar side, which can change the five separator
vertices.  The four boundary ends in the construction are degree-two
vertices of the displayed subdivision, rather than its branch vertices.
The theorem therefore does not by itself justify four prescribed branch
vertices in the fixed set `R`.

Outcome 1 leaves exactly one potentially uncontacted `K_5` branch set.
Outcome 2 gives a coherent one-apex structure in `J`.  Neither conclusion
alone produces a `K_7` minor, but both are host-level alternatives rather
than a finite boundary classification.

## 6. A local exchange that is too strong

The collision in Corollary 4.2 cannot in general be repaired by holding
six `Q` branch sets fixed and moving one root into an empty branch set.
The following ten-vertex graph is an explicit obstruction.  Its vertex
set is `0,...,9`, and its edges are

```text
03 04 06 08 09 13 15 16 17 18 24 25 27
28 29 36 38 39 46 47 49 57 58 59 67 89
```

Put `p=8`, `v=9`, and `T={0,2,6,7,8,9}`.  This graph is five-connected;
contracting `89` gives the four-connected planar graph with graph6 string
`HEher^{`.  The components after deleting `T` are `{4}` and `{1,3,5}`,
with neighbourhoods `T-{8}` and `T`, respectively.

It has the spanning `Q` model

\[
 B_0=016,\ B_1=2,\ B_2=5,\ B_3=4,\ B_4=38,\ B_5=7,\ B_6=9.       \tag{6.1}
\]

Exactly five bags meet `T`; the collision is `{0,6} subseteq B_0`, and
`B_2,B_3` avoid `T`.  None of the four moves taking `0` or `6` from
`B_0` to `B_2` or `B_3`, while leaving every other bag fixed, preserves
a `Q` model:

- `0` into `B_2` disconnects the receiver and destroys the required
  `B_0B_6` adjacency;
- `0` into `B_3` destroys that same adjacency;
- `6` into `B_2` disconnects both donor and receiver; and
- `6` into `B_3` disconnects the donor.

This is only a barrier to the fixed-bag move.  Global reselection succeeds:

\[
 C_0=013,\ C_1=2,\ C_2=5,\ C_3=46,\ C_4=8,\ C_5=7,\ C_6=9,       \tag{6.2}
\]

and all six vertices of `T` now occupy distinct contacted bags.  Thus the
example supports the correct exchange formulation: reselect the whole
model, or expose the full separator, rather than prescribe a one-vertex
transfer inside a fixed model.  The deterministic verifier
[`hc7_split_planar_fixed_bag_barrier_verify.py`](hc7_split_planar_fixed_bag_barrier_verify.py)
checks the connectivity, planar contraction, both models, and all four
failed moves.

## 7. Exact remaining exchange problem

The split-planar residue is therefore not an arbitrary unrooted `K_5`
obstruction.  It contains a spanning `\overline{P_7}` model in which:

- the two split vertices occupy one of ten explicit pairs of model bags;
- two model bags have no common-root vertex; and
- some third model bag contains a collision of the six common roots.

Closing this branch amounts to a label-preserving global exchange: reselect
the spanning `Q` model so that one of the colliding vertices of `T` enters
an uncontacted branch set, or use the failure to obtain an order-seven
separation with compatible shore colourings.  One successful exchange that
raises `|I(\mathcal B)|` to six is terminal by Lemma 4.1.  Section 6 shows
why the model must be allowed to change globally.

The fixed-five-separation route gives a second precise target.  In
Theorem 5.2(1), join the unused vertex `r` to the fifth, uncontacted
`K_5` branch set without destroying the four rooted branch sets; failure
should return a compatible exact separation.  In outcome 2, exploit the
planar graph `J-r` together with contraction-critical colourings.  Neither
step follows from connectivity alone.

Neither the Ding--Lewchalermvongs--Maharry theorem nor the ordinary
Kelmans--Seymour `TK_5` theorem supplies this rooted exchange.  In
particular, the fact that `Q/24` is planar does not justify assuming that
an arbitrary `Q` model in `J` places `p,v` in bags `B_2,B_4`; Lemma 3.1 is
the strongest restriction obtained here from quotient `K_5` models.

Thus this note replaces the generic “find a rooted `K_5`” gap by two
specific host-level alternatives--global collision-to-empty-bag exchange,
or four-root completion versus one-apex planarity--but closes neither
alternative and does not prove `HC_7`.
