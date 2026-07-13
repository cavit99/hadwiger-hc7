# Exact forced-colour exchange on a removable outer fan

## 1. A path relation, not a case split

Let (P=x_1\cdots x_m) be a path.  Fix a palette (Omega) and nonempty
lists (L_i\subseteq\Omega).  Put

\[
 R_1=L_1,
 \qquad
 R_i=\{\gamma\in L_i:
          R_{i-1}\not\subseteq\{\gamma\}\}
 \quad(2\le i\le m).
 \tag{1.1}
\]

Thus (R_i) is the set of colours which can occur at (x_i) in a
proper list-colouring of the prefix (x_1\cdots x_i).

### Lemma 1.1 (exact path recurrence)

The interpretation above is exact.  In particular:

1. if (|R_{i-1}|\ge2), then (R_i=L_i);
2. if (R_{i-1}=\{\alpha\}), then
   (R_i=L_i-\{\alpha\}); and
3. the path is list-colourable if and only if (R_m\ne\varnothing).

The proof is immediate induction: a proposed colour (gamma) at (x_i)
is available precisely when some realizable colour at (x_{i-1}) differs
from (gamma).

Define the symmetric suffix sets (S_i) by applying the same recurrence
from right to left.

## 2. Exact contraction obstruction

Contract the edge (x_ix_{i+1}), and give the contracted vertex the list

\[
 L_i\cap L_{i+1}.
\]

### Theorem 2.1 (two forced shores)

If (P/x_ix_{i+1}) is list-colourable but (P) is not, then there is a
unique colour (alpha) such that

\[
 R_i=S_{i+1}=\{\alpha\}.
 \tag{2.1}
\]

Conversely, (2.1) makes the original edge uncolourable; its contraction is
colourable exactly when (alpha\in L_i\cap L_{i+1}).

### Proof

A colouring of the contraction with colour (alpha) restricts to a
prefix colouring ending in (alpha) and a suffix colouring beginning in
(alpha).  Hence
(alpha\in R_i\cap S_{i+1}).

The uncontracted path is colourable if and only if there are
(eta\in R_i) and (gamma\in S_{i+1}) with (eta\ne\gamma).
Since the two sets have a common element but admit no unequal pair, both
must be the same singleton.  This proves (2.1) and the converse. \(\square\)

This is stronger than saying that the contracted ends happen to receive
the same colour.  The two sides of the edge independently *force* that
colour.

## 3. Application to a planar shore fan

Suppose an internally four-connected triangulated disk has a removable
outer fan

\[
 F=x_1\cdots x_m
\]

whose vertices have a common internal neighbour (h).  Fix a colouring
of the graph outside (F), including the labelled external boundary
(L).  The extension problem over (F) is exactly the path problem with

\[
 L_i=\Omega-
 \bigl(\{c(h)\}\cup c(N_L(x_i))\bigr).
 \tag{3.1}
\]

Therefore a minor-critical obstruction created by contracting a fan edge
is not an arbitrary high boundary state: Theorem 2.1 gives two oppositely
oriented forced-colour chains meeting at that edge.

Likewise, if deleting the whole fan gives a colouring which does not
extend, let (j) be the first index with (R_j=\varnothing).  Then

\[
 R_{j-1}=\{\alpha\},\qquad L_j=\{\alpha\}.
 \tag{3.2}

Tracing back to the last index at which a reachable set had order at
least two gives a contiguous deterministic chain.  Every list after that
last reset has order at most two, and the forced colour changes according
to

\[
 \{\alpha\}\longmapsto L_i-\{\alpha\}.
 \tag{3.3}

Thus canonical-order fan removal converts nonextendability into a bounded
six-colour automaton on portal profiles.  No arbitrary contraction-chain
pumping is used: the entire fan and both forced relations occur
simultaneously in the original graph.

## 4. Exact Moser ordinary-profile atlas

For the reserved Moser shore, an ordinary degree-three fan vertex has one
of five root profiles and sees both (a,w).  The program
`moser_fan_forced_chain_probe.py` applies (1.1) to all

\[
 30\cdot6\cdot6=1080
\]

choices of high-root/nonstar trace, colour of (w), and colour of the
common fan neighbour (h).

Its exact output is:

* in 686 cells, no word of ordinary profiles can fail to extend;
* in the other 394 cells, a singleton ordinary row exists; and
* the shortest possible obstruction is always two consecutive copies of
  one singleton row.

The last configuration has a structural meaning.  A consecutive block of
one ordinary profile sees exactly its two root labels together with
(a,w).  In an outer fan its internal interface consists of the common
neighbour and the two ends of the block.  Hence its total interface has
order

\[
 4+3=7.
\]

So the atomic list obstruction is exactly a tight order-seven adhesion,
not a new unbounded routing pattern.  Longer deterministic chains may use
several profiles; their conversion to a covering bad split is the remaining
fan-exchange step.

## 5. Scope

Theorem 2.1 is label-free and applies at every palette size.  It supplies
the missing invariant for the non-wheel planar core: safe contraction or
fan deletion yields forced-colour chains, while repeated singleton-profile
blocks expose minimum adhesions.  It does not yet prove that every mixed
forced chain creates a crossed full split; that is the exact remaining
conversion needed to combine this note with
`hadwiger_full_split_cyclic_hull.md`.
