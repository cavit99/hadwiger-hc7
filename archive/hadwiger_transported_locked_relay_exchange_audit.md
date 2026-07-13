# Audit: transported locked-relay detour

## Verdict

**GREEN.**  The detour gives a literal `U`-meeting `K_6` for every
locked four-clique relay state, independent of the two shore orders.

## Bag audit

Let `T` be the old-boundary `K_4`, choose `q in T-P` with `py_q` an
edge, and choose its opposite-triangle neighbour `r` (arbitrary there
when `q=z`).

1. `C_q={q,r,y_r}` is connected through `qr,ry_r` and meets `U` at
   `y_r`.  Its representative `q`, the singleton representatives in
   `P`, and the representatives of the unchanged `{x,y_x}` bags form
   the clique `T`; hence the four row bags are pairwise adjacent.
2. In the transported partition `F=H union(S-P)`.  Therefore
   `F-(Q union {r})` is connected: it contains connected `H`, and every
   retained old-boundary vertex has an edge to `H`.  Adding `y_a` for
   either remaining opposite-triangle label `a` gives a connected
   `U`-meeting bag.
3. `R union {y_q}` is connected because `R` sees every member of
   `U-{p}`.  It sees the deficient singleton `{p}` through the locked
   edge `py_q`, sees `C_q` through `qy_q`, and sees every unchanged row
   through its nondeficient `U` trace.
4. The two shore-derived bags are adjacent through an `R-y_a` edge.
   The canonical bag sees every row representative through the old full
   shore `H`.  All displayed bags are disjoint: `q,r,y_r,y_q,y_a` occur
   in their named bags only.

The six bags all meet `U`; adjoining `{u}` gives `K_7`.  No palette
alignment, virtual edge, or omitted optional contact is used.  The only
transported row left by this theorem is the antipodal three-clique row.
