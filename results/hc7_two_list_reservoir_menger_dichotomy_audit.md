# Independent audit: two-list singleton-reservoir Menger dichotomy

## Verdict

**GREEN** at frozen source SHA-256
`4adc0abf44f501a8784ebd892e6c3311f6b372f85be54dccb2f122712548d130`.

The abstract list theorem, its canonical atomic application, and the
four-label portal matching corollary are correct.  The theorem repairs the
old Helly argument and isolates its only missed case: a star whose every
list is the same singleton.

It does **not** decode the four labels into carriers or a rooted model.
The sign classes are component-orientation requirements, not carrier
labels, and the existing four-port theorem has a genuine disk outcome.

## 1. Orientation reduction

Fix bipartition parity `p`.  A proper two-colouring of a connected
component has the form

\[
                         c(v)=p(v)\mathbin{\mathsf{xor}}e
\]

for one orientation bit `e`.  A singleton list `{c(v)}` therefore forces
`e=c(v) xor p(v)`.  A component is list-colourable exactly when it does
not meet both `F_0` and `F_1`.

If there are no two disjoint `F_0-F_1` paths, set-Menger gives a transversal
of order at most one.  An empty transversal already makes `H`
list-colourable, and connectedness supplies an edge, hence both labels.  If
the transversal is `{x}`, every component of `H-x` is list-colourable.  An
edge again supplies both labels.  If no edge remains, connectedness makes
`H` a star.  Its isolated leaves can use both labels unless all their lists
are one common singleton; the original star then returns unless the centre
has that singleton too.  This proves exactly the source dichotomy.

## 2. Atomic application

For the canonical split `{z}|(A-z)`, the compulsory literal `u` is forced
to the first carrier, while root-deletion makes every member of
`W=S-{u}` able to use the second carrier.  Thus the uniform-singleton star
is impossible.  Failure of the adaptive return therefore supplies two
vertex-disjoint bad paths with four distinct literal endpoints for every
connected-bipartite frontier, including `C_6` with a pendant vertex.

The endpoint signs must not be renamed as carrier labels.  They are

\[
                    \text{forced label}\mathbin{\mathsf{xor}}
                    \text{bipartition parity}.
\]

Consequently a bad path need not join vertices forced to opposite
carriers.

## 3. Portal matching

For `Q' subseteq Q`, Hall failure gives
`|N_A(Q')|<|Q'|<=4`.  Since the live atom has `|A|>=4`, the set
`A-N_A(Q')` is nonempty.  The set

\[
                         (S-Q')\cup N_A(Q')
\]

has order at most six and separates it from the nonempty far shore,
contradicting seven-connectivity.  Hence the four labels have distinct
literal portals.  Forced labels have all portals on their forced side, so
the matching respects an actual carrier cut.

This SDR is useful but is not the safest way to invoke generalized webs:
applying Humeau--Pous to internal portals does not automatically eliminate
filled facial cliques, because all seven boundary vertices can contribute
external neighbours.  The already-audited artificial-root four-port
linkage-or-disk theorem clears those cliques with only three unrepresented
boundary vertices and should be used instead.

## 4. Trust boundary

The result proves the four-root certificate.  It does not prove that an
`st`-ordering forces the linkage outcome.  Maximal outerplanar fully crossed
shores give the disk branch.  The remaining theorem must decode both the
literal linkage and the literal disk into an adaptive carrier return or an
`S`-rooted `K_5`; no completion edge may be treated as a host edge.
