# Independent audit: five-vertex cyclability after three deletions

## Verdict and audited revision

**GREEN.**  The proof is correct under its stated hypotheses.  In particular,
the cited Watkins--Mesner result supplies the *specified* four-vertex
separator used in the proof, and the exact-seven packet theorem applies to
the resulting actual separation without an unstated connected-shore
hypothesis.

This audit checks
`results/hc7_three_vertex_deletion_five_cyclability.md` at SHA-256

```text
93d4c49b90ea06d5143fcb4e04ed7c76a4160b92c63c7fdf7969325c7281c1c7
```

The only change from the previously audited revision
`ee6bfa81673d6ad65c35bf430a88137ec714229c6af6b64a382532db5dedf816`
is the status line: “independent audit pending” was replaced by “separate
internal audit.”  The theorem statement, proof, application, and citation
boundary are byte-for-byte unchanged.  No finite computation is used in this
theorem.

## 1. Connectivity and the cases of at most two deletions

Let `H=G-X`.  Deleting `r` vertices from a seven-connected graph leaves a
`(7-r)`-connected graph, provided vertices remain.  Thus `H` is at least
five-connected when `|X|<=2`.  Dirac's prescribed-vertex cycle theorem then
puts any prescribed five vertices on one cycle.

When `|X|=3`, `H` is four-connected.  The five-connected subcase is again
closed by Dirac.  Hence a counterexample to the asserted cyclability must
satisfy

\[
                              \kappa(H)=4.                  \tag{1.1}
\]

This reduction is valid and exhausts the connectivity alternatives.

## 2. Exact Watkins--Mesner implication

The relevant primary source is M. E. Watkins and D. M. Mesner, *Cycles and
Connectivity in Graphs*, Canadian Journal of Mathematics 19 (1967),
1319--1328, Theorem 1 and its necessity proof,
<https://doi.org/10.4153/CJM-1967-121-2>.

The statement of Theorem 1 characterizes the equality between connectivity
`lambda` and guaranteed cyclability by a separator of order `lambda` leaving
at least `lambda+1` components (p. 1319).  The stronger specified-set fact
used here is proved in its necessity direction: starting with prescribed
vertices

\[
                         c_1,\ldots,c_{\lambda+1}
\]

that lie on no common cycle, the proof constructs one set `S` of order
`lambda` and proves that those particular vertices lie in distinct
components of `H-S` (pp. 1321--1324, especially the conclusion on p. 1322).
The concluding observation on p. 1328 also states the uniqueness of this
separator relative to the specified noncyclable set.

Here the equality hypothesis is automatic.  Dirac's theorem says every
four-set of the four-connected graph `H` is cyclable, whereas the assumed
noncyclable five-set `W` shows that not every five-set is cyclable.  Hence
Watkins and Mesner's guaranteed-cyclability parameter is exactly
`lambda=4`.  For this value, therefore, the prescribed set `W`
gives a set `S` of order four such that the five members of `W` lie in five
distinct components of `H-S`.  The source theorem is not being replaced by
the weaker assertion that *some* four-cut has five components; it gives the
exact implication required by the proof.

## 3. Lifting to an actual order-seven separation

Since `X` and `S` lie in disjoint vertex sets, the set

\[
                              T=X\mathbin{\dot\cup}S
\]

has order seven.  The components of `G-T` are precisely those of `H-S`, so
there are at least five.

For any component `C` of `G-T`, all its neighbours lie in `T`.  Since another
component of `G-T` is nonempty, `N_G(C)` is an actual vertex cut separating
`C` from that component.  Seven-connectivity yields

\[
                         7\le |N_G(C)|\le |T|=7,
\]

and hence `N_G(C)=T`.  Thus every component is a connected `T`-full
subgraph.  No collective-fullness assumption is substituted for literal
adjacency to each member of `T`.

Choose one component as one open shore and take the union of all remaining
components as the other.  The shores are nonempty and anticomplete and have
literal common boundary `T`, so this is an actual order-seven separation.
The first shore contains one `T`-full connected subgraph and the other
contains at least four pairwise vertex-disjoint such subgraphs.  Therefore

\[
                              \nu_1+\nu_2\ge5.              \tag{3.1}
\]

## 4. Packet-theorem dependency

The invoked dependency is
`results/hc7_exact_seven_packet_packing.md`, at SHA-256

```text
501f581d764607ef9cd13b854150dae95ea251efde0fdd28c77bb9632415fc57
```

Its adjacent audit is GREEN and has been pinned to that revision.  Its
hypotheses are exactly those assumed here: seven-connectivity,
`K_7`-minor-freeness, `chi(G)=7`, and six-colourability of every proper
minor.  It permits disconnected open shores and defines `nu_i` using
arbitrary disjoint full connected subgraphs.  Consequently its bound

\[
                              \nu_1+\nu_2\le4
\]

contradicts (3.1).  This completes the audit of the proof.

## 5. Degree-eight application

For each `i`, the displayed deletion set

\[
                         X=\{v\}\cup(B-\{b_i\})
\]

has order three and is disjoint from the five-set `C`, so the theorem gives
the claimed cycle.  The application correctly records only three possibly
different cycles.  It does not infer a single cycle avoiding all four
vertices `\{v\}\cup B`, and it does not infer a cycle avoiding a prescribed
connected branch set.

## 6. Trust boundary

The audited theorem proves five-vertex cyclability in `G-X` for every
`|X|<=3`.  It does **not** prove any of the following:

- that a prescribed connected subgraph can simultaneously be avoided;
- that the resulting cycles can be chosen compatibly or combined;
- that the five vertices occur in a prescribed cyclic order;
- that an order-seven separation returned elsewhere has compatible shore
  colourings; or
- that `HC_7` follows.

The result uses the full contraction-critical hypotheses only through the
exact-seven packet theorem.  It should not be generalized to arbitrary
seven-connected `K_7`-minor-free graphs without replacing that input.
