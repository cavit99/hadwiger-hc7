# Bilateral packet derangement has genuine cycle realizations

## 1. Purpose

Corollary 6.6 of `hadwiger_double_interface_contraction_exchange.md`
reduces the four-block XOR residue to three normalized modes on which the
minimum shore and the accepting shore own disjoint packet types.  This note
tests whether the abstract derangement is already impossible for actual
portal graphs.

It is not.  Five of the ten choices of the two locked modes have exact
realizations by two labelled cycles.  Thus packet geometry alone cannot close
the residue; the minimum-fragment/interface placement and (K_7)-minor
exclusion must be used.

## 2. Cycle societies

For a circular order (O) of the seven labels, let (R(O)) be a cycle with
one vertex (p_s) for each (s\in S), in order (O), and let the portal set
of (s) be the singleton \(\{p_s\}\).  This is a connected full shore.

For two disjoint two-label blocks (ab,cd), the shore (R(O)) has an
(ab|cd)-packet if and only if the four labels do **not** alternate in
(O).  The forward implication is the elementary crossing obstruction on a
circle.  For the reverse implication, choose the two disjoint cycle arcs
joining the nonalternating pairs.  Consequently a normalized three-pair mode
is totally packet-deficient precisely when its three matching edges are
pairwise alternating in (O).

## 3. Five exact derangements

Number the normalized modes as in
`hadwiger_moser_matching_holonomy.md`.  The following table gives an accepting
order (O^*) and a minimum-side order (O).  In every row:

* (R(O^*)) is totally packet-deficient for the two displayed locked modes;
* (R(O^*)) owns at least one packet type for each other mode;
* (R(O)) owns at least one packet type for every mode; and
* for each of the three nonlocked modes, the packet-type sets of (R(O^*))
  and (R(O)) are disjoint.

\[
\begin{array}{c|c|c}
\text{locked modes}&O^*&O\\ \hline
1,2&(0,1,4,5,3,2,6)&(0,1,2,6,5,4,3)\\
1,3&(0,1,2,5,6,3,4)&(0,1,2,3,6,5,4)\\
2,5&(0,1,6,5,3,4,2)&(0,1,2,3,6,5,4)\\
3,4&(0,1,2,6,3,4,5)&(0,1,2,6,5,4,3)\\
4,5&(0,1,5,6,3,2,4)&(0,1,2,3,6,5,4)
\end{array}                                      \tag{3.1}
\]

Each assertion is checked merely by the four-point alternation criterion.
The dependency-free exhaustive verifier
`moser_bilateral_cycle_derangement.py` prints the packet type on both sides
for every mode.  It searches the (720^2) labelled order pairs and exhausts
the full set whenever no witness exists.  Exactly the five locked pairs in
(3.1) have a cycle realization; the other five do not.

The five surviving locked pairs are

\[
12,13,25,34,45,
\]

which themselves form a five-cycle on the five normalized modes.  This is
the same five-cycle that appears as the exact-two-signature residue in the
matching circular-order census.

## 4. Consequence

The derangement in Corollary 6.6 is compatible with honest connected portal
graphs and honest vertex-disjoint path packets.  It is not merely a Boolean
or set-system artefact.  A proof that only compares which packet types occur
on the two shores cannot eliminate the five rows of (3.1).

These cycle societies are not asserted to satisfy ambient
seven-connectivity or the atomic interface rows.  Those are now the exact
remaining source of leverage.  Concretely, a successful exchange lemma must
show that the alternating XOR cycle in the minimum fragment cannot project
its seven portal classes to one of the five orders (O) in (3.1) while the
opposite common web has order (O^*).  Failure of such a projection should
produce the desired exact seven-adhesion.  Merely invoking gammoid exchange
or packet ownership is insufficient.
