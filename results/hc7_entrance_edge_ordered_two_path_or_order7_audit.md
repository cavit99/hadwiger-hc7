# Audit of the entrance-edge ordered-two-path alternative

**Audit status:** separate internal audit; **GREEN**.

**Audited source:**
[`hc7_entrance_edge_ordered_two_path_or_order7.md`](hc7_entrance_edge_ordered_two_path_or_order7.md)

**Promoted source SHA-256:**
`a24964893bc7ed9cb2b46d6025c93c9c744ceecd7e683d0666b910f23741fd4a`

**Pre-promotion source SHA-256:**
`6b88f6f9188ece166a597926421bd5885be00452f5b3e86e2b1a1e12dc766a25`

The promoted source differs from the audited active draft only in its
opening status paragraph: the pending-audit wording was replaced by a link
to this GREEN audit.  Reversing that metadata-only edit reproduces the
pre-promotion hash above.  The theorem statement, proof, corollary,
references, and trust boundary are unchanged.  This audit therefore binds
the same mathematical revision at its promoted path and current hash.

**Scope:** Theorem 1, Corollary 2, the stated trust boundary, and the use of
Jung's two-linkage theorem.  This is an internal mathematical audit, not
external peer review.

## Verdict

The theorem and corollary are correct as written.  The proof yields exactly
the claimed alternative:

1. two vertex-disjoint paths preserving both nominated initial edges and all
   six terminal identities; or
2. an actual order-seven separation containing the two outside ends, with
   every component outside the boundary adjacent to every boundary vertex.

The source correctly states that the separator alternative does **not**
provide a common closed-shore colouring partition and that the theorem does
not solve the two-demand branch-set allocation problem or `HC_7`.

No unresolved mathematical assumption remains within the stated scope.

## Detailed audit

### 1. Connectivity after deleting the outside ends

Set

\[
                     J=G-\{x_0,y_0\}.
\]

The inference that `J` is five-connected is valid.  If deleting a set `W`
of at most four vertices disconnected `J`, then deleting
`W\cup\{x_0,y_0\}` would disconnect `G` after removing at most six vertices,
contrary to seven-connectivity.

The order condition is also handled correctly.  Since `G` is
seven-connected, it has at least eight vertices, so `J` has at least six.
If `|V(J)|=6`, then `|V(G)|=8`; seven-connectivity forces minimum degree at
least seven and therefore `G=K_8`.  The paths

\[
                     x_0x_1x_2,\qquad y_0y_1y_2
\]

are then present and disjoint because the six nominated vertices are
pairwise distinct.  This explicit case is necessary under the standard
convention that `K_6` is five-connected rather than six-connected.

Consequently the remaining argument may assume `|V(J)|>=7`.

### 2. The six-connected branch

The cited external input is correct:

> Every six-connected graph is two-linked.

The source identifies the original reference as H. A. Jung,
“Eine Verallgemeinerung des n-fachen Zusammenhangs fuer Graphen,”
*Mathematische Annalen* **187** (1970), 95--103, and gives the traceable
modern restatement in Stephens--Ye, *Connectivity for Kite-Linked Graphs*,
Theorem 1.1, arXiv:1912.02873.

Applying the theorem in `J` to the distinct pairs

\[
                       (x_1,x_2),\qquad (y_1,y_2)
\]

gives vertex-disjoint paths `Q_x,Q_y`.  Neither `x_0` nor `y_0` belongs to
`J`.  Hence prepending `x_0x_1` to `Q_x` and `y_0y_1` to `Q_y` introduces no
repeated vertex.  The resulting paths remain vertex-disjoint because the
two outside ends are distinct and each is absent from both original paths.
They encounter the nominated triples in the required orders.

### 3. The non-six-connected branch

Here `J` is five-connected, has at least seven vertices, and is not
six-connected.  Therefore its vertex connectivity is exactly five, so
there are disjoint nonempty sets `A,B` and a five-set `T` such that

\[
                  V(J)=A\mathbin{\dot\cup}T
                         \mathbin{\dot\cup}B
\]

and no edge joins `A` to `B`.

The set

\[
                         S=T\cup\{x_0,y_0\}
\]

has order seven because `T\subseteq V(J)`.  Moreover `G-S=J-T` contains
vertices in both `A` and `B`, and no edge joins those two sets.  Thus `S`
is the boundary of an actual order-seven separation, rather than merely an
auxiliary quotient separator.

### 4. Fullness of the returned boundary

Let `C` be any component of `G-S`.  All neighbours of `C` outside `C` lie
in `S`.  If `C` had no neighbour at some `s\in S`, then

\[
                          N_G(C)\subseteq S-\{s\},
\]

so `|N_G(C)|<=6`.  There is another component of `G-S`, because the sets
`A` and `B` lie on different sides.  Hence deleting `N_G(C)` separates `C`
from that component, contradicting seven-connectivity.  It follows that
every component of `G-S` is adjacent to every literal vertex of `S`.

### 5. Corollary and trust boundary

Corollary 2 explicitly assumes that the two entrance edges are disjoint and
that all six nominated vertices are pairwise distinct.  These are exactly
the terminal hypotheses of Theorem 1, so the corollary is a valid direct
application.

The source also records all material limitations correctly:

- each output is a path with one fixed entrance edge and one further
  nominated terminal, not a branching connected subgraph meeting two
  independent terminal sets;
- no ownership by inherited branch-set labels is inferred;
- the order-seven separation carries no automatically compatible equality
  partition;
- no `K_7`-minor exclusion or contraction-critical colouring response is
  used; and
- the theorem therefore does not prove `HC_7`.

The cited adjacent barrier is used only for sharpness.  The theorem's proof
does not depend on that barrier.

## Final determination

The audited revision is suitable for promotion as a proved, separately
internally audited host-level separator alternative.  Any later application
must separately establish that the returned order-seven boundary carries a
common complete colouring partition, or must spend the additional
contraction-critical hypotheses to obtain an explicit `K_7`-minor model.
