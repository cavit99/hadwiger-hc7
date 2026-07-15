# Audit of stateful pullback at global support six

## Verdict

**AMBER overall.**  Lemmas 2.1 and 3.1 and Theorem 4.1 are **GREEN**.
Corollary 4.2 is **GREEN only as the existence of a finite global rank on
all actual oriented `(1,2)` separations**; it does not provide a recursive
transition preserving the selected pair or model.  Sections 5--6 are
**AMBER/RED as an exact description of the remaining seven-connected
branch**, because they retain but then omit the independent equal-support
case `mu_H(R)=6`.

The theorem should remain in `active/`.  It may be promoted after the
maximization domain and final strategic consequence are corrected.  No
counterexample was found to any of the elementary lemmas.

## 1. Setup and notation

### Maximization domain -- AMBER wording, GREEN intended statement

After extending `mu_J(R)` to arbitrary deletion sets, the sentence “let
`P` maximize `mu_G(P)`” must say explicitly that the maximum is over
**two-vertex sets**.  Maximization over arbitrary vertex sets would be
meaningless here: deleting all vertices gives value infinity.

With that clarification, the setup is sound.  The assumption that the
maximum equals six implies that `P` meets every literal `K_5`, because a
literal `K_5` is exactly a support-five `K_5` model.  Hence the audited
support-six dichotomy applies and gives four singleton bags `Q` and one
edge-bag `xy`.

The definition of `mu_J(R)` for arbitrary `R` is otherwise coherent.  All
substantive applications in the note use a two-set, as stated.

## 2. Lemma 2.1: exact contraction pullback -- GREEN

Let a support-at-most-`s` `K_5` model in `G-R` be given, with `z notin R`.
There are exactly three nonsplit possibilities:

1. it avoids both `x,y`;
2. it uses exactly one of them; or
3. it uses both in the same branch set.

Contracting `xy` preserves five disjoint connected branch sets in the
first two cases and contracts inside one branch set in the third.  Support
does not increase (and falls by one in case 3).  Thus `mu_H(R)>s` excludes
all three.  The only remaining possibility places `x,y` in distinct rows.

For `R={z,r}`, a model in `G-{x,r}` which also avoids `y` is literally a
model in `G-{x,y,r}=H-{z,r}`; the symmetric assertion is identical.  This
proves both forced-pole statements.  No adjacency or label preservation
beyond that stated in the lemma is inferred.

## 3. Lemma 3.1: terminal-pair chromatic lock -- GREEN

The phrase “with no support bound” can be formalized as follows.  If one
of the asserted deleted graphs contained a finite model of support `k`,
apply Lemma 2.1 with `s=max{5,k}` and
`mu_H(R)=infinity`.  This proves the minor-free assertions.

Known `HC_5` four-colours `H-R`.  In the case `R={r,s}` with `z notin R`,
give `r,s` two distinct fresh colours and initially give both split
endpoints the old colour of `z`.

* If, for example, `xr` is absent, recolour `x` with the fresh colour used
  only on `r`; this resolves `xy` and is proper.  The same argument gives
  all four edges from `{x,y}` to `{r,s}`.
* If `r` misses an old colour class, recolour `r` with that colour, give
  one split endpoint the now unused fresh colour of `r`, and leave the
  other in the old colour of `z`.  This is again a proper six-colouring.
  The argument for `s` is symmetric.

When `R={z,r}`, the deleted graph is `G-{x,y,r}`.  Two fresh colours on
`z,r` give the same adjacency argument; after recolouring `r` into a
missing old class, the two now unused fresh colours may be assigned to
`x,y`.  Every recolouring is literal and uses at most six colours.  Thus
the adjacency and saturation conclusions are correct, including for a
nominal four-colouring with an empty colour class.

## 4. Theorem 4.1: lifted exact-seven handoff -- GREEN

The audited contraction dichotomy supplies a separator `T` of `H` of
order six containing `z`.  With

```
S=(T-{z}) union {x,y},
```

deleting `T` from `H` and deleting `S` from `G` have exactly the same
components.

For each such component `C`, its neighbourhood lies in the seven-set `S`.
There is another component, so `N(C)` separates `C` from a nonempty part of
the graph.  Seven-connectivity forces `|N(C)|>=7`, hence `N(C)=S`; every
component is therefore an `S`-full packet.

The set `Q union {z}` is a clique in `H`.  Two vertices of `Q-T` cannot
occupy different components of `H-T`, because their clique edge would join
those components.  Thus all of `Q-T` lies in at most one component `C_Q`.
Vertices of `Q cap T`, together with `x,y`, lie in `S`, so the whole
support `W` lies in `S union C_Q` (or in `S` when `Q subseteq T`).

If there are at least three components, for any chosen component `C` the
opposite shore contains two disjoint full component-packets.  The exact
seven packet theorem forces the chosen shore to have packet number one and
the opposite shore to have packet number two or three.  The audited
adaptive reflection theorem eliminates three, leaving `(1,2)`.  Choosing
`C ne C_Q` preserves `W` in the opposite closed shore.

If there are exactly two components, each supplies one packet.  The same
packet theorem and `(1,3)` elimination leave `(1,1)` or `(1,2)`, and the
clique argument still locates `W` in one closed shore.  All four numbered
claims are therefore proved.

## 5. Corollary 4.2: what the rank does and does not do

### Existence of a rank -- GREEN

Once any actual `(1,2)` separation exists, the finite graph has a minimum
open packet-one shore among all oriented actual `(1,2)` separations.  If a
proof begins with such a globally minimum separation, a valid `(1,2)`
receiver with strictly smaller open packet-one shore is impossible.  The
word “shore” should be clarified as **open shore**, although including the
fixed seven-vertex boundary would give the same ordering.

### Recursive/model-preserving transition -- NOT PROVED

The component handoff gives one `(1,2)` cell which preserves `W` in a named
closed shore.  Reselecting a globally minimum `(1,2)` cell need not preserve
`W`, `P`, the split edge, or any equality state.  Conversely, an arbitrary
model-preserving receiver has not been proved to remain inside a subclass
on which the same minimum was selected.  The corollary correctly admits
this, so it is logically sound, but it is not yet the well-founded global
transition sought by the programme.

The phrase “model-preserving `(1,2)` global-rank initialization” in Section
6 should therefore be split into two facts: the theorem produces a
model-preserving cell, and it proves that the globally ranked class is
nonempty.  Those properties need not coexist after global reselection.

## 6. Section 5: seven-connected contraction

The application of the literal-`K_5` transversal theorem to seven-connected
`H` is **GREEN**.  It returns a two-set `R` with `mu_H(R)>=6`, and `R` meets
the literal clique `Q union {z}`.

The three numerical cases are as follows.

1. If `z notin R` and `mu_H(R)>=7`, every support-at-most-six model in
   `G-R` is split-row.  Global maximality at six ensures such models exist.
2. If `R={z,r}` and `mu_H(R)>=7`, every support-at-most-six model for
   `{x,r}` contains `y`, and symmetrically every such model for `{y,r}`
   contains `x`.  Global maximality again makes the statement nonvacuous.
3. If `mu_H(R)=6`, Lemma 2.1 supplies no row or pole constraint.  A neutral
   nonsplit support-six response is compatible with every proved result.

Items 1--3 are **GREEN**.  The “either” formulation in the second bullet is
unnecessarily weak, since the forced-pole universal statement follows
whenever `mu_H(R)>=7`; global maximality merely guarantees responses.

## 7. Claimed exact remaining obstruction -- RED until corrected

Sections 5--6 describe split-row/forced-pole response coupling as the
single remaining seven-contractible obstruction.  This omits case 3 above:
the global transversal theorem guarantees only `mu_H(R)>=6`, and when
equality holds there is no named-row conclusion at all.  No argument in the
note upgrades equality to seven or couples an equal-support model in `H-R`
to the original edge-bag model.

Accordingly the actual seven-connected residue has **two branches**:

1. the equal-support branch `mu_H(R)=6`, requiring a new stateful neutral
   exchange or a terminal outcome; and
2. the strict branch `mu_H(R)>=7`, requiring split-row/forced-pole response
   coupling.

The top status line and Section 6 should name both.  After that correction,
the note is a sound global normalization theorem, but still not a strict
global invariant or a closure of support six.
