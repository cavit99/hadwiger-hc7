# Same-vertex saturation of the atomic defect-rotation graph

**Status:** written proof; computer-assisted finite result; separate internal
audit GREEN.

This note proves a fixed-vertex saturation result for the thirteen-vertex
graph in the
[`shared-hub defect-rotation barrier`](../barriers/hc7_atomic_shared_hub_defect_rotation_barrier.md).
It does not concern supergraphs obtained by adding vertices.

The adjacent
[`deterministic checker`](hc7_atomic_shared_hub_same_vertex_saturation_verify.py)
validates every branch-set model and every finite incidence claim below.

## 1. The graph

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}
\]

on core vertices `a,b,c,d,e,f,g` and the additional vertex `x`.  Subdivide
`ac,bd,ad,bc` once, with respective new vertices
`p_ac,p_bd,p_ad,p_bc`, and add

\[
 fp_{ac},\quad fp_{bd},\quad gp_{ad},\quad gp_{bc}.
\]

Finally replace `fg` by `f-h-g` and add `eh,hx`.  Denote the resulting
thirteen-vertex, thirty-four-edge graph by `G_*`.

## 2. Fixed-vertex saturation theorem

### Theorem 2.1

Let `Q` be a simple graph on exactly `V(G_*)` with `G_*` as a spanning
subgraph.  If \(\delta(Q)\ge 7\), then `Q` contains a `K_7` minor.  Consequently
there is no seven-connected, `K_7`-minor-free supergraph of `G_*` on the
same thirteen vertices.

### Proof

Put `q=p_ad`.  Its neighbours in `G_*` are exactly `a,d,g`, so its nine
nonneighbours are

\[
 b,c,e,f,h,x,p_{ac},p_{bd},p_{bc}.                       \tag{2.1}
\]

Adding any one of

\[
 qb,qc,qp_{ac},qp_{bd},qp_{bc}                           \tag{2.2}
\]

already gives a `K_7` minor.  The following table gives seven spanning
branch sets for each addition.  Within each row the sets are connected,
pairwise disjoint, and pairwise adjacent.

| added edge | seven branch sets |
|---|---|
| `b-p_ad` | `{a,p_ac,p_ad}`; `{b}`; `{c,p_bc}`; `{e}`; `{f,p_bd}`; `{g,h}`; `{d,x}` |
| `c-p_ad` | `{a,p_ac}`; `{b,p_bd,p_bc,x}`; `{c}`; `{d,p_ad}`; `{e}`; `{g}`; `{f,h}` |
| `p_ac-p_ad` | `{b}`; `{d,p_ac,p_ad,p_bd}`; `{e}`; `{f}`; `{a,g}`; `{x,h}`; `{c,p_bc}` |
| `p_bd-p_ad` | `{b,p_bd,p_bc}`; `{c}`; `{e}`; `{d,f}`; `{g}`; `{a,p_ac,p_ad}`; `{x,h}` |
| `p_bc-p_ad` | `{d,p_ad}`; `{e}`; `{b,f,p_bd}`; `{g}`; `{a,p_ac}`; `{c,p_bc}`; `{x,h}` |

Since the existence of a minor is monotone under edge addition, a
`K_7`-minor-free `Q` contains none of the five edges in (2.2).  To raise
the degree of `q` from three to at least seven, `Q` must therefore contain
all four remaining possible incident edges

\[
                       qe,qf,qh,qx.                      \tag{2.3}
\]

In particular, `hp_ad` belongs to `E(Q)`.

The permutation

\[
 \sigma=(a\ b)(c\ d)(p_{ac}\ p_{bd})(p_{ad}\ p_{bc})   \tag{2.4}
\]

fixing `e,f,g,h,x` is an automorphism of `G_*`.  Indeed, it preserves the
two absent core edges `ab,cd`; interchanges the subdivided routes
`a-p_ac-c` and `b-p_bd-d`; interchanges `a-p_ad-d` and `b-p_bc-c`;
interchanges the two `f`-anchor edges and the two `g`-anchor edges; and
fixes the subdivided `fg` route and `eh,hx`.

Applying `sigma` to the five explicit models above gives the corresponding
five forbidden one-edge additions at `p_bc`.  This does not assume that
`Q` is invariant under `sigma`; it transfers certificates from `G_*` to
itself.  Since \(N_{G_*}(p_{bc})=\{b,c,g\}\), the same degree argument forces
`hp_bc` into `E(Q)`.

It remains to audit what the two forced edges do.  In

\[
                     G_*+hp_{ad}+hp_{bc},                \tag{2.5}
\]

take the seven branch sets

\[
\begin{array}{lll}
 E=\{e\},&F=\{f\},&A=\{a,g,p_{ac}\},\\
 H=\{h,p_{ad}\},&B=\{b,p_{bc}\},&D=\{d,p_{bd}\},\\
 C=\{c,x\}.&&
\end{array}                                               \tag{2.6}
\]

They partition `V(G_*)`.  Their nontrivial connectedness is witnessed by
`ag,a-p_ac`, `h-p_ad`, `b-p_bc`, `d-p_bd`, and `cx`.  One contact edge for
each of the twenty-one branch-set pairs is:

| first bag | contacts with later bags |
|---|---|
| `E` | `EF:ef`, `EA:ea`, `EH:eh`, `EB:eb`, `ED:ed`, `EC:ec` |
| `F` | `FA:fa`, `FH:fh`, `FB:fb`, `FD:fd`, `FC:fc` |
| `A` | `AH:a-p_ad`, `AB:gb`, `AD:gd`, `AC:ax` |
| `H` | `HB:h-p_bc`, `HD:p_ad-d`, `HC:hx` |
| `B` | `BD:b-p_bd`, `BC:bx` |
| `D` | `DC:dx` |

Thus (2.6) is an explicit `K_7`-minor model in `Q`, proving the theorem.
\(\square\)

## 3. Verification

Run from the repository root:

```text
.venv/bin/python -B results/hc7_atomic_shared_hub_same_vertex_saturation_verify.py
```

The exact output is

```text
GREEN atomic shared-hub same-vertex saturation
host: vertices=13 edges=34 degree(p_ad)=3 degree(p_bc)=3
automorphism: p_ad<->p_bc verified
one_edge_K7_models: p_ad-b,p_ad-c,p_ad-p_ac,p_ad-p_bd,p_ad-p_bc
remaining_incident_edges: p_ad-e,p_ad-f,p_ad-h,p_ad-x
forced_edges: h-p_ad,h-p_bc
two_edge_K7_model: branch_sets=7 contact_edges=21 verified
conclusion: same_vertex_minimum_degree_7_K7_free_supergraph=no
```

The checker reconstructs `G_*` independently.  It verifies the displayed
permutation on the whole edge set, the exact degree and nonneighbour lists,
all five one-edge models, and every connectedness and adjacency claim in
the final two-edge model.

## 4. Trust boundary

The theorem is only about edge additions on the same thirteen vertices.
New vertices can raise the degrees of `p_ad,p_bc` without adding either of
the forced incident edges used above.  Therefore this result does not imply
that an arbitrary seven-connected host containing `G_*` has a `K_7` minor.

Moreover, `G_*` itself is three-connected and three-colourable.  The result
does not use proper-minor colouring responses and does not close the dirty
replacement-path case in an unbounded host.  It records exactly why the
sparse obstruction cannot be repaired by adding edges while retaining its
vertex set.
