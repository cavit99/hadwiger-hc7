# Audit: private-pair V-extraction

**Verdict:** GREEN.

## 1. Endpoint labels

Because the private pair `P={p,q}` meets every support except `A` and the
whole family has no two-transversal, `P` must avoid `A`.  For each `a in A`,
a support missed by `{q,a}` cannot be `A`; it must meet `P`, and avoidance
of `q` therefore forces it to contain literal `p`.  This proves the exact
trace `P cap B_a={p}`.  The symmetric argument gives exact trace `{q}`.

No colouring, contraction, or implicit branch-set identification is used
in this step.

## 2. Intersection bound

Small-model supports have order five or six.  For `|A|=5`, avoidance of
one chosen `a` gives intersection at most four immediately.  For
`|A|=6`, failure of that bound for all six choices means intersection
exactly five.  Since the arm already contains `p` outside `A` and has order
at most six, it is exactly `(A-{a}) union {p}`.  The six arms plus `A`
are therefore all seven six-subsets of `A union {p}`; there are no missing
or duplicated deletion cases.

## 3. Terminal full-top step

The existing audited lemma says that if every vertex deletion from a
seven-vertex graph leaves a spanning `K_5` model, the graph has a spanning
`K_6` model.  Every six-subset displayed above is a genuine support, so its
hypothesis applies literally.  A `K_6` model on at most seven vertices in a
seven-connected graph lifts to `K_7`.  This contradicts the theorem's
host assumptions and closes the only failure case.

## 4. Scope

The conclusion controls the two intersections with the avoided support,
not the intersection of the two arms with each other.  It also says
nothing about their split-row decorations.  Treating the V as already
contraction-clean would be an invalid strengthening.
