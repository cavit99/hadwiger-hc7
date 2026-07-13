# Archived audit addendum: block-terminal cell evacuation

**Archived after merger into
`../results/hc7_exact7_block_terminal_web_audit.md`.**

Audited source: Section 5 of `results/hc7_exact7_block_terminal_web.md`
(the source was promoted from `active/` while this audit was running).

## Verdict

Lemma 5.1 and Theorem 5.2 are **GREEN under the inherited Section 3
setting**.  For standalone use, Lemma 5.1 should say explicitly that it
retains all of that setting, in particular

\[
 L\subseteq W,
 \qquad P^\circ\subseteq N_G(L)\cap V(K),
 \qquad |P^\circ|\ge3,
\]

that `P^circ` lies on the rib, and that the exact trace of `K` supplies
literal old adjacencies to both target blocks.  These facts are present in
the surrounding section and are exactly what its proof uses.

## 1. Connectivity after deleting the cell

Let `D` be one actual carrier component in a cell behind `Delta`.  The
proved equality `N_K(D)=V(Delta)` makes `D` a component of
`K-V(Delta)`.  There is another component containing the marked rib
vertices outside the three-element gate.  Three-connectivity makes every
component of `K-V(Delta)` adjacent to all three gate vertices.  Hence the
union of `V(Delta)` with any one far component is connected and contains
all three gate vertices, and every additional component attaches to it.
Therefore `K-D` is connected.

This remains true in the hostile triangle 3-sum example where deleting
`D` lowers the carrier's connectivity from three to one or two.  The
competitor in the lexicographic optimization is required only to be a
connected branch-set realization, so no preservation of
three-connectivity is needed.

## 2. The four reallocations

The two binary questions “does `D` see `W`?” and “does `D` see
`A union B`?” give exactly the four cases listed.

1. If it sees neither, leaving `D` unused preserves every branch set.
2. If it sees only `W`, `W union D` is connected and sees `K-D` through
   the literal `D-Delta` contacts.
3. If it sees a target `A_0` but not `W`, `A_0 union D` is connected.
   It remains adjacent to `K-D` through the unchanged literal trace edge,
   and to the other target through the old target-target adjacency.
4. If it sees both, moving `D` into `W` keeps the `W-(K-D)` contact
   through `Delta` and retains (indeed may add) the target contact through
   the literal `D-A_0` edge.

If `D` sees both target blocks, choosing either one in case 3 is harmless:
the other contact becomes an additional target-target edge.  In every
case the moved or discarded set contains no adhesion vertex, so all four
literal traces are unchanged and all three core blocks remain disjoint,
connected, and pairwise adjacent.

In cases 1 and 3, `W` is not enlarged.  Its contact with the smaller
carrier is nevertheless retained because every member of `P^circ` lies
on the rib, outside `D`, and is a literal neighbour of the fixed
`L subseteq W`.  This is why the inherited `L,P^circ` hypotheses should
be explicit in Lemma 5.1.

## 3. Raw and admissible ranks

No old `W` contact is lost.  In cases 2 and 4, a possible former
`W-D` contact to the old carrier becomes internal, but the actual
`D-Delta` edges replace it by a contact to `K-D`.  Contacts to `A,B`
whose endpoints were already in `W` remain.  Case 4 can add one or both
target contacts.

Admissibility depends only on `w` and the fixed literal trace of the
contacted core block.  Since every trace is unchanged, retaining a raw
contact retains its old admissibility, while a new raw contact is counted
as admissible exactly when its unchanged trace permits it.  Thus the
admissible rank is nondecreasing first, and the raw rank is nondecreasing
second, in the stated lexicographic order.

## 4. Why the optimization fixes `L` and the threshold

Theorem 5.2 correctly optimizes over **all** supported realizations with
the frame traces fixed, the same connected set `L subseteq W`, and
`|N_G(L) cap V(K)|>=5`, before asking whether its selected carrier is
three-connected.  Corollary 4.1 says `E(D,L)=empty`, so evacuation leaves

\[
 N_G(L)\cap(V(K)-D)=N_G(L)\cap V(K)
\]

literally unchanged.  The competitor therefore remains in the same
optimization domain.  Without fixing `L` and this threshold, minimizing
`|K|` could compare unrelated decorations and would not contradict the
chosen five-attachment lock.

The evacuated carrier need not preserve the three-bypass portals, the web
certificate, or three-connectivity.  None is required of a competitor.
If the selected lex-optimal carrier is three-connected, any nonempty cell
would provide the strictly smaller valid competitor above, so all its
vertices lie on the planar rib.  This proves Theorem 5.2 exactly.
