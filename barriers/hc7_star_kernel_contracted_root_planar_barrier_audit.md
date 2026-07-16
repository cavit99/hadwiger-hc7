# Independent audit of the contracted-root planar barrier

**Verdict:** GREEN for the exact revisions audited.

## Audited revisions

- statement: `hc7_star_kernel_contracted_root_planar_barrier.md`
- statement SHA-256: `995d80c5e1fa442ab6159e14870139d3d4946987b4c317508050723112c29bd1`
- checker: `hc7_star_kernel_contracted_root_planar_barrier_verify.py`
- checker SHA-256: `3e81526fb4c5fa897a3bc70a68522eebe87569d5c3bcbf71ebd2b5660a0aed57`

The checker was rerun from the repository root and returned

```text
GREEN: contracted-root planar star-kernel barrier verified
connectivity T,Q,J,H,G0 5 5 5 4 8
facial roots (12, 0, 13, 1)
repair target sets [5, 14, 19] [14, 15, 16]
```

## Construction and connectivity

The 32-vertex graph `T` has the stated incidence/dual construction, 90
edges, and a planar embedding.  The checker verifies `kappa(T)=5`.  Removing
`12-13` gives `Q` with connectivity five and merges the two incident
triangles into the facial four-cycle `12,0,13,1`.  The claimed edge on its
opposite side has third vertex `18`.

The expansion adds one adjacent true twin of `a=13` and one of `b=1`.
Every old neighbour is copied and the cross-twin edge is added, so
contracting the two twin edges recovers exactly the vertex and edge sets of
`Q`.  The computed connectivities `kappa(J)=5` and
`kappa(J-{u,v})=4` are exact.  The adjacency assertions for the two twin
edges follow directly from the two missing diagonals of the facial
four-cycle.  Since `a,b,p` form a triangle and true-twin expansion copies
all its adjacencies, `{a,a',b,b',p}` is a literal `K_5`.

## Topological nonlinkage

Lemma 2.1 is a valid Jordan-curve obstruction.  A path from `a` to a
nonfacial-sector neighbour of `u`, together with `ux,av,vu`, forms a simple
cycle.  The facial rotation at `v` places `b` and every eligible other end
of the second path on opposite sides.  A second path avoiding `u,v` and the
first path would cross that cycle.

If disjoint connected repairs existed after twin expansion, the repair
containing `aa'` could use neither `b` nor `b'`, and the other could use
neither `a` nor `a'`.  Contracting each twin edge therefore preserves
disjointness.  Shortest paths inside the two images end in exactly
`N_Q(u)-{v,b}` and `N_Q(v)-{u,a}`, producing the forbidden pair.  The
two-commodity checker encodes simple directed paths: unit in/out degrees
give one path per commodity, increasing order variables exclude cycles,
and the shared-vertex constraints enforce vertex-disjointness.  All terminal
choices are unsatisfiable.

Lemma 2.2 is also correct.  In a three-connected plane graph a facial
boundary is a cycle.  The four vertices must occur in their induced-cycle
order, and any nontrivial facial arc between consecutive cycle vertices
would be separated from the other two roots by its ends.  Hence the induced
cofacial four-cycle is itself facial.

## Full five-edge extension

The extension `G_0` leaves the exterior `H` unchanged and makes
`L_0={u,v,r,s,t}` a clique.  Each of the five displayed defect edges is
anticomplete to its indexed leaf and collectively adjacent to every other
leaf; the checker verifies these incidences directly.  The five edges are
distinct, the second literal `K_5` remains disjoint from `L_0`, and
`kappa(G_0)=8`.  Since `G_0-L_0=H`, the selected pair `e_u,e_v` retains the
proved nonlinkage.

The two displayed connected sets for `e_s,e_t` are disjoint, adjacent, and
each adjacent to all five leaves.  They and the singleton leaf clique are an
explicit `K_7`-minor model.  Thus the extension is intentionally not
`K_7`-minor-free, exactly as the scope section states.

## Scope

The basic example refutes the local implication using a second literal
five-clique and a highly connected contracted quotient.  The extension also
shows that eight-connectivity and all five normalized incidences do not
force repair for a *specified* disjoint pair.  It does not refute the active
five-support theorem: it is not `K_7`-minor-free or contraction-critical,
and its explicit `K_7` model allows a successful different pair.  The note
states these limitations accurately.
