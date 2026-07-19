# Independent internal audit of the endpoint-`K_4` transfer theorem

**Verdict:** GREEN for the exact source revision

```text
results/hc7_endpoint_k4_transfer_or_order7.md
SHA-256 da446cbcacde393aa24bb8f0a3bdce86527e392c2065dfd170fe8bb6f800e81d
```

This is a separate internal mathematical audit, not external peer review.
The audit checked the imported three-owner concentration hypotheses, every
branch-set modification, the separator count, preservation of the literal
response data, and the relaxed first-hit-rank argument.

## 1. Imported structure

The cited concentration theorem supplies the disjoint decomposition

\[
                     U=U_0\mathbin{\dot\cup}C,
\]

where `U_0` is connected, contains the prescribed root of `U`, and is
adjacent to `C`.  All three owner portal sets lie in `C`.  The six branch
sets other than `U` contribute exactly one vertex each to the outside
neighbourhood of `C`, while the two selected contact edges have distinct
ends `a,b` in `C` and distinct owner labels.  Under the endpoint-`K_4`
hypothesis all six edges among `a,b,r_i,r_j` are present; in particular the
proof may use `ab`, `ar_i`, `ar_j`, `br_i`, and `br_j` exactly as stated.

## 2. The separated-component branch

Let `Q` be the component of `G[U-a]` containing `U_0`.  If `b` is not in
`Q`, the component `B` containing `b` is contained in `C`, because all of
`U_0` lies in `Q`.  Since `B` is a component after deleting `a`, its only
possible neighbour in `U` is `a`; the edge `ab` shows that `a` is indeed a
neighbour.  Every neighbour of `B` outside `U` is a neighbour of `C`, so

\[
 N_G(B)\subseteq
 \{a,s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.
\]

The nonempty component `Q` avoids both `B` and its full neighbourhood.
Thus `N_G(B)` is an actual vertex cut, not merely a quotient boundary.
Seven-connectivity gives the lower bound seven, while the displayed set
gives the upper bound seven.  Equality forces every displayed vertex to
occur and proves the exact order-seven boundary asserted by the theorem.

## 3. The branch-set transfer

Suppose `b` lies in `Q` and put `L=U-Q`.  The set `L` consists of `a`
together with every other component of `G[U-a]`.  Each such component has a
neighbour at `a`, since `G[U]` is connected, so `L` is connected.  It is a
nonempty subset of `C`, contains `a`, omits `b`, and is adjacent to the
connected retained donor `Q` through `ab`.

The two portal cases are exhaustive.

- If the third owner retains a portal in `Q`, absorbing `L` into `R_i`
  gives a connected branch set through `ar_i`.  The donor retains its
  contacts with `R_i` and `R_j` through `br_i` and `br_j`, and with the
  third owner through its retained portal.
- If the third owner has no portal in `Q`, all of its nonempty portal set
  lies in `L`.  Absorbing `L` into that owner gives a connected branch set,
  and `ab` supplies its contact with the retained donor.  The edges `br_i`
  and `br_j` again retain the other two owner contacts.

Every nonowner keeps its old edge to `U'\subseteq U_0\subseteq Q`, and `D`
keeps the fixed response edge to `U'`.  Enlarging one recipient destroys no
old adjacency.  The modified sets are connected, pairwise disjoint and
still span `G`.  Therefore either the missing `X-Y` adjacency is present,
giving the explicit `K_7`-minor model, or the only possible missing pair is
still `X,Y`.

## 4. Roots, response data and first-hit rank

The prescribed donor root remains in `U_0\subseteq Q`; the other branch
sets only stay fixed or enlarge.  The fixed connected response subgraph
remains inside `D`, and the selected boundary partition is a literal object
of the unchanged host graph.

The relaxed first-hit rank does not decrease.  A ranked path whose terminal
label is not `U` avoided the whole old donor and hence avoids `L`.  If the
ranked `U`-path ends in `L`, retain its designated source port, travel inside
the fixed connected response subgraph, and use the fixed response edge into
`U'\subseteq Q`.  Overlap inside the response subgraph is allowed, while
outside it the replacement contains only its new terminal.  Other ranked
paths avoided old `U`, so outside-response disjointness and literal
first-hit ownership are preserved.

Since `L` is nonempty, `Q` is a proper subset of `U`.  Maximum relaxed
first-hit rank followed by minimum donor order therefore excludes this
nonterminal transfer.  In a `K_7`-minor-free host the explicit-minor outcome
is also excluded, leaving the order-seven separation.

## 5. Trust boundary

The theorem is conditional on the complete three-owner concentration
setting and on the four endpoints of two differently labelled owner-contact
edges inducing a `K_4`.  It does not show that this endpoint clique must
exist.

The returned order-seven separation is literal and exact, but the theorem
does **not** produce six-colourings of both closed shores with the same
boundary equality partition.  It supplies no common shore trace, no
colour-gluing conclusion, and no proof of `HC_7`.  Those omissions are
stated correctly in the source.
