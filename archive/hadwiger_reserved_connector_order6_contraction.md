# Contraction reduction for an order-six reserved-connector shore

This note records the first extension beyond the certified order-five closure
in `hadwiger_reserved_connector_portal_transfer.md`.  It is not a closure of
the full order-six cell: it eliminates 67 of the 112 internal types and leaves
45 explicitly listed blocked types.

## 1. Safe contraction

Let (D) be a connected shore with boundary (L), where (|L|=7), and put

$$
\phi_D(X)=|N_D(X)-X|+|N_L(X)|
$$

for (arnothing\ne X\subsetneq D).  In the reserved-connector cell one has
(phi_D(X)\ge7), (N_L(D)=L), and the terminal inequality

$$
\epsilon+|N_D(a)|\ge3,                              \tag{1.1}
$$

where (epsilon) records the edge (aw).

Contract an edge (xyin E(D)).  Full (L)-coverage is preserved.  The
terminal inequality can fail only when (1.1) is tight and both (x,y) see
(a).  Every other failure has the following form: there is a set
(Y\subseteq D-\{x,y\}) with

$$
\phi_D(Y)=7,
\qquad x,y\in N_D(Y).                               \tag{1.2}
$$

Indeed, a set containing the contracted vertex is the image of a set
containing both (x,y), and its internal and boundary neighbourhoods are
unchanged.  A set avoiding the contracted vertex is a set (Y) disjoint from
({x,y}).  Its boundary neighbourhood is unchanged, while its internal
neighbourhood loses exactly one vertex precisely when both (x) and (y)
belong to (N_D(Y)).  This proves the assertion.

Call (xy) **safe** if neither obstruction occurs.  If (|D|=6) and some
edge is safe, contracting it produces an order-five shore satisfying every
hypothesis of Lemma 10.1 in the main note.  The certified order-five theorem
then gives an (N)-meeting (K_6)-model in the contraction, which lifts to
the original graph.  Therefore only attachment systems in which every edge
is blocked require new work.

## 2. Exact census of blocked internal types

The program `portal_order6_contraction_obstruction.py` regenerates all 112
connected unlabelled graphs on six vertices from the NetworkX graph atlas.  It
encodes all 62 nonempty proper shore-subset inequalities, full attachment,
the shore-vertex degree conditions, and (1.1).  For every internal edge it
forms the contracted five-row system explicitly and requires at least one
order-five hypothesis to fail.

The exact outcome is:

$$
\begin{array}{c|r}
\text{status}&\text{internal types}\\ \hline
\text{no all-edge-blocked attachment system}&47\\
\text{an all-edge-blocked attachment system exists}&65.
\end{array}                                         \tag{2.1}
$$

The archive `portal_order6_contraction_obstruction.json` records a complete
row witness for every one of the 65 surviving types, all tight sets, and the
precise failed condition after each edge contraction.  Every failure has
exactly one of the two forms proved in Section 1; thus the run also audits the
contraction calculation independently at the integer-row level.

## 3. Direct closures inside the blocked cell

The probe `portal_k6k1_probe.py --blocked-only` adds explicit monotone
(N)-meeting (K_6) supports only after imposing that every contraction is
blocked.  The completed partial archives

* `portal_k6k1_blocked_0_28.json`,
* `portal_k6k1_blocked_28_56.json`,
* `portal_k6k1_blocked_56_84.json`, and
* `portal_k6k1_blocked_84_112.json`

close 20 of the 65 genuinely blocked types, with 8,916 explicit supports.
Together with the 47 safe-contraction types, this eliminates 67 of the 112
order-six internal types.

The independent replay `portal_order6_contraction_verify.py` imports neither
discovery program.  It regenerates the 112 atlas types, rechecks every one of
the 47 unsatisfiable contraction formulas, pins and verifies all 65 blocked
witnesses, validates every one of the 8,916 branch-set models from its listed
support edges, expands those supports by the full internal automorphism group,
and proves coverage over all labelled blocked attachment systems.  Its final
output is

```text
verified order-six contraction census: 47 automatic, 65 blocked
verified partial order-six closure: 47 safe-contraction types +
20 direct types = 67 of 112
```

The remaining 45 blocked types are

```text
g049 g051 g054 g055;
g065 g068 g069 g070 g073 g074 g075 g076 g077 g078 g079;
g080 g081 g082 g083 g086 g087 g088 g089 g090 g091 g092 g093;
g094 g095 g096 g097 g098 g099 g100 g101 g102;
g103 g104 g105 g106 g107; g108 g109; g110; g111.
```

Here `gNNN` is the stable atlas index prefix printed by
`portal_k6k1_probe.py`; the archive contains the full graph6 code and edge
set.  No survivor has been found by the direct search, but these 45 types have
not yet received a complete independent certificate and are not claimed
closed here.
