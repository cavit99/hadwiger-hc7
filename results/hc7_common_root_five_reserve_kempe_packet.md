# The tight common-root trace carries one five-reserve Kempe packet

**Status:** written proof; separately audited GREEN.  This theorem
does not prove `HC_7`.

## 1. Fixed-colouring setup

Assume either tight atomic outcome of the audited
[short-trace classification](hc7_common_root_short_trace_classification.md):
the atomic three-trace case in degree eight or the exact four-trace case in
degree nine.  Let `I` contain one representative of every boundary
two-colour trace, put

\[
                         X=N_G(u),\qquad R=X-I,          \tag{1.1}
\]

and use the colouring `c` of `G-u` supplied by Theorem 5 there.  Thus `I`
has one colour `gamma`, while the five vertices of `R` have the five other
colours, one each.  The two components of `G-N[u]` are denoted `E,F` and
are both adjacent to every vertex of `X`.

## 2. All reserve pairs are coupled in one colouring

### Theorem 2.1 (five-reserve Kempe packet)

In the one fixed colouring `c`:

1. every two distinct vertices `r,s in R` lie in one
   `c(r)`--`c(s)` component of `G-u`;
2. for every `r in R`, the `c(r)`--`gamma` component containing `r` meets
   `I`; and
3. a shortest path witnessing either assertion has no internal vertex in
   `X`, and its open interior lies wholly in `E` or wholly in `F`.

In particular, all ten pairs in `binom(R,2)` have simultaneous
bichromatic support in one colouring: a boundary edge supports an adjacent
pair directly, while every nonedge has a literal path with a shore label.
In the four-trace degree-nine case, the same colouring coexists with the
`I`-rooted `K_4` model from Theorem 5(5) of the short-trace classification.

#### Proof

Fix distinct `r,s in R`, and let `K` be the full
`c(r)`--`c(s)` component containing `r`.  If `s` were not in `K`, interchange
the two colours on `K`.  The vertex `r` is the unique boundary vertex of
colour `c(r)`, while `s` is the unique boundary vertex of colour `c(s)`.
After the interchange, colour `c(r)` would therefore be absent from `X`.
Assigning it to `u` would give a proper six-colouring of `G`, a
contradiction.  This proves item 1.

Now let `K` be the `c(r)`--`gamma` component containing `r`.  If it missed
`I`, interchange its two colours.  Again `r` was the unique boundary vertex
of colour `c(r)`, so that colour would disappear from `X` and could be
assigned to `u`.  This proves item 2.

For item 1, the only boundary vertices using the two selected colours are
`r,s`; a shortest joining path therefore has no other boundary vertex.  For
item 2, stop a shortest path on its first visit to `I`; its only boundary
vertices are its ends because `r` is the sole `c(r)` vertex of `X` and `I`
is the whole `gamma`-class there.  The graph outside `X union {u}` is the
disjoint union of the anticomplete components `E,F`.  Every nonempty open
path interior consequently lies in exactly one of them; an empty interior
needs no shore label.  \(\square\)

The paths supplied by Theorem 2.1 are not asserted to be pairwise
disjoint.  Their force is that all ten pairs occur in one colouring and
every nonedge retains literal shore provenance.

### Theorem 2.2 (the five-colour core is robust)

Let `Gamma` be the whole `gamma`-colour class of `c` in `G-u`, and put

\[
                         Q=(G-u)-\Gamma .               \tag{2.1}
\]

Then `chi(Q)=5`.  Moreover, in every proper five-colouring of `Q`, the five
vertices of `R` receive five distinct colours.  Consequently, for every
such colouring and every two distinct `r,s in R`, the vertices `r,s` lie
in one component induced by their two colours.

#### Proof

The restriction of `c` gives a five-colouring of `Q`.  If `Q` were
four-colourable, colour the independent set `Gamma` with a fifth colour
and give `u` a sixth colour.  This would six-colour `G`, so `chi(Q)=5`.

Now take any proper five-colouring of `Q`.  If it used at most four colours
on `R`, colour `Gamma` with a sixth colour and give `u` one of the five
colours absent from `R`.  Since `N_G(u)=I union R` and `I subseteq Gamma`,
this again gives a proper six-colouring of `G`, a contradiction.  Thus `R`
is rainbow.

Finally, if two roots `r,s` lay in different components induced by their
two colours, interchange those colours on the component containing `r`.
This would produce another five-colouring of `Q` in which `r,s` have the
same colour, contradicting the rainbow conclusion.  \(\square\)

## 3. Exact rooted-minor consequences

Write `H_R=G[R]` and let

\[
                         q=\binom52-|E(H_R)|            \tag{3.1}
\]

be its number of nonedges.  For a nonedge `rs`, call a shore available
when Theorem 2.1 has an `r`--`s` path whose open interior lies there.

### Theorem 3.1 (six-demand conversion and the reserved-shore exit)

The following hold.

1. If `q<=6`, then `G-u` contains an `R`-rooted `K_5`-minor model.
2. More generally, suppose every nonedge of `H_R` can be assigned to an
   available shore so that at most six are assigned to either shore.  Then
   `G-u` contains an `R`-rooted `K_5` model obtained by uniting two
   same-root shore models.
3. If `q<=6` and all nonedges are available in one shore, then `G`
   contains an explicit `K_7`-minor model.

#### Proof

Use the five-coloured graph `Q` from Theorem 2.2.  For every nonedge of
`H_R`, Theorem 2.1 puts its two roots in one component induced by their two
colour classes.

Kriesell--Mohr, Theorem 7, proves that every graph on five vertices with at
most six edges has their property `(*)`: the required two-colour
connections can be converted into pairwise disjoint connected root bags
realizing every edge of that graph.  Apply it to the graph of nonedges of
`H_R`.  When `q<=6`, it gives five rooted bags adjacent across every
boundary nonedge.  A literal edge of `H_R` joins the two bags containing its
ends.  Hence all ten adjacencies are present, proving item 1.

For item 2, apply the same theorem to the subgraph of `Q` induced by
`E union R` for the demand graph assigned to `E`, and symmetrically for
`F`.  A demand assigned to a shore has its bichromatic path in that
subgraph, so the required Kempe-component hypothesis holds.  For each
`r in R`, unite its two rooted bags at their common vertex `r`.  Bags with
different roots remain disjoint, and every required adjacency survives
from its assigned shore or as a literal edge of `H_R`.  This is the
asserted rooted `K_5` model.

For item 3, let `P` be the shore in which every nonedge is available.
Apply Kriesell--Mohr inside the subgraph of `Q` induced by `P union R` to
the `q<=6` nonedge-demand graph.  Literal edges of `H_R` then complete an
`R`-rooted `K_5` model wholly contained in that subgraph.  Let `P'` be the
other shore.  The seven sets

\[
   \text{the five rooted bags},\qquad \{u\},\qquad P'\cup I             \tag{3.2}
\]

are disjoint and connected.  The set `P' union I` is connected because
`P'` is connected and adjacent to every vertex of `I`.  It meets every
rooted bag through that bag's vertex in `R`, and it meets `{u}` through
`I`.  The singleton `{u}` meets every rooted bag through its root in `R`.
Thus (3.2) is an explicit `K_7`-minor model.  \(\square\)

### Corollary 3.2 (the only shore-allocation obstruction is concentrated)

Call a reserve nonedge `E`-exclusive if it is available in `E` but not in
`F`, and define `F`-exclusive symmetrically.  Then either `G-u` contains an
`R`-rooted `K_5` model, or at least seven reserve nonedges are exclusive to
one shore.

#### Proof

Let `a,b,c` be the numbers of `E`-exclusive, `F`-exclusive, and
two-shore-available reserve nonedges.  If `a<=6` and `b<=6`, assign some of
the `c` flexible demands to each shore so that neither shore receives more
than six.  Such an assignment exists because

\[
                         a+b+c\leq\binom52=10<12.
\]

Explicitly, the number assigned to `E` may be chosen between
`max(0,b+c-6)` and `min(c,6-a)`; the displayed bound and `a,b<=6` make this
interval nonempty.  Theorem 3.1(2) then gives the rooted model.  Therefore
failure forces `a>=7` or `b>=7`.  \(\square\)

### Corollary 3.3 (maximum-independent reserve rotation)

Retain the host `G,u,X,E,F` from Section 1, but let `J` be any independent
subset of `X` with

\[
                         |J|=d_G(u)-5,
        \qquad R_J=X-J.                               \tag{3.3}
\]

Then `|R_J|=5`, and there is one proper six-colouring `c_J` of `G-u` whose
boundary partition is

\[
                         J\mid\{r\}\quad(r\in R_J).   \tag{3.4}
\]

For this colouring, every pair of `R_J` is bichromatically coupled, every
nonedge of `G[R_J]` has a literal path in at least one named shore, and the
five-colour core obtained by deleting the colour class of `J` satisfies
Theorem 2.2.  The rooted-minor conclusions of Theorem 3.1 and the
concentration conclusion of Corollary 3.2 therefore hold with `J,R_J,c_J`
in place of `I,R,c`.

#### Proof

Contract the connected star on `{u} union J` and six-colour the resulting
proper minor.  Expand its contraction vertex over `{u} union J`, omitting
only the edges from `u` to `J`.  If the five vertices of `R_J` used at most
four of the other colours, one colour would be absent from `X`; assigning
that colour to `u` and restoring the omitted edges would six-colour `G`.
Thus the five vertices of `R_J` use the five other colours, one each.
Deleting `u` removes every omitted edge and gives `c_J` with (3.4).

The Kempe-coupling and shore-localization assertions invoked above from
Theorem 2.1, and the proof of Theorem 2.2, use only this fixed
singleton-reserve partition, the two full exterior components, and the fact
that `G` is not six-colourable.  The proofs of Theorem 3.1 and Corollary 3.2
then apply verbatim.  \(\square\)

## Exact trust boundary

This theorem replaces ten unrelated responses by one fixed-colouring
Kempe packet with literal shore tags.  Six or fewer nonedge demands already
give an `R`-rooted `K_5`; if one shore carries them all, the opposite full
shore is reserved and the construction is terminal.

The general case remains open.  A rooted `K_5` assembled from both shores
may consume both full components, leaving only `{u}` as a sixth bag.  If
even that rooted model cannot be assembled, Corollary 3.2 concentrates at
least seven exclusive demands in one shore, beyond Kriesell--Mohr's
six-edge theorem; their property `(*)` for `K_5` is itself open.
Corollary 3.3 permits a maximum independent set found inside that
concentration to generate a new packet, but it does not by itself make the
successive rooted models or shore labels compatible.
Seven-connectivity does not by itself reserve a connected subgraph adjacent
to all five rooted bags or upper-bound the neighbourhood of a failed
linkage.  The next valid lemma must either reserve one shore, retain an
`I`-containing connected seventh bag, or return an actual bounded
response-preserving component descent.

## Inputs

- [low-degree common-root short-trace classification](hc7_common_root_short_trace_classification.md)
- Matthias Kriesell and Samuel Mohr,
  [*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
  Theorem 7.
