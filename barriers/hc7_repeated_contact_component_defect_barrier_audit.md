# Independent audit of the repeated-contact component-defect barrier

**Verdict:** **GREEN** at the exact source and verifier revisions recorded
below.  Both labelled models have defect one and retain either an incident
or an independent repeated contact without changing the component-contact
graph.  The host is seven-connected and `K_7`-minor-free, but is
six-colourable and carries none of the selected dynamic colouring data of a
hypothetical counterexample.

This is a separate internal mathematical audit, not external peer review.

## Exact revisions audited

```text
a4a194219a8cdc917f421501daddb86fef6acb11172b16e7fa7f6c790a23a9a5  barriers/hc7_repeated_contact_component_defect_barrier.md
4af016a40a34baa3c7e193c6efc3e56809c9576e97c30e23fc5aef196dda480b  barriers/hc7_repeated_contact_component_defect_barrier_verify.py
```

The source change after the mathematical audit is status-only: it replaces
"audit pending" with a link to this GREEN audit.

## 1. The host graph

The listed thirty edges give the standard icosahedral graph `I`: every
vertex has degree five.  I independently checked that the graph is planar,
five-connected and isomorphic to the standard icosahedral graph.  The
verifier checks the edge count and all degrees directly.

In `G=K_2 vee I`, deletion of at most six vertices leaves a universal apex,
unless both apex vertices were deleted.  In the latter case at most four
vertices of the five-connected graph `I` were deleted, so the remainder is
connected.  Hence `kappa(G)>=7`.  Every old vertex has degree seven, so its
neighbourhood is a cut of order seven; equivalently `kappa(G)=7`, as stated
by the verifier.

If `G` had a `K_7`-minor model, at most two branch sets could contain the two
apex vertices.  At least five branch sets would lie wholly in `I` and form a
`K_5` minor there, impossible in a planar graph.  Thus `G` is
`K_7`-minor-free.  This is an unbounded written implication from planarity,
not a bounded minor-oracle calculation.

## 2. Incident repeated contacts

The sets

```text
{p}, {q}, {3,4,7,8,9,10,11}, {5}, {0,1}, {2}, {6}
```

are disjoint, connected and spanning.  The first three are pairwise
adjacent and adjacent to every one of the last four.  On the protected
sets, the verifier checks that the only absent pair is `{5},{2}`; the five
present pairs are witnessed by the edges listed in the source.

Thus the four-vertex component-contact graph is `K_4` minus one edge.  Five
bichromatic pair graphs have one component and the missing pair has two,
so

```text
Delta = 5 + 2 - 4 - 2 = 1.
```

The two edges `50,51` share their endpoint `5` and both join the same two
selected subgraphs.  Replacing one by both changes no quotient adjacency,
component count or defect.

## 3. Independent repeated contacts

The second sets

```text
{p}, {q}, {4,5,7,9,10,11}, {0,1}, {8,2}, {3}, {6}
```

are again disjoint, connected and spanning.  Direct inspection, replayed
by the verifier, gives the same protected contact graph `K_4` minus the
first--third edge.  The two contacts `08,12` are vertex-disjoint and both
join the first two protected subgraphs.  The same calculation therefore
gives defect one, unchanged by the repeated literal contact.

Both quotient graphs are two-trees: `K_4` minus one edge is obtained from a
triangle by stacking the fourth vertex on an edge.  The three anchors turn
either labelled quotient into a spanning `K_7`-minus-one-edge model, not a
`K_7` model.

## 4. Scope and verifier

The icosahedron is four-colourable and the two adjacent universal vertices
can use two new colours, so `G` is six-colourable.  It is not a
minor-minimal non-six-colourable graph.  No selected boundary trace,
fixed-trace critical subgraph, Rado first-hit defect or operation-specific
response is present.  The examples therefore refute only a static inference
from repeated contact multiplicity to lower component defect.  They do not
refute a dynamic exchange theorem using contraction-criticality.

Running

```text
python3 barriers/hc7_repeated_contact_component_defect_barrier_verify.py
```

at the audited revisions prints exactly

```text
GREEN repeated-contact component-defect barrier: kappa(G)=7, incident and independent defect-one models verified
```

No unresolved gap remains within this barrier's stated scope.
