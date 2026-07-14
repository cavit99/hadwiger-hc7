# Atomic blocking path and packet escape

**Status:** partial constructive result.  Sections 2--5 are proved.  They
do not close the atomic cell.  Section 6 identifies the first exact
noncommuting-state obstruction.

## 1. Frozen atomic setup

Retain the atomic setup of
`../results/hc7_compulsory_portal_atomic_state_exchange.md` and
`../results/hc7_compulsory_portal_bridge_composition.md`.  Thus

\[
 S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

the thin shore `A` is connected and `S`-full, the rich shore `R` is
connected and contains two disjoint `S`-full packets, and `zu` is the
unique `A-u` edge.  There is no `A-R` edge.  Every proper minor is
six-colourable.

Use the audited width-two partition

\[
 S=I\mathbin{\dot\cup}J\mathbin{\dot\cup}K,            \tag{1.1}
\]

where `I,J` are independent, `u in I`, both `I,J` have order at least
two, and `K` is empty or a singleton clique.  The last size assertion is
proved in the audit of the atomic state-exchange theorem.

The original trace theorem contracts `A union I`.  In a counterexample it
returns a colouring with `I` exact and a literal blocking path in `R`
between two `J`-blocks, or from the possible singleton in `K` to a
`J`-block.

## 2. The blocking state is genuinely high demand

### Lemma 2.1

In a hypothetical counterexample, whenever the block-Kempe procedure of
the atomic trace theorem stops at a path, its current exact boundary state
`Pi` has packet demand at least three.

### Proof

All preceding Kempe swaps are legal colourings of `G[R union S]` and
preserve the exact current state.  If `d_{G[S]}(Pi)<=2`, the two disjoint
`S`-full packets in `R` reproduce exactly `Pi` on `G[A union S]` by the
audited adaptive packet-reflection theorem.  Palette alignment then glues
the two closed-shore colourings, since there is no `A-R` edge.  This would
six-colour `G`.  Hence a live blocking state has demand at least three.
`square`

Thus the path is not merely an unfortunate early choice in a state which
the existing packet theorem could already reflect.

## 3. The opposite trace exists as well

### Theorem 3.1 (bilateral trace obstruction)

In a hypothetical counterexample there are two independently attained
trace colourings of the rich closed shore:

1. one has `I` as an exact block and supplies a literal path in `R`
   between two distinct `J`-blocks, or from `K` to a `J`-block; and
2. one has `J` as an exact block and supplies a literal path in `R`
   between two distinct `I`-blocks, or from `K` to an `I`-block.

Every internal vertex of both paths lies in `R`.  The two paths need not
belong to the same colouring, be disjoint, or meet the same packets.

### Proof

The first assertion is the audited atomic trace-exchange theorem.

For the second, interchange the roles of `I,J`.  The set `A union J` is
connected because `A` is connected and `S`-full, while `J` is independent.
Contract a spanning tree of this set.  A six-colouring of the proper minor,
restricted to `R union S` and expanded only over the literal vertices of
`J`, makes `J` one exact equality block: the contracted representative is
adjacent to every member of `S-J` by fullness of `A`.

Both `I` and `J` have order at least two, so the reservoir-detachment and
block-Kempe proof of the atomic theorem applies verbatim with their names
interchanged.  If it compresses all `I`-blocks, the resulting state is

\[
                         J\mid I
 \quad\hbox{or}\quad J\mid I\mid K,
\]

and has demand at most two.  Packet reflection and gluing then
six-colour `G`.  Otherwise the shortest two-colour path returned by the
proof has its internal vertices outside `S`, hence in `R`, and has one of
the two forms in item 2.  `square`

This is a real strengthening of the one-sided trace theorem: a survivor
has a blocking connection on each bipartition duty.  It is not yet a
two-linkage, because the witnesses come from unrelated proper-minor
colourings.

## 4. What geometric first-hit surgery does give

Enlarge the two old packets to an adjacent connected cover

\[
                         R=P\mathbin{\dot\cup}Q
                                                               \tag{4.1}
\]

using the audited adjacent-cover lemma.

### Lemma 4.1 (monotone packet path)

For any literal `x-y` path whose internal vertices lie in `R`, there is an
`x-y` path with internal vertices in `R` whose packet-membership word under
(4.1) is one of

\[
                         P,\quad Q,\quad PQ,\quad QP. \tag{4.2}
\]

In particular it crosses the literal `P-Q` cut at most once.

### Proof

Choose an `x-y` path minimizing the number of transitions between `P` and
`Q`, and then its length.  If its membership word contains `PQP`, take the
subpath between the first and last displayed `P` vertices.  Since `G[P]`
is connected, replace that subpath by a path in `P`, and simplify the
resulting walk.  This strictly reduces the number of transitions.  The
same argument excludes `QPQ`.  Any binary word avoiding both alternating
subwords has at most one transition, giving (4.2).  `square`

The replacement is a literal carrier path, but generally is not
bichromatic in the trace colouring.  Therefore Lemma 4.1 is valid for
branch-set surgery and invalid as a state-preserving Kempe replacement.
This is the precise limit of cover enlargement alone.

## 5. The two commuting carrier contractions

Assume first that the blocking outcome has the duty--duty form.  Let `Pi`
be that blocking state, let `B,C` be its two named `J`-blocks, and put
`D=B union C`.  Then `D` is independent because `D subseteq J`.  Choose
any connected `S`-full set `F subseteq R` containing the blocking path;
taking `F=R` is always legal.  (A reservoir--duty path need not make the
union of its two whole equality blocks independent, so the contraction
below is deliberately not asserted for that outcome.)

The sets

\[
                         X=A\cup I,\qquad Y=F\cup D    \tag{5.1}
\]

are disjoint and connected.  Hence their contractions commute as graph
operations:

\[
                    (G/X)/Y=(G/Y)/X.                  \tag{5.2}
\]

In `G/X`, restriction to the rich closed shore makes `I` exact.  In
`G/Y`, restriction to the thin closed shore makes `D` exact, because `F`
is `S`-full.  Define

* `T_X` to be the set of exact partitions of `S` returned on
  `G[R union S]` by six-colourings of `G/X`; and
* `T_Y` to be the set of exact partitions of `S` returned on
  `G[A union S]` by six-colourings of `G/Y`.

### Lemma 5.1 (state-language separation)

In a hypothetical counterexample,

\[
                              T_X\cap T_Y=\varnothing. \tag{5.3}
\]

### Proof

An element of the intersection gives proper six-colourings of the two
literal closed shores with the same exact equality partition on `S`.
Permute one palette so corresponding block colours agree.  The colourings
then glue over `S`, since there is no `A-R` edge, producing a six-colouring
of `G`.  `square`

Equation (5.3), not failure of the graph contractions to commute, is the
actual obstruction in the duty--duty case.  A colouring of the double
contraction in (5.2) does not lift through either contracted carrier and
therefore need not produce an element of `T_X` or `T_Y`.

## 6. Why the bridge locks do not yet repair the square

The exact `I`-trace contraction necessarily uses the compulsory bridge
`zu`.  Indeed, after deleting `zu`, the vertex `u` is isolated from
`A union (I-{u})` inside the intended contraction set: `zu` is the unique
`A-u` edge and `I` is independent.  Consequently

\[
                         (A\cup I)-zu
\]

is disconnected, so the exact trace contraction is not a legal connected
contraction in `G-zu`.

By contrast, the five exact Kempe locks live in six-colourings of
`G-zu`.  Thus criticality currently supplies:

* a blocking path in a colouring after contracting the bridge-containing
  carrier `A union I`; and
* five locked `z-u` paths in a different colouring after deleting that
  same bridge.

It supplies no legal colouring in which both structures coexist.  This is
the first exact noncommuting-state obstruction:

\[
 \boxed{
 \text{the trace contraction needs }zu,
 \quad
 \text{the Kempe locks need }G-zu,
 \quad
 \text{and the common state languages in (5.3) are disjoint.}}
                                                               \tag{6.1}
\]

The newly audited two-carrier list theorem sharpens the geometric side but
does not remove (6.1).  If a literal split `C_1,C_2 subseteq A` is found,
the connected bipartite frontier has only one parity bit to repair; a legal
piece reassignment closes exactly when its affected portal set hits the
conflicting forced orientation.  The blocking path lies wholly in `R`, so
it changes none of those literal `A`-carrier lists.  It helps only if a
fan or bridge rotation lifts it to an actual connected reassignment inside
`A`.

Accordingly the first still-unproved implication is now narrowly stated:

> Convert one of the two rich-shore blocking paths of Theorem 3.1, together
> with the saturated bridge fan, into a legal literal reassignment of two
> adjacent carriers in `A` whose affected set repairs the single frontier
> parity bit; or decode the failed lift as a labelled near-`K_7` model or a
> strict exact-seven descent.

Neither a monotone path in the packet cover nor the commuting minor square
alone transports the exact trace.  Claiming packet escape from either
would conflate graph-minor commutation with colouring-state pullback.
