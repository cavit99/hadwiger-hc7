# Independent audit: Kempe-trace synchronization at an exact seven-adhesion

## Verdict

**GREEN WITH THE STATED SCOPE.** The critical-edge fan, synchronized
boundary switch, portal-incidence exchange, and rooted-diamond lemma are
correct. The note also correctly refuses to infer a \(K_7\) minor from
an arbitrary clean chain: a model-specific lift or a coherent web
argument is still required.

The strongest conclusion supported by the note alone is:

> Failure of a compatible colour repair gives a shortest chain of actual
> bichromatic regions, with each segment represented by a boundary-clean
> connector or by a named first dirty boundary hit.

It does not say that two chains split between different shores form a
same-shore crossing.

## 1. Critical-edge fan

In an \(r\)-colouring of \(G-ab\), the ends \(a,b\) must have the same
colour \(\alpha\). If their \(\alpha/\beta\) Kempe components differ,
switching the component of \(a\) makes the deleted edge proper. Thus the
ends lie in one component for every \(\beta\ne\alpha\), giving an actual
bichromatic path and all five other neighbour colours when \(r=6\).
Lemma 1.1 is exact.

## 2. Boundary synchronized switch

For each shore, the \(\alpha/\beta\)-components partition their nonempty
boundary traces. A class of the join of these partitions is a union of
blocks of every shore partition. Therefore switching every component
whose trace lies in the join class \(X\) changes precisely the colours
of \(X\) on every closed shore. The restrictions still agree on the
adhesion.

If \(a\in X\) and \(b\notin X\), exactly one deleted-edge endpoint
switches, so \(ab\) can be restored. Conversely, if \(a,b\) lie in one
join class, a shortest path in the bipartite support graph gives the
asserted boundary-simple sequence. Consecutive region nodes cannot
belong to the same shore: two bichromatic components of one shore
containing their common boundary vertex would be the same node.

Choosing a shortest path within each actual region yields exactly the
clean/first-dirty-hit alternative. No disjointness between all regions
is asserted.

## 3. Portal incidence

For an operated edge \(ux\), the incidence component containing \(C_u\)
determines a boundary-label set \(X\). Switching its operated-side
component nodes and all far-side components in its incident join blocks
again changes exactly \(X\) on every side. If \(C_x\) is outside that
incidence component, \(u\) switches and \(x\) does not; the edge is
restored and \(G\) is coloured.

Hence criticality forces either one local \(u\)-\(x\) Kempe region or an
alternating incidence path. Expanding far-side join blocks by shortest
support paths preserves the clean/dirty certificate. The proof does not
assume a common equality partition beyond the synchronized switch it
constructs.

## 4. Ordered crossing

For ordered spine vertices \(a<b<c<d\), internally disjoint off-spine
paths \(P_{ac},P_{bd}\) together with the three spine intervals represent

\[
                         ab,bc,cd,ac,bd,
\]

which is a rooted subdivision of \(K_4-ad\). Lemma 4.1 is correct.
The subsequent prose keeps the necessary qualification: only an
application that separately lifts this rooted diamond may conclude a
\(K_7\) minor.

For the sharp \(K_3\dot\cup2K_2\) exact boundary, the successful lift is
the stronger same-shore crossing in
`hadwiger_k322_full_web_closure.md`. Two clean paths lying in different
shores are insufficient; the exact six-connected counterexample in
`exact7_split_clean_crossing_counterexample_verify.py` proves this
limit.

## 5. Central edge and counterarchitecture

The five central-edge chains follow correctly from Lemma 1.1 and the
join-switch theorem. In particular:

* for \(\beta=c(v)\), \(5-v-6\) is a literal bichromatic path;
* for \(\beta=c(1)\), the edge \(16\) puts \(1,6\) together and the
  edges \(12,26\) exclude \(2\) from both colours; and
* the symmetric statement holds for \(c(2)\).

The nineteen-vertex state-only barrier also reproduces. Running
`degree9_exact7_palette_core_counterarchitecture_verify.py` gives:

```
connected/full K6 shores: PASS
boundary signatures 32 and 9, disjoint: PASS
all interior/portal deletions and contractions: PASS
all interior vertex deletions: PASS
portal endpoint equality and five-colour fans: PASS
connectivity exactly five; explicit K7 model: PASS
```

Thus operation states and Kempe fans alone do not force a common boundary
state. The example deliberately lacks seven-connectivity and is not
\(K_7\)-minor-free. The positive five-defect theorem uses exactly the
missing geometric input: seven-connectivity removes inserted web cells,
and a true same-shore crossing has an explicit labelled lift.
