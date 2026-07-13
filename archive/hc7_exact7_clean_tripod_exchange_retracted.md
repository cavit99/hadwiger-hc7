# RETRACTED — Exact-seven clean two-tripod exchange

This note is retained only as provenance.  Its hypotheses make each selected
arm separable in the thin shore by two vertices, contradicting the standing
three-connectivity assumption; moreover (2.2) ignores exits through unused
components.  It is not an active or proved exchange theorem.  See the
companion RED audit.

## 1. Statement

Retain the exact-seven `(1,3)` setup:

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `G` is seven-connected, there are no `LR` edges, and `R` contains
three pairwise disjoint connected `S`-full packets.  Let
`T={t_1,t_2,t_3}` be an edgeless three-cut of the three-connected shore
`L`, with exactly two lobes `C,D`.

The sparse-gate median theorem leaves rooted-triangle-free connectors in
this cell.  A standard rooted-`K_3` obstruction is a tripod: one cutvertex
separates the three rooted arms.  The theorem below closes the entire
aligned clean two-tripod family.

### Theorem 1.1 (clean two-tripod exchange)

Suppose there are vertices `z_C in C`, `z_D in D` and components

\[
 C_i\text{ of }C-z_C,\qquad D_i\text{ of }D-z_D
 \quad(1\le i\le3)
\]

such that:

1. `z_C` has a neighbour in every `C_i`, and `z_D` has a neighbour in
   every `D_i`;
2. `C_i` and `D_i` each have a neighbour at `t_i`; and
3. neither `C_i` nor `D_i` has a neighbour at `T-{t_i}`.

Then `G` contains a literal `K_7` minor.

The hypotheses allow arbitrary additional components of `C-z_C` and
`D-z_D`; they are simply unused.  Thus this is a clean-sector theorem,
not an assertion that the two tripods span their lobes.

## 2. Three large literal sectors

For `i=1,2,3`, put

\[
                       H_i=C_i\cup\{t_i\}\cup D_i.       \tag{2.1}
\]

The sets `H_i` are pairwise disjoint and connected.  They have no edges
between them: different `C_i` (and different `D_i`) are components after
deleting their centre, the two lobes are anticomplete, and `T` is
edgeless; condition 3 excludes crossed lobe-to-gate edges.

Moreover

\[
                      N_L(H_i)\subseteq\{z_C,z_D\}.       \tag{2.2}
\]

Indeed every exit from `C_i` inside `C` uses `z_C`, every exit from
`D_i` inside `D` uses `z_D`, and condition 3 lists the only gate vertex
met by either component.  Therefore

\[
                 N_G(H_i)\subseteq\{z_C,z_D\}\cup N_S(H_i).
                                                                  \tag{2.3}
\]

Deleting the right side of (2.3) separates the nonempty set `H_i` from
the opposite open shore.  Seven-connectivity gives

\[
                         |N_S(H_i)|\ge5.                 \tag{2.4}
\]

Since three subsets of a seven-set, each with complement of order at
most two, have nonempty common intersection,

\[
              N_S(H_1)\cap N_S(H_2)\cap N_S(H_3)\neq\varnothing.
                                                                  \tag{2.5}
\]

Fix a common literal label `q`.

## 3. Four labelled clique carriers

Define

\[
 B_1=H_1\cup\{z_C\},\qquad
 B_2=H_2\cup\{z_D\},\qquad
 B_3=H_3.                                             \tag{3.1}
\]

These three sets are disjoint and connected.  They are pairwise
adjacent:

* `z_C` has a neighbour in `C_2 subseteq B_2` and in
  `C_3 subseteq B_3`; and
* `z_D` has a neighbour in `D_1 subseteq B_1` and in
  `D_3 subseteq B_3`.

Every `B_i` is adjacent to the singleton bag `{q}` by (2.5).  Thus

\[
                         B_1,B_2,B_3,\{q\}              \tag{3.2}
\]

are four literal clique carriers before the remaining anchors are added.

For each `i`, the set `N_S(H_i)-{q}` has order at least four.  Three
sets of order at least four in a seven-set have an SDR, so choose distinct

\[
 s_i\in N_S(H_i)-\{q\}\quad(1\le i\le3).               \tag{3.3}
\]

Enlarge `B_i` by `s_i`.  The four bags in (3.2) remain disjoint,
connected and pairwise adjacent.  Anchor the three disjoint full packets
in `R` at the three remaining vertices of
`S-{q,s_1,s_2,s_3}`.  Packet fullness gives every packet--packet and
packet--carrier adjacency.  These seven literal bags form a `K_7` minor,
proving Theorem 1.1. `square`

## 4. Exact use

The theorem converts the clean negative certificate of a pair of rooted
three-arm linkages into the positive clique model.  Therefore an edgeless
two-lobe survivor cannot have aligned clean tripod centres on both sides.
At least one of the following must occur:

1. a rooted-triangle or boundary-edge repair already covered by the
   sparse-gate median theorem;
2. a crossed sector meets the wrong gate vertex;
3. the rooted-`K_3` obstruction uses a terminal arm itself rather than an
   external tripod centre; or
4. the two tripod decompositions cannot be aligned by the same gate
   labels.

The next exchange must use a crossed sector as a carrier, or turn the
terminal-centred/nonaligned obstruction into the matching proper-minor
state.  The theorem makes no bounded-transversal claim from packet number
one.
