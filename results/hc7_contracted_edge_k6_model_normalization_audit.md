# Internal audit of the minimal contraction-bag normalization

**Verdict:** GREEN, subject to the explicit limitations in Section 6 of the
source.

**Audited source:** `hc7_contracted_edge_k6_model_normalization.md`,
SHA-256

```text
61fa3c094c34d06590efcef8a6903356f36bc8aadcdec75f834aa7e5cfd82936
```

This is a separate internal mathematical audit, not external peer review.

## 1. Contracted graph

The proof that `chi(G/e)=6` is correct.  Proper-minor minimality gives the
upper bound; a five-colouring would lift by retaining one endpoint colour
and giving the other endpoint a fresh sixth colour, six-colouring `G`.

The separator lift proving six-connectivity is also correct.  A separator
which avoids the contraction image lifts unchanged.  If it contains that
image, replacing it by both edge endpoints increases its order by one, so a
cut of order at most five would contradict seven-connectivity of `G`.

Known `HC_6` supplies a `K_6` model.  Connectedness permits a path from the
contraction image to that model to be absorbed into one branch set.  The
term `x`-rooted is used only in the sense `x in D`, not as a singleton-root
claim.  The extremal choice ranges over all such models, not only spanning
models.

## 2. Extremal root branch set

For a detachable `Z`, the zero-label case simply deletes `Z` from `D`.  In
the one-label case, all old contact with the exceptional `B_j` lies in `Z`,
so `B_j union Z` is connected; an edge across the connected `D` cut keeps
it adjacent to `D-Z`.  All other model adjacencies survive.  Both operations
contradict minimum `|D|`, proving that every detachable piece monopolizes at
least two labels.

Every component of `H[D-x]` is detachable: connectedness of `D` makes it
adjacent to `x`, while `x` joins all the other components in its complement.
Two different components cannot monopolize the same nonempty `D`--`B_i`
contact.  Their label sets are disjoint and have order at least two, so at
most two components occur.

## 3. Uncovered components and lifting

If a component outside the model union met a `B_i`, absorbing it into that
branch set would increase the covered union without changing `D`.  Hence its
neighbourhood lies in `D` and has order at least six.  Equality without `x`
would lift to a six-cut of `G`; equality with `x` lifts to the displayed
seven-set.  Seven-connectivity forces that seven-set to be the full
neighbourhood, and the usual one-missed-boundary-vertex argument makes every
complementary component full.

The preimage of `D` is connected.  A spanning tree of that branch set can
be chosen to contain `pv`; deleting the tree edge gives the two connected
sides.  If both retain all five contacts, the seven displayed branch sets
are an explicit `K_7` model.  Otherwise the full neighbourhood of a
deficient side is a genuine separator, but the theorem supplies no upper
bound on its order.

Finally, a connected subgraph wholly outside the model union lies in one
uncovered component and is anticomplete to every `B_i`.  This does not rule
out a repair which combines such a component with vertices reassigned from
`D`, nor does it align palette colours with branch-set labels.

## 4. Exact trust boundary

The theorem is an unbounded, well-founded normalization.  It does not prove
a singleton contraction bag, a clean split, an exact separator in every
deficient case, a compatible boundary partition, or `HC_7`.
