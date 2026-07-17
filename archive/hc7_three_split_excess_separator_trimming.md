# Trimming excess separators around three split models

## Status

Proved, pending independent audit.

This note extends the exact bundle-separator handoff from expanded order
seven to expanded orders eight and nine whenever the excess boundary
vertices can be assigned to the appropriate model shore.  It does not
infer a labelled assignment from mere colour contacts.  Instead it gives
an exact, finite obstruction: at order eight every boundary atom is locked,
and at order nine the movable atoms have compatibility number at most one.

The statement is independent of colouring and contraction-criticality.

## 1. Setup

Let `G` contain three pairwise vertex-disjoint support-six `K_5` models

\[
 M_i=Q_i\mathbin{\dot\cup}\{x_i,y_i\},\qquad i=1,2,3,
\]

where `Q_i` consists of four singleton bags and `x_i y_i` is the unique
two-vertex bag.  Contract the three split edges, write `z_i` for the image
of `x_i y_i`, and put

\[
 H=G/x_1y_1/x_2y_2/x_3y_3,
 \qquad L_i=Q_i\cup\{z_i\}.
\]

Thus the `L_i` are pairwise disjoint literal `K_5` cliques.  Let `T` be a
separator of `H`, put

\[
 I(T)=\{i:z_i\in T\},\qquad \rho(T)=|I(T)|,
\]

and let

\[
 T^+=\bigl(T-\{z_1,z_2,z_3\}\bigr)
       \cup\bigcup_{i\in I(T)}\{x_i,y_i\}.
\]

Then `|T^+|=|T|+rho(T)`.  The components of `H-T` expand bijectively to
the components of `G-T^+`.

Fix a nontrivial bipartition `(mathcal A,mathcal B)` of those components,
and let `A_0,B_0` be the corresponding unions of expanded components in
`G-T^+`.

Every vertex of `T^+` is called a **boundary atom**.  Atoms in
`Q_i cap T` and the two atoms `x_i,y_i` when `z_i in T` are owned by
model `i`; all other atoms are unowned.  Since the three models are
vertex-disjoint, ownership is unique.

For every `i`, all vertices of `M_i-T^+` lie in at most one component of
`G-T^+`.  If this set is nonempty, orient model `i` toward the side
containing it.  If it is empty, choose either side as its orientation.

## 2. Carrier-compatible atoms

An owned atom is **movable** when it has no neighbour in the open side
opposite its model orientation.  Its only permitted destination is the
oriented side.  An unowned atom is movable to `A_0` when it has no
neighbour in `B_0`, and movable to `B_0` symmetrically.

A set `R subseteq T^+` is **carrier-compatible** if every member is
movable with a selected permitted destination and

\[
 E_G(R_A,R_B)=\varnothing,                              \tag{2.1}
\]

where `R_A,R_B` are the atoms selected for the two respective sides.
Atoms owned by one model automatically have the same permitted
destination.  Condition (2.1) is needed only for atoms with opposite
destinations.

### Theorem 2.1 (excess-boundary trimming)

Let `R` be carrier-compatible.  Then

\[
 S=T^+-R                                                   \tag{2.2}
\]

is the boundary of a separation of `G` with open shores

\[
 A_0\cup R_A,\qquad B_0\cup R_B.                          \tag{2.3}
\]

Both open shores are nonempty, and each named model `M_i` is contained
in one of the two closed shores.  In particular, if

\[
 |R|=|T|+\rho(T)-7,                                       \tag{2.4}
\]

then (2.2) is a model-preserving actual exact-seven separation.

#### Proof

There is no edge between `A_0` and `B_0`, because they are unions of
distinct components of `G-T^+`.  A member of `R_A` has no neighbour in
`B_0`, and a member of `R_B` has no neighbour in `A_0`, by movability.
Condition (2.1) excludes the only remaining possible edge between the two
sets in (2.3).  Thus (2.2)--(2.3) define a separation.  Both original
component classes were nonempty, so moving boundary atoms cannot empty
either open shore.

Fix `i`.  The clique `L_i-T` lies in at most one component of `H-T`.
After expansion, `M_i-T^+` therefore lies in at most one component of
`G-T^+`.  Every moved atom owned by `i` was put on that same oriented
side (or on the one side chosen when the residual model was empty), and
every unmoved atom remains in `S`.  Hence the whole carrier `M_i` lies in
one closed shore.  Formula (2.4) and
`|T^+|=|T|+rho(T)` give `|S|=7`.  \(\square\)

### Corollary 2.2 (the complete numerical residue)

Assume `G` is seven-connected and `|T|<=6`.  Then

\[
 7\le |T|+\rho(T)\le9.                                   \tag{2.5}
\]

Expanded order seven is the previously proved exact handoff.  At expanded
order eight, one movable atom gives the exact handoff.  At expanded order
nine, any compatible pair of movable atoms gives the exact handoff.

Consequently, if no model-preserving exact-seven handoff is available,
the only excess types and locks are

\[
\begin{array}{c|c|c}
(|T|,\rho(T))&|T^+|&\text{necessary lock}\\ \hline
(5,3),(6,2)&8&\text{no movable boundary atom},\\
(6,3)&9&\text{no carrier-compatible pair of movable atoms}.
\end{array}                                               \tag{2.6}
\]

#### Proof

The lower bound in (2.5) is the anchored-separator law: `T^+` separates
the seven-connected graph `G`.  The upper bound follows from
`|T|<=6` and `rho(T)<=3`.  Theorem 2.1 gives the assertions at orders
eight and nine.  Solving `|T|+rho(T)=8,9` under the same bounds gives
exactly (2.6); equality seven gives `(4,3),(5,2),(6,1)`.  \(\square\)

## 3. Global component-contact consequences

The lock in (2.6) is stronger than a statement about one chosen pair of
shores.  Apply it to the bipartition consisting of one component `C` of
`H-T` against all the others.  For a hit model `i`, call the component
containing `Q_i-T` its **core component**, when `Q_i-T` is nonempty.

### Corollary 3.1 (order-eight all-component lock)

Suppose `|T^+|=8` and no model-preserving exact-seven handoff exists.
Then every hit endpoint `x_i,y_i` has a neighbour in every component of
`H-T` other than its core component.  It also has a neighbour outside its
core component whenever that component exists and there is another
component.

The same assertions hold for every ordinary atom owned by a model.  Every
unowned ordinary atom has neighbours on both sides of every nontrivial
bipartition of the components.

#### Proof

Let `C` differ from the core component of model `i`, and orient the model
toward the complementary union which contains its core.  If an owned atom
had no neighbour in `C`, it would be movable, contrary to (2.6).  If `C`
is the core component, orient toward `C`; nonmovability says that the atom
has a neighbour in the complementary union.  An unowned atom which misses
one side is movable to the other.  \(\square\)

### Corollary 3.2 (order-nine pairwise lock)

Suppose `|T^+|=9` and no model-preserving exact-seven handoff exists.  Fix
a component `C` of `H-T`.

1. Among atoms whose model cores lie outside `C`, at most one can miss
   `C`.
2. Among atoms whose model cores lie in `C`, at most one can miss the
   union of the other components.
3. If one atom of each kind has the indicated missing contact, the two
   atoms must be adjacent.

The clauses include unowned atoms after choosing their permitted side.

#### Proof

Two atoms in clause 1 would both be movable toward the complementary
side, and two atoms in clause 2 would both be movable toward `C`.  In
either case they have the same destination and hence form a compatible
pair, contrary to (2.6).  In clause 3 the destinations are opposite, so
the pair fails compatibility only if its two members are adjacent.  \(\square\)

## 4. What remains

The theorem eliminates all excess RST separators except the literal
two-sided locks in Corollaries 3.1 and 3.2.  Those locks are global across
the component partition: they cannot be represented by choosing one
portal in one shore.

What is not proved is that a locked order-eight or order-nine separator
contains a `K_7` model.  Seven-connectivity supplies the displayed
contacts, but does not by itself identify those contacts with the four
singleton rows inside each normalized model.  This is precisely the
remaining palette-to-labelled-carrier gap.  Any completion of the
three-model theorem must now decode one of the two uniform contact locks,
not another list of local portal arrangements.
