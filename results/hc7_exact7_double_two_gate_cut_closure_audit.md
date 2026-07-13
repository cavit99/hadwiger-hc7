# Independent audit: exact-seven double-two-gate cut closure

## Verdict

**GREEN** for Theorem 2.1 and Corollary 3.1.  Every separator is genuine,
the three selected gates are distinct, the proposed carriers are disjoint,
connected, pairwise adjacent and spanning, each carrier has literal boundary
support at least four, and the promoted boundary rooted-model trichotomy
applies exactly.  The corollary is genuinely rank-free.

There is one correction to the final scope sentence.  If exactly one deletion
side has all three gate contacts and the other has two, the lower-bound cell
is `3/4/4`.  If **both** sides meet all three gates, the direct separator
bounds are `3/3/4`.  Corollary 3.1 permits this latter case, and the present
theorem does not close it without an additional mechanism.  Thus the exact
remaining rank-free interface is `3/4/4` **or** `3/3/4`, unless a separately
audited result excludes the double-full support pattern.  This does not
affect the theorem or corollary.

The phrase “audited exact-seven `(1,3)` three-gate cell” also carries the
standard promoted dependencies: `G` is seven-connected and strongly
seven-contraction-critical, `G[L]` is three-connected, both open shores are
nonempty, there are no `LR` edges, and the right shore has three disjoint
connected `S`-full packets.  These are needed for the separator and
six-colouring conclusions.

## 1. Gate-side separator bounds

Let `A` be one of the two components of `J-z`.  All exits from `A` in the
whole graph lie in

\[
                       \{z\}\cup U_A\cup N_S(A).
\]

Indeed:

* another vertex of `J` outside `A` can be reached only through the
  cutvertex `z`;
* there are no edges from `A` to the other `T`-lobe `K` except through the
  gate set `T`, and precisely the gates in `U_A` have an `A` neighbour;
* all exits through the literal boundary are in `N_S(A)`; and
* there are no edges between the two open shores.

After deleting this set, `A` remains nonempty, while the opposite lobe and
the nonempty opposite open shore also retain vertices.  It is therefore a
genuine vertex separator.  Its three displayed parts are disjoint, so
seven-connectivity and `|U_A|=2` give

\[
                 1+2+|N_S(A)|\ge7,
                 \qquad |N_S(A)|\ge4.
\]

The same argument applies to `D`.

For the opposite lobe `K`, every exit lies in

\[
                           T\cup N_S(K).
\]

Deleting this set leaves `K`, the nonempty other lobe, and vertices of the
opposite open shore in different surviving parts.  Hence it too is a genuine
separator, and

\[
                         3+|N_S(K)|\ge7,
                         \qquad |N_S(K)|\ge4.
\]

No boundary-contact count is inferred from a palette name or a model bag;
all three are literal neighbourhood counts.

## 2. Selection of the three gate vertices

The supports `U_A,U_D` are two-subsets of the three-set `T`.  They have a
system of distinct representatives.

* If they are equal, assign their two different members one to each side.
* If they differ, each has one member outside the other; assign those two
  exclusive members.

Thus one can choose distinct

\[
                       g_A\in U_A,
                       \qquad g_D\in U_D.
\]

There is then a unique remaining gate `g_0 in T-\{g_A,g_D\}`.  The choice
does not require the two supports to be differently labelled and covers all
nine ordered pairs of two-subsets.

## 3. Carrier connectivity, disjointness and spanning

The proposed carriers are

\[
 C_A=A\cup\{z,g_A\},\qquad
 C_D=D\cup\{g_D\},\qquad
 C_K=K\cup\{g_0\}.
\]

They are pairwise disjoint:

* `A,D` are distinct components of `J-z`;
* `z` belongs to neither component;
* `K` is the other component of `G[L]-T`; and
* `g_A,g_D,g_0` are the three distinct literal vertices of `T`.

Each carrier is connected.

* Since `J` is connected, `z` has a neighbour in every component of
  `J-z`, in particular in `A`.  Since `g_A in U_A`, it also has a neighbour
  in `A`.  Hence `A\cup\{z,g_A\}` is connected.
* `D\cup\{g_D\}` is connected because `g_D in U_D`.
* `K\cup\{g_0\}` is connected because three-connectivity of `G[L]` forces
  every `T`-lobe to meet every gate; otherwise the other two gates would
  separate that lobe.

They span `L`, since

\[
 L=A\mathbin{\dot\cup}D\mathbin{\dot\cup}\{z\}
   \mathbin{\dot\cup}K\mathbin{\dot\cup}T
\]

and the three selected gates partition `T`.

## 4. All carrier adjacencies

The three carrier pairs have literal witnesses.

| Pair | Literal witness |
|---|---|
| `C_AC_D` | an edge from `z` to `D` |
| `C_AC_K` | an edge from `g_A` to `K` |
| `C_DC_K` | an edge from `g_D` to `K` |

The first exists because `D` is a component of the connected graph `J-z`.
The latter two exist because `K` meets every literal gate.  Therefore the
three carriers form a spanning clique partition, not merely three connected
sets.

## 5. Boundary-trichotomy hypotheses

The carrier contact set of `C_A` contains `N_S(A)`, that of `C_D` contains
`N_S(D)`, and that of `C_K` contains `N_S(K)`.  Sections 1--2 therefore give
support at least four for each of the three carrier colours.

Every literal boundary vertex has a nonempty carrier-contact list.  In the
audited exact `(1,3)` setting the connected thin shore `L` is `S`-full; this
also follows directly from seven-connectivity at the literal seven-boundary.
The boundary graph `G[S]` is triangle-free by the exact packet theorem.

Thus all hypotheses of the promoted exact-seven boundary rooted-model
trichotomy hold for `(C_A,C_D,C_K)`.  Its outcomes lift as follows.

1. A proper boundary list-colouring synchronizes the exact equality blocks
   across the two proper minors and yields a six-colouring.
2. An anchored auxiliary `K_4` lifts to four literal clique carriers; the
   three opposite full packets give the remaining branch sets and all
   `6+12+3=21` adjacencies of a literal `K_7`.
3. The adjacent two-vertex cover gives the independent five-block and two
   singleton clique vertices.  One full packet on each shore contracts this
   exact boundary partition on both sides, after which a palette permutation
   aligns and glues the two six-colourings.

This proves Theorem 2.1.  No outcome of the trichotomy is left unresolved.

## 6. Rank-free corollary

If `z` is a cutvertex of a surviving lobe, `J-z` has at least two components
by definition.  The promoted nested-cutvertex exchange excludes three or
more, so it has exactly two components `A,D`.

Three-connectivity of `G[L]` gives

\[
                         |U_A|,|U_D|\ge2:
\]

if one side met at most one gate, `z` together with that gate would be a
separator of order at most two from the nonempty opposite lobe.  If neither
side met all three gates, both supports would have order exactly two and
Theorem 2.1 would give a `K_7` or a six-colouring, impossible in a
hypothetical counterexample.  Hence at least one side meets all three gates.

This argument uses no rooted triangle, no portal matching, and no assumption
on portal rank.  Corollary 3.1 is therefore genuinely rank-free.

## 7. Exact trust boundary

Along a block-chain, the left raw gate supports are nested increasingly and
the right supports decreasingly.  Corollary 3.1 says only that at every cut
at least one of the two supports is all of `T`.  It does not by itself select
one globally consistent full side, increase that side's boundary contact
bound from three to four, or manufacture a new carrier split.

For a side with three gate contacts, the separator estimate is

\[
                 1+3+|N_S(A)|\ge7,
                 \qquad |N_S(A)|\ge3.
\]

Thus the direct unresolved capacity patterns are

* `3/4/4` when the two deletion sides have gate-support orders three and
  two; and
* `3/3/4` when both have order three,

where the final `4` is the opposite lobe `K`.  The promoted boundary
trichotomy requires all three supports to have order at least four and
therefore cannot be invoked directly in either pattern.
