# Audit of the special five-plus-two exact-seven response theorem

**Verdict:** GREEN.

**Audited source:**
[`hc7_special_five_plus_two_exact7_response.md`](hc7_special_five_plus_two_exact7_response.md)
with SHA-256

```text
abcfb4a16616bfa5260826c798589afc93aa592f0f73068ea2bf7a95f8e34f19
```

This is a separate internal mathematical audit, not external peer review.
The verdict covers Theorem 2.1 and its proof in the exact inherited setting
stated in Section 1.  It does not promote any stronger conclusion about an
arbitrary order-seven separation.

## 1. Boundary extraction

The invocation of the concentrated three-owner order-eight reduction is
correct.  Its proof gives a vertex `v`, a separator

\[
 Z\subseteq V(H_0)-\{v\},\qquad |Z|\le2,
\]

and the component `A` of `H_0-Z` containing `v`, with

\[
 N_G(A)\subseteq(S_8-T)\cup Z.
\]

Here `Z` lies in `C union T`, whereas `S_8-T` consists of the two internal
transversal vertices and the three nonowner boundary representatives.
Thus the two sets on the right are disjoint.  At least one of the three
owner representatives lies outside `Z`; the fan-separator property puts it
outside `A`, and it is not on the displayed right-hand side.  Therefore the
separation is nontrivial.  Seven-connectivity forces

\[
 |Z|=2,\qquad N_G(A)=(S_8-T)\mathbin{\dot\cup}Z,
 \qquad |N_G(A)|=7.
\]

Consequently `A` and its complement outside the boundary are nonempty,
connected-side versus possibly disconnected-side open shores with no edge
between them.  The normal form in equations (1.5)--(1.6) is valid.

## 2. Full connected subgraphs and packing vector

For every component `K` of `G-Y`, its neighbourhood is contained in `Y`.
If `K` missed a boundary vertex, its neighbourhood would have order at most
six and would separate it from the nonempty opposite shore.  Thus every
component is adjacent to every literal boundary vertex.

The hypotheses of the exact-seven full-subgraph packing theorem are all
present: `G` is seven-connected, `K_7`-minor-free, seven-chromatic, every
proper minor is six-colourable, the boundary has order seven, and both open
shores are nonempty.  It gives

\[
 \nu_A+\nu_B\le4,
 \qquad \min\{\nu_A,\nu_B\}=1.
\]

The adaptive `(1,3)` reflection theorem applies to the remaining
orientation `(1,3)` and would give either a `K_7` minor or a six-colouring,
both excluded.  Hence, up to orientation, only `(1,1)` and `(1,2)` remain.
Item 1 is correct.

## 3. Boundary chromatic number

The exact-seven boundary classification applies to this actual separation.
It gives `chi(F)<=5`.  In the equality case it gives

\[
 F\cong K_2\vee C_5,
\]

connected open shores, full adjacency of each shore to the boundary, and a
`K_5` minor in the graph obtained by deleting the two universal boundary
vertices.  These are exactly the hypotheses of the cycle-boundary
completion theorem: the five remaining boundary vertices induce a cycle,
the two universal vertices are adjacent to one another and to the cycle,
and the complement of the seven-set has exactly the two connected full
shores.  That theorem would give a `K_7` minor.  Therefore the equality case
is impossible and `chi(F)<=4`.  Item 2 is correct.

## 4. Operation-specific partition and reflection demand

Since `Y=N_G(A)`, every `z in Z` has a neighbour `a in A`.  A six-colouring
`c` of the proper minor `G-za` must satisfy `c(z)=c(a)`, or it would already
colour `G`.  The deleted edge does not occur in the opposite closed shore,
so `c` restricts there and induces the stated exact boundary partition
`Pi_z`.

If the same partition extended through the original `A`-side, a permutation
of the six colour names would align the two exact partitions and the
colourings would glue.  Hence the set difference in (2.3) is correct.

Applying the exact packet-reflection lemma to `nu_B` disjoint full connected
subgraphs in `B` shows that `d_F(Pi_z)<=nu_B` would produce either a
`K_7` minor or precisely the forbidden extension through `A`.  Thus

\[
 d_F(\Pi_z)>\nu_B.
\]

For the mixed-support claim, the transported-partition Hall theorem is
applied after interchanging its abstract shore names: the original
colouring and the displayed connected supports both lie in `B`, and the
conclusion is a colouring of the closed `A`-side.  The `nu_B` full connected
subgraphs are universal vertices of the incidence graph, while the `W_i`
have exactly the duty incidences defined in (2.6).  Failure of a saturating
matching therefore yields

\[
 \nu_B+|N_{\{W_1,\ldots,W_t\}}(X)|<|X|.
\]

When the number `d` of blocks not represented by the selected maximum
singleton clique is `nu_B+1`, every nonempty family of at most `nu_B`
blocks already sees all universal vertices.  The Hall-deficient family is
therefore the entire block set, and it has no `W_i`-neighbour.  This proves
the two stated sharp cases.  Item 3 is correct.

## 5. Critical-edge fan and strict descent

The critical-edge Kempe argument applies to `za`: for every colour other
than `alpha=c(z)=c(a)`, the two endpoints belong to one bichromatic
component, and truncating a path at its first boundary vertex keeps every
internal vertex in the component `A` of `G-Y`.

The hypotheses of the critical boundary-edge fan theorem hold with its
boundary endpoint equal to `z`, its source equal to `a`, and its open
component equal to `A`.  Theorem 2.1 therefore supplies the six-ended fan
with distinct boundary ends while preserving the direct edge and the five
prescribed first edges.

The set `T_0` has order at most six.  If it has order six, the first
alternative is exactly the normalized outcome recorded in the draft.  If
it has order at most five, Theorem 3.1 applies to any five-set `T'`
containing it.  Its packing outcome is the five-path statement in item 4.2.
Its failure outcome gives a nonempty proper connected subset `A'`, a
four-set in `A-a`, the exact order-seven boundary in (2.9), and the strict
inequality `|A'|<|A|`.

The only improper edge of `c` in the original graph is `za`.  In the
descent outcome `z` lies in `T'` and hence outside the new closed `A'`-side,
so the restricted colouring is proper there.  The cited corollary supplies
on the opposite closed shore the same exact `alpha`-coloured boundary block.
It does not supply the rest of the boundary partition.  Item 4 is correct.

## 6. Trust boundary and residual obligation

The draft states its limitations accurately:

- the fan conclusions preserve the five first edges but do not allocate
  the paths to the inherited clique-minor branch-set labels;
- the target-retaining packing may repeat boundary endpoints;
- the strict descent is available only when `|T_0|<=5` and that packing
  fails;
- the descent synchronizes one exact boundary block, not a complete
  equality partition; and
- no cited result turns the returned separation by itself into a
  six-colouring or a `K_7`-minor model.

Accordingly, the proved normal form is useful and unbounded, but the exact
remaining step is still an operation-specific, label-preserving completion
or complete boundary-colouring synchronization.  The theorem does not
prove `HC_7`.

## 7. Finalized editorial changes

After the mathematical audit, the source status line was updated to record
this adjacent audit, `d=d_F(Pi_z)` was made explicit, and the separation was
written as the literal partition
`V(G)=A dotcup Y dotcup B` with `E_G(A,B)=emptyset`.  These are expository
changes only; they do not alter the theorem, proof, hypotheses, or trust
boundary checked above.  The audited hash at the head of this note is the
hash of that finalized source.
