# Independent audit of the bichromatic gate theorem

## Verdict

**GREEN.**  The set-Menger dichotomy, both exact cuts, both peel
certificates, and the two-lobe minimal-bag lemma in
`hadwiger_bichromatic_gate_peel_or_adhesion.md` are correct.  The result
does not by itself close the three-path branch, and Section 7 correctly
states that limitation.

The accompanying finite falsification probe has also been made
dependency-free and replayed successfully.

## 1. Set-Menger and the exact cuts

Deleting the four roots (X) from a six-connected graph leaves a
two-connected graph: deleting one additional vertex removes only five
vertices from the original graph.  Contract the connected, anticomplete
sets (A,B) to two terminals and use the terminal form of vertex Menger.
This is the form in which path endpoints may coincide inside (A) or
inside (B), while path interiors are disjoint.  Its dual separators do
not contain either terminal.

Consequently the local (A)-(B) connectivity in (H-X) is at least
two.  It is either at least three, giving the three paths, or it equals
two and a separator ({p,q}) exists outside (Acup Bcup X).  In the
latter case (Xcup{p,q}) really separates the nonempty sets (A,B)
in (H).  Its order is six, and six-connectivity makes it a minimum
("exact") six-cut.  When (H=G-v), adding (v) to the cut removes every
new route through the apex, so the displayed order-seven set separates
the same two sides in (G); seven-connectivity makes it exact.

When lifting paths after contracting (A,B), take the first edge out of
(A) and the last edge into (B), or equivalently trim each path.  The
interiors then avoid (Acup B), as required by the later branch-set
arguments.

## 2. Peel certificates

For Lemma 3.1 the proposed six bags are

\[
                  A\cup P, B, Q, R_j\ (j\ne i).
\]

The edge (PB) repairs the deficient pair, (PQ) preserves the split
bag adjacency, (QB) and (QR_j) give every contact required of the
residue, and all contacts from (A\cup P) to the untouched rooted bags
survive through (A).  No adjacency is implicit.

For Lemma 3.2 the six bags

\[
 A\cup P_1, B\cup P_2, Q_1, Q_2, R_3, R_4
\]

are connected and disjoint.  The literal root edge (x_1x_2) joins the
first two; (P_iQ_i) gives the two own-residue contacts; item 3 gives
the crossed residue contacts; (Q_1Q_2), the four (Q_iR_j) contacts,
and the old gate contacts give all remaining pairs.  The stated
replacement of a gate--residue edge by (P_1Q_2) or (P_2Q_1) is valid
because the corresponding (P_i) already belongs to the enlarged gate
bag.

## 3. Minimal two-lobe structure

For a component (C) of (R_i-x_i), every other component has a
neighbour at (x_i), so (R_i-C) is connected.  It retains both gate
contacts at (x_i), the root, and the mate-bag contact through the
literal matching edge (x_ix_{\bar i}).  Minimality therefore forces it
to lose one of exactly the two nonmate bag contacts.  Equivalently, every
(R_i)-side endpoint of that contact lies in (C).

One target bag cannot charge two different components: its nonempty set
of neighbours in (R_i) cannot be contained in two disjoint components.
There are only two nonmate target bags, so there are at most two
components; if there are two, their charges are distinct and hence
bijective.  This also covers the singleton-root case, where there are no
components.

## 4. Kempe switch and scope

The Menger separator is disjoint from the two gate sets.  In the Moser
specialization it is therefore disjoint from (K_0), so switching the
two omitted colours on (K_0) fixes every vertex of the actual adhesion.
The note correctly allows (p,q) to lie in some other component of the
two omitted colour classes; they need not lie in the four-colour core.

The theorem stops at the right point.  Three root-avoiding paths through
the contracted lobe skeleton do not force a peel: the ten-vertex quotient
in Section 7 has no (K_6)-minor.  After replacing its NetworkX-only
local-connectivity call by an exhaustive search through the four lobe
vertices, `bichromatic_gate_lobe_probe.py` reproduces that survivor with
no third-party dependencies.

