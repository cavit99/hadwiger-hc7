# A literal decoder for the exact-two four-gate obstruction

**Status:** proved.  The displayed branch sets give a direct certificate.
The accompanying script checks the certificate for every minimal row-support
assignment and independently replays one instance with an exact SMT minor
oracle.  This result excludes the specific augmentation barrier in
`active/hc7_five_colour_exact_two_row_linkage.md`; it is not a proof of the
general exact-two branch or of `HC_7`.

## 1. A label-free three-carrier decoder

### Lemma 1.1

Let `A,B` be disjoint connected subgraphs with an edge between them, and let
`X` be a four-clique disjoint from `A union B`.  Suppose `A` is adjacent to
every vertex of `X`.  Fix `x in X`.  Suppose there are three pairwise
disjoint, pairwise adjacent connected subgraphs `R_1,R_2,R_3`, disjoint from
`A union B union X`, such that

* `R_1` is adjacent to `A` and to every vertex of `X-{x}`;
* `R_2` is adjacent to `B` and to every vertex of `X`;
* `R_3` is adjacent to every vertex of `X`.

Then the host graph contains a `K_7` minor.

#### Proof

The seven branch sets are

\[
 \{q\}\ (q\in X-\{x\}),\qquad
 A\cup\{x\},\qquad
 R_1,\qquad B\cup R_2,\qquad R_3.                    \tag{1.1}
\]

They are connected and disjoint.  The four sets arising from `X` are
pairwise adjacent.  The last three are pairwise adjacent by hypothesis.
The displayed contact assumptions give all adjacencies between these two
groups: `R_1` uses `A` for the exceptional set `A union {x}`, while `R_2`
and `R_3` contact `x` directly.  Finally `A` is adjacent to `B`, so
`A union {x}` is adjacent to `B union R_2`.  Thus (1.1) is a `K_7` model.
\(\square\)

This lemma is the reusable content of the calculation below.  It makes no
reference to colours, path order, or the particular four-gate graph.  What
is special to that graph is the availability of the three carriers with the
stated asymmetric contacts.

## 2. Literal four-gate corollary

Let `A,B` be disjoint connected subgraphs with an edge between them.  Let

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad
 Y=\{y_0,y_2,y_3,y_4\}
\]

be disjoint four-cliques, disjoint from `A union B`, such that `A` has a
neighbour at every vertex of `X` and `B` has a neighbour at every vertex of
`Y`.  Let `z_0,z_1,z_2,z_3` be further distinct vertices, disjoint from all
these objects.  Assume the following literal adjacencies:

* `z_3` is adjacent to `y_2`, to `x_1,x_2,x_4`, and to `A`;
* `z_0` is adjacent to `y_3` and to every vertex of `X`;
* `y_4` is adjacent to both `z_1,z_2`;
* `z_2x_1,z_1x_2,z_1x_3,z_1x_4` are edges.

No adjacency between `z_2` and `z_3` is required.

### Corollary 2.1

Under these hypotheses the host graph contains a `K_7` minor.

#### Proof

Use Lemma 1.1 with

\[
 x=x_3,\quad R_1=\{y_2,z_3\},\quad
 R_2=\{y_3,z_0\},\quad R_3=\{y_4,z_1,z_2\}.
\]

Equivalently, the following are the seven branch sets:

\[
 \{x_1\},\quad
 \{x_2\},\quad
 A\cup\{x_3\},\quad
 \{x_4\},\quad
 \{y_2,z_3\},\quad
 B\cup\{y_3,z_0\},\quad
 \{y_4,z_1,z_2\}.                                      \tag{2.1}
\]

They are nonempty, connected and pairwise disjoint.  The first four are
pairwise adjacent because `X` is a clique.  The last three are pairwise
adjacent through the clique edges `y_2y_3,y_2y_4,y_3y_4`.

The fifth set meets the first, second and fourth through `z_3`, and meets
the third through the edge from `z_3` to `A`.  The sixth meets all first
four through `z_0`.  Finally, the seventh meets `x_1` through `z_2` and
meets `x_2,x_3,x_4` through `z_1`.  Thus all seven sets in (2.1) are
pairwise adjacent.  They are a literal `K_7` model.  \(\square\)

## 3. Application to the audited gate graph

In the twelve-vertex graph of Section 7 of
`active/hc7_five_colour_exact_two_row_linkage.md`, give the vertices the
notation

\[
 X=\{x_1,x_2,x_3,x_4\},\quad
 Y=\{y_0,y_2,y_3,y_4\},\quad
 Z=\{z_0,z_1,z_2,z_3\}.
\]

The gate rule joins `z_i` to every core vertex of a different colour, so all
literal adjacencies in Corollary 2.1 hold.  The two equal row bags play the
roles of `A,B`.  Their support-six property gives the required contacts with
`X,Y`, and the declared common contact of `z_3` gives the edge from `z_3` to
`A`.

Consequently **every** extension described there already has a `K_7` minor.
This is independent of which endpoint of a two-vertex row supplies any
required contact.  In particular, the raw-path-to-four-linkage obstruction
is real inside `H`, but this exact coloured four-gate realization cannot be
the residue of a `K_7`-minor-free host.

The script `active/hc7_exact_two_gate_k7_probe.py` enumerates all `4096`
minimal endpoint choices and validates the same model (2.1) in every case.
It separately checks Kempe connectivity in the matching-deleted graph; `256`
of the minimal assignments realize both named locks, and all of those are
therefore excluded a fortiori.
Its output is

```text
minimal_support_graphs 4096
two_lock_graphs 256
graphs_with_literal_uniform_K7 4096
uniform_K7_model ((0,), (1,), (2, 12, 13), (3,), (5, 11),
                  (6, 8, 14, 15), (7, 9, 10))
```

## 4. Exact remaining gap

Corollary 2.1 uses the gate's near-complete colour-incidence matrix.  A general
raw nonmonotone path in a four-connected residue need not provide that
matrix, and `K_7`-minor-freeness alone does not turn the raw path into a
member of a four-linkage by any argument given here.

The next useful augmentation statement must therefore extract, from the
edge-local double-critical paths and the two literal core cliques, either

1. the three-carrier pattern of Lemma 1.1 (possibly after contracting disjoint
   shore paths);
2. a four-linkage with a nonmonotone member; or
3. an actual separator retaining the named support models.

Merely retaining two differently coloured common-contact vertices is not
the missing invariant.
