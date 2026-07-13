# Critical edges become side-labelled Kempe cycles after contraction

## 1. The operation-level lemma

### Theorem 1.1 (split-cycle fan)

Let (G) be (k)-contraction-critical, let (xy\in E(G)), and let
(p) be the image of (xy) in (L=G/xy).  For every proper
((k-1))-colouring (c) of (L), put
(alpha=c(p)).  For each other colour (eta), one of the following
holds.

1. (x) and (y) have a common (eta)-coloured neighbour in
   (G-xy); or
2. the (alpha,eta)-subgraph of (L) contains a cycle through
   (p), and its two edges at (p) lift to different sides of the
   split vertex: one is an (x)-edge and the other a (y)-edge.

In either case, each of (x,y) has a neighbour of colour (eta).
Thus every colouring of the contracted graph carries a five-member
side-labelled fan when (k=7).

#### Proof

Expand (p) back to the two nonadjacent vertices (x,y), giving both
the colour (alpha).  This is a ((k-1))-colouring of (G-xy).
For every (eta\nealpha), the vertices (x,y) lie in the same
(alpha,eta)-component.  Otherwise interchange (alpha,eta) on
the component containing (x); then (x,y) have different colours and
the edge (xy) can be restored, contrary to
(chi(G)=k).

Choose a simple (x)-(y) path (P_eta) in that bichromatic
component.  Its first and last edges prove the neighbourhood assertion.
If (P_eta=xwy), then (w) is the common neighbour in outcome 1.
Otherwise its two neighbours of (x,y) are distinct.  Identifying
(x,y) turns (P_eta) into a simple bichromatic cycle through (p),
and its two incident edges at (p) have the asserted different lifts.
\(\square\)

The side labels are essential.  An ordinary cycle through (p) may use
two edges which both came from (x), and then says nothing about the
critical split (p\rightsquigarrow xy).

## 2. The central Moser edge

Apply Theorem 1.1 to the edge (56) of a hypothetical minimal
(HC_7) counterexample.  The contraction (G/56) has chromatic number
exactly six: it is at most six by minor-criticality, while a five-colouring
would expand to a five-colouring of (G-56), after which one endpoint
could receive a fresh sixth colour, producing a six-colouring of (G).

Consequently every six-colouring of (G/56) supplies, for each of the
five colours other than (c(56)), either a common neighbour of (5,6)
or a bichromatic cycle through the contracted vertex using one
(5)-side and one (6)-side incidence.

This decorates both outcomes of Theorem 4.5 in
`hadwiger_four_connected_rooted_diamond.md`:

* in the full-seven-adhesion outcome, every split cycle either stays on
  one full shore or crosses the exact boundary in a side-labelled way;
* in the dirty-connector outcome, a cycle entering the first dirty rooted
  bag supplies an alternative return to the opposite side of (56).

The remaining exchange lemma must preserve these side labels.  Counting
unlabelled Kempe components, or merely recording their boundary equality
partition, loses precisely the information established above.
