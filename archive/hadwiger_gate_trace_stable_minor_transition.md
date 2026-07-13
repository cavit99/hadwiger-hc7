# Far-gate minor transitions: the exact trace-stability boundary

## 1. Setting and notation

Use the audited antipodal gate adhesion

\[
                 D_0\mid L\mid D_{56},
 \qquad L=\{v\}\mathbin{\dot\cup}X
                 \mathbin{\dot\cup}\{p,q\},
 \qquad X=\{1,2,3,4\}.                           \tag{1.1}
\]

The graph \(G\) is a proper-minor-minimal non-six-colourable graph,
\(L\) is an exact seven-cut, and
`hadwiger_gate_exact_adhesion_multishore.md` proves that these are the
only two components of \(G-L\).  The original star-contraction colouring
of \(H=G-v\) has exact trace

\[
                         05\mid1\mid2\mid3\mid4\mid6              \tag{1.2}
\]

or, after switching \(K_0\), the exact trace with \(05\) replaced by
\(06\).  This fixed colouring supplies the palette-deletion rooted
\(K_4\) on \(X\).  It is not a colouring of \(G\), since all six
colours occur on \(N(v)\).

For \(i\in\{0,56\}\), let \(\mathcal E_i\) be the exact equality
partitions of \(L\) which extend to a six-colouring of
\(G[D_i\cup L]\).  If \(\mu\) is an \(L\)-label-preserving operation
internal to \(D_{56}\), write \(\mathcal E_{56}^{\mu}\) for the
extension family of the operated shore.  No state in this note is said to
extend \(D_{56}\) unless membership in \(\mathcal E_{56}\), rather than
merely \(\mathcal E_{56}^{\mu}\), has been proved.

## 2. What minor-criticality really supplies

### Theorem 2.1 (far-gate transition polarity)

Let \(\mu\) be any of the following operations in \(D_{56}\):

* delete an internal vertex;
* delete an internal edge; or
* contract an internal edge.

Then a six-colouring \(c_\mu\) of the proper minor \(G^\mu\) induces
an exact cut state \(\Pi_\mu\) satisfying

\[
          \Pi_\mu\in
          \mathcal E_0\cap\mathcal E_{56}^{\mu}
          \setminus\mathcal E_{56}.               \tag{2.1}
\]

Moreover:

1. \(c_\mu(v)\) is absent from \(N(v)\), and the block of \(v\) on
   \(L\) is contained in \(\{v,p,q\}\);
2. the colour classes on the seven Moser vertices \(N(v)\) form either
   two or three disjoint nonedge pairs, with every other class a
   singleton; equivalently, \(N(v)\) uses five or four colours; and
3. for an internal edge deletion \(xy\), one may choose the witness so
   that
   \[
      c_\mu(x)=c_\mu(y),                            \tag{2.2}
   \]
   each endpoint sees every other colour, and for every other colour
   \(\gamma\), \(x,y\) lie in one
   \(\{c_\mu(x),\gamma\}\)-component.  A contraction witness expands
   to the same equal-endpoint deletion witness.

#### Proof

Colour the proper minor \(G^\mu\) with six colours and restrict it to
the two closed shores.  This proves membership in
\(\mathcal E_0\cap\mathcal E_{56}^{\mu}\).  If the same state extended
the unmodified \(D_{56}\)-shore, align its block colours with the
restriction on \(D_0\) and glue across \(L\).  This would six-colour
\(G\), proving the exclusion in (2.1).

The vertex \(v\) remains adjacent to every vertex of \(N(v)\), so its
colour is absent there.  In particular it differs from every member of
\(X\), proving item 1.  Dirac's neighbourhood inequality gives
\(\alpha(G[N(v)])\le2\).  Thus every colour class on \(N(v)\) has
order at most two.  Seven vertices coloured from the five colours other
than \(c_\mu(v)\) use at least four colours.  If they used six, there
would be no colour for \(v\); hence they use four or five.  Their
nonsingleton classes are consequently a matching of order three or two,
proving item 2.

For an edge deletion, restoring \(xy\) would colour \(G\) unless its
ends agree.  If an endpoint missed another colour on its neighbourhood,
recolouring that endpoint would separate the ends and again restore the
edge.  If the ends lay in different bichromatic components for another
colour, switching the component containing one end would do the same.
This proves item 3.  A colouring of \(G/xy\) expands to a colouring of
\(G-xy\) with equal endpoint colours. \(\square\)

The direction in (2.1) is essential: the transition state is accepted by
the unchanged \(D_0\)-shore and the **operated** far shore, and is rejected
by the original far shore.

## 3. Why the exact star trace cannot be imposed on a transition

### Lemma 3.1 (star trace and a full transition state are incompatible)

No six-colouring of a graph containing \(v\) can simultaneously induce
one of the exact six-colour traces (1.2) on \(N(v)\).  In particular,
the state \(\Pi_\mu\) in Theorem 2.1 cannot itself retain the original
exact \(05\)- or \(06\)-trace.

#### Proof

The exact trace uses all six colours on \(N(v)\), while \(v\) is
adjacent to every vertex of \(N(v)\).  No colour remains for \(v\).
\(\square\)

There are two tempting but invalid ways to evade this observation.

### Lemma 3.2 (the star contraction is not an adhesion operation)

Contracting the star on \(\{v,0,5\}\), or on
\(\{v,0,6\}\), is not \(L\)-label-preserving.  It identifies the cut
vertex \(v\) with a vertex of \(D_0\) and a vertex of \(D_{56}\), and
therefore destroys the two-piece decomposition (1.1).  A colouring of
that contracted minor cannot be restricted to an unchanged opposite
shore in the proof of Theorem 2.1.

Furthermore, after expanding the star and deleting its contracted image,
one cannot give \(v\) the star colour: it is adjacent to both expanded
star leaves \(0,5\) (or \(0,6\)).

#### Proof

The placements

\[
        v\in L,\qquad 0\in D_0,qquad
        \{5,6\}\subseteq D_{56}
\]

are part of the exact gate construction.  Hence the contraction has one
branch set meeting all three parts of the separation.  This violates the
definition of a label-preserving piece operation.  The final assertion is
the pair of literal edges from \(v\) to the two contracted neighbourhood
vertices. \(\square\)

### Lemma 3.3 (saturation is lost after a simultaneous operation)

Even if one performs \(\mu\) and the \(05\)-star contraction
simultaneously, minor-criticality and the contracted boundary edges imply
only that \(0,5\) have one colour which is absent from the other five
Moser vertices.  The assertion that those other five vertices have five
different colours is not a formal consequence of these inputs.

#### Proof

The original exactness proof used that a colour absent from \(N(v)\) in
a colouring of the unoperated \(H=G-v\) could be assigned to \(v\),
contradicting non-six-colourability.  After \(\mu\), the full graph is a
proper minor and is already six-colourable.  That saturation contradiction
is unavailable.

Concretely, in the star-contracted boundary give the star image colour
\(a\), give \(1,3\) colour \(b\), give \(2,4\) colour \(c\), and
give \(6\) colour \(d\).  This is proper: \(13,24\) are Moser
nonedges, \(12,34\) join different colours, and \(6\) differs from its
neighbours \(1,2\) and from the star image through \(56\).  Expanding
the star gives the non-exact trace

\[
                         05\mid13\mid24\mid\{6\}.                  \tag{3.1}
\]

Thus the claimed exactness cannot follow from the contracted boundary
edges. \(\square\)

### Lemma 3.4 (palette deletion is witness-specific)

The rooted four-colour core supplied by
`hadwiger_palette_deletion_rooted_core.md` cannot automatically be
relabelled as the four-colour core of \(c_\mu\).  More precisely, at
least one of the following additional facts would have to be proved:

1. \(X\) has four distinct colours in \(c_\mu\) and the corresponding
   four transition colour classes are \(X\)-saturating; or
2. the original rooted \(K_4\)-model survives \(\mu\) and its four bag
   labels can be aligned with four distinct blocks of \(\Pi_\mu\).

Neither follows from Theorem 2.1.

#### Proof

Palette deletion was applied to the fixed six-colouring of the
**unoperated** graph \(H=G-v\), whose neighbourhood \(N(v)\) is
six-saturating.  The transition colouring is a colouring of a proper
minor containing \(v\); its colour is absent from \(N(v)\), so the same
neighbourhood is visibly not six-saturating in that colouring.  Item 2 of
Theorem 2.1 also permits a transition matching to identify two vertices
of \(X\), and the operation \(\mu\) may meet a branch bag of the fixed
rooted model.  Thus neither listed alignment is supplied by the existing
theorems. \(\square\)

Lemmas 3.1--3.3 are the trace-stability obstruction.  The original star
colouring and a minor-transition colouring are two different witnesses;
their colour labels or Kempe components cannot be identified without an
additional theorem.

## 4. The transition states which can be normalized safely

There is nevertheless a substantial trace-free normalization.  A Kempe
switch performed in the **whole proper minor** \(G^\mu\) preserves both
memberships in (2.1).  If its new state extended the original far shore,
the same gluing contradiction would apply.

Call \(c_\mu\) **core-rainbow** when the four vertices of \(X\) have
four distinct colours.  Call a colour a *gate colour* when it is not one
of those four core colours.

### Theorem 4.1 (rainbow transition normalization)

Assume that \(c_\mu\) is core-rainbow and at least one of \(p,q\) has
a gate colour.  By a sequence of global Kempe switches in \(G^\mu\),
one obtains at least one of the following.

1. A transition state in
   \(
     \mathcal E_0\cap\mathcal E_{56}^{\mu}
       \setminus\mathcal E_{56}
   \)
   which is one of the pair modes in
   `hadwiger_gate_pairmode_all_gate_placements.md`.
2. Two vertex-disjoint bichromatic carriers for one of the core
   matchings \(13\mid24\) or \(14\mid23\).
3. One of these explicit carrier frames:
   * a bichromatic path joining \(v\) to the unique gate-coloured member
     of \(\{p,q\}\);
   * a connected bichromatic carrier containing all of \(v,p,q\); or
   * a rooted triangle on three members of \(X\), made from two
     bichromatic arms at a common root and the literal leaf edge
     \(12\) or \(34\).

Every path or carrier in outcomes 2--3 is an actual connected subgraph of
the operated graph; for a contraction operation it lifts through the
contracted internal edge.

#### Proof

Let \(\Gamma\) be the two colours outside the four colours on \(X\).
The colour of \(v\) belongs to \(\Gamma\).

First suppose both \(p,q\) use colours in \(\Gamma\).  If the restriction
to \(\{v,p,q\}\) has two colour blocks, one block has order two and is
the gate pair \(B_0\), while the other vertex is the singleton.  If all
three have one colour, inspect their components in the subgraph induced
by \(\Gamma\).  Unless all three lie in one component, switch a component
meeting exactly one of them; this produces a two-plus-one split.  If all
three lie in one component, a minimal tree in that component connecting
them is the second carrier frame in outcome 3.

Now suppose exactly one, say \(p\), has a gate colour, while \(q\) has
the colour of the unique root \(x_i\).  If \(v,p\) have different gate
colours, either they lie in different two-colour components, in which case
switching the component containing \(v\) makes them a pair, or they have
a bichromatic \(v\)-\(p\) path, the first carrier frame in outcome 3.
Thus outside outcome 3 the two fixed independent blocks are

\[
                         \{v,p\},\qquad\{q,x_i\}.                 \tag{4.1}
\]

Among the other three roots, the two missing edges share a centre and
their leaves form the other literal edge of \(G[X]\).  If either missing
pair has its ends in different bichromatic components, switch one end
component and obtain the pair mode of Theorem 4.1 in the cited note.  If
both pairs are connected, their two paths form the rooted triangle in
outcome 3.

It remains to normalize the four roots in the both-gate case.  Let

\[
 F=\{ij\in\{13,14,23,24\}:i,j\text{ lie in one global
 bichromatic component of }G^\mu\}.
\]

If the complement of \(F\) contains one of the two perfect matchings of
the missing \(C_4\), switch one endpoint component for each of its two
edges.  The colour pairs are disjoint, so the switches commute and create
the corresponding pair mode.  If \(F\) contains a perfect matching,
choose its two paths; their disjoint colour pairs make their vertex sets
disjoint, giving outcome 2.  If neither \(F\) nor its complement contains
a perfect matching, \(F\) is an adjacent two-edge star.  Its two paths,
joined at their common root, and the literal edge between their leaves
give the rooted triangle in outcome 3.

All switches were made in the whole proper minor, so the resulting state
still extends \(D_0\) and the operated far shore.  If it extended the
original far shore, gluing would colour \(G\), proving the stated
polarity.  An internal contraction replaces at most one vertex of a path;
expanding it to its adjacent two-vertex preimage preserves connectedness
and disjointness. \(\square\)

The theorem is deliberately global.  Switching only on \(D_0\) would
preserve acceptance there but need not preserve acceptance by the operated
far shore; that invalid direction is not used.

The pure-core placement also has a direct carrier alternative.

### Theorem 4.2 (rainbow pure-core reduction)

Assume \(X\) is rainbow and both \(p,q\) use core colours.  Then global
Kempe switches in \(G^\mu\) give either an outcome of Theorem 4.1 or one
of the following actual carrier frames:

1. if \(p,q\) have the colour of the same root \(x_i\), a connected
   two-colour subgraph containing \(p,q,x_i\); or
2. if \(p,q\) have the colours of distinct roots \(x_i,x_j\), two
   paths, one joining \(p\) to \(x_i\) and the other joining \(q\) to
   \(x_j\).  The paths use a common gate colour as their second colour;
   they are either disjoint or meet only in vertices of that gate colour.

As in Theorem 4.1, every normalized state remains in the transition
difference (2.1), and every carrier lifts through an internal contraction.

#### Proof

Let \(\delta\) be the gate colour different from \(c_\mu(v)\).  No
vertex of \(X\) has colour \(\delta\).

Suppose first that \(p,q,x_i\) have one core colour \(\gamma\).  Inspect
the \(\{\gamma,\delta\}\)-components containing these three vertices.
If they do not all lie in one component, some component avoids \(x_i\)
and contains one or both of \(p,q\).  Switch that component.  The roots
in \(X\) remain rainbow and at least one of \(p,q\) now has a gate
colour, so Theorem 4.1 applies.  If all three lie in one component, a
minimal tree in it connecting them is the carrier in outcome 1.

Now suppose \(p\) has the colour of \(x_i\), while \(q\) has the
different colour of \(x_j\).  In the
\(\{c_\mu(p),\delta\}\)-subgraph, either \(p,x_i\) are in different
components or there is a path joining them.  In the first case switch the
component containing \(p\); it contains no member of \(X\), since the
only boundary root of that colour is \(x_i\) in the other component.
Thus \(p\) becomes gate-coloured and Theorem 4.1 applies.  Make the
symmetric test for \(q,x_j\).  If neither switch is available, choose the
two displayed paths.  Their non-gate colours are different, so an
intersection can only have colour \(\delta\), proving outcome 2.

All operations are global Kempe switches of the proper minor, so the
polarity and contraction-lifting arguments from Theorem 4.1 apply
unchanged. \(\square\)

Finally, a nonrainbow transition can be made rainbow unless it already
contains a core carrier.

### Theorem 4.3 (nonrainbow transition rainbowization)

Suppose two vertices \(x_i,x_j\in X\) have one colour in
\(c_\mu\).  Then \(x_ix_j\notin E(G)\), and a global Kempe operation
does one of the following:

1. increases by one the number of colours used on \(X\), without
   changing \(c_\mu(v)\); or
2. supplies a connected bichromatic carrier joining \(x_i\) to
   \(x_j\).

Consequently, after at most two applications, every transition state
either becomes core-rainbow and enters Theorem 4.1 or 4.2, or already has
an actual core carrier.  All resulting states retain the polarity (2.1).

#### Proof

Because \(G[X]\) consists of the two edges \(12,34\), every independent
colour class in \(X\) has order at most two.  Thus \(x_i,x_j\) are the
only members of \(X\) in their common colour \(\gamma\), and their edge
is absent.

At least two colours are absent from \(X\) when \(X\) is nonrainbow.
Choose one, \(\delta\), different from \(c_\mu(v)\).  If
\(x_i,x_j\) lie in distinct \(\{\gamma,\delta\}\)-components, switch
the component containing \(x_i\).  It contains no other member of
\(X\): no other root has colour \(\gamma\), and no root has colour
\(\delta\).  Hence \(x_i\) receives the new colour \(\delta\), all
other root colours remain fixed, and the number of colours on \(X\)
increases by one.  Since neither switched colour is \(c_\mu(v)\), the
colour of \(v\) and its absence from \(N(v)\) are preserved.

If the two roots lie in one component, a shortest path between them in
that component is the carrier in outcome 2.  Initially \(X\) uses two or
three colours, so at most two successful switches make it rainbow.  Each
switch is global in \(G^\mu\), and hence preserves the extension and
nonextension argument of Theorem 4.1. \(\square\)

### Proposition 4.4 (the alternatives are the helper/carrier inputs)

The non-state outcomes of Theorems 4.1--4.3 have the following exact
interpretation.

1. A \(v\)-to-\(p\) or \(v\)-to-\(q\) path is a carrier for the gate
   pair block used in the corresponding mode.
2. Two disjoint core paths are two-block capacity for that mode.
3. A connected carrier containing \(v,p,q\) can be split into a carrier
   for some independent pair among these three and an adjacent helper
   piece containing the remaining singleton.
4. The rooted triangle and the pure-core \(p\)-to-root paths are the
   partial rooted bags required by the carrier-web branch.
5. A path joining an equal-coloured root pair in Theorem 4.3 is a carrier
   for that existing boundary block.

#### Proof

Only item 3 needs explanation.  Shrink the connected triple carrier to a
minimal tree containing \(v,p,q\).  Choose a terminal which is a leaf of
this tree as the singleton \(r\).  If the minimal tree is a path with one
terminal internal, choose an endpoint terminal.  Delete the first edge on
the path from \(r\) toward the subtree containing the other two terminals.
The \(r\)-side and the other side are nonempty, connected, adjacent, and
respectively contain the singleton and an independent gate pair.  The
other items are immediate from the definitions of a carrier, two-block
capacity, and a rooted partial model. \(\square\)

## 5. Exact residual and an explicit obstruction

Theorems 4.1--4.3 leave no unclassified equality state.  Every transition
normalizes to an existing pair mode or supplies an actual carrier frame.
There is nevertheless an important obstruction to obtaining this
conclusion from the equality partition and star trace *without* the global
Kempe argument.

The obstruction already appears on the contracted boundary.  Use the
proper colouring from (3.1), take \(p\) to have the colour of \(1,3\),
take \(q\) to have the colour of \(2,4\), and give the restored cut
vertex \(v\) a fifth colour.  Choose the unrestricted boundary contacts
so that \(p\) misses \(1,3\) and \(q\) misses \(2,4\).  The induced
state on \(L\) is

\[
              \{v\}\mid\{1,3,p\}\mid\{2,4,q\}.                  \tag{5.1}
\]

It is proper and satisfies every forced local edge and colour-count
condition: \(v\) differs from \(X\), \(12,34\) have differently
coloured ends, and the trace on \(N(v)\) is the legal three-pair matching
\(05\mid13\mid24\mid\{6\}\).  But (5.1) is not a
\(2+2+2+1\) mode, and Kempe switching cannot be inferred from its equality
partition alone.  This is an explicit obstruction to any proof which
claims that the star contraction plus minor-criticality *formally* forces
one of the existing pair modes.

The example is not asserted to realize all global counterexample
hypotheses.  Its role is exact: it disproves the proposed inference from
the star contraction, the fixed boundary edges, and the transition colour
count.  Theorem 4.3 resolves (5.1) for an actual global transition
colouring: a spare-colour switch either separates each repeated root pair
or exposes its bichromatic carrier.  That global component information is
precisely what the static boundary example omits.

## 6. Net result

Minor-criticality on \(D_{56}\) gives a strong, correctly directed state
transition (2.1).  Theorems 4.1--4.3 normalize every transition, in the
whole operated graph, to an existing pair mode or an explicit carrier
frame.  What they do not give is trace stability with the original
\(05/06\) colouring.

Thus every internal far-shore operation gives the dichotomy

\[
 \boxed{\text{catalogued pair-mode transition}
        \quad\text{or}\quad
        \text{explicit bichromatic carrier frame}.}
\]

The remaining work is geometric rather than state-theoretic: turn the
carrier frames into the singleton-helper transfer or a tight adhesion.
The edge-witness Kempe fan in Theorem 2.1(3) is additional structure for
that conversion.  No unmodified-shore extension has been assumed anywhere
above.

The conclusion is operation-by-operation.  Different operations may
normalize to different pair modes, and a carrier produced by a global
Kempe component may meet both shores.  Nothing here asserts recurrence of
one fixed mode, shore-locality of every carrier, or extension of any
transition state over the unmodified \(D_{56}\).  Those are the exact
remaining alignment requirements.
