# The direct-reserve substitution has a canonical fifth bag

**Status:** retracted during self-audit.

**Fatal gap.**  The two packets are full only to the literal old boundary
`S`.  The substituted root `z` lies in the old open shore, not in `S`, and
there is no `A-R` edge.  Hence neither packet is forced adjacent to the
substituted `z`-bag.  Lemma 1 below is correct, but Theorem 2 is false as
stated: its claimed packet--`z`-bag adjacencies are unsupported.  The note
is retained only as a barrier against repeating this lift.

## Setup

Use the frozen connected-bipartite atomic separation and the notation of
`hc7_direct_reserve_one_root_substitution.md`.  Thus

\[
 S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

`H=G[S]` is connected, `zu` is the unique `A-u` edge, and the direct bad
edge has ends `x,y in W`.  Let `r in W-{x,y}` be the retained endpoint of
the nontrivial bad path.  The audited substitution theorem supplies a
`{z,x,y,r}`-rooted `K_4^-` model in

\[
                     J=G[(A-z)\cup\{z,x,y,r\}].        \tag{1.1}
\]

Let `P_1,P_2 subseteq R` be the two disjoint adjacent connected `S`-full
packets from the atomic setup.

## Lemma 1 (canonical reserved component)

Let `C` be the vertex set of the component of

\[
                         H-\{x,y,r\}                   \tag{1.2}
\]

that contains `u`.  Then `C` is nonempty and connected, is disjoint from
the host (1.1), and is adjacent to the rooted `z`-bag and to at least one
of the rooted `x,y,r` bags in every model in (1.1).

### Proof

The three deleted vertices lie in `W`, so `u` belongs to a well-defined
nonempty component `C` of (1.2).  The host (1.1) contains no boundary
vertex outside `{x,y,r}`, hence `C` is disjoint from every one of its
branch sets.

The literal edge `uz` makes `C` adjacent to the branch set rooted at `z`.
Since `H` is connected and `C` is a proper nonempty subset of `V(H)`, an
edge of `H` leaves `C`.  Every vertex outside `C` but not among `x,y,r`
lies in a different component of (1.2), so the other end of such an edge
must be one of `x,y,r`.  Therefore `C` is adjacent to the corresponding
rooted branch set.  `square`

## Theorem 2 (rooted-`K_4` upgrade gives a labelled near-`K_7`)

If the substituted host (1.1) contains a literal
`{z,x,y,r}`-rooted `K_4` model, then its four bags together with

\[
                             C,P_1,P_2                 \tag{2.1}
\]

form a labelled `K_7^vee` model whose possible missing adjacencies are
both incident with `C`.  If `C` contacts three of the four rooted bags the
model is a `K_7^-`; if it contacts all four it is a literal `K_7`.

### Proof

The four rooted bags form a clique model and are disjoint from `C` by
Lemma 1.  The set `C` contacts at least two of them by that lemma.  Each
packet `P_i` is adjacent to every rooted bag through its literal root, and
to `C` because `C` is a nonempty subset of `S`.  The packets are disjoint,
connected, adjacent to one another, and lie in the open shore `R`, so all
seven displayed bags are pairwise disjoint.  Thus only the at most two
rooted bags not contacted by `C` can be nonadjacent to `C`.  The asserted
near-clique types follow.  `square`

## Exact remaining local gap

The direct-reserve rural residue no longer requires a search for a fifth
bag or a portal-contact maximization.  It requires the following one-edge
upgrade, with literal avoidance:

> Starting from an audited substituted rooted `K_4^-` in (1.1), either
> upgrade it to a rooted `K_4` while staying disjoint from `C`, obtain the
> already audited adjacent near-full carriers, or expose an actual cut of
> order at most six.

The first outcome gives Theorem 2.  The second invokes the audited adaptive
carrier return, and the third contradicts seven-connectivity.  A generic
rooted-diamond theorem does not supply this upgrade: its unique missing
pair is uncontrolled.  That labelled repair/web-exchange is the next
research target.
