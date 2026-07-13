# Adversarial audit: four-connected rooted carrier funnel

This audits hadwiger_four_connected_rooted_diamond.md.

## Dependency check

* The only external structural input in the proofs is the
  Fabila-Monroy--Wood rooted-\(K_4\) theorem for four-connected graphs.
  The quoted form is exact: rooted \(K_4\), or planar with the four
  roots cofacial.
* The Kawarabayashi--Lee--Yu result is used only for research guidance,
  not in Corollary 4.1 or Theorem 4.5.  The cited final result is their
  Theorem 1.2: a prescribed-end path with two-connected remainder,
  except for a double wheel centred at those ends.  Their weaker
  Theorem 2.3 is an intermediate lemma.
* No computational enumeration is used in any positive conclusion.

## Branch-set and overlap audit

1. In Corollary 4.1, the carrier path lies in \(D\cup R_5\), hence is
   disjoint from \(e_6,e_0,v,3,4,h,1,2\).  It contains \(6\) and the
   right exterior root \(r_5\), so its lifted bag really sees
   \(1,2\) and \(h\), respectively.
2. The literal \(K_4\) in the quotient is genuine:
   \(pv,p3,p4\) lift through \(6v,r_53,r_54\), and
   \(v3,v4,34\) are Moser edges.
3. In Lemma 4.3, the prefix bag need not initially see \(h\); this is
   why the lift is only \(K_7^-\).  A clean suffix can be absorbed
   because it meets none of the other three rooted bags and is disjoint
   from \(h,1,2\).  This repairs exactly the missing \(h\)-edge.
4. In Lemma 4.4 the three protected roots are explicitly assumed
   outside the four-cut and in distinct components.  The anchors
   \(y_i,z_i\) are therefore available, and all four displayed bags are
   disjoint.  The note does not silently extend the conclusion to
   root-on-cut or shared-component cases.
5. In Theorem 4.5, the non-four-connected outcome forces two, not
   merely at most two, exceptional vertices because a shore must have
   \(4-|Y|\) distinct neighbours in the two-vertex carrier
   \(\{5,6\}\).
6. In Corollary 4.6, the four shore components are pairwise disjoint
   and anticomplete, but adjacency of the four composite bags is
   supplied by fullness to the distinct boundary vertices
   \(h,5,y,z\).  The singleton bags \(1,2,6\) form the required
   triangle.

## Connectivity audit

* Deleting \(h,1,2\) from a seven-connected graph leaves a
  four-connected graph: a cut of order at most three in the remainder
  would lift to a cut of order at most six.
* Contracting a carrier is never assumed to preserve
  four-connectivity.  Theorem 3.1 records the exact failure, and
  Lemma 4.2 stops immediately before the first noncontractible edge.
* At that first failure, replacing the quotient cut vertex by the two
  edge ends yields a separator of order at most four; four-connectivity
  forces an exact four-cut.
* Every component behind an exact \(k\)-gate has the stated portal load
  because its entire neighbourhood lies in the path, the gate, and
  \(\{h,1,2\}\), while \(G\) is seven-connected.

## Sharp limitations

* A rooted diamond joined to \(h,1,2\) is only \(K_7^-\).  No conclusion
  in the note treats it as \(K_7\) without an independent repair edge.
* A prescribed connected/path root is false in general; the
  \(P_4\vee I_3\) example blocks that shortcut.
* The KLY path is not carrier-confined and need not avoid the protected
  roots.  The note therefore does not claim that its two-connected
  remainder is already available in the Moser carrier.
* The full seven-adhesion and dirty-routing outcomes of Theorem 4.5
  remain to be eliminated.  Thus this note is a structural funnel, not
  a proof of \(HC_7\).

Verdict: the displayed positive lemmas are branch-set and
connectivity-clean under the standing nested-Moser hypotheses.  The
remaining gap is stated without conflating \(K_7^-\) with \(K_7\) or
assuming contraction preserves connectivity.
