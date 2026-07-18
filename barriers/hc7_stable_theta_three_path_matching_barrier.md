# Three terminal-capacitated paths do not force matching sector defects

**Status:** explicit finite barrier with deterministic verifier; independent
audit pending.  This graph is not seven-connected and is not asserted to be
contraction-critical or `K_7`-minor-free.

The accompanying checker is
[`hc7_stable_theta_three_path_matching_barrier_verify.py`](hc7_stable_theta_three_path_matching_barrier_verify.py).

## Refuted statement

The following inference is false without additional host hypotheses.

> Let an order-seven boundary be partitioned as
> (T=U\mathbin{\dot\cup}B), where (|U|=4) and (|B|=3).  Suppose a
> degree-eight vertex has five pairwise disjoint, cyclically adjacent
> connected sets through its five non-`B` neighbours, with the four members
> of `U` in four distinct sets.  Suppose also that a disjoint connected set
> meets seven of the eight labels, and that three paths from one vertex of
> `B` to a prescribed two-set in `U` are pairwise disjoint outside their
> prescribed terminals.  Then the nonadjacency graph between `B` and the
> five cyclic connected sets is a matching of order at most two.

Thus the three-path packing furnished by terminal-capacitated Menger does
not, by itself, supply the incidence hypothesis of the cyclic
connected-set contact-allocation theorem.

## Construction

Put

\[
 U=\{u_0,u_1,u_2,u_3\},\qquad B=\{b,q,r\},\qquad T=U\mathbin{\dot\cup}B.
\]

Let

\[
 L=\{v,x_0,x_1,x_2,x_3,x_4\},\qquad R=\{d,e,f\}.
\]

The vertices `x_0,...,x_4` induce the cycle

\[
                         x_0x_1x_2x_3x_4x_0.             \tag{2.1}
\]

Add the four edges `u_i x_i` for (0\le i\le3), and make `v`
adjacent exactly to

\[
                         B\cup\{x_0,x_1,x_2,x_3,x_4\}.  \tag{2.2}
\]

Make `R` a triangle and add every edge between `R` and `T`.  Add every
edge from a vertex of `B` to a vertex of

\[
 \{u_0,x_0,u_1,x_1,u_2,x_2,u_3,x_3,x_4\},              \tag{2.3}
\]

except the three edges

\[
                              ru_1,\quad rx_1,\quad rx_4. \tag{2.4}
\]

Finally add the root cycle

\[
                              u_0u_1u_2u_3u_0.           \tag{2.5}
\]

There are no edges from `L` to `R`.  These rules completely define `G`.

## The literal branch-set data

Put

\[
 C_i=G[\{u_i,x_i\}]\quad(0\le i\le3),\qquad
 C_4=G[\{x_4\}],\qquad D=G[R].                         \tag{3.1}
\]

The five sets are pairwise disjoint, nonempty and connected.  Consecutive
sets are adjacent through (2.1).  Each contains the specified neighbour
`x_i` of `v`, and the four roots occur in four distinct sets.  Also

\[
                              d_G(v)=8.                  \tag{3.2}
\]

The connected set `D` is adjacent to each singleton label in `B` and to
`C_0,C_1,C_2,C_3`, through the corresponding boundary roots.  It is
anticomplete to `C_4`, because `C_4` lies in `L` and there are no
`L`--`R` edges.  Thus `D` meets exactly seven of the eight labels

\[
                         B,C_0,C_1,C_2,C_3,C_4.          \tag{3.3}
\]

With (I=\{u_0,u_2\}), the three paths

\[
                  bdu_0,\qquad beu_0,\qquad bfu_0       \tag{3.4}
\]

are pairwise vertex-disjoint outside the allowed terminal set

\[
                              \{b\}\cup I.              \tag{3.5}
\]

Their final vertices are allowed to coincide, exactly as in the
terminal-capacitated packing theorem.

Nevertheless the bipartite nonadjacency graph between `B` and
`C_0,...,C_4` is

\[
                              \{rC_1,rC_4\}.             \tag{3.6}
\]

The two edges share `r`, so (3.6) is not a matching.

## Exact consequence and missing hypotheses

The path packing lies wholly on the far closed shore, whereas the
singleton-to-sector incidence graph records independently chosen edges
from the boundary into the opposite shore.  The three paths therefore do
not force the matching-defect hypothesis needed by contact allocation.

This example is intentionally not an `HC_7` host: for example `x_1` has
degree six, so the graph is not seven-connected.  It also does not encode
the universal proper-minor colouring responses of a hypothetical
minor-minimal counterexample.  A positive continuation must use those
missing host hypotheses to turn a rooted nonmatching defect into an
explicit `K_7`-minor model, a colour-compatible order-seven separation, or
a strict full-neighbourhood-separator descent.  The barrier says only that
the three already-proved combinatorial outputs cannot be composed by
incidence counting alone.
