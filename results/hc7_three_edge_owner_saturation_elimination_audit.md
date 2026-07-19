# Independent internal audit of the three-probe saturation theorem

**Verdict:** GREEN for the exact source revision

```text
779b6ce18ae3ba9761648ff7cacdbb33b62510cee6b550e502f379468da0fee1
```

of
[`hc7_three_edge_owner_saturation_elimination.md`](hc7_three_edge_owner_saturation_elimination.md).
This is a separate internal mathematical audit, not external peer review.
It checks the connected-transversal lemma, the imported three-owner and
opposite-shore hypotheses, the endpoint-saturation argument, the literal
branch-set transfer, preservation of the selected response data and relaxed
first-hit rank, and the spanning `K_6` conclusion.

The proof body is identical to the independently checked revision
`4a3a1c879b157ca464b9840fb3c6ccfa0698a94fc915a45fd3b5895bb0b286eb`;
the new hash records only promotion status and same-directory link repairs.

## 1. Imported setting

The audited three-owner concentration theorem supplies the precise facts
used here.  In its concentrated branch,

```text
U = U_0 dotcup C
```

has `U_0` and `C` nonempty and connected, `U_0` adjacent to `C`, every old
contact from `U` to an owner `R_i` contained in `C`, and every nonowner
contact retained at `U_0`.  The prescribed `U`-root and the endpoint of the
fixed response edge lie in `U_0`.  Consequently the sets

```text
B = N(U_0) cap C,       A_i = N(R_i) cap C
```

are all nonempty.  The same theorem gives, for each pair of owners, two
vertex-disjoint contact edges with distinct ends in `C`.  The pair may use
different ends for different choices of owners; the proof requires no
global consistency among those choices.

The edge `h` and its anticompleteness to the selected contact-edge endpoints
are additional explicit hypotheses of the audited source.  They are exactly
what the joint three-edge chromatic fork needs in order to put the common
deletion graph in the `{5,6}` chromatic alternative.  The theorem does not
claim to derive the existence of `h` from three-owner concentration alone.

## 2. Connected-transversal lemma

Choose an inclusion-minimal connected vertex set `T` meeting
`B,A_1,A_2,A_3`.  If every `A_i` were contained in `T`, then each `A_i`
would have at least two vertices.  In a spanning tree of `C[T]`, deleting
any leaf leaves a connected set.  Minimality therefore makes every leaf the
unique member of one of the four target sets.  No leaf can be unique in an
`A_i`; hence every leaf would have to be the unique member of `B cap T`.
Two distinct leaves cannot both be that one vertex.  This contradiction
proves that some owner-contact vertex lies outside `T`.

For the component `L` of `C-T` containing such a vertex, connectedness of
`C` makes every component of `C-T` adjacent to `T`.  Thus `C-L`, consisting
of `T` and all the other components, is connected.  It meets `B` and every
`A_i`, while `L` is nonempty, connected, proper and meets an `A_i`.  This
establishes every conclusion of Lemma 2.1; no hidden two-connectivity
assumption on `C` is used.

## 3. From three five-chromatic probes to pairwise portal intersections

Suppose, more strongly, that the four selected endpoints induce a `K_4` for
each of the three owner pairs.  If the `C`-ends for one pair are
`a_i,a_j`, then both are adjacent to both owner branch sets.  Hence

```text
{a_i,a_j} subseteq A_i cap A_j.
```

The two vertices are distinct because the contact edges are vertex-disjoint.
Repeating this independently for the three owner pairs proves
`|A_i cap A_j| >= 2` for every pair.  The notation does not require the
vertex called `a_i` in one pair to be reused in another pair.  Sections 2
and 4 below then contradict the lexicographic choice of the labelled model.
Thus at least one owner pair has four endpoints which do **not** induce a
`K_4`.

For that pair, the selected contact edges are vertex-disjoint and both are
anticomplete to the ends of `h` by hypothesis.  The audited joint three-edge
fork places its common deletion graph in `{5,6}` and says that the
five-chromatic case would force precisely the excluded endpoint `K_4`.
Consequently this pair's common deletion graph is six-chromatic.  This
checks the stronger order of conclusions in the current source; it does not
merely infer that one of three unspecified probes is six-chromatic.

## 4. Literal branch-set transfer

Apply Lemma 2.1 and put `U* = U_0 union (C-L)`.  Since `C-L` is connected
and meets `B`, it has an edge to connected `U_0`; hence `U*` is connected.
It contains the prescribed root and the fixed response endpoint.  Because
`C-L` meets every `A_i`, `U*` retains an edge to every owner.  It retains
all nonowner contacts through `U_0`, including the fixed contact with `D`.

Choose an owner `R_i` met by `L` and replace it by `R_i union L`.  This
enlarged branch set is connected.  The seven branch sets remain nonempty,
pairwise disjoint and spanning.  Enlargement cannot destroy an adjacency
not incident with `U`, and the preceding paragraph checks every adjacency
incident with `U*`.  Thus the transfer either creates the formerly missing
`X-Y` edge and yields an explicit `K_7`-minor model, or yields another
compatible spanning labelled `K_7`-minus-one-edge model.  No palette colour
is used as a branch-set label.

The selected response subgraph and fixed edge into `U_0` are untouched.
Every ranked path with a terminal label other than `U` avoided the whole old
branch set `U`, and therefore avoids the moved set `L`.  A ranked `U`-path
ending in `L` can be replaced, from its same source port, by a path in the
fixed connected response subgraph and the fixed final edge into `U_0`.
The relaxed rank permits overlap inside that response subgraph and all other
ranked paths avoid the new terminal in old `U`.  Hence rank does not
decrease.  The new model has the same maximum rank and strictly smaller
`U`, contradicting the declared secondary minimum.

## 5. Six-chromatic probe and spanning model

The contradiction shows that not all three common-deletion graphs are
five-chromatic.  The joint fork places each in `{5,6}`, so one is exactly
six-chromatic.  The established parameter-six case of Hadwiger gives it a
`K_6` minor.

A seven-connected graph is seven-edge-connected.  Deleting the three
marked edges therefore leaves the common deletion graph connected.  In a
connected graph, a clique-minor model can be made spanning: take every
component of the vertices outside the model and absorb it, along an edge in
a spanning forest of the contracted remainder, into an adjacent branch
set.  This preserves disjointness, connectedness and all existing branch-set
adjacencies.  The source's spanning conclusion is therefore valid.

## 6. Exact trust boundary

The theorem is conditional on the concentrated three-owner configuration
and on an opposite-shore edge satisfying the explicit anticompleteness
hypothesis.  It proves only that one of the three common deletion hosts is
six-chromatic and has a spanning unlabelled `K_6`-minor model.  It does not
align that model with the inherited five labels, preserve a selected
boundary trace inside that model, produce a common closed-shore partition,
or construct a `K_7` minor from the surviving probe.  No unresolved gap
remains in the theorem as stated.
