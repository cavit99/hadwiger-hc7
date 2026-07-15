# Audit: six-terminal irreducible-kernel classification

## Verdict

**GREEN.**  The proof in
[`hc7_six_terminal_kernel_classification.md`](hc7_six_terminal_kernel_classification.md)
correctly classifies the one-nonterminal irreducible kernels and proves
that every six prescribed vertices of a simple three-connected graph have
a rooted `C_6` model.  The exhaustive checker agrees with the hand proof
but is not needed by it.

## 1. Kernel reduction and contraction criterion

The previously audited terminal-legal kernel theorem gives a spanning
rooted kernel of order six or seven.  In the order-seven branch the unique
nonterminal `v` is incident only with terminal-legal edges, so
irreducibility makes every edge at `v` noncontractible.

Lemma 2.1 is valid.  After contracting `vx` to `z`, a deletion avoiding
`z` lifts to the same deletion in the three-connected graph `M`.  Deleting
`z`, and possibly one further vertex, leaves `H-x`, or one vertex deleted
from `H-x`; these graphs are connected because `H-x` is two-connected.
Thus the simplified contraction is three-connected.

## 2. Hamiltonicity of the six-terminal remainder

Put `H=M-v`.  Wu's theorem supplies at least four neighbours of `v` of
degree three in `M`, hence at least four degree-two vertices in `H`.  With

```text
D={x:d_H(x)=2},   B=V(H)-D,
```

we have `|B|<=2`.  The cases `|B|=0,1` reduce correctly to a cycle.

The only substantive case is exactly `B={a,b}`.  Every component of
`H[D]` is an `a-b` path: a cycle component would disconnect `H`, and a
path whose two external attachments coincide would make `a` or `b` a
cutvertex.  Suppression therefore gives parallel `a-b` routes, at most one
of which is the literal edge `ab`.  There are at least three routes because
both branch vertices have degree at least three.

If there are exactly two long routes, their union contains all four
vertices of `D` and is a Hamilton cycle.  Hence a non-Hamiltonian remainder
has at least three long routes.  Their positive weights sum to four, so
one is `a-x-b`.  Removing `x` leaves at least two expanded `a-b` routes
covering every remaining vertex, and consequently `H-x` is
two-connected.  Since `M-{a,b}` is connected while `x` has only `a,b` as
neighbours in `H`, the edge `vx` is forced.  Lemma 2.1 then contradicts
irreducibility.  This closes the only nontrivial branch.

## 3. Exact order-seven types

Let `C` be the Hamilton cycle in `H`, and let `A` be Wu's set of at least
four degree-two vertices of `H`.  No member of `A` can be a chord end, so
all chord ends lie in the at-most-two-set `T-A`.  Therefore `H` has at most
one chord.

If there is no chord, `H=C_6`.  A missed rim terminal would lie in a
maximal interval of missed terminals; deleting the two distinct boundary
neighbours of that interval separates it from `v` and the rest of the
rim.  Three-connectivity therefore forces `v` to be universal.

If there is a chord `uw`, then `A=T-{u,w}`.  Thus `v` is adjacent to the
other four terminals and may independently see either chord end.  A
distance-two chord has an intervening vertex `x in A`; then `H-x` is the
five-cycle formed by the chord and the opposite rim arc.  Because `vx` is
present, Lemma 2.1 makes `vx` contractible.  Hence the sole chord must join
opposite rim vertices.  These are exactly the four rooted types stated in
the theorem.

For an order-six kernel, minimum degree three and Dirac's circumference
bound give a spanning `C_6`.  Expanding the terminal-legal contractions
preserves all six distinct roots and all cycle adjacencies, so the global
rooted-model conclusion follows.

## 4. Independent replay

Running

```text
python3 active/hc7_six_terminal_kernel_probe.py
```

returns `17` three-connected order-six graphs, all Hamiltonian, and exactly
`4` rooted irreducible order-seven isomorphism types, with no
nonclassified instance.  This matches the structural proof exactly.
