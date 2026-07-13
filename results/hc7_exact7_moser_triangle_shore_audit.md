# Independent audit: triangular exterior shore in the pure-Moser crossing

**Status:** **GREEN**; the two expository corrections recorded below have
been applied.  The
finite enumeration, the defect reduction, and the literal minor lift are all
valid.  This audit does not address the order-at-least-four 3-connected
remainder.

## 1. Local hypotheses and defects

Write `N=N_G(v)`.  The component

\[
                         D=\{x_1,x_2,x_3\}
\]

of `G-N[v]` is a triangle.  Hence each `x_i` has exactly two neighbours in
`D`, is not adjacent to `v`, has no neighbour in any other component of
`G-N[v]`, and has all of its remaining neighbours in `N`.  Therefore

\[
  7\le d_G(x_i)=2+|N_G(x_i)\cap N|,
\]

so, for `D_i=N-N_G(x_i)`, one has `|D_i|<=2`.

The assertion that `D` is `N`-full means that every literal `s in N` has a
neighbour among `x_1,x_2,x_3`.  Equivalently, there is no `s` missed by all
three vertices, which is exactly

\[
                         D_1\cap D_2\cap D_3=\varnothing.
\]

No additional pairwise-intersection restriction is used by the verifier.
It therefore checks a superset of any states that might also be excluded by
seven-connectivity.

## 2. Independent reconstruction of the crossed page

The verifier constructs the correct ten-vertex graph:

* vertices `0,...,6` induce exactly the eleven displayed Moser edges;
* vertex `7=v` is adjacent to all seven boundary vertices;
* `8=p05` gives the path `0-8-5`;
* `9=p24` gives the path `2-9-4`;
* no other edge is inserted.

I independently re-enumerated this graph using `frozenset` vertex sets,
NetworkX connectivity, and direct edge tests, without importing any function
from the certificate.  This gave

```text
connected boundary-meeting subsets = 696
distinct boundary traces of K4 models = 598
```

The certificate's own `connected` routine is a standard fixed-point search
from the least set bit and returns true exactly when the selected subgraph is
connected.  Its recursive search is exhaustive:

1. `connected_sets` contains every nonempty connected subset meeting the
   literal boundary;
2. increasing indices enumerate every unordered four-set of candidate bags
   exactly once;
3. `bag & used` enforces vertex-disjointness;
4. `neighbours[bag] & old_bag` is exactly the existence of a literal edge
   between the two disjoint bags; and
5. the test against every previously selected bag enforces all six `K_4`
   adjacencies.

Every relevant bag must meet the boundary, because it must contain a
literal neighbour of each `x_i`; hence the initial boundary-meeting filter
loses no witness.  Passing from models to boundary traces also loses no
information: all later contact predicates depend only on those traces, and
one actual connected model is retained for every trace.

## 3. Exhaustiveness of the defect states

There are

\[
                    1+\binom71+\binom72=29
\]

defect sets of order at most two.  Since permuting `x_1,x_2,x_3` changes
nothing, `combinations_with_replacement` correctly enumerates their
unordered triples, including repetitions.

There are \(\binom{31}{3}=4495\) unordered triples before imposing fullness.
For a fixed boundary element, there are seven defects containing it and
hence \(\binom{9}{3}=84\) triples in which it belongs to the total intersection.
Summing over the seven elements gives `588`; a triple whose intersection is
the two-set `{s,t}` is counted twice, and there is exactly one such triple
for each of the `21` pairs.  No intersection has order three.  Thus the
number discarded is

\[
                         588-21=567,
\]

and the number retained is

\[
                         4495-567=3928.
\]

For each retained triple, the verifier sets `contact_i=N-D_i` and tests

\[
       (B_j\cap N)\cap contact_i\ne\varnothing
       \qquad(1\le i\le3,\ 1\le j\le4).
\]

This is exactly the condition that every `x_i` has a literal boundary edge
to every bag `B_j`.  My independent enumeration found a witness for all
3928 triples and no failure.  Independently rebuilding the canonical
state-to-trace table also reproduced

```text
f98e3da2c226d53104ba3bfb877cb18b1be9dd65c50363201414d939f63f123e
```

The verifier imports only `hashlib` and `itertools` from the Python standard
library, so the advertised certificate is dependency-free.

One sentence in Lemma 2 should be read with the quantifiers made explicit:
each bag contains, **for every `i`**, a boundary vertex outside `D_i`.
It need not contain one boundary vertex lying outside all three defects.
The following sentence, saying equivalently that each `x_i` sees each bag,
states the intended and verified condition correctly.

## 4. Audit of the contraction and lift

The Moser pairs `05` and `24` are nonedges, so each external path has a
nonempty interior.  The paths are vertex-disjoint, their four endpoints are
distinct, and their interiors lie outside `N[v]`.  They also lie in an
exterior component different from `D`.

For complete precision, first pass to the subgraph consisting of `N[v]` and
the two selected paths, delete every unused edge, and discard every unused
vertex.  On each path contract all edges between consecutive internal
vertices, leaving its endpoints uncontracted.  The nonempty connected
interior becomes `p05` or `p24`, and the quotient is exactly the crossed
page `W`.

Let `pi` be this contraction map.  For a quotient bag `B_j`, put

\[
                    \widetilde B_j
                    =\bigcup_{z\in B_j}\pi^{-1}(z).
\]

Every point-preimage is connected: it is a singleton for a literal vertex
and the whole path interior for `p05` or `p24`.  A quotient edge retained in
`W` has a literal preimage edge, so connectivity of `B_j` implies
connectivity of `widetilde B_j`.  Distinct quotient bags have disjoint
point-preimages, and every quotient adjacency likewise lifts through a
retained literal edge.  This remains valid if one bag contains both path
vertices or if an adjacency uses an endpoint--path edge.

The literal boundary vertices are never contracted.  Consequently every
contact certified from the trace of `B_j` remains a literal edge from
`x_i` to `widetilde B_j`.  The four lifted bags lie outside `D`; the three
singletons `{x_1},{x_2},{x_3}` are mutually adjacent because `D` is a
triangle.  Thus these seven bags are disjoint, connected, and pairwise
adjacent, giving the claimed literal `K_7` model.

The proof text should explicitly mention deletion of unused vertices before
forming the ten-vertex page.  This is a harmless subgraph operation, not a
mathematical gap; after finding the quotient model, the argument correctly
lifts it back to the original graph before adjoining the triangle bags.

## 5. Scope

The certificate and lift close exactly the triangular exterior shore in the
stated favourable two-path crossing.  They do not establish the existence of
those two disjoint external paths and say nothing about a 3-connected
exterior component of order at least four.
