# Independent audit: small boundary models through two full shores

Audited file:
`results/hc7_two_full_shore_small_model_exclusion.md`.

Audited SHA-256:
`a00784b4dccd5f51bab6e8a935e0c8ad261eb506d1d9a8390fc66ea84ee7860b`.

The source then incorporated exactly the three wording-only repairs in
Section 5.  Its resulting SHA-256 is
`69c44a925b7d3e142d01705f3b17b8244cf9c2927963346df4a813f2032de1e6`;
no mathematical statement or construction changed.

**Verdict:** **GREEN.**

The proper-boundary lift is a literal clique-minor model: all branch sets
are disjoint and connected, and every pair has an explicit witnessing
edge.  The support-at-most-six consequence orients a named model exactly
when that model is already known to lie in one closed shore.  Finally,
`K_2 vee C_5` has exactly five missing boundary edges, and adding any one
of them creates a five-vertex clique with the two apices.  Thus the frame
is edge-maximal and its apex pair is intrinsic.

No mathematical repair is needed.  Three wording repairs listed in
Section 5 would make the scope immune to misreading.

## 1. Theorem 1.1: literal model audit

Write

\[
                       W=\bigcup_{i=1}^r V(D_i)
\]

and choose `s in S-W` as in lines 26--35.  The asserted branch sets are

\[
                D_1,\ldots,D_r,\qquad A\cup\{s\},\qquad B.       \tag{A.1}
\]

Their disjointness is complete:

* the `D_i` are pairwise disjoint by the definition of a minor model;
* every `D_i` lies in `S`, while `A` and `B` are disjoint from `S`;
* `s` lies outside every `D_i`; and
* `A union {s}` is disjoint from `B` because `A,S,B` are pairwise
  disjoint.

Their connectivity is also literal.  Each `D_i` is connected in `G[S]`
and hence in `G`; `B` is connected by hypothesis; and an edge from `s` to
`A` attaches `s` to the connected set `A`.

Every required clique adjacency has a witness:

| Pair of branch sets | Witness |
|---|---|
| `D_i,D_j` | adjacency in the given `K_r` model |
| `D_i,A union {s}` | choose `x in D_i`; fullness gives an `x-A` edge |
| `D_i,B` | the same `x` has a neighbour in `B` |
| `A union {s},B` | fullness at `s` gives an `s-B` edge |

This accounts for all pairs in (A.1), including `r=1`.  Lines 32--44
therefore prove a genuine `K_{r+2}` model.  The no-`A-B`-edge hypothesis
at line 18 is not used; it is natural for the shore application, but the
theorem remains true if that hypothesis is deleted.

## 2. Corollary 2.1: exact-seven orientation

Since `|S|=7`, a `K_5` model on at most six vertices has support properly
contained in `S`.  Theorem 1.1 therefore excludes such a model from
`G[S]`, exactly as lines 61--63 assert.

For the orientation assertion, denote the open shores by `A,B`, so the
closed shores are `A union S` and `B union S`.  Suppose the support `W` of
the named model satisfies `W subseteq A union S`.  If `W cap A` were empty,
then `W subseteq S`, contradicting the first part of the corollary.  Hence
`W cap A` is nonempty.  Because `A` is disjoint from `B union S`, the same
model cannot also be contained in the opposite closed shore.  The argument
is symmetric with `A,B` interchanged.

Thus the claimed orientation is unique.  It applies only to a
support-at-most-six model already carried by a closed shore; it makes no
claim about a model straddling both open shores.  No separate convention
that a named model is “not allowed to straddle” is needed.

## 3. Corollary 3.1: maximality and uniqueness of the frame

Let the apices be `p,q` and let the cycle be
`v_0 v_1 v_2 v_3 v_4 v_0`.  The frame already contains `pq`, all ten
apex-to-cycle edges, and the five cycle edges.  Its only missing edges are
the five cycle chords.

For every chord `v_i v_{i+2}`, the vertices
`v_i,v_{i+1},v_{i+2}` form a triangle after that chord is added (indices
modulo five).  Together with `p,q`, they form a literal `K_5` on five
boundary vertices.  Corollary 2.1 excludes that proper-support model.
Consequently no chord of the cycle can occur in `G[S]`, and because there
are no other missing pairs, `G[S]=H_0`.

The degree sequence of `H_0` is

\[
                             6,6,4,4,4,4,4.
\]

Hence `p,q` are the only possible apices of any spanning
`K_2 vee C_5` subgraph.  There is also a direct edge-count proof of frame
uniqueness: every such spanning frame has

\[
                              1+10+5=16
\]

edges, while it is a subgraph of the now-established 16-edge graph
`G[S]=H_0`.  Its edge set must therefore equal `E(H_0)`.  This proves both
the asserted edge-set rigidity and the apex-pair rigidity.

## 4. Counterexample search and sharpness checks

The cyclic frame itself does not contradict Corollary 2.1.  It has the
following `K_5` model:

\[
   \{p\},\quad \{q\},\quad \{v_0,v_1\},\quad
   \{v_2,v_3\},\quad \{v_4\}.
\]

All seven boundary vertices are used.  Thus the word “proper” in Theorem
1.1 and the support bound six in Corollary 2.1 are essential.  The
`I vee K_2` sharp example in
`results/hc7_near_k7_exact7_boundary_threshold.md` realizes this exact
boundary with two full shores in a `K_7`-minor-free graph.

As a finite sanity check, exhaustive enumeration of all five-branch-set
assignments on the seven labelled vertices gave minimum `K_5` support
seven for `K_2 vee C_5`.  Repeating the enumeration after adding each of
the five possible chords gave minimum support five in every case.  A
separate enumeration of spanning `K_2 vee C_5` subgraphs of `H_0` found
one edge set and one apex pair.  These checks agree with the proofs above;
the verdict does not depend on them.

No counterexample survives the literal branch-set, orientation, or frame
tests.

## 5. Wording repairs

These edits do not change any mathematical claim.

1. At lines 63--66, replace the appeal to what a named model is “allowed”
   to do by the direct support argument:

   > If the model is contained in `A union S` but not in `S`, its support
   > meets `A`.  Since `A` is disjoint from `B union S`, it is not contained
   > in the opposite closed shore.  The other orientation is symmetric.

2. At lines 98--100, avoid any ambiguity over whether a “frame” includes
   a chosen cyclic presentation:

   > Any second spanning `K_2 vee C_5` subgraph has 16 edges and is a
   > subgraph of the 16-edge graph `G[S]=H_0`; hence it has the same edge
   > set.  Its apices are the two degree-six vertices.

3. Qualify the summary at lines 111--114.  The proved statement is:

   > a named support-at-most-six `K_5` model known to lie in one closed
   > shore supplies a unique orientation of that cell.

After this audit exists, the status line at line 3 may also be updated from
“independent audit pending” as an editorial bookkeeping change.
