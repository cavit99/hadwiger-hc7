# Audit: atomic literal three-gate normal form

**Verdict:** GREEN.

## Lobe budget

Two-connectivity forces every component of `A-Z` to meet at least two of
the three gate vertices.  Relative seven-connectivity then gives

\[
             |\operatorname{Att}(C)|+|N_S(C)|\ge7.
\]

Thus a support-four component meets the whole gate and has an exact literal
seven-boundary.  Excluding this case really does give support at least five
for every component; this quantifier over every component is necessary.

## Carrier split

For `E ne D` and `e in Att(E)`, the set `E union {e}` is connected.  Its
complement is connected because the distinguished component `D` meets all
three gates, joins the two gates left outside, and every other component
retains at least one attachment after `e` is removed.  A second attachment
of `E` gives a literal edge between the two carriers.  Their supports
contain `T_E,T_D`, so unordered `(5,6)` closure applies unless both are
exactly five.

## Component and support audit

With three or more components, using two different choices of `E` forces
all component supports to be one five-set.  Choosing an attachment different
from any nominated gate then forces every gate support into the same set,
contradicting `S`-fullness.  Hence exactly two components remain.

The two support sets have order five and cover `S`; their intersection has
order three.  The allocation formulas put every gate support in `T_D`, and
put the support of each gate meeting `E` in the intersection.  The root
argument is literal: if `z` were a gate, an allocation leaving it on the
`D`-side would put `u` in `T_D`, contradicting uniqueness of `zu`.

If `E` has only two attachments, deleting those two gates leaves exactly
`E` and `D` together with the third gate.  The latter is connected and has
support `T_D`, so the configuration is the already identified twin exact
two-gate seam.  Otherwise both components meet all three gates and the
`K_{2,3}` description is exact.

## Scope

The theorem is a geometric normal form, not the missing state-composition
theorem.  A support-four boundary supplies only the audited one-sided
receiver certificate.  The symmetric seam supplies neither a common exact
state nor a packet orientation.  Those limitations are stated explicitly,
so the result closes an infinite gate family without claiming `HC_7`.
