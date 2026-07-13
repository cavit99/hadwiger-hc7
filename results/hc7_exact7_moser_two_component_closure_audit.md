# Independent audit: complete pure-Moser two-component closure

Audited file: `hc7_exact7_moser_two_component_closure.md`.

Four-corner dependency:
`hc7_exact7_moser_four_corner_exchange_audit.md`.

**Verdict:** **GREEN.**

The current hypotheses match every cited theorem: `G` is seven-connected,
`K7`-minor-free, and proper-minor-minimal subject to not being
six-colourable; `N(v)=S` is exactly the displayed Moser spindle; and

\[
                         G-N[v]=C\mathbin{\dot\cup}D
\]

has exactly two nonempty connected components.  Proper-minor minimality
also implies `chi(G)=7`, so the four-corner exchange is within scope.

## 1. Order one

If `D={q}`, fullness and exact componenthood give

\[
                         N(q)=S=N(v),\qquad qv\notin E(G).
\]

There are no neighbours of `q` in `C`.  A six-colouring of the proper minor
`G-q` extends by assigning `q` the colour of its open twin `v`.  This is a
valid contradiction.

## 2. Order two

Let `D={p,q}`; connectedness gives the edge `pq`.  For `A in {L,R}`, put

\[
             P_D(A)=\{d\in D:E(d,A)\ne\varnothing\}.
\]

If `|P_D(A)|<=1`, then

\[
                         P_D(A)\cup(S-A)
\]

has order at most six and separates the nonempty set `D-P_D(A)` from the
apex and `C`.  Hence `P_D(L)=P_D(R)=D`: each singleton carrier sees at
least one label in each side.  Fullness says every label in each side is
seen by some carrier.

In either two-by-two carrier--label incidence graph, every vertex has
positive degree.  Hall's condition follows: a singleton carrier has a
neighbour, and both carriers together see both labels.  Choose independent
perfect matchings on `L={1,2}` and `R={3,4}`.  Pairing the labels assigned
to each carrier gives precisely one of

\[
                         13\mid24,qquad14\mid23.
\]

The paired labels are independent; each singleton carrier contacts both of
its labels; and the carriers are adjacent through `pq`.  The audited exact
four-corner exchange therefore gives a six-colouring contradiction.  The
argument does not call `K2` two-connected.

## 3. Order three

A connected simple graph on three vertices is a path or a triangle.  A path
has a cutvertex, contrary to the GREEN pure-Moser low-cut theorem
`results/hc7_exact7_moser_rich_twocut_exchange.md`.  All of that theorem's
hypotheses, including `K7`-minor-freeness and the exact two-component
decomposition, are present.

A triangle is two-connected and has order three, so the GREEN four-corner
Theorem 4.1 applies directly.  The independent direct proof retained in the
tiny-shore note is also valid: the same separator argument yields
`|P_D(L)|,|P_D(R)|>=2`; these two subsets of a three-set intersect.  For
`t` in the intersection, `X={t}` and `Y=D-{t}` are disjoint, connected,
and adjacent.  Each carrier sees at least one label on both sides, and
fullness makes each label visible.  Hall again returns one of the two
complementary matchings above.

## 4. Exhaustion

The independently audited low-cut theorem says that an exterior component
of order at least four has no cutvertex or two-cut and is therefore
three-connected.  It is in particular two-connected, so the GREEN
four-corner theorem eliminates it.

Orders one, two, and three are eliminated in Sections 1--3, and every
exterior component is nonempty and connected.  These cases exhaust all
possibilities.  Therefore the degree-seven pure-Moser branch with exactly
two exterior components is closed completely.

The only computational trust boundary is the finite quotient atlas already
exposed and independently audited in the low-cut theorem.  The tiny-shore
proof and the four-corner exchange use no computation.  This closes this
specific branch; it does not by itself settle the other degree-seven
neighbourhoods, other exterior-component counts, or all of `HC7`.
