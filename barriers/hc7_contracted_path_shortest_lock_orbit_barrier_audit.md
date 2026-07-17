# Audit of the shortest-lock Kempe-orbit barrier

**Verdict:** GREEN (internal proof replay; not external peer review)

**Audited barrier revision:** SHA-256
`eb15326b1ee482a2fde8650749851cd2168dfe0f6e75e7f87e217d2ad39060df`
of `hc7_contracted_path_shortest_lock_orbit_barrier.md`.

## 1. Construction and chromatic number

The adjacency specification is unambiguous.  The displayed four-colouring
of `F_m` is valid.  In a hypothetical three-colouring, completeness of
both path ends to `K union L` forces that union to use exactly two colours
and both path ends to use the third.  Connectedness of each `K_{m,m}`
then makes its two sides the two colour classes.  The two orientations of
`L` give exactly the two conflicts at `v_2v_1` and `v_3v_4`.  Hence
`chi(F_m)=4`, and join additivity gives `chi(G_m)=7`.

## 2. Connectivity and the separator

Deleting `V(P)` separates the two complete bipartite components.  For the
reverse inequality, when at least one of `v_1,v_4` remains it joins all
surviving vertices in `K union L`; each other surviving path vertex has a
surviving neighbour there because its prescribed two sides have total
order at least four.  When both ends are deleted, at most one additional
vertex is absent, and `v_2v_3` together with the still-connected
bipartite components joins the graph.  Thus `kappa(F_m)=4`.

The three vertices in the join factor are universal, so every cut of
`G_m` contains all three and a four-cut of `F_m`.  Therefore
`kappa(G_m)=7`, and `V(K_3) union V(P)` is the stated actual order-seven
separator.

## 3. Contracted path and Kempe orbit

After contraction, the contracted vertex and the original triangle form
a `K_4` complete to `K dotunion L`.  Every six-colouring therefore gives
the `K_4` four distinct colours and gives both connected bipartite
components the remaining two colours, with independent orientations.
The outside-neighbour calculation gives exactly (4.3)--(4.5).

Switching either one of the two bichromatic components reverses exactly
one orientation and transfers the one-edge lock.  Switching a colour of
the `K_3` factor with one of the two bipartite colours is a Kempe
interchange on a connected component because of the join.  Together with
palette permutations and the two independent orientation changes, these
moves reach every six-colouring with the contracted vertex's colour fixed.
Thus the shortest lock length is always one.  The prefix recurrence fails
at indices two and four in the two orientations, respectively, so the
latest-failure extremum is (4.5).  At its saturated vertex `v_3`, the two
neighbour colours occur in distinct components `K,L`; the endpoint
criterion genuinely fails there.

## 4. Scope and positive outcomes

The `K_7` certificate is valid.  Choose a `K_{2,2}` inside `K`; one
adjacent pair gives two singleton branch sets, the remaining adjacent pair
is one connected branch set, and `{v_1}` is the fourth.  These four branch
sets form a `K_4` model, and the three universal join vertices extend it
to a `K_7` model.

The example is not minor-minimal: for `m>=2`, deleting one vertex from a
bipartition side leaves both complete bipartite components connected with
an edge and preserves the same four-chromatic argument.  Hence the note
correctly refutes only the Kempe-orbit extremal mechanism.  It does not
refute a theorem retaining the `K_7` or actual-order-seven-separation
alternatives, and it is not a counterexample to `HC_7`.
