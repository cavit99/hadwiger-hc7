# Independent audit: maximal support pairs in one private-pair kernel

**Verdict:** GREEN.

**Audited source:**
`hc7_maximal_support_pair_private_pair_bridge.md`.

**Source SHA-256:**
`bada5f69a91748c0c66e83cd531f3e80854484e0f8bcfb8083e32cb536e4795e`.

The preceding revision had SHA-256
`753d4b31154a7a06917f1c31639ec50dbe2d1178f98dc2e7ceb9c72c5bb542ca`.
The current revision changes only one relative link in Remark 2.2, from
`../active/hc7_nine_vertex_support_six_closure.md` to
`../results/hc7_nine_vertex_support_six_closure.md`, after that dependency
was promoted.  The theorem statements, hypotheses, proofs, corollaries,
and mathematical dependencies are byte-for-byte unchanged.  This link-only
diff was checked before rebinding the audit to the current hash.

The mathematical revision originally audited had SHA-256
`36fab787459610712bc3a914009a3a4cdd1991d7933c4648a50728a1b1dfe600`.
The later revision changes only the status declaration to link this audit;
its definitions, theorem statements, proofs, corollaries, and limitations
are unchanged.  That metadata-only change was checked before rebinding the
audit to the new hash.

An earlier requested hash was superseded before the mathematical audit by
the final strengthening represented by the preceding hash.  This audit
checks the minimal-family construction, the support potential, the
Bollobas bound and equality case, and every imported extraction and
contraction theorem used in Sections 2--3.

## 1. Existence and minimality of the exact-six family

The graph is finite, so both support families are finite.  Put

\[
 \mathcal E=\mathcal F_6(G)-\mathcal F_5(G).
\]

Every member of `\mathcal E` has order exactly six: a support in
`\mathcal F_6` has order five or six, and every order-five `K_5` model has
five singleton branch sets and is a literal `K_5`, hence belongs to
`\mathcal F_5`.

The audited global literal-`K_5` transversal theorem gives
`tau(\mathcal F_5)<=2`, while the standing contradiction says
`tau(\mathcal F_5\cup\mathcal E)>2`.  Therefore `\mathcal E` is nonempty,
and finiteness permits a nonempty inclusion-minimal subfamily
`\mathcal C` for which

\[
             \tau(\mathcal F_5\cup\mathcal C)>2.       \tag{1.1}
\]

For every `A_i in \mathcal C`, minimality gives a transversal `P_i^0` of

\[
 \mathcal H_i=\mathcal F_5\cup(\mathcal C-\{A_i\})
\]

of order at most two.  If `P_i^0` met `A_i`, it would meet every member of
`\mathcal H_i\cup\{A_i\}`, contradicting (1.1).  Thus `P_i^0` is disjoint
from `A_i`.

## 2. Enlargement to a literal two-set

A seven-connected graph has at least eight vertices.  Since `|A_i|=6`,
there are at least two vertices outside `A_i`.  The set `P_i^0` is already
contained outside `A_i` and has order at most two, so it can be enlarged,
without moving any existing member, to a two-set `P_i` contained in
`V(G)-A_i`.  Enlargement preserves the transversal property for
`\mathcal H_i`.

This verifies the point that the new vertex cannot accidentally enter the
avoided support.  No assumption that a minimum transversal already has
order two is used.

## 3. Exact support height and global maximality

Because `\mathcal F_5 subseteq \mathcal H_i`, the pair `P_i` meets every
literal `K_5`.  Therefore `G-P_i` has no five-vertex `K_5` model, and

\[
                         \mu_G(P_i)\ge6.               \tag{3.1}
\]

The exact-six support `A_i` is disjoint from `P_i`, so its model survives
in `G-P_i` and proves the reverse inequality.  Hence `\mu_G(P_i)=6`.

The assumption `tau(\mathcal F_6)>2` says that every two-set `R` misses
some member of `\mathcal F_6`.  That member supplies a `K_5` model in
`G-R` on at most six vertices, so `\mu_G(R)<=6`.  Consequently every one
of the pairs `P_i` is globally maximizing and

\[
                       \max_{|R|=2}\mu_G(R)=6.          \tag{3.2}
\]

This argument also excludes an infinite value at any pair under the
standing contradiction.

Conversely, if the maximum in (3.2) is six, then every pair `P` has
`\mu_G(P)<=6` and is disjoint from some support in `\mathcal F_6`.
Thus no two-set is a transversal.  A transversal of order zero or one
could be enlarged to a two-set, so none exists either, and
`tau(\mathcal F_6)>2`.  This proves Corollary 2.3 exactly.  Its forward
direction uses the audited literal-`K_5` transversal theorem through
Theorem 2.1; it is not a statement for arbitrary graphs without the
seven-connectivity and `K_7`-minor exclusion hypotheses.

## 4. Bollobas set-pair hypotheses and the bound

For distinct `i,j`, the support `A_i` belongs to `\mathcal H_j`, so the
transversal `P_j` meets `A_i`.  Together with `A_i cap P_i=emptyset`, this
gives

\[
 A_i\cap P_i=\varnothing,
 \qquad A_i\cap P_j\ne\varnothing\quad(i\ne j).        \tag{4.1}
\]

All first sets have order six and all second sets have order two.  These
are precisely the symmetric hypotheses of Bollobas's Two Families
Theorem, which gives

\[
                         |\mathcal C|\le {8\choose6}=28.
\]

No dummy-element uniformization or one-directional version of the theorem
is being used.

At equality, the standard unique equality case gives one eight-set `X`
such that the ordered pairs are all complementary `(6,2)` partitions of
`X`.  Hence

\[
                         \mathcal C={X\choose6}.        \tag{4.2}
\]

The family in (4.2) has transversal number three.  A seven-connected
`K_7`-minor-free graph has at least nine vertices: at order eight,
minimum degree seven would make it `K_8`.  Extend `X` by one host vertex
to a nine-set `X'`.  Every member of (4.2) is an exact six-support in
`X'`, so the full exact-support family in `X'` also has transversal number
greater than two.  The independently audited nine-vertex support closure
would then give a `K_7` minor.  Thus the optional graph-global sharpening
from twenty-eight to twenty-seven is valid.  The elementary bridge itself
correctly retains only the bound twenty-eight.

## 5. Applicability of the private-pair extraction results

For fixed `i`, take

\[
 \mathcal F=\mathcal H_i\cup\{A_i\},\qquad
 A=A_i,qquad P=P_i.
\]

Then `\mathcal F subseteq\mathcal F_6(G)`, its transversal number exceeds
two, and `P` is disjoint from `A` while meeting every other member.  These
are exactly the hypotheses of the audited private-pair extraction theorem;
that theorem does not require the family itself to have been selected by
any stronger criticality convention.  It therefore returns the two
labelled arms in `\mathcal H_i` with the traces and intersection bounds in
Corollary 3.1.

The corrected, graph-specific cross-arm dichotomy has the same host,
family, support, and private-pair hypotheses.  Its own proof supplies the
genuinely separated arms required by its definition, including the former
`5/5` defect.  In the present application the avoided support `A_i` in
fact has order six.  The separated-triple/common-core alternatives and
the replacement supports quoted in Corollary 3.1 are therefore exact.
The bridge does not rely on the retracted purely set-system version.

Finally, `P_i` is a literal-`K_5` transversal, `\mu_G(P_i)=6`, and the
chosen support `A_i` is disjoint from it.  These are exactly the hypotheses
of the audited global support-six contraction dichotomy.  Thus its four
deficiency patterns and its alternative between a seven-connected edge
contraction and an actual order-seven separation containing the split
edge apply separately to every selected model, as stated in Corollary
3.2.

## 6. Exact scope

The bridge validly synchronizes two choices that were previously made
separately: every member of one bounded exact-six witness family has a
private pair that is also globally maximal for `\mu_G` and meets every
literal `K_5`.

It does not show that:

- every globally maximizing pair occurs as one of these private pairs;
- the split branch sets selected for different supports are disjoint or
  compatible;
- their contractions preserve connectivity simultaneously;
- any returned order-seven separations share roots, side assignments, or
  a strict induction parameter;
- a pair has support height at least seven; or
- the support-six transversal theorem or `HC_7` follows.

The theorem file states these limitations accurately.  The only
computer-assisted dependency is the separately audited nine-vertex
closure used for the optional `28`-to-`27` sharpening.
