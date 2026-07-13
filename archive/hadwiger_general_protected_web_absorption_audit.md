# Audit of the all-\(t\) protected-web absorption theorem

Audited source: hadwiger_general_protected_web_absorption.md.

## Verdict

**GREEN within its stated scope.**  The theorem eliminates all
off-core bridge geometry in a \(K_t^-\)-model with two portal classes
of order at least two.  It does not create that near-clique model and
does not preserve two-portal capacity after absorbing a terminal owner
lobe.

## Checks

1. **Two-target linkage.**  After contracting the protected core \(W\),
   every target in \(B'\cup\{w\}\) is a nonloop of the strict gammoid.
   Failure of one path to \(B'\) disjoint from one path to \(w\) makes
   the target union rank one, so Menger gives exactly the displayed
   singleton or protected-core transversal.
2. **Allocated split.**  The two lifted paths give disjoint connected
   seeds \(X_0,Y_0\).  A spanning-tree edge on the path between their
   contractions extends them to a connected bipartition and supplies
   the \(XY\)-edge.  The four resulting bags have all six required
   adjacencies; together with the \(t-4\) old clique bags they form
   \(K_t\).
3. **Purity.**  Applying the two-target alternative in both
   orientations shows that an off-\(W\) component cannot carry both
   shore labels, including the cases in which one complete portal class
   lies in \(W\).
4. **Absorption.**  A pure component moved into its shore cannot create
   the deficient shore edge.  Two-connectivity gives two distinct
   attachments on \(W\), which become two new gate-to-shore portal
   vertices.  The opposite portal class is untouched.
5. **Iteration.**  Whole components of \(K-W\) are mutually
   anticomplete, so absorption changes labels only on \(W\).  The same
   protected core remains valid.  For a shortest two-terminal core,
   exhausting all bridges leaves an induced path and hence a
   non-two-connected gate.
6. **Cutvertex endpoint.**  Pure owner lobes may be absorbed after
   allowing capacity to fall to the single cutvertex portal.  The only
   lobe not absorbable into either deficient shore is a mixed lobe
   owning both portal classes.

## Trust boundary

The proof uses only ordinary vertex Menger/strict-gammoid rank two and
explicit branch-set surgery.  It assumes the input \(K_t^-\)-model,
protected core, and two initial portal multiplicities.  Applying it
before those objects are constructed would be circular.
