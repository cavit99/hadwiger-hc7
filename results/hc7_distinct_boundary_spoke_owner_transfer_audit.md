# Independent internal audit of the distinct-boundary prescribed-spoke transfer

**Verdict:** **GREEN** for the exact source revision

```text
results/hc7_distinct_boundary_spoke_owner_transfer.md
SHA-256 65a166ff3768ccbc69c0afe0380164f180a496852a863487dcdc0d048e66287a
```

This is a separate internal mathematical audit, not external peer review.  It
checks the application of the prescribed-spoke theorem, the literal
first-boundary truncation, the connected seed partition, every branch-set
adjacency after reassignment, preservation of the fixed response data and
relaxed first-hit rank, strict decrease of the branch set labelled `U`, and
the all-direct equality case.
The pinned revision differs from the line-by-line audited revision only by
replacing the opening “audit pending” status with the link to this audit.

## 1. Imported setting

The source uses the exact extremal model and notation of the audited
three-owner concentration theorem.  In particular, the retained set `U_0`
contains the prescribed root of `U` and the retained donor `U'`; the fixed
edge from the response subgraph in `D` ends in `U'`; and every branch set in
`{X,Y,F_1,F_2,F_3}` outside the complete owner set has an old edge to `U'`.
These inherited facts are the ones used below.  They are stronger than the
bare assertions that `C` and `U_0` are connected and adjacent.

The boundary equality

```text
N_G(C)={k_1,k_2,s_D,s_X,s_Y,s_F1,s_F2,s_F3}
```

puts `k_1,k_2` in `U_0` and puts each other displayed vertex in its named
branch set.  The set `C` is therefore a component of the graph obtained by
deleting this boundary.

## 2. The prescribed-spoke fan

Theorem 2.1 of the source correctly applies the audited prescribed-first-edge
theorem with `k=5` and target set `S=N_G(C)`.  The target excludes `v`, has
order eight, and seven-connectivity implies the required six-connectivity.
Thus the cited theorem supplies one path for each of the five prescribed
edges, with distinct ends in `S` and with no shared vertex outside `v`.

Stopping each path at its first vertex of `S` preserves its prescribed first
edge.  Two stopped paths cannot acquire the same end, since that vertex would
already have belonged to both original paths outside `v`.  Starting at
`v in C`, a path cannot leave `C` before meeting `S=N_G(C)`.  Hence every
internal vertex of every stopped path lies in `C`, including the degenerate
case of a one-edge path, which has no internal vertex.

Only `k_1` and `k_2` repeat an inherited label: both have label `U`.  The six
other boundary vertices have six pairwise different non-`U` labels.  Five
distinct ends therefore use at least four labels.  Four labels occur exactly
when both vertices of `K` are ends, and the other three ends then have three
different non-`U` labels.  No palette colour is used to infer any of these
labels.

## 3. Seed partition of `C`

For Theorem 3.1, the `C`-parts of the two paths ending in `k_1,k_2` are two
initial path segments sharing `v`.  Their union `D_0` is consequently
connected, contains `v`, and has an endpoint edge to each `k_j in U_0`.

For each owner path `P_i`, the set `L_i` is empty precisely when `P_i` has no
vertex of `C` other than `v`.  When nonempty, it is a connected path segment,
has its first edge to `v in D_0`, and has its last edge to the literal owner
representative `s_i in R_i`.  Disjointness of the five fan paths outside `v`
makes `D_0,L_1,L_2,L_3` pairwise disjoint after `v` is removed from every
`L_i`.

Every component left after deleting the nonempty seeds has an edge to their
union, because `G[C]` is connected.  Assigning that whole component to one
adjacent nonempty seed preserves connectedness.  The resulting sets
`D_0',L_1',L_2',L_3'` are disjoint, cover `C`, are connected when nonempty,
and satisfy `L_i'=empty` exactly when `L_i=empty`.

## 4. Spanning labelled model after reassignment

The reassigned sets

```text
U*=U_0 union D_0',
R_i*=R_i union L_i'
```

are connected.  The first is joined to `U_0` through either endpoint edge
into `K`; each nonempty enlarged owner is joined to its old branch set by the
last edge of its seed path.  Together with the three unchanged branch sets,
they remain pairwise disjoint and partition the whole host.

All required model adjacencies survive:

- If `L_i'` is nonempty, the first edge of `P_i` joins `D_0' subseteq U*` to
  `L_i' subseteq R_i*`.  If it is empty, `P_i` is the edge `vs_i`, which
  gives the same `U*`--`R_i*` adjacency.
- Every nonowner among `X,Y,F_1,F_2,F_3` retains an edge to
  `U' subseteq U_0 subseteq U*` by the inherited complete-owner definition.
- The fixed response edge from `D` to `U'` preserves the `D`--`U*`
  adjacency.
- Every old adjacency between two non-`U` branch sets survives because their
  old branch sets are retained as subsets of the new ones.

Consequently `X-Y` is the only pair that can remain nonadjacent.  If the
reassignment makes that pair adjacent, the seven displayed connected,
disjoint sets give an explicit `K_7`-minor model.  Otherwise they give the
claimed spanning labelled `K_7`-minus-one-edge model.

The root of `U` remains in `U' subseteq U_0`; every other prescribed root
remains in its unreduced old branch set.  The selected boundary partition is
a fixed literal object in the unchanged host, and the connected response
subgraph remains inside the unchanged branch set `D`.  Its fixed edge still
ends in `U'`.  Thus all of the response data claimed in outcome 2 are
preserved literally.

## 5. Relaxed first-hit rank

A ranked path with terminal label different from `U` avoided every vertex of
the old branch set `U`, so it also avoids every transferred set `L_i'`.  It
therefore remains a valid literal first-hit path after an owner is enlarged.
An old `U`-path whose terminal remains in `U*` also remains valid.

If the old `U`-terminal lies in a transferred `L_i'`, keep the same designated
port, travel inside the fixed connected response subgraph to the endpoint of
the fixed response edge, and use that edge into `U' subseteq U*`.  The
replacement has only its new terminal outside the response subgraph.  Other
ranked paths avoided old `U`, hence avoid that terminal; overlap inside the
response subgraph is explicitly allowed by the relaxed rank.  Distinct ports
and literal first-hit ownership are unchanged.  A maximum old family thus
gives a new family of the same order, so the rank cannot decrease.

## 6. Strict decrease and the direct case

If some `L_i` is nonempty, then `L_i subseteq L_i'` is nonempty.  Since the
four primed sets partition `C`,

```text
|U*| = |U_0| + |D_0'|
     = |U| - sum_i |L_i'|
     < |U|.
```

This proves the strict descent in outcome 2.  If every `L_i` is empty, each
`P_i` has no internal vertex: its endpoint is `s_i`, and Theorem 2.1 placed
all internal vertices in `C`.  Hence `P_i` is exactly the edge `vs_i` for all
three owners.  Conversely, three such direct edges leave all `L_i` empty, so
the stated common-vertex alternative is exactly the equality obstruction to
this reassignment.

## 7. Trust boundary

The proof is conditional on the fan endpoint set being exactly
`{k_1,k_2,s_1,s_2,s_3}`.  It does not force that endpoint allocation; the
remaining patterns may contain one or more nonowner representatives.  It
also does not retain the bichromatic colour of a prescribed spoke, prescribe
which spoke ends at which target, or identify a palette colour with a
branch-set label.

The common-vertex outcome proves the three edges `vs_i` and their three
literal owner labels.  It does not say that these are the only owner contacts
of `C`, produce two disjoint rooted connected subgraphs, or by itself produce
an order-seven separation.  The strict descent uses the imported complete
owner set, prescribed roots, fixed response subgraph, permitted ports, and
relaxed rank; it would not follow from an unlabelled near-`K_7` model.

Global extremality excludes the nonterminal strict descent in the intended
application, and global `K_7`-minor exclusion excludes the first outcome.
Neither hypothesis forces the remaining endpoint pattern, and the theorem
does not prove `HC_7`.  No unresolved assumption or gap was found within
these stated limits.
