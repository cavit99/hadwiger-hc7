# The exact five-colour lock at a leaf-rooted drop edge

**Status:** proved.  This is the complete palette statement in the branch
`chi(C-{u,v})=5`; it is not a labelled minor theorem.

## Theorem

Let `C` be a six-chromatic graph, let `uv` be an edge, and suppose

\[
                         R=C-\{u,v\}
\]

is five-colourable.  For a proper five-colouring `phi` of `R`, write

\[
 M_u(\phi)=[5]-\phi(N_C(u)\cap V(R)),\qquad
 M_v(\phi)=[5]-\phi(N_C(v)\cap V(R)).              \tag{1.1}
\]

Then every five-colouring of `R` satisfies at least one of

\[
 M_u(\phi)=\varnothing,\qquad
 M_v(\phi)=\varnothing,\qquad
 M_u(\phi)=M_v(\phi)=\{c\}\text{ for some }c.       \tag{1.2}
\]

Equivalently, if neither endpoint sees all five colours, the two endpoints
have exactly one available colour and it is the same colour.

### Proof

If there were colours `a in M_u(phi)` and `b in M_v(phi)` with `a!=b`,
then assigning `a` to `u` and `b` to `v` would extend `phi` to a proper
five-colouring of `C`; the only edge between the two newly coloured
vertices is `uv`, and its endpoints receive different colours.  This is
impossible because `chi(C)=6`.

Thus every pair in the Cartesian product `M_u(phi) times M_v(phi)` has
equal coordinates.  If either set is empty, the first or second outcome
of (1.2) holds.  If both are nonempty, choose elements from them.  Equality
of every cross-pair forces both sets to be the same singleton.  \(\square\)

## Sharpness and interpretation

The Hajós barrier in
`../barriers/hc7_leaf_drop_hajos_barrier.md` realizes the third outcome
for every five-colouring.  There `R` is two `K_5` subgraphs sharing `a`;
the four neighbours of `u` in the left clique and the four neighbours of
`v` in the right clique omit exactly the common colour of `a`.

Therefore the five-chromatic branch has one precise state obstruction:
a **common missing-colour lock**.  An unrooted `K_5` model in `R` carries
no information capable of breaking that lock.  A valid continuation must
either

1. use ambient attachments to make one endpoint see the missing colour;
2. transfer to another five-colouring in which the lock changes in a
   label-faithful way; or
3. expose the separator supporting the common lock and return a labelled
   near-`K_7`/exact-adhesion handoff.

This is the palette analogue of the Hajós separator.  It does not identify
palette colours with branch sets of the regenerated `K_5` model.
