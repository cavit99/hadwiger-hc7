# Cross-lobe duty failure forces one common literal face

**Status:** proved and independently audited.  This theorem closes the
nonplanar part of the cross-lobe one-sibling family and extracts one literal
alternating facial cycle.  It does not yet transport an equality state
across the resulting planar page.

## 1. Abstract common-face theorem

Let `G` be a seven-connected graph.  Let `S` be a set of seven vertices,
let `C` be a component of `G-S`, and assume that

\[
                    G-(S\cup V(C))\ne\varnothing .       \tag{1.1}
\]

Choose distinct vertices

\[
              a_1,t_1,a_2,t_2,a_3,t_3,c\in S            \tag{1.2}
\]

such that `a_i t_i` is not an edge for every `i`.  Assume that `C` is
three-connected.  Finally, suppose that for each `i` there are
nonadjacent literal witnesses

\[
                  p_i\in N_C(a_i),\qquad
                  q_i\in N_C(t_i).                       \tag{1.3}
\]

### Theorem 1.1 (three duty failures have one common face)

Suppose that for every two distinct indices `i,j` there do not exist
vertex-disjoint connected subgraphs `P_i,P_j` of `C` such that

\[
 \{a_i,t_i\}\subseteq N_S(P_i),\qquad
 \{a_j,t_j\}\subseteq N_S(P_j).                         \tag{1.4}
\]

Then `C` is planar.  In its unique plane embedding there is one face `F`
incident with every vertex of

\[
             \bigcup_{i=1}^3\bigl(N_C(a_i)\cup N_C(t_i)\bigr). \tag{1.5}
\]

More precisely, for each pair `i\ne j`, form `C_ij^+` by adjoining four
new artificial terminals

\[
              \alpha_i,\alpha_j,\tau_i,\tau_j,            \tag{1.6}
\]

where `alpha_r` is adjacent exactly to `N_C(a_r)`, `tau_r` is adjacent
exactly to `N_C(t_r)`, and no other new edge is added.  Then `C_ij^+` has
a plane embedding in a closed disk in which the four artificial terminals
occur on the boundary in the cyclic order

\[
                \alpha_i,\alpha_j,\tau_i,\tau_j.          \tag{1.7}
\]

The artificial terminals are bookkeeping devices.  No edge added by a web
completion is asserted to be an edge of `G`.

### Proof

Fix distinct `i,j`, and let `k` be the third index.  Put

\[
                         H_{ij}=C_{ij}^+.                 \tag{1.8}
\]

Consider the ordered four-tuple

\[
              (\alpha_i,\alpha_j,\tau_i,\tau_j).          \tag{1.9}
\]

A crossing of this tuple consists of disjoint `alpha_i-tau_i` and
`alpha_j-tau_j` paths.  The paths are terminal-clean and the artificial
terminals have no edges between them.  Deleting their first and last edges
therefore leaves the two carriers forbidden by (1.4).  Consequently the
tuple (1.9) is crossless.

The generalized Two Paths Theorem gives a same-vertex edge completion of
`H_ij` to a four-web with frame (1.9).  We next show that no actual vertex
of `C` lies in the interior of a clique cell of this web.  Suppose
otherwise, and let `D` be a component of the actual graph induced by the
`C`-vertices in the interior of one such cell.  Let `Delta` be the facial
rib triangle supporting that cell.
In the completed web every neighbour of a cell vertex outside the cell is
in `Delta`.  By the choice of `D`, an actual edge to another actual cell
vertex would put that vertex in the same component.  Hence, in the
original graph,

\[
       N_G(D)\subseteq \mu(V(\Delta))\cup\{c,a_k,t_k\}.   \tag{1.10}
\]

Here `mu` fixes a triangle vertex in `C` and replaces an artificial
terminal by its corresponding literal member of `S`, so
`|mu(V(Delta))|<=3`.  There are no other exits: `C` is a component of
`G-S`, and every edge to one of the four represented boundary labels is
encoded by its artificial terminal.  Thus the right side of (1.10) has
order at most six.  It separates the nonempty set `D` from the nonempty far
side in (1.1), contradicting seven-connectivity.

All vertices of `C` and all artificial portal edges of `H_ij` therefore
lie in the planar rib.
Deleting completion edges can only merge faces, so `H_ij` has the disk
embedding in (1.7).  After the four frame vertices are deleted, all of
their literal neighbours in `C` are incident with one face of the inherited
embedding of `C`; call it `F_ij`.  This proves planarity of `C` and the
pairwise assertion.

Because `C` is three-connected, its plane embedding is unique up to
reflection.  In a three-connected plane graph two distinct facial cycles
meet in at most one edge.  The faces `F_12` and `F_13` are both incident
with all vertices of

\[
                         N_C(a_1)\cup N_C(t_1).           \tag{1.11}
\]

By (1.3), this set contains the two nonadjacent vertices `p_1,q_1`.
Therefore `F_12=F_13`.  Comparing `F_12` and `F_23` in the same way, using
`p_2,q_2`, gives `F_12=F_23`.  Their common value `F` is incident with all
six portal sets, proving (1.5).  `square`

## 2. Exact-seven one-sibling application

Use the notation of
`../results/hc7_exact7_one_sibling_gate_funnel.md`.  Thus

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 \Pi=\{\{a_i,t_i\}:i\in[3]\}\cup\{\{c\}\},             \tag{2.1}
\]

`C-X` has lobes `K,J`,

\[
 N_S(K)=\{c,a_1,a_2,a_3\},\qquad
 \{t_1,t_2,t_3\}\subseteq N_S(J),                       \tag{2.2}
\]

and a second disjoint `S`-full packet `Q` is available in the rich shore.

### Corollary 2.1 (the cross-lobe survivor is one planar page)

If the attained state `Pi` does not reflect, then `C` is planar and one
face of `C` is incident with every literal `C`-portal of the six vertices
`a_i,t_i`.

### Proof

If two duties `B_i=\{a_i,t_i\}` and `B_j=\{a_j,t_j\}` had disjoint
connected carriers in `C`, assign them to those two blocks and let the
full packet `Q` fund the third block.  The literal edge between every two
old blocks, the fullness of `Q`, and the named `c-B_r` boundary edges give
the exact attained-state reflection contraction.  Hence (1.4) holds.

For each `i`, (2.2) supplies a portal `p_i\in K` of `a_i` and a portal
`q_i\in J` of `t_i`.  They are nonadjacent because `K,J` are different
components of `C-X`.  Theorem 1.1 applies.  `square`

This eliminates every nonplanar three-connected member of the entire
cross-lobe support family `T\subseteq N_S(J)`; it does not assume the
minimal support `N_S(J)=\{c,t_1,t_2,t_3\}`.

### Lemma 2.2 (the cross-lobe component has order at least six)

In a nonreflecting instance of Corollary 2.1,

\[
                              |C|\ge6.                  \tag{2.3}
\]

### Proof

The cut `X` has order three and `C-X` has the two nonempty lobes `K,J`, so
`|C|>=5`.  Suppose equality holds.  Write `K={k}` and `J={j}`.  Every gate
vertex is adjacent to both `k,j`.

The neighbourhood of `C-j` is contained in

\[
                      \{j\}\cup A\cup N_S(X),           \tag{2.4}
\]

where `A={c,a_1,a_2,a_3}`.  This neighbourhood separates the nonempty set
`C-j` from the old far shore.  Seven-connectivity therefore gives

\[
                         |A\cup N_S(X)|\ge6.             \tag{2.5}
\]

Thus at least two distinct labels from `T={t_1,t_2,t_3}` have a gate
neighbour; equivalently at least two of the sets `U_i=N_X(t_i)` are
nonempty.

Put `F={i:B_i\subseteq B}`, as in Section 4 of the one-sibling funnel.  If
`F={r}`, that theorem makes every `U_i` with `i\ne r` empty, contradicting
(2.5).  If `|F|>=2`, it makes every `U_i` empty, again a contradiction.
It remains that `F` is empty.  Since `T\subseteq B` and `|B|>=4`, this
forces

\[
                             B=T\cup\{c\}.               \tag{2.6}
\]

Apply the same neighbourhood argument to `C-k`.  It gives

\[
                         |B\cup N_S(X)|\ge6,             \tag{2.7}
\]

so at least two of `W_i=N_X(a_i)` are nonempty.

In (2.6), the exact nonreflection condition (3.6) of the funnel says that
for `i\ne j`, every member of `U_i` equals every member of `W_j`.  Form the
bipartite graph between the indices of the nonempty `U`-sets and nonempty
`W`-sets, retaining the unequal-index pairs.  Every component of this
index graph forces all of its portal sets to be one common singleton.  If
both index classes have order at least two, the index graph is connected
except when both classes are the same two-set; in that exceptional case it
has exactly two one-edge components.  Consequently all nonempty sets among

\[
                         U_1,U_2,U_3,W_1,W_2,W_3         \tag{2.8}
\]

are supported on at most two vertices of `X`.  Some third gate vertex can
therefore contact no member of `S-{c}`.  It has at most two neighbours in
`X`, the two neighbours `k,j`, and possibly the one boundary neighbour
`c`; hence its degree is at most five.  This contradicts
seven-connectivity.  `square`

### Lemma 2.3 (six prescribed labels have distinct portals)

In the abstract setting of Theorem 1.1, if `|C|>=6`, the incidence graph
between

\[
                D=\{a_1,t_1,a_2,t_2,a_3,t_3\}           \tag{2.9}
\]

and `C` has a matching saturating `D`.

### Proof

If Hall fails, choose nonempty `U\subseteq D` with
`|N_C(U)|<|U|`.  Since `|C|>=6` while `|N_C(U)|<=5`, the set
`C-N_C(U)` is nonempty.  Delete

\[
                       Z=(S-U)\cup N_C(U).               \tag{2.10}
\]

Its order is `7-|U|+|N_C(U)|<7`.  A component of
`C-N_C(U)` cannot leave through a surviving member of `U`, by the
definition of `N_C(U)`; every other boundary exit was deleted, and `C` is
a component of `G-S`.  The far side (1.1) survives.  Thus `Z` is a cut of
order below seven, a contradiction.  `square`

### Corollary 2.4 (one literal alternating portal cycle)

Every nonreflecting cross-lobe instance contains on the facial cycle `F`
six pairwise distinct literal portal witnesses, one for every member of
`S-{c}`, whose duty word is, up to rotation, reversal, and renaming,

\[
                              A\ B\ D\ A\ B\ D.          \tag{2.11}
\]

### Proof

Lemmas 2.2 and 2.3 give six distinct matched portals on `F`.  For any two
duties, their four selected portals must alternate on `F`; otherwise the
two disjoint complementary subpaths of the facial cycle would be two
duty-correct carriers and Corollary 2.1 would reflect `Pi`.  Three pairs on
a circle which alternate pairwise have exactly the cyclic word (2.11).
`square`

Thus the whole cross-lobe family has reached the literal alternating-cycle
interface.  This is stronger than merely obtaining three unrelated web
completions: the cycle is an actual cycle of `C`, all six portals are
literal and distinct, and no completion edge is used.  The remaining issue
is the **orientation/state** of the three pairs, not extraction of a cyclic
packet core.

## 3. A literal reversal sublemma

The common-face conclusion should not be confused with a simultaneous
six-terminal embedding.  The following safe statement records exactly
when the familiar reversal linkage is literal.

### Lemma 3.1 (cofacial reversal)

In the setting of Corollary 2.1, suppose there are portal edges

\[
             a_i p_i\quad(p_i\in K),\qquad
             t_i q_i\quad(q_i\in J),\qquad i\in[3],      \tag{3.1}
\]

such that `p_1,p_2,p_3` are pairwise distinct and
`q_1,q_2,q_3` are pairwise distinct.  (For example, the two triples may
come from side-specific saturating matchings.)  Suppose also that the graph
obtained from `C` by attaching six new degree-one
terminal copies along these selected portal edges has a plane embedding
with the copies cofacial in the order

\[
                       a_1,a_2,a_3,t_1,t_2,t_3.          \tag{3.2}
\]

Then `C` contains three disjoint cross-lobe carriers with endpoint pairing

\[
                 a_1t_3,\qquad a_2t_2,\qquad a_3t_1.    \tag{3.3}
\]

### Proof

Let `P={p_1,p_2,p_3}` and `Q'={q_1,q_2,q_3}`.  Three-connectivity and the
set form of Menger's theorem give three vertex-disjoint `P-Q'` paths.  To
see the separator condition directly, deleting at most two vertices leaves
`C` connected and leaves at least one member of each of the two three-sets.
Every `K-J` path meets `X`.  Since the three paths are disjoint and
`|X|=3`, each uses exactly one distinct member of `X`.

Append the six terminal-copy edges.  In the disk embedding, two disjoint
paths cannot join alternating boundary pairs.  Thus the bijection from the
ordered `a`-copies to the ordered `t`-copies is strictly decreasing.
Replacing each copy edge by its corresponding literal boundary--portal
edge gives exactly (3.3).  `square`

## 4. Trust boundary and next exact implication

Theorem 1.1 uses three separate four-terminal web certificates only to
prove a common **literal face**.  It does not assert that their completion
edges agree, that all six terminal stars can be embedded simultaneously,
or that the three reversed pairs in (3.3) are equality blocks of a legally
attained colouring.

The remaining cross-lobe implication is now state-specific:

1. either interleaving portal stars on the common face give a
   label-faithful crossing which reflects an attainable permutation of
   `Pi` or regenerates a named near-`K_7` model; or
2. a simultaneous cofacial selection gives the transposition in (3.3),
   and a proper-minor/Kempe transition must attain that transposed state or
   expose one coherent two-vertex lock.

Merely contracting the three reversed carriers is not valid state
transport.  The only fixed duty in (3.3) is `B_2`, and palette colours may
not be identified with the two transposed block labels without a legal
colouring transition.
