# Internal audit: planar-deficit closure of the sharp relative-seven quotients

**Status:** separate internal audit.

**Verdict:** **GREEN for the theorem and finite classification exactly as
stated.** The result closes the specified 48 quotient instances after the
literal expansion described in Theorem 4.1. It does not show that the live
order-eight problem always reaches this quotient family.

## Audited revision

This audit checked the following exact contents:

- theorem note
  `hc7_relative7_planar_deficit_closure.md`:
  `ceb1054dbea46b3a2df88ef8c8a65919056e6bdcbc09cd2c1e7bf9d6a702ead8`;
- exhaustive verifier
  `hc7_relative7_planar_deficit_verify.py`:
  `74b655bb0db80c51f9ffb916bbe3bd0fd4a974e2cdd6c320fc139132616f4a55`;
- independent catalogue checker
  `hc7_relative7_planar_deficit_certificate_check.py`:
  `339aa66677de3c1eaed08e929f6e59c4d4eadf46c27140defb95629fad5e589f`;
- checked-in catalogue
  `hc7_relative7_planar_deficit_catalogue.json`:
  `62a2e9e4478e8e16bf51b784fa0decd191c5f65bf35b2faf713bb2d1e2657c7d`.

All hashes are SHA-256.

## Written-proof audit

The cited external result is correctly identified. Theorem 6 of
Fabila-Monroy and Wood, *Rooted \(K_4\)-Minors*, EJC 20(2) (2013), P64,
states that for four distinct nominated vertices in a four-connected graph,
either there is a \(K_4\)-minor rooted at those vertices, or the graph is
planar and the four vertices lie on one face. Lemma 1.1 uses only the
planarity part of the second outcome.

Deleting the triangle from a seven-connected graph leaves a
four-connected graph. In the rooted-minor outcome, each singleton triangle
vertex is adjacent to each rooted branch set through its nominated vertex,
so the four rooted branch sets and three singleton branch sets form a
\(K_7\)-minor model.

In the planar outcome, seven-connectivity gives

\[
 6-d_H(x)\leq |N_G(x)\cap\Delta|-1.
\]

The contribution from every vertex in \(D\) is nonpositive. The stated
bound on the remaining contributions therefore gives a total at most
eleven. Since \(H\) is a simple planar four-connected graph, Euler's
inequality gives

\[
 6|V(H)|-2|E(H)|\geq12,
\]

which is the required contradiction. No face-order conclusion from the
rooted-minor theorem is used.

For each hard triple, the selected agreement endpoints together with vertex
6 form the claimed triangle. The vertices \(p,v\) and both endpoints of the
disagreement pair are complete to it. Contracting the connected replacement
of \(z\) back to \(z\) and using \(U\cap\Delta=\{6\}\) implies that every
replacement vertex has at most one neighbour in the triangle. The other two
fixed vertices each have two triangle neighbours. Thus the fixed-vertex
deficit is exactly

\[
 4(3-1)+2(2-1)=10,
\]

and Lemma 1.1 applies. For a direct quotient \(K_7\)-minor, replacing the
occurrence of \(z\) in its branch set by its connected preimage is valid
minor transitivity.

## Finite-classification audit

The 27 allowed root sets are exactly the subsets containing vertex 6 and a
nonempty subset of each of the three missing-edge pairs. Hence the ordered
universe has size \(27^3\).

The verifier exhausts:

- all connected, pairwise adjacent four-bag minor models in \(R\);
- all ordered triples of the 27 root sets;
- every cut of size at most six avoiding \(z\);
- exact five- and six-colourability;
- every seven-bag clique-minor model on the ten quotient vertices; and
- every protected-triangle certificate for a hard instance.

The minor enumeration permits unused vertices and arbitrary nonempty
connected branch sets, so it is not restricted to subgraphs or to a
preselected contraction pattern. The relative-connectivity predicate is
exactly connectivity after every deletion of at most six quotient vertices
other than \(z\), which is the necessary property inherited by contracting
a connected subgraph in a seven-connected host.

Both checked-in programs completed successfully and reported:

```text
root_sets=27 rooted_K4_models=644 triple_model_free=912
relative_survivors=48 direct_K7=24 hard=24
explicit_K7_minor_models=24 checked_adjacencies=504
unique_planar_deficit_certificates=24 deficit=10
survivor_complete=48 direct_K7_models=24 planar_deficit=24
checked_branch_sets=168 checked_adjacencies=504 deficit=10
fixed_graph6=I]~vy}jhw
catalogue_sha256=2cd2a8faf6f70327a9d2c7b4ec7084bd5981349d529a59708d69e84f05acdaa2
```

The last hash is the SHA-256 of the canonical compact serialization of the
two certificate lists, not the hash of the JSON file. The independent
checker does not import the exhaustive verifier. It regenerates the 24
stated hard patterns and, independently, all 48 triples satisfying the
rooted-\(K_4\)-free and relative-connectivity predicates. It checks that the
two disjoint catalogue sections exhaust those 48 triples. For every direct
case it checks seven nonempty, pairwise disjoint, connected branch sets and
all 21 required adjacencies. For every hard case it checks the local host
certificate, and it recomputes the catalogue digest.

An additional cold connected-set enumeration during this audit independently
reproduced the counts 644, 912, 48, 24 and 24. The graph6 regression was also
decoded independently with `showg`; its adjacency list agrees with the
stated \(A,B,U\). Both programs refuse to run when Python optimization has
disabled assertions.

## Unresolved dependencies and scope

1. The independent checker verifies existence of the 24 direct
   \(K_7\)-minor models. The assertion that none of the 24 hard quotients has
   a \(K_7\)-minor still rests on the exhaustive verifier's complete
   seven-bag search.
2. Theorem 4.1 assumes an exact literal expansion of the marker: the host is
   obtained from the stated quotient by replacing \(z\) with one nonempty
   connected subgraph, with no additional host vertices.
3. Nothing audited here proves that every operated-shore residue has this
   quotient form, that a marker-containing cut preserves the required
   colouring response, or that the remaining order-eight response-coupling
   theorem follows.
