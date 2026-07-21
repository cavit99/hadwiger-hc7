# An inclusion-minimal forest landing on the exact atomic quotient

**Status:** written proof; separate internal audit GREEN.

Let

\[
 J=K_8-\{xe,ab,cd\},
 \qquad O=J[\{x,e,a,b,c,d\}]=K_{2,2,2}.
\]

The two vertices outside the octahedron `O` are the adjacent universal
vertices `f,g`.  This note closes the case in which a forest contraction
lands on `J` for the first time in the strong inclusion-minimal sense.  It
does not close a contraction chain whose connectivity first fails at an
earlier partial expansion of `J`.

## 1. Exact contraction setup

Let `G` be a finite simple graph and let `F` be a nonempty forest in `G`.
We identify `F` with its edge set.  Thus \(F'\subseteq F\) below always
means an edge subset, and `G/F'` contracts the components of that
subforest.
Contract every component of `F` to one vertex, suppressing loops and
parallel edges, and assume that the resulting labelled simple graph is
exactly `J`:

\[
                              G/F=J.                 \tag{1.1}
\]

For `z in V(J)`, let `R_z` be the fibre of `z`.  Thus `R_z` is either a
singleton or the vertex set of one nontrivial tree component of `F`.
Exactness in (1.1) means that two distinct fibres have a host edge between
them exactly when their labels are adjacent in `J`.

Assume the following all-subsets minimality, not merely minimality along
one chosen ordering of the forest edges:

\[
 G/F'\text{ is seven-connected for every }F'\subsetneq F.       \tag{1.2}
\]

In particular `G` is seven-connected.

### Theorem 1.1 (exact minimal-forest landing)

Under (1.1)--(1.2), `G` contains an explicit `K_7`-minor model or has an
actual vertex separator of order seven.  In the separator outcome, every
one of the eight labelled fibres is contained in one of the two closed
shores.

## 2. Only the two universal fibres can be nontrivial

For each absent pair `P` in

\[
                         \{\{a,b\},\{c,d\},\{x,e\}\},             \tag{2.1}
\]

the set

\[
                         T_P=V(J)-P                               \tag{2.2}
\]

is a six-vertex separator of `J`.

### Lemma 2.1 (fibre localization)

Every nontrivial component of `F` contracts to `f` or to `g`.

#### Proof

Let `h` be an edge of a nontrivial component of `F`, and let `z` be the
image of that component in `J`.  Put

\[
                         H_h=G/(F-\{h\}).                         \tag{2.3}
\]

By (1.2), `H_h` is seven-connected.  In `H_h`, the vertex `z` is split
into two adjacent vertices representing the two components of the tree
`F[R_z]-h`.

Fix one of the sets `T_P` in (2.2).  If `z notin T_P`, splitting `z` only
replaces one vertex of one component of `J-T_P` by a connected edge.  It
does not join the two components of `J-T_P`.  Hence the same six-set
`T_P` would separate `H_h`, contradicting seven-connectivity.  Therefore
`z` belongs to all three sets in (2.2).  Their intersection is

\[
             T_{ab}\cap T_{cd}\cap T_{xe}=\{f,g\},               \tag{2.4}
\]

which proves the lemma.  \(\square\)

Consequently all six vertices of `O` are literal singleton fibres in
`G`.  Only `R_f` and `R_g` may be nontrivial, and at least one is
nontrivial because `F` is nonempty.

## 3. Every side of every fibre-tree edge meets all six octahedral vertices

### Lemma 3.1 (six-contact split sides)

Let `z in {f,g}`, let `h` be an edge of the tree `F[R_z]`, and let `U,V`
be the vertex sets of the two components of `F[R_z]-h`.  Then each of
`U,V`, as a connected branch set in `G`, is adjacent to every literal
vertex of `O`.

#### Proof

In the seven-connected graph `H_h` from (2.3), write `u_h,v_h` for the
two quotient vertices represented by `U,V`.  Fix an absent pair `P` from
(2.1).  Since `z in T_P`, the set

\[
 S_{P,h}=(T_P-\{z\})\cup\{u_h,v_h\}                              \tag{3.1}
\]

has order seven.  The graph `H_h-S_{P,h}` consists exactly of the two
literal singleton vertices in `P`.  They are nonadjacent because (1.1)
is the exact quotient `J`.

For either `p in P`, its neighbourhood in `H_h` is contained in the
seven-set `S_{P,h}` and separates `p` from the other member of `P`.
Seven-connectivity therefore gives

\[
                         N_{H_h}(p)=S_{P,h}.                       \tag{3.2}
\]

In particular both `u_h` and `v_h` are adjacent to both members of `P`.
Applying this to `P={a,b}`, `{c,d}`, and `{x,e}` shows that both split
sides meet all six vertices of `O`.  Expanding the quotient vertices
back to their connected preimages gives the stated host adjacencies.
\(\square\)

The use of all three antipodal pairs is essential.  A degree count at one
split vertex `u_h` or `v_h` alone is insufficient: among the other eight
vertices it may miss one octahedral vertex.  Applying
\(\delta(H_h)\ge7\) separately to each literal vertex in an antipodal pair is
equivalent to the exact-cut proof above.  That literal vertex has only the
seven vertices of `S_{P,h}` available as neighbours, so it sees both split
vertices; repeating this for all three pairs forces all six contacts.

## 4. The cross-fibre edge dichotomy

There is at least one edge between `R_f` and `R_g`, because `fg` is an
edge of the exact quotient `J`.

### Proof of Theorem 1.1

First suppose there is exactly one edge between the two fibres, say
`uv` with `u in R_f` and `v in R_g`.  Choose its endpoint `w` in a
nontrivial fibre `R_z`; such an endpoint exists because at least one fibre
is nontrivial.  Put

\[
                         S=V(O)\cup\{w\}.                          \tag{4.1}
\]

The set has order seven.  The set `R_z-{w}` is nonempty, the other fibre
is nonempty, and the unique cross-fibre edge has been deleted.  Extra
edges internal to either fibre do not join the two fibres.  Since

\[
                         V(G)=V(O)\mathbin{\dot\cup}R_f
                                      \mathbin{\dot\cup}R_g,
\]

the graph `G-S` is disconnected.  Thus (4.1) is an actual order-seven
separator.  Put all components contained in `R_z-{w}` on one open side
and the other fibre on the other.  Then `R_z` lies in the first closed
shore, the other fibre lies in the second, and all six singleton fibres
of `O` lie in the boundary.  This proves the asserted label preservation.

Now suppose there are at least two edges between `R_f` and `R_g`.  Since
`G` is simple, one of the two fibres, say `R_z`, contains two distinct
endpoints `p,q` of cross-fibre edges.  Choose an edge `h` on the unique
`p`--`q` path in the tree `F[R_z]`.  Let `U,V` be the two sides of
`F[R_z]-h`, labelled so that `p in U` and `q in V`.  Let `z'` be the
other member of `\{f,g\}` and put

\[
                              W=R_{z'}.
\]

The three sets `U,V,W` are nonempty, pairwise disjoint and connected.
The edge `h` joins `U` to `V`, while the two selected cross-fibre edges
join `W` to `U` and to `V`.  Hence they are pairwise adjacent.  Lemma 3.1
makes `U` and `V` adjacent to every vertex of `O`, and exactness of the
quotient makes the whole fibre `W` adjacent to every vertex of `O`.

Inside the octahedron `O`, the four sets

\[
                 \{x,a\},\qquad \{e,c\},\qquad \{b\},\qquad \{d\}       \tag{4.2}
\]

are connected and pairwise adjacent.  Indeed, the only missing edges of
`O` are `xe,ab,cd`.  Thus (4.2) is an explicit `K_4`-minor model in `O`.
Every one of its four bags is adjacent to each of `U,V,W`.  Consequently

\[
 U,\quad V,\quad W,\quad \{x,a\},\quad \{e,c\},\quad \{b\},\quad \{d\}
                                                                    \tag{4.3}
\]

are seven pairwise disjoint, connected and pairwise adjacent branch sets.
They form an explicit `K_7`-minor model in `G`.  This completes the proof.
\(\square\)

## 5. Exact-boundary response in a minor-critical host

In the separator outcome, seven-connectivity makes every component of
`G-S` adjacent to every vertex of `S`: its neighbourhood is a subset of
the seven-set `S` and is itself a genuine separator.

If, in addition, `G` is seven-chromatic and every proper minor is
six-colourable, then every nonempty independent set `I` of `G[S]` has the
standard exact-block response on either closed shore.  Choose a connected
`S`-full component on the opposite open side, contract it together with
`I`, six-colour the proper minor, expand `I`, and restrict to the desired
closed shore.  Independence makes the expansion proper, while fullness
makes `I` exactly one boundary colour class.  Reversing the two sides gives
the opposite response.

## 6. Trust boundary

The theorem proves the terminal disjunction only when the **entire**
forest landing on `J` satisfies (1.2) for every proper edge subset.  A
first bad prefix of one chosen contraction ordering supplies minimality
only for earlier prefixes.  Taking an inclusion-minimal bad subset repairs
that quantifier, but its quotient can be a larger partial expansion rather
than `J`; the three antipodal six-cuts used above are then unavailable.

The proof preserves the eight quotient fibres in the separator outcome.
It does not automatically preserve an additional named support which
uses vertices from several different fibres.  It uses no colouring in the
main theorem and does not prove the atomic collision theorem or `HC_7`.
