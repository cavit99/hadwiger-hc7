# Kempe reachability for a movable boundary portal

## 1. Exact one-coordinate lemma

Let (Q) have a proper (r)-colouring (c), and let (X\subseteq V(Q))
be a labelled boundary.  Suppose (w\in X) is the only boundary vertex
of colour (alpha).  Let

\[
 B=\{x\in X:c(x)=\beta\}
\]

for a second colour (eta\ne\alpha), and assume (w) is nonadjacent to
every vertex of (B).  Thus replacing the singleton boundary block
(\{w\}) by (B\cup\{w\}) is a proper equality state on (X).

### Lemma 1.1 (decoration or Kempe connector)

At least one of the following conclusions is forced.

1. (Q) has a proper (r)-colouring with the same equality state on
   (X-w) in which (w) joins the block (B); or
2. in the original colouring, the (alpha/\beta)-component containing
   (w) contains a vertex of (B), and hence contains a (w)-(B)
   path whose internal vertices avoid (X).

### Proof

Let (K) be the component of the subgraph induced by colours
(\alpha,\beta) that contains (w).  If (Kcap B=\varnothing), interchange
(alpha,eta) on (K).  No boundary vertex other than (w) of colour
(alpha) exists, and no boundary vertex of colour (eta) lies in (K).
Thus the switch changes only (w)'s boundary block, joining it to (B).
If this conclusion is unavailable, (Kcap B\ne\varnothing); a shortest
path in (K) from (w) to (B) has no other boundary vertex internally.
□

The statement is deliberately about a singleton boundary coordinate.  If
the current (alpha)-block contains other boundary vertices, a switch may
move those vertices with (w), and the clean conclusion is false without
recording that second obstruction.

## 2. Multi-target form

Let (B_1,\ldots,B_m) be boundary colour blocks, each legal to merge with
the singleton (w)-block.  If none of the (m) merged states extends, then
for every (i) there is a bichromatic (w)-(B_i) path.  The union of
these paths is connected and gives a single (w)-region touching every
target block.

This is the rigorous exchange behind the proposed `w`-state majority
arguments.  It has an unavoidable geometric residue: the paths for
different target colours may meet prescribed rooted supports.  In the
reserved Moser connector, that yields the exact dichotomy

\[
 \text{a new decorated boundary state}
 \quad\text{or}\quad
 \text{a connected }w\text{-region meeting the locked supports}.
\]

If the region avoids the two supported-frame carriers, it is the
singleton-(w) absorber used by the bilateral portal-transfer theorem.  If
it meets a carrier, its first intersection is a concrete rerouting portal.
The remaining task is to prove that the resulting rerouting either preserves
the other carrier or exposes a minimum adhesion; abstract equality-state
data alone does not decide that disjointness question.

## 3. Scope

No minor-criticality is required for Lemma 1.1.  Minor-criticality supplies
the colourings and says that a missing decoration created by an internal
operation must be compatible with the opposite side.  The lemma then turns
failure of a desired state into an actual coloured path, which is the
geometric information lost by a finite state table.
