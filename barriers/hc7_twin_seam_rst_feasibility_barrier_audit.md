# Independent audit: RST-feasibility localization barrier

**Verdict:** **GREEN at the frozen hashes below.**  The 25-vertex host
has all of the local twin-seam, packet, colouring, lock and response-bundle
properties asserted in
[`hc7_twin_seam_rst_feasibility_barrier.md`](hc7_twin_seam_rst_feasibility_barrier.md),
while exactly one of the two local Robertson--Seymour--Thomas pairings
fails in the reserve quotient.  Both corresponding pairings nevertheless
exist globally in the common edge-deleted host.

The scope restriction is essential and correct: the host has a proper
six-colouring and a literal `K_7` model.  It therefore falsifies only the
claim that the **local packet geometry plus the separating response bundle
and an equal/equal state** force both reserve-quotient pairings.  It does
not falsify the active terminal-disjunctive theorem, strong
seven-contraction-criticality, or `HC_7`.

## 1. Frozen artifacts

The audit used these exact files:

```text
731c007ea0dc6f12065fd4adea27ab046f3a5d7a104304508639f790ea685d7a  active/hc7_twin_seam_rst_feasibility_falsifier.py
554c5ef5ed20b5ecb2aec4734deba2fbfac9c24c8a5280ea796eba0348149412  barriers/hc7_twin_seam_rst_feasibility_barrier.md
```

For an additional implementation-independent fingerprint, form a text
stream consisting first of the sorted lines `V vertex`, then the sorted
lines `E endpoint1 endpoint2`, with every edge endpoint pair sorted and a
final newline.  Its SHA-256 values are

```text
4812f99c65cc3550e7f32f48ab5f1171aee7fa76155e58ee29f2fa0c0dd3a163  host: 25 vertices, 120 edges
5f1a5f52939d997ede7a2609f87c7cd15b1a83b2db87467f26982dcdb3c5f20a  reserve quotient: 12 vertices, 27 edges
```

Running the supplied verifier gives

```text
GREEN twin_seam_rst_feasibility_falsifier
order=25 connectivity=7 packet_vector=(1,1)/(1,1)
pairing_p_c1_q_c2=false pairing_q_c1_p_c2=true
response_paths {2: ['q', 'i1', 'w2'], 3: ['q', 'i2', 'w2'], 4: ['q', 'w9', 'w2'], 5: ['q', 'w7', 'w10', 'w3', 'w2']}
global_pairings=true local_first_pairing=false
equal_equal=true proper_proper=true literal_K7=true
```

All checks below were then repeated without calling the verifier's
`verify`, `proper_off`, `exact_partition`, `packet_number_one`,
`paired_feasible`, or `literal_clique_model` helpers.

## 2. Literal regions, actual separations and connectivity

The declared sets are pairwise disjoint and exhaust the host:

\[
 A=Z\mathbin{\dot\cup}D\mathbin{\dot\cup}E,
 \qquad S=I\mathbin{\dot\cup}A_0\mathbin{\dot\cup}B_0,
 \qquad R=\{r_1,r_2\}.
\]

Direct neighbourhood computation gives

```text
N(A)=N(R)=S,
N(D)=N(E union B0 union R)=Omega_D,
N(E)=N(D union A0 union R)=Omega_E.
```

Thus the old cell and both residual twin cells are literal actual
separations.  There is no hidden quotient identification.  The open old
thin shore is biconnected: deleting each of its 16 vertices leaves it
connected.  The old boundary is connected and bipartite, with bipartition

```text
{a1,i1,u} | {a2,b,i2,i3}.
```

There is no old thin--rich edge, and `z` is the unique old-thin neighbour
of `u`, so `e=zu` has the asserted literal role.  The lobe neighbourhoods
are exactly

\[
 N(D)=\{p,q,i_1,i_2,i_3,a_1,a_2\},
 \qquad
 N(E)=\{p,q,i_1,i_2,i_3,u,b\}.
\]

An independent bitset search deleted every vertex set of order at most
six.  It tested

```text
1 + 25 + 300 + 2300 + 12650 + 53130 + 177100 = 245506
```

sets, and every remainder was connected.  Deleting the literal seven-set
`S` separates `A` from `R`, so the connectivity is exactly seven.  The
minimum degree is independently seven.

## 3. Exact residual packet vector

Every nonempty subset of each open shore was independently tested for
induced connectivity and for a literal neighbour at every boundary
vertex.  In the order

```text
D over Omega_D,
E union B0 union R over Omega_D,
E over Omega_E,
D union A0 union R over Omega_E,
```

the numbers of connected full packets, followed by their minimum orders,
are

```text
(81,4), (265,4), (16,2), (1185,4).
```

In each family every two full packets intersect.  Since each family is
nonempty, all four packing numbers equal one.  Separately, `r1` and `r2`
are disjoint singleton `S`-full packets on the old rich shore.  Hence the
claimed residual `(1,1)/(1,1)` geometry and the selected old packet pair
are literal.

## 4. Reserve quotient and both RST pairings

The reserve host is induced on

\[
 D\cup A_0\cup\{r_1,r_2,p,q\}.
\]

Contracting `a1-r1` to `c1` and `a2-r2` to `c2` gives the 12-vertex,
27-edge quotient fingerprinted above.  A planarity computation returns a
face

```text
p, w11, c2, c1, w2, q,
```

whose reverse terminal order is `p,q,c1,c2`.  This directly confirms the
claimed failed-pair web order.

For each prescribed pairing, an independent exhaustive search chose every
connected carrier containing the first terminal pair and excluding the
second pair, then tested whether the remaining graph connects the second
pair.  For

\[
 \{p,c_1\}\mid\{q,c_2\}
\]

all 91 possible connected carriers fail.  For

\[
 \{q,c_1\}\mid\{p,c_2\}
\]

the disjoint connected witnesses

```text
{q,w2,c1}       {p,w11,c2}
```

work.  Thus the two local feasibility values are exactly `false,true`,
as claimed.

Both pairings exist globally after deleting both named edges.  Literal
representatives are

```text
p-i2-a1       q-i1-a2,
q-i2-a1       p-i1-a2.
```

The two paths in each row are vertex-disjoint, avoid both `e=zu` and
`f=qw2`, and leave the reserve host through `i1,i2`.  This verifies the
precise localization failure rather than merely the existence of some
unlabelled global linkage.

## 5. Exact colour states and the separating response bundle

An independent scan of all 120 host edges found these exact sets of
monochromatic edges:

| displayed colouring | monochromatic host edges |
|---|---|
| `PHI` | `zu` only |
| `PSI` | `qw2` only |
| `EQUAL_EQUAL` | `zu` and `qw2` only |
| `PROPER_PROPER` | none |

Consequently `PHI` is a six-colouring of `G/e`, `PSI` is a six-colouring
of `G/f`, the equal/equal state descends through both named contractions,
and `PROPER_PROPER` is a literal proper six-colouring of the whole host.

The exact crossed boundary partitions are

```text
             PHI                              PSI
Omega_D:    {a1,q}|{a2,p}|{i1}|{i2,i3}       {a1,p}|{a2,q}|{i1}|{i2,i3}
Omega_E:    {q,u}|{b,p}|{i1}|{i2,i3}         {p,u}|{b,q}|{i1}|{i2,i3}.
```

In the `0-1` graph of `G-e` under `PHI`, the edge `f=qw2` is a bridge.
After deleting it, the relevant two components are

```text
{p,q,z}
{a1,a2,b,u,w10,w2,w4}.
```

Swapping precisely the first component gives `PSI`.  In `G-f` the five
literal, pairwise internally disjoint response paths are

```text
q-i1-w2                    colours 1,2
q-i2-w2                    colours 1,3
q-w9-w2                    colours 1,4
q-w7-w10-w3-w2             colours 1,5
q-p-z-u-a2-a1-w2           colours 1,0.
```

The last path contains `e=zu`; the other four avoid it.  All five avoid
`f`.  This is the asserted full separating five-rung response bundle, not
five paths that silently reuse a portal.

## 6. Literal terminal certificates

The displayed `PROPER_PROPER` assignment has no monochromatic host edge,
so the shell is six-colourable.  It is therefore not a seven-chromatic,
strongly seven-contraction-critical graph.

The seven displayed minor bags are nonempty and pairwise disjoint.
Connected spanning edges inside the nonsingleton bags may be chosen as

```text
B1: b-r2
B2: i2-w10
B3: q-w9, w9-w3, q-e1, e1-z, z-y4
B4: a1-r1, a1-w6, w6-w4
B5: i3-w2
B6: singleton u
B7: i1-a2, i1-p, i1-w11, i1-w7, i1-y3.
```

One literal edge for every interbag pair is:

```text
B1-B2 r2-i2    B1-B3 b-e1      B1-B4 b-a1
B1-B5 r2-i3    B1-B6 b-u       B1-B7 b-i1
B2-B3 i2-e1    B2-B4 i2-a1     B2-B5 i2-w2
B2-B6 i2-u     B2-B7 i2-i1     B3-B4 w3-w4
B3-B5 e1-i3    B3-B6 z-u       B3-B7 e1-i1
B4-B5 a1-i3    B4-B6 r1-u      B4-B7 a1-a2
B5-B6 i3-u     B5-B7 i3-i1     B6-B7 u-a2.
```

Hence the certificate is a literal `K_7` model in the full host.  The
host takes both permitted terminal exits: a proper six-colouring and a
`K_7` minor.

## 7. Verifier micro-audit and safe conclusion

The source was read line by line.

* `build` deterministically constructs the declared simple graph.  The
  relabelled icosahedron has exactly the intended terminal labels; the
  three removed edges are present before deletion.  All later edge
  additions respect the declared regions.
* `external_neighbourhood` computes literal open neighbourhoods.  The
  stronger two-sided actual-separation equalities were checked
  independently above.
* `proper_off` permits equality only on the explicitly named omitted
  edges.  Every colouring dictionary has exactly the full 25-vertex key
  set.  The independent monochromatic-edge table removes any risk from an
  omitted-edge convention.
* `exact_partition` groups literal boundary vertices by their displayed
  colours; it makes no quotient identification or boundary relabelling.
* `full_packet_masks` enumerates every nonempty subset of a finite shore,
  tests induced connectivity, and then literal boundary contact.
  `packet_number_one` is logically exact because a packing of order at
  least two exists exactly when two enumerated masks are disjoint.
* `reserve_quotient` contracts precisely the two connected reserve pairs.
  Its edge set and both pairing values were rebuilt independently.
* `paired_feasible` is an exact two-fragment test: one connected carrier
  is selected, and a path in its complement supplies the other.  The
  independent 91-carrier enumeration confirms the negative case.
* `literal_clique_model` checks nonempty disjoint bags, induced
  connectivity, and a literal edge for every bag pair.  The spanning and
  interbag edge lists above independently certify all of these conditions.

No assertion in the barrier requires global minimum-shore rank, absence
of a terminal outcome, or strong contraction-criticality.  Conversely,
the certificate gives no reason to weaken those hypotheses in the active
theorem.  The exact safe conclusion is:

> The local twin-seam geometry, residual `(1,1)/(1,1)` packet data,
> crossed named responses, an equal/equal state, and the complete
> separating response bundle do not by themselves force both local RST
> feasibility pairings.  A failed pairing can be a genuine four-web even
> though both labelled pairings exist globally.  Eliminating that web in
> the active proof must use strong criticality or discharge one of the
> permitted terminal/strict-handoff outcomes.
