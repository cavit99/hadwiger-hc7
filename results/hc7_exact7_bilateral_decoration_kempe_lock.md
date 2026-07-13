# Bilateral decoration mismatch gives an owned first-hit Kempe gate

**Status:** proved and independently audited in the stated exact-order-six
cell.  This is a dynamic proper-minor exchange in the exact terminal
interface.  It does not close the rural page by itself; it converts
abstract state mismatch into one
literal, label-faithful first-hit path for gate descent.

## 1. Exact three-block interface

Use the exact-order-six terminal separation from
`../results/hc7_exact7_moser_order6_decorated_exchange.md`.  Thus

\[
                         T=U\mathbin{\dot\cup}\{w\},
\]

the two open terminal shores are anticomplete, and the side terminals are
the repeated pair `a,b`.  Fix the same supported frame on both sides.  Its
three independent traces partition `U`; write them

\[
                              B_1,B_2,B_3.             \tag{1.1}
\]

On side `s`, let `C_i^s` be the connected core block with trace `B_i`.
The three core blocks are disjoint and pairwise adjacent.

A decoration `i` is **admissible** when

\[
                              B_i\cup\{w\}
\]

is independent.  Let `Sigma_s` be the set of all admissible decorations
which are geometrically supported on side `s` by some connected set with
trace `{w}`, disjoint from the three core blocks and the side terminal,
and adjacent to `C_i^s`.  This is the full supported-decoration set for
the fixed core, not a selected subset.

The standard contraction on one side has the following exact consequence.
If `i in Sigma_{3-s}`, then the expanded opposite closed side `s` has a
proper six-colouring `c_i^s` in which the equality blocks on `T` are

\[
       (B_i\cup\{w\})\mid B_j\mid B_k,
       \qquad \{i,j,k\}=\{1,2,3\},                 \tag{1.2}
\]

and the side terminal has a fourth colour, distinct from the three colours
in (1.2).  Indeed, on side `3-s` contract the repeated-pair star
`{v,a,b}`, contract `C_i^{3-s}` together with a supported `i`-witness, and
contract the other two core blocks separately.  Colour this proper minor
and expand only the opposite closed side `s`.  The four contracted images
form a clique, so the partition and the restored terminal colour are exact.

## 2. The switch-or-first-hit lemma

### Theorem 2.1 (owned first-hit Kempe gate)

Assume `i in Sigma_{3-s}` and `j in Sigma_s`, with `i ne j`.  In a
hypothetical counterexample, one of the following occurs.

1. A literal boundary-incompatibility certificate occurs: the first core
   block reached below has trace `B_h` with `B_h union {w}` not independent.
2. In the colouring `c_i^s`, there is a path `P` from `w` to the fixed core
   on side `s` such that
   * every internal vertex of `P` lies in the open terminal shore;
   * `P-w` uses only the two colours of the blocks
     `B_i union {w}` and `B_j`;
   * no internal vertex belongs to any fixed core block; and
   * the first core block met by `P` is `C_h^s` for some
     `h in Sigma_s`.

If neither outcome occurs, `G` is six-colourable.

#### Proof

Let

\[
       \alpha=c_i^s(w)=c_i^s(B_i),\qquad
       \beta=c_i^s(B_j).
\]

Let `Z` be the `alpha/beta` Kempe component containing `w`.

Suppose first that

\[
                         Z\cap(B_i\cup B_j)=\varnothing.       \tag{2.1}
\]

Switch `alpha,beta` on `Z`.  The only boundary vertex moved is `w`:
vertices in `B_i union B_j` are excluded by (2.1), vertices in `B_k`
have the third block colour, and the side terminal has the fourth colour.
The new exact boundary state is therefore

\[
       B_i\mid(B_j\cup\{w\})\mid B_k.              \tag{2.2}
\]

Side `s` now has a colouring with decoration state `j`.  Since
`j in Sigma_s`, contracting its supported realization gives a colouring
of the opposite closed side with the same state.  Align the three block
colours and the two terminal colours and glue the closed sides.  The two
repeated terminals receive one common fourth colour, while `U` uses the
three block colours.  Hence only four colours occur on `N(v)`, so one of
the other two palette colours may be assigned to `v`.  This gives a proper
six-colouring of `G`, a
contradiction.

Consequently `Z` meets `B_i union B_j`.  Choose a shortest path `R` in
`Z` from `w` to this set.  Its internal vertices avoid `T`: every boundary
vertex of either Kempe colour belongs to
`B_i union B_j union {w}`, and the endpoint was chosen at the first such
vertex.  The side terminal also avoids `R`, since its fourth colour is
neither `alpha` nor `beta`.  Thus every internal vertex of `R` lies in the
open terminal shore.

The endpoint of `R` belongs to the fixed core, so `R` has a first vertex
`z` in

\[
                         C_1^s\cup C_2^s\cup C_3^s.
\]

Let `P` be the prefix ending at `z`, and let `W_P=P-z`.  Then `W_P` is
connected, has exact trace `{w}`, avoids the side terminal and all three
core blocks, and has a literal edge to the unique block `C_h^s` containing
`z`.  If `B_h union {w}` is independent, `W_P` supports decoration `h`.
By the definition of the **full** support set, `h in Sigma_s`, giving
outcome 2.  Otherwise the failed independence is precisely outcome 1.
\(\square\)

## 3. Exact bilateral lock

### Corollary 3.1 (support-owned gate system)

Assume the three decorations are admissible and `G` is a counterexample.
Then

\[
                              \Sigma_1\cap\Sigma_2=\varnothing, \tag{3.1}
\]

and, for every ordered pair

\[
                  i\in\Sigma_{3-s},\qquad j\in\Sigma_s,
\]

the colouring `c_i^s` contains a terminal-free bichromatic path from `w`
whose first fixed-core hit belongs to a block indexed by `Sigma_s`.

#### Proof

An index in the intersection gives the same supported decoration on both
sides, so the audited bilateral decorated-overlap theorem six-colours
`G`.  This proves (3.1).  Theorem 2.1 applies to every ordered pair; full
admissibility removes its first outcome. \(\square\)

In particular, in the rank-one mismatch

\[
                         \Sigma_1=\{p\},\qquad
                         \Sigma_2=\{q\},                       \tag{3.2}
\]

the colouring of side 1 returned by the supported `q`-state has a clean
first-hit path back into block `p`, and symmetrically the colouring of side
2 returned by the supported `p`-state has a clean first-hit path back into
block `q`.  The mismatch is therefore not merely two abstract extension
states: it is a pair of literal **self-locking gates**, one in each open
shore.

## 4. Relation to the rural duty conversion

Apply Corollary 3.1 to the terminal-free rural triple

\[
              V(J_s^\circ)=K_s\mathbin{\dot\cup}X_s
                                      \mathbin{\dot\cup}Y_s.
\]

The first-hit path is label-faithful because its label is the actual fixed
core block it first meets; no colour is identified with a contracted pole.
It also avoids the side terminal.  Thus it is a legitimate input to the
existing protected-tree/lobe gate descent.

What is not yet proved is the final conversion.  A self-locking path may
return to the already supported pair block through a portal already owned
by the locked region, or may first hit a nontransferable central part of a
target block.  Neither event alone supplies the attained duty of the
opposite decoration.  The next constructive statement should therefore be
formulated on the two self-locking first-hit paths:

> **Self-lock gate descent.**  After choosing the fixed cores and their
> supported witnesses lexicographically minimally, the two paths in
> (3.2) either shorten/reselect one witness, expose a duty-correct pendant
> lobe transfer, give a literal `K_7`, or have common gates defining a
> colour-gluable adhesion.

Theorem 2.1 is the dynamic source of those gates.  The displayed descent is
the remaining graph-theoretic step; it cannot be replaced by an
unconditional defect-at-most-two carrier assertion.
