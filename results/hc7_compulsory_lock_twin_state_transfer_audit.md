# Independent audit: twin-boundary compulsory-lock state transfer

**Verdict:** GREEN.

**Audited source:** `results/hc7_compulsory_lock_twin_state_transfer.md`

**Source SHA-256:** `d9c460d21d4e021b1ac70d9b32ab0320f6c869655c8d8a886c26d88745776f07`

## 1. Twin separation and packet numbers

The root-deletion normalization makes `C=A-z` nonempty, connected and
`W`-full. Connectedness of `A` supplies a `C-z` edge, so `C` is full to
`Omega=W union {z}`. The set `B=R union {u}` is connected and full to
`Omega` through the old packet contacts and `uz`. There is no `C-B` edge.
Thus this is an actual order-seven separation.

Inside `B`, the only neighbour of `z` is `u`. Every full packet in `B`
therefore contains `u`, while `B` itself is full. Hence `nu_B=1`.

If `C` contained disjoint full packets `D_1,D_2`, the old thin shore would
contain the adjacent connected carriers `D_1 union {z}` and `D_2`, with
old-boundary supports seven and six. All hypotheses of the audited atomic
near-full two-carrier theorem are explicit in the source, including the
two possible frontier forms and adjacent rich packets. That theorem
six-colours `G` or displays a literal `K_7`. Thus `nu_C=1`.

## 2. Exact state transfer

Every allowed `f` has an endpoint in `R` and lies outside the induced
left closed shore. Thus `psi` colours that shore intact. Its endpoints
have the same colour, so `psi` descends to `G/f`. For a boundary-rich
edge at `W`, contracting the rich endpoint into the literal `W` endpoint
preserves all seven `Omega` labels; the other allowed cases contract
wholly off `Omega`.

All members of `W` have the same colours in the old and new boundary
views. The lock swap leaves `u` in the `alpha` block and puts `z` in the
`beta` block. Deleting `u` and inserting `z` is therefore exactly the
claimed root substitution.

If the transferred partition had packet demand at most one, exact packet
reflection through `C` would give a literal `K_7` or an intact right-shore
colouring with the same exact partition. The latter aligns with the intact
left colouring and glues. Hence its demand is at least two.

## 3. Receiver lock localization

For an alternate colour, let `K` be the right-shore bichromatic component
containing the rich endpoint `r` of `f`. If the other endpoint `q` is not
in `K`, swapping `K` changes `r` but not `q` and restores `f`. Its exact
boundary change is the trace `T=K intersect Omega`. If whole left-shore
bichromatic components reproduce `T`, the shores glue. Otherwise one left
component meets both `T` and its complement, and a shortest path between
them has distinct boundary endpoints and all internal vertices in `C`.
This proves Theorem 4.1, including empty/full traces, which glue.

## 4. Scope

The packet sum genuinely drops from three to two, and the recipient carries
a literal root map, exact state, named `f`-contraction, and receiver lock
alternatives. This is a normalized entry into the open S4 stratum.
It is not yet a global well-founded S4/S1 rank: no receiver theorem prevents
a later increase or an involutive root-exchange cycle. The source states
that limitation and does not claim S4 or `HC_7` is closed.

Corollary 5.1 is also correctly limited to the residual branch after these
handoffs are delegated. It excludes rich-internal and boundary-rich
separating lock bridges, but makes no vertex-disjointness claim.
