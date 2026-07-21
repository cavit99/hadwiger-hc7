# Independent audit: prescribed deleted-colour `K_4` contact barrier

**Verdict:** **GREEN** for the precise fixed-deletion counterexample at the
revisions below.  This is a separate internal mathematical and computational
cold audit, not external peer review.

## Exact revisions audited

```text
6d3fad97f6507192bfce9559d56879b92e783f094fc52748c022c3165ac9db77  barriers/hc7_degree8_deleted_colour_k4_contact_barrier.md
052d4534a8cf6885240446bdf8f87fff0d1889dee07415f37dd728c55c07aa69  barriers/hc7_degree8_deleted_colour_k4_contact_barrier_verify.py
```

Any change to the construction, refuted statement, verifier, or trust
boundary requires renewed audit.

## Reproduction

I ran

```text
.venv/bin/python barriers/hc7_degree8_deleted_colour_k4_contact_barrier_verify.py
```

and obtained

```text
five_colourings=253200 colourful_on_U=253200
routing_pairs=10 designated_paths=shortest_disjoint
rooted_K4_models=927 maximum_contact_vector_e_r1_r2_r3_r4=(1,4,4,4,4)
explicit_U_rooted_K5=PASS
scope=fixed-deletion contact shortcut only; existential deletion survives
```

## Mathematical and encoding audit

The listed edges make the five displayed classes independent.  The clique
`{q} union W` proves five-chromaticity.  In every proper five-colouring it
uses all colours; the clique `T` avoids the colour of `q`, forcing `e` to
that colour, while `q` together with `W-{w_i}` forces `r_i` to the colour of
`w_i`.  Thus all five roots are colourful.  The verifier independently
enumerates all `253,200` labelled proper five-colourings and confirms this.

The explicit bichromatic paths connect every root pair.  The designated
paths

```text
e-t1-p1-r1  and  r2-w3-w2-r3
```

are vertex-disjoint, use only their endpoint colours, and have distance
three because their endpoints are nonadjacent and have no common neighbour
in the relevant two-colour subgraph.

After deleting `A_e`, the graph consists of the rooted `W` side and the
clique `T`, joined by the unique edge `w1t2`.  Any rooted branch set which
meets `T` must contain that edge, so disjoint branch sets allow at most one
`e`-contact.  The displayed rooted `K_4` attains one.  The verifier's
`5^8=390,625` assignments exhaust every placement of the eight nonroots into
four fixed rooted bags or no bag; exactly `927` are rooted `K_4` models and
none has more than one contact.

For deletion of each `A_i`, the verifier checks the displayed four-bag model
inside the remaining colour classes.  All four bags contact the deleted
root, attaining the trivial upper bound four.  Hence the exact maximum
vector is `(1,4,4,4,4)`.  The separately displayed five bags also form a
valid `U`-rooted `K_5`: their connectedness and every pairwise contact check
directly.

Martinsson--Steiner Theorem 1.3 supplies a rooted `K_4` for a colourful set
in a four-chromatic graph; it supplies no extra contact condition.  Its use
in the note is therefore within the cited theorem's scope.

## Trust boundary and research status

This graph refutes only the shortcut after a **prescribed** deletion, here
`x=e`.  It does not refute the existential assertion that some deletion has
three contacts: the other four deletions each have four.  Thus the broad
conclusion that every Martinsson--Steiner deleted-colour contact strategy is
false would be too strong.  What is proved is that a proof cannot commit to
an arbitrary fixed deleted colour and infer three contacts from complete
routing alone; an existential-over-`x` strategy remains open.

The graph already has a rooted `K_5` and is not embedded in a
seven-connected, contraction-critical, `K_7`-minor-free host.  It neither
refutes the component-aware bridge theorem nor `HC_7`, and its unique bridge
is not an aligned host separator or strict same-form reduction.  Complete
routing therefore still leaves the special five-root rooted-`K_5`-or-aligned
host-separator inference unresolved; this barrier rules out only the stated
fixed-deletion shortcut for supplying that inference.
