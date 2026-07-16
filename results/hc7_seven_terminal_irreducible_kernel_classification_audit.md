# Audit of the exact seven-terminal irreducible kernels

## Verdict

**GREEN.**  The hand classification in
[`hc7_seven_terminal_irreducible_kernel_classification.md`](hc7_seven_terminal_irreducible_kernel_classification.md)
is correct.  In particular:

* Lemma 1.1 is an equivalence, not merely a sufficient condition;
* the Hamilton-remainder input used in the proof is valid;
* the three displayed order-eight families are necessary and sufficient;
* all neighbours of the extra vertex are legal owners;
* the order-seven universal branch really is the set of `5,495` labelled
  inclusion-minimal spanning three-connected carriers; and
* the final catalogue has the asserted universal/existential quantifier
  order.

The independent enumerations described below found no missing rooted type
and no counterexample to any converse.

## 1. Contraction criterion

Let `z` denote the image of `xv` in the simplified contraction `M/xv`.
If the quotient is three-connected, deleting `z` leaves

```text
M-{x,v}=H-v,
```

which is two-connected.  This proves necessity.

Conversely, assume `H-v` is two-connected.  A deletion of at most two
quotient vertices which avoids `z` lifts to the same deletion in the
three-connected graph `M`; contracting `xv` preserves connectedness.  A
deletion which contains `z` leaves either `H-v` or `(H-v)-w`, both connected.
Moreover `H-v` has at least three vertices, so the quotient has at least four
vertices.  Thus the quotient is three-connected.  Parallel-edge
simplification does not affect this connectivity argument.  Lemma 1.1 is
therefore correct in both directions.

## 2. Hamilton-remainder dependency

The proof uses Lemma 2.2 of
[`hc7_seven_terminal_rooted_cycle_or_biclique.md`](hc7_seven_terminal_rooted_cycle_or_biclique.md):
if an eight-vertex simple three-connected graph has a vertex `x` incident
with no contractible edge, then deleting `x` leaves a Hamiltonian graph.
This dependency was checked directly rather than assumed from that file's
status.

Wu supplies at least four degree-three neighbours of `x`; these become
degree-two vertices in the two-connected graph `H=M-x`.  Hence at most three
vertices of `H` have degree at least three.  Suppressing the degree-two
paths gives:

* with two high-degree vertices, a bundle of at least three parallel routes;
  non-Hamiltonicity forces at least three long routes, one of which has one
  internal vertex because their positive weights sum to five;
* with three high-degree vertices, the underlying suppressed graph is a
  triangle; non-Hamiltonicity forces two parallel long routes, and one has
  one internal vertex because the total long-edge weight is four.

In either case, deleting the unique internal vertex of the short route
leaves a two-connected graph.  Three-connectivity forces that vertex to be
adjacent to `x`, and Lemma 1.1 then makes the corresponding edge
contractible, a contradiction.  This establishes exactly the Hamiltonian
remainder needed by Theorem 2.1.

## 3. Necessity of the three order-eight families

Write `C` for a Hamilton cycle of `H=M-x` and

```text
A={a in T : xa is an edge and d_M(a)=3},
B=T-A.
```

Wu gives `|A|>=4`.  Every `a in A` has degree two in `H`, so no chord of `C`
is incident with `A`.  Every `b in B` must be incident with a chord: if its
degree in `H` were two, minimum degree in `M` would force `xb`, putting `b`
back in `A`.  Therefore the chord graph `R` on `B` has minimum degree one and
`|B|<=3`.

The resulting cases are exhaustive.

* If `B` is empty, `H=C` and minimum degree forces `x` to see all seven
  terminals: the wheel type.
* `|B|=1` is impossible because `R` has minimum degree one.
* If `|B|=2`, `R` is its unique edge.  A distance-two chord, together with
  the complementary rim arc after deleting the intervening member of `A`,
  leaves a six-cycle.  Lemma 1.1 would then contract the edge from `x` to
  that intervening vertex.  Thus the chord has cyclic distance three, giving
  the one-chord family and precisely the two optional contacts at its ends.
* If `|B|=3`, `R` is a path or triangle.  In the triangle case, the three
  vertices of `B` are pairwise nonconsecutive on `C`.  Their three cyclic
  gaps contain the four vertices of `A`, so one gap has one internal vertex;
  deleting it and using the chord across that gap again leaves a spanning
  cycle and contradicts Lemma 1.1.  Hence `R` is a path.

For the path case, let `b` be its centre.  Either chord from `b` to a leaf
cannot have cyclic distance two.  If its intervening vertex lies in `A`, the
same contraction argument applies.  If the intervening vertex is the other
leaf, that leaf is already a rim neighbour of `b`, whereas its required
edge to `b` in `R` must be a chord.  Thus both leaves are at cyclic distance
three from `b`.  On a seven-cycle those two positions are adjacent, yielding
exactly

```text
C+t_0t_4+t_1t_4
```

and the four mandatory contacts from `x`.  Contacts to the three chord
vertices are genuinely independent optional edges.  No case is omitted.

## 4. Sufficiency and irreducibility

It is enough to check the templates with all optional edges omitted, because
adding edges preserves three-connectivity.  Direct deletion checks confirm
three-connectivity of the three minimal templates:

* the wheel is standard;
* in the one-chord template, a rim component lacking a mandatory neighbour
  of `x` can contain only a chord end and is joined through the chord;
* in the two-chord template, the only rim intervals lacking a mandatory
  neighbour of `x` lie in `{t_0,t_1}` or `{t_4}`, and the two chords join
  them.  Isolating such an interval would require more than the allowed two
  deletions.

Only edges incident with `x` are `T`-legal.  Lemma 1.1 reduces their
noncontractibility to showing that `H-v` is not two-connected.  In the wheel
it is a path.  In the one-chord family, deleting a chord end removes the
chord, while deleting another vertex leaves a path with a degree-one end.
In the two-chord family:

* deleting `t_4` leaves a path;
* deleting `t_0` or `t_1` leaves a path with one chord and a degree-one end;
* deleting any of `t_2,t_3,t_5,t_6` likewise leaves a degree-one end.

This check is independent of the optional contacts from `x`, because
Lemma 1.1 examines the fixed terminal graph `H`.  Every displayed graph is
therefore simple, three-connected, and `T`-irreducible.

The rooted isomorphism count is also correct.  The wheel gives one type.  In
the one-chord family the two chord ends are interchangeable, giving three
orbits according to `|U|`.  In the two-chord family the two leaves are
interchangeable while the chord centre is fixed, giving

```text
2 choices for the centre contact times 3 choices for the number of leaf contacts = 6
```

types.  The total is `1+3+6=10`.

## 5. Owner absorption and catalogue quantifiers

For any exact template `K`, any `w in W=N_K(x)` may absorb `x`: the bag
`{w,x}` is connected, remains disjoint from all other singleton terminal
bags, retains every edge of `H=K[T]`, and gains the edges

```text
wv for every v in W-{w}.
```

Its adjacency graph therefore contains exactly the claimed graph `Q(K,w)`.
There is no requirement that `w` belong to Wu's charged set; adjacency `wx`
is the only condition needed for legal absorption.  Thus the theorem really
supplies every owner in `W`.

On seven vertices, repeatedly delete an edge while three-connectivity is
preserved.  The process stops at an inclusion-minimal spanning
three-connected subgraph, so every order-seven kernel contains a member of
`E_7`.  Consequently a complete composition test must be universal over
`F in E_7`.  In the order-eight branch the actual template is unknown, so
the test is universal over templates, but for each fixed template the proof
may choose any legal owner.  The required condition is therefore

```text
for every K, there exists w in N_K(x) that closes Q(K,w),
```

exactly as stated.  It does not assert one owner that works simultaneously
for all templates.

## 6. Independent finite checks

Two independent `geng`/NetworkX checks were run without using the project's
classification routine as a source of candidates.

First, all simple three-connected graphs on seven vertices were tested for
edge-minimality while preserving the full vertex set.  The five unlabelled
types have automorphism-group orders

```text
144, 4, 12, 4, 2.
```

Hence the number of distinct labelled graphs is

```text
7!/144 + 7!/4 + 7!/12 + 7!/4 + 7!/2
= 35 + 1260 + 420 + 1260 + 2520
= 5495.
```

Second, all simple three-connected graphs on eight vertices were enumerated,
and each possible distinguished extra vertex was tested by directly
contracting every incident edge.  Exactly ten root-preserving isomorphism
classes were terminal-irreducible.  Each matched exactly one of the three
families in Theorem 2.1; there were no exceptions.

A separate labelled-mask generation gives `30,600` exact templates.  This
also follows from the classification: there are `360` labelled seven-cycles,
and for each cycle there are

```text
1 wheel presentation
+ 7*4 one-chord presentations
+ 7*8 two-chord presentations
= 85
```

distinct exact templates.  Thus `360*85=30,600`.  Canonical masks confirm
that no two of these presentations coincide.

## 7. Scope

The result is a complete bounded rooted-carrier catalogue.  It does not by
itself show that any particular `HC_7` composition closes: that still
requires checking every order-seven carrier and, for every order-eight
template, finding a closing legal owner.  The theorem and its audit make no
claim beyond that quantifier-exact decoder rule.
