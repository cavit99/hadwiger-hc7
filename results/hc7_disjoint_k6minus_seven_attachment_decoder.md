# Seven endpoint attachments in the exceptional `3+1` linkage

**Status:** written reduction with a deterministic finite certificate checker;
independently audited in
[`hc7_disjoint_k6minus_seven_attachment_decoder_audit.md`](hc7_disjoint_k6minus_seven_attachment_decoder_audit.md).
The theorem eliminates an infinite family of connected off-linkage
subgraphs, but it does not close the exceptional linkage configuration or
prove `HC_7`.

## 1. Normalized linkage

Let

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},\qquad
 B=\{b_0,b_1,b_2,r,p,q\}.
\]

Assume that `a0,a1,a2,a3` induce a clique, that

\[
 xy,\ xa_0,\ xa_1,\ xa_2,\ ya_3
\]

are edges, and that `B` induces `K6-pq`.  Let six pairwise
vertex-disjoint paths, internally disjoint from `A union B`, have ends

\[
 a_i b_i\ (0\le i\le2),\qquad a_3p,\qquad xq,\qquad yr.       \tag{1.1}
\]

Write `Sigma` for their union.  A connected subgraph outside `Sigma` means
a connected subgraph whose vertex set is disjoint from `V(Sigma)`.

## 2. Endpoint-attachment theorem

### Theorem 2.1

Let `D` be a connected subgraph outside `Sigma`.  If `D` has a neighbour at
each of `a3,x` and at least five further vertices of

\[
 (A\cup B)-\{a_3,x\},                                      \tag{2.1}
\]

then `G` contains a `K7` minor.

#### Proof

Contract `D` to one vertex `c`, and contract each path in (1.1) until its
two named ends are adjacent.  Delete every edge not specified in Section 1
or supplied by an attachment of `D`.  Choose any five of the further
endpoint contacts.  The resulting graph contains the thirteen-vertex graph
consisting of the normalized twelve-vertex quotient and a vertex `c`
adjacent to `a3,x` and the chosen five endpoints.

There are

\[
             \binom{10}{5}=252                              \tag{2.2}
\]

such minimal graphs.  The adjacent checker finds and directly verifies
seven pairwise adjacent, nonempty, connected, pairwise disjoint branch sets
in every one.  Thus every minimal graph has a `K7` minor.  Adding contacts
cannot destroy a minor model, so the same is true with more than five
further endpoint contacts.  Every operation used to obtain the quotient is
a minor operation, and the conclusion therefore lifts to `G`.  \(\square\)

The finite part of the proof has 72 orbits under the simultaneous
permutations of

\[
 (a_0,a_1,a_2)\quad\hbox{and}\quad(b_0,b_1,b_2).
\]

The checker searches all 252 labelled cases rather than relying on the
orbit reduction.

### Proposition 2.2 (sharp six-contact classification)

Suppose `c` is adjacent to `a3,x` and exactly four further normalized
endpoints.  Of the 210 possible attachment sets, precisely seven give a
`K7`-minor-free thirteen-vertex quotient.  Up to the simultaneous
permutations above, they have the following three forms:

\[
\begin{aligned}
 &\{a_3,x,a_0,a_1,a_2,y\};                              \tag{2.3}\
 &\{a_3,x,a_i,a_j,b_i,b_j\}, &&0\le i<j\le2;             \tag{2.4}\
 &\{a_3,x,y,r,b_i,b_j\},   &&0\le i<j\le2.              \tag{2.5}
\end{aligned}
\]

Every other six-contact quotient contains a `K7` minor.

#### Proof

The checker examines all 210 attachment sets by an exact connected-branch-set
search.  It verifies a model in 203 cases and returns no model precisely in
the seven displayed cases.  The same exhaustive search proves the negative
assertion: in a graph of order thirteen, a seven-branch model has at least
one singleton branch set.  The checker tries every possible exact singleton
clique and then every family of mutually adjacent, disjoint, connected
non-singleton branch sets.  Unused vertices are permitted, so the search is
complete for minor models rather than only spanning models.  \(\square\)

The third exceptional form is the endpoint obstruction already visible
when a connected subgraph meets `a3,x,y,r`.  Proposition 2.2 shows that it
is one of three, rather than an isolated accident.

## 3. Attachments in path interiors

### Corollary 3.1

Let `D` be a connected subgraph outside `Sigma`, adjacent to `a3` and `x`.
If `D` has an attachment in the interior of each of at least five distinct
paths from (1.1), then `G` contains a `K7` minor.

#### Proof

For the six paths in the order displayed in (1.1), designate respectively
the endpoints

\[
                    a_0,a_1,a_2,p,q,y.                    \tag{3.1}
\]

These six vertices are distinct and avoid `a3,x`.  For each of five paths
met by `D`, select one attachment and contract the subpath from that
attachment to its designated endpoint.  Contract the remainder of every
path until its two named ends are adjacent.  The image of `D` is now
adjacent to `a3,x` and five distinct further normalized endpoints.
Theorem 2.1 applies.  \(\square\)

The checker independently constructs the once-subdivided version of all
six paths and verifies each of the six projections obtained by retaining
five interior contacts.  This is a check of the contraction argument, not
a finite substitute for it.

The same proof permits a mixture of literal endpoint contacts and interior
contacts whenever five distinct further normalized endpoints can be
obtained by contracting pairwise internally disjoint terminal subpaths.
No claim is made when several attachments are concentrated on too few of
the six paths.

### Proposition 3.2 (one-subdivision mixed catalogue)

Subdivide each of the six paths in the endpoint quotient at most once, and
write `m_i` for the possible subdivision vertex of the path `P_i`.  Let `c`
be adjacent to `a3,x` and to five distinct sites selected from

\[
 \{a_0,a_1,a_2,y,b_0,b_1,b_2,r,p,q,m_0,\ldots,m_5\}.   \tag{3.2}
\]

There are 4368 such five-site sets.  Precisely 21 produce a `K7`-minor-free
finite quotient.  Up to simultaneous permutations of indices `0,1,2`,
they have the following four forms, where `i,j` are distinct members of
`{0,1,2}`:

\[
\begin{aligned}
 &\{a_i,a_j,b_i,b_j,m_i\};                              \tag{3.3}\
 &\{a_i,a_j,b_i,m_i,m_j\};                              \tag{3.4}\
 &\{a_i,b_i,b_j,m_i,m_j\};                              \tag{3.5}\
 &\{y,r,b_i,b_j,m_5\}.                                  \tag{3.6}
\end{aligned}
\]

There are respectively six, six, six, and three labelled instances of
these forms.  Every other five-site quotient contains a `K7` minor.

#### Proof

For each site set, first orient every selected `m_i` toward either endpoint
of `P_i`.  If some orientation gives seven distinct endpoint contacts, or
six contacts not listed in (2.3)--(2.5), contraction to that endpoint
quotient proves the minor.  This settles 4327 of the 4368 sets.

The checker constructs the actual once-subdivided graph for each of the 41
remaining sets.  It finds a `K7` minor in 20 and none in the 21 sets
(3.3)--(3.6).  The exact search repeatedly uses the following exhaustive
recurrence.  If a vertex `v` has degree below six, then in a `K7` model it
cannot be a singleton branch set.  Hence the model either avoids `v` or
contains an edge `vw` in its branch set for some neighbour `w`.  It is
therefore enough to test deletion of `v` and contraction of each incident
edge.  Every graph above order thirteen has a degree-three subdivision
vertex, so the recurrence reaches the complete order-thirteen search from
Proposition 2.2.  This proves both the positive and negative assertions.
\(\square\)

Proposition 3.2 is a finite one-subdivision theorem, not a statement about
arbitrarily many ordered attachments along a long path.  Its value is that
all finite negative patterns concentrate their interior attachments on at
most two of `P0,P1,P2`, or only on `P5`; neither `P3` nor `P4` occurs.

## 4. The distribution inside the connected subgraph is irrelevant

Theorem 2.1 depends only on the union of the endpoint neighbourhoods of the
vertices of `D`.  In particular, it applies when `D` is an edge `cd` and
the seven compulsory contacts are divided arbitrarily between `c` and `d`:
contracting `cd` produces exactly the one-vertex graph used in the proof.

As a guardrail, the checker enumerates all

\[
       \binom{10}{5}3^7=551124                             \tag{4.1}
\]

assignments in which each of the seven contacts belongs only to `c`, only
to `d`, or to both.  Every contraction gives the corresponding verified
seven-contact quotient.  The same contraction argument works for a
connected subgraph of arbitrary order; the two-vertex enumeration is not
being extrapolated to prove that fact.

## 5. Consequence and exact residue

After stable rerouting, every nontrivial component outside the six-path
system has at least seven distinct attachments to the path system.  Theorem
2.1 and Corollary 3.1 imply the following necessary condition for a
`K7`-minor-free host whenever such a component meets `a3,x`:

- it has at most four further contacts among the other ten normalized
  endpoints; and
- its interior attachments cannot occupy five distinct paths from (1.1).

If it has six normalized endpoint contacts in total, those contacts must
have one of the three forms (2.3)--(2.5).  Thus the unresolved geometry is
attachment concentration along at most four named paths, not arbitrary
seven-attachment saturation.  This conclusion does not yet supply a
bounded separator or a strictly decreasing replacement of the labelled
`K5` model.

## 6. Verification

Run from the repository root:

```sh
python3 results/hc7_disjoint_k6minus_seven_attachment_decoder.py
```

Expected output:

```text
minimal_seven_attachment_sets 252
minimal_seven_attachment_orbits 72
certificate_digest 2b2b5f5b30bed58f598a3f491ec434682d3845951235cf0d710ddffd1ad368cb
six_attachment_positive_sets 203
six_attachment_negative_sets 7
six_attachment_negative_orbits 3
five_of_six_interior_rail_projections 6
mixed_site_sets 4368
mixed_projection_resistant_sets 41
mixed_actual_negative_sets 21
mixed_actual_negative_orbits 4
mixed_status_digest 24c1fc7e8b81591d71c7d0dc701f867d0682f8bad19a9a60161fbf1df96195d7
two_vertex_contact_distributions 551124
GREEN: endpoint saturation and projection checks verified
```

The checker uses only the Python standard library.  It stores no generated
catalogue: the digest fixes the canonical list of all 252 positive
certificates, while every certificate is reconstructed and checked on each
run.  Proposition 2.2 is a computer-assisted finite result.  The contraction
reductions in Theorem 2.1 and Corollary 3.1 are written unbounded arguments.
