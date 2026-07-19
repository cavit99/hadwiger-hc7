# Independent audit: two--three linkage reduction

**Audit status:** separate internal audit; **GREEN**.

**Audited source:**
[`hc7_rotation_two_three_linked_reduction.md`](hc7_rotation_two_three_linked_reduction.md)

**Audited source SHA-256:**
`139b2048ae8e46c33407ce75576bf3185705e2713acda2d5659eef1b548a9a2c`

After this audit, the source status line was changed only to record the
GREEN verdict and link to this file.  No theorem statement, proof, scope,
or trust boundary changed.  The resulting source SHA-256 is
`f32397318c4bff6c88f5a2c716ce1e32c9ce32ea8600aee8b15a30c1fae8d6e1`.

**Scope:** Theorem 1.1, Theorem 2.1, Lemma 2.2, Proposition 2.3,
Lemma 3.1, Corollary 3.2, and the stated comparison with the
entrance-edge theorem.  This is an internal mathematical audit, not
external peer review.

## Verdict

The exact revision identified above is correct within its stated scope.
Xie's five-terminal theorem is quoted with the right completion and literal
distinctness hypothesis; the applications to the rotation datum preserve
the attachment roots and all demand occurrences; and the cut-lifting
arithmetic is exact.  The note also distinguishes the Menger paths produced
by Lemma 3.1 from the paths in the separate Jung-based entrance-edge
theorem.

No unresolved mathematical assumption remains inside the stated theorem
outputs.  The final section accurately records the unresolved composition,
colouring, collision, and branch-set-allocation requirements.

## 1. External linkage inputs

### Xie's two--three linkage theorem

The primary source was checked directly.  The cited result is Theorem 1.2.1
of Shijie Xie's 2019 dissertation, on page 4.  For five distinct vertices

\[
                      a_0,a_1,a_2,b_1,b_2,
\]

it assumes that

\[
 G+b_1b_2+\{a_i b_j:i\in\{0,1,2\},\ j\in\{1,2\}\}
\]

is six-connected and concludes that the original graph has two disjoint
connected vertex sets containing the nominated triple and pair,
respectively.  This is exactly Theorem 1.1 of the audited source.  In
particular:

- all seven added edges are the ones in Xie's completion;
- the two connected subgraphs lie in the original graph, not merely in the
  completion; and
- the source requires five literal distinct vertices, exactly as imposed in
  every application here.

No ordinary six-connectivity assumption on `G[Z]` is substituted for the
completion hypothesis.

### Jung's two-linkage theorem

Jung's theorem is not used to prove Theorem 2.1, Proposition 2.3, or
Lemma 3.1.  It enters only through the separately audited entrance-edge
comparison in Section 4.  The current entrance-edge source has SHA-256
`a24964893bc7ed9cb2b46d6025c93c9c744ceecd7e683d0666b910f23741fd4a`
and matches the hash in its adjacent GREEN audit.

The modern traceable restatement, Stephens--Ye, Theorem 1.1, says exactly
that every six-connected graph is two-linked.  The audited source correctly
restates the additional hypotheses needed for the entrance-edge theorem:
the host is seven-connected, the two nominated entrance edges are disjoint,
and all six nominated vertices are distinct.  It makes no direct Jung
application inside `G[Z]`.

## 2. The four completed-connector cuts

The rotation dependency was rechecked at the current source revision

`871125e9b0dc8201ac48d210bc9698f05ccad6d869a46e1806ea4a57bace2a6b`.

Its Theorem 5 says that two disjoint rooted connected subgraphs covering
three of the four demand occurrences yield a seven-branch-set model with at
most one absent adjacency, hence a `K_7^-` minor, and possibly a `K_7`
minor.  The two orientations in Theorem 2.1 meet those hypotheses exactly.

For `H^D_j`, Xie's theorem gives disjoint connected subgraphs containing

\[
                 \{\alpha,p_1,p_2\},\qquad\{\beta,q_j\}.
\]

The first contains the fixed `X`-attachment root and meets both old portal
classes.  The second contains the fixed `W`-attachment root and meets the
selected new portal class.  They therefore cover exactly the required two
old occurrences and at least the selected new occurrence.  Accidental extra
portal contacts only strengthen the resulting minor model.

The reverse orientation is identical with old and new interchanged.  A
label common to `D` and `E` still represents two different centre--row
adjacency demands, so a cross-side repeated label does not invalidate the
four-occurrence count.  The source explicitly assumes `|D|=|E|=2`, hence
the two labels on either one side are distinct.

Thus six-connectivity of any displayed completion contradicts the excluded
minor.  When `|Z|>=7`, failure of six-connectivity gives a separation of
order at most five under the standard definition of vertex connectivity.
No separation conclusion is asserted for connector order at most six.

## 3. Literal collision scope

Every Xie invocation explicitly requires its five nominated vertices to be
distinct.  This excludes all of the relevant literal failures, including:

- coincident attachment roots;
- a root used as a selected portal;
- too few distinct representatives in overlapping portal classes; and
- a singleton portal class shared by old and new demands.

The proof never duplicates a connector vertex into two abstract terminals.
Failure to choose the five vertices is correctly classified as a separate
collision case, not as a linkage obstruction or as a cut supplied by
Theorem 2.1.  The theorem is therefore conditional on each displayed valid
choice; it does not claim that all four choices always exist.

## 4. Shape and host neighbourhood of a completed-connector cut

Lemma 2.2 is exact.  If both open sides contain nominated terminals, the
added edge `b_1b_2` prevents the two surviving `b`-vertices from lying on
opposite sides.  If either `b`-vertex survived outside the separator, all
surviving `a`-vertices would be adjacent to it and hence on the same side.
Therefore both `b_1,b_2` belong to the separator, and surviving members of
the `a`-triple occur on both open sides.

The repaired consequence correctly allows an `a_i` itself to lie in the
separator.  If there is no terminal-free component, every component of
`H^+-T` contains a surviving member of the triple.  Hence there are at most
three such components and at least two, with no unanchored component.  No
claim is made that all three nominated `a`-vertices survive.

If `C` is terminal-free, none of the seven added edges is incident with
`C`, so

\[
                         N_{G[Z]}(C)\subseteq T.
\]

A vertex on the opposite open side is outside `C\cup N_G(C)`, making
`N_G(C)` the boundary of an actual separation.  Seven-connectivity gives
`|N_G(C)|>=7`.  Since at most `|T|` of these neighbours lie in `Z`, at least
`7-|T|` are distinct vertices outside `Z`.  Equality gives an actual
order-seven full-neighbourhood separation; larger neighbourhoods are
correctly retained as positive-excess separations rather than silently
relabelled order seven.

## 5. Lower-demand orientations

Proposition 2.3 uses the same external theorem correctly.

- In the one-versus-two case, Xie returns a `W`-rooted connected subgraph
  meeting both new portal classes and a disjoint `X`-rooted connected
  subgraph meeting the old portal class.  The rotation note's Theorem 2 then
  gives a `K_7` minor.
- In the one-versus-one case, the extra literal terminal `r` is used only to
  form Xie's required triple.  Deleting that requirement from the returned
  connected subgraph leaves the two rooted connected subgraphs required by
  the rotation theorem.

The five-terminal distinctness conditions remain explicit, and the
small-order qualification for converting non-six-connectivity into a cut is
the same as in Theorem 2.1.

## 6. Cut lifting and Menger arithmetic

Let the completed-connector cut have order `t<=5`, with `a,b` chosen on its
opposite open sides.  Deleting `T` from a seven-connected graph leaves a
`(7-t)`-connected graph.  Because `H` contains `G[Z]` and has no open-side
crossing edge, `G[Z]-T` has no `a`--`b` path; in particular, `a,b` are
nonadjacent.

For the minimum end-excluding `a`--`b` separator order `r` in `G-T`,

\[
                              r\ge 7-t.
\]

If equality holds, adjoining `T` gives a separator of order

\[
                         t+(7-t)=7
\]

with `a,b` in nonempty opposite components.  If equality fails, integrality
gives `r>=8-t`, and the vertex form of Menger's theorem supplies at least
`8-t` internally vertex-disjoint `a`--`b` paths in `G-T`.  No such path can
be contained in `Z`; because both endpoints lie in `Z`, every path has an
internal vertex outside `Z`.

For `t<=5`, this yields at least three paths.  Their first vertices outside
`Z` are distinct because those vertices are internal to pairwise internally
disjoint paths.  The proof does not infer that these vertices lie in
distinct named branch sets, or even that they lie in any named branch set.

## 7. Claimed exits and unresolved trust boundary

The source now keeps the two linkage mechanisms separate.  Lemma 3.1
constructs its own Menger paths for a selected opposite-side pair.  It does
not identify those paths with the fixed paths returned by the entrance-edge
theorem; such a fixed path may meet `T` or have its relevant vertices on one
side.

The following matters remain explicitly unresolved and are not used as if
proved:

- existence of all four five-terminal representative choices;
- conversion of every positive-excess full neighbourhood into an
  order-seven boundary;
- a common complete equality partition on the two closed shores of a
  returned order-seven separation;
- allocation of first exits to distinct fixed branch sets; and
- compatibility or a common refinement of the four low-order cuts.

Accordingly, the audited result is a confined linkage-to-cut reduction plus
an exact host-level cut/bypass alternative.  It proves neither the global
two-demand rotation composition theorem nor `HC_7`.
