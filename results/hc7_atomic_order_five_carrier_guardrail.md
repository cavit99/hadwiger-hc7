# Order-five compulsory-atom carrier guardrail

**Status:** bounded exact falsification support.  The search stops at order
five and is not an unbounded census or a proof of the crossed-hull theorem.

The companion verifier uses the NetworkX graph atlas to enumerate every
rooted isomorphism type `(A,z)` satisfying

```text
|A|=5,
A is biconnected,
d_A(z)>=3,
A-z is connected.
```

There are ten unrooted biconnected atlas graphs, 32 eligible labelled root
choices, and 14 rooted isomorphism types.  The boundary generator produces
192 labelled paired width-two frontiers and 19 rooted isomorphism types
after distinguishing the compulsory literal `u` (nine if `u` is required
to be adjacent to the paired singleton `c`; that extra assumption is not
made).  For each thin rooted type and each of these 19 rooted frontiers,
Z3 exhausts all `2^30`
literal `A-W` contact maps.  It imposes exactly:

1. `zu` is the sole `A-u` contact;
2. `A-z` is `W=S-{u}`-full; and
3. `|N_A(D)|+|N_S(D)|>=7` for every nonempty connected `D subseteq A`.

It then negates every adaptive return made from two disjoint nonempty
connected adjacent carriers `X,Y subseteq A`, with `z in X`, and every
partition

```text
S = I dotunion J dotunion U
```

where `I,J` are nonempty independent seed sets and `U` is a clique
reservoir.  Both seed orientations are tested.

The earlier 70-cell run used only five unrooted frontier representatives
and was incomplete.  A first 266-cell rerun was also invalid: the
generalized helper accidentally computed `N_A(D)` over the old four
string-labelled vertices, making the order-five relative-cut thresholds
too strong.  The current verifier computes internal neighbours over the
local atlas vertex tuple.  The result of that corrected run is recorded
below; no earlier `UNSAT` output is evidence.  The corrected run ends with

```text
GREEN unrooted_graphs 10 eligible_labelled_roots 32 rooted_isomorphism_types 14 frontiers 19 unsat_cells 266
```

Thus every order-five
thin-shore contact system satisfying the frozen literal geometry already
has an adaptive carrier return.  In the hypothetical-counterexample
kernel, the audited adaptive clique-reservoir theorem supplies the named
proper-minor response and six-colours `G`.

No SAT witness exists, so no canonical-rich-packet `K_7` or rooted-`K_5`
trust classification is needed.  This does not verify the global kernel on
a standalone host: it proves the stronger local fact that the carrier exit
is unavoidable before those terminal tests arise.

## Guardrail conclusion

The first possible obstruction to the post-lock state-lifting implication
has at least six thin-shore vertices.  In particular, neither an order-four
nor an order-five portal pattern can witness the fully crossed failure or
the all-locks edge-nonseparable residue.  Further atlas orders are outside
the agreed scope of this guardrail.
