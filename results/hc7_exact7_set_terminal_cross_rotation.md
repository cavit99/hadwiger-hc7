# Set-terminal crosses are exact decoration rotations

**Status:** proved and independently audited as a local carrier exchange.
The
theorem converts one literal cross into either the already-audited rank-two
peel or a label-faithful move of all contacts supplied by the locked region
`L` to a named target block.  It is not a palette-to-label inference.

## 1. Labelled setting

Let `K,A,B` be disjoint connected pairwise adjacent core blocks with fixed
adhesion traces.  Assume

\[
                         K\cap T=\{x,y\},                       \tag{1.1}
\]

the carrier `K` is three-connected, and `xy` is absent.  Its two literal
trace vertices retain an edge to the trace of each target block `A,B`.
Let `L` be a connected set disjoint from the core, put

\[
                         P=N(L)\cap K,                           \tag{1.2}
\]

and assume `L` is anticomplete to `A union B`.  In the exact-six
application `W=\{w\} union L` is the connected decorated block and
`|P|>=5`.

Let `q in K-(\{x,y\} union P)` have a literal edge to one named target,
say `A`.  Let `p in P`.

## 2. Cross-to-rotation theorem

### Theorem 2.1 (peel or exact decoration rotation)

If `K` contains vertex-disjoint paths joining respectively

\[
                              x-y,\qquad q-p,                    \tag{2.1}
\]

then one of the following occurs.

1. `K` has a label-faithful peel toward `A`; hence `L` contacts both the
   retained pair carrier and the enlarged target block.
2. There is another three-block core `K',A',B` with exactly the same
   adhesion traces and pairwise adjacencies such that

   \[
                     N(L)\cap K'=empty,qquad E(L,A')\ne empty.  \tag{2.2}
   \]

   Thus the `L`-based contact has moved literally from the pair carrier to
   the named target `A`.  Under the inherited raw-rank-one hypothesis this
   is the unique raw decoration.  In the exact decorated cell it is a
   supported target decoration precisely when
   `\{w\} union (A cap T)` is independent; otherwise the failed
   independence is the corresponding literal boundary-incompatibility
   certificate.

#### Proof

By the connected-pair linkage equivalence in the audited block-terminal
theorem, (2.1) gives a nonseparating `x-y` path `R` avoiding `q,p`.  Put

\[
                         C=K-V(R).                              \tag{2.3}
\]

Then `C` is connected and contains both `q,p`.

If `R` meets `P`, the partition

\[
                         V(K)=C\mathbin{\dot\cup}V(R)            \tag{2.4}
\]

is exactly a labelled peel toward `A`: both sides are connected; the
whole trace `{x,y}` lies on the retained `R` side; `C` contains the portal
`q`; and both sides meet `P` because `p in C` while `R cap P` is nonempty.
This is outcome 1.

Assume now that `R cap P=empty`.  Then every member of `P` lies in the
connected set `C`.  Define

\[
                         K'=G[V(R)],\qquad A'=G[A\cup C].         \tag{2.5}
\]

The set `A'` is connected through the literal `A-q` edge, and `K'` is the
path `R`.  The two new blocks are disjoint.  They are adjacent because the
connected carrier `K` has an edge between the nonempty parts `R,C`.
The old `A-B` edge remains, while `K'` retains its old literal trace edge
to `B` and its old literal trace edge to `A subseteq A'`.  Hence
`K',A',B` remain pairwise adjacent.

All vertices of `C` are nontrace carrier vertices: `R` contains both
`x,y`, and `K` had no other adhesion vertex.  Thus (2.5) preserves every
trace.  Since `P subseteq C`, the literal `L-P` edges make `L` adjacent to
`A'`.  Since `R cap P=empty` and `P=N(L) cap K`, `L` is anticomplete to
`K'`.  This proves (2.2).

Finally, geometric support of `W` at `A'` is now literal.  The only
remaining supported-state condition is independence of its unchanged
trace with `w`, exactly as asserted. \(\square\)

## 3. Consequence for the spanning rural quadrichotomy

### Corollary 3.1 (a cross aimed at the opposite state glues)

Work in the exact bilateral decorated Moser cell with the same labelled
frame on both terminal shores.  Suppose one side supports the pair-carrier
decoration `w->K` and the other supports `w->A`.  If the first side has a
set-terminal cross (2.1) whose portal `q` is labelled to `A`, then `G` is
six-colourable.

#### Proof

Admissibility of the trace of `A` depends only on the literal edges from
`w` to the common adhesion, so the fact that `w->A` is supported on the
opposite shore makes the same trace admissible on the first side.  Apply
Theorem 2.1 there.  In outcome 1 the peel makes `W` contact `A` as well as
the retained pair carrier; in outcome 2 the exact rotation makes it
contact `A` instead.  In either case the first side now supports `w->A`.
The audited bilateral decorated-overlap theorem aligns this common exact
state and six-colours `G`. \(\square\)

Thus a surviving cross may only point at a target state which is not the
state supported on the opposite shore (or expose the already named
boundary-incompatibility certificate).

Whenever the set-terminal cross in
`../results/hc7_exact7_spanning_rural_quotient.md` uses a portal which is
already labelled to `A` or `B`, has its other end in the original set
`N(L) cap K`, and the spanning carrier avoids the side terminal, Theorem
2.1 discharges that outcome completely:

\[
             \text{cross}\Longrightarrow
             \text{rank promotion or exact named decoration rotation}.
                                                                    \tag{3.1}
\]

For a general cross returned by the spanning theorem, either endpoint may
have only a topological pole duty: the `Q` end may contact an absorbed part
of the target pole, and the `P` end may contact `Y-L` rather than `L`.
Moreover the spanning carrier may contain the side terminal.  In those
cases an endpoint-transfer and side-terminal reassignment must first be
made without changing the attained boundary duty.  These qualifications
are the exact remaining label-assignment conditions; the local carrier
path argument itself is finished by Theorem 2.1.
