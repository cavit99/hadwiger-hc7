# Boundary classification for three full order-eight components

**Status:** computer-assisted finite result; adjacent internal audit GREEN.
The host-level reductions in Sections 2 and 3 are written proofs.  The
82-type census in Section 4 is verified by the adjacent deterministic
script.  This note does not close the three-component interface.

## 1. Setting

Let `G` be a graph such that every proper minor of `G` is six-colourable,
`G` is not six-colourable, and `G` has no `K_7` minor.  Let `X` be an
eight-vertex set, put

\[
                              H=G[X],
\]

and suppose that `G-X` has at least three components, each adjacent to every
literal vertex of `X`.  Fix three of them, denoted `C_1,C_2,C_3`.

The promoted two-full-shore boundary-absorption theorem already gives

\[
                              \chi(H)\le4.                 \tag{1.1}
\]

The following two reductions identify the exact boundary-only residue left
by the third full component.

## 2. Compact `K_4` models lift to `K_7`

### Lemma 2.1

If some two-set `Z subseteq X` satisfies

\[
                              H-Z\succcurlyeq K_4,          \tag{2.1}
\]

then `G` contains a `K_7` minor.

### Proof

Write `Z={z_2,z_3}` and let `B_1,...,B_4` be the branch sets of a `K_4`
model in `H-Z`.  The seven sets

\[
 C_1,\qquad C_2\cup\{z_2\},\qquad C_3\cup\{z_3\},
 \qquad B_1,B_2,B_3,B_4                              \tag{2.2}
\]

are pairwise disjoint and connected.  Fullness makes each of the first
three sets adjacent to every `B_i`.  It also makes the unanchored set `C_1`
adjacent to each anchored set through its anchor, and makes the two anchored
sets adjacent through either opposite anchor.  The last four sets are
pairwise adjacent by the `K_4` model.  Thus (2.2) is an explicit `K_7`-minor
model.  \(\square\)

Equivalently, every `K_4` model in `H` must use at least seven of the eight
boundary vertices.  This is an unbounded host reduction: the component
interiors are never enumerated.

## 3. A clique odd-cycle transversal synchronizes all components

A **clique odd-cycle transversal** of `H` is a clique `U` for which `H-U`
is bipartite.

### Lemma 3.1

If `H` has a clique odd-cycle transversal, then `G` is six-colourable.

### Proof

Choose a bipartition

\[
                         X-U=P\mathbin{\dot\cup}Q           \tag{3.1}
\]

with `P,Q` independent; an empty side may be split when `H-U` is edgeless,
so both can be taken nonempty.  Lemma 2.1 excludes a boundary `K_4`, and
hence `|U|<=3`.  Put

\[
              \Pi=\{P,Q\}\cup\bigl\{\{u\}:u\in U\bigr\}. \tag{3.2}
\]

Fix a component `C` of `G-X` and choose two other full components `D_P,D_Q`.
Contract spanning trees of the disjoint connected sets

\[
                         D_P\cup P,\qquad D_Q\cup Q,        \tag{3.3}
\]

and delete every unused component of `G-X`, leaving `C` untouched.  This is
a proper minor.  The two contraction images together with the literal
vertices of `U` form a clique: the two components are full, and `U` is a
clique.  In every six-colouring their colours are therefore pairwise
distinct.

Pull the colouring back only to `G[C\cup X]`, assigning the colour of the
first image to `P` and the colour of the second image to `Q`.  This is
proper, and its exact equality partition on `X` is (3.2).  Repeating the
construction for every component gives component-side colourings with the
same literal partition.  Permute colour names to make them agree on `X` and
glue; distinct components of `G-X` are anticomplete.  The result is a
six-colouring of `G`.  \(\square\)

This includes the bipartite case `U=emptyset`.  It also gives the exact
state interpretation.  For a proper equality partition `Theta` of `H`, put

\[
 d_H(\Theta)=|\Theta|-\omega
   \bigl(H[\operatorname{sing}(\Theta)]\bigr).          \tag{3.4}
\]

There exists a partition of demand at most two if and only if `H` has a
clique odd-cycle transversal.  Indeed, a maximum clique of singleton blocks
leaves at most two independent blocks when the demand is at most two;
conversely (3.2) has demand at most two.  Thus failure of Lemma 3.1 means
that **every** boundary equality partition has demand at least three.  Two
opposite full components cannot reflect any returned state by the ordinary
packet-demand argument.

## 4. Exact order-eight census

### Theorem 4.1 (computer-assisted finite classification)

Up to isomorphism, exactly 82 graphs `H` on eight vertices satisfy all of

1. `chi(H) in {3,4}`;
2. `H` has no clique odd-cycle transversal; and
3. `H-Z` is `K_4`-minor-free for every two-set `Z`.

All 82 are three-colourable; there is no four-chromatic survivor.  Every
survivor contains two vertex-disjoint odd cycles.  More precisely,

\[
\begin{array}{c|r}
\text{orders of a displayed disjoint odd-cycle pair}&\text{count}\\ \hline
(3,3)&80\\
(3,5)&2.
\end{array}                                             \tag{4.1}
\]

The 82 graphs have between one and 54 exact three-colour equality
partitions.  Hence the residue does not collapse to one uniformly selected
three-colour state.  Under single-edge deletion while retaining all three
conditions, the 82 types have five edge-minimal cores, with graph6 codes

```text
G?`CQG  G?otYw  G?qbUG  GCQR@O  GCR`uo
```

The first is `2K_3` plus two isolated vertices, and `GCQR@O` is
`K_3 dotcup C_5`.  The other three codes are compact certificates for the
remaining connected or one-isolate core geometries.  The complete sorted
82-code catalogue is emitted by the verifier's `--list` option; its SHA-256
is

```text
f415269d09d9b0673b030a2125cd20a15b46a20c202463bf20d70864179e68fc
```

### Reproducible verification

Run

```text
geng -q 8 |
  python3 results/hc7_order8_three_component_boundary_verify.py
```

The exact output is

```text
order-eight graphs: 12346
three-chromatic without clique OCT: 746
four-chromatic without clique OCT: 953
compact-K4-free survivors: 82
four-chromatic survivors: 0
survivor odd-cycle packings: (3,3)=80 (3,5)=2
three-colour partition counts: min=1 max=54
edge-minimal survivor cores: 5
core graph6 codes: G?`CQG G?otYw G?qbUG GCQR@O GCR`uo
survivor-code sha256: f415269d09d9b0673b030a2125cd20a15b46a20c202463bf20d70864179e68fc
```

The verifier is dependency-free Python.  It implements exact DSATUR
backtracking, exhaustive clique-transversal testing, and an exact
deletion/contraction search for `K_4` minors on each six-vertex induced
subgraph.  It also verifies the odd-cycle packing, the full three-colour
partition spectrum, and the five edge-minimal codes.

The finite trust boundary is the standard completeness of the nauty
`geng -q 8` unlabelled catalogue, the graph6 decoder, the Python runtime,
and the displayed verifier.  No host interior occurs in the census.

## 5. Exact remaining scope

The three-component interface is reduced to the 82 isomorphism types in
Theorem 4.1, all carrying two disjoint odd cycles and only demand-at-least-
three boundary states.  This is not yet an unbounded closure.  In
particular, a proper-minor contraction can return a partition using four,
five, or six colours; the existence, or even uniqueness, of a
three-colouring of `H` does not force that contraction to select it.

The finite classification does not close the interface: no geometric
theorem yet converts the
two disjoint odd cycles, the inherited exact-seven labels, or the returned
proper-minor state into a common boundary partition or an explicit
`K_7` model.

## 6. Dependencies

- [two full shores force a four-colour boundary](hc7_two_full_shore_boundary_absorption.md)
- [adaptive packet reflection](hc7_exact7_adaptive_packet_reflection.md)
- [nested full-neighbourhood descent](hc7_nested_full_neighbourhood_descent.md)
