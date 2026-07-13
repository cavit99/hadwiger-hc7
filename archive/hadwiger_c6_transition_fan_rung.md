# Fan refinement at an (L)-(M)-(R) transition

## 1. Why endpoint side is not first-neighbour side

Use the notation of `hadwiger_c6_rope_defect_transition.md` at an
(L	o M) transition:

[
 D=Adotcup{u}dotcup B,qquad
 d_A={c_5,c_1},qquad d_B={c_0,c_2}.
]

The transition lock gives

[
 c_2in N_W(u),qquad
 N_W(u)subseteq{c_2,c_4}.                        	ag{1.1}
]

Seven-connectivity gives a seven-fan from (u) to
(S={c_0,ldots,c_5,z}), and direct arms may be shortened to edges.
The arm ending at (c_0) has its last portal in (A); arms ending at
(c_1,c_5) have their last portals in (B).  It is not valid to infer
that their first neighbours of (u) lie on those sides.  An arm may
start in (A), cross an (A)-(B) edge, and end in (B), or vice
versa.

## 2. The correct local Menger alternative

Adjoin two independent artificial terminals (t_1,t_5) to (B+u),
with neighbourhoods (P_1) and (P_5).  A **side-respecting
two-fan** is a pair of internally disjoint paths from (u) to
(t_1,t_5) in this graph.

### Lemma 2.1

Either the side-respecting two-fan exists, or there is a vertex
(xin B) such that every (B)-internal route from (u) to
(P_1cup P_5) uses (x).

### Proof

Give every vertex except (u) capacity one, join (t_1,t_5) to a
new sink through capacity-one edges, and apply the integral form of
Menger's theorem.  A flow of value two uses both artificial terminals
and is the desired fan.  If the maximum has value one, a one-vertex
separator exists.  It cannot be (t_1) or (t_5), since (B) is
connected, (u) has a (B)-neighbour, and both portal sets are
nonempty; deleting either artificial terminal leaves a route to the
other.  Hence the separator is a vertex (xin B). (square)

Let (C) be a component of (B-x) containing a (P_1)- or
(P_5)-portal on the far side of this separator.  It contains no
(B)-neighbour of (u).  Therefore

[
 N_G(C)subseteq
 {x}cup N_A(C)cup N_S(C),qquad
 N_S(C)subseteq{c_1,c_3,c_4,c_5,z}.             	ag{2.1}
]

Seven-connectivity gives the exact inequality

[
 |N_A(C)|+|N_S(C)|ge6.                            	ag{2.2}
]

Thus failure of the side-respecting fan does not automatically give a
cut of order at most six.  There are two further outcomes:

1. a large (A)-interface, which supplies several distinct crossing
   entries into the terminal piece; or
2. equality in (2.2).  In the extremal contact case this is the exact
   seven-adhesion cell

   [
   N_G(C)={x,a,c_1,c_3,c_4,c_5,z}                	ag{2.3}
   ]

   for one (ain A).

The (M	o R) statement is obtained by reflection: its local
(A)-fan targets (c_0,c_2), and its exact cell has the reflected
five-label boundary row.

## 3. Interaction with the global seven-fan

In the separator outcome, the global seven-fan still has disjoint arms
to (c_1,c_5).  At most one can enter their far-side portal region
through (x).  Every other such arm has a last (A)-to-(C) crossing.
Consequently the cell carries two distinct labelled entries, one through
(x) and one through (A), or two distinct (A)-entries.  These are
the pieces that a valid quotient must retain; replacing them by an
unlabelled split of (A) loses the information.

This proves the sound trichotomy

[
egin{array}{c}
	ext{side-respecting labelled fan},\
	ext{large cross-interface},\
	ext{exact seven-adhesion labelled rung}.
end{array}                                         	ag{3.1}
]

A two-outcome statement with “fan or a cut of order at most six” is
false at the level of the established hypotheses: (2.3) is compatible
with seven-connectivity and is exactly the full-adhesion rung already
produced by the Yu obstruction theorem.

## 4. Quotient sanity checks

Two computations delimit what contact-only arguments can prove.

* `c6_transition_fan_quotient.cpp` retains four disjoint fan arms as
  separate labelled helpers.  The resulting star quotients remain
  (K_7)-minor-free for all three transition types; fan existence alone
  is insufficient.
* `c6_rope_split_transition_quotient.cpp` splits a multiply hit side
  into two adjacent (u)-neighbour pieces and enumerates every
  distribution of its five aggregate boundary contacts.  It leaves 63,
  39, and 33 negative distributions for (L	o M), (M	o R), and a
  direct (L	o R) jump respectively.

The next positive quotient must combine the *labels* of the fan arms
with the *two entries* of (3.1).  Neither datum by itself suffices.

## 5. The exact cell with one bottleneck entry closes

Suppose the two fan arms to (c_1,c_5) enter the exact cell with one
entry through (x) and the other through (A).  Inside the connected
cell, take the two disjoint terminal pieces supplied by the fan and
partition a spanning tree between them into adjacent connected sets
(R_1,R_5), with

[
 R_1	ext{ touching }c_1,qquad
 R_5	ext{ touching }c_5,qquad
 xR_1, AR_5, R_1R_5.                              	ag{5.1}
]

All remaining contacts (c_3,c_4,z) of the cell distribute arbitrarily
between (R_1,R_5).  Contract the opposite shore to a full helper (H)
and the left side to (A).  The following seven bags form a (K_7)
model, independently of that distribution:

[
{c_0,c_3},quad
{c_1,u,x,R_1},quad
{c_2},quad
{c_4,H},quad
{c_5},quad
{z},quad
{A,R_5}.                                          	ag{5.2}
]

Connectivity uses (ux,xR_1,c_1R_1) in the second bag and (AR_5)
in the last.  Pairwise adjacency is a direct complement-cycle check;
notably the second and last bags meet through (uA).  Hence this entire
seven-adhesion outcome is impossible.

`c6_transition_fan_quotient.cpp` independently enumerates all
20,912,320 branch partitions for each of the (3^3=27) distributions
of (c_3,c_4,z), and finds all 27 positive.

## 6. Both entries through (A): exact remaining portal lock

If both arms bypass (x), contracting their two prefixes to one
connected (A)-helper loses essential order information.  The coarse
quotient is negative in exactly nine of the 27 cell distributions:

[
 c_4	ext{ belongs only to the }c_1	ext{-side piece }R_1.           	ag{6.1}
]

Retaining two disjoint prefixes and a connected residual (A)-core
closes every distribution when the core retains the full aggregate
(A)-row.  It is still not universal under arbitrary portal placement.
An explicit surviving minimal pattern puts every aggregate (A)-contact

[
 {c_0,c_2,c_3,c_4,z}
]

and every unassigned cell contact ({c_3,c_4,z}) on (R_1), while
(R_5) touches only (c_5) and the residual core has no boundary
contact.  In that quotient, adding a (c_0)- or (c_4)-contact from
the residual core or (R_5) immediately gives a (K_7)-model.

Thus the fan analysis eliminates the exact rung unless both labelled
arms bypass the bottleneck and the two repair labels (c_0,c_4) remain
concentrated on the (c_1)-side.  This is a genuine ordered portal
lock, not another unlabelled contact deficit.  The next hand lemma must
either reroute one arm through (x), distribute (c_0) or (c_4), or
turn their simultaneous concentration into a smaller separator.
