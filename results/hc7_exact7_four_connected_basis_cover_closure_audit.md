# Independent audit: four-connected basis-cover closure

**Verdict:** GREEN.

**Audited source:**
`results/hc7_exact7_four_connected_basis_cover_closure.md`

**Source SHA-256:**
`fc41b67243dd31c4463716de9d0b6cf1842681d2d6d9546aad00a36fa7cbd062`

Promotion changed only the source status line and filename; the audited
mathematical text is unchanged.

The audit treats the displayed literal setup as hypotheses.  In particular,
it does not claim that an arbitrary exact-seven `(1,2)` cell automatically
has a four-connected thin shore, adjacent rich packets, or the three named
boundary literals required in the setup.

## 1. Boundary matchability and the separator

Lemma 2.1 is correct.  If a nonempty `W subseteq A` violates Hall, put
`X=N_L(W)`.  Since `|W|<=4` and `|X|<|W|`, one has `|X|<=3`.  A
four-connected graph has at least five vertices, so `L-X` is nonempty.

The set

\[
                         (S-W)\cup X
\]

separates `L-X` from the nonempty opposite shore `R`: there is no `L-R`
edge by the literal separation, and no vertex of `L-X` sees a member of
`W` by the definition of `X`.  Its order is

\[
             7-|W|+|X|\le 6,
\]

contradicting seven-connectivity.  Thus every boundary set of order at
most four is matchable into `L`.

## 2. Complete basis coverage

Lemma 3.1 is correct.  Its forced-Hall proof may be checked as follows.
After reserving `sz`, a minimal deficient set
`U subseteq A-{s}` has

\[
 Y=N_{L-\{z\}}(U),\qquad |Y|=|U|-1.
\]

Every proper subset of `U` satisfies Hall into `Y`.  Lemma 2.1 makes `U`
matchable into `L`; because only `|U|-1` neighbours remain after deleting
`z`, the vertex `z` has some neighbour `u_0 in U` and
`N_L(U)=Y union {z}`.  Minimality matches `U-{u_0}` into `Y`.

If `A-U` did not match into `L-N_L(U)`, a Hall witness
`W subseteq A-U` would give

\[
\begin{aligned}
 |N_L(U\cup W)|
 &=|N_L(U)\cup N_{L-N_L(U)}(W)|\\
 &<|U|+|W|,
\end{aligned}
\]

contradicting Lemma 2.1 for `U union W subseteq A`.  The resulting three
matchings use the disjoint right sides `Y`, `{z}`, and
`L-N_L(U)`, so they form an `A`-basis containing `z`.  The originally
prescribed label `s` need not represent `z`; only the literal root must be
retained, exactly as the theorem states.

There is also a shorter equivalent verification.  For fixed `A`, the
`A`-bases are the bases of the transversal matroid on `N_L(A)`.  Lemma 2.1
gives that matroid rank `|A|`, and every `z in N_L(A)` is a nonloop.
Every nonloop extends to a basis.  This proves Corollary 3.2 directly and
shows that no packet classification, descended equality state, or
minimum-shore argument is needed.

## 3. Rooted-face principle

Lemma 4.1 is correct.  The basis-exchange graph of a matroid is connected,
and adjacent rank-four bases share three literal vertices.  If no basis
roots a `K_4`, the four-connected rooted-`K_4` theorem puts every basis on
a face of the unique plane embedding of `G[L]`.  Two distinct faces of a
three-connected plane graph share at most two vertices, so consecutive
bases use the same face.  Basis-graph connectivity and complete basis
coverage then put all of `N_L(A)` on that face.

## 4. Rooted-model lift

The rooted-model branch of Theorem 5.1 is correct.  An `A_Y`-basis comes
with a matching between its four roots and the four literal labels of
`A_Y`.  Adjoining each matched boundary label to its rooted `K_4` bag
preserves connectivity, disjointness, and all pairwise bag adjacencies.
Together with the disjoint adjacent `S`-full packets `P,Q`, these bags form
a literal `K_6` model.

The singleton `{c}` meets `P` and `Q` by fullness and meets the two bags
anchored at `d_1,d_2` through the assumed edges `cd_1,cd_2`.  It may miss
only the two remaining rim bags.  Both possible missing adjacencies are
incident with `{c}`.  Hence the seven bags form the claimed labelled
`K_7^vee` model after surplus adjacencies are ignored.

## 5. Face synchronization

The synchronization argument is correct.  If two two-sets `Y,Y'` share a
label, then `A_Y` and `A_Y'` share three labels.  Choose an `A_Y`-basis and
the three distinct roots representing these common labels.  They lie on
`F_Y`; each also belongs to `N_L(A_Y')`, whose entire portal union lies on
`F_Y'`.  Thus the two faces share three literal vertices and are equal.

The intersection graph on the two-subsets of the four-set `W` is
connected.  Therefore all the faces coincide, and every portal belonging
to `S-{c}` lies on one face.  This uses complete portal sets, not merely
one chosen representative per boundary label.

## 6. Curvature and final contradiction

The use of the audited cofacial-portal degree theorem is valid.  Its
hypotheses hold for the literal separation and the four-connected planar
shore, with all portals of `S-{c}` on the synchronized face.  It supplies
an off-face vertex of `L` with internal degree at most five.  Such a vertex
has no neighbour in `R`, no neighbour in `S-{c}`, and at most the one
remaining boundary neighbour `c`; hence its total degree in `G` is at most
six.  This contradicts seven-connectivity.

## 7. Exact scope

The proved conclusion is a literal labelled `K_7^vee` model under the
displayed local hypotheses.  It is **not** a literal `K_7` model and does
not by itself prove `HC_7`; a separate near-`K_7` composition or terminal
argument remains necessary.  Conversely, the proof does genuinely remove
the earlier global-minimum and state-pullback obligations from this
four-connected local branch.
