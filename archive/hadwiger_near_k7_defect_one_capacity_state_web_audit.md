# Independent audit: near-`K_7` defect-one capacity/state web

## Post-audit four-piece correction

The original audit verified the five-piece theorem but did not test the
full four-piece quotients corresponding to the two overlap words.  Both
overlaps already contain `K_7`:

\[
\begin{array}{c|c}
abba&\{a,b,X_1,X_2\}\mid\{c\}\mid\{q_1\}\mid\{q_2\}
      \mid\{q_3\}\mid X_3\mid X_4\\
acca&\{a,c,X_1,X_2\}\mid\{b\}\mid\{q_1\}\mid\{q_2\}
      \mid\{q_3\}\mid X_3\mid X_4.
\end{array}
\]

Each first bag is connected through the consecutive-piece edge and the
two complementary label contacts; all other adjacencies are forced by the
displayed defect word.  Hence four consecutive defect-one pieces, not
five, force `K_7`.  The corrected retained-web bound is

\[
                         1+108+108^2=11,773.
\]

This strengthens rather than invalidates the audited results below.

## 1. Verdict table

| Claim | Verdict |
|---|---|
| Theorem 2.1, three-piece quotient classification | **GREEN, computer-assisted** |
| Corollary 3.1, four-piece words | **GREEN** |
| Theorem 3.2, five-piece chain | **GREEN** |
| Lemma 4.1, 108-state branching | **GREEN under the actual common-two-cut hypotheses** |
| Theorem 4.2, finite web bound | **GREEN conditional on the stated defect-one decomposition** |
| Lemma 5.1, rural expansion | **GREEN conditional on a plane full-piece quotient and compatible rural societies** |
| Corollary 5.2, large-web trichotomy | **GREEN under all preceding decomposition hypotheses** |
| Existence of such a decomposition for an arbitrary `K_7^vee` minor | **UNPROVED / AMBER route** |
| Closure of the near-`K_7` route or `HC_7` | **RED** |

One genuine statement gap was repaired during the audit: the web
decomposition must explicitly cover the whole complex bag.  Without

\[
                         V(B)=\mathop{\dot\bigcup}_tX_t,
\]

the rural disk substitution need not draw leftover vertices or their
edges.  This coverage condition is now item 1 of the definition.

The phrase "independently replays" was also weakened to "replays": the
main verifier reruns the same direct certificate predicate.  As an audit,
I separately ran a different nonspanning connected-subset search; its
result is recorded in Section 2.

## 2. Exact verifier audit

### Profile coverage

For each of the three path vertices there are exactly seven minimal
support types:

* `None`, meaning complete to all six labels; or
* one of the six labels, meaning that this is the unique missed label.

Thus `product(types,repeat=3)` checks all `7^3=343` profiles.  A real piece
which sees at least five labels contracts to one of these profiles after
surplus edges are deleted.

### Partition coverage

The restricted-growth generator starts with vertex 0 in block 0, at each
step uses an existing block or creates the next block, and accepts exactly
seven blocks.  It emits

\[
                            {9\brace7}=462
\]

partitions, with no block-order duplication.

It is legitimate to search only spanning models.  Every quotient is
connected: the six-label graph `K_6-{ab,ac}` is connected, and every path
vertex meets at least five labels.  Given any nonspanning clique model,
each component of the unused graph has an edge to the model union and may
be absorbed into one incident branch bag.  Repeating makes the model
spanning without destroying connectedness or any adjacency.

For every candidate partition, `verify_model()` checks:

1. seven nonempty blocks;
2. total support order nine and pairwise disjointness, hence exact coverage;
3. connectedness of every block by a direct bitset search; and
4. all 21 unordered branch-bag adjacencies.

The normal run reproduces:

```
profiles 343
K7-positive 333
K7-negative 10
negative words [(a,b,b),(a,c,c),(b,b,a),(b,q1,c),(b,q2,c),
                (b,q3,c),(c,c,a),(c,q1,b),(c,q2,b),(c,q3,b)]
length-four words [(a,b,b,a),(a,c,c,a)]
length-five words 0
```

I also reran all 343 profiles with an independent algorithm which:

* enumerates every nonempty connected subset of the nine-vertex quotient;
* recursively selects seven disjoint pairwise adjacent subsets; and
* permits unused vertices rather than relying on spanning normalization.

It again found 333 positives and the identical ten negatives.  Every
positive result was replayed for disjointness, connectedness, and all 21
adjacencies.  This independently confirms the finite classification.

### Use of `assert`

The verifier is intended to be run normally, as in the audit.  Python's
`-O` flag disables assertions and must not be used for a certificate run.
This is an execution qualification, not a mathematical gap.

## 3. Lift from a quotient to arbitrary connected pieces

Let `X_1,X_2,X_3` be the displayed disjoint connected sets.  Contracting
them simultaneously is a legitimate minor operation.  Every forced
quotient edge has a literal lift:

* an `x_i`--label edge is an actual portal edge from `X_i`;
* `x_1x_2` and `x_2x_3` lift through the two assumed interpiece edges;
* label-label edges are the edges of `K_6-{ab,ac}`.

To lift a quotient branch bag, replace each `x_i` it contains by all of
`X_i`.  Connectivity lifts along the same quotient edges.  Distinct bags
remain disjoint because the pieces and labels are pairwise disjoint.
Every quotient bag adjacency has one of the literal edges above.  Thus a
positive quotient certificate is a genuine `K_7`-minor in the original
graph, regardless of the pieces' order, treewidth, or internal structure.

Extra label contacts, nonconsecutive interpiece edges, and unused vertices
are monotone additions.  The classification is only one-way on the ten
negative profiles, exactly as the theorem states.

**Verdict: GREEN.**

## 4. Overlap audit

If a four-piece chain were `K_7`-minor-free, both consecutive length-three
words must be in the verified negative set.  The only matching
suffix/prefix pairs are

\[
                         abba,\qquad acca.
\]

Neither terminal pair `ba` nor `ca` starts a negative triple, so neither
four-letter word extends to a five-letter word.  Applying Theorem 2.1 to
the last triple gives the contradiction.

No induced-path assumption is used: pairwise disjointness and consecutive
adjacency suffice, while additional edges only help a minor.  The source
definition was clarified accordingly.

**Verdict: GREEN.**

## 5. Faithful-state branching audit

At one branching node the child-subtree unions `D_i` must be components or
open lobes behind the **same actual** two-cut `{x,y}`.  They are pairwise
anticomplete and satisfy

\[
                       N_G(D_i)\subseteq
                       W=L\mathbin{\dot\cup}\{x,y\}.
\]

These are essential hypotheses; abstract children of a decomposition tree
would not suffice.

In every six-colouring of `G-D_i`, the five-clique
`{b,c,q_1,q_2,q_3}` gives five distinct boundary blocks.  Since `a` sees
all three `q_i`, its block is that of `b`, that of `c`, or the sixth block.
Each of `x,y` has at most six choices.  Hence there are at most
`3*6^2=108` equality partitions of `W`.

If `G-D_i` and `G-D_j` give the same equality partition, align palettes on
`W`.  Colour `D_i` from the minor retaining `D_i`, colour `D_j` from the
minor retaining `D_j`, and use either colouring on the common remainder.
There is no `D_iD_j` edge and every external lobe edge ends in `W`, so the
splice restores both deleted lobes and six-colours `G`.  Proper-minor
minimality supplies a colouring for every nonempty lobe deletion.

Thus 109 children force a common faithful state and a contradiction.

**Verdict: GREEN under the common-boundary lobe hypotheses.**

## 6. Tree-size and rural audits

Under the explicit defect-one condition on **every individual node
piece**, Theorem 3.2 forbids five nodes on a root-to-leaf path.  Under the
actual-two-cut condition on child-subtree lobes, Lemma 4.1 bounds every
node's number of children by 108.  A rooted tree with at most four levels
therefore has at most

\[
                     1+108+108^2+108^3=1,271,485
\]

nodes.  The count is correct.

For the rural alternative, the hypotheses now explicitly require:

1. the pieces cover the whole complex bag;
2. the quotient obtained by contracting every piece separately has a
   plane embedding after deleting two neutral singleton vertices;
3. every parallel contact occurrence is retained in that quotient; and
4. every piece has a disk embedding rural in the induced rotation.

Replacing disjoint quotient-vertex disks by those rural drawings draws
every vertex and edge of `G-{q_1,q_2}`.  Hence that deletion is planar and
the graph is two-apex.  Planarity of the coarse contracted
`K_5-{ab,ac}` alone would not suffice, and the theorem does not claim it
does.

**Verdict: both conclusions are GREEN under their explicit hypotheses.**

## 7. Exact conditional scope

The following inputs are **not proved** by this theorem:

1. Norin--Totschnig gives a `K_7^vee` minor, not automatically a spanning
   model with exactly one complex bag and six singleton bags.
2. Even in a one-complex normalization, seven-connectivity forces a whole
   lobe behind one two-cut to see at least five singleton labels, but it
   does not force every annular difference or node piece in a nested web
   to do so.  Parent and child adhesions may contribute four or more
   nonlabel boundary vertices.
3. An arbitrary complex bag is not proved to possess the rooted-tree
   decomposition in Section 4.
4. The full piece quotient is not proved to be planar, nor are its society
   rotations proved globally compatible.
5. The theorem leaves every bounded web, every `abba/acca` four-piece
   conflict, and every defect-at-least-two piece unresolved.

Therefore the fully proved new mathematical content is:

> **Any five disjoint consecutive connected pieces, each meeting at least
> five rows of a singleton `K_6-{ab,ac}`, force a `K_7`-minor.**

The finite web theorem is a correct conditional corollary.  It is not a
reduction already known to hold for every hypothetical `HC_7`
counterexample.

## 8. Final assessment

**Overall verdict: AMBER as a route, with GREEN component theorems.**  The
chain theorem is an independently verified infinite-family result.  The
web/state and rural conclusions are rigorous conditional statements after
the coverage repair.  The unproved decomposition/existence step is large
and must remain visible; suppressing it would turn the result into a false
claim of progress on all near-`K_7` models.
