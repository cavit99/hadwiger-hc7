# Independent audit: bounded-interface pole-move normal form

**Verdict:** **GREEN** for the exact source revision

```text
01fa19f3a58a232a92a7479877b786d55341990cd3dd81af92a384231d99794f  results/hc7_bounded_interface_pole_move_normal_form.md
```

This is a separate internal mathematical cold audit, not external peer
review.  Any change to the theorem, proof, quantifiers, or trust boundary
requires renewed audit.

## 1. Quantifiers and colour orientation

The transition fixes the exact-block colour on `I`.  In the last pole
move, the forward orientation changes `x` from the pole colour `delta` to
`beta`; the reverse orientation assigns `x` the colour of `u`.  Since
`delta` is absent from the final boundary, the operated boundary component
is the singleton `{x}`.

Outcome 1 correctly quantifies over **some** extension of the fixed final
boundary trace.  This is essential: when at most four boundary colours are
used, the proof changes from the initially fixed extension to one obtained
by switching the full `delta`--`epsilon` component containing `u`.  The
negation of that existential outcome correctly gives the universal
isolation statement for every final `B`-extension in outcome 2.

## 2. Low-palette branch

With at most four colours on `S`, there are two boundary-absent colours,
`delta,epsilon`.  Switching their full component containing `u` leaves the
labelled boundary trace fixed and changes the colour of `u` to `epsilon`.
The last `delta`--`beta` interchange then avoids `u`.  If its full component
met no other boundary component, it would extend the predecessor through
`B`, contradicting shortest endpoint choice.  A shortest first-contact path
therefore has interior in `B-(S union {u})`, as claimed.

## 3. Five-colour residue

If the final `beta`-block were `{x}`, globally transposing `beta,delta`
would carry the final boundary colouring to its predecessor.  Boundary
extension is palette-invariant, so the predecessor would extend through
`B`, a contradiction.  The `beta`-block is therefore non-singleton and,
because the exact-block colour is excluded from every move, disjoint from
`I`.  The predecessor uses all six colours and is exactly the split of
`x` into a singleton `delta`-block.

In this five-colour case `delta` is the unique boundary-absent label, so
every extension gives `u` colour `delta`.  Any component of `x` in the
displayed two-colour graph after deleting `u` which reaches another
boundary vertex supplies outcome 1 by a shortest first-contact path.
Otherwise the asserted isolation holds for every extension.

## 4. Trust boundary

The result is nonterminal.  It neither synchronizes the shore colourings
nor makes its path disjoint from the first `C`-shore obstruction.  The
claim that an anchored colouring of `G-ux` can be spliced into the same
transition is explicitly rejected: the proper-minor colouring has an
uncontrolled boundary trace.  The only direct dependency is the separately
audited exact-block lifting theorem, used within its stated scope.
