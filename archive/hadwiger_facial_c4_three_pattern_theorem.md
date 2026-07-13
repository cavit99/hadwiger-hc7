# The facial-\(C_4\) three-pattern theorem

## 1. Statement

Let \(H\) be a plane graph and let

\[
                 C=a b c d a
\]

be an induced facial four-cycle.  Up to a permutation of four colour
names, a proper colouring of \(C\) has exactly one of the following
four equality patterns:

\[
\begin{array}{c|c|c}
\text{pattern}&\text{representative}&\text{equalities}\\ \hline
P_4&1212&a=c,\ b=d,\\
P_A&1214&a=c,\ b\ne d,\\
P_B&1232&a\ne c,\ b=d,\\
P_0&1234&a,b,c,d\text{ pairwise distinct}.
\end{array}
\tag{1.1}
\]

### Theorem 1.1 (facial-\(C_4\) three-pattern theorem)

At least three of \(P_4,P_A,P_B,P_0\) extend to proper
four-colourings of \(H\).

The theorem uses the Four Colour Theorem, but no case enumeration.  Its
second ingredient is the four-ring count identity of Birkhoff and
Lewis; a complete Kempe-chain proof is included below.

## 2. The four-ring count identity

For \(X\in\{P_4,P_A,P_B,P_0\}\), let \(x_X\) be the number of proper
four-colourings of \(H\) whose restriction to \(a,b,c,d\) is the fixed
representative of \(X\) in (1.1).  These are finite nonnegative
integers.  A pattern extends if and only if its corresponding \(x_X\)
is positive, since any other choice of colour names can be permuted to
the displayed representative.

### Lemma 2.1 (Birkhoff--Lewis four-ring identity)

\[
                   x_{P_4}+x_{P_0}=x_{P_A}+x_{P_B}.       \tag{2.1}
\]

#### Proof

Regard the facial disk bounded by \(C\) as the outside face, so that all
of \(H-C\) lies in the complementary closed disk.  We construct a
bijection

\[
 {\cal C}(P_4)\mathbin{\dot\cup}{\cal C}(P_0)
 \longleftrightarrow
 {\cal C}(P_A)\mathbin{\dot\cup}{\cal C}(P_B),             \tag{2.2}
\]

where \({\cal C}(X)\) is the set counted by \(x_X\).

Take a colouring \(f\) on the left of (2.2), and consider the components
of the subgraph induced by colours \(1\) and \(3\).

* If \(a,c\) lie in different \(1/3\)-components, interchange colours
  \(1,3\) on the component containing \(c\).  From boundary word
  \(1212\) this produces \(1232\), and from \(1234\) it produces
  \(1214\).
* If \(a,c\) lie in the same \(1/3\)-component, that component contains
  an \(a\)-\(c\) path.  The vertices \(b,d\) cannot then lie in one
  \(2/4\)-component: otherwise the two components would contain
  vertex-disjoint \(a\)-\(c\) and \(b\)-\(d\) paths whose endpoints
  alternate on the boundary of a disk.  Interchange colours \(2,4\) on
  the component containing \(d\).  From \(1212\) this produces
  \(1214\), and from \(1234\) it produces \(1232\).

Both operations are ordinary Kempe interchanges and preserve properness.
They therefore define a map from the left side of (2.2) to the right.

The same rule is its inverse.  Indeed, start from boundary word \(1214\)
or \(1232\) and again test whether \(a,c\) lie in the same
\(1/3\)-component.  If they are different, swapping the component of
\(c\) gives respectively \(1234\) or \(1212\).  If they are the same,
planarity again separates \(b,d\) in the \(2/4\)-subgraph, and swapping
the component of \(d\) gives respectively \(1212\) or \(1234\).
The relevant component partition is unchanged by merely interchanging
its two colour names, so the two operations undo one another.

Thus (2.2) is a bijection, and counting its two sides gives (2.1).
\(\square\)

The topological input used here is only the elementary alternating-path
fact: two vertex-disjoint paths joining opposite pairs of four
cofacial vertices cannot exist in a plane graph.

## 3. Four planar coverage clauses

### Lemma 3.1

The set \({\cal E}\) of extendable patterns satisfies

\[
\begin{array}{ll}
P_0\in{\cal E}\ \text{or}\ P_B\in{\cal E},&
P_4\in{\cal E}\ \text{or}\ P_A\in{\cal E},\\
P_0\in{\cal E}\ \text{or}\ P_A\in{\cal E},&
P_4\in{\cal E}\ \text{or}\ P_B\in{\cal E}.
\end{array}
\tag{3.1}
\]

#### Proof

Because \(C\) is induced and facial, the diagonal \(ac\) can be drawn
inside its face.  Apply the Four Colour Theorem to \(H+ac\).  Restricting
the resulting colouring to \(H\) gives \(a\ne c\), hence pattern \(P_0\)
or \(P_B\).  Adding \(bd\) in the same way gives \(P_0\) or \(P_A\).

Identifying the cofacial nonadjacent vertices \(a,c\) also preserves
planarity: draw an \(a\)-\(c\) arc through the empty face and contract
it, deleting any parallel edges.  A four-colouring of the resulting
plane graph expands to a colouring of \(H\) with \(a=c\), hence pattern
\(P_4\) or \(P_A\).  Identifying \(b,d\) similarly gives \(P_4\) or
\(P_B\).  These are exactly the four clauses in (3.1). \(\square\)

## 4. Proof of Theorem 1.1

Suppose at most two patterns extend.  The four clauses (3.1) imply that
exactly two extend.  Checking the four clauses, the only possible
two-element sets are

\[
                 \{P_0,P_4\},\qquad \{P_A,P_B\}.           \tag{4.1}
\]

In the first case the left side of (2.1) is positive and its right side
is zero.  In the second case the left side is zero and its right side is
positive.  Both contradict Lemma 2.1.  Therefore at least three patterns
extend. \(\square\)

## 5. Three-shore Helly consequence

### Corollary 5.1 (three facial frames have a common state)

Let \(H_1,H_2,H_3\) be three plane graphs having the same labelled
induced facial frame \(a b c d a\).  Then there is one equality pattern
\(P\in\{P_4,P_A,P_B,P_0\}\) which extends to a four-colouring of every
\(H_i\).

#### Proof

Let \({\cal E}_i\) be the extension set of \(H_i\).  Theorem 1.1 gives
\(|{\cal E}_i|\ge3\), so each complement in the four-element pattern
set has order at most one.  The union of three such complements has
order at most three and therefore cannot cover all four patterns.
Any pattern outside that union belongs to all three extension sets.
\(\square\)

After permuting colour names, the three colourings in Corollary 5.1 can
be made to agree on the four labelled boundary vertices.  Consequently
they glue whenever their interiors are pairwise anticomplete.  In the
Hadwiger programme this supplies the missing Helly mechanism for three
bare-web shores once the four artificial frame edges are legitimate and
all omitted boundary-root colours have already been reserved.  Those
lifting conditions remain separate; the corollary must not be applied
to a web shore whose planar extension is allowed to reuse a forbidden
omitted-root colour on an actual portal neighbour.

## 6. Scope

The theorem is label-free and holds for arbitrarily large plane graphs.
The facial and induced hypotheses are both used by the four planar
modifications.  The equality (2.1) itself needs only that the four ring
vertices occur cofacially in cyclic order.  No claim is made here for
nonfacial four-cycles or for list-colouring constraints on vertices
inside the disk.
