# Two opposite Kempe failures do not pair into a decoration exchange

**Status:** exact component-swap lemma proved; explicit static
counterexample to the proposed pairing step.  The counterexample does not
satisfy seven-connectivity or contraction-criticality, so a positive HC7
theorem must spend one of those hypotheses after producing the paths.

## 1. Exact component-swap statement

### Lemma 1.1 (fixed-`U` component swap)

Let `J` have a proper colouring `c`, let `S=U dotcup {w}`, and let
`alpha=c(w)`.  Let `beta` be the colour of one equality block `B subseteq U`,
and assume that `w` is nonadjacent to every member of `B`.  Let `C` be the
component containing `w` in the subgraph induced by colours
`{alpha,beta}`.  Then exactly one of the following operations is returned:

1. `C cap U=empty`, and swapping `alpha,beta` on `C` fixes every vertex
   of `U` and recolours `w` to `beta`; or
2. `C cap U` is nonempty, and `J` contains a literal `w-U` path using
   only colours `alpha,beta`, with all internal vertices outside `S`.

#### Proof

If `C cap U=empty`, an ordinary Kempe swap on `C` preserves properness,
fixes `U`, and changes the colour of `w` from `alpha` to `beta`.

Otherwise choose a shortest path in `C` from `w` to `U`.  By the choice of
its first `U` vertex, every internal vertex lies outside `S`; all its
vertices have one of the two displayed colours.  \(\square\)

The endpoint in outcome 2 need not belong to `B`.  It may be any member of
`U` carrying either `alpha` or `beta`.  The path need not avoid any
supported frame block.

## 2. Literal opposite-decoration certificate

Use the pure-Moser five-set

\[
 U=\{0,2,4,5,6\},\qquad
 E(G[U])=\{02,26,65,54,40\}.                                  \tag{2.1}
\]

Fix the frame

\[
                         E=05,\qquad F=24,qquad R=\{6\}.       \tag{2.2}
\]

The two closed shores meet exactly in `S=U union {w}` and have no edge
between their open parts.

On the left add vertices `e_L,f_L,l` and edges

\[
                  0e_L,e_L5,\quad 2f_L,f_L4,
                  \quad wl,le_L.                              \tag{2.3}
\]

The connected sets

\[
 E_L=\{0,e_L,5\},\quad F_L=\{2,f_L,4\},\quad R_L=\{6\},
 \quad W_L=\{w,l\}                                             \tag{2.4}
\]

form a supported frame with exactly the decoration `w->E`: the three
core blocks are pairwise adjacent through the literal cycle (2.1),
`W_L` contacts `E_L`, and it contacts neither `F_L` nor `R_L`.

On the right add vertices `e_R,f_R,r` and edges

\[
                  0e_R,e_R5,\quad 2f_R,f_R4,
                  \quad wr,rf_R.                              \tag{2.5}
\]

The analogous core has exactly the decoration `w->F`.

Define a proper colouring `c_L` of the left closed shore by

\[
\begin{array}{c|c}
1&0,5,l,f_L\\
2&2,4,w,e_L\\
3&6,
\end{array}                                                    \tag{2.6}
\]

and a proper colouring `c_R` of the right closed shore by

\[
\begin{array}{c|c}
1&0,5,w,f_R\\
2&2,4,r,e_R\\
3&6.
\end{array}                                                    \tag{2.7}
\]

Unused colours may be added to regard these as six-colourings.  On `S`,
`c_L` induces `Pi_F` and `c_R` induces `Pi_E`, exactly as in the proposed
two-shore mechanism.

In `c_L`, attempting to move `w` from the `F` colour to the `E` colour
fails because its two-colour component contains the literal path

\[
                         w-l-e_L-0.                             \tag{2.8}
\]

In `c_R`, the reverse attempt fails along

\[
                         w-r-f_R-2.                             \tag{2.9}
\]

Both are exact paths returned by Lemma 1.1.  Each path runs through the
core block which already supports that shore's geometric decoration.
Absorbing the path into the `w`-region would overlap that core; it creates
no contact with the other named block.  At the displayed fixed cores,
the left attainable geometric duty remains only `E` and the right duty
remains only `F`.

The whole graph has 12 vertices and 17 edges, hence no `K_7` minor: seven
disjoint branch sets realizing `K_7` require 21 distinct host edges between
the 21 branch-set pairs.  There is also no `Q-P` carrier structure in the
two failure paths; their only labelled information is their boundary
colour endpoint.

## 3. Exact obstruction to the pairing argument

From the two failed swaps one may conclude only

\[
 \begin{array}{c}
 P_L:w\leadsto E\cup F\text{ in the left }E/F\text{-colours},\\
 P_R:w\leadsto E\cup F\text{ in the right }E/F\text{-colours}.
 \end{array}                                                    \tag{3.1}
\]

The endpoints may be in the already supported blocks, as in (2.8)--(2.9),
and the interiors may use those blocks.  Since palette colours are not
branch-set labels away from `U`, pairing `P_L,P_R` does not itself yield:

* a path avoiding the protected cores;
* a connected transferable carrier piece;
* a literal `Q-P` path;
* promotion to the opposite decoration; or
* seven pairwise adjacent branch sets.

A valid positive theorem needs at least one additional output, for example:

1. one failure path reaches the **opposite** named root block before
   meeting the already decorated core and is internally disjoint from the
   other two core blocks;
2. a first-hit segment has actual endpoints in the named portal sets
   `Q,P` and leaves a connected retained pair carrier; or
3. minor-criticality supplies a second colouring in which the obstructing
   component is forced to change owner, yielding a genuine state
   transition rather than the same static supported contact.

Without such labelled avoidance/transition data, the paired-failure step
is false.
