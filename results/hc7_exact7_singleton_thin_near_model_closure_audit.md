# Audit: singleton-thin Moser packet paths force a labelled near model

**Verdict:** GREEN.  The mathematical source was independently audited at
SHA-256
`d7d995f90386ca43a9816a50c6926ccc0de003a1ce2834dba8cf125708b2182f`.
The promoted source has SHA-256
`37557494c96da87127efdd19f8e4f3bf1344b96c982dd58d4bf3527e7634500c`;
the only intervening edits mark the status as audited and add a
cross-reference to the superseded avoiding-path branch.  The theorem and
proof are unchanged.

The exact-trace/Kempe argument and both displayed branch-set models are
correct.  The proof uses neither a `P_1-P_2` edge nor the added edge `13`;
it therefore applies uniformly to the pure Moser spindle and `M+13`.
The final reduction to those two boundary types is sound only inside the
frozen adaptive `(1,2)` residual, exactly as the draft states.

## 1. Exact trace and all six boundary colours

The set `q union {2,5}` is connected because `q2,q5` are literal edges,
while `25` is a nonedge in both `M` and `M+13`.  Contracting that star is a
proper minor.  After six-colouring it, remove the contracted image and
give `2,5` its colour in `G-q`.

This expansion is proper: every retained neighbour of either `2` or `5`
was adjacent to the contracted image.  It is also exact on the boundary.
The image of the star was adjacent through `q` to every literal of
`S-{2,5}`, so none of those five vertices has the colour of `2,5`.

All six palette colours must occur on `S`.  If at most five occurred,
some palette colour would be absent from `S`; assigning it to `q` would be
proper because `N(q)=S` and `q` is anticomplete to `R`.  This would
six-colour `G`, contrary to the setup.  Since `25` is one exact block, the
five vertices `0,1,3,4,6` therefore have five pairwise distinct colours,
all distinct from the colour on `25`.

In particular `4` and `6` are singleton boundary colour blocks.  If they
belonged to different components of the subgraph induced by their two
colours, switching the component containing `4` would give `4,6` the same
boundary colour.  No other boundary vertex changes, because no other
boundary vertex has either colour.  One of the six colours would then be
absent from `S` and could again colour `q`, a contradiction.

Thus `4,6` lie in one bichromatic component.  A simple path `W` between
them contains no other boundary vertex internally, since `4,6` are the
only boundary vertices of those two colours.  The colouring is on `G-q`,
so `q` is also absent.  From the partition

\[
 V(G-q)=S\mathbin{\dot\cup}R
\]

all internal vertices of `W` consequently lie in `R`.  This verifies
Lemma 2.1 without using the unique safe-state computation for `M+13`.

## 2. Packet-avoiding path: literal `K_7`

Let `X` be the interior of `W` and assume it avoids `P_1 union P_2`.  The
seven bags

\[
 \{1\},\ \{2\},\ \{6\},\ \{3,q\},\
 \{5\}\cup P_1,\ P_2,\ \{0,4\}\cup X
\]

are pairwise disjoint.  They are connected: `q3` joins the fourth bag,
fullness at `5` joins the fifth, and `04` together with the initial part
of `W` joins the last.  The final edge of `W` joins the last bag to `{6}`.

A complete pair check is as follows.

* `{1},{2},{6}` form the literal triangle `126`.
* `{3,q}` meets every bag with a boundary anchor through `q`, and it meets
  the unanchored packet `P_2` because `P_2` contacts boundary literal `3`.
* Each packet meets every boundary-anchored bag by `S`-fullness.
* The two packet bags are adjacent because `P_2` contacts the literal `5`
  inside `P_1 union {5}`.  No `P_1-P_2` edge is used.
* The last bag meets `{1},{2}` through `01,02`, meets `{3,q}` through
  `q0` (also common Moser edges are available), and meets each packet by
  fullness at `0` or `4`.

These account for all twenty-one pairs, so Lemma 3.1 is a literal `K_7`
model.  Every boundary edge needed here belongs to the common Moser edge
set; `13` is unused.

## 3. First packet hit: literal `K_7^-`

Suppose the interior of `W` meets the packet union.  On orienting from `4`
to `6`, let `w` be the first such vertex, let `P_h` contain `w`, and let
`P_o` be the other packet.  Vertex-disjointness of `P_1,P_2` makes `P_h`
unique.  The vertices `Z` strictly between `4` and `w` avoid both packets,
so the seven bags

\[
 A=\{0,4\}\cup Z,
 \quad B=P_h\cup\{5\},
 \quad C=\{6\},
 \quad D=P_o,
 \quad E=\{3,q\},
 \quad F=\{1\},
 \quad G=\{2\}
\]

are disjoint.  Bag `A` is connected by `04` and the truncated path (also
when `Z` is empty), `B` is connected by fullness at `5`, and `E` by `q3`.
The last truncated path edge gives `A-B`.

The six bags `B,C,D,E,F,G` form a literal `K_6`:

* each packet bag meets `C,E,F,G` at their literal anchors;
* `B-D` is witnessed by the contact of `P_o` with literal `5` in `B`;
* `E` meets `C,F,G` through `q6,q1,q2`; and
* `C,F,G` form triangle `612`.

Again no edge between the two packets is assumed.  Bag `A` meets `B` by
the truncated path, `D` by fullness at `0`, `E` through `q0`, and `F,G`
through `01,02`.  Its only possibly absent rim edge is `A-C`.  Hence the
seven bags contain `K_7^-`; by omitting one further `A`-spoke (after first
regarding `A-C` as the omitted target edge if it happens to exist), they
contain the normalized `K_7^vee` with both possible missing edges incident
with `A`.

This validates Lemma 4.1 in both the nonempty-`Z` and direct `4-w` cases.

## 4. Exhaustion and residual reduction

Every returned path either avoids `P_1 union P_2` or has a first internal
hit, so Lemmas 3.1 and 4.1 exhaust all possibilities and prove Theorem 5.1.
No simultaneity with a second Kempe path and no packet rerouting is needed.

The last paragraph correctly invokes an external frozen input rather than
claiming a new classification.  In a singleton thin shore, `d(q)=7`, so
Dirac's critical-neighbourhood inequality gives
`alpha(G[S])<=2`.  The independently audited extraction from the frozen
129-boundary adaptive `(1,2)` residual identifies exactly two such orbits:
the displayed Moser spindle and `M+13`.  Therefore Theorem 5.1 applies to
the entire singleton-thin part of that residual.  The conclusion is an
`S1` near-model handoff, not a contradiction from `K_7`-minor-freeness
alone.

The `M/M+13` assertion would be false if detached from membership in the
frozen 129-boundary residual; the draft does not detach it.

## 5. Relation to existing results

Sections 2 and 3 overlap the already audited
`hc7_exact7_singleton_thin_moser_extension_escape` result for `M+13`.
The new note makes two genuine advances:

1. it observes that the trace and avoiding-path proof uses only edges
   common to `M` and `M+13`; and
2. Lemma 4.1 closes the prior packet-entanglement residue by truncating at
   the first packet hit and outputting `K_7^-`.

No existing result located in the repository contains this packet-hit
truncation certificate.  Thus the note is not merely a duplicate, although
its old `M+13` avoiding branch should be cross-referenced when promoted.
