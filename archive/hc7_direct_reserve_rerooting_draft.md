# Direct-reserve rerooting across the compulsory root

**Status:** superseded draft.  The corrected theorem and independent audit
are `../results/hc7_direct_reserve_one_root_substitution.md` and its adjacent
audit.

## Setup

Use the frozen atomic separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |W|=6,
\]

where `G` is seven-connected, `A` and `R` are nonempty, there is no
`A-R` edge, and `zu` is the unique edge from `A` to `u`.  Assume the
nonsingleton atomic shore has reached the audited normalization:

\[
                  A-z\text{ is connected and `W`-full},
                  \qquad |A|\ge3.
\]

Let `xy` be the literal-edge member of the sole direct-reserve rural
residue.  Thus `x,y` are the ends of a direct parity-bad path in the
canonical two-list obstruction at the split `{z}|(A-z)`.

## Lemma 1 (the direct bad edge avoids the compulsory root)

Both `x` and `y` lie in `W`, are forced to the carrier `A-z`, and satisfy

\[
                            zx,zy\notin E(G).
\]

### Proof

In the canonical lists, `u` is the only boundary vertex forced to the
carrier `{z}`.  Every other singleton list is the carrier `A-z`; a
flexible vertex has both carrier labels.  The ends of a parity-bad path
are singleton-list vertices.  On a one-edge path, the bipartite parity
condition fails exactly when its two prescribed labels are equal.
There cannot be two distinct vertices forced to `{z}`, so the two ends
are forced to `A-z`.  In particular neither is `u`, and the definition of
the literal list says that neither has an edge to `z`.  \(\square\)

## Theorem 2 (a substituted rooted diamond)

Reorient the same literal separation as

\[
 A'=A-z,\qquad S'=W\cup\{z\},\qquad R'=R\cup\{u\}.
\]

Then `A',S',R'` are a partition of `V(G)`, both open shores are nonempty,
`|S'|=7`, and there is no `A'-R'` edge.

Let `Q` be the four original rural roots, with `x,y in Q`, and choose

\[
                         r\in(Q\cap W)-\{x,y\}.
\]

The graph

\[
                  G[(A-z)\cup\{z,x,y,r\}]
\]

contains a `{z,x,y,r}`-rooted `K_4^-` model.  In particular this model
uses neither `u` nor the fourth original root omitted from
`{z,x,y,r}`.

### Proof

The displayed sets form a partition by construction.  The set `A-z` is
nonempty.  The set `R union {u}` is nonempty because `R` is.  There is no
edge from `A-z` to `R` by the original separation, and no edge from
`A-z` to `u` because `zu` was the unique `A-u` edge.  Hence there is no
`A'-R'` edge.

The set `S'=W union {z}` has order seven.  Apply the audited closed-shore
rooted-connectivity theorem to this reoriented separation and the
four-set

\[
                             \{z,x,y,r\}\subseteq S'.
\]

It follows that the rooted pair

\[
       \bigl(G[(A-z)\cup\{z,x,y,r\}],\{z,x,y,r\}\bigr)
\]

is internally four-connected.  Since `|A|>=3`, this graph has at least
six vertices.  Jorgensen's rooted-diamond theorem therefore supplies the
claimed rooted `K_4^-` model.

The host graph used for that model contains neither `u` nor any member of
`Q-{x,y,r}`.  The avoidance assertion follows literally.  \(\square\)

## Scope

This is a genuine label-preserving model-regeneration step.  It does not
identify a colour with a branch-set label and does not preserve the old
rooted model.  It also does not yet close the direct-reserve cell: the
new diamond's missing pair must be repaired or exchanged while preserving
the omitted root as a usable fifth label.

The next proof must compare all such rerooted diamonds by a finite portal
signature.  A blocked exchange may expose an actual exact-seven adhesion;
seven-connectivity rules out only adhesions of order at most six.
