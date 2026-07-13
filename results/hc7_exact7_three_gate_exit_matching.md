# Three-gate exit matching: a state-free packet-vector pullback

**Status:** proved and independently audited.

This note isolates the first transition after the exact three-gate descent
in `../results/hc7_exact7_binary_duty_cycle_or_gate.md`.  It uses no
prescribed equality state on the new boundary.  Its conclusion is only a
packet-vector pullback, together with the exact two residual exit systems
which that elementary pullback does not handle.

## 1. Setup

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

be an actual separation in a seven-connected graph.  Thus there is no edge
between `L` and `R`, and both sets are nonempty.  Assume that:

1. `P\subseteq L` is a connected `S`-full packet;
2. `C` is a component of `G[R]`;
3. `Q\subseteq R-C` is a connected `S`-full packet;
4. `C` is three-connected and `X\subseteq V(C)` is a three-vertex cut;
5. `K` is one component of `C-X`, and

   \[
                         A=N_S(K),\qquad |A|=4;          \tag{1.1}
   \]

6. every vertex of `X` has a neighbour in `K`.

Here `S`-full means that every literal vertex of `S` has a neighbour in
the packet.  In the attained paired-triangle application, items 5--6 are
exactly the dutyless-lobe conclusion: `A` is the retained singleton plus
one literal from each of the three attained binary duties.  The proof below
uses only (1.1), not that interpretation and not any colouring on the new
boundary.

Put

\[
                    T=S-A,\qquad |T|=3,
 \qquad             \Omega=X\cup A.                    \tag{1.2}
\]

Let `\mathcal J` be the family of components of `C-X` other than `K`.
It is nonempty because `X` is a cut.  For `J\in\mathcal J`, call `J`
**self-full** when

\[
                         A\subseteq N_S(J).              \tag{1.3}
\]

For a non-self-full lobe define its **exit set**

\[
                         E(J)=N_S(J)\cap T.              \tag{1.4}
\]

## 2. Literal preliminary facts

### Lemma 2.1 (all lobes hit the gate and four boundary literals)

Every component `J` of `C-X` is adjacent in `C` to all three vertices of
`X`, and

\[
                         |N_S(J)|\ge4.                   \tag{2.1}
\]

Consequently every exit set in (1.4) is nonempty.

#### Proof

Suppose `J` missed `x\in X`.  The set `X-\{x\}` would then separate `J`
from any other component of `C-X`: distinct components of `C-X` have no
edge between them, and the only remaining gate vertex `x` has no edge to
`J`.  This contradicts three-connectivity of `C`.  Hence `J` hits every
member of `X`.

Because `C` is a component of the old open shore and `J` is a component of
`C-X`,

\[
                        N_G(J)=X\cup N_S(J).             \tag{2.2}
\]

The nonempty old opposite shore `L` is disjoint from and anticomplete to
`J`.  Thus (2.2) is a separator of `G`.  Seven-connectivity gives

\[
                7\le |N_G(J)|=3+|N_S(J)|,
\]

which is (2.1).  If `J` is not self-full, it misses at least one of the
four members of `A`.  A boundary support of order at least four must then
contain a member of the complementary three-set `T`; hence `E(J)` is
nonempty.  \(\square\)

### Lemma 2.2 (the new boundary is literal)

The set `\Omega` is the literal neighbourhood of `K`:

\[
                             N_G(K)=\Omega.              \tag{2.3}
\]

Consequently `K` and its complement behind `\Omega` are the two nonempty
open shores of an actual separation of order seven, and `K` is
`\Omega`-full.

#### Proof

Componenthood gives `N_C(K)\subseteq X`; item 6 gives equality.  Equation
(1.1) gives the boundary neighbours, and `C` being a component of the old
open shore excludes every further neighbour.  Thus

\[
              N_G(K)=N_C(K)\mathbin{\dot\cup}N_S(K)
                    =X\mathbin{\dot\cup}A=\Omega.
\]

The set has order seven.  The shore `K` is nonempty, while the old shore
`L` lies in the other component side and is nonempty.  Every member of
`X` and `A` has a literal neighbour in connected `K`, so `K` is
`\Omega`-full.  \(\square\)

## 3. Exit matching

### Lemma 3.1 (two literal packets from two matched lobes)

The new open shore opposite `K` contains two pairwise vertex-disjoint
connected `\Omega`-full packets whenever at least one of the following
holds:

1. two members of `\mathcal J` are self-full;
2. one member is self-full and `|\mathcal J|\ge2`; or
3. there are distinct non-self-full lobes `J_0,J_1` and distinct literals
   `t_0,t_1\in T` with

   \[
                         t_i\in E(J_i)\quad(i=0,1).       \tag{3.1}
   \]

#### Proof

A self-full lobe `J` is itself a connected `\Omega`-full packet.  Indeed,
Lemma 2.1 supplies its contacts to all three members of `X`, while (1.3)
supplies its contacts to all four members of `A`.

Let `J` instead be non-self-full and choose `t\in E(J)`.  For either
`F\in\{P,Q\}`, put

\[
                         W(F,J,t)=F\cup\{t\}\cup J.      \tag{3.2}
\]

This set lies wholly in the new open shore: `F` avoids `\Omega`,
`t\in T=S-A`, and `J` avoids `X\cup S`.  It is connected because
`S`-fullness gives an `F-t` edge and `t\in N_S(J)` gives a `t-J` edge.
It contacts every member of `A` through `F` and every member of `X`
through `J`.  Hence (3.2) is a connected `\Omega`-full packet.

In case 1 use the two self-full lobes themselves.  In case 2 use the
self-full lobe and, if the second selected lobe is non-self-full, a packet
of the form `W(P,J,t)`; case 1 already handles a second self-full lobe.
The sets are disjoint because distinct lobes of `C-X` are disjoint and
`P\subseteq L` avoids `C\cup S`.

In case 3 use

\[
                         W(P,J_0,t_0),
                 \qquad W(Q,J_1,t_1).                   \tag{3.3}
\]

The old packets `P` and `Q` are disjoint, the lobes are distinct, the
anchors `t_0,t_1` are distinct, and the four ambient regions

\[
                  L,\quad R-C,\quad C-X,\quad S
\]

are pairwise disjoint where used in (3.3).  Thus the two packets in (3.3)
are literally vertex-disjoint.  \(\square\)

The next elementary statement is the exact set-system check needed when
exit sets overlap or have more than one member.

### Lemma 3.2 (rank-one exit systems)

Let `\mathcal E=(E_j:j\in I)` be a family of nonempty subsets of `T` with
`|I|\ge2`.  There are no distinct indices `i,j` and distinct representatives
`t_i\in E_i,t_j\in E_j` if and only if, for one `t\in T`,

\[
                              E_j=\{t\}
                              \quad\hbox{for every }j.    \tag{3.4}
\]

#### Proof

Condition (3.4) plainly forbids two distinct representatives.  Conversely,
suppose that `\bigcup_jE_j` contains distinct elements `u,v`.  If they
belong to different sets, those sets already have distinct representatives.
If both first occur in one set `E_i`, choose any `j\ne i` and any
`w\in E_j`.  Use `w` for `E_j` and choose from `\{u,v\}` an element
different from `w` for `E_i`.  Again there are distinct representatives.
Therefore failure of a two-representative matching forces the union of the
family to be one singleton, which is equivalent to (3.4) because every
set is nonempty.  \(\square\)

### Theorem 3.3 (state-free three-gate exit matching)

Under the setup in Section 1, at least one of the following holds.

1. The new open shore opposite `K` contains two pairwise vertex-disjoint
   connected `\Omega`-full packets.
2. `K` has exactly one sibling lobe:

   \[
                              |\mathcal J|=1.             \tag{3.5}
   \]

   If that sibling is non-self-full, its exit set may have order one, two,
   or three; if it is self-full, (1.4) is not defined for it.  No common
   singleton conclusion is asserted in this outcome.
3. There is a literal `t\in T` such that every sibling lobe is
   non-self-full and

   \[
                              E(J)=\{t\}
                              \quad(J\in\mathcal J).      \tag{3.6}
   \]

More sharply, if outcome 1 fails, then either outcome 2 holds or outcome 3
holds with `|\mathcal J|\ge2`.

#### Proof

Assume outcome 1 fails.  If `|\mathcal J|=1`, this is outcome 2.  Hence
assume at least two sibling lobes exist.

There is no self-full sibling: one such lobe together with any other lobe
would invoke Lemma 3.1(1) or (2).  All exit sets are therefore defined and
nonempty by Lemma 2.1.  Lemma 3.1(3) says that they admit no matching of
two distinct lobes to two distinct exits.  Lemma 3.2 now gives one
`t\in T` for which every exit set is exactly `\{t\}`.  This is outcome 3.
\(\square\)

The singleton in (3.6) is therefore an exact conclusion when there are at
least two sibling lobes.  It would be false to append it to the one-sibling
case: one lobe can have `E(J)` equal to any nonempty subset of the three-set
`T` without providing two disjoint lobe resources.

## 4. Packet-vector consequence in the counterexample kernel

### Corollary 4.1 (state-free vector pullback)

Assume in addition that `G` is `K_7`-minor-free, `\chi(G)=7`, and every
proper minor of `G` is six-colourable.  In outcome 1 of Theorem 3.3, the new exact-seven
separation at `\Omega` has packet vector, with `K` listed first,

\[
                             (1,2)\quad\hbox{or}\quad(1,3). \tag{4.1}
\]

The `(1,3)` alternative is impossible by adaptive packet reflection.
Thus every surviving outcome-1 descendant is a new `(1,2)` cell in which
`K` is literally the packet-thin shore.

#### Proof

Lemma 2.2 supplies one `\Omega`-full packet on the `K` shore, while
Theorem 3.3(1) supplies at least two on the opposite shore.  Apply the
audited exact-seven packet theorem.  Its minimum packet number is one and
the sum is at most four.  Since the opposite number is at least two, the
`K`-shore number must be exactly one and the opposite number is two or
three.  This is (4.1).  The audited `(1,3)` adaptive reflection theorem
eliminates the latter value.  \(\square\)

No equality partition on `\Omega` has been selected, forced, transported,
or asserted.  In particular Corollary 4.1 is not a state-preserving
induction: `K` becomes the new thin shore, and its order need not be smaller
than the old thin shore `L`.

## 5. Exact remaining target and measure warning

The elementary packet pullback leaves only:

1. a **one-return-lobe** gate, where the single sibling may have any
   nonempty exit set and may itself be `\Omega`-full; and
2. a **common-exit gate**, where at least two siblings are all
   non-self-full and their entire literal support in `T` is the same
   singleton `\{t\}`.

These are the narrow places at which model regeneration may be tested as
an `S1` escape.  This note does not claim that `t` is a cutvertex, that the
new cell has vector `(1,1)`, that deleting two vertices kills every `K_5`
model, or that an unlabelled regenerated `K_6` model supplies a labelled
near-`K_7` handoff.

There is also no current lexicographic transition measure.  The only strict
containment is `K\subsetneq C`.  In the surviving vector from Corollary 4.1,
`K` is the new thin shore, whereas the next rich packet may lie outside
`K`; moreover the new attained state is unrestricted.  Thus neither thin
shore order nor active rich-component order is proved to decrease.  The
audited single-gate near-model rotations are exact involutions, so an `S1`
rank cannot be inserted without a separate orientation theorem.
