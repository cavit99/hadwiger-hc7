# Independent audit: leaf-rooted chromatic drop

**Verdict:** **GREEN after correction.**

The contraction-forest argument, all chromatic equalities, the literal-leaf
claim, the corrected rooted-model fork, and the uses of `HC_4`, `HC_5`, and
Martinsson--Steiner are valid.  The pre-audit draft contained two material
overstatements and one missing qualification:

1. a `K_5` model in `C/uv` need not use the contracted vertex, so its direct
   expansion need not contain the edge `uv`;
2. `|F_0|` is not yet a recursive rank on the active proof spine; and
3. `C` must be taken as an **induced** six-vertex-critical subgraph of `H`
   (or otherwise explicitly required to contain the edge `uv`).

All three points have been corrected in the theorem file.

## 1. Audit of Theorem 1.1

### The terminal contraction

Let `T_A,T_B` be spanning trees of the two connected shores.  Contracting
their edges really does produce `I_2 \vee G[S]`:

* each shore becomes one vertex;
* the two new vertices are nonadjacent because there is no `A-B` edge; and
* each is adjacent to every literal vertex of `S` by pointwise fullness.

Thus the quotient is five-colourable from a four-colouring of `G[S]`.  The
set `F=E(T_A)\cup E(T_B)` cannot be empty, since otherwise `G` itself would
be this five-colourable quotient, contrary to `chi(G)=7`.  Hence a nonempty
inclusion-minimal `F_0 \subseteq F` with `G/F_0` five-colourable exists.

### Minimality and exact chromatic numbers

`F_0` is a forest because it is a subset of the disjoint union of two
trees.  It has at least two edges: if `F_0={e}`, the assumed equality
`chi(G/e)=6` would contradict the five-colourability of `G/F_0`.

For every `e\in F_0`, inclusion-minimality says that
`G/(F_0-{e})` is not five-colourable, hence has chromatic number at least
six.  Since at least one edge is still contracted, this graph is a proper
minor of `G`, and the proper-minor hypothesis makes it six-colourable.
Its chromatic number is therefore exactly six.

The terminal quotient `G/F_0` is exactly five-chromatic, not merely at most
five.  If it had a four-colouring, splitting the image of the last edge and
giving one endpoint one fresh colour would five-colour the corresponding
six-chromatic predecessor.  This is a valid lift because the fresh colour
is used only once.

### Literal leaf preservation

Choose an edge `e=uv` incident with a leaf `u` of the forest `(V(G),F_0)`.
No edge of `F_0-{e}` is incident with `u`, so contracting all those other
edges leaves `u` as a literal singleton original vertex.  The other
endpoint becomes the image of its connected component in `F_0-{e}`.  The
entire component lies in the same original shore as `e`.  Edges of
`F-F_0` do not affect this conclusion because they are not contracted.

Finally, either endpoint can be assigned a fresh sixth colour when a
five-colouring of `H/uv` is lifted.  This proves both unique-colour claims.

## 2. Audit of Theorem 2.1

The theorem now takes `C` to be an induced six-vertex-critical subgraph of
`H`.  Such a subgraph exists because `chi(H)=6`; inducedness ensures that
once both endpoints lie in `C`, the edge `uv` also lies in `C`.

The five-colouring of `H/uv` restricts to five-colourings of both `H-u`
and `H-v`.  Hence a six-chromatic subgraph `C` cannot omit either endpoint.
The displayed chromatic equalities then follow:

* `C/uv` is at most five-colourable as a subgraph of `H/uv`; if it were
  four-colourable, splitting `uv` with one fresh colour would five-colour
  `C`;
* vertex-criticality gives `chi(C-u),chi(C-v)\le5`, while
  `chi(C)\le chi(C-u)+1` and its symmetric form give the reverse lower
  bounds; and
* `C-{u,v}` is at most five-colourable, while a three-colouring together
  with two distinct fresh colours on the adjacent vertices `u,v` would
  five-colour `C`.

The three exactly five-chromatic graphs consequently contain `K_5` minors
by `HC_5`, and `C-{u,v}` contains a `K_4` minor by the contrapositive of
`HC_4`.

The original draft incorrectly claimed that an arbitrary quotient model
must expand to a branch bag containing `uv`.  A quotient model may omit the
contracted vertex.  The corrected statement records the exact alternative:
if the contracted vertex is used, its bag expands to contain the connected
edge `uv`; if it is omitted, the model avoids both endpoints.

## 3. Audit of Corollary 2.2

The two chromatic branches in Corollary 2.2 are exhaustive because
`chi(C-{u,v})` is either four or five.

In the five-chromatic branch, `HC_5` directly gives a `K_5` model avoiding
both endpoints.

In the four-chromatic branch, any five-vertex-critical induced subgraph of
`C-u` must contain `v`, because `(C-u)-v` is four-colourable.  The
Martinsson--Steiner theorem therefore applies with prescribed vertex `v`
and yields a `K_5` model with singleton bag `{v}`.  The symmetric argument
gives singleton bag `{u}` in `C-v`.  Likewise, every five-critical induced
subgraph of `C/uv` contains the contracted vertex, since deleting it leaves
`C-{u,v}`.  Prescribing that vertex as a singleton and expanding it gives
a branch bag equal to the edge `{u,v}`.

This is exactly Corollary 1.4 of Martinsson--Steiner, *Strengthening
Hadwiger's conjecture for 4- and 5-chromatic graphs*, JCTB 164 (2024): in a
five-vertex-critical graph any prescribed vertex can be a singleton branch
set of a `K_5` minor.

## 4. Audit of Theorem 2.3 and Corollary 2.4

The uniform common-neighbour theorem is GREEN.

Put `R=J-{u,v}`.  The upper bound `chi(R)<=k` is assumed.  If
`chi(R)<=k-1`, colouring `u,v` with two distinct fresh colours would use at
most `k+1` colours on `J`, contradicting `chi(J)=k+2`; hence `chi(R)=k`.

Now fix any `k`-colouring of `R` and a colour `i` omitted by the common
neighbour set `X`.  The colour-`i` neighbours of `u` form an independent
set.  Recolouring all of them with one fresh colour remains proper.  None
is adjacent to `v`, since any such vertex would be a common neighbour of
colour `i`.  Thus assigning colour `i` to `u` and the fresh colour to `v`
is a proper `(k+1)`-colouring of `J`, the required contradiction.  This
checks the only delicate recolouring step and proves that `X` is colourful
in `R`.

An `X`-rooted `K_k` model has every bag meeting `X`, hence every bag is
adjacent to both singleton vertices `u,v`; the edge `uv` supplies their
mutual adjacency.  Adding those two singleton bags therefore gives a
literal `K_{k+2}` model.  Applying this with `J=C,k=4` is legitimate in the
four-chromatic branch and yields Corollary 2.4: a `K_6` model with
singleton bags `{u},{v}`.

The subsequent separate-neighbour-set comparison is also correct but
strictly weaker.  If a four-colouring of `R=C-{u,v}` omits a colour on
`N_C(u)\cap R`, assigning that colour to `u` and one fresh fifth colour to
`v` five-colours `C`; hence this neighbour set is colourful.  The symmetric
claim and its conditional bi-rooted composition follow as written.

## 5. Rank assessment

The pre-audit claim that `|F_0|` is already a strict well-founded global
rank was **RED**.  Although it is a positive integer attached to the local
witness, contracting its selected leaf takes the six-chromatic predecessor
to the five-chromatic graph `G/F_0`; it does not return a seven-chromatic
two-shore instance.  Nor is there presently a theorem showing that a
nonterminal model-composition outcome has a new compatible minimal forest
of smaller size.

Accordingly, `|F_0|` is a finite **local witness size** and a possible
future rank component, not a proved recursive descent parameter.  The
corrected result makes exactly this limited claim.

## 6. Final trust boundary

The audited result supplies a literal drop edge, exact chromatic levels,
endpoint-avoiding `K_5` models, the rooted fork, and in its four-chromatic
branch a label-faithful `K_6` model with singleton bags `{u},{v}`.  It does
not preserve the additional carrier needed to extend that model to `K_7`
or establish a recursive transition.  Subject to that boundary, the
corrected theorem is GREEN.
