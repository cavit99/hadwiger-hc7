# Independent audit: uniform seven-root trichotomy

## Verdict

**GREEN after correction of the simultaneous-transfer interface.**  The
proof correctly applies the audited donor exchanges to an arbitrary
seven-vertex selection from a larger neutral separator.  It closes every
root distribution into `K_7`, an actual separator, or a labelled
deficiency rotation with a proper neutral subbag as centre.

## Checks

1. Every neutral bag contains a selectable root because `X` meets it.
   Seven selected roots across four nonempty bags have either surplus in
   at least two donors or all three surplus roots in one donor; there is
   no third distribution type.
2. In the multi-donor case, the row-core/opposite-root theorem gives a
   monopoly-free piece or an advertised separator/rotation.  A
   monopoly-free piece missing one twin itself has an actual separator,
   so outside that output it meets both and supports either target.
   Distinct donors make the pieces disjoint, but that alone does not make
   simultaneous transfer faithful: both old donor--donor edges might end
   in moved pieces.  The corrected proof checks the two residual donors.
   If they are adjacent, the transfer is faithful; if they are
   anticomplete, one residual donor's open neighbourhood is an actual
   separator with the other on a far side.
3. After transfer, all six old clique bags contain distinct selected
   roots.  Since every selected root lies in `N(X)`, the connected set
   `X` is adjacent to every rooted bag and is a valid seventh branch set.
4. In the one-donor case, the spanning-tree lemma supplies three connected
   rooted parts and literal central cut edges.  If moved parts meet both
   twins, the six proposed foreign bags around `U_0` are pairwise
   adjacent.  Exactly zero, one, or two lost untouched-neutral contacts
   give `K_7,K_7^-,K_7^vee`; losing all three makes any missed neutral bag
   a far side of `N(U_0)`.
5. Every separator output is actual because a whole connected old bag is
   anticomplete to the displayed connected near side.  Seven-connectivity
   gives its lower bound.  Fullness is claimed only at exact order seven.
6. The proof never assumes that unselected vertices of a larger `S` are
   deleted or belong to branch bags.  They may simply remain unused in a
   minor model.  Hence the selection works unchanged for `|S|>7`.
7. Every separator output comes with a named connected near side and a
   whole old bag on a far side.  Therefore the equality-partition
   extension sets are defined on an actual separation.  Standard
   proper-minor criticality gives the stated one-side transition, and
   equality with an opposite-operation partition permits colour-name
   permutation and gluing.  No fullness assumption is used for this
   state interface.

## Scope

The word “rotation” is not termination.  The new deficient centre is a
proper part of an old neutral bag, but no global potential has yet been
proved to decrease across successive rotations, and a separator of order
greater than seven is not automatically colour-gluable.  Those are the
exact remaining gaps.
