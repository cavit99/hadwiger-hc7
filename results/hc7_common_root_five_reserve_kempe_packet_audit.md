# Audit: five-reserve common-root Kempe packet

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_common_root_five_reserve_kempe_packet.md`](hc7_common_root_five_reserve_kempe_packet.md)

Audited source SHA-256:

```text
f38da54340e869415be4ae9f43946b18b8fdbf4e07d9886b92a7c8b1f6da1638
```

## Checked scope

- In the fixed colouring of `G-u`, every vertex of `R` is the unique
  boundary vertex of its colour and `I` is the complete boundary
  `gamma`-class.  If the bichromatic component through `r` missed `s`, or
  if its `c(r)`--`gamma` component missed `I`, the stated Kempe interchange
  would remove `c(r)` from all of `X`.  Giving that colour to `u` would
  six-colour `G`.  Both packet conclusions are therefore valid in the one
  fixed colouring.
- A shortest reserve-pair path has no internal boundary vertex.  For a
  path from `r` to `I`, stopping at its first visit to `I` gives the same
  conclusion.  Since `G-(X union {u})` has exactly the two anticomplete
  components `E,F`, every nonempty path interior lies wholly in one of
  them.  A direct boundary edge has empty interior and needs no shore
  label; a boundary nonedge cannot have an empty-interior path, so every
  demanded nonedge has at least one literal shore label.
- Deleting the entire `gamma`-colour class gives the induced graph `Q` and
  leaves a proper five-colouring using all five colours on `R`.  A
  four-colouring of `Q`, or a five-colouring using at most four colours on
  `R`, extends with a fresh colour on the independent set `Gamma` and a
  colour absent from `N(u)=I union R` on `u`.  Either extension would
  six-colour `G`.  Thus `chi(Q)=5` and `R` is rainbow in every
  five-colouring of `Q`.
- In any such five-colouring, interchanging two colours on the component
  containing `r` when it misses `s` makes `r,s` monochromatic.  This
  contradicts the preceding universal rainbow conclusion, so Theorem 2.2
  has the stated quantifiers.

## Kriesell--Mohr conversion

Kriesell--Mohr, *Kempe Chains and Rooted Minors*, Theorem 7 states that
every graph on five vertices with at most six edges has property `(*)`.
The application here matches its hypotheses exactly:

- the five colour classes of `Q` are nonempty and `R` is a transversal;
- the demand graph has vertex set `R` and exactly
  `q=10-|E(G[R])|` edges;
- `q<=6` is explicit in Theorem 3.1(1) and (3); and
- every demanded pair belongs to one bichromatic component, so the demand
  graph is a spanning subgraph of the corresponding routing graph.

Property `(*)` therefore supplies five pairwise disjoint connected rooted
bags adjacent across every demanded nonedge.  Every omitted demand is an
actual edge of `G[R]`, which joins the two bags containing its endpoints.
This correctly completes an `R`-rooted `K_5` model.

For the two-shore construction, the relevant graphs are the induced
subgraphs `Q[E union R]` and `Q[F union R]`.  Each still contains the five
roots and hence all five colour classes.  A demand assigned to a shore has
a two-colour path in that induced subgraph, and each assigned demand graph
has at most six edges.  The two rooted certificates intersect across
shores only at `R`; within either certificate, the bag rooted at `r`
cannot contain a different root because the rooted bags are disjoint.
Uniting the two bags with common root `r` is therefore connected and
preserves pairwise disjointness.  Every demand adjacency survives from its
assigned shore, while every edge of `G[R]` remains literal.

## Terminal construction

When all nonedges are available in one shore `P` and `q<=6`, the corrected
proof applies Theorem 7 directly inside `Q[P union R]`.  The resulting five
rooted bags are wholly contained there and avoid `I`, the opposite shore
`P'`, and `u`.  The set `P' union I` is connected because `P'` is connected
and is adjacent to every vertex of `I`.  It is adjacent to every rooted bag
through that bag's root in `R`, and to `{u}` through the nonempty set `I`.
The singleton `{u}` is adjacent to every rooted bag through its root.
Together with the five pairwise adjacent rooted bags, these are seven
disjoint connected pairwise adjacent sets, so the displayed `K_7` model is
literal and complete.

## Corollary 3.2 capacity check

Every reserve nonedge is available in at least one shore, so the three
classes counted by `a,b,c`--`E`-exclusive, `F`-exclusive, and available in
both shores--are exhaustive and disjoint.  If `x` of the `c` flexible
demands are assigned to `E`, the two shore loads are

```text
a+x,    b+c-x.
```

They are both at most six precisely when the integer `x` can be chosen in

```text
[max(0,b+c-6), min(c,6-a)].
```

Under `a<=6` and `b<=6`, the upper endpoint is nonnegative, the lower
endpoint is at most `c`, and

```text
b+c-6 <= 6-a
```

follows from `a+b+c<=10<12`.  Hence this integer interval is nonempty.
Theorem 3.1(2) then supplies the rooted model.  The contrapositive is
exactly the corollary: if no `R`-rooted `K_5` exists, then `a>=7` or
`b>=7`.  The conclusion is inclusive--it makes no concentration claim in
instances where a rooted model already exists.

## Corollary 3.3 rotation check

Let `J` be any independent subset of `X` of order `d_G(u)-5`.  Since
`|X|=d_G(u)`, its complement `R_J=X-J` has exactly five vertices.  The star
on `{u} union J` is connected and its contraction is a proper minor, so it
has a proper six-colouring.  On expansion, assigning the contraction colour
to `u union J` is proper after omitting exactly the edges from `u` to `J`:
`J` is independent, and every edge from the contracted set to its exterior
was represented at the contraction vertex.

Every member of `R_J` is adjacent to the contraction vertex and hence avoids
its colour.  If these five vertices used at most four of the other five
colours, one of those colours would be absent from all of `X`.  Recolouring
`u` with it and restoring the omitted `uJ` edges would six-colour `G`.
Thus `R_J` uses all five other colours, one each.  Deleting `u` also deletes
every omitted edge, yielding the exact boundary partition
`J | {r} (r in R_J)` in a proper colouring of `G-u`.

The pair-coupling, root-to-`J` coupling, and shore-local shortest-path
assertions of Theorem 2.1 use only this exact singleton-reserve partition,
the two `X`-full components, and non-six-colourability of `G`.  Theorem 2.2
then uses only the same partition and `N(u)=J union R_J`.  Its deleted colour
class is independent because it is a colour class, and its extension
arguments remain valid.  The applications of Kriesell--Mohr in Theorem 3.1
and the capacity count in Corollary 3.2 consequently reapply with
`J,R_J,c_J`.

The revised proof correctly limits this generic reuse to the
Kempe-coupling and shore-localization assertions invoked from Theorem 2.1.
It does not transfer that theorem's separate degree-nine coexistence
observation, which depends on the trace-specific `I`-rooted `K_4` model, to
an arbitrary `J`.

## Dependencies and unresolved limits

No internal proof gap was found in the claimed conclusions.  The result
depends on the audited
short-trace classification, including its contraction-minor colouring and
the fact that the two exterior components are both `X`-full, and on the
exact cited Kriesell--Mohr theorem.

The theorem does not synchronize the packet paths with the crossed
`I`-rooted `K_4` model.  Its paths may intersect, and the
`c(r)`--`gamma` components may meet arbitrary members of `I`.  If seven or
more nonedge demands must be handled in one shore, Theorem 7 does not
apply; property `(*)` for `K_5` remains open.  A rooted `K_5` assembled
from both shores may consume both full components and supplies only six
bags after adding `{u}`.  No bounded separator or strict same-host
component descent follows from the packet alone.

The status-only promotion of the audited source has hash

```text
8471ee1cd4e82cf6e6906a4be0762c75df69ca0e09be76034c810d17e0f101cf
```

and makes no mathematical change to the revision audited above.
