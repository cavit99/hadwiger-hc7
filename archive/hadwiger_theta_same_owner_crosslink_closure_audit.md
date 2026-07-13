# Independent audit: theta same-owner crosslink closure

**Verdict: GREEN.**  The proof in
`hadwiger_theta_same_owner_crosslink_closure.md` correctly eliminates the
case in which one full shore owns both theta crossbars.

## Checks

For the theta complement

\[
 \{01,02,05,12,15,24,45\},
\]

the `05|12` packet contains mutually disjoint paths `P_05,P_12`.  Since
`52,14,40` are boundary edges,

\[
 P_{05}\cup 52\cup P_{21}\cup14\cup40
\]

is a simple cycle through `0,5,2,1` in that cyclic order.  The `15|02`
packet in the same shore contains mutually disjoint paths `P_15,P_02`,
which join the opposite pairs `(5,1)` and `(0,2)`.

Fabila-Monroy and Wood, *Rooted K4-Minors*, Lemma 7 has exactly the
strength used here: a cycle containing `a,b,c,d` in order together with
an `(ac,bd)` linkage gives a `K_4` minor rooted at those four vertices.
The two linkage paths must be disjoint from each other; they need not be
disjoint from the cycle.  Thus the two packet systems may intersect.

The resulting four rooted bags use only the common owner shore and the
boundary vertices `0,1,2,4,5`.  The opposite full shore is untouched.
It is adjacent to every rooted bag through its named root and to the
singletons `3,6`; those singletons are adjacent to each other and to all
four roots.  Hence the rooted `K_4`, the opposite shore, `{3}`, and `{6}`
are a valid seven-bag clique model.

## Exact consequence and limit

Together with the audited theta nonowner descent, this proves that in a
target-free theta cell the crossbars have opposite owners and each shore
contains a proper fragment behind a nested exact seven-cut.  Therefore a
theta adhesion cannot have a globally minimum exact-seven fragment as a
shore.

The tempting stronger assertion with the two packets in opposite shores
is **RED**.  Although a rooted cycle/linkage can again be assembled, it
may consume both full shores.  Moreover the proposed replacement seventh
bag `{4}` is not adjacent to the rooted bags at `2` and `5`, because
`24,45` are precisely missing boundary edges.  The Fabila-Monroy--Wood
construction gives no required `4`-portals in those two bags.  The theorem
must retain its same-owner hypothesis.
