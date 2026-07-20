# Independent audit: small-side closure in the endpoint-reversal case

**Verdict: GREEN.**  This is a separate internal mathematical audit, not
external peer review.  The promoted source
[`hc7_order8_strict_reversal_small_side_closure.md`](hc7_order8_strict_reversal_small_side_closure.md)
has SHA-256

```text
f69a8b40e92c200b22b4d0afb566c00ba1711d3c046d9b18bdb01e16df3392d4
```

The underlying mathematical revision checked independently had SHA-256
`9d6a600a705a1da3e5f3b9e10b68d2b4b5f75f260f47c32feea1e4a732270e28`.
The intermediate revision
`c71bc3539ff6efb9a7e96d3000419a73ef0b50a307a17b386613922ff9d62345`
changed only the opening status from audit pending to GREEN.  The current
revision adds the adjacent-audit link and reflows the following scope
sentence.  No hypothesis, conclusion, proof step, or trust boundary changed.

The audit treats the nonexistence of the split boundary colouring (1.3) as
an explicit additional hypothesis of the theorem's setting.  That
nonexistence is not a conclusion of the cited symmetric-allocation theorem.
With this scope understood, no mathematical gap was found.

## 1. Audited inputs

The following cited inputs were checked at their current revisions and
against their adjacent GREEN audits:

- the symmetric allocation theorem at
  `5a506ab80f1a32a0d0e7097c248c626369a16a28cad044e19f4bd220ca8a4335`;
- the generic exact-seven response restart at
  `e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a`;
- the small-boundary lobe descent at
  `de980671b3053459e4e11845e510e5d96bb0a4f18d1a8bd50fe4b9dfae996d52`;
  and
- the two-full-shore boundary-absorption theorem at
  `f66559a43b49cdf77963f3dd64066f71da9defd69a111107e030e5a626602d8d`.

The exact endpoint-reversal data imply that the neighbours of `a` outside
`D` are precisely `b,d,x_d,y_d`, while those of `b` outside `D` are
precisely `a,c,d`.  Minimum degree seven therefore gives

\[
                         |N_D(a)|\ge3,
                 \qquad |N_D(b)|\ge4.
\]

The normalization also makes `D` anticomplete to `d`, `E` anticomplete to
`e`, and makes every portal set used later nonempty.

## 2. Lemma 2.1: every three-colourable `D`

The proposed colouring works for a three-colourable `G[D]` of arbitrary
order.  It uses four distinct boundary colours on

```text
X, Y, d, e
```

and the two remaining colours together with the colour of `d` on `D`.
This is proper because `D` is anticomplete to `d`, while neither remaining
colour appears on the boundary.

The colouring of the path `a-b-c` is also proper:

- `a,c` are nonadjacent and receive the colour of `e`; `E` is anticomplete
  to `e`, and `D` does not use that colour;
- `b` receives the colour of `X`; the exact singleton portal equations
  show that `b` has no neighbour in `X`, and `D` does not use that colour;
  and
- the two path edges and every `E`--`D` edge have differently coloured
  ends.

Thus the construction really is a proper colouring of the whole closed
shore `G[L union S]`, and its exact boundary equality partition is

\[
                     X\mid Y\mid\{d\}\mid\{e\}.
\]

It contradicts precisely the explicitly assumed rejection of (1.3).
Consequently a survivor has `chi(G[D])>=4`; the cited known case `HC_4`
then gives a `K_4` minor in `G[D]`.  No later argument incorrectly treats
that minor as a `K_4` subgraph.

## 3. Theorem 2.2: the `K_4` matching branch

If `|D|<=4` and `G[D]` is not `K_4`, then it is three-colourable and
Lemma 2.1 applies.  In the remaining case `G[D]=K_4`, failure of a matching
from the four vertices of `D` to
four distinct boundary neighbours gives a nonempty `U subseteq D` with

\[
                         |N(U)\cap S|\le |U|-1.
\]

There are no `D`--`R` edges.  Since `D` is a clique, every possible
neighbour of `U` lies in

\[
            (D-U)\cup E\cup(N(U)\cap S),
\]

whose order is at most

\[
                  (4-|U|)+3+(|U|-1)=6.
\]

The connected nonempty set `U` and the nonempty old opposite shore give a
genuine separation, contradicting seven-connectivity.  Hall's theorem
therefore supplies the four distinct representatives used in (2.6).

There is a fifth boundary vertex `s_0` in `S-{e}` outside those four
representatives.  The seven displayed branch sets in (2.8) are disjoint
and connected.  Their pairwise adjacencies are all literal:

- `P_0,P_1` are adjacent to one another and each meets every later branch
  set through its displayed boundary vertex;
- the four `D`-based branch sets are pairwise adjacent through the `K_4`;
  and
- `E union {s_0}` is adjacent to each `D`-based branch set because
  `|N_D(b)|>=4` forces `b` to be adjacent to every vertex of `D`.

Hence (2.8) is an explicit `K_7`-minor model.  Theorem 2.2 is valid.

## 4. Hall failure and its operation-specific response

Every portal set in (3.1) is nonempty, so a Hall-deficient subfamily has at
least two members and has nonempty union `Z`.  If `D=Z`, the preceding
Hall calculation gives `|D|<=4`, which Theorem 2.2 has eliminated.  A
component `C` of `D-Z` is therefore nonempty and proper in `D`.

The symmetric-allocation Hall calculation applies verbatim:

\[
 |N_G(C)|
  \le |Z|+10-|I|
  \le9.
\]

Its full neighbourhood is an actual separator because the old `R`-shore
survives outside it.  Seven-connectivity supplies the lower bound seven.

For a boundary edge `uv` with `u in C`, every six-colouring of `G-uv`
makes `u,v` equal; otherwise restoring `uv` six-colours `G`.  The fixed
merged-root colouring covers `G[C union B]`.  If the outside colouring
induced the same equality partition on `B`, a permutation of the six colour
names would align the two boundary assignments vertexwise, and the two
colourings would glue.  The rejected-partition conclusion of Lemma 3.1 is
therefore exact.

## 5. Orders seven and eight

At `|B|=7`, the component `C`, its full neighbourhood `B`, any crossing
edge, and a six-colouring after deleting that edge satisfy the definition
of a generic exact-seven response interface.  The old `R`-shore is a
nonempty opposite side, and `C subsetneq D` gives the declared strictness.

At `|B|=8`, apply the small-boundary lobe theorem with:

- its original boundary equal to the old eight-set `S`;
- its component equal to the old connected shore `L=E union D`; and
- its proper connected subset equal to the present `C`.

There are no `L`--`R` edges, so

\[
 |N_{G[L]}(C)|+|N_G(C)\cap S|=|N_G(C)|=8.
\]

All hypotheses of that theorem hold.  It gives either an actual
order-seven separation or a strict boundary-full order-eight descent with
selected shore `C`.  Independently of which structural outcome occurs,
Lemma 3.1's edge-deletion response at every original `C`--`B` edge remains
valid.  The source does not overclaim that the old labelled boundary
partition is preserved by the lobe theorem.

## 6. Exact order-nine equality

The Hall bound is the chain

\[
 9=|B|\le |Z|+10-|I|\le9.
\]

Equality therefore forces both `|Z|=|I|-1` and
`N_D(C)=Z`, and it forces `C` to meet every one of the `10-|I|` permitted
vertices in `E union (S-{d})`.  It misses exactly the outside vertices
whose portal sets belong to `I`.

The classification of `I` is exhaustive:

- if `Q_b in I`, then `|Z|>=4`, so `|I|=5`;
- if `Q_a in I` but `Q_b notin I`, then `|Z|>=3`, so `|I|=4` and the
  family is exactly the listed four-set family; and
- if neither belongs to `I`, nonempty portal sets exclude a deficient
  singleton, leaving precisely the two- and three-member subfamilies of
  `Q_e,Q_{x_d},Q_{y_d}`.

Proposition 4.1 is therefore correct.

## 7. Order-nine boundary absorption

With `B=N_G(C)`, the connected set `C` is a component of `G-B` and is
adjacent to every literal member of `B`.  The old `R`-shore guarantees at
least one other component `H` of `G-B`.

If such an `H` misses a boundary vertex, then `N_G(H) subseteq B` has
order at most eight.  It is a genuine separation boundary with `C` on the
opposite side, so seven-connectivity makes its order seven or eight.  Edge
deletion at an `H`--`N(H)` edge gives the claimed operation-specific
response by the same restoration-and-gluing argument as Lemma 3.1.

Otherwise every component of `G-B` is full to `B`.  Choosing `C` and one
other component gives two nonempty, connected, anticomplete subgraphs each
adjacent to all nine vertices of `B`.  The GREEN-audited boundary-absorption
theorem applies literally and yields

\[
                 \chi(G[B])\le4
       \quad\text{or}\quad
                 G[B]\cong K_2\vee C_7.
\]

This proves Proposition 4.2.

## 8. Localization of the cyclic order-nine exception

In every equality form, all four vertices

\[
                         W=\{x_e,y_e,x_0,y_0\}
\]

belong to `B`.  No member of `W` is universal in `G[B]`, because it has a
second member of its same independent boundary colour class in `W` and is
nonadjacent to that vertex.

In Hall form 3, the vertices `a,b,c,W` all belong to `B`.  The vertex `c`
is adjacent to `b` and every member of `W`, so its degree in `G[B]` is at
least five.  It is nonadjacent to `a`, so its degree is at most seven.  This
is impossible in `K_2 vee C_7`, whose vertex degrees are exactly four and
eight.  Form 3 is therefore excluded.

In form 2, one has

\[
                         B=Z\cup\{b,c\}\cup W.
\]

The same five displayed neighbours force `c` to have degree eight and be
universal.  The vertex `b` is nonadjacent to every member of `W`, while no
member of `W` is universal, so the second universal vertex lies in `Z`.

In form 1, one has

\[
                         B=Z\cup\{c\}\cup W.
\]

The four neighbours in `W` force `c` to have degree four or eight.  If its
degree were four, it would be nonadjacent to all of `Z`.  Since neither
universal vertex can lie in `W`, both would lie in `Z`, contradicting the
fact that each universal vertex must be adjacent to `c`.  Hence `c` is
universal, and the second universal vertex again lies in `Z`.

Proposition 4.3 and its exact universal pair `{c,z}`, `z in Z`, are
therefore valid.

## 9. Trust boundary

The audited theorem is conditional on the full endpoint-reversal geometry
and on the explicit rejection of the split boundary partition (1.3).  It
eliminates `|D|<=4`, converts Hall failure into an operation-specific
separator of order seven to nine, absorbs orders seven and eight into
existing machinery, and classifies the exact order-nine boundary outcome.

It does **not** eliminate the distinct-representative cases `|D|=5,6`,
produce compatible closed-shore colourings at the returned separators,
turn an order-nine response into a recursive order-eight interface, or
prove `HC_7`.  In the exceptional cyclic order-nine boundary it localizes
the two universal vertices but does not make them a global transversal or
produce compatible shore colourings.  Within this stated scope, no
unresolved assumption remains.
