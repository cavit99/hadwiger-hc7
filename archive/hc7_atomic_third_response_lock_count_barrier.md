# Barrier: five third-response locks are not an allocation invariant

**Status:** proved dependency barrier, with a separately verified sharp
rural host.  This does not falsify the full twin-seam terminal disjunction:
the rural host has the permitted fixed-pair outcome.  It identifies exactly
which part of a future third-response theorem must carry new information.

## 1. Lock count is already dominated by seven-connectivity

### Lemma 1.1

If `G` is seven-connected and `xy` is an edge, then `G-xy` contains six
pairwise internally vertex-disjoint `x-y` paths.

### Proof

Suppose `X subseteq V(G)-{x,y}`, with `|X|<=5`, separates `x` from `y` in
`G-xy`.  Let `C_x,C_y` be the corresponding sides.  If `C_x-{x}` is
nonempty, then `X union {x}` is a vertex cut of `G` of order at most six,
separating `C_x-{x}` from `y`.  If `C_x={x}`, then every neighbour of `x`
other than `y` lies in `X`, contrary to `d_G(x)>=7`.  The same applies at
the `y` side.  Thus no such `X` exists.  The vertex form of Menger's
theorem in `G-xy` gives six internally disjoint `x-y` paths. `square`

An internal-edge contraction response gives five bichromatic endpoint
locks, one for each alternate colour.  Lemma 1.1 shows that the *existence
and number* of those paths add no uncoloured linkage strength to the frozen
kernel.  Their only potentially new information is:

1. their exact two-colour traces on the twin boundaries;
2. how those traces change between different named internal-edge
   responses; or
3. localization of a trace to one labelled lobe, carrier, or regenerated
   model row.

Counting the locks, endpoint saturation, or replacing them by arbitrary
unlabelled paths cannot prove an allocation theorem.

## 2. The rural endpoint is sharp even with palette and model data

The independently executable certificate
[`../barriers/hc7_near_k7_palette_rural_counterarchitecture_verify.py`](../barriers/hc7_near_k7_palette_rural_counterarchitecture_verify.py)
verifies the graph in
[`../barriers/hc7_near_k7_palette_rural_counterarchitecture.md`](../barriers/hc7_near_k7_palette_rural_counterarchitecture.md).
It has all of the following simultaneously:

* exact seven-connectivity and no `K_7` minor;
* one deleted edge whose equal-coloured endpoints are joined in every one
  of the five alternate bichromatic layers;
* endpoint saturation in every alternate colour;
* a fixed `K_5` model containing a distinct-colour transversal;
* a literal exact-seven lobe with two poles, a repeated owner portal and
  one missed model row; and
* no labelled row split producing `K_7`.

The graph is `K_2` joined to a planar five-connected triangulation.  Its
two join vertices form a fixed pair whose deletion is planar.  Thus it
realizes the fixed-pair branch of the active theorem, rather than refuting
it.

This certificate is stronger than a palette-only shell: even a palette
SDR inside a fixed five-row frame and repeated literal portal ownership do
not align a Kempe lock with a model duty.  The fixed-pair alternative is
logically indispensable.

## 3. Consequence for the third-response grid

The audited third-response grid supplies three facts:

1. opposite intact-side orientations and exact-state rejection;
2. five endpoint locks for every internal lobe edge; and
3. a state-preserving endpoint-saturation fork after a paired contraction.

Items 2--3 cannot by themselves yield an adaptive carrier, labelled row
split, `K_7`, or ranked receiver.  A valid next theorem must spend item 1
in one of two literal ways:

* **exclusive trace:** some named lock has a trace containing an exclusive
  `A_0`- or `B_0`-duty and can be localized to a disjoint carrier/model
  row; or
* **dynamic rural coherence:** if every named response remains confined to
  the common five-set or to one web order, the response transitions prove
  that the same two vertices meet every `K_5` model, giving the permitted
  fixed-pair terminal.

Merely choosing a sixth path, another saturated response, or a different
unrooted `K_6` model repeats information already present in the two examples
above.

## 4. Falsification outcome for the exact twin seam

No counterexample to the full terminal-disjunctive twin-seam theorem was
found.  In particular, the cyclic two-lobe/two-gate probe
[`hc7_atomic_twin_seam_web_counterprobe.py`](hc7_atomic_twin_seam_web_counterprobe.py)
tested relative-seven-cut contact maps for lobe orders four, five and six;
every sampled map already had an adaptive carrier return before any lock
was invoked.  A second run sampled biconnected twin topologies rather than
one cyclic topology.  It found no irreducible map among respectively
`44,112`, `32,235`, and `13,111` relative-cut survivors of total thin
orders seven, eight, and nine.  The existing exact small-shell probes give
the same outcome on their declared finite families.

These computations are guardrails, not proof.  Their useful diagnosis is
that a meaningful falsifier must start with a genuinely static-return-
irreducible web.  Adding lock variables to a shell already closed by a
carrier cannot test the third-response implication.

The full disjunction therefore remains open.  What is decisively falsified
is the proposed *mechanism* in which five locks or endpoint saturation are
treated as labelled allocation evidence without an exclusive trace or a
proof of coherent rurality.
