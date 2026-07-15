# Audit of the overlap-four exterior-connectivity closure

## Verdict

**GREEN.**  The four-connected exterior theorem, its exact-seven separator
corollary, and its strongly contraction-critical packet normalization are
correct under the eleven stated **irredundant** support-six hypotheses.
The strength of the published rooted-`K_4` theorem, the common-face
propagation, the peripheral facial-cycle step, the construction of the five
rooted cycle bags, the crossed-gate repair, and both packet dependencies
all match the hypotheses of their cited results.

The most delicate point is the last one.  Enlarging the bag rooted at `6`
by the connected facial-cycle remainder gives an actual adjacency for a
fixed gate defect.  The cycle decoder's one-gate repair is tested in the
final quotient edge layer and its general branch-set lift remains valid
with this enlarged bag.  Thus the proof does not confuse a virtual
terminal edge with a literal edge of `G`.

The first corollary is an **unranked handoff** only.  Under strong
contraction-criticality, the second corollary determines the possible
packet vectors but still does not preserve a colouring state, identify the
thin side with a pre-existing named shore, or establish a strict recursive
descent.

## 1. Hypotheses and normalization

The closure uses exactly the normalization of both audited decoders:

```text
A={0,1,2,3,4,5}, I={0,1,2,3}, X=I union {6},
p=7, q=8, T={4,5,6,7,8}.
```

Its eleven support assumptions are exactly

```text
A, X+p, X+q,
(A-i)+p, (A-i)+q for i in I.
```

In particular, it retains the decoders' essential irredundancy condition:
none of the six five-subsets of any displayed support is a literal `K_5`.
No conclusion of this audit applies if the word *irredundant* is dropped.

Putting `H=G-I` loses four vertices.  If `H-Z` were disconnected for
`|Z|<=2`, then

```text
G-(I union Z)=H-Z
```

would be disconnected after deleting at most six vertices.  This
contradicts seven-connectivity.  Since `H` contains the five distinct
vertices of `T`, the usual order convention for connectivity causes no
exception.  Hence `H` is three-connected, exactly as claimed.

## 2. Published rooted-`K_4` input

The cited result is Theorem 6 of Fabila-Monroy and Wood,
[*Rooted `K_4`-Minors*](https://doi.org/10.37236/3476).  It states that for
four distinct nominated vertices in a four-connected graph, either they
root a `K_4` minor, or the graph is planar and the four vertices lie on a
common face.  This is precisely the dichotomy used here; the proof does
not invoke the stronger statement for an arbitrary three-connected
nonplanar graph.

Apply the theorem to each `T-{t}`.  If one set roots a `K_4`, the audited
rooted-`K_4` decoder applies because the model lies in `H=G-I`.  Its direct
outcome is already a literal `K_7`.  Its common-model outcome is a
support-at-most-five `K_4` in some `A-{i}`, contacted by the three distinct
vertices `i,p,q`; it meets every hypothesis of the independently audited
three-rooted small-`K_4` composition theorem.

The rooted decoder explicitly allows its four exterior bags to contain
the omitted fifth terminal.  Thus no unstated fifth-terminal avoidance is
needed at this step.

If no four-subset roots a `K_4`, Theorem 6 first makes `H` planar and then
makes every four-subset of `T` cofacial.  Because `H` is three-connected,
its plane embedding is polyhedral and unique up to reflection.  In such an
embedding two distinct facial cycles meet in at most one edge, and in
particular share at most two vertices.  A face containing

```text
T-{6}={4,5,p,q}
```

and a face containing

```text
T-{4}={5,6,p,q}
```

share the three distinct vertices `5,p,q`; hence they are the same face.
Their union contains every member of `T`, so all five terminals lie on one
face.  Only these two four-subsets are needed for this propagation, though
the theorem legitimately supplies all five.

## 3. Peripheral face and rooted cycle bags

For a three-connected plane graph, facial cycles are peripheral: their
boundary is an induced cycle and deleting its vertices leaves a connected
graph, possibly empty.  This is the standard planar form of the
peripheral-cycle theorem.  It applies to the common face boundary `C`.

Here the remainder cannot be empty.  Four-connectivity and the presence of
five distinct terminals give `delta(H)>=4`.  Since `C` is induced, each
vertex of `C` has exactly its two cycle neighbours within `C`, so each has
at least two—and in particular at least one—neighbours outside `C`.
Consequently

```text
R=H-V(C)
```

is nonempty and connected, and every vertex of `C` has a neighbour in
`R`.

Cutting `C` immediately before each of the five terminals in cyclic order
partitions it into five nonempty, vertex-disjoint path bags.  Each bag is
connected and contains its named terminal; the five cut edges give exactly
the consecutive cycle adjacencies, including the wrap-around edge.  This
is exactly the rooted five-cycle required by the audited cycle decoder.
The construction remains valid when two consecutive terminals are
adjacent, in which case the corresponding arc bag can be a singleton.

For ten cyclic orders the decoder closes directly or returns the common
rooted-`K_4` outcome already handled above.  The independently rerun
dependency-free checker reproduced the two exceptional orders and 27
states each, as well as the assertion that clearing any one of the four
fixed gate defects makes every residual state contain a `K_7` model.

## 4. Crossed-order remainder and the `R` merge

This is the critical lifting step.  In a bad order write the five path bags
in the order

```text
l_1,l_2,r,6,s.
```

They all lie on `C`.  Therefore `R` is disjoint from all five bags.  Put

```text
B_6'=B_6 union R.
```

The following properties hold literally in `G`:

1. `B_6'` is connected, because `R` is connected and has a neighbour at
   every vertex of `C`, hence at a vertex of `B_6`.
2. It remains disjoint from the other four cycle bags, since those bags
   are contained in `C`.
3. It preserves every previous adjacency of `B_6`, because it contains
   `B_6`.
4. It is adjacent to each other cycle bag, because every one of those bags
   contains a vertex of `C` and every such vertex has a neighbour in `R`.

In particular, item 4 supplies the fixed gate adjacency `l_1-6` (and also
`l_2-6`) as an actual edge between the literal bags `B_{l_1}` and `B_6'`.

The cycle verifier tests gate maximality after the five cycle edges have
been added in the virtual edge layer: for each of the four fixed defects it
clears that complement bit and exhaustively verifies a `K_7` model in all
27 states.  The audited lift of a quotient model replaces every terminal
label by its rooted bag.  If the new gate edge lies between two quotient
branch bags, the actual `B_{l_1}`--`B_6'` edge gives their adjacency; if it
lies inside one quotient branch bag, the same edge makes the corresponding
union connected.  Original edges incident with terminal `6` still lift
because the literal root `6` remains in `B_6 subseteq B_6'`.  All other
cycle edges and all disjointness relations are unchanged.

Thus enlarging the `6`-bag is a label-faithful realization of the one-gate
repair.  The finite certificate does not require a literal edge `l_1 6`
in `G`, and the proof does not feed the new adjacency back into any of the
eleven original-edge support constraints.

## 5. Exact-seven separator corollary

If `G` is `K_7`-minor-free, the theorem rules out four-connectivity of
`H`.  Since `H` is three-connected and has at least five vertices, failure
of four-connectivity yields a vertex cut `Z` of order exactly three.
The sets `I` and `Z` are disjoint because `Z subseteq V(H)=V(G)-I`.
Therefore

```text
S=I union Z
```

has order exactly seven and

```text
G-S=H-Z
```

is disconnected.  Hence `S` is a literal separator, not a quotient
boundary.

Let `D` be any component of `G-S`.  Its external neighbourhood is contained
in `S`.  If it missed one member `s` of `S`, then

```text
N_G(D) subseteq S-{s}
```

would have order at most six.  Since `G-S` has another nonempty component,
deleting `N_G(D)` would separate `D` from that component, contradicting
seven-connectivity.  Thus `N_G(D)=S`, and every component is an `S`-full
connected packet.  Grouping the components into any two nonempty classes
therefore gives the asserted actual seven-separation with a full packet in
each open shore.

## 6. Adversarial checks and trust boundary

The following potential failure modes were checked and do not occur:

* The Fabila-Monroy--Wood theorem is used only at four-connectivity, its
  valid strength.
* Cofaciality is transferred in the unique polyhedral embedding; faces
  from unrelated embeddings are not silently identified.
* The common face has length at least five because it contains the five
  distinct terminals, so the induced-cycle degree count is valid.
* The `R` merge uses a remainder disjoint from all rooted cycle bags and
  from `I`; no branch-set collision is introduced.
* The one added gate is a bag adjacency in the final quotient layer, not
  an original label edge and not an input to an irredundancy constraint.
* The separator is genuinely of order seven: `I` has order four, `Z` has
  order three, and they are disjoint.

The computer-assisted trust boundary remains exactly that of the two
adjacent audited decoders.  This audit independently reran

```text
python3 active/hc7_cross_arm_overlap_four_cycle_decoder_verify.py
```

without an assertion failure.  The exterior-connectivity argument itself
is direct and unbounded in the order of `H`.

## 7. Critical packet normalization

Corollary 3.2 adds the hypotheses

```text
chi(G)=7 and every proper minor of G is six-colourable.
```

Together with seven-connectivity and `K_7`-minor-freeness already in force,
these are exactly the hypotheses of the independently GREEN exact-seven
packet theorem.  Every grouping of the components of `G-S` into two
nonempty classes is an actual separation with literal boundary `S`, so the
theorem applies to every such grouping, not just to one preferred
orientation.

Let the components of `G-S=H-Z` be `C_1,...,C_m`.  Corollary 3.1 gives
`m>=2` and makes each `C_i` an `S`-full packet.  If `m>=4`, put two
components on one side and the other `m-2>=2` components on the other.
Each shore contains two disjoint full packets, contradicting the exact
packet theorem's conclusion that the smaller packet maximum is one.
Therefore `m` is two or three.

For each component define

```text
c_i=max{number of pairwise disjoint S-full packets contained in C_i}.
```

The asserted additivity is exact.  There is no edge between distinct
components of `G-S`, so every connected packet in a union of components is
contained in one component.  This gives the upper bound

```text
nu(union_{i in J} C_i) <= sum_{i in J} c_i.
```

Conversely, take a maximum packet family independently inside each
component.  Families from different components are vertex-disjoint, so
their union is a packet family in the grouped shore and gives the reverse
inequality.  Hence equality holds.  Finiteness of `G` ensures that all
these maxima are attained.

If `m=3` and some `c_i>=2`, the grouping

```text
C_i  |  C_j union C_k
```

has packet maxima at least two on both sides: the second side contains the
two full component packets `C_j,C_k`.  This contradicts the exact packet
theorem.  Thus every `c_i=1`.  Additivity then shows that **every**
nontrivial grouping has vector `(1,2)` up to orientation.

If `m=2`, additivity identifies the shore maxima with `(c_1,c_2)`.  The
exact packet theorem leaves only `(1,1)`, `(1,2)`, or `(1,3)` up to
orientation.  Its strong contraction-critical hypothesis is also exactly
the hypothesis of the independently GREEN adaptive `(1,3)` reflection
theorem.  That theorem turns an actual `(1,3)` separation into either a
literal `K_7` or two proper closed-shore colourings with the same exact
boundary partition, which glue to a six-colouring of `G`.  The first
contradicts `K_7`-minor-freeness and the second contradicts `chi(G)=7`.
Thus the only vectors are `(1,1)` and `(1,2)`.

No stronger identity follows.  The argument does not:

* choose an attained boundary colouring state;
* assign packet duties or ranks;
* identify the packet-thin side with a pre-existing named shore or labelled
  local object;
* say that packet maximum one gives a small vertex transversal; or
* make the separator handoff strict under any recursive measure.

It classifies only the number of components and the packet maxima of every
component grouping.
