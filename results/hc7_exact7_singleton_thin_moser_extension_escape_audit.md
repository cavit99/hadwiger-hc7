# Independent audit: singleton-thin reduction and `M+13` packet escape

Audited file:
`results/hc7_exact7_singleton_thin_moser_extension_escape.md`.

**Overall verdict:** E2 **GREEN**; E4 **GREEN in the precise singleton-thin
`M+13` setting**, with the packet-escape branch sets supplied explicitly
below.  The surviving conclusion is only packet entanglement, not a
reserved connector or a new packet.

## E2. Dirac reduction and the frozen 129 census

### E2(a): conceptual implication — GREEN

Let

\[
                V(G)=\{q\}\mathbin{\dot\cup}S
                     \mathbin{\dot\cup}R,
\]

where `q` is anticomplete to `R` and `N(q)=S`, `|S|=7`.  Then `d(q)=7`.
For a seven-contraction-critical graph, Dirac's neighbourhood inequality
gives

\[
                \alpha(G[N(q)])\le d(q)-7+2=2.
\]

Thus, with `H=G[S]=G[N(q)]`,

\[
                            \alpha(H)\le2.
\]

This implication is conceptual and does not use the boundary census.

### E2(b): identification inside the 129 residuals — GREEN, census-dependent

The conclusion “`H` is `M` or `M+13`” does **not** follow from
`alpha(H)<=2` alone.  It uses the additional assumption that `H` belongs to
the already-audited 129-graph residual of the adaptive `(1,2)` census.

The frozen verifier
`results/hc7_exact7_adaptive_12_boundary_verify.py` asserts that the residual
counter is

```text
(alpha=2, some_safe=False): 1
(alpha=2, some_safe=True):  1.
```

A targeted isomorphism extraction using the verifier's existing residual
predicates gives exactly:

* the eleven-edge Moser spindle

  \[
  E(M)=\{01,02,03,04,12,16,26,34,35,45,56\};
  \]

* its twelve-edge extension `M+13`.

The first atlas representative already has the displayed labelling.  For
the second, an explicit isomorphism from the displayed `M+13` to the atlas
representative is

```text
0->3, 1->0, 2->6, 3->4, 4->2, 5->1, 6->5.
```

The edge counts distinguish the two types.  This certifies the names of the
two already-counted alpha-two orbits; it is not a new classification of all
seven-vertex alpha-two graphs.

## E4. The `M+13` Kempe/packet-escape package

Assume henceforth the exact singleton-thin separation above, with
`H=M+13`, and let `P1,P2` be disjoint connected `S`-full packets in `R`.

### E4(a): unique safe state — GREEN, finite boundary fact

Among all proper equality partitions of the labelled `M+13` boundary with
at most six blocks, the existing partition enumeration has exactly one of
packet demand at most two:

\[
                    \Pi^*=\{0\}\mid\{1\}\mid\{3\}
                           \mid\{2,5\}\mid\{4,6\}.
\]

Indeed, the singleton vertices `0,1,3` induce the triangle created by the
added edge `13`, so `d_H(Pi*)=5-3=2`.  The frozen enumeration finds no other
safe partition.  The only seven-block partition is the all-singleton one;
it has demand `7-omega(H)=4`, so `Pi*` is also unique if all independent
partitions are allowed.  This is an abstract boundary classification; by
itself it does not force a legal shore colouring to realize `Pi*`.

### E4(b): exact `25` trace and Kempe exchange — GREEN

Contract the connected star `q union {2,5}` and six-colour the proper
minor.  Delete the contracted connector `q` and expand only the independent
literal block `25` on the closed rich shore

\[
                            J=G[R\cup S].
\]

Fullness of `q` makes `25` an **exact** boundary block: its representative
is adjacent to every literal in `S-{2,5}`.

In a hypothetical counterexample, the boundary of this colouring must use
all six colours.  Otherwise some colour from the six-colour palette is
absent on `S`, and assigning that colour to `q` extends the colouring of
`J` to a six-colouring of `G`.  Since `25` is already one block, all five
remaining boundary vertices `0,1,3,4,6` must consequently be singleton
blocks with distinct colours.

Apply the audited singleton-block Kempe lemma to the nonedge `46`.

* A successful swap merges exactly `4,6` and returns `Pi*`; its five
  boundary colours again leave a sixth colour for `q`, contradicting the
  counterexample.
* Otherwise there is a literal `4-6` bichromatic path whose internal
  vertices all lie in `R`.

Thus the claimed dichotomy is valid.  The singleton hypothesis for `4,6`
is not automatic from an arbitrary partition containing `25`; it follows
from the preceding all-six-boundary-colours argument and must remain in the
proof.

### E4(c): packet escape for the `4-6` path — GREEN with explicit model

Let `X` be the nonempty connected interior of the returned `4-6` path.  If
`X` is disjoint from `P1 union P2`, the following seven sets are literal
branch sets:

\[
 \{1\},\quad \{2\},\quad \{6\},\quad
 \{3,q\},\quad \{5\}\cup P_1,\quad P_2,
 \quad \{0,4\}\cup X.                                 \tag{E4.1}
\]

They are disjoint and connected.  The first three form the boundary
triangle `126`.  The full vertices/packets `q,P1,P2` supply every missing
contact from their anchored bags; `35,45,01,02,03,04` and the Moser edges
supply the remaining boundary contacts; and the last edge of the `4-6`
path joins `X` to the singleton bag `{6}`.  A direct pair check gives all
21 adjacencies.  Hence (E4.1) is a literal `K7` model.

No adjacency between `P1` and `P2` is assumed: their anchored interaction is
witnessed, for example, by the contact of `P2` with literal `5` in the
`P1 union {5}` bag.

Therefore a `K7`-minor-free survivor forces every such returned `4-6` path
to meet `P1 union P2`.

### E4(d): symmetric `46` trace — GREEN

Contracting `q union {4,6}` instead forces the exact block `46`.  The same
all-six-colours argument makes `2,5` singleton blocks, and their Kempe
exchange either returns `Pi*` or yields a literal `2-5` path with interior
in `R`.

If its interior `Y` avoids `P1 union P2`, the symmetric literal `K7` model
is

\[
 \{3\},\quad \{4\},\quad \{5\},\quad
 \{1,q\},\quad \{6\}\cup P_1,\quad P_2,
 \quad \{0,2\}\cup Y.                                 \tag{E4.2}
\]

The first three bags form triangle `345`, and the final bag meets `{5}`
through the last edge of the `2-5` path.  Fullness supplies the remaining
packet contacts.  Thus the symmetric escape claim is also proved.

### E4(e): exact surviving conclusion

The rigorous residue is:

* the exact `25` trace yields a `4-6` bichromatic path meeting
  `P1 union P2`; and
* the exact `46` trace yields a `2-5` bichromatic path meeting
  `P1 union P2`.

The two paths may come from different six-colourings.  Nothing proved here
makes them simultaneous, disjoint from each other, incident with both
packets, or confined to the same packet.  Any stronger “reserved connector”
or packet-splitting conclusion remains an additional theorem.
