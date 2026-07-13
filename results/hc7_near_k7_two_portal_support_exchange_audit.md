# Independent audit: two-portal support exchange

## Verdict

**GREEN after the incorporated scope corrections.**  The set-Menger
dichotomies, protected shore construction and full-profile extension are
valid.  The source now states the necessary helper-family attachment
hypothesis and distinguishes a true cutvertex portal arm from the
degenerate one-vertex side gate in the flexible theorem.

## 1. Exact set-Menger formulation

For disjoint terminal sets `S={l,r}` and `T={x,y}`, use the vertex
version in which a separator `Z` may meet `S union T`, and separation
means that `K-Z` has no path from `S-Z` to `T-Z`.  Equivalently, add
superterminals and give every vertex of `K` unit capacity.  If two
vertex-disjoint `S-T` paths do not exist, the minimum separator has order
at most one.  Connectedness of `K` excludes the empty separator.

Two disjoint paths necessarily use distinct members of each two-element
terminal set, hence saturate both sets.  The linkage and separator
outcomes are mutually exclusive: deleting one vertex destroys at most
one of the two disjoint paths, while the other survives with both of its
terminal ends.

The same argument in Theorem 3 is valid after adding `lambda,rho`.
Neither new source vertex can be the one-vertex separator, because the
other source still reaches nonempty `X_Q` through connected `K`.  Thus
the separator lies in `K`, and its component formulation is exactly the
absence of a source-to-target path in the augmented graph.

## 2. Shores and literal contacts

In the linkage outcome, deleting the artificial sources if present
leaves two vertex-disjoint paths.  Their initial vertices have literal
edges to `L,R`, respectively, so adjoining them to the two connected path
sides gives disjoint connected shores.  The old cut edge joins the
shores.  Their distinct terminal portals have literal edges to the
unchanged connected row `Q`.

All new vertices lie in the one old exterior piece `K`.  Other old
exterior pieces and every foreign bag are disjoint from `K`; no helper
contact is consumed.  To compose with literal shore completion, the
helper families must additionally be mutually disjoint, avoid `K`, and
already attach to their assigned path sides.  That hypothesis is now
explicit in Corollary 2, so adjoining the helpers preserves both
connectedness and every literal row contact.

If both protected portals individually meet every row in `mathcal Q`,
the two linkage paths terminate at different such portals.  Each shore
therefore meets every row in the full profile.  No claim is made from
the weaker condition that their combined neighbourhood covers the
profile.

## 3. Two-connected and flexible cases

With four distinct terminals, deleting any one vertex of a
two-connected `K` leaves a connected graph and leaves both terminal sets
nonempty.  Hence no one-vertex set-separator exists and the linkage
outcome follows.

For flexible attachment sets, outcome 2 does not always make `z` a
cutvertex.  Since `|X_Q|>=2`, a surviving target portal remains after
deleting `z`.  If `K-z` is connected, the component condition forces

\[
                    A_L\cup A_R\subseteq\{z\}.
\]

Otherwise `z` is a cutvertex and every component containing a surviving
`Q` portal contains no side attachment.  The corrected source records
exactly these two possibilities.  This matters for recursion: the first
is a concentrated side gate, not a block-cut portal arm.

## Scope

The theorem is one protected exchange, not a terminating recursion.
Any continuation through successive foreign bags must still exhibit a
strictly decreasing measure, and a rural terminal must cover the whole
host with one literal apex pair.  Neither conclusion is inferred here.
