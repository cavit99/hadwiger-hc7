# Independent audit: terminal-free bilateral planar endgame

Audited file: `results/hc7_exact7_terminal_free_bilateral_endgame.md`.

## Verdict

**GREEN.**  Two terminal-free disk pages with the same literal boundary
cycle give a plane drawing of `G-{v,w,a,b}`.  The exact Moser edges and the
audited portal nonedges make `{a,b,w}` independent, so a four-colouring of
the planar core extends with one shared new colour on that independent set
and a sixth colour on `v`.

This conclusion needs no embedding of either side terminal.  It is
specific to the exact cell and does not say that the present rural quotient
has already supplied the required two disk embeddings.

## 1. Exact exhaustion

In the exact cell,

```
N_G(D_a)=U union {w,a},
N_G(D_b)=U union {w,b},
```

the open shores are anticomplete, and the frozen cell accounts for every
vertex as

```
D_a dotunion D_b dotunion U dotunion {v,w,a,b}.
```

Therefore deleting `{v,w,a,b}` leaves exactly the union of
`J_a^circ=G[D_a union U]` and `J_b^circ=G[D_b union U]`, identified on
their common induced graph `G[U]`.  There is no omitted opposite-shore
edge or extra vertex class.

## 2. Disk gluing

The literal graph `G[U]` has edges

```
02, 26, 65, 54, 40,
```

and is a five-cycle.  In each assumed disk embedding this same labelled
cycle is the entire graph-boundary intersection.  Reflecting one disk if
needed reverses its cyclic order.  Gluing the two disks along the labelled
cycle creates no crossing: one page lies inside, the other outside, and
the exact anticompleteness of `D_a,D_b` accounts for every edge between
the pages.  The resulting graph is exactly `G-{v,w,a,b}`, not merely a
subgraph of it.  It is planar.

## 3. Independence of the fifth-colour class

The Moser boundary has `ab=13` absent.  The audited exact-cell portal
lemma proves `wa,wb` absent.  Hence

```
{a,b,w}
```

is a literal independent set.  No further nonedge is needed.  In
particular, `v` is not put in this class.

## 4. Six-colour extension

Apply the Four Colour Theorem to `G-{v,w,a,b}` and use colours 1--4.
Give `a,b,w` colour 5 and `v` colour 6.

Every edge from the four reinserted vertices to the planar core joins a
colour in `{5,6}` to one in `{1,2,3,4}`.  There is no edge inside the
colour-5 class.  Every possible edge within `{v,w,a,b}` not already
excluded has `v` as one endpoint and therefore joins colours 6 and 5.
Thus the extension is a proper colouring of the literal original graph.

## 5. Trust boundary

The theorem proves the exact conditional implication

```
two terminal-free cofacial disk pages => chi(G)<=6.
```

It does not prove that a planar quotient with contracted poles expands to
such a page.  Induced-pole expansion remains the sole geometric obligation
in this branch after the separately audited low-cut descent.
