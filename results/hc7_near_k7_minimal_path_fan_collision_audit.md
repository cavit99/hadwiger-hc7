# Exact-file audit of the minimum-path fan-collision theorem

**Status:** separate internal audit — **GREEN**.

## Audited revision

- File: `results/hc7_near_k7_minimal_path_fan_collision.md`
- SHA-256: `367dcc0da0cb245730dd1f8a9a1c33bd6d3791df228019b277ab648ce788b696`
- Scope: cold, line-by-line audit of this file alone.  No surrounding research
  narrative was used to supply a missing hypothesis or inference.

The cold audit was performed on SHA-256
`9901823130fe65593d0b2bad695d540ed1914c412d146dbf8fe80fbd2cda5611`.
The only subsequent source change was line 3, from the draft-status notice to
`**Status:** written proof; separate internal audit — **GREEN**.`  No
mathematical content changed.  Reverting that status line exactly reproduces
SHA-256 `9901823130fe65593d0b2bad695d540ed1914c412d146dbf8fe80fbd2cda5611`;
the GREEN verdict therefore applies unchanged to the promoted file hash above.

## Verdict

**GREEN.**  The stated results follow from the hypotheses in the audited
revision.  I found no invalid branch-set replacement, fan truncation, label
exclusion, `2+2`/`2+3` deduction, or separation-order claim.  There is no
unresolved mathematical assumption or proof gap within the stated scope.

This is a genuinely unbounded graph-theoretic result: it uses no enumeration,
finite search bound, or bounded-order reduction.  Under the standard convention
that the graphs under discussion are finite, it applies uniformly to every
graph satisfying its hypotheses.

## Hypotheses and trust boundary checked

The proof uses exactly the following host-level assumptions.

1. `G` is seven-connected (lines 29, 167--176, and 267).
2. `G` has no `K_7` minor (lines 25--27 and 199).
3. `G` contains an oriented `K_7^-` model as defined in lines 13--23.
4. The displayed orientation is chosen with `|L|` globally minimum over **all**
   oriented `K_7^-` models in the fixed graph, including both orientations of
   every deficient pair (lines 29--37).  This full minimization is what licenses
   every later contradiction by a smaller distinguished branch set.

Seven-chromaticity, contraction-criticality, proper-minor colourings, and the
more restrictive component-contact configurations are not used.  The trust
boundary described in lines 304--334 is therefore accurate: the exchanges
preserve an oriented near-clique model, but are not shown to preserve any of
that additional colouring or label data.

## Principal claims checked

### 1. Path normal form (Proposition 1.1, lines 46--110)

For a non-cutvertex `x` of `G[L]`, deleting `x` leaves a nonempty connected
branch set.  If `P_L(x)` is empty, all five contacts survive.  If
`P_L(x)={i}`, moving `x` into `B_i` makes `B_i union {x}` connected, preserves
all old named-branch-set adjacencies, and leaves `L-{x}` adjacent to the
enlarged branch set through an edge from `x` to `L-{x}` (lines 76--90).
Because `L` and `R` are anticomplete under `K_7`-minor exclusion, the deficient
pair remains nonadjacent.

Hence every non-cutvertex owns at least two private labels.  Private-label sets
for distinct vertices are disjoint, so five labels allow exactly two
non-cutvertices.  The spanning-tree argument in lines 98--107 correctly forces
`G[L]` to be a path.  Two disjoint endpoint-label sets of size at least two in a
five-element set give only `2+2` or `2+3`, with the stated leftover/partition
conclusions.

### 2. Clean-path exchanges (Lemma 2.1, lines 119--157)

A clean `L`--`R` path can be absorbed into `L` up to its last vertex, producing
seven pairwise disjoint connected branch sets with every required adjacency
(lines 137--140).  For the endpoint exchange, the clean paths enlarge distinct
`B_i` without intersecting one another or another old branch set; the one
unserved private label absorbs the endpoint, while `L` loses that endpoint
(lines 142--151).  All five contacts and all old adjacencies persist.  The new
distinguished branch set has size `|L|-1`, so global oriented-model minimality
excludes these exchanges.

### 3. Five-fan collision (Theorem 3.1, lines 159--212)

Deleting `s,t` from a seven-connected graph leaves a five-connected graph.
The Fan Lemma therefore gives a five-fan from an internal vertex of `L` to any
five chosen targets in distinct sets among `B_1,...,B_5,R`.  Truncating each fan
path after its last vertex of `L` and at its first later model branch set makes
it clean; fan disjointness preserves disjointness outside `L` and gives
distinct first-entry vertices (lines 167--184).

An entry in `R` would yield a `K_7` minor.  An entry with a label private to the
two-label endpoint would trigger the one-path endpoint exchange.  Thus in the
`2+2` case only `B_e` remains.  In the `2+3` case, two distinct remaining
private labels at the three-label endpoint would trigger the two-path endpoint
exchange; consequently all five entries use one branch set.  The exclusions
and both collision conclusions are exhaustive.

### 4. Balanced full-neighbourhood separation (Theorem 4.1, lines 219--282)

If the component `C` met `R` or a named branch set other than `B_e`, a path in
`C`, stopped at its first model branch set and shortened after its last vertex
in `L`, would be a forbidden clean path of one of the preceding types.  Hence
those branch sets lie outside `C`, and the component definition gives
`N_G(C) subseteq {s,t} union V(B_e)` (lines 253--266).

The opposite open side is nonempty because it contains `R` and the four other
named branch sets.  Seven-connectivity therefore gives `|N_G(C)|>=7`.  Both
path endpoints lie in `N_G(C)`, so at least five boundary vertices lie in
`B_e`.  If exactly five do, the boundary has exactly the two endpoints plus
those five vertices and hence order seven; `|B_e|=5` forces that equality.
The draft correctly makes no unconditional upper-bound claim.

## Non-mathematical presentation caveats

These do not affect the GREEN verdict.

1. Finiteness and the usual simple-graph convention are implicit rather than
   stated.  Finiteness matters to the literal `|L|-1<|L|` descent; the theorem
   should not be read as an infinite-graph statement without reformulation.
2. “Full-neighbourhood separation” is used without spelling out the ordered
   pair.  The proof supports the standard separation
   `(C union N_G(C), V(G)-C)`, whose separator is `N_G(C)` and whose open sides
   are `C` and `V(G)-(C union N_G(C))`.
