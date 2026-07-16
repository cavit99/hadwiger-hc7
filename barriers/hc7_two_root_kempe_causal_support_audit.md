# Independent audit: two-root Kempe causal-support draft

**Audited source:** `hc7_two_root_kempe_causal_support.md`

**SHA-256:** `d18bb332eb8e253201ac602ca9d63e49a5fbc02be4fde66a8ab8b284e5ec547a`

**Verdict:** **GREEN**
**Audit type:** line-by-line proof audit plus an independent exhaustive check of
the stated `q=6` example.

The exact barrier revision was rechecked on 2026-07-16 after its status
header and adjacent-audit link were updated.  The mathematical content is
the content audited below.

## Scope of the verdict

The source correctly proves the exact one-step contact formulas, the
shortest-path and strongly commuting-square statements, and the uniform
family in Proposition 4.1.  The family is a valid counterexample to a
causal-support conclusion based only on universal two-root colour
domination.

This verdict does **not** promote an `HC_7` conclusion.  The example at
`q=6` is four-connected, not five-connected, and is not asserted to be the
two-root deletion of a seven-connected, strongly
seven-contraction-critical, `K_7`-minor-free graph.

## 1. Shortest-path normal form

Lemma 1.1 is correct with the quantifiers stated.  The path is chosen
shortest among all paths in one Kempe component with an `A` endpoint and a
`B` endpoint.  Therefore:

- an internal `A` vertex gives a shorter suffix ending at the chosen `B`;
- an internal `B` vertex gives a shorter prefix beginning at the chosen
  `A`; and
- condition (U) excludes the only remaining fourth possibility, in which
  neither root is colour-dominating.

Thus every internal vertex has status `AB`.  The source also correctly
keeps separate the case in which the two exclusive witnesses lie in
different Kempe components.

## 2. Exact one-step formulas

Let an `alpha-beta` component `K` be interchanged.  Directly tracking a
root's contacts before and after the interchange gives:

- before: `alpha` is seen in
  `I_r^alpha union O_r^alpha`, and `beta` in
  `I_r^beta union O_r^beta`;
- after: `alpha` is seen in
  `O_r^alpha union I_r^beta`, and `beta` in
  `O_r^beta union I_r^alpha`.

These identities verify (2.3).  They also verify the sharper gain and loss
statements:

- if `gamma` is gained, all old `gamma` contacts are absent, an old
  `bar(gamma)` contact in `K` creates `gamma`, and one outside `K` retains
  `bar(gamma)`, giving exactly (2.1);
- if `lambda` is lost, every old `lambda` contact lies in `K` and no old
  `bar(lambda)` contact lies in `K`; old domination then supplies the two
  asserted nonempty sets, giving exactly (2.2).

Untouched colours cannot be gained or lost, so the uniqueness assertions
are valid.  Consequently the translations `A -> AB` and `AB -> B` at the
end of Section 2 are also correct.

## 3. Strong commutation

The definition used in the source is sufficiently strong: the second move
retains the same colour pair and the same component vertex set after the
first move, and both orders produce the same fourth colouring.  Hence the
fourth corner really is adjacent to both endpoints of the two-edge segment.

For a shortest segment

```text
c_(i-1) -- c_i -- c_(i+1),
```

an `A` fourth corner has an `A`-to-`B` suffix of length strictly less than
`m`, while a `B` fourth corner has an `A`-to-`B` prefix of length strictly
less than `m`.  Condition (U) again excludes the neither-dominating status.
Proposition 3.1 follows.

The cube paragraph is also correct under its explicit hypotheses.  A
proper noninitial `A` corner has a cube route to the terminal `B` corner of
length less than `m`; a proper nonterminal `B` corner has a route from the
initial `A` corner of length less than `m`.  It is a conditional observation,
not a claim that every path canonically extends to a full cube.  The later
two-outcome discussion should likewise be read as identifying two mechanisms
that a future theorem must accommodate, not as an already proved exhaustive
dichotomy for arbitrary Kempe paths.

## 4. Uniform construction

For `J_q=K_(q-2) join 4K_2`, every proper `q`-colouring has the following
forced form:

1. the clique uses `q-2` distinct colours;
2. every one of the four disjoint edges uses both remaining colours; and
3. a colouring is therefore encoded by four edge orientations.

With the root neighbourhoods in (4.1), the first root fails exactly on the
two constant orientation vectors.  The second root fails exactly on the
two vectors of the form `delta,delta,bar(delta),bar(delta)`.  The two events
are disjoint, proving (U), and these are precisely the `B` and `A` vectors,
respectively.

An interchange of the two nonclique colours flips one edge orientation.
An interchange of two clique colours only permutes clique colours.  If a
clique colour is interchanged with a nonclique colour, its bichromatic
subgraph is one star consisting of the clique vertex and one endpoint of
each of the four disjoint edges.  The move renames one nonclique colour but
preserves all four relative orientations and hence both root statuses.
This exhausts the possible colour pairs.  It proves that no Kempe edge is
an `A`-to-`B` edge.

The `A` and `B` orientation sets have Hamming distance two.  Flipping the
third and fourth edges from the displayed `A` vector gives a strongly
commuting square with statuses

```text
A  AB
AB B.
```

This proves all four items of Proposition 4.1, including the cases `q=2`
and `q=3`, where the statements involving unavailable clique-colour pairs
are simply vacuous.

## 5. Independent `q=6` computation

I independently generated all proper six-colourings of `J_6` and all
single-component Kempe neighbours.  No graph-specific shortcut from the
written proof was used in the status-distance calculation.

The enumeration returned:

```text
proper six-colourings:       5760
status A:                     720
status AB:                   4320
status B:                     720
neither-dominating status:      0
Kempe edges joining A to B:      0
minimum A--B distance:            2
explicit square statuses:   A, AB, AB, B
```

An exhaustive vertex-cut check found no cut of order at most three and one
cut of order four, namely deletion of the `K_4` join part.  Thus
`kappa(J_6)=4`.  Also, a join-part `K_4` together with any one of the four
edges induces a `K_6`, while the generated six-colourings give the reverse
bound, so `chi(J_6)=6`.

These checks agree exactly with the final paragraph of Proposition 4.1.

## Residual cautions

There is no mathematical defect requiring a source change.  Two scope
boundaries should remain explicit when this result is cited:

1. universal two-root domination alone does not control the connectivity
   or branch-set labels of the supports of successive Kempe moves; and
2. the construction does not falsify a strengthened theorem that uses the
   full minimal-`HC_7` hypotheses.
