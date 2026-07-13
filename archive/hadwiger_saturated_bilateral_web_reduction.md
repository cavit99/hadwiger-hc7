# Saturated bilateral webs: actual cell peeling and the covered-packet exit

## 1. Scope

Let `C` be one open shore of the forced bilateral exact-eight gate `X`,
and let `R` be the opposite connected shore full to `X`.  Assume an
actual saturated Two-Paths web has been found inside `C`: every rib edge
used below is an edge of the host, and each filled facial cell is the
literal clique attached to its facial triangle.  This is stronger than
being a spanning subgraph of an edge-maximal web completion.

The distinction is essential.  Nothing below replaces a virtual rib edge
by an unspecified path.

## 2. Filled cells peel to an actual adhesion

### Lemma 2.1 (literal facial-cell gate)

Let `Delta` be a facial triangle of the rib and let `K` be its nonempty
inserted clique.  Then

\[
                         N_G(K)=\Delta\mathbin{\dot\cup}N_X(K). \tag{2.1}
\]

In particular `Delta union N_X(K)` is an actual separator.  If
`|N_X(K)|` is four or five, it is an actual order-seven or order-eight
adhesion.

### Proof

By the definition of a filled web cell, vertices of `K` have no neighbour
in the rib outside `Delta` and no neighbour in another cell.  The open
shore has no neighbours outside `C union X`, proving (2.1).  The outer
rib contains a nominated terminal outside the facial triangle, and the
opposite shore `R` lies outside `C union X`; hence vertices survive on
both sides and the displayed neighbourhood is a genuine separator.

Seven-connectivity gives `|Delta|+|N_X(K)|>=7`, so the two displayed
contact orders give separators of order seven and eight.  QED.

Thus every nonempty facial cell either supplies the required descent or
has at least six literal gate contacts.  Clique insertion is not harmless:
the six-, seven-, and eight-contact cells remain a named high-contact
residue and may not simply be contracted into one rib vertex.

### Theorem 2.2 (a high-contact cell has order at most two)

In a seven-connected, `K_7`-minor-free bilateral gate, every nonempty
filled facial clique has order at most two.  If a two-vertex cell has a
vertex with three or four gate neighbours, that vertex exposes an actual
order-seven or order-eight cut, respectively.

### Proof

Let the facial triangle be `Delta={d_1,d_2,d_3}` and let its clique be
`K`.

If `|K|>=4`, any four vertices of `K` together with the three vertices
of `Delta` induce a `K_7`: the cell is a clique, the triangle is a clique,
and the cell is complete to its facial triangle.  Hence `|K|<=3`.

Suppose `|K|=3`.  Then `Q=K\mathbin{\dot\cup}\Delta` is a literal
`K_6`.  Since `G` is seven-connected, `G-Q` is connected.  It is
nonempty, and every vertex of `Q` has a neighbour in it: each has at
most five neighbours in `Q`, whereas seven-connectivity gives minimum
degree at least seven.  The six singleton bags of `Q` together with the
connected bag `G-Q` are therefore a `K_7` model, a contradiction.

Finally let `K={u,v}` and suppose `|N_X(u)|` is three or four.  The filled-cell
definition gives

\[
 N_G(u)=\{v\}\mathbin{\dot\cup}\Delta
        \mathbin{\dot\cup}N_X(u),                  \tag{2.2}
\]

an actual cut of order `4+|N_X(u)|`, hence seven or eight: deleting it
isolates `u`, while the opposite full shore survives.  QED.

The proof is label-free and uses only actual edges.  Thus clique-filled
cells of order at least three are completely removed.  Away from an
order-seven/eight descent, a two-vertex cell has at least five gate
neighbours at each endpoint.  Since `|X|=8`, the two endpoint portal
rows then intersect in at least two boundary vertices.

## 3. The bilateral covered-packet exit

### Lemma 3.1 (covered `K_4` exit)

Suppose the actual web contains four disjoint connected pairwise adjacent
bags `F_1,...,F_4`.  Suppose two adjacent gate vertices `a,b` contact
every `F_i`, and two further gate vertices `p,q` collectively contact
every `F_i`.  Then `G` contains a `K_7` minor.

### Proof

The seven bags are

\[
               F_1,F_2,F_3,F_4,\quad
               \{a\},\quad\{b\},\quad R\cup\{p,q\}. \tag{3.1}
\]

Fullness of `R` makes the last bag connected and adjacent to `a,b`.
The hypotheses give its contacts with the first four bags and give every
remaining adjacency.  No intershore edge is used.  QED.

The four-rim atomic wheel is exactly this outcome with

\[
 (F_1,F_2,F_3,F_4)=(v_0,v_3,h,v_1v_2),
 \qquad(a,b,p,q)=(c_0,z,p,q).
\]

Hence it is eliminated by Lemma 3.1.

## 4. Exact residual for a uniform web-to-wheel theorem

After Lemmas 2.1 and 3.1, a surviving saturated web must satisfy both:

1. every filled facial cell has order one or two and at least six literal
   contacts with `X`; otherwise an actual order-seven/eight adhesion or
   the explicit model (2.4) has already appeared;
2. every rooted `K_4` packet supplied by curvature or a rooted-minor
   theorem fails the neutral normalization in Lemma 3.1: there are no two
   adjacent gate tags common to all four bags together with a two-tag
   cover of the four bags.

The second condition pinpoints the neutral-deficit problem.  Atomicity
forces a positive-curvature vertex to meet at least three of the four
neutral tags in the bare hard web, but it does not by itself force the
same adjacent pair—such as `c_0,z`—at four selected roots.  The first
condition pinpoints the cell problem: a six-contact clique cell is not an
order-eight descent, and absorbing it into a rib branch bag can erase a
literal portal label.

Therefore the remaining uniform statement is precisely:

> a saturated hard web with a six-contact filled cell or with four
> positive roots having nonconstant neutral deficits either has the
> prescribed two-linkage, contains the covered packet of Lemma 3.1, or
> exposes another actual order-seven/eight adhesion.

No virtual completion edge is available in this residue.  Proving this
last statement would close the saturated web family; the present note
proves its two extremal exits and records the exact two configurations
that still need exchange.
