# A six-terminal carrier from five designated roots

## Status

Proved, conditional only on the independently audited four-connected
clique-or-fan theorem.  This is a general rooted-minor theorem; the words
"good" and "bad" refer only to a later composition application.

## Theorem 1.1 (five-root clique or six-root fan)

Let `H` be a simple four-connected graph.  Let `W` be a set of five
vertices and let `b` be a sixth vertex outside `W`.  Then at least one of
the following holds.

1. Four members of `W` root a `K_4` minor in `H`.
2. The six vertices `W union {b}` root

   ```text
   F_6 = K_1 join P_5.
   ```

In outcome 1 the four rooted bags are not asserted to avoid the fifth
member of `W` or `b`.  An application which uses them must not use either
omitted terminal as a separate branch set.

### Proof

Apply the audited four-connected terminal clique-or-fan theorem to `W`,
with any three members as its anchor triple.  Its first outcome is exactly
outcome 1 above.  We may therefore assume its second outcome.  Thus `H` is
planar, all five members of `W` lie on one facial cycle `C`, and

```text
R = H-V(C)
```

is connected and meets every vertex of `C`.  The latter facts are the
peripheral-cycle and minimum-degree conclusions proved in the source
theorem.

Suppose first that `b` lies on `C`.  Cut `C` immediately before its six
members of `W union {b}` in cyclic order.  This gives six disjoint
terminal-rooted path bags arranged in a cycle.  Add all of `R` to the bag
rooted at any prescribed terminal.  That enlarged bag is connected and
adjacent to every other bag, while the other five bags form a path.  The
bags therefore form a rooted `K_1 join P_5` model.

Suppose instead that `b` does not lie on `C`.  Then `b in R`.  Cut `C`
immediately before its five members of `W`.  The five resulting rooted
path bags form a cycle.  Use all of `R` as a sixth bag, rooted at `b`.
This bag is connected and adjacent to every path bag because `R` meets
every vertex of `C`.  The six bags form `K_1 join C_5`, which contains
`K_1 join P_5` after one outer-cycle edge is ignored.  This is outcome 2.
\(\square\)

## Corollary 1.2 (labelled composition template)

Let `I` be a three-clique disjoint from `W union {b}` in a supergraph of
`H`, and suppose every vertex of `W` is adjacent to every vertex of `I`.
Then outcome 1 of Theorem 1.1 gives a literal `K_7` model: use the four
rooted exterior bags and the three singleton bags in `I`.  The omitted
members of `W union {b}` are not used separately, so absorption of either
by a rooted exterior bag causes no conflict.

Consequently, in any application with a decoder that turns every labelled
`(W union {b})`-rooted `F_6` into `K_7`, Theorem 1.1 closes the whole
six-terminal interface.

### Proof

Every exterior bag in outcome 1 contains a member of `W`, hence is
adjacent to each singleton in `I`.  The four exterior bags are pairwise
adjacent, and the three vertices of `I` are pairwise adjacent.  These are
seven disjoint pairwise adjacent connected bags.  The last sentence is
then immediate from the two outcomes of Theorem 1.1.  \(\square\)

## Trust boundary

The theorem produces no prescribed bijection between the six terminals
and the hub/path positions of `F_6`.  A finite labelled decoder must cover
all `6*5!/2=360` choices.  It must also keep virtual bag adjacencies
separate from the original edge constraints.
