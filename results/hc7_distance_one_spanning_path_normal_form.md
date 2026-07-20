# Normal form when a distance-one obstruction path spans a shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_distance_one_spanning_path_normal_form_audit.md`](hc7_distance_one_spanning_path_normal_form_audit.md).

This note continues the distance-one path-splitting theorem at its atomic
endpoint: the chosen shortest two-colour obstruction path has all vertices
of one open shore in its interior.  Either the path splits into two
boundary-full connected subgraphs and gives an explicit `K_7` minor, or its
boundary attachments have one of the two standard interval obstructions:
a shared portal or two oppositely missing boundary vertices.

## 1. Setting

Retain the normalized live interface

\[
 V(G)=E\mathbin{\dot\cup}B\mathbin{\dot\cup}C,
 \qquad |B|=9,
 \qquad E_G(E,C)=\varnothing,
\]

where

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\},
 \qquad B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |W|=2,
\]

all displayed vertices are distinct, and `d x_d y_d d` and
`e x_e y_e e` are triangles.  Assume that `E` is full to `B`.  Retain also
the connected adjacent partition `C=Q_0 dotcup Q_1` from the
contact-concentration theorem: one of `Q_0,Q_1` is full to `B`, and the
other is full to `B-W=S-{e}`.  In particular both are adjacent to every
vertex of

\[
                         S-\{e\}.
\]

Assume `G` is seven-connected, is not six-colourable, and every proper
minor is six-colourable.

Let

\[
                     u p_1p_2\cdots p_r v             \tag{1.1}
\]

be a shortest first-hit obstruction path from one boundary two-colour
component to a different boundary two-colour component in the `E`-shore.
Assume

\[
                         E=\{p_1,\ldots,p_r\}.          \tag{1.2}
\]

For `s in B`, let `f(s)` and `ell(s)` be respectively the first and last
indices of a neighbour of `s` on the path.  They are defined because `E`
is full to `B`.

## 2. Prefix and suffix contacts

### Lemma 2.1

The graph `G[E]` is the induced path `p_1...p_r`.  If no connected
singleton-side response of order seven or eight has already been returned,
then every nonempty proper prefix and suffix of this path is adjacent to at
least eight of the nine vertices of `B`.

#### Proof

Every vertex of `E` lies on the two-colour path (1.1).  A nonconsecutive
edge `p_ip_j`, with `j>=i+2`, would be a chord of that path and would give a
shorter path between the same two boundary components.  Thus `G[E]` is the
displayed induced path.

For `1<=i<r`, put

\[
 E_i^- =\{p_1,\ldots,p_i\},
 \qquad
 E_i^+ =\{p_{i+1},\ldots,p_r\}.
\]

The full neighbourhood of `E_i^-` consists of its boundary neighbours and
the single vertex `p_{i+1}`.  It separates the prefix from the nonempty
opposite shore `C`.  If the prefix met at most seven boundary vertices,
its full neighbourhood would have order at most eight; seven-connectivity
and the standard crossing-edge colouring would give an order-seven or
order-eight response.  Hence it meets at least eight boundary vertices.
The suffix argument is symmetric. \(\square\)

## 3. A full--full split is terminal

### Theorem 3.1

If some `i` with `1<=i<r` makes both `E_i^-` and `E_i^+` full to `B`, then
`G` contains a `K_7` minor.

#### Proof

Use the four distinct boundary vertices

\[
                         x_e,y_e,x_0,y_0
\]

as anchors, and form

\[
 E_i^-\cup\{x_e\},\qquad
 E_i^+\cup\{y_e\},\qquad
 Q_0\cup\{x_0\},\qquad
 Q_1\cup\{y_0\}.                                    \tag{3.1}
\]

All four sets are connected and pairwise disjoint.  The first two are
adjacent through the path edge `p_ip_{i+1}`, and the last two are adjacent
by the connected partition of `C`.  Every cross pair is adjacent because
each path side is full to `B`, while both `Q_0,Q_1` are adjacent to all
four displayed anchors.

Each set in (3.1) is adjacent to every vertex of the boundary triangle

\[
                            d x_d y_d d.
\]

The path sides are boundary-full, and both `Q`-parts are full to
`S-{e}`.  Therefore the four sets in (3.1), together with

\[
                            \{d\},\quad\{x_d\},\quad\{y_d\},
\]

are seven pairwise adjacent connected branch sets. \(\square\)

## 4. Attachment-interval trichotomy

Put

\[
                      F_*=\max_{s\in B} f(s),
              \qquad L_*=\min_{s\in B} \ell(s),       \tag{4.1}
\]

and choose `a,b in B` with `f(a)=F_*` and `ell(b)=L_*`.

### Theorem 4.1

Outside the response exit of Lemma 2.1, exactly one of the following holds.

1. `F_*<L_*`.  Some internal edge of the path separates two connected
   subgraphs which are both full to `B`, and Theorem 3.1 gives a `K_7`
   minor.
2. `F_*=L_*`.  The vertex `p_{F_*}` is adjacent to both `a` and `b`.  This
   is the shared-portal outcome; `a` and `b` are allowed to coincide.
3. `F_*>L_*`.  The vertices `a,b` are distinct.  For every integer
   `i` with

   \[
                              L_*\le i<F_*,            \tag{4.2}
   \]

   the prefix `E_i^-` is full to `B-{a}` and misses `a`, while the suffix
   `E_i^+` is full to `B-{b}` and misses `b`.  Thus the two adjacent path
   parts have complementary one-vertex contact defects.

#### Proof

If `F_*<L_*`, choose `i` with `F_*<=i<L_*`.  Every boundary vertex has a
neighbour in the prefix because `f(s)<=F_*<=i`, and a neighbour in the
suffix because `ell(s)>=L_*>i`.  Outcome 1 and Theorem 3.1 follow.

If equality holds, the definitions give

\[
              f(a)=F_*=L_*=\ell(b),
\]

so `p_{F_*}` is adjacent to both selected boundary vertices.  This is
outcome 2.

Finally suppose `F_*>L_*` and choose `i` as in (4.2).  The prefix misses
`a`, because its last index is below `f(a)`.  Lemma 2.1 says it misses at
most one boundary vertex, so it is full to `B-{a}`.  Similarly the suffix
misses `b`, because every index on it exceeds `ell(b)`, and it is full to
`B-{b}`.  The vertices are distinct: if `a=b`, then
`f(a)<=ell(a)`, contrary to `F_*>L_*`. \(\square\)

## 5. Exact remaining issue

The distance-one shore-spanning outcome is therefore not an arbitrary
long path.  It is one of:

- a `K_7`-minor model;
- an order-seven or order-eight response;
- a single shared attachment vertex; or
- two adjacent connected path parts, each missing exactly one distinct
  boundary vertex, with the two omissions in reverse path order.

The last two alternatives are label-sensitive.  The older order-eight
shared-portal and strict-reversal theorems cannot be invoked verbatim: the
present boundary has order nine, and one of `Q_0,Q_1` misses the two
vertices of `W`.  Closing them requires either assigning the two omitted
vertices and the two `W`-contacts to the four anchored branch sets, or
returning a smaller full-neighbourhood response.
