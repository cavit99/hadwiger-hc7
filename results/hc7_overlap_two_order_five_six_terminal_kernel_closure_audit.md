# Audit: six-terminal kernel closure at overlap two

## Verdict

**GREEN.**  The exact support list, irredundancy relation, common-rooted
`K_4` branch, category symmetries, fixed-reserve quantifiers, kernel
catalogue, quotient-minor test, and branch-set lift in
[`hc7_overlap_two_order_five_six_terminal_kernel_closure.md`](hc7_overlap_two_order_five_six_terminal_kernel_closure.md)
are correct.

The main verifier
[`../active/hc7_overlap_two_order_five_six_terminal_kernel_verify.py`](../active/hc7_overlap_two_order_five_six_terminal_kernel_verify.py)
directly checks the fixed pair `{p,q}` on all `240` literal noncommon
states.  Its proof therefore does not depend on orbit inference.  An
independently written cold enumerator reproduced the complete state set,
all counts, the fixed-pair closure, and the stronger reserved-pair profile.

This closes the stated normalized order-five-arm, overlap-two cell.  It
does not prove the support-six transversal theorem or `HC_7`.

## 1. Exact normalized cell

The labels are

```text
A={0,1,2,3,4,5},       I=A cap X={0,1},
X={0,1,6,7},            p=8, q=9,
T={2,3,4,5,6,7,8,9}.
```

For an avoided support `A` of order six, rigid arms of order five and
overlap two give exactly the two literal supports `X+p,X+q` and the four
forced replacements

```text
(A-{0})+p, (A-{0})+q, (A-{1})+p, (A-{1})+q.
```

After the upstream family is pruned before selection of the critical
kernel, `A` and all four order-six replacements are irredundant.  Each
order-five arm is a literal `K_5`.  Thus the five six-support relations
and two literal cliques used by the finite decoder are precisely the
relations forced by the normalized cell; no support has been added or
silently omitted.

On six vertices a spanning `K_5` model has bag sizes
`(2,1,1,1,1)`.  Irredundancy is exactly the exclusion of a literal
five-clique.  Direct enumeration gives `375` labelled induced
edge/nonedge relations.  The independent replay regenerated these
relations from the definition rather than importing the production list.

The two literal cliques overlap on `X`.  Their edge masks must therefore
be combined by bitwise union, not arithmetic addition.  Both the main
verifier and the cold replay use union.  This guards against the duplicate
bit/carry error that would otherwise corrupt the joined relation.

## 2. Joined relation and common branch

Joining the five exact relations while fixing only the two literal
cliques gives

```text
1,419 joined states,
1,179 common states,
240 noncommon states.
```

The independent replay produced exactly the same set of `1,419` pairs of
forced-edge and forced-nonedge masks.  Every noncommon state has nine
unconstrained original edges.  None is assumed present in the minor
decoder.

A state is common precisely when for some `i in I`, the five-set `A-{i}`
contains four disjoint connected, pairwise adjacent bags contacted by all
three of `i,p,q`.  The cold detector independently enumerated all
partitions of four- and five-vertex supports into four connected bags and
selected exactly the same `1,179` states.

This is exactly the hypothesis of the audited three-rooted small-`K_4`
composition theorem.  The rooted `K_4` is disjoint from `i,p,q` and has
total support at most five.  Deleting its support from a seven-connected
graph leaves a two-connected graph containing those three roots; they
therefore root a triangle model.  The four and three rooted bags form a
literal `K_7` model.  No extra exterior connectivity is being assumed.

## 3. Symmetry and fixed-reserve quantifier

The category-preserving group is

```text
Sym(I) times Sym(A-I) times Sym(X-I) times Sym({p,q}),
```

of order `2!*4!*2!*2!=192`.  It preserves every support relation, both
literal cliques, the common-state predicate, and the unordered pair
`{p,q}`.  Its action reduces the `240` noncommon states to `9` full
orbits; the independent replay checked every orbit as a subset of the
literal noncommon state set and reproduced all orbit weights.

More importantly, the main verifier now separately tests every one of the
`240` states with the same fixed pair `{p,q}`.  The exact logical
quantifier proved is

```text
for every noncommon literal state,
  for every order-six carrier, K7 is obtained; and
  for every order-seven kernel,
    there exists an adjacent owner of its nonterminal giving K7.
```

Thus the reserve is selected before the terminal kernel is exposed, and
the owner is selected only after the actual order-seven kernel is known.
This is the safe order of quantifiers.  The stronger diagnostic over all
unordered reserve pairs reproduces the weighted profile

```text
10:12, 13:48, 14:24, 16:108, 18:24, 19:24.
```

Every one of the nine orbits contains `{p,q}` among its valid pairs.

## 4. Connectivity and the terminal kernel

Put `H=G-I`.  Deleting the two vertices of `I` from a seven-connected
graph leaves a five-connected graph.  Reserving `p,q` gives

```text
J=G-(I union {p,q}),
```

which is three-connected and still contains the six distinct terminals
`{2,3,4,5,6,7}`.  The audited terminal-legal contraction theorem therefore
returns a terminal-irreducible rooted minor of order six or seven.

For order six, deletion to an edge-minimal spanning three-connected graph
gives exactly `142` labelled carriers (`70` with nine edges and `72` with
ten).  For order seven, the unique nonterminal gives exactly `780`
labelled kernels.  The cold replay regenerated the first catalogue from
all `2^15` labelled graphs.  It regenerated the second from the independent
structural description:

* `60` labelled terminal six-cycles with a universal nonterminal; and
* for each terminal six-cycle and each of its three opposite chords, the
  nonterminal sees the other four rim vertices and any subset of the two
  chord ends.

After duplicate removal this gives `60+60*3*4=780` masks, exactly equal to
the direct `2^21` catalogue used by the main verifier.

In an order-seven kernel the only terminal-legal edges are those from the
nonterminal to a terminal.  Uniting the nonterminal preimage bag with any
adjacent terminal bag is a valid minor operation even if it does not
preserve three-connectivity.  It keeps that terminal root, preserves
disjointness from the other five rooted bags, and transfers every contact
of the nonterminal.  Hence the adaptive owner used by the finite decoder
is legitimate.

## 5. Exact quotient test

The quotient has ten objects: the singleton vertices `0,1,p,q` and the
six rooted carrier bags.  Any seven-bag model on at most ten objects has at
least four singleton bags.  The production detector exhausts the four
possible singleton counts `7,6,5,4`, allowing unused objects whenever the
count permits them and checking all internal connectivity and inter-bag
contacts.

The cold replay instead enumerated arbitrary set partitions of every
permitted support into seven connected pairwise adjacent bags.  It agreed
with the specialized detector on all `36,918` fixed-`{p,q}`
orbit/carrier/owner quotient masks.  It found no counterstate.  It also
reproduced the complete closure:

```text
closed states  = 240 of 240,
closed orbits  = 9 of 9,
failure states = 0.
```

The reported hashes are useful deterministic replay checks, but the proof
depends on the exhaustive relation, catalogue, and minor tests above, not
on a hash value.

## 6. Literal branch-set lift

The six carrier bags lie in `J`, so they avoid all four singleton objects
`0,1,p,q`.  Every original quotient edge used by the certificate is a
literal edge between its named terminal vertices.  Every carrier edge is
an actual adjacency between rooted preimage bags.  If a quotient branch
set merges several objects, a spanning tree of quotient adjacencies lifts
to a connected union of their preimages.  Distinct quotient branch sets
remain disjoint, and every quotient contact lifts to an actual edge between
the corresponding unions.

For an order-seven kernel, the preliminary merger of the nonterminal bag
with its selected owner is connected and disjoint from all other objects,
so the same argument applies.  Hence every quotient certificate lifts to
a literal seven-bag `K_7` model in `G`.

## 7. Scope

The theorem may be invoked globally only after the pruned rigid
private-pair reduction has produced an avoided support of order six,
literal arms of order five, overlap exactly two, all four forced
replacements, and their irredundancy.  Under those hypotheses the cell is
closed.  The theorem does not address overlap one, the separated-triple
branch, or the global support-six transversal conjecture.
