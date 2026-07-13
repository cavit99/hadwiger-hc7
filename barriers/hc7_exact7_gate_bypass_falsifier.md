# Gate bypass does not by itself separate attained duties

**Status:** adversarial local certificate.  This is not an `HC_7`
counterexample.  It falsifies the unqualified implication

> a complementary bridge bypassing the Helly gate reroutes two attained
> duty hulls to be vertex-disjoint.

The obstruction uses literal attained duties and unique packet portals.  It
therefore cannot be dismissed as an artefact of replacing duties by support
size or of choosing bad portal witnesses.

## 1. Exact normalized Moser state

Take the standard Moser boundary on `S={0,...,6}`,

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

The normalized contraction block `I={0,5}` has the legal exact state

\[
 \Pi=\{A,B,D,\{6\}\},\qquad
 A=\{2,3\},\quad B=\{1,4\},\quad D=\{0,5\}.
\]

Every displayed block is independent.  The only singleton block is `{6}`,
so choose `C={6}`.  Then

\[
 d_H(\Pi)=|\Pi|-|C|=3.
\]

Moreover `6` has a neighbour in each of `A,B,D`, respectively through
`2,1,5`.  Hence the three literal
attained duties are exactly

\[
 D_{\Pi,C}(A)=A,
 \qquad D_{\Pi,C}(B)=B,
 \qquad D_{\Pi,C}(D)=D.                    \tag{1.1}
\]

Thus this example lies inside the frozen normalized Moser state family and
uses the actual state duties, not unconditional carrier defect.

## 2. The labelled full packet

Let the packet `P` be the six-cycle

\[
 u_0u_1u_2u_3u_4u_5u_0.
\]

Give the six duty labels unique literal portals in cyclic order

\[
\begin{array}{c|cccccc}
\text{packet vertex}&u_0&u_1&u_2&u_3&u_4&u_5\\ \hline
\text{duty label having this unique portal}
 &2&1&0&3&4&5.
\end{array}                                      \tag{2.1}
\]

Equivalently, the two portals for `A` are `u_0,u_3`, those for `B` are
`u_1,u_4`, and those for `D` are `u_2,u_5`.  Finally join `6` to `u_0`
(and to no other packet vertex).  The packet is connected and `S`-full.
All witnesses relevant to (1.1) are forced.

This is the smallest nondegenerate cyclic example with two distinct private
portals for each of three duties: six such portals require six packet
vertices, and (2.1) uses exactly six.  Smaller examples exist only by
co-locating different duty labels or by forcing a common label into several
duties.

The local closed shore `H union P` is not excluded by clique-minor
monotonicity.  In fact it has treewidth at most four.  One explicit tree
decomposition has the following bags (write `u_i` instead of vertex
`7+i`):

\[
\begin{array}{lll}
X=\{0,5,u_0,u_2,u_4\},
&X_1=\{0,5,6,u_0,u_2\},
&X_2=\{0,3,5,u_2,u_4\},\\
X_3=\{5,u_0,u_4,u_5\},
&X_{11}=\{0,1,6,u_0,u_2\},
&X_{21}=\{0,3,4,5,u_4\},\\
X_{22}=\{3,u_2,u_3,u_4\},
&X_{111}=\{0,1,2,6,u_0\},
&X_{112}=\{1,u_0,u_1,u_2\}.
\end{array}
\]

Join `X` to `X_1,X_2,X_3`, join `X_1` to `X_{11}`, join `X_2` to
`X_{21},X_{22}`, and join `X_{11}` to `X_{111},X_{112}`.  Direct inspection
checks edge coverage and the running-intersection property.  Every bag has
order at most five, so `tw(H union P)<=4`; in particular this local graph
has no `K_6` minor, hence no `K_7` minor.  The certificate still does not
claim that the graph extends to a seven-connected contraction-critical host.

## 3. Every packet tree has a bypassed Helly gate

Any tree `T subseteq P` containing all selected duty witnesses is a spanning
tree of the cycle, hence

\[
                       T=P-e
\]

for one cycle edge `e`.  In the linear order on this path, the two witnesses
of each of `A,B,D` determine its duty hull.  Around the original cycle, the
terminal pairs of every two duties alternate:

\[
 A,B,A,B;\qquad A,D,A,D;\qquad B,D,B,D.     \tag{3.1}
\]

Consequently the three interval hulls in `T` meet pairwise.  By interval
Helly they have a common vertex.  More explicitly, if `e=u_5u_0`, then

\[
 K_A=u_0Tu_3,\qquad K_B=u_1Tu_4,\qquad K_D=u_2Tu_5,
\]

and

\[
 K_A\cap K_B\cap K_D=\{u_2,u_3\}.           \tag{3.2}
\]

Rotation gives the same statement for every choice of `e`: the common
intersection consists of the two middle vertices of the spanning path.
In particular, neither endpoint of `T` is a common gate.  (An endpoint is a
witness for only one of the three duties.)

The omitted cycle edge `e` is a literal `T`-bridge with its two endpoints as
attachments and empty interior.  The attachment-to-attachment path in `T`
is all of `T`, so it contains every possible common gate as an internal
vertex.  Thus `e` bypasses the Helly gate in the strongest elementary sense.

## 4. Exact cycle-packet dichotomy

### Lemma 4.1 (private two-portal cycle exchange)

Let a cyclic packet contain six mutually distinct selected portal vertices,
two for each of three attained duties `A,B,D`.  If the two portal pairs for some
two duties do not alternate in the cyclic order, then those duties have
vertex-disjoint adjacent connected carriers in the cycle.  With the other
full packet funding the third duty, the attained state reflects.

If, conversely, the six portals are the only packet contacts for their six
literal duty labels, then no two duties have vertex-disjoint connected
carriers exactly when, up to rotation, reversal, and renaming the duties,
the cyclic portal word is

\[
                         A\,B\,D\,A\,B\,D.           \tag{4.1}
\]

#### Proof

For two nonalternating pairs, choose the two disjoint cycle arcs joining
the endpoints of the respective pairs and containing no endpoint of the
other pair.  If the arcs are not already adjacent, extend them disjointly
through one intervening gap until one cycle edge joins them.  They remain
connected and contain the selected portal pair for their respective duties,
so they are adjacent duty-correct carriers.  The attained-duty split theorem
then reflects the state.

For the converse, unique literal portals force every carrier for a duty to
contain both vertices of its portal pair.  Two connected subgraphs of a
cycle joining alternating terminal pairs cannot be vertex-disjoint: each
of the two arcs joining the first pair contains a terminal of the second.
Thus pairwise alternation forbids every carrier pair.

It remains only to identify the cyclic word.  Fix the two `A` occurrences.
Alternation with `A` places one `B` and one `D` in each of the two open
`A-A` arcs.  After possibly interchanging `B,D`, the first arc reads `B,D`.
For the `B` and `D` pairs also to alternate, the second arc must read `B,D`,
not `D,B`.  This gives (4.1), and the displayed word plainly has all three
pairwise alternations.  \(\square\)

This closes every private two-portal cyclic packet except one labelled
width-two web order.  It remains valid after arbitrary subdivisions and
after adding portal-free trees with a single attachment to the cycle.
A subgraph with two or more cycle attachments is a chord-like bypass and
requires the label-compatible bridge analysis; no claim is made for it here.

### The surviving alternating packet

The obstruction is independent of the selected packet tree.  We prove the
stronger statement that `P` contains no two vertex-disjoint connected
subgraphs which fund two distinct duties.

Indeed, because the portals in (2.1) are unique, a carrier funding `A` must
contain both `u_0,u_3`, one funding `B` must contain both `u_1,u_4`, and one
funding `D` must contain both `u_2,u_5`.  In a cycle, two vertex-disjoint
connected subgraphs cannot connect alternating terminal pairs.  To see this
directly, a proper connected subgraph containing the two terminals of one
pair contains one of the two arcs between them; by alternation, each such arc
contains a terminal of the other pair.  If the connected subgraph is the
whole cycle, intersection is immediate.  Applying this observation to each
of the three alternating pairs in (3.1) proves the claim.

It follows that using the bridge `e`, changing the omitted edge of `T`, or
reselecting portal witnesses cannot make two attained-duty hulls or carriers
vertex-disjoint.

Thus (2.1) realizes the unique cyclic private-portal obstruction from
Lemma 4.1, not merely one bad drawing.

## 5. Exact lesson for the gate programme

A topological bypass of `g` is insufficient.  The bypass must also be
**label compatible**: it must defeat the alternating order of the literal
duty portal sets.  The six-cycle above is the minimal private-portal
`A B D A B D` web obstruction.

Accordingly, a correct next lemma needs a dichotomy of the following form.

1. A bridge gives a label-compatible rerouting and hence two disjoint
   attained-duty carriers; or
2. the portal order is web-like (the certificate above is its atomic form),
   and that web structure yields the promised literal adhesion, colour
   gluing, or `K_7` by using the second packet and the ambient critical graph.

This certificate does not rule out that second, global conclusion.  It shows
that the web/adhesion outcome is logically indispensable: it cannot be
replaced by the assertion that every gate-bypassing bridge yields a carrier
split.
