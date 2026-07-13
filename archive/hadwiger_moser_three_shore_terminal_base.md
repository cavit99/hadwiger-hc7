# Terminal base of the Moser owner descent

## 1. Result

Use the three-full-shore pure-Moser setting and unique capacity ownership
from `hadwiger_moser_three_shore_owner_descent.md`.  Call a shore
**low-owner** if it owns at most five of the sixteen optimal Moser
partitions.

### Theorem 1.1 (certified terminal base)

Suppose a low-owner shore \(D\) has no cutvertex, no internal two-cut
which yields the exact-seven descent of Lemma 6.2 in the owner-descent
note, and \(|D|\le6\).  Under the necessary conditions

\[
 \delta(G)\ge7,
 \qquad
 |N_G(X)|\ge7\quad
 (\varnothing\ne X\subsetneq D),                 \tag{1.1}
\]

the only possible shore is a single vertex complete to the seven
boundary roots.

In a hypothetical \(HC_7\) counterexample that singleton is impossible.
Indeed, if \(D=\{x\}\), then \(N_G(x)=S\), so \(d(x)=7\), its
neighbourhood is the pure Moser spindle, and

\[
 G-N[x]
\]

has exactly the other two full components.  This is precisely the
already-audited pure-Moser two-component degree-seven cell eliminated in
`hadwiger_moser_supported_pair_transfer_closure.md`.

Consequently the finite alternative in the low-owner descent has no
terminal survivor.  Every three-shore Moser cut exposes a proper nested
exact seven-fragment.

## 2. Transparent facial proof for orders four to six

The finite claim no longer depends on a black-box UNSAT answer.
The hand-checkable reduction in
hadwiger_moser_three_shore_small_face_certificate.md proves the
stronger statement that every three-connected shore of order four to
six owns every one of the sixteen partitions.

For a fixed allegedly unowned partition, its three crossless pair
demands give faces \(F_{12},F_{13},F_{23}\) in the unique embedding of
the shore.  If \(m(u)\) is the number of the three pairwise face
intersections containing \(u\), then

\[
             |N_S(u)|\le 1+2m(u).
\]

Consequently minimum degree requires

\[
             d_D(u)+1+2m(u)\ge7.                 \tag{2.1}
\]

There are only ten planar three-connected graphs of orders four to six.
The facial table in the cited note checks every triple of their faces;
none satisfies (2.1) at all vertices.  Nonplanar internal graphs were
already excluded by the first bare web.  Orders two and three have the
elementary carrier proofs recorded there.

## 3. Independent finite verifier

The dependency-declared script

`moser_three_shore_terminal_cegis.py`

performs the finite check.  It uses the complete NetworkX atlas of
unlabelled graphs through order six.  It checks every connected graph at
orders one to three and every three-connected graph at orders four to
six.  This is complete for the terminal branch: a cutvertex is excluded
by Lemma 6.1 of the owner-descent note, while an internal two-cut gives
the exact descent by Lemma 6.2.

For every internal graph, the seven root-contact incidences are Boolean
variables.  The solver imposes exactly:

1. **fullness:** every boundary root contacts the shore;
2. **minimum degree:** for every shore vertex \(u\),
   \(d_D(u)+|N_S(u)|\ge7\);
3. **relative seven-connectivity:** for every nonempty proper
   \(X\subset D\),

   \[
    |N_D(X)-X|+|N_S(X)|\ge7;                      \tag{3.1}
   \]

4. **low ownership:** among the sixteen optimal boundary partitions,
   at most five have two pair blocks supported by disjoint connected
   vertex masks of \(D\).

Condition 4 is exact.  If two disjoint connected carriers are not
adjacent, a shortest path between them can be split and absorbed into
the carriers.  Conversely every double realization contains the two
enumerated disjoint masks.

The execution output is:

```text
order 1 terminal candidate graphs 1
SURVIVOR order 1 ... owners [] rows {0: [0, 1, 2, 3, 4, 5, 6]}
order 2 terminal candidate graphs 1
UNSAT A_ iterations 0
order 3 terminal candidate graphs 2
UNSAT Bo iterations 0
UNSAT Bw iterations 0
order 4 terminal candidate graphs 1
UNSAT C~ iterations 0
order 5 terminal candidate graphs 3
UNSAT Dl{ iterations 0
UNSAT Dn{ iterations 0
UNSAT D~{ iterations 0
order 6 terminal candidate graphs 17
UNSAT (all seventeen graph types) iterations 0
records 25 sha256 d74287d353e0f3d49b1f24c90f42938b08ba40e3543cad5070348a908d75576b
```

The zero iteration counts mean that fullness, (1.1), and low ownership
are already inconsistent; the optional exact \(K_7\)-model CEGIS layer
is not used for these UNSAT rows.  The sole satisfying assignment is the
full singleton described in Section 1.  The script asserts the atlas
counts, the exact singleton record, the zero-iteration status of all
twenty-four UNSAT rows, and the displayed SHA-256 digest.

The shorter script moser_three_shore_small_face_verify.py independently
reconstructs the ten-row facial table without Z3 or a minor-model
search.

## 4. Scope

This theorem closes the bounded endpoint of the three-shore descent.  It
does not by itself eliminate the nested exact seven-cut: that cut may
have two components and feed the general two-shore portal-lock problem.
Its contribution is to prove that the three-shore Moser geometry cannot
terminate locally or persist as an unbounded web.  It must strictly
export the obstruction to a smaller exact adhesion.
