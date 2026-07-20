# Audit of paired list-critical excess density at order eight

**Audited file:** `hc7_order8_paired_all_tight_closure.md`
**Mathematical revision SHA-256:**
`1f811c98aeb2953ed4b79cedc7bfe29ed88729b59590cd56f70dab9dc4005767`
**Promoted revision SHA-256:**
`9a3473314f9e57e09b9bee26fce830e6b3d252f0d8ce52c8537051fcfdf418b5`
**Audit date:** 2026-07-20
**Verdict:** **GREEN as a conditional theorem.**  The outcome disjunction,
both excess inequalities, the all-tight specialization and the
singleton-response output are correct at the audited revision.

The promoted revision differs from the mathematical revision only in its
status line and link to this audit.

## 1. Extremal eligibility

Since `S=N_G(R)` contains every neighbour of `R` outside `R` and `R` is
connected, `R` is one of the two components `A,D`; hence `|R|>=2`.  The
host has at least twelve vertices.  A degree-eight vertex anywhere in the
host would therefore give an eligible singleton with pair `(8,1)`,
contradicting the selected `(8,|R|)`.  Thus, in the absence of a
degree-seven vertex, seven-connectivity gives `delta(G)>=9`.

## 2. Excess signs and edge decomposition

With the notation of the source,

\[
 \sum_{v\in A\cup D}d_{G[Z]}(v)=6s-C+E,
 \qquad e_{\rm int}=3s-C/2+E/2.
\]

The shore--boundary edge count satisfies

\[
 e_{\rm cross}
   =\sum_{v\in A\cup D}(d_G(v)-d_{G[Z]}(v))
   \ge3s+C-E.
\]

The signs of both `E` terms are correct.  Because `A,D` are the only
components of `G-S`, they are anticomplete and

\[
 |E(G)|=e_{\rm int}+e_{\rm cross}+h
       \ge6s+C/2-E/2+h.
\]

Comparing this with the strict bound `|E(G)|<=5s+24` gives

\[
                         E\ge2s+C+2h-48.              \tag{A.1}
\]

The handshake lemma and minimum degree nine give

\[
 9(s+8)/2\le |E(G)|\le5s+24,
\]

so `s>=24`.  Substitution in (A.1) proves the second lower bound
`E>=C+2h`.

## 3. All-tight and exact-seven outcomes

For each colour used on the nonempty boundary, fullness gives a neighbour
of one boundary vertex of that colour in each shore.  It follows that
`C>=2b>=2`.  Thus the all-tight case `E=0` cannot satisfy
`E>=C+2h` and must enter the degree-seven outcome.

For a degree-seven vertex `x`, the host order is at least twelve, so
`G-N_G[x]` is nonempty and `N_G(x)` is a genuine order-seven singleton
boundary.  Every six-colouring of a proper edge deletion `G-xy` makes the
ends equal.  The restrictions colour the modified closed shores; an intact
singleton extension with the same boundary equality partition would align
and glue to a six-colouring of `G`.  This verifies the generic exact-seven
response.

## 4. Trust boundary

The theorem assumes a minimum order-eight boundary, exactly two nontrivial
boundary-full components, and one boundary colouring whose residual lists
give spanning nonnegative-excess kernels.  It does not prove that every
order-eight response reaches those hypotheses.  Positive excess satisfying
the lower bound is not yet converted into a labelled minor model or common
boundary colouring.  The exact-seven output is recursive rather than a
completed proof of `HC_7`.
