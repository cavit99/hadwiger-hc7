# Wholesale transfer of every foreign-contacting exterior piece

## Status

This strengthens the off-face vertex transfer.  After coherent transport
has selected one fixed missed twin, no added exterior piece which touches
a retained foreign row needs to remain in the deficient bag: transfer the
whole piece to a suitable foreign bag.  The operation preserves the
spanning labelled near-`K_7` model and the normalized path core.

Consequently, in a deficient-bag-minimal coherent spanning model every
piece outside the path core has all of its external neighbours on the
path.  In particular a foreign-contacting locked two-row carrier cannot
remain as an **independent piece of the deficient bag**, regardless of
its internal connectivity, portal rank, or rural embedding.  Its vertices
are moved into one retained foreign bag.  This does not resolve a two-row
collision internal to that now-nonsingleton bag, and it does not give the
absorbed vertices two simultaneous foreign labels.

This is a normalization theorem, not yet `HC_7`: the remaining path-only
lobes can still obstruct colouring states, and the five nonsingleton
foreign bags still have to be met on both sides of one path cut.

## Setting

Let

\[
                  A,D,E,U_1,U_2,U_3,U_4
\]

be a spanning labelled near-`K_7` model.  The six foreign bags are
connected, pairwise disjoint and pairwise adjacent.  The deficient bag
`A` is anticomplete to the fixed missed twin `D`, is adjacent to `E`,
and contains the normalized path core `P`.  The four required
`A-U_i` adjacencies have fixed literal edges at the two endpoints of
`P`.

Assume

\[
                         A=P\cup K_1\cup\cdots\cup K_s,  \tag{1.1}
\]

where the displayed sets are pairwise disjoint, every `K_i` is connected
and has an edge to `P`, and distinct `K_i` are anticomplete.  This is the
decomposition produced by coherent transport from the normalized
nonspanning model.

## Theorem 1 (whole-piece transfer)

Let `K=K_i`.  If `K` has an edge to a retained foreign bag, then there is
a spanning labelled near-`K_7` model with the same path core, the same
four fixed endpoint-row edges, the same missed twin `D`, and deficient
bag `A-K`.

### Proof

The coherence theorem makes `A` anticomplete to `D`, so `K` has no edge
to `D`.  If `K` has an edge to `E`, put `T=E`; otherwise choose any
retained foreign bag `T` met by `K`.  Define

\[
                         A'=A-K,\qquad T'=T\cup K,        \tag{1.2}
\]

and leave every other bag unchanged.

The target bag `T'` is connected through the chosen `KT` edge.  The bag
`A'` is connected: it contains the connected path `P`, and every
remaining piece `K_j` is connected and attached to `P`.  The old `PK`
edge now runs between `A'` and `T'`.

All old foreign-foreign adjacencies survive because `T'` contains all of
`T`.  Every required `A'U_i` adjacency survives at its fixed endpoint
edge on `P`.  If `T=E`, the old `PK` edge supplies the required `A'E`
adjacency.  If `T!=E`, then `K` has no edge to `E` by the choice rule, so
removing `K` from `A` does not remove the old `AE` adjacency.  Finally
`A'D` remains absent because `A' subseteq A`.

The bags remain pairwise disjoint and their union is unchanged, so the
new model is spanning.  The path core and its endpoint edges were not
moved.  This proves the theorem. \(\square\)

## Corollary 2 (minimal deficient bag has only path-private lobes)

Among coherent spanning models satisfying (1.1), fix `P`, its endpoint
edges, and `D`, and minimize `|A|`.  Then every remaining piece satisfies

\[
                       N_G(K_i)\subseteq V(P).             \tag{2.1}
\]

If the host is seven-connected, every such piece has at least seven
distinct neighbours on `P`.

### Proof

Distinct pieces are anticomplete.  A piece has no neighbour in `D` by
the fixed missing pair.  If it met any other foreign bag, Theorem 1 would
strictly reduce `|A|`.  Its only remaining external neighbours are
therefore in `P`, proving (2.1).  The connectivity assertion follows
because `N_G(K_i)` separates the nonempty piece from the rest of the
spanning model.  The far side is nonempty: the fixed missed twin `D` is a
nonempty foreign bag and is anticomplete to `K_i`.  Hence
seven-connectivity gives `|N_G(K_i)|>=7`. \(\square\)

## Corollary 3 (no locked exterior carrier survives as an `A`-piece)

A crossing piece with portal families to foreign rows `H,Q` meets
retained foreign bags.  It is therefore absent in the minimal model of
Corollary 2.  This eliminates the entire four-connected/rank-four locked
carrier and, more strongly, its lower-connectivity and low-rank versions
**as auxiliary pieces of `A`** whenever they arise as one of the coherent
transported pieces in (1.1).

The operation does not delete the carrier or split it between `H` and
`Q`.  It puts all of it into one chosen target row `T`.  Contacts from the
absorbed piece to every other foreign bag are then merely old
foreign--foreign adjacencies.  They do not make a path side meet those
other rows.  Thus a two-row capacity collision can survive inside the
enlarged nonsingleton target bag and must be handled at the remaining
path interface.

The conclusion uses no palette-to-label inference and no unlabelled
minor operation.  It is a direct reassignment of actual vertices between
labelled branch bags.

## Remaining path interface

After all transfers, the only material of `A-P` consists of connected
lobes whose neighbourhood is contained in `P`.  Omitting those lobes
from the model leaves a nonspanning labelled one-missing near-clique
model with deficient bag exactly the induced path `P`; every transferred
piece remains inside one actual foreign bag and turns each of its old
`PK` attachments into a literal portal to **that chosen target row only**.
Its contacts to other foreign bags do not create additional row portals.

Thus the old portal-placement problem reduces to a path interface:
either one path edge has both sides meeting all five retained foreign
rows, giving the audited two-shore completion, or the five literal portal
sets of the enlarged, generally nonsingleton foreign bags have an ordered
interval obstruction.  Proper-minor colour states, possible collisions
inside those bags, and the path-private lobes still have to eliminate
that obstruction.
