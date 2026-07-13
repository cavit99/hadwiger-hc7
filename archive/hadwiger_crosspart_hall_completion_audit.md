# Independent audit: cross-part Hall completion

## Verdict

**GREEN AS PATCHED.**  The branch-set construction is correct.  There is
one harmless but real notation error in the exchange paragraph: after
replacing the representative `t_h` by the formerly unused root `u`, the
two unused roots are the old `v` and the old `t_h`, not the old `u,v`.
Renaming the old `t_h` to `w` repairs (1.5) and (1.6).

The hypotheses in the note are considerably stronger than necessary.
In particular:

* collective coverage of **every root** can be weakened to collective
  coverage of **at least one root in every pair part**; and
* the relative-boundary lower bound in Corollary 2.1 can be weakened
  from `k+1` to `k-2`.

The result is a sound uniform completion module.  It does **not** by
itself close the current `C_6 dotcup K_1` state: that boundary is not
pair-mode, and the remaining rank-two/rank-two SPQR architecture has not
yet been shown to contain the required four pairwise adjacent pieces.

## 1. Exact corrected theorem

Let `k=2q+1`, with `q>=2`, and put

\[
 T=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_q,
 \qquad |B_j|=2,\qquad S=T\mathbin{\dot\cup}\{s\}.
\]

It is enough that `G[S]` **contain** all edges between distinct parts and
all edges from `s` to `T`; edges inside a part may also be present.  Let
`R` be a connected set disjoint from `S` with a neighbour at every
vertex of `S`.  Let

\[
 U_1,\ldots,U_{k-3}
\]

be nonempty, connected, pairwise disjoint, pairwise adjacent sets,
disjoint from `R union S`, and put `P_i=N_S(U_i) cap T`.

Then the following two portal conditions are equivalent.

1. There is an injection `f:{1,...,k-3}->T`, with `f(i) in P_i`, whose
   two omitted roots lie in different pair parts.
2. The family `(P_i)` satisfies Hall's condition and
   \[
       (\bigcup_iP_i)\cap B_j\ne\varnothing
       \quad\hbox{for every }j.
   \]

Under either condition, `G` contains a `K_k` minor.

The original Theorem 1.1 follows, since covering every root certainly
meets every pair part.

### Proof of the equivalence

Condition 1 immediately implies Hall.  If the union of the rows missed
some `B_j`, both vertices of `B_j` would have to be omitted by every
representative system, contradicting the cross-part conclusion.

Conversely, take an arbitrary Hall transversal.  If its two omitted
roots lie in different parts, stop.  If they are `u,v in B_j`, choose
`u in P_h` for some `h`, which is possible because the union meets
`B_j`.  Replace the old representative `t_h` by `u`.  The old matching
used neither member of `B_j`, so `w:=t_h` is outside `B_j`.  The new
omitted pair is therefore `v,w`, a cross-part pair.

### Correct branch sets

With a transversal whose omitted roots are `u,v` in different parts,
use

\[
 U_i\cup\{t_i\}\quad(1\le i\le k-3),\qquad
 R,\qquad \{s\},\qquad\{u,v\}.
\]

There are exactly `k` sets.  They are disjoint.  Each enlarged `U_i` is
connected because `t_i in N_S(U_i)`, and `{u,v}` is connected by the
cross-part boundary edge.  The enlarged `U_i` are mutually adjacent
through the original `U_i`.  Each is adjacent to `R` through `t_i`, to
`{s}` through `t_i s`, and to `{u,v}` because two roots in different
parts cannot both lie in the part containing `t_i`.  Finally, fullness
of `R` supplies its adjacencies to all three kinds of boundary bags, and
`s` is adjacent to both `u` and `v`.  Thus every required bag adjacency
is present.

This also checks that no illicit contraction, overlap, or hidden
connectivity assumption occurs in the construction.

## 2. Line-by-line audit of the submitted proof

* **(1.1):** sound, but equality with the complete multipartite graph is
  stronger than needed; containment suffices.
* **(1.2)--(1.4):** Hall gives exactly `k-3` distinct representatives in
  the `k-1`-vertex set `T`, so precisely two roots remain.
* **Exchange paragraph:** the combinatorial exchange is valid.  The
  displayed names after the exchange are wrong.  If the old unused pair
  is `u,v` and `u` replaces `t_h`, the new unused pair is `v,t_h`.
* **Connectivity/disjointness of (1.6):** valid after that renaming.
  No `U_i` meets `S` or `R`, and the chosen roots are all distinct.
* **Adjacency among enlarged pieces:** valid because pairwise adjacency
  of sets means an actual edge joins every pair `U_i,U_j`.
* **Adjacency to `R`:** valid through the matched root, not through an
  unstated `U_i-R` edge.
* **Adjacency to `{s}`:** valid through `t_i s`.
* **Adjacency to the final two-root bag:** valid for the precise reason
  stated above: at least one omitted root is outside the part of `t_i`.
* **Remaining three bags:** all adjacencies follow from `R` being full
  to `S`, the universal role of `s`, and the cross-part edge `uv`.
* **Parameter edge case:** `q=2` is valid.  Then `k=5`, there are two
  pieces, and the same exchange and bag count work.  The stated range
  `q>=2` is therefore correct.  (For `q=1` the coverage hypotheses with
  zero pieces cannot hold.)

## 3. Corrected strict-clique consequence

The following strengthens Corollary 2.1.

Let `D` be a clique of order `k-3`, disjoint from `R union S`.  It is
enough to assume

\[
 N_T(D)=T
\]

(collective `T`-fullness; contact with `s` is unnecessary) and

\[
 |(N_D(X)-X)\mathbin{\dot\cup}N_S(X)|\ge k-2
 \tag{A}
\]

for every nonempty proper `X subset D`.  Then `G` has a `K_k` minor.

Indeed, cliquehood gives `N_D(X)-X=D-X`.  From (A),

\[
 |N_T(X)|\ge |N_S(X)|-1
 \ge (k-2)-|D-X|-1=|X|.
\]

Thus every proper subfamily satisfies Hall.  At `X=D`, collective
`T`-fullness gives `|N_T(D)|=k-1>|D|`; it also makes every pair part
meet the union of the rows.  The corrected theorem applies.

The submitted bound `k+1` gives the stronger, correctly calculated
estimate `|N_T(X)|>=|X|+3`, so its corollary is certainly valid.  The
word "full" should be defined explicitly as collective fullness
`N_S(D)=S`; it must not be read as complete bipartite adjacency of every
vertex of `D` to every vertex of `S`.

The threshold `k-2` is the natural sharp threshold for this automatic
Hall derivation: at `k-3`, a proper `X` can have `|N_S(X)|=|X|`, with
`s` among those neighbours, leaving only `|X|-1` available roots in
`T`.

## 4. Independent finite check at `k=7`

The existing exact monotone verifier
`strict_order4_full_gate_verify.py` was rerun under NetworkX/Z3.  It
enumerates all strict `4 x 7` contact matrices in the original
order-four cell and independently checks explicit `K_7` models.  It
returned

```text
displayed connectivity 7; unique minimum cut (0, 1, 2, 3, 4, 5, 6)
displayed K7 bags ((3, 7), (4, 8), (5, 9), (1, 10), (11,), (6,), (0, 2))
all strict K4 contact matrices {'status': 'unsat', 'iterations': 55}
```

This is not needed for the hand proof, but it independently checks the
`q=3` application against every contact matrix in that finite strict
cell.

## 5. Interface with the remaining `C_6 dotcup K_1` state

The theorem does not directly apply to that boundary.  If the missing
graph on the six non-universal roots is `C_6`, choosing three pair parts
from alternate cycle edges still leaves the other three cycle edges
missing **between** parts.  Hence the cross-part completeness used in
the bag-adjacency check is absent.

There is, however, a precise reusable interface.  The same branch-set
proof works for an arbitrary boundary whenever a portal transversal
leaves roots `u,v` such that

1. `uv` is an edge, and
2. every matched root is adjacent to at least one of `u,v`.

For a `C_6` missing graph, every antipodal pair has exactly this
property: it is an edge of `G[S]`, and it dominates the other four roots
in `G[S]`.  Consequently:

> Four disjoint pairwise adjacent carrier pieces, with a portal
> transversal onto the four roots outside some antipodal pair, together
> with the opposite full shore and the universal root, force `K_7`.

This gives a clean terminal condition for the `C_6` carrier programme.
What is still missing is the extraction.  The current rank-two/rank-two
SPQR survivor supplies six portal classes and simultaneous crossless
states, but it has not been proved to contain four pairwise adjacent
pieces with the required antipode-avoiding transversal.  Therefore this
Hall completion composes with a future capacity-three/K4-core outcome;
it does not replace the needed simultaneous-web/SPQR exchange theorem.

## Final classification

* Theorem 1.1: **GREEN after renaming the post-swap unused roots.**
* Corollary 2.1: **GREEN**, with a valid but non-sharp `k+1` hypothesis;
  `k-2` suffices.
* Uniform value: genuine and parameter-uniform.
* Immediate `C_6` closure: **not obtained**; the precise missing input is
  a four-piece antipode-avoiding carrier extraction.
