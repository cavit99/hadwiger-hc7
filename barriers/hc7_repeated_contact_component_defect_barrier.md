# Repeated contacts do not lower component defect

**Status:** explicit finite barrier; deterministic verifier included;
separate internal audit GREEN in
[`hc7_repeated_contact_component_defect_barrier_audit.md`](hc7_repeated_contact_component_defect_barrier_audit.md).
The examples are seven-connected, `K_7`-minor-free and have a
spanning labelled `K_7`-minus-one-edge model whose four non-anchor branch
sets have component defect one.  One example has two incident contacts and
the other has two independent contacts between the same two named branch
sets.  Both graphs are six-colourable and do not carry the selected
fixed-trace response of a hypothetical counterexample.

The accompanying checker is
[`hc7_repeated_contact_component_defect_barrier_verify.py`](hc7_repeated_contact_component_defect_barrier_verify.py).

## 1. Host graph

Let `I` be the icosahedral graph on vertices `0,...,11`, with edges

```text
01 05 07 08 0-11
12 15 16 18
23 26 28 29
34 36 39 3-10
45 46 4-10 4-11
56 5-11
78 79 7-10 7-11
89
9-10
10-11
```

and all symmetric incidences understood.  Add adjacent vertices `p,q`,
each complete to `I`, and call the resulting graph

\[
                              G=K_2\vee I.             \tag{1.1}
\]

### Lemma 1.1

The graph `G` is seven-connected and has no `K_7` minor.

#### Proof

The icosahedral graph is planar and five-connected.  Delete at most six
vertices of `G`.  If `p` or `q` remains, that vertex joins every remaining
vertex.  If both are deleted, at most four vertices of `I` were deleted,
so the remainder of `I` is connected.  Thus `G` is seven-connected.

In any `K_7`-minor model in `G`, at most two branch sets contain `p` or
`q`.  The other at least five branch sets lie in `I` and would form a
`K_5` minor there.  This is impossible because `I` is planar. \(\square\)

## 2. Two incident contacts

Use the three anchor branch sets

\[
 \{p\},\qquad \{q\},\qquad
 R=\{3,4,7,8,9,10,11\},                               \tag{2.1}
\]

and four further branch sets

\[
 A=\{5\},\qquad B=\{0,1\},\qquad C=\{2\},\qquad
 D=\{6\}.                                             \tag{2.2}
\]

These seven sets partition `V(G)`.  They are connected.  The first three
are pairwise adjacent and each is adjacent to every set in (2.2).  Among
the four latter sets every pair is adjacent except `A,C`; explicitly the
five adjacencies are witnessed by

\[
 50,\ 51;\qquad 56;\qquad 12;\qquad 16;\qquad 26.     \tag{2.3}
\]

Thus they give a spanning labelled `K_7`-minus-one-edge model, and the
component-contact graph on `A,B,C,D` is `K_4` minus the edge `AC`.  It is a
two-tree.  Its five present bichromatic pairs are connected, while the
missing pair has two components, so

\[
                              \Delta=5+2-4-2=1.        \tag{2.4}
\]

The two edges `50,51` are incident and join the same two named branch
sets.  They leave the contact graph and (2.4) unchanged.

## 3. Two independent contacts

Use instead

\[
 \begin{aligned}
 R'&=\{4,5,7,9,10,11\},\\
 A'&=\{0,1\},& B'&=\{8,2\},& C'&=\{3\},& D'&=\{6\}.
 \end{aligned}                                        \tag{3.1}
\]

Together with `{p},{q}`, these again partition `V(G)` into seven connected
sets.  The set `R'` is adjacent to all four other sets.  Their contact graph
is again `K_4` minus `A'C'`; the five present adjacencies are witnessed by

\[
 08,\ 18,\ 12;\qquad 16;\qquad 23;\qquad 26;\qquad 36.
                                                               \tag{3.2}
\]

The independent edges `08,12` both join `A'` to `B'`.  As before, the
component defect is exactly one and the repeated contact does not alter it.

## 4. Exact scope

The construction simultaneously has:

* seven-connectivity;
* `K_7`-minor exclusion;
* a spanning labelled `K_7`-minus-one-edge model;
* three pairwise adjacent connected anchor sets;
* four nonempty protected labels, each adjacent to every anchor;
* a defect-one two-tree component-contact graph; and
* either an incident or an independent pair of literal edges between one
  pair of named branch sets.

It therefore refutes every static claim that such a repeated pair must
lower the component defect or complete the missing model adjacency.

It does **not** satisfy the dynamic hypotheses of the active `HC_7`
branch.  The graph is six-colourable (`I` is four-colourable and the two
universal adjacent vertices use two new colours), is not a minor-minimal
non-six-colourable graph, and no fixed boundary trace or Rado first-hit
failure is specified.  It also does not show that either repeated edge is
forced into a fixed-trace critical subgraph.  Thus it does not refute a
theorem that couples the pair to the full proper-minor colouring response.

## 5. Verification

From the repository root run

```text
python3 barriers/hc7_repeated_contact_component_defect_barrier_verify.py
```

Expected output:

```text
GREEN repeated-contact component-defect barrier: kappa(G)=7, incident and independent defect-one models verified
```
