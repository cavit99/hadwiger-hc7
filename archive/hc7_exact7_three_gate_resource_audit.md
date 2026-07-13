# Superseded audit: literal three-gate resource exchange

The audited theorem remains correct, but its content is subsumed by
`../results/hc7_exact7_three_gate_resource_exchange_audit.md`.

## Verdict

**GREEN AS PATCHED.**  Lemma 1.1, Theorem 2.1, and the classifications
for two, three, and at least four gate lobes are correct.  The proof uses
only literal graph edges.  It neither imports a virtual edge of the web
completion nor identifies a colour class with a branch set.

Two expository defects were patched in the source:

1. the displayed two-set Hall obstruction now says that either endpoint
   portal set is empty or their union has order at most one; and
2. Corollary 3.4 now invokes Theorem 2.1 directly when `c>2`, rather than
   citing the two-lobe wording of Corollary 3.3.

No mathematical hypothesis was added.

## 1. Gate lobes and the actual separator

Let `C_i` be a component of `L-T`.  Its neighbourhood in `L` is a subset
of the three-element cut `T`.  If it missed a gate vertex, its at-most-two
remaining gate neighbours would separate `C_i` from another component of
`L-T`, contrary to three-connectivity.  Hence

```text
N_L(C_i)=T.
```

There are no edges from `L` to `R`, and different components of `L-T`
have no edges between them.  Therefore, literally,

```text
N_G(C_i)=T union N_S(C_i).
```

After deleting this set, `C_i` remains on one side and the nonempty shore
`R` (indeed its three packets) remains on the other.  Thus this is an
actual separator, not merely a separator in `L` or a web completion.
Seven-connectivity gives

```text
3 + |N_S(C_i)| >= 7,
```

so every lobe meets all three literal gate vertices and at least four
literal boundary labels.

## 2. The four carrier bags

For a literal clique `U subseteq T`, choose one lobe `C_0` and, for every
`t in T-U`, a different lobe `C_t`.  The count is exactly

```text
1 + |T-U| = 4-|U|,
```

so the assumed lobe budget is necessary and sufficient for this choice.
The four pre-anchor bags are

```text
C_0,
C_t union {t}       for t in T-U,
{u}                 for u in U.
```

They are connected and disjoint.  Their six pairwise adjacencies are all
literal:

* `C_0` meets every gate vertex;
* a lobe `C_t` meets every gate vertex, so an enlarged lobe bag meets
  every other gate bag; and
* two singleton gate bags are adjacent because `U` is a literal clique.

This verifies the construction for every clique size `0,1,2,3`; no edge
of the ambient web rib is being assumed.

## 3. Hall extension with arbitrary overlaps

There are exactly four portal-choice sets.  Each choice set belonging to
a lobe bag has order at least four.  The singleton-gate subfamily has an
SDR by the stated portal-rank hypothesis.

For any subfamily containing a lobe set, its union has order at least
four, while the subfamily has at most four members.  For any subfamily
containing only gate sets, Hall follows from the gate SDR.  These are all
subfamilies, so the whole four-set family has an SDR.  This remains valid
when every lobe portal set is identical and overlaps all gate portal
sets; no disjointness of portal sets was silently used.

As a finite adversarial check, I exhaustively enumerated all ordered
families of `k=0,1,2,3` gate portal sets on a seven-element boundary,
retained exactly those with an SDR, and adjoined `4-k` identical lobe
sets of order four (the maximal-overlap test).  Every resulting
four-family passed Hall.  The numbers of retained gate families were

```text
k=0:         1
k=1:       127
k=2:    16,122
k=3: 2,045,457
```

and no counterexample occurred.  The exhaustive check is redundant with
the preceding two-line Hall proof but guards precisely the overlap issue.

## 4. All literal `K_7` adjacencies

Attach four distinct boundary representatives to the four carrier bags.
They remain connected, disjoint, and pairwise adjacent.  Let the three
unused boundary vertices be `r_1,r_2,r_3`, and form packet bags

```text
P_j union {r_j}.
```

Each packet bag is connected by fullness.  For two packet bags, `P_i`
has a literal edge to the other bag's anchor `r_j`.  For a packet bag and
a carrier bag, `P_i` has a literal edge to the carrier's boundary anchor.
The six carrier-carrier adjacencies were checked in Section 2.  Hence all
21 adjacencies of the seven branch sets are present, and all seven bags
are pairwise disjoint.

## 5. Corollary classification

* If `c>=4`, choose `U` empty.  The theorem closes the cell.
* If `c=3`, any gate vertex with a boundary neighbour gives a rank-one
  clique `U={u}` and closes the cell.  A survivor therefore has
  `N_S(T)` empty.
* If `c=2`, a literal gate edge closes whenever its two endpoint portal
  sets have a two-set SDR.  Failure is exactly: one set is empty, or the
  two nonempty sets have one-element union.
* If `T` is a literal triangle and the transversal rank of its three
  portal sets is at least two, some two gate vertices have distinct
  representatives; their literal edge is a size-two clique and Theorem
  2.1 closes the cell.  Thus a surviving triangle gate has portal rank at
  most one.

Because `T` is a vertex cut, `L-T` has at least two components.  Together
with the `c>=4` closure, the only lobe counts left are exactly two and
exactly three, with precisely the restrictions stated in Section 4 of
the source.

## 6. Scope

The result does not close either residual cell.  In particular, three-
connectivity alone does not split a lobe into two usable carrier bags,
and the theorem makes no apex, transversal, or equality-state claim.
What is proved is the reusable literal resource principle: enough gate
lobes plus a portal-ranked literal gate clique always assemble four
carriers, which three full opposite packets lift to a `K_7` model.
