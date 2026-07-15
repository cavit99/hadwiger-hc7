# Audit: same-row minimal portal core

**Verdict:** GREEN as stated.  The two-owner transfer preserves the stated
comparison class and the two corollaries follow.  The theorem deliberately
optimizes over clique models which need not be spanning; its empty-owner
move is not valid in a spanning-only comparison class.

## 1. The singleton-owner transfer

Let `X` be root-free detachable and suppose
`Omega_F(X)={i}`.  The replacement

\[
 F'=F-X,\qquad F_i'=F_i\cup X
\]

has all required properties.

* `F'` is connected by detachability and still contains the fixed distinct
  pole neighbours `x,y`.
* There is an old `X-F_i` model edge: the nonempty set of `F`-ends of all
  `F-F_i` edges is contained in `X`.  Hence `F_i'` is connected.
* For every `j ne i`, the assertion `j notin Omega_F(X)` gives an old
  `F-F_j` edge whose `F`-end lies in `F-X`.  Thus `F'` retains every such
  foreign-row adjacency.
* Since `X` and `F-X` are nonempty and `G[F]` is connected, an edge crosses
  that split.  After the move it is an `F'-F_i'` edge.
* Every old adjacency between `F_i` and another foreign row survives because
  the whole old bag `F_i` is retained.

No pole contact is lost: the first row still contains `x,y`, while all
other old rows remain subsets of their new rows.  The only possible change
is an added pole contact to row `i`.  Therefore every contact potential
having the stated monotonicity is nondecreasing.  Strict increase
contradicts the primary maximum; equality contradicts the secondary
minimum of `|F|`.  The comparison-class step is valid.

If fixed first-hit vertices on two prescribed paths are also retained as
auxiliary data, the transfer does not disturb them: the model union is
unchanged and `x,y` remain in the first row.  This observation does not
license arbitrary additional comparison constraints; only constraints
preserved by the displayed move may be added.

## 2. Empty owner and the spanning qualification

When `Omega_F(X)` is empty, deleting `X` from the model leaves `F-X`
connected, containing `x,y`, and retaining an edge to every foreign row.
Clique-minor branch sets need not span the host, so omission of `X` is
legal and strictly reduces `|F|`.

This is the exact trust boundary.  If the comparison class were restricted
to **spanning** models, omission would leave vertices unassigned and this
argument would fail.  The theorem itself imposes no spanning condition.
It may be applied after regenerating a spanning model only by reoptimizing
over the larger, nonspanning class stated in the theorem, or by separately
proving a spanning-preserving move.

## 3. Corollaries

For disjoint detachable sets `X,Y`, the owner sets are disjoint.  Indeed,
if one label belonged to both, the nonempty set of all first-row ends of
edges to that foreign row would be contained in both disjoint sets.  Each
owner set has size at least two, so five labels support at most two such
sets.

The interior of a leaf block not containing `x` or `y` is connected,
nonempty and detachable, and distinct leaf-block interiors are disjoint.
At most two are root-free by the preceding paragraph, while at most two
others can contain the two fixed roots.  The four-leaf conclusion follows.

## 4. Audit of the adjacent two-apex barrier

The checker
`../barriers/hc7_same_row_split_two_apex_icosahedron_check.py` completes
successfully.  Its model enumeration covers the required optimization.

Any `K_6` model in

\[
                  (K_2\vee I)-\{z,u\}
\]

must use both universal vertices in distinct branch sets.  If one were
unused, or if both occurred in one bag, at least five remaining bags would
form a `K_5` minor wholly in the planar icosahedron.  Removing the two
universal-containing bags therefore leaves four disjoint, nonempty,
connected, pairwise adjacent subsets of `I-{z,u}`.

The checker enumerates all 696 connected nonempty subsets of that
ten-vertex graph and all 4,645 unordered four-bag `K_4` models.  The maximum
base contact profile is `(3,5)`.  Each universal-containing row is
contacted by both poles, so restoring those two rows contributes exactly
two to the union and four to the contact sum.  Thus `(5,9)` is an upper
bound for every `K_6` model, and the displayed model attains it.  The
enumeration may include base models which do not extend to two disjoint
apex bags; that only enlarges the search family and is harmless for this
upper bound.

The six displayed bags partition twelve vertices into six pairs, so their
spanning size vector is absolutely balanced.  More importantly for the
local theorem, the fixed first row already has the minimum possible order
two because it must contain the two distinct vertices `U3,U4`.

The checker verifies connectivity through order six, the displayed model,
the portal sets, split failure and the contact optimum.  It does not run a
general `K_7`-minor solver.  `K_7`-minor-freeness instead follows from the
complete planar argument: deleting the at most two branch sets containing
the universal vertices from a hypothetical seven-bag model leaves at least
five bags forming a `K_5` minor in `I`.  Accordingly the checker's printed
phrase `K7-free` relies on this mathematical proof rather than a separate
enumeration.

The barrier is therefore genuine.  It also has the intended fixed-pair
terminal `{a,b}`, since deleting the two universal vertices leaves the
planar icosahedron.  It refutes geometry-only same-row splitting but not a
split-or-terminal theorem.
