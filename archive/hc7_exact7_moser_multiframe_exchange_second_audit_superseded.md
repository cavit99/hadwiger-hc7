# Superseded second audit: pure-Moser four-corner exchange

Audited file: `active/hc7_exact7_moser_multiframe_exchange.md`.

**Verdict:** **GREEN in the intended exact two-component, seven-connected
HC7 setting, subject to the two hypothesis clarifications in Section 1.**

The strengthened Theorem 4.1 is valid.  A single application of the audited
four-port theorem to the ordered literal roots `1,2,3,4` returns one of two
complementary carrier matchings, and the exact-state argument closes either
matching.  It no longer depends on synchronizing several independently
chosen rural embeddings.

## 1. Two hypotheses that should be literal in the statement

The proof uses both of the following facts.

1. `C,D` are **all** of the exterior: one should write

   \[
                     G-N[v]=C\mathbin{\dot\cup}D.
   \]

   Merely assuming that `C,D` are two among possibly more exterior
   components would not suffice, because the two closed-shore colourings in
   Section 3 would not cover the omitted components of `G-v`.  The title,
   setup, and intended “two-component Moser cell” all impose the exact
   equality, but the sentence “has two ... components `C,D`” should be made
   unambiguous.

2. Seven-connectivity is used in Lemma 2.1 and in the four-port theorem.
   It follows from the audited minimal-HC7 kernel (Mader's connectivity
   theorem for the noncomplete contraction-critical graph), but a
   self-contained local statement should either assume that `G` is
   seven-connected explicitly or cite this dependency at the start.

With these intended hypotheses, both exterior components are connected,
anticomplete, and `S`-full.  Fullness follows because if one component
missed a literal `s`, the other component together with `v` would lie beyond
the at-most-six separator `S-{s}`.

## 2. Literal rural carrier lemma

For the order `(a,x,b,y)` with `{a,x}={1,2}` and `{b,y}={3,4}`, the two
portal-union estimates are correct.  If, for example,

\[
                 |N_D(\{a,x\})|\leq1,
\]

then

\[
                 N_D(\{a,x\})\cup(S-\{a,x\})
\]

has order at most six.  Since `|D|>=4`, the set left in
`D-N_D({a,x})` is nonempty; it has no edge to the surviving literals
`a,x`, to `v`, or to `C`.  The displayed set is therefore a genuine cut.
The argument for `{b,y}` is identical.

The literal edges `ax=12` and `by=34`, together with the two union-rank
conditions, satisfy the audited two-ear lemma and make

\[
                 Q=G[D\cup\{a,x,b,y\}]
\]

two-connected.  In the supplied disk embedding, the outer-face boundary is
therefore a simple cycle.  In cyclic order `a,x,b,y`, the consecutive pairs
`a-y` and `x-b` are Moser nonedges.  Their two open outer-face arcs are
disjoint, have nonempty connected interiors in `D`, and contact exactly the
required endpoint pairs.  A shortest path inside connected `D` enlarges one
interior until the two carriers are adjacent, without losing disjointness or
any portal contact.  This proves carrier hypothesis (2).

It is important that this is a **literal disk embedding of one four-root
closure**, not an inference from four cyclic portal labels alone.  The
audited four-port theorem supplies exactly that object in its rural outcome.

## 3. First proper minor and the complete return-state list

For any allowed orientations, put

\[
 r=\{a,y\},\qquad e=\{x,b\}.
\]

Both are independent because the Moser boundary has no `L-R` edge.  The
sets `{v} union r` and `C union e` are disjoint and connected; the latter
uses connectedness and `S`-fullness of `C`.  They are adjacent through a
`v-e` edge, and their simultaneous contraction is a proper minor.

After six-colouring that minor, delete the connector vertices and pull back
only to the unchanged closed `D`-shore.  Expanding `r,e` is legitimate
because they are independent.  The representative of `{v} union r` sees
every literal in `S-r` through `v`, while the representative of `C union e`
sees every literal in `S-e` through fullness of `C`.  Consequently `r,e`
are distinct exact colour blocks and neither colour occurs on `0,5,6`.

The only edge in `G[{0,5,6}]` is `56`.  Thus the equality partition on
literal `S` is exactly one of

```text
R0 = r | e | 0  | 5 | 6
R5 = r | e | 05 | 6
R6 = r | e | 06 | 5.
```

There is no fourth case: `5` and `6` have distinct colours, and `0` either
uses a third colour or exactly one of theirs.

## 4. Reflection minor and carrier adjacencies

The contraction sets

\[
                 X\cup r,\qquad Y\cup e,
                 \qquad \{v\}\cup I_q
\]

are pairwise disjoint and connected.  The first two are adjacent by the
carrier edge.  Every carrier block contains one `L` corner and one `R`
corner, so each sees literal `6` through its `L` corner and literal `5`
through its `R` corner.  The star representative sees the other blocks and
remaining literals through `v`.

The forcing cliques are therefore literal:

* for `q=0`, `X+r`, `Y+e`, `v+0`, `5`, `6` form a `K5`;
* for `q=5`, `X+r`, `Y+e`, `v+{0,5}`, `6` form a `K4`; and
* for `q=6`, `X+r`, `Y+e`, `v+{0,6}`, `5` form a `K4`.

The remaining boundary blocks `13`, `14`, `23`, `24`, `05`, and `06` that
occur in the two possible matchings are all independent when used.  After
restricting to the unchanged closed `C`-shore, the relevant independent
blocks can therefore be expanded safely.  The displayed clique makes the
boundary equality partition exactly `R_q`, rather than merely a coarsening.

Choosing the returned `q`, a permutation of the six colour names aligns the
two exact partitions vertex by vertex.  Since `C,D` are anticomplete, the
colourings glue on all of `G-v`.  Every `R_q` uses at most five colours on
`S`, so an unused sixth colour is available for `v`.  This is the claimed
six-colouring contradiction.

## 5. Audit of the single four-port application

Apply the already-GREEN seven-boundary four-port linkage-or-disk theorem to

\[
                           (1,2,3,4).
\]

Its far-side hypothesis holds because `C union {v}` is nonempty, and every
root has a neighbour in the `S`-full component `D`.

### Linkage outcome

The theorem returns disjoint paths `P_13,P_24` with interiors in `D`.
The literal edges `13,24` are absent, so both interiors are nonempty.
Adjacent enlargement in connected `D` gives carriers contacting

\[
                          13\mid24.
\]

Take `(a,x)=(1,2)` and `(b,y)=(4,3)`.  Then

\[
                  r=\{a,y\}=13,\qquad e=\{x,b\}=24,
\]

so Sections 3--4 apply exactly.

### Rural outcome

The theorem returns one literal disk embedding of
`G[D union {1,2,3,4}]` in cyclic order `1,2,3,4`.  Lemma 2.1, with

\[
                     (a,x,b,y)=(1,2,3,4),
\]

gives carriers contacting

\[
                          14\mid23.
\]

Here `r=14` and `e=23`, so the same exact-state argument applies.

Thus the two exhaustive outcomes are precisely the two perfect matchings

\[
                    (13\mid24)\quad\text{and}\quad(14\mid23),
\]

and both are funded by the same state-reflection mechanism.  No favourable
five-root crossing, sign comparison, or compatibility of several disk
embeddings is required.  This directly repairs the gap identified in the
first multiframe audit; that older gap applied to the previous attempted
multi-embedding extraction, not to strengthened Theorem 4.1.

## 6. Dependencies and the tiny-shore reduction

The strengthened theorem depends on:

1. the audited minimal-HC7 facts that `G` is seven-connected and every
   proper minor is six-colourable;
2. the GREEN seven-boundary four-port linkage-or-disk theorem in
   `results/hc7_moser_crossing_carrier.md`;
3. the GREEN two-ear and consecutive-facial-carrier lemmas in
   `results/hc7_exact7_moser_3connected_web_exchange.md`; and
4. only elementary palette permutation and gluing across the exact
   two-component separation.

There is no new computational input in Theorem 4.1.

Combining it with the independently audited pure-Moser low-cut theorem is
legitimate.  That theorem says that, in this exact two-component cell, each
exterior component of order at least four has no cutvertex or two-cut and is
therefore three-connected.  Strengthened Theorem 4.1 says that the presence
of even one such component is impossible.  Hence a surviving pure-Moser
two-component configuration must satisfy

\[
                           |C|\leq3,qquad |D|\leq3.
\]

This last reduction is conditional on the already-audited, computer-assisted
low-cut theorem and inherits its finite-certificate trust boundary.  It does
not itself eliminate the tiny components, and it should not be quoted for a
general exact `(1,2)` adhesion with a different exterior-component
decomposition.
