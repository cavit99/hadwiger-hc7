# Independent audit of the exact two-cut order-eight completion

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_order8_two_cut_completion.md`](hc7_order8_two_cut_completion.md),
draft SHA-256

```text
bf0bfe7b178910e151149b93288ad177636c6be4a040bb36f713251ea0600d60
```

and promoted SHA-256

```text
70dc6941781f5023e0848c6db7c3924d2ae78382e98aeb909882a1eaa54ec206
```

The promoted revision changes only the status metadata and adds the link to
this audit.  This is a separate internal mathematical audit, not external
peer review.  The theorem closes one unbounded conditional residue; it is
not a proof of `HC_7`.

## 1. Imported response normal form

The audited response-orientation theorem supplies exactly the hypotheses
used here.  In particular:

- `A_d,A_e` are disjoint, connected, adjacent, and have exact defects
  `d,e`;
- `P,R` are nonempty independent sets and an actual `P`--`R` edge exists;
- `d,e` are nonadjacent and each has a neighbour in both `P,R`;
- the closed `C`-side realizes the four-block partition
  `P|R|{d}|{e}`; and
- every `Q_i` is connected and adjacent to every literal boundary vertex.

No palette colour is identified with a branch-set label in the completion
argument.

## 2. Exhaustion of the portal cases

For fixed `j`, the two portal sets

```text
D_d = N(d) intersect V(Q_j),
D_e = N(e) intersect V(Q_j)
```

are nonempty.  They have distinct representatives unless their union has
order one.  In the latter case nonemptiness forces
`D_d=D_e={q}`.  Thus the two cases in the proof are exhaustive.

When distinct representatives `q_d,q_e` exist, a simple
`q_d`--`q_e` path in connected `Q_j` is nontrivial.  It is disjoint from
`A_d,A_e`, which lie in the different component `C`.  Splitting the path
at any edge gives nonempty adjacent connected subpaths: the prefix retains
the literal `d`-contact at `q_d`, and the suffix retains the literal
`e`-contact at `q_e`.  The three connected subgraphs therefore satisfy the
audited reserved-path theorem with boundary blocks `P,R`.  That theorem
does not require its supporting open shore to be connected, so using
`C union Q_j` causes no hidden hypothesis failure.

## 3. The common-portal contraction

Suppose `D_d=D_e={q}`.  The three sets

```text
{q,d},   A_d union P,   A_e union R
```

are pairwise disjoint and connected.  Each contains an edge: `qd` is an
edge, and every boundary vertex in `P` or `R` has a neighbour in its
displayed defect-one connected subgraph.  Hence their simultaneous
contraction is a proper minor.

Write their images as `Z_d,Z_P,Z_R`.  Together with the untouched vertex
`e`, all six required adjacencies of a `K_4` are present:

1. `Z_d e` is represented by `qe`, since `q` is also the unique
   `e`-portal;
2. `Z_d Z_P` and `Z_d Z_R` are represented by the neighbours of `d` in
   `P` and `R`;
3. `e Z_P` and `e Z_R` are represented by the neighbours of `e` in
   `P` and `R`; and
4. `Z_P Z_R` is represented by an actual boundary edge between `P,R`.

Thus the four objects receive four distinct colours in every proper
six-colouring of the minor.

The sentence in the source about restricting to the “untouched vertices
`Q_i union S`” is read together with its immediately following pullback:
the literal vertices `d` and those in `P,R` were contracted, so one keeps
the colouring on `Q_i union {e}` and assigns to those boundary vertices the
colours of `Z_d,Z_P,Z_R`.  No vertex of `q,A_d,A_e` is expanded.  This is
the same restriction-and-boundary-pullback operation used by the audited
reflection theorems.

The pullback is proper.  Each of `P,R,{d},{e}` is independent; the four
blocks receive different colours; and every edge from an untouched vertex
of `Q_i` to a contracted boundary vertex is represented by an edge to the
corresponding contraction image.  It therefore induces exactly
`P|R|{d}|{e}`, not a coarsening.

## 4. Three-way gluing

The preceding argument applies separately with `i=0` and `i=1`; it does
not require the two resulting proper minors or colourings to coexist.
Each individual closed component-side realizes the same four labelled
blocks.  The imported closed `C`-side colouring realizes those blocks as
well.  A bijection on the four used block colours extends to a permutation
of the six-colour palette, so the three restrictions can be aligned on
every literal boundary vertex.  The open components `C,Q_0,Q_1` are
pairwise anticomplete, and the aligned colourings consequently glue to a
proper six-colouring of `G`.

## 5. Trust boundary

The proof is independent of the orders and internal structures of the
three components and handles both bipartition sizes.  It closes the exact
two-lobe two-cut response normal form completely.  It does not prove that
an arbitrary order-eight component has such a two-cut, nor does it close
the remaining three-connected or singleton-selected order-eight cases.

Within the theorem's stated hypotheses, no gap was found.
