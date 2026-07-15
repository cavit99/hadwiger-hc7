# Two-list singleton-reservoir Menger dichotomy

**Status:** proved and independently audited.

This note repairs the first combinatorial step of the atomic fully crossed
programme.  The earlier path-Helly formulation missed one genuine
degeneracy.  The correct proof is a set-Menger argument and works for every
connected bipartite frontier, not only for trees.

## 1. Abstract theorem

Let `H` be a connected bipartite graph of order at least three.  Give every
vertex a nonempty list

\[
                     \Lambda(v)\subseteq\{0,1\}.
\]

Call a set `U` an adaptive singleton reservoir when `|U|<=1` and `H-U`
has a proper `Lambda`-list-colouring which uses both labels.

Fix a bipartition parity `p:V(H)->{0,1}`.  A vertex with singleton list
`{c}` demands the component orientation

\[
                         \theta(v)=c\mathbin{\mathsf{xor}}p(v).
\]

Put `F_i={v:Lambda(v)={i xor p(v)}}`.  A **bad path** is an
`F_0-F_1` path.

### Theorem 1.1

Exactly one of the following obstructions is needed when no adaptive
singleton reservoir exists:

1. `H` contains two vertex-disjoint bad paths; or
2. `H` is a star and every vertex has the same singleton list.

Equivalently, if neither obstruction occurs, an adaptive singleton
reservoir exists.

#### Proof

In every connected component of a bipartite graph, a proper two-colouring
is determined up to reversal.  A singleton-list vertex `v` requires that
component's reversal bit to equal `theta(v)`.  Hence `H-U` is
`Lambda`-list-colourable if and only if no component of `H-U` contains both
an `F_0` vertex and an `F_1` vertex.

Suppose there are no two vertex-disjoint bad paths.  The vertex form of
Menger's theorem for paths between two sets supplies a set `X` of order at
most one meeting every `F_0-F_1` path.  If `X` is empty, `H` itself is
`Lambda`-list-colourable; since it is connected and has an edge, that
colouring uses both labels.  We may therefore write `X={x}`.  No component
of `H-x` contains both terminal types, so `H-x` is
`Lambda`-list-colourable.

If `H-x` contains an edge, every proper two-colouring of its component uses
both labels, so `U={x}` is an adaptive reservoir.  Suppose instead that
`H-x` is independent.  Since `H` is connected, `H` is a star with centre
`x`.  Because at least two vertices survive, a list-colouring of `H-x`
fails to use both labels only when all surviving lists are the same
singleton, say `{c}`.  If `1-c` belonged to `Lambda(x)`, assigning `1-c`
to the centre and `c` to every leaf would be a proper list-colouring of
`H` using both labels.  Thus total failure forces
`Lambda(x)={c}` as well.  This is outcome 2.

Conversely, if a star has the same singleton list at every vertex, deleting
the centre leaves only that one label, while deleting any other vertex (or
none) leaves a monochromatic edge.  It has no adaptive singleton
reservoir.  This proves the theorem. `square`

## 2. Canonical atomic consequence

Use the canonical atomic split

\[
                         C_0=\{z\},\qquad C_1=A-z
\]

in the connected-bipartite exact-seven cell.  Root-deletion gives that
`C_1` is connected and contacts every member of `W=S-{u}`; the compulsory
edge `zu` is the unique `A-u` edge.  Thus

\[
 \Lambda(u)=\{0\},\qquad
 1\in\Lambda(w)\quad(w\in W),
\]

with `0 in Lambda(w)` exactly when `z` contacts `w`.

### Corollary 2.1

If the canonical split does not already invoke the audited adaptive
clique-reservoir return theorem, then `H=G[S]` contains two vertex-disjoint
bad paths and hence four distinct literal boundary endpoints.

#### Proof

The monochromatic-star outcome of Theorem 1.1 is impossible: `u` is forced
to carrier zero, whereas every member of `W` can use carrier one.  Therefore
failure of the adaptive return gives outcome 1. `square`

The signs `F_0,F_1` are orientation demands, not carrier labels.  In
particular, the four endpoints need not consist of two vertices forced to
each carrier.  They are four distinct boundary literals, but chosen portal
witnesses in `A` need not initially be distinct.

### Corollary 2.2 (four literal labels have distinct portals)

Assume `|A|>=4`.  Every four-set `Q subseteq S` has a matching into `A`
along literal boundary--shore edges.

#### Proof

If Hall's condition failed, some nonempty `Q' subseteq Q` would satisfy

\[
                         |N_A(Q')|<|Q'|.
\]

Since `|Q'|<=4` and `|A|>=4`, the set `A-N_A(Q')` is nonempty.  Now

\[
                         (S-Q')\cup N_A(Q')
\]

has order at most `7-|Q'|+|N_A(Q')|<=6` and separates that nonempty set
from the nonempty far shore `R`: there is no `A-R` edge, every
`A-Q'` edge ends in `N_A(Q')`, and the rest of `S` was deleted.  This
contradicts seven-connectivity. `square`

If a boundary label is forced to one side of an actual carrier partition,
all of its portals lie on that side, so the matching respects those forced
sides.  This observation removes portal collision when a theorem genuinely
needs four distinct internal representatives.  It does not license the use
of completion edges or clear the fill cliques of a web obtained from those
internal portals.

## 3. What this does and does not prove

The corollary legally produces the four literal roots needed for the
audited seven-boundary four-port linkage-or-disk theorem.  That theorem may
be applied directly to the roots, so shared internal portal witnesses do
not invalidate the call.

It returns either two literal disjoint paths through `A` or a literal disk
embedding with the four roots in the prescribed order.  Neither outcome is
yet an admissible carrier allocation or an `S`-rooted `K_5`.  Decoding that
linkage/disk dichotomy is the next geometric theorem; it may not be replaced
by identifying the orientation signs with carrier names or by treating a
web-completion edge as a host edge.

## 4. Exact verification

`active/hc7_two_list_reservoir_obstruction_check.py` independently exhausts
all `3^7` nonempty list assignments on every seven-vertex tree and on the
six-cycle with one pendant vertex.  It reports

```text
TWO_LIST_DICHOTOMY checked 26244 no_return 8086
disjoint_bad 8084 monochromatic_star 2 unresolved 0
```

The computation is verification evidence only; the proof of Theorem 1.1
is uniform and does not depend on it.
