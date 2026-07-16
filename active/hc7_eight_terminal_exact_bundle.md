# Exact eight-terminal kernel bundle: catalogue draft

## Status

**Order eight and order nine:** deterministic census complete; structural use
still depends on the terminal-kernel theorem and on an independent audit of
the generator.

**Order ten:** analytic classification proved below, using the already
audited terminal-kernel theorem and Wu's theorem used there.

This note is a composition interface, not an `HC_7` result.  It preserves the
contacts discarded by the coarse `C8`, `K3,5`, `F8` carrier trichotomy.

## 1. Encoding

Fix terminal labels `T={0,...,7}` and order the 28 pairs of labels
lexicographically.  A terminal graph is represented by its 28-bit edge mask.

For an order-nine kernel `K` with unique nonterminal `x`, its exact template
is

```text
( E(K[T]) << 8 ) | N_K(x).                              (1.1)
```

For each actual neighbour `w` of `x`, let `Q(K,w)` be the terminal graph
obtained by absorbing `x` into the bag rooted at `w`.  Thus `Q(K,w)` has all
edges of `K[T]` and all edges from `w` to `N_K(x)-{w}`.  The exact owner
family of `K` is

```text
F(K)={Q(K,w):w in N_K(x)}.                              (1.2)
```

The analogous order-ten family absorbs the two nonterminals into a chosen
pair of their actual terminal neighbours.

## 2. Exact census

### Order eight

There are 18 unlabelled edge-minimal three-connected graphs on eight
vertices.  Their edge profile is

```text
edges                 12     13      14     15
unlabelled graphs       4     11       2      1
```

Their complete labelled union has 196,976 masks, with profile

```text
edges                 12       13      14     15
labelled masks     16,800  173,880   6,240     56.
```

For the sorted masks encoded as four-byte big-endian integers, the SHA-256
digest is

```text
2191c87cc229cbf109b19bf66badb40c115838c5b1350709c64fd9a2ec2f020d.
```

### Order nine

The exhaustive `geng` scan finds 97 unlabelled rooted occurrences `(K,x)`
in which `K` is three-connected and no edge incident with `x` is
contractible.  After all terminal labellings and exact-template
deduplication, there are

```text
2,408,280 exact labelled templates.                     (2.1)
```

Their exact edge and root-degree profiles are

```text
|E(K)|       14       15       16       17       18      19     20
count     35,280  305,760  753,480  806,400  411,600  90,720  5,040

d_K(x)        4        5        6        7        8
count    151,200  584,640  883,680  618,240  170,520.
```

The template digest, using (1.1) as sorted eight-byte big-endian integers,
is

```text
7fadafedb382d766267504eee62f441f60aef0cc756aea0c453f62a4ce516dd4.
```

The map from an exact template to its set (1.2) is injective in this census:
there are again 2,408,280 distinct owner families.  The family-size profile
is the displayed root-degree profile.  Encode a family by one byte for its
size followed by its sorted four-byte quotient masks, and sort families
lexicographically.  The digest is

```text
5251ac96f42ec8d18d8d4db24f291f91183d031a34c31089a0d52657238c892c.
```

### Order ten normal form

The analytic classification in Section 3 says that `K[T]` is an eight-cycle,
the two nonterminals are nonadjacent, and their complementary four-neighbour
sets occur cyclically as `AABBAABB`.  There are 10,080 exact labelled
templates when the two nonterminals are temporarily ordered.  Their
template digest is

```text
78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418.
```

Swapping the two nonterminals produces the same owner family.  Hence the
10,080 templates give 5,040 distinct owner families, each of size 16.  Their
digest is

```text
9b0f7300357d8b8443e9ddacf5b15118859642f5c77bbfe559cab120fc182ac8.
```

## 3. Exact order-ten classification

We use the following elementary criterion.

### Lemma 3.1 (contraction criterion)

Let `uv` be an edge of a simple three-connected graph `J` of order at least
five.  Then `uv` is contractible if and only if `J-{u,v}` is two-connected.

### Proof

Put `z=uv` in `J/uv`.  If `J/uv` is three-connected, deleting `z` leaves the
two-connected graph `J-{u,v}`.  Conversely, suppose `J-{u,v}` is
two-connected.  A separator of order at most two in `J/uv` not containing
`z` would lift to a separator of the same order in `J`.  A separator
containing `z`, say `{z}` or `{z,w}`, would say respectively that
`J-{u,v}` or `J-{u,v,w}` is disconnected, contrary to two-connectivity.
Thus `J/uv` is three-connected.  \(\square\)

### Lemma 3.2 (path-apex criterion)

Let `P=p_1...p_m` be a path, and join a new vertex `z` to a nonempty set
`W subseteq V(P)`.  The resulting graph is two-connected if and only if
both ends `p_1,p_m` lie in `W`.

### Proof

If both ends lie in `W`, deletion of `z` leaves `P`; deletion of any vertex
of `P` leaves every remaining path interval joined through `z` using the two
end attachments.  Conversely, if (say) `p_1` is not in `W`, the first member
of `W` encountered from `p_1` is a cutvertex.  \(\square\)

### Theorem 3.3 (exact two-nonterminal residue)

Let `T` be eight terminals and let `K` be a `T`-irreducible simple
three-connected graph with

```text
V(K)=T disjoint_union {x,y}.
```

Then, after possibly interchanging `x,y`, all of the following hold.

1. `K[T]` is an eight-cycle.
2. `xy` is absent.
3. The sets `A=N_K(x)` and `B=N_K(y)` are complementary four-subsets of
   `T`; neither nonterminal has another terminal neighbour.
4. Around `K[T]` the membership word is `AABBAABB`, up to cyclic reversal
   and rotation.

Conversely, every graph of this form is simple, three-connected and
`T`-irreducible.

### Proof

The terminal-kernel theorem applies Wu's theorem to `x` and `y`.  It gives
disjoint charge sets `A_x,A_y subseteq T`, each of order at least four.
Since `|T|=8`, both have order four and partition `T`.  Every charged
terminal has degree three: one edge joins it to its charging nonterminal and
its other two (contractible) edges join terminals.  Thus every terminal is
charged exactly once, no terminal sees the other nonterminal, and `K[T]` is
two-regular.  Three-connectivity makes `K-{x,y}=K[T]` connected, so it is an
eight-cycle.  This proves items 1 and 3.

If `xy` were present, then `K-{x,y}=C_8` would be two-connected.  Lemma 3.1
would make the `T`-legal edge `xy` contractible, contrary to
`T`-irreducibility.  This proves item 2.

Colour the terminal cycle by `A=N_K(x)` and `B=N_K(y)`.  Fix `a in A` and
delete `x,a`.  What remains is the path `C_8-a` together with `y`, joined
exactly to its four `B` vertices.  By Lemmas 3.1 and 3.2, `xa` would be
contractible precisely when both cyclic neighbours of `a` belonged to `B`.
It is not contractible, so `a` has an `A` neighbour on the cycle.  The same
argument with `x,y` exchanged says that every `B` vertex has a `B` cyclic
neighbour.

Consequently every monochromatic run in the cyclic binary word has length at
least two.  There are four letters of each kind.  Either there is one run of
each colour, giving `AAAABBBB`, or there are two runs of each colour, all of
length two, giving `AABBAABB`.  The first word is impossible: deleting the
two endvertices of the four-vertex `A` run separates `x` and the two internal
`A` vertices from `y` and the `B` run.  This is a two-cut.  Item 4 follows.

Conversely, take the displayed normal-form graph.  Deleting `x,y` leaves the
cycle.  Deleting one nonterminal and one terminal leaves a terminal path,
with the other nonterminal attached to at least three of its vertices.  If
two terminals are deleted, the cycle leaves at most two path components.
If there are two, they cannot be respectively `A`-only and `B`-only: a
monochromatic component lies inside one two-vertex run, while the other
component still contains a vertex of that same colour.  Hence `x` or `y`
joins the two components.  These cases, together with the easier deletions
of zero or one vertex, show that deletion of any at most two vertices leaves
the graph connected.  The graph is three-connected.

Finally, every `T`-legal edge is of the form `xa` with `a in A` or `yb` with
`b in B`.  In the word `AABBAABB`, each terminal has one cyclic neighbour of
its own colour.  Lemmas 3.1 and 3.2 therefore show that none of these edges
is contractible.  The graph is `T`-irreducible.  \(\square\)

### Corollary 3.4 (owner-pair bundle)

For every exact order-ten kernel and every pair

```text
(w_x,w_y) in N_K(x) cross N_K(y),
```

the eight sets `{x,w_x}`, `{y,w_y}` and the six remaining singleton
terminals are pairwise disjoint connected rooted bags.  Their adjacency
graph is exactly the quotient recorded by the generator.  Thus all 16 owner
pairs are legal.  Interchanging `x,y` leaves the owner-family set unchanged,
which explains the reduction from 10,080 ordered templates to 5,040 owner
families.

## 4. Safe composition rule

Let `Close(F)` mean that adding terminal carrier `F` to the fixed external
support state produces the required literal minor or other certified
closure.  The exact catalogue supports precisely the following rules:

```text
order 8:   for every labelled carrier F, Close(F);

order 9:   for every exact template K,
             there exists w in N_K(x) with Close(Q(K,w));

order 10:  for every exact template K,
             there exist wx in N_K(x), wy in N_K(y)
             with Close(Q(K,wx,wy)).
```

The owner or owner pair is chosen **after** the actual exact kernel is known.
It may depend on that kernel.  Replacing a family by a single arbitrarily
chosen quotient, or exchanging these quantifiers, is invalid.  Deduplicating
two templates only when they have literally identical owner-family sets is
safe for this formula.

## 5. Inputs and reproduction boundary

The only non-elementary structural input to Theorem 3.3 is Wu's
contractible-edge theorem through the audited terminal-kernel theorem in
[`../results/hc7_five_terminal_rooted_fan.md`](../results/hc7_five_terminal_rooted_fan.md).
In particular, Wu supplies the disjoint four-vertex charge sets and the
degree-three conclusion.  Lemmas 3.1 and 3.2 and the charge-word argument are
proved here.  The published source is H. Wu, *Contractible Elements in Graphs
and Matroids*, Combinatorics, Probability and Computing **12** (2003),
457--465, [doi:10.1017/S0963548302005497](https://doi.org/10.1017/S0963548302005497).

The finite counts use nauty's `geng`; no output of `geng` is used in the
analytic order-ten proof.  The software reference is B. D. McKay and
A. Piperno, *Practical graph isomorphism, II*, Journal of Symbolic
Computation **60** (2014), 94--112,
[doi:10.1016/j.jsc.2013.09.003](https://doi.org/10.1016/j.jsc.2013.09.003).

The self-contained generator is
[`hc7_eight_terminal_exact_bundle_catalogue.py`](hc7_eight_terminal_exact_bundle_catalogue.py).
It uses only Python's standard library and nauty's `geng`.  It independently
checks three-connectivity and contractibility.  The computation is not a
substitute for:

1. the terminal-legal reduction to kernels of order at most ten;
2. independent verification of the finite order-eight/order-nine census; or
3. literal branch-set auditing in any downstream `HC_7` composition.
