# Packet demand as clique-deletion chromatic number

**Status:** proved and independently audited.

## Theorem

Let `H` be a finite graph.  Let `P(H)` be the set of partitions `Pi` of
`V(H)` into independent blocks.  Write `sing(Pi)` for the vertices whose
blocks in `Pi` are singletons, and define

\[
 d_H(\Pi)=|\Pi|-\omega\bigl(H[\operatorname{sing}(\Pi)]\bigr),
 \qquad
 \delta_{\rm pkt}(H)=\min_{\Pi\in P(H)}d_H(\Pi).
\]

We admit the empty set as a clique and use
`omega(empty)=chi(empty)=0`; the empty graph has its unique empty
independent-block partition.  With these conventions,

\[
 \boxed{
 \delta_{\rm pkt}(H)
 =\min\{\chi(H-U):U\subseteq V(H),\ H[U]\text{ is a clique}\}.}
 \tag{1}
\]

Consequently `delta_pkt(H)<=2` if and only if `H` has a clique `U` such
that `H-U` is bipartite; equivalently, `H` has a clique odd-cycle
transversal.

## Proof

Fix an independent-block partition `Pi`, and let `U` be a maximum clique in
`H[sing(Pi)]`.  Delete the `|U|` singleton blocks belonging to `U`.  Every
remaining block of `Pi` is still independent, and these

\[
 |\Pi|-|U|
 =|\Pi|-\omega\bigl(H[\operatorname{sing}(\Pi)]\bigr)
 =d_H(\Pi)
\]

blocks partition `V(H)-U`.  Therefore

\[
 \chi(H-U)\le d_H(\Pi).
\]

Taking first the minimum over clique sets `U` and then the minimum over
partitions `Pi` proves that the right side of (1) is at most its left side.

Conversely, fix a clique `U` and a proper `k`-colouring of `H-U`, where
`k=chi(H-U)`.  Form an independent-block partition `Pi_U` from the `k`
colour classes of `H-U` together with one singleton block for each vertex
of `U`.  The singleton-block graph of `Pi_U` contains the clique `U`; it may
also contain singleton colour classes, which only increase its clique
number.  Hence

\[
 d_H(\Pi_U)
 \le (k+|U|)-|U|
 =k.
\]

Minimizing over clique sets `U` proves the reverse inequality in (1).

Finally, the right side of (1) is at most two exactly when some clique
deletion leaves a graph of chromatic number at most two, which is exactly a
bipartite graph.  This proves the consequence.  `square`

## HC7 interpretation and trust boundary

This identity gives a structural name to every two-packet-reflectable
boundary target:

1. retain a clique `U` as singleton blocks; and
2. use the two colour classes of a bipartition of `H-U` as the funded
   nonsingleton blocks.

Combined with the already-audited 129-boundary census, it says that the 119
residuals admitting a demand-at-most-two partition are precisely the
residuals having a clique odd-cycle transversal, while the ten
absolute-demand-three residuals have none.

The theorem is purely combinatorial.  It does **not** show that a legal
proper-minor operation on the thin shore returns the desired partition, nor
does it close an actual `(1,2)` adhesion.  It replaces a list of safe states
by the uniform target “force a clique-OCT state.”
