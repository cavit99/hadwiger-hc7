# Independent audit: surplus row cores and canonical gates

## Verdict

**GREEN after replacing the unsafe cardinal-minimal-core claim by the
rootwise avoidable/unavoidable definition.**  The theorem gives an exact
transfer-or-adhesion conclusion for every core-avoidable surplus root and
a literal multi-owner detachable gate for every core-unavoidable root.

## Checks

1. If `K` is a component of `U-T`, then every other component of `U-T`
   attaches to connected `T`; hence `U-K` is connected.  Since `T` meets
   every literal row portal set, deleting `K` loses no row adjacency, so
   `Omega_U(K)=empty`.
2. A target edge from `K` is therefore sufficient for wholesale transfer:
   the cut edge restores donor--target adjacency and the retained core
   preserves all other donor contacts.
3. If such a component misses either twin, that connected twin bag lies
   wholly beyond `N(K)`, providing a nonempty far side.  Thus its open
   neighbourhood is an actual separator, not merely a list of model
   labels.  Seven-connectivity gives order at least seven; exact order
   seven is full by the standard six-cut contradiction.
4. For a core-unavoidable root `s`, every component of `U-s` outside the
   protected-root component attaches to `s`.  Their union with `s` is
   connected, so `Z_s=U-C_s` is detachable.  If `C_s` met every portal
   family, a finite union of paths inside connected `C_s` would be a
   retained core avoiding `s`.  Therefore a whole portal family lies in
   `Z_s`, proving nonempty monopoly.
5. For a twin actually met by `Z_s`, the earlier transfer lemma applies
   exactly when `Omega(Z_s)` is contained in that twin.  Failure is thus
   witnessed by a second, literal owned row; no palette label is used.

## Scope

Different avoidable-root components in one donor may overlap, so the
classification alone does not invoke the two-piece transfer theorem
there.  Distinct donors are automatically disjoint.  A multi-owner gate
need not have order-seven boundary and need not be planar.  The remaining
dynamic theorem must splice its actual boundary state or establish one
coherent two-apex expansion.

## Deficiency-rotation check

For a detachable gate `Z` meeting both twins, `A'=X union Z` is connected
through the marked `S-X` edge.  It has literal edges to both twins through
`Z`, to the three other neutral bags through the old path core in `X`,
and to the residual donor `W=U-Z` through the gate cut.  Hence, with `W`
as centre, the other six bags really are a clique model.  A spoke
`W-F` is lost exactly when every old `U-F` endpoint lay in `Z`, which is
the definition of `F in Omega_U(Z)`.  Thus monopoly orders `0,1,2` give
respectively `K_7`, `K_7^-`, and `K_7^vee`; order at least three is the
only non-adhesion/non-near-clique warehouse residue.  If one twin is
missed by `Z`, that entire bag supplies the far side of the actual
separator.  The added theorem is GREEN.

## Opposite-root check

For roots `r,s`, a vertex in both opposite gates would force every
`r-v` path through `s` and every `s-v` path through `r`; the suffix of a
simple `r-v` path after its first visit to `s` contradicts the latter.
Thus the gates are disjoint.  Their monopoly sets are disjoint because a
nonempty row portal set cannot lie wholly in both gates.  Five row labels
then force one monopoly order at most two.  Applying the already checked
transfer/adhesion classification when a root is avoidable, and the
deficiency-rotation theorem when both are unavoidable, proves the
two-root discharge.  This extension is GREEN.

## Two-donor check

Outside a retained core the monopoly set is empty.  If the component
misses either twin, that missed bag gives the actual far side; hence in
the no-adhesion branch it meets both and may be assigned to either target.
Applying the two-root discharge in two distinct donors therefore gives
either descent/rotation immediately or two disjoint pieces supporting
both twins.  Assigning them to different targets satisfies the individual
transfer hypotheses.  The corrected two-target theorem then either
performs both transfers when the residual donors remain adjacent, or
exposes the open-neighbourhood separator of one residual donor when they
are anticomplete.  This closes the `2+2+2+1` and `3+2+1+1` exact-seven
distributions, leaving only `4+1+1+1` modulo descent/rotation.  The
corollary is GREEN.
