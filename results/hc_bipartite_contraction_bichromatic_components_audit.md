# Independent audit: bichromatic component constraints after a bipartite contraction

**Audited file:**
[`hc_bipartite_contraction_bichromatic_components.md`](hc_bipartite_contraction_bichromatic_components.md)

**Audited source SHA-256:**
`ca1d5ba0defb2af5c5db6c10c96e3279c68fb64fa0ffb07543a44a1db93b7eae`

**Previous mathematically audited revision SHA-256:**
`b9661505caf7c2479d6ae5874f950ed2a57fe86ae353398cc66269272c643921`

**Verdict:** **GREEN.**

The revised source has the same mathematical content as the previous GREEN
revision.  Its changes are terminology-only, together with corresponding
line wrapping.  The detailed deductive audit of the previous revision is
preserved in
[`hc_bipartite_contraction_cross_lock_audit.md`](../archive/hc_bipartite_contraction_cross_lock_audit.md).
The arguments were also rechecked against the revised text; no mathematical
repair is required.

The promoted source differs from the terminology-audited revision only in
changing its status line from “audit pending” to “audit GREEN”; its
mathematical statement and proof are unchanged.

## 1. Revision comparison

The revision makes the following descriptive substitutions:

- the title and Section 2 now describe bichromatic component constraints and
  a diagonal component theorem;
- Theorem 2.1 is named the diagonal bichromatic component theorem;
- Corollary 3.1 is named a matching of disjoint bichromatic components;
- later references to the selected components use “diagonal bichromatic
  components”; and
- “nonbuffer colour” is expanded as a colour other than the contracted
  colour, or equivalently a colour other than `gamma`.

These substitutions do not change an object, hypothesis, quantifier, or
conclusion.  In particular, all displayed definitions and equations
(1.1), (2.1)--(2.5), the two alternatives of Theorem 2.2, and the separation
pair in its proof are unchanged.  The `k=7` phrase “five colours other than
`gamma`” is exactly the earlier set of five “nonbuffer” colours.

## 2. Mathematical recheck

For `i != gamma`, the canonical identification
`V(G/Q)-{q}=R` makes `psi^{-1}(i)` a subset of `R`.  Thus the terminal sets
in (1.1) are well-defined subsets of `R`, may overlap between the two
bipartition sides, and are nonempty by the promoted palette theorem.

In Theorem 2.1, the proof still switches every whole `i,j`-component meeting
`A_i union B_j`.  Under the contradictory assumption, no switched component
meets `A_j union B_i`.  The simultaneous switch therefore removes colour
`i` from the external neighbourhood of `A` and colour `j` from the external
neighbourhood of `B` without recreating either conflict.  Colouring `A` with
`i` and `B` with `j` is proper on the boundary and on the induced bipartite
graph `G[W]`, giving the same contradiction.

In Theorem 2.2, a unique boundary component contains all four terminal sets.
If there is more than one, then for each chosen `L` another terminal
component `L'` supplies a vertex outside `L union N_G(L)`, since distinct
components of the induced two-colour graph are anticomplete.  Hence

\[
 X=L\cup N_G(L),\qquad Y=V(G)-L
\]

is still an actual separation with two nonempty open sides.  The boundary
part in `W` is nonempty, while every boundary vertex in `R` has a colour
outside `{i,j}`; otherwise it would lie in the same two-colour component.
The connectivity conclusion is unchanged.

Corollary 3.1 still follows because components assigned to different edges
of a colour matching use disjoint pairs of colour classes.  For `k=7`,
`chi(G/Q)=6`, so there are exactly five colours other than `gamma`.  Two
matching edges use four, leaving `h`; the two selected components use those
four classes and the common support component uses only `gamma,h`.  The
three connected subgraphs are therefore pairwise vertex-disjoint.  Under
outcome 1 for both matched pairs, all three are adjacent to both sides, and
when `Q` is an edge they contain three internally vertex-disjoint external
paths between its endpoints exactly as in the previous revision.

## 3. Assumptions and limitations

This audit uses the same standard conventions as the previous audit:
graphs are finite and simple, `N_G(S)` is the external open neighbourhood,
and `ell`-connectivity excludes separations of order below `ell` with two
nonempty open sides.  It relies on the exact promoted palette theorem
identified in the previous audit.  There are no unresolved assumptions or
gaps under these conventions.

The revised terminology does not strengthen the result.  A selected
bichromatic component need not meet both bipartition sides or contain
distinct literal terminals.  Separators obtained from different components
need not coincide, witnesses for different matchings need not be compatible,
and the three `k=7` witnesses are not automatically aligned with a labelled
clique-minor model.  No `K_7`-minor conclusion is asserted.
