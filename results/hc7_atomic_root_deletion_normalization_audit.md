# Independent audit: atomic root-deletion normalization

## Verdict

**GREEN** at frozen source SHA-256
`95d51c06de89493cd5cf490439a57d86e9ea4d32e7d027b6da2df917b77b9f3e`.

The cutvertex contradiction, exact two-carrier list colouring, six-cut
argument, connector avoidance, rooted-leaf path/`Y` normalization, and
component bridge inequality are all correct under the stated
`|A|>=2` hypothesis.  The geometric replacement connector need not be
bichromatic; the source explicitly preserves this trust boundary.

## 1. Setup and the exceptional frontier

The atom has a literal separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},
\]

with no `A-R` edge.  The unique `A-u` edge is `zu`, so `z in A` and no
vertex of `A-z` sees `u`.

The retained-clique convention in the exceptional frontier is legal.  The
audited atomic trace theorem permits a triangle vertex `k ne u` to be
retained.  Consequently `u in V(F)` and

\[
 F=K_{1,3}\mathbin{\dot\cup}K_2.
\]

Every proper two-colouring of the remaining triangle edge assigns its two
ends to different carriers, so each nonempty carrier block contains a
literal neighbour of `k`.  The retained duty is therefore automatic even
if one endpoint of that edge is `u`.  In the connected case `U` is empty,
so there is no retained duty.

The two opposite packets need not be adjacent.  The invoked nonspanning
two-carrier theorem only requires them to be disjoint, connected and
`S`-full: when both boundary blocks occur, packet fullness itself supplies
cross-adjacency through the opposite boundary block.

## 2. The root cannot be a cutvertex

Assume `A-z` has at least two components and choose one, `X`.  Every
neighbour of `X` outside it lies in `W union {z}`:

* another component of `A-z` is anticomplete to `X`;
* there is no `A-R` edge; and
* the unique `A-u` edge has its `A` end at the deleted vertex `z`.

The seven-set `W union {z}` separates `X` from the nonempty rich shore.
Seven-connectivity gives `|N_G(X)|>=7`, while the displayed containment
gives the reverse inequality.  Hence

\[
                         N_G(X)=W\cup\{z\}.
\]

In particular every component of `A-z` is `W`-full and adjacent to `z`.

For `C_2=X` and `C_1=A-X`, the assumption of at least two components is
essential and is used correctly: `C_1` contains `z` and at least one other
component.  It is connected because every remaining component meets `z`.
The two carriers are adjacent through an `X-z` edge.  The first is
`W`-full; the second is `S`-full because a remaining component supplies
all of `W` and `z` supplies `u`.

Thus every member of `F-{u}` has list `{1,2}`, while `u` has list `{1}`.
The graph `F` is bipartite, so orient the component containing `u` to give
it label `1` and orient the other components arbitrarily.  This is a
proper literal list colouring.  In the exceptional case the retained duty
was verified in Section 1.  The audited nonspanning two-carrier theorem
therefore gives the claimed six-colouring contradiction.  No implicit
palette-to-carrier identification occurs.

This proves `A-z` connected when `|A|>=2`.  The nonsingleton assumption is
necessary here: when `A={z}`, the deleted shore is empty and neither the
connectivity nor carrier conclusion is meaningful.

## 3. Exact six-cut argument

Now `A-z` is nonempty and connected.  It has no neighbour at `u`.  If it
also missed some `w in W`, then all its external neighbours would lie in

\[
                         \{z\}\cup(S-\{u,w\}),
\]

a set of order six.  This set is disjoint from `A-z`, and deleting it
separates the latter from the nonempty rich shore.  That contradicts
seven-connectivity.  Hence `A-z` sees every member of `W` and no member of
`{u}`, proving

\[
                         N_S(A-z)=W.
\]

There is no hidden assumption that `z` is the only `A`-neighbour of a
member of `W`; the argument needs only one surviving portal for each such
literal.

## 4. Connector avoidance and the path/`Y` core

For disjoint nonempty `B,C subseteq W`, choose one literal from each and
neighbours in the connected graph `A-z`.  A path between the two neighbours,
with the two boundary incidence edges added, gives the required `B-C`
path.  Coincident portal witnesses cause no exception: they give a
length-two boundary-to-boundary path through their common neighbour.

This replacement is purely geometric.  It need not lie in the two-colour
subgraph of the localization colouring and must not replace the original
lock in an argument that uses bichromaticity.  It is valid for subsequent
branch-set or carrier geometry, exactly as the source states.

The internal path `Q` avoids `z`.  A shortest `z-Q` path `Z`, stopped at
its first vertex `r` of `Q`, has no other vertex on `Q`.  Therefore
`Q union Z` is a tree.  Only `r` can have degree three, and `z` is an end
of the nontrivial path `Z`, hence a leaf.  This proves the claimed path or
subdivided-`Y` form, including the case that `Q` is a singleton.

The phrase that `Q` is inclusion-minimal is harmless but not needed for
the degree conclusion; retaining `Q` as the fixed path subgraph is the
essential convention.

## 5. Component bridge certificate

Let `D` be a component of `A-T`.  Every `A`-neighbour of `D` lies in `T`,
distinct components of `A-T` are anticomplete, and there is no `D-R` edge.
Consequently

\[
 N_G(D)=N_T(D)\mathbin{\dot\cup}N_S(D).
\]

Deleting this neighbourhood separates nonempty `D` from nonempty `R`, so
seven-connectivity gives

\[
                         |N_T(D)|+|N_S(D)|\ge7.
\]

If equality holds, this literal neighbourhood has order seven.  Taking
`D` as one open side and

\[
 V(G)-(D\cup N_G(D))
\]

as the other gives an actual separation; the other side is nonempty
because it contains `R`.  Thus the exact-boundary assertion is valid.
It carries no equality state merely from this geometry, as the source
correctly warns.

## 6. Trust boundary

The result proves exactly the following normalization for a nonsingleton
atom:

* `A-z` is one connected `W`-full packet;
* any two named non-`u` boundary sets have a connector avoiding `z`;
* adjoining a shortest root path produces a path/`Y` with `z` as a leaf;
* every complementary component obeys the displayed attachment/support
  budget, with an actual seven-boundary at equality.

It does **not** prove that the new connector is bichromatic, allocate the
frontier duties between two carriers, preserve an attained state at a new
seven-boundary, or handle the singleton atom `A={z}`.  None of those
stronger conclusions is used in the source.
