# Audit of the packet-to-root-connectivity theorem

**Verdict:** GREEN after the corrections recorded in the theorem file.

## 1. The additive connectivity count

Put `H=J[S]` and `r=kappa_H(S)`.  Every `S`-separator `X` of `J` must meet
all `q` packets outside `S`: a packet disjoint from `X` would join every
surviving root.  Thus `|X-S|>=q`.  Also `X cap S` must be an `S`-separator
of `H`, since an `H-(X cap S)` path is a `J-X` path.  Hence
`|X cap S|>=r`.  If `H` has no `S`-separator, neither does `J`; otherwise
the two disjoint contributions add.  This proves the stronger bound

\[
  \kappa_J(S)\ge \min\{q+\kappa_{J[S]}(S),|S|-1\}.
\]

For disconnected `J[S]`, this contains the packet-only bound
`kappa_J(S)>=min{q,|S|-1}`.  Connected and two-connected boundaries give
the additive `q+1` and `q+2`, respectively.  The packet-only term is
sharp: for independent `S` and `q` singleton universal packets, deleting
all packet vertices is an `S`-separator of order `q`.

## 2. Use of the cited theorem

Theorem 3 of Boehme--Harant--Kriesell--Mohr--Schmidt states that
`kappa_J(S)>=k`, for `k in {1,2,3,4}`, yields a `k`-connected `S`-minor;
for `k<=3` it yields a topological `S`-minor.  Substituting
`k=min{q+r,4,|S|-1}` is valid.  In particular, two packets behind a
connected seven-boundary give a three-connected topological `S`-minor;
behind a two-connected seven-boundary they give a four-connected
`S`-minor.  Three packets behind a connected boundary also give a
four-connected `S`-minor.

The rooted convention is also used correctly: all roots survive, no
certificate bag contains two roots, and all contractions are `S`-legal.

## 3. Confined proper-minor coupling

For `J=G[R union S]`, a certificate can be implemented by deletions and
`S`-legal contractions wholly in the rich closed shore, leaving
`G[L union S]` unchanged.  If at least one operation is genuine, the
result is a proper minor.  A six-colouring of that minor restricts to a
proper colouring of the untouched closed shore and hence returns one exact
partition on literal `S`.  The rooted minor and that returned state thus
coexist in the same operation.

This is only an existential coupling.  The theorem does not say that the
returned partition is a named attained state, that its blocks have
connected carriers in the rooted core, or that the certificate preserves
the packets which supplied the connectivity.  If the certificate is the
identity, even this proper-operation conclusion needs a separate operation
and is not automatic.

## 4. Label and packet reservation fail

Two explicit examples delimit the result.

1. Put `W=K_1 join K_{3,3}` and declare all seven vertices to be `S`.
   The graph is four-connected: deleting at most three vertices leaves the
   universal vertex or leaves a connected remainder of `K_{3,3}`, while
   the universal vertex together with one bipartition class is a cut of
   order four.  It is nonplanar and edge-minimal four-connected, since
   every non-universal vertex has degree four.  As every vertex is a root,
   a `K_4` model which reserves the other three roots would have four
   singleton branch sets.  This is impossible because `omega(W)=3`.
   Thus even a minimal nonplanar four-connected `S`-minor does not provide
   the required label-reserving rooted `K_4`.
2. Let `J[S]` be a seven-vertex path and add three independent vertices,
   each adjacent to all of `S`.  The added vertices are three disjoint full
   packets and the theorem gives `kappa_J(S)>=4`.  Any model disjoint from
   all three packet interiors lies in the path and therefore cannot contain
   `K_4`.  The four-connected rooted minor cannot in general be used while
   reserving the same three packets for the final packet lift.

The standard theorem that a four-connected nonplanar graph has a rooted
`K_4` at any prescribed four vertices does not repair the first example:
its rooted model is allowed to consume one or more of the other three
literal boundary vertices.

## 5. Global-invariant verdict

The result supplies a reusable local existence theorem, not a canonical
rooted torso.  Different certificates may overlap different packets and
need not be nested or compatible after a state transition.  Minimality by
vertex or edge count does not make the certificate unique, and neither its
planar rotation nor a candidate apex pair lifts monotonically from a minor
to the original graph.

Accordingly, this theorem may normalize one fixed `(1,2)` cell before a
stateful web argument, but it cannot itself be the well-founded global
invariant.  A further label-reserving carrier/rural theorem, with an
explicit transition rule, remains necessary.
