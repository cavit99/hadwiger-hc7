# Crossed frames forbid the proposed terminal-free disk page

**Status:** exact structural barrier.  This does not contradict the
conditional bilateral colouring theorem; it shows that its disk-page
hypothesis cannot be reached from a supported crossed frame without first
changing or consuming one of the two frame carriers.

## 1. The literal obstruction

In the pure-Moser exact cell put

\[
 U=\{0,2,4,5,6\}.
\]

The present edges on `U` form the cycle

\[
                 C=0\,2\,6\,5\,4\,0,                 \tag{1.1}
\]

while the missing edges form the cycle

\[
                 0\,5\,2\,4\,6\,0.                  \tag{1.2}
\]

### Lemma 1.1 (crossed-frame disk obstruction)

Let `e,f` be two vertex-disjoint edges of the missing-edge cycle (1.2).
Suppose `E,F` are disjoint connected subgraphs with exact traces

\[
                         E\cap U=e,\qquad F\cap U=f.             \tag{1.3}
\]

Then `G[U\cup E\cup F]` has no embedding in a closed disk whose boundary
meets the graph exactly in the literal cycle `C`.

Moreover, `C\cup E\cup F` contains a subdivision of `K_4` rooted at the
four ends of `e\cup f`.

#### Proof

Choose an end-to-end path `P_e` in `E` and an end-to-end path `P_f` in
`F`.  Exactness of the traces puts every internal vertex of these paths
outside `U`, and disjointness of the two blocks makes the paths disjoint.

Two disjoint edges of the five-cycle (1.2) have alternating ends in the
cyclic order (1.1).  For example, `e=05` and `f=24` occur as

\[
                         0,2,5,4
\]

after deleting the unused vertex `6` from (1.1).  The other choices follow
by the dihedral symmetry of the two complementary five-cycles.

In a disk, one of the two arcs of `P_e` together with a boundary arc of
`C` is a Jordan curve separating the two ends of `P_f`.  Thus a disjoint
`P_f` cannot be drawn in the same disk.  This proves the first assertion.

The four arcs of `C` between successive selected ends, together with
`P_e` and `P_f`, are the six internally disjoint edge-paths of a
subdivision of `K_4`.  Its four branch vertices are the literal ends of
`e\cup f`.  \(\square\)

### Corollary 1.2 (the current rural endgame cannot occur)

Every supported crossed-frame core in a terminal-free shore already
contains the two blocks `E,F` of Lemma 1.1.  Consequently that whole shore
cannot have the `U`-boundary disk embedding required by the current
terminal-free bilateral planar endgame.

This conclusion precedes induced-pole expansion: even perfectly rural
induced poles cannot remove the two alternating frame paths already
present in disjoint core blocks.

## 2. Smallest certificate: rooted `K_4` is not a `K_7` conversion

Let `H_0` have vertex set

\[
                         U\cup\{p,q\}
\]

and edges

\[
 E(C)\cup\{0p,p5,2q,q4\}.                           \tag{2.1}
\]

Thus

\[
 E=H_0[\{0,p,5\}],\qquad
 F=H_0[\{2,q,4\}],\qquad
 R=H_0[\{6\}]
\]

are disjoint connected pairwise adjacent frame blocks with traces
`05`, `24`, and `{6}`.  The graph has the exact rooted-`K_4`
subdivision from Lemma 1.1 and no `U`-boundary disk embedding.

Nevertheless it has no `K_7` minor.  It has exactly seven vertices and is
not `K_7`; a minor with seven nonempty branch sets would have to use seven
singleton branch sets and hence would require every missing host edge.

To see that no new decoration duty follows from this topology, add vertices
`ell,w` and edges `well,ellp`.  Put `W={w,ell}`.  Relative to the displayed
frame, `W` contacts exactly the block `E`, and `{w,0,5}` is independent.
Thus `w->E` is supported while neither `w->F` nor `w->R` is even a raw
contact.  The resulting nine-vertex graph still has only eleven edges, so
it cannot have a `K_7` minor (a `K_7` minor requires at least the 21
distinct inter-branch edges already in the host).

This certificate is not seven-connected or contraction-critical.  Its
role is exact: the crossed-frame/rooted-`K_4` object alone implies neither
a literal `K_7` nor promotion to a second attained duty.  Any positive
conversion must spend the critical transition or the remaining labelled
portal structure.

## 3. A spanning rural-quotient certificate

The obstruction persists after imposing the local hypotheses of the
terminal-free rural outcome: a three-connected carrier, two anticomplete
connected poles, disjoint portal sets of orders three and five, an exact
five-attachment locked singleton, a supported decoration, and a planar
quotient spanning the selected side.

Let `K` be the wheel with hub `h` and rim

\[
       0,q_1,q_2,q_3,5,p_1,p_2,p_3,p_4,p_5,0.                  \tag{3.1}
\]

Put

\[
 X=\{2,m,4,6\},\qquad Y=\{\ell\},                              \tag{3.2}
\]

and add the following edges beyond the wheel:

\[
\begin{split}
 &02,26,65,54,40,\quad 2m,m4,\\
 &q_1 2,q_2 m,q_3 4,q_2 6,\quad
 \ell p_i\ (1\le i\le5),\quad w\ell,t\ell .                 \tag{3.3}
\end{split}
\]

Then:

* `K` is three-connected and has trace `{0,5}`;
* `A=H[{2,m,4}]` and `B={6}` are connected and adjacent, and the
  traces of `K,A,B` partition `U` as `05|24|6`;
* `X=A union B` and `Y` are connected and anticomplete;
* the open-shore set `V(H)-(U union {w,t})` is connected and has literal
  neighbourhood exactly `U union {w,t}`;
* the nonroot portal sets are exactly

  \[
       Q(K,X)=\{q_1,q_2,q_3\},\qquad
       P(K,Y)=\{p_1,p_2,p_3,p_4,p_5\};                        \tag{3.4}
  \]

* `W={w,ell}` supports the decoration `w->K` and contacts neither
  named target block; moreover `N(Y)=P(K,Y) union {w,t}` is the exact
  seven-vertex neighbourhood of the locked singleton; and
* contracting `X,Y` gives a planar whole-side quotient.  Draw the wheel
  hub inside its rim, the image of `X` outside the
  `0 q_1 q_2 q_3 5` arc, and the image of `Y` outside the complementary
  arc.  The vertices `w,t` are omitted in the terminal-free quotient.

Nevertheless the uncontracted graph has no `U`-boundary disk embedding:
the paths in `K` from `0` to `5` and `2-a-4` in `A` join alternating
pairs.  It also has no `K_7` minor.  The verifier beside this note contains
a tree decomposition of width five, and treewidth is minor-monotone while
`tw(K_7)=6`.

Thus even the full **local** rural-quotient package does not turn the
forced crossing into `K_7` or a new attained duty.  What this example omits
is precisely the global seven-connectivity/contraction-critical transition;
those hypotheses, rather than pole rurality, must drive the remaining
conversion.

## 4. Consequence for the proof spine

The rural alternative cannot end by expanding both poles and gluing two
one-disk shores along `U`.  A valid replacement must first do one of the
following label-faithfully:

1. consume or rotate one of the two alternating frame carriers into a
   common attained boundary state;
2. complete the rooted `K_4` by three disjoint, pairwise adjacent labelled
   duty carriers, each adjacent to all four rooted branch sets, giving a
   literal `K_7`; or
3. produce a coherent multi-page/annular decomposition together with an
   independently proved six-colouring splice.

Merely proving that each contracted pole society is rural is insufficient,
because the obstruction lies in the two disjoint core carriers rather than
inside either pole.
