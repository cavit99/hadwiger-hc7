# Audit of the global adjacent-pair `K_5` contact rank

## Verdict

**GREEN**, with one corrected checker citation.

Lemma 2.1 is literal and lossless.  The two path-end segments have no
model vertices internally and are disjoint unless they enter the same row,
where their union with that row is connected.  Absorption preserves every
old row adjacency.  If the path avoids the model, all its internal vertices
lie in one exterior component; adjoining that component to any attachment
row gives both pole contacts.

Deleting one edge from a seven-connected graph leaves a six-connected
graph, so Menger gives the six channels in Corollary 3.1.  Internal
disjointness makes their first hits distinct and the pigeonhole count is
correct.

The order-at-most-eleven census was rerun with
`hc7_avoided_pair_falsifier.py`: the counts `1,5,87,9940` are correct and
every seven-connected host found has a `K_7` model.  The note correctly
stops at a first-hit lock; it does not claim a ranked equality transition.
