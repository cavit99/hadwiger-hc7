# The full-singleton terminal is an operation-critical alternating lock

## 1. Setting

Retain the exact triangle boundary

\[
 B=\{h,1,2,r,a,b,c\},qquad
 P=\{h,c\},\quad Q=\{r,a\},\quad R=\{1,2,b\},     \tag{1.1}
\]

from `hadwiger_singleton_triangle_q2_web_exchange.md`.  The first two
sets are independent, (R) is a triangle, and

\[
 P\mid Q\mid\{1\}\mid\{2\}\mid\{b\}             \tag{1.2}
\]

has complete block quotient.  Assume

\[
                         G-B=\{d\}\mathbin{\dot\cup}O,            \tag{1.3}
\]

where (d) is full to (B), (O) is a connected full shore, and
(d) is anticomplete to (O).  By the unique-orientation theorem,
(O) contains disjoint (P)- and (Q)-carriers.

Put (H=G-d=G[B\cup O]).  The graph (G) is assumed six-minor-critical
and not six-colourable.

## 2. Exact boundary saturation

### Lemma 2.1 (the owner has only one-pair states)

Every proper six-colouring of (H) uses all six colours on (B).
Consequently its equality partition on (B) consists of exactly one
two-vertex independent block and five singleton blocks.

#### Proof

If at most five colours occurred on (B=N(d)), a sixth colour absent
from (B) could be assigned to (d), six-colouring (G).  Thus all
six occur.  The seven-vertex boundary has independence number at most
two, so precisely one colour occurs twice and all others occur once.
\(\square\)

### Lemma 2.2 (both exact star traces exist)

The graph (H) has a six-colouring whose unique repeated boundary pair
is (P=\{h,c\}), and another whose unique repeated boundary pair is
(Q=\{r,a\}).

#### Proof

Contract the connected star on \(\{d,h,c\}\), with centre (d), to
one vertex.  Its leaves are independent by (hc\notin E(G)).  Colour
the proper minor with six colours, delete the contracted centre (d),
and expand (h,c) with its colour.  This gives a proper colouring of
(H) in which (h,c) agree.  Lemma 2.1 says that no other boundary
equality occurs.  The proof for \(\{d,r,a\}\) is identical. \(\square\)

The two traces are genuine counterexample-derived data.  Static
fullness of the shore does not imply them.

## 3. Every operation crosses the five-block threshold

For a proper labelled minor operation \(\mu\) wholly in (O), let
(O^\mu) be the operated shore.

### Theorem 3.1 (singleton transition polarity)

After every vertex deletion, internal edge deletion or contraction, or
label-preserving boundary--shore edge deletion or contraction in (O),
the graph (G^\mu) has a six-colouring whose boundary partition is a
matching of order two or three in \(\overline{G[B]}\).  That exact state
extends (O^\mu) and does not extend the original (O).

#### Proof

The proper minor (G^\mu) is six-colourable.  Its retained singleton
(d) is adjacent to every boundary vertex, so the colour of (d) is
absent from (B).  Hence (B) uses at most five colours.  Since every
independent set of (B) has order at most two, its nonsingleton colour
classes form a matching; seven vertices in four or five colours give a
matching of order three or two, respectively.

The state plainly extends the operated shore.  If it extended the
original shore, align the boundary block colours with the colouring of
(B\cup\{d\}) and glue, six-colouring (G).  Thus it did not extend
the original (O). \(\square\)

### Lemma 3.2 (edge-transition Kempe fan)

Let (xy\) be an internal edge of (O).  In every six-colouring of
(G-xy),

\[
                         c(x)=c(y)=\alpha,          \tag{3.1}
\]

and for each colour \(\beta\ne\alpha\), the vertices (x,y) lie in
one \(\alpha/\beta\)-component of (G-xy).

The same assertion holds for a deleted boundary--shore edge, with its
two endpoints in place of (x,y).

#### Proof

If the deleted-edge endpoints had different colours, the edge could be
restored.  If their common colour were \(\alpha\) and they lay in
different \(\alpha/\beta\)-components, interchange the two colours in
the component containing one endpoint.  They then have different
colours, so the edge can again be restored.  Either event gives a
six-colouring of (G), a contradiction. \(\square\)

Thus the remaining lock is operation-critical in a literal sense:
every edge has five alternative bichromatic detours, while every
operation changes the boundary from one pair to at least two pairs.

## 4. The protected split which finishes immediately

### Lemma 4.1 (enriched packet certificate)

Suppose (O) contains disjoint connected sets (X_P,X_Q) such that

\[
 X_P\sim h,c,1,2,qquad X_Q\sim r,a.               \tag{4.1}
\]

Then (G\succeq K_7).  The symmetric conclusion holds when

\[
 X_P\sim h,c,qquad X_Q\sim r,a,1,2.               \tag{4.2}
\]

#### Proof

Under (4.1), use the seven bags

\[
 \{d\}\mid\{h\}\mid\{1\}\mid\{2\}\mid\{r\}
 \mid(\{c\}\cup X_P)\mid(\{a,b\}\cup X_Q).       \tag{4.3}
\]

The first five form a (K_5).  The (cX_P)-bag sees (d) through
(c), sees (h,1,2) through (X_P), and sees (r) through (cr).
The (abX_Q)-bag sees (d) through (a), sees (h) through (ah),
sees (1,2) through (b), and sees (r) through (X_Q).  The last
two bags are adjacent through (ca) (also (cb)).  This is a
(K_7)-model.

Under (4.2), use instead

\[
 \{d\}\mid\{h\}\mid\{1\}\mid\{2\}\mid\{r\}
 \mid(\{b,c\}\cup X_P)\mid(\{a\}\cup X_Q),       \tag{4.4}
\]

and check the same adjacencies with the roles reversed. \(\square\)

Thus the singleton problem is exactly an **enriched packet** problem,
not an arbitrary branch-set split.

## 5. Failure has one alternating two-side form

Fix any packet (X_P,X_Q\) in (O).  Let (C_P) be the component of
(O-X_Q) containing (X_P), and let (C_Q) be the component of
(O-X_P) containing (X_Q).

### Theorem 5.1 (alternating lock)

If neither enriched packet in Lemma 4.1 exists, then, after interchanging
the labels (1,2),

\[
 N_{C_P}(1)=\varnothing,\qquad
 N_{C_Q}(2)=\varnothing.                            \tag{5.1}
\]

Moreover

\[
 N_O(1)\subseteq C_Q,\qquad N_O(2)\subseteq C_P,   \tag{5.2}
\]

and every component of (O-(X_P\cup X_Q)) which attaches to both
carriers has no portal to either (1) or (2).

#### Proof

If (C_P) met both the (1)- and (2)-portal sets, then (C_P) and
(X_Q) would be the disjoint enriched packet (4.1).  Thus (C_P)
misses at least one of (1,2).  Symmetrically (C_Q) misses at least
one.

They cannot miss the same label, say (1).  Indeed, every vertex of
(O) belongs to (C_P\cup C_Q).  To see this, a component of
(O-(X_P\cup X_Q)) attaches to (X_P), to (X_Q), or to both, and
therefore lies in the corresponding one or both of (C_P,C_Q); the
carrier vertices themselves lie in their named component.  Fullness
supplies a (1)-portal somewhere in (O), which would then lie in
(C_P) or (C_Q), a contradiction.  Hence the missed labels are
different, giving (5.1) after relabelling.

The covering (O=C_P\cup C_Q) now proves (5.2): a (1)-portal cannot
lie in (C_P), and a (2)-portal cannot lie in (C_Q).  A component
attaching to both carriers lies in (C_P\cap C_Q), so (5.1) excludes
both portal labels from it. \(\square\)

The lock is not a fiction.  At the purely static level take
(O=xy\cong K_2), let (x) see (h,c,2,b), and let (y) see
(r,a,1,b).  This shore is full to (B), and (\{x\},\{y\}) is a
(P,Q)-packet, but neither carrier is enriched and no alternative
disjoint packet exists.  This two-vertex gadget is not asserted to be
seven-connected or operation-critical.  It proves that fullness plus a
packet alone cannot close the singleton cell; Theorems 2.2 and 3.1 are
essential extra hypotheses.

### Corollary 5.2 (short locked carrier exports an exact cut)

In the orientation (5.1),

\[
 N_G(C_P)\subseteq X_Q\cup(B-\{1\}),\qquad
 N_G(C_Q)\subseteq X_P\cup(B-\{2\}).              \tag{5.3}
\]

Consequently, if either carrier is a singleton, (G) has a nested exact
seven-cut.  More generally, if \(|X_Q|\le2\) and (C_P) misses both
(1,2), or symmetrically, there is a nested exact seven-cut.

#### Proof

The set (C_P) is a component of (O-X_Q), it has no (1)-portal,
and (d) is anticomplete to (O).  These facts give the first
inclusion in (5.3); the second is symmetric.  The displayed sets are
genuine separators, since (C_P,C_Q) are nonempty and the full
singleton (d) lies on the far side.  If \(|X_Q|=1\), the first has
order at most (1+6=7).  Seven-connectivity forces equality and hence
an exact seven-cut.  If (C_P) misses both labels and \(|X_Q|\le2\),
replace (B-\{1\}) by (B-\{1,2\}), obtaining the same upper bound.
The symmetric cases are identical. \(\square\)

Thus a lock with no exact-cut exit has both carriers of order at least
two, and every order-two carrier has the opposite side supported by
exactly one of the labels (1,2).  The operation-critical theorem only
has to attack these genuinely distributed locks.

## 6. Exact remaining theorem

The full-singleton cell is therefore reduced to the following sharply
operation-level statement.

> **Protected split-or-state theorem.**  In the setting (1.1)--(1.3),
> an owner satisfying the transition polarity of Theorem 3.1 and the
> edge fans of Lemma 3.2 cannot realize the alternating lock (5.1)--(5.2)
> for every packet.  Equivalently, some packet becomes enriched, or
> some one-step state can be normalized to (1.2) on the unoperated
> owner side.

The first outcome gives the explicit (K_7) in Lemma 4.1; the second
six-colours (G) by giving (d) the sixth colour.  This formulation
uses all the data absent from static counterarchitectures: two exact
one-pair traces, an order-two/three transition after every operation,
and five Kempe detours at every deleted edge.

What remains unproved is the last sentence of the displayed theorem.
In particular, Theorem 5.1 must not be mistaken for a contradiction:
an alternating carrier lock is a genuine static possibility.  The next
proof must show that an operation-critical lock cannot persist.
