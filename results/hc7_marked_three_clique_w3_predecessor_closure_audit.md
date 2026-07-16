# Cold audit of the balanced-three predecessor closure

**Verdict: GREEN.**  The predecessor lift in
[`hc7_marked_three_clique_w3_predecessor_closure.md`](hc7_marked_three_clique_w3_predecessor_closure.md)
is valid under its stated hypotheses and produces seven literal branch
sets in `H_a`.  The source version audited here has SHA-256

```text
50f4179051a808337cddcb0ae0ec6b10eeacc150f2350760afea2c891a708a21
```

This closes the actual balanced `|W|=3` branch when the three marks are
the images of a matching of split edges and each one-edge predecessor is
seven-connected.  It does not prove the abstract marked three-clique
theorem or the `|W|=4,5` branches.

## 1. Hypotheses and expanded cuts

Let `e_a=x_ay_a` and `H_a=G/(F-{e_a})`, so that contracting the one
remaining literal edge `x_ay_a` gives `H`.  The matching assumption on
`F` makes `x_a,y_a` two new vertices distinct from the other two marked
images and from every `B_i` vertex.

For a row cut `S_i=W union B_i`, deleting

\[
 S_i^a=(S_i-\{z_a\})\cup\{x_a,y_a\}
\]

from `H_a` deletes exactly the material represented by deleting `z_a`
from `H`.  All other vertices and edges are unchanged.  Consequently
`H_a-S_i^a` and `H-S_i` have literally the same two nonempty open
components.  Thus `S_i^a` is a genuine separator of order seven.

Because `H_a` is seven-connected, this is a minimum separator.  Every
member of a minimum separator has a neighbour in each open component:
if one boundary vertex missed one component, deleting the other six
boundary vertices would still separate it.  Applying this fact separately
to `S_a^a` and `S_b^a` gives

\[
 x_a,y_a\in N_{H_a}(P_a)\cap N_{H_a}(P_b).
\]

The use of two different row cuts is essential and is explicit in the
source.  Fullness of only `S_a^a` would not identify `P_b` inside its
opposite shore.

The descriptive phrase "inclusion-minimal three-edge contraction" is not
defined or used in this theorem.  The operative hypothesis is the stated
seven-connectivity of every `H_a`.  Whether a proposed global minimality
choice supplies that hypothesis is a separate obligation and is not
certified by this audit; no additional minimality conclusion is used
inside the displayed proof.

The companion one-mark decoder's small-tail lemma has no missing
singleton case.  If `|P|=1`, the four-clique
`Q subseteq P union B` has three vertices in the three-set `B`, so the
terminal-row decoder applies.  If `|P|=2`, either the same case applies or
`Q cap P={q,q'}` and `Q cap B={u_1,u_2}`.  Each of `q,q'` has the four
fixed neighbours consisting of the other packet vertex and
`z_i,u_1,u_2`.  Missing either outside mark would force both remaining
possible boundary neighbours, make its six-vertex neighbourhood a marked
six-cut omitting that mark, and contradict the standing cut law.  Fullness
at the third boundary vertex then supplies the advertised literal `K_7`
bags.  Thus invocation of the one-mark model below is safe; a tail of
order at most two would already close the cell in `H`.

## 2. Lifting the supported edge

The one-mark model has a literal edge from `R_a` to the omitted endpoint
`z_a`: it is the last edge of the path ending at `z_a`.  Under contraction
of `x_ay_a`, that edge comes from an edge to at least one of `x_a,y_a`.
Renaming the two ends if necessary therefore makes it an `R_a-x_a` edge.
The replacement bags

\[
 R'=R_a\cup\{x_a\},\qquad A'=P_a\cup\{y_a\}
\]

are connected: the first uses the lifted last edge and the second uses the
`y_a-P_a` contact from `S_a^a`.  They are adjacent through the literal
split edge `x_ay_a`.

The seven bags are disjoint.  Before expansion the one-mark model used
`z_a` only in `D_a=P_a union {z_a}` and omitted it from `R_a`.  Expansion
removes that contracted vertex and places its two distinct ends in the two
replacement bags.  The matching assumption prevents either end from
being an unchanged marked vertex, and the other five original bags were
already disjoint from `P_a,R_a,z_a` in the required combinations.

## 3. All twenty-one adjacencies

Write the seven lifted bags as

\[
 C_1,C_2,C_3,\quad R',\quad Z=\{z_h\},\quad
 A'=P_a\cup\{y_a\},\quad B'=P_b\cup\{z_b\}.
\]

The twenty-one unordered pairs are exhausted as follows.

| Pair type | Number | Literal witness |
|---|---:|---|
| `C_j-C_k` | 3 | the distinct roots in the clique `Q_h` |
| `C_j-R'` | 3 | the old `C_j-R_a` clique-root edge |
| `C_j-Z` | 3 | the old root--`z_h` edge in `L_h` |
| `C_j-A'` | 3 | `P_a` contacts the row vertex `x_{aj}` in `C_j` |
| `C_j-B'` | 3 | `P_b` contacts the row vertex `x_{bj}` in `C_j` |
| `R'-Z` | 1 | inherited from `R_a-Z` |
| `R'-A'` | 1 | the split edge `x_ay_a` |
| `R'-B'` | 1 | the `x_a-P_b` contact from `S_b^a` |
| `Z-A'` | 1 | the `z_h-P_a` row-fullness edge |
| `Z-B'` | 1 | the `z_h-P_b` row-fullness edge |
| `A'-B'` | 1 | the `z_b-P_a` row-fullness edge |

The first five rows contribute fifteen pairs and the last six rows are the
six pairs among `R',Z,A',B'`.  Hence no adjacency is omitted.  In
particular, `A'` retains every old duty of `D_a` using `P_a`; none depends
on the endpoint `x_a` moved into `R'`.

All witnesses are edges of `H_a`.  No virtual torso edge, quotient-only
contact, or contraction-created adjacency is used.  The bags therefore
form a literal `K_7` model in `H_a`, which lifts immediately to `G` because
`H_a` is a minor of `G`.

## 4. Scope

The audited implication is exactly

```text
balanced |W|=3 marked Mader cell
+ three disjoint split edges
+ seven-connected one-edge predecessors
=> literal K7 minor.
```

It does not show that an arbitrary six-connected marked quotient has such
predecessors, does not address the balanced `|W|=4,5` cells, and does not
by itself prove the global support-six rung or `HC_7`.
