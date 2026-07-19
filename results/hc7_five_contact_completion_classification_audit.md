# Internal audit: exact completion with five outside contacts

**Verdict:** GREEN for the exact source revision

```text
02949267b281bc8dc883cd13e94490b10e9be8601bc9bb7a11a3f72855ee83f0
```

of
[`hc7_five_contact_completion_classification.md`](hc7_five_contact_completion_classification.md).
This is a separate internal audit, not external peer review.  The
line-by-line mathematical audit checked the immediately preceding revision;
the pinned revision changes only its opening status line to link this audit.

## 1. Constructive completion table

The six outside branch sets form a `K_6` model except possibly for `X-Y`.
The two further connected sets `A,R` are adjacent, and each misses at most
one outside set.  Under the standing reserved-component hypothesis that the
possible miss of `A` is not `D`, the source's table exhausts every ordered
miss pair.

- A polar miss together with no miss or the same polar miss is removed by
  discarding that polar bag.
- A polar miss and a universal miss are repaired by merging those two
  adjacent outside bags.
- If `A` misses `F_i`, merging `X` or `Y` with `F_i` handles precisely the
  displayed no-miss, same-miss, and polar-miss cases.

Each merger is connected, repairs `X-Y` through its universal member, and
is contacted by `A,R` through complementary members.  The five resulting
outside bags together with `A,R` are seven explicit pairwise adjacent
connected branch sets.

## 2. Sharp exceptional quotients

For distinct universal misses, the missing edges are the matching

\[
                         XY,\quad AF_i,\quad Rb.
\]

For crossed polar misses, the missing-edge graph is the four-vertex path

\[
                              A-X-Y-R.
\]

A seven-branch-set model in an eight-vertex quotient either deletes one
vertex and uses seven singletons, or uses all vertices with one connected
two-vertex bag.  Deletion cannot cover all three missing edges in either
quotient.  In the matching quotient one contraction covers at most two
matching edges.  In the path quotient the only two-vertex covers are
exactly those listed in the source; one is nonadjacent and each other one
leaves the merged bag anticomplete to a remaining singleton.  Thus both
sharpness assertions are correct.

Repairing any one of the three missing adjacencies is terminal.  In the
matching quotient, contract a present cross-edge between endpoints of the
two remaining missing edges.  In the path quotient, repair of the middle
edge permits contraction of `A-R`, while repair of an end edge permits
deletion of the other internal path vertex.  A path used as the repair must
have interior disjoint from all eight old connected sets, exactly as the
source states.

## 3. Three-owner specialization and bridge count

Choosing an omitted owner `F_i` eliminates the crossed-polar exception but
does not make raw five-contact support terminal.  The precise surviving
misses are `D` and the other `F_j`, producing `K_8-3K_2`.  This corrects the
false stronger claim that every five-contact residual completes the model.

For a residual component after deleting the two linkage paths, the literal
order-eight normal form exhausts its possible neighbours outside `C`: at
most two transversal vertices, the unique representatives of the outside
labels it contacts, and its attachments to the linkage inside `C`.  With at
most four outside contacts, one linkage attachment gives neighbourhood
order at most seven.  Seven-connectivity and the nonempty opposite component
make that an actual order-seven separation; absent that exit there must be
at least two distinct linkage attachments.  With five outside contacts,
one attachment can already give order eight, so the source correctly makes
no stronger claim.

## 4. Trust boundary

The theorem is an exact quotient construction and a literal neighbourhood
count.  It does not force a repair path, a connected residual with a usable
outside `K_5` packing, a common boundary partition, or `HC_7`.  Its quotient
sharpness is not a host counterexample: additional internally disjoint paths
or contraction-critical colouring responses may repair one of the three
gaps.
