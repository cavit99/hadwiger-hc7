# Audit: static candidate through order ten

## Verdict

**GREEN, computer-assisted.**  The complement classification is complete
and duplication-free, the reported counts reproduce, and the connected-
branch-set search is exhaustive.  Therefore every seven-connected graph
of order at most ten has a `K_7` minor.

This is a finite lower bound on a static counterexample, not a proof of
`P1`.

## 1. Complement classification

If `G` is seven-connected on `n` vertices, then `delta(G)>=7`, so

\[
 d_{\overline G}(v)=n-1-d_G(v)\le n-8.
\]

For `n=8` the complement is edgeless.  For `n=9` it is a matching plus
isolated vertices.  For `n=10` it has maximum degree at most two, and
therefore every connected component is exactly a path or a cycle.

The recursive generator lists multisets in nondecreasing order in the
fixed type list

\[
 P_1,\ldots,P_n,C_3,\ldots,C_n.
\]

Every recursive choice retains its current type index, so repeated
components are allowed while permutations of the same multiset are not.
Connected path/cycle component multisets determine the isomorphism type,
so no other isomorphism duplication occurs.  The degree filter correctly
removes path/cycle types which are unavailable at orders eight and nine.

The reproduced counts are

```text
(8, 1, 1), (9, 5, 5), (10, 106, 87)
```

where the last coordinate is the exact NetworkX vertex-connectivity
filter.

## 2. Clique-minor search

Every branch set of a seven-bag model on `n` vertices has order at most
`n-6`, because the other six bags are nonempty and disjoint.  Unused
vertices only make this upper bound smaller, so the mask cutoff loses no
model.

The verifier enumerates every nonempty connected mask within that bound.
Two masks are compatible exactly when they are disjoint and an original
graph edge joins them.  The recursive search is an exhaustive include/
exclude clique search:

* the current `available` list is inductively compatible with all chosen
  masks;
* the recursive list is additionally filtered for compatibility with the
  new mask; and
* after an unsuccessful include branch, popping the mask and continuing
  the loop is exactly the exclude branch.

The final replay checks seven nonempty connected bags, disjointness via
the equality between total bag size and union size, and all 21 interbag
adjacencies.  A representative for each complement isomorphism type is
sufficient because vertex connectivity and minor containment are
isomorphism-invariant.

I reran the verifier under the workspace venv and obtained

```text
GREEN [(8, 1, 1), (9, 5, 5), (10, 106, 87)]
certificate_sha256 00cc01e52c690006261a1979c4eeceb7ca2ceead6f9f7d7ff2f0bff02da47bbf
```

The trust boundary is the short generator/search program, NetworkX's
exact connectivity/connectedness routines, and the Python runtime.
