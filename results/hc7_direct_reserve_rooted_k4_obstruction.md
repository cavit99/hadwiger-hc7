# The substituted direct-reserve host is rooted-`K_4` or a clean rural disk

**Status:** proved and independently audited; literature-dependent.

## Setup

Use the frozen direct-reserve atom and the audited one-root substitution.
Thus

\[
 J=G[A\cup\{x,y,r\}],\qquad Q'=\{z,x,y,r\},
\]

where `z in A`, `x,y,r in W subseteq S`, `xy in E(G)`, and

\[
                       zx,zy,zr\notin E(G).             \tag{1.1}
\]

The last nonedge follows for `r` exactly as for `x,y`: all three are
forced-one endpoints.  The audited closed-shore theorem says that
`(J,Q')` is internally four-connected, and `|V(J)|>=6`.

## Theorem (exact rooted obstruction)

Exactly one of the following holds.

1. `J` contains a literal `Q'`-rooted `K_4` model.
2. `J` has a planar embedding in which `z,x,y,r` all lie on the boundary
   of one face.

In outcome 2 no completion edge or fill-clique vertex is being treated as
a host edge: the embedding is an embedding of the literal graph `J`.

### Proof

Assume outcome 1 fails.  By Fabila-Monroy--Wood, Theorem 15, `J` is a
spanning subgraph of one of their six rooted obstructions
`A,B,C,D,E,F`, with nominated vertices `Q'`.

First remove a feature common to all six obstruction classes.  Write the
containing obstruction as `H+`, with each set `X_T` a clique placed behind
a facial triangle `T` of the base graph `H`.  No `X_T` is nonempty.
Indeed, all nominated vertices belong to `H`, while every neighbour of
`X_T` in `H+` lies in `T union X_T`.  Thus a nonempty `X_T` gives in the
spanning subgraph `J` a separation of order at most three with a nonempty
open side containing no root and all four roots on the other side (roots
in `T` lie in the adhesion).  This contradicts the internal
four-connectivity of `(J,Q')`.  Consequently the containing obstruction
has the same vertex set as its literal base graph `H`.

Now observe that `z` cannot be a degree-two nominated vertex of the base
obstruction.  In that case `d_J(z)<=2`.  Every neighbour of `z` outside
`J` lies in the four-set `S-{x,y,r}`: there is no `A-R` edge and `J`
already contains all of `A`.  Hence

\[
             d_G(z)\le d_J(z)+|S-\{x,y,r\}|\le6,
\]

contrary to seven-connectivity (equivalently, to minimum degree at least
seven).

Classes `B,C,F` have every nominated vertex of degree two, so they are
impossible.  In class `A`, either `z` is one of the three degree-two
nominated vertices, which is impossible by the preceding paragraph, or
`z` is the exceptional nominated vertex `p`.  In the latter case the
other three nominated vertices are pairwise nonadjacent in the
obstruction, contradicting the literal edge `xy` in its spanning
subgraph.

In class `E`, two nominated vertices have degree two, while the only edge
between nominated vertices is the edge joining the other two nominated
outer-face vertices.  Since `xy` is literal, `x,y` would have to be those
two outer vertices, leaving `z` degree two, again impossible.

Only class `D` remains.  By the first paragraph its containing obstruction
is the literal planar skeleton `H`, with the four nominated vertices on
its outer face.  Thus `J` is a spanning subgraph of `H`.  Restricting
the embedding of `H` to `J` gives a planar embedding of `J`; deleting edges
can only merge faces, so the four nominated outer-face vertices remain on
one common face.  This is outcome 2.  Fabila-Monroy--Wood's web obstruction
also shows the two outcomes are exclusive.  `square`

## Exact consequence and obstruction

The proposed unconditional assertion that the substituted host always has
a rooted `K_4` is therefore not justified by the frozen hypotheses.  Its
only possible failure is now a **literal clean rural disk**, not one of the
five low-separation rooted obstructions and not a web with hidden fill
cliques.

This does not itself yield an actual exact-seven adhesion.  The remaining
constructive obligation is sharply:

> In the clean rural embedding, use the three omitted vertices of `W`,
> their literal portals into `A-z`, the compulsory edge `zu`, and the two
> rich packets to obtain either (i) a rooted-`K_4` crossing, (ii) two
> adjacent near-full carriers, or (iii) a literal separator whose old
> boundary lift has order seven and comes with a named receiving packet or
> near-model certificate.

Any proof that merely returns another unlabelled web has made no progress.

## Primary source

R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electronic Journal
of Combinatorics 20(2) (2013), Theorem 15 and the definitions of classes
`A`--`F`: <https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i2p64/pdf/>.
