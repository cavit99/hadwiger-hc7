# Audit: oppositely ordered missing-colour paths barrier

**Verdict:** GREEN as a computer-assisted counterexample to the narrow
intermediate inference stated in the source note.  It is not an `HC_7`
counterexample and does not satisfy the live seven-connectivity,
contraction-criticality, or literal split-edge hypotheses.

## Audited revision

This audit checks exactly:

- `hc7_balanced_order8_two_missing_colour_paths.md`, SHA-256
  `cfd4f58623213aab11c0398a40d24343f4dafac3dd71cae3176af62b9a1ed74c`;
- `hc7_balanced_order8_two_missing_colour_paths_verify.py`, SHA-256
  `792d6108748c255966424abd2c6649a0a30fe0fe3437898633e5d4ef90092ad8`.

Any change to either file requires a new audit or an explicit hash update
after rechecking the changed claim.

## Reproduction

From the repository root I ran

```text
python3 barriers/hc7_balanced_order8_two_missing_colour_paths_verify.py
```

The verifier completed successfully and reported the unique three-cut, the
five ordinary bichromatic endpoint connections, the two oppositely ordered
three-colour paths, strong connectivity of the root three-colour component,
the complementary-palette path/response configuration, absence of both
prescribed two-linkages, and absence of a `K_7` minor.

## Independent checks

### Graph and separator data

Expanding the construction gives 15 vertices in `Q` and 18 in `H`.  Direct
edge checks confirm both displayed five-cliques, the three missing root
edges `ac`, `bd`, `cd`, and the three present root edges `ab`, `ad`, `bc`.
Exhaustive enumeration of the three-subsets of `V(Q)` gives the unique cut
`{p,A1,A2}`.  Deleting `R union {p,A1,A2}` from `H` gives exactly the two
components stated in the note, and each component has a neighbour at every
one of the six boundary vertices.  NetworkX independently returns
`kappa(Q)=3` and `kappa(H)=5`.

The linkage routine is exhaustive: it enumerates every simple path for the
first prescribed pair, deletes all its vertices, and tests connectivity of
the second pair.  The four terminals are distinct in every call.  It
therefore correctly verifies the two present linkages, the absent
`(ac,bd)` linkage in `Q`, and the absent closed-large-side
`(b-t,a-c)` linkage.

### Colouring claims

For each displayed colouring I checked coverage of all vertices and every
edge after the stated deletion or deletions.  In (3.1), explicit paths put
`a` and `b` in the same `0-j` component for every `j=1,...,5`; hence no
single ordinary Kempe interchange separates their colours.  In (4.1), both
deleted edges are monochromatic, the reserved triangle has colours
`3,4,5`, and the two directed paths have cyclic colour words
`0,1,2,0` in opposite endpoint directions.  Reversing the second path gives
the opposite cyclic order `0,2,1,0`.  Direct strongly-connected-component
enumeration gives exactly the eight-vertex set displayed in (4.5), which is
also the entire underlying three-colour component containing `a,b`.

For the added colouring (4.6), direct edge checking confirms that it is a
proper colouring after deleting `g=A0A4` and `h=uv`, with both deleted
edges monochromatic.  The natural support of `g` is exactly `{0,1,2}`:
the reserved triangle uses `{3,4,5}`.  The natural support of `h` is exactly
`{3,4,5}`: the other three vertices `p,A2,w` of its five-clique use
`{0,1,2}`.  Thus the two supports are genuinely disjoint.

The two displayed `g`-paths have colour words `0,1,2,0` and `0,2,1,0`.
The displayed `h`-path has word `5,3,4,5`, and its vertex set is disjoint
from both `g`-paths.  In the reverse `(5,4,3)` orientation, the reachable
set from `u` is exactly `{u}`, so it does not contain `v`.  Rotating that
set sends the colour of `u` from 5 to 4; restoring `h` then leaves a proper
six-colouring in which `h` is proper and `g` remains monochromatic.  This
is exactly the claimed local path/response conclusion.  It does not make
the example satisfy the non-six-colourability hypothesis of the abstract
coupling theorem, and the source note correctly says that the full host
input is absent.

The final six-colouring in the verifier proves that `H` is six-colourable.
For the note's assertion that this host is not contraction-critical, there
is also a short independent certificate: the induced subgraph on

```text
{A0,A1,A2,A4,p,r0,r1,r2,u,v,w}
```

has 11 vertices and independence number two, so it needs at least six
colours.  It avoids `q`; consequently deleting `q` leaves chromatic number
six.  Thus `H` is not even vertex-critical, and in particular is not
contraction-critical.

### `K_7`-minor exclusion

The retained verifier's integer-flow formulation is sound.  Every vertex is
assigned to exactly one nonempty branch set.  For each branch, the
least-indexed member supplies `|B|-1` integral flow units and every other
member consumes one, with flow permitted only on edges internal to the
branch.  Feasibility is therefore equivalent to connectedness of every
branch set.  The final constraints require an edge between every pair of
branch sets.  Ordering their least members removes only label symmetry.

Restricting to spanning models loses nothing in a connected host: every
component outside a minor model has an edge to its union and may be absorbed
into an adjacent branch set.  The solver returned `UNSAT` for `H` and `SAT`
for the positive `K_7` control.

As an independent formulation, I replaced the flow constraints by
rooted integer levels: every nonroot member of a branch set must have an
internal neighbour at a strictly smaller level.  With the same partition
and pairwise-adjacency constraints, this second encoding also returned
`UNSAT`.  Thus the minor exclusion does not depend on the particular flow
encoding.

## Exact trust boundary

The checked conclusion is only that ordered missing-colour paths, even when
they lie in opposite cyclic orders and their three-colour component is
strongly connected, do not by themselves force the missing rooted linkage
or a `K_7` minor in this quotient configuration.  The strengthened example
also shows that the local conclusion of the disjoint-palette coupling
theorem--two paths for one edge, a disjoint path for the other, and the
opposite one-edge response--does not supply that rooted linkage by itself.

The example has only vertex-connectivity five, is six-colourable, is not
contraction-critical, and replaces two literal defect edges by single
contracted vertices.  It also has a lower-order separation that can be
enlarged to order seven.  Accordingly it does **not** refute a theorem that
also uses seven-connectivity, proper-minor colouring transitions, literal
endpoint placement, or the full alternative allowing an order-seven
separation.
