# Independent audit of one-step minor dynamics

**Verdict:** **GREEN for the mathematical theorems and finite witnesses at
the exact revisions below.**  The result is promoted.

## Audited revisions

- Source: `results/hc7_star_core_one_step_minor_dynamics.md`
- Source SHA-256:
  `f1e976266afb7b4e2daeb9ee36c0da13518d59540ae6c5244fd82cd3cb37e3b8`
- Verifier: `results/hc7_star_core_one_step_minor_dynamics_verify.py`
- Verifier SHA-256:
  `a6830f490ad5aa2896b52d160ca2b52316c548c027396dc8ec8cb29fc743224f`

## 1. Elementary-minor chromatic response

Lemma 2.1 is correct for all three operations.  Each resulting graph is a
proper minor, hence is `(k-1)`-colourable.  If it were `(k-2)`-colourable,
then:

- after a vertex deletion, the deleted vertex can receive one new colour;
- after an edge deletion, a monochromatic restored edge can be repaired by
  recolouring one endpoint with one new colour; and
- after an edge contraction, one expanded endpoint keeps the quotient
  colour and the other receives one new colour.

In the contraction case, every neighbour of the endpoint retaining the old
colour was a neighbour of the quotient vertex.  The fresh colour occurs
nowhere else, and the restored edge has differently coloured ends.  Thus
each construction really gives a `(k-1)`-colouring of `G`, the required
contradiction.

## 2. Common-hole law and chromatic bounds

For a `p`-colouring of `Q_m`, distinct colours missing respectively from
`S_m` and `T_m` can be assigned to the independent bipartition classes
`A,B`.  All edges from `X` to `Q_m` are then proper by the definitions of
the two attachment sets, and all edges of `X` cross the bipartition.  This
would `p=k-2` colour `H`, contradicting Lemma 2.1.  Two nonempty subsets of
the palette with no distinct representatives must be the same singleton,
so the three alternatives in (3.1) are exhaustive.

The allowed operations do not remove an `X`--`Q_m` edge.  In the contraction
case a quotient vertex retains every incident attachment supplied by either
endpoint.  Hence `X` remains connected and dominating and contracting it
gives exactly `K_1 vee Q_m`.  This is a proper minor of `G`, proving
`chi(Q_m)<=p`.  A `(p-2)`-colouring would leave two palette colours absent
from both attachment sets and violate the common-hole law.  Therefore
`p-1<=chi(Q_m)<=p` exactly as claimed.

## 3. Intersection colourfulness

Theorem 4.1's recolouring is valid.  In a `(p-1)`-colouring, the one unused
colour and the common-hole law first force both attachment sets to meet
every active colour class.  If one active colour class misses
`U=S_m cap T_m`, its intersections with `S_m` and `T_m` are nonempty and
disjoint.  Recolouring the `S_m` intersection with the globally unused
colour remains proper because the whole original colour class is
independent.  It removes the old colour from `S_m` and leaves the new colour
absent from `T_m`, producing two distinct holes.  This proves every active
colour occurs on `U`.

The auxiliary-vertex reformulation is also exact: in the chromatic-drop
branch `Q_m` uses `p-1` colours, two adjacent auxiliary vertices need two
fresh colours, and their common-neighbour set is precisely `U`.

## 4. Strong Hadwiger dependency and lifting

Corollary 4.2 is conditional on exactly Holroyd's Strong Hadwiger statement
for `p-1` colours: a colourful set in a `(p-1)`-chromatic graph roots a
`K_{p-1}` minor.  For `HC_7`, `p-1=4`; Martinsson--Steiner, Theorem 1.3,
proves precisely that a colourful set in a four-chromatic graph roots a
`K_4` minor.  No five-colour or paired-root strengthening is being assumed.

The model lifts through every allowed operation.  Deleted edges or vertices
may simply be restored and left unused.  For a contracted edge, replace the
quotient vertex in its unique branch set by both original endpoints.  The
preimage is connected; if the quotient vertex supplied an `A`-contact and a
`B`-contact through different endpoints, both endpoints lie in that same
preimage.  Thus every lifted branch set retains both prescribed contacts.

## 5. Root-trace lifting tests

The preliminary assertion `chi(Q)=p` also uses the setup correctly.  Since
both bipartition classes are nonempty and `X` is connected, `|V(X)|>=2`;
contracting all of `X` in `G` therefore is a **proper** minor and gives
`K_1 vee Q`.  This excludes the singleton-apex counterexample that would
arise if one dropped the nonempty-two-class hypothesis.  Conversely a
`(p-1)`-colouring of `Q`, followed by two fresh colours on `A,B`, would
`(k-1)`-colour `G`.  Thus `chi(Q)=p`, and the subsequent saturation argument
is valid.

All three tests in Section 5 are exact.

- A colouring of an edge-deleted graph lifts exactly when the restored
  endpoints differ.
- A colouring after deleting a vertex extends exactly when some palette
  colour is absent from its old neighbourhood.
- After contracting `vw`, assigning colours to the two expanded endpoints
  is exactly a two-set system-of-distinct-representatives problem for
  `L_v,L_w`.  The quotient colour belongs to both lists.  Consequently an
  expansion fails exactly when both lists equal the singleton containing
  that quotient colour.

When the affected vertices are outside both attachment sets, their root
traces are unchanged.  Otherwise equation (5.1) is genuinely additional;
the source correctly does not infer trace preservation merely from a
proper lift.

## 6. Finite `HEhutxm` witnesses

The verifier was run under NetworkX 3.6.1 and returned:

```text
PASS HEhutxm full-root saturation
PASS vertex deletion, edge deletion and edge contraction witnesses
```

It exhausts all 6,840 labelled five-colourings of the eleven-vertex graph
and checks that both displayed root sets use all five colours.  It then
checks the three explicit colourings, their missing/full root patterns, and
the exact reason each fails to lift.  In the contraction example it also
recomputes both expansion lists from the original graph and obtains the
same singleton.  Direct inspection of the two overlapping pairs of `K_4`s
also proves the written five-chromaticity argument for the induced `T_0`
subgraph.

These are finite sharpness witnesses for **static root saturation**, not
examples satisfying the original minor-critical bipartite-compression
setup.

## 7. Repaired scope language

The audited revision says that each **type** of elementary operation admits
the displayed response, explicitly states that `HEhutxm` does not realize
the minor-minimal host and connected bipartite subgraph from the setup, and
calls the two chromatic outcomes an exact rather than a well-founded
dichotomy.  These statements now match the proofs and trust boundary.

## Trust boundary

The audited result does not split the independent sets `A,B` into connected
branch sets and therefore does not construct a `K_7` model.  In the
five-chromatic branch it proves only the common-hole alternatives.  No
recursive decrease follows from Lemma 2.1 beyond one operation from the
original minor-minimal graph.
