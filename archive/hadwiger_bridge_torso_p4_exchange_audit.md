# Adversarial audit of the bridge--torso `P4` exchange

Date: 2026-07-12

Audited file: `hadwiger_bridge_torso_p4_exchange.md`

## Overall verdict

**GREEN after repairs** for the precise static results in Theorem 2.1,
Corollary 2.2, Theorem 3.1, and Lemma 4.1, under the hypotheses now
stated in the file.

**RED** for either of the following stronger readings:

1. that the note supplies the missing dynamic warehouse exchange; or
2. that the example in Section 5 is `K_7`-minor-free.

The note proves a useful block-level reduction, not `HC_7`.  Its last
dynamic step remains explicitly open.

## 1. Theorem 2.1: branch-set audit

### Item 1: GREEN

Write

\[
 P=A\cup X,\qquad Q=D\cup B_y,\qquad R=Y.
\]

The displayed sets and the remaining old bags are pairwise disjoint.
Their connectivity and adjacencies are all justified:

* `P` is connected by the `A-X` edge and `Q` by the `D-B_y` edge;
* `PQ` is supplied by `X-B_y`, since `y in M` and `X` is an A-arm;
* `PR` is `X-Y`;
* `P-B_j` is supplied by `A` for `j in I_A` and by `X` for `j in M`;
* `Q-R` and `R-B_j` follow from `Lambda(X)=emptyset`;
* `Q-B_j` and every remaining pair are old clique-model adjacencies.

No contraction is being used in a direction that could lose an
adjacency.

### Item 2: GREEN

When `Lambda(X)={j}`, every old `B_x-B_j` edge has its `B_x` endpoint
in `X`, so `B_j union X` is connected.  It sees `Y` through `X-Y` and
all other bags through `B_j`.  The bag `Y` sees every old bag except
possibly `B_j`, and its adjacency to the enlarged `j`-bag is again
`X-Y`.  The fixed roots `u_x` and `u_j` remain in their named bags.

The `A`-contact potential is computed correctly: `A-u_x` prevents loss
of label `x`, old contacts in every other unchanged bag persist, and
moving `X` adds `j` exactly when `j in M`.

### Lexicographic domain: GREEN after repair

The admissible-model domain consists of rooted models on the same
union whose `x`-bag is anticomplete to `D`.  The rotation preserves:

* the union;
* all named roots;
* disjointness and connectivity of the bags; and
* the `D-B_x` defect, because the new `x`-bag is the subset `Y`.

The original proof wording tacitly reused the initially selected label
`y` after optimizing the model.  That label need not remain outside
the optimized `A`-contact set.  The repaired proof does not need it.
If the optimized contact set is proper, choose any `h in M`.  For an
empty-monopoly A-arm, moving `X` into `B_h` is a valid rooted-model
rotation and strictly enlarges `I_A`.  A singleton monopoly is handled
by item 2.  If `M` is empty, `A,B_1,...,B_m` is already the obvious
clique model.  Thus every surviving A-arm has at least two monopoly
labels.

This repair retains the advertised label-free scope; no additional
root-cover hypothesis is needed for the potential argument.

## 2. Corollary 2.2: GREEN after one necessary qualification

If `u_xu_j` is an edge, then `u_x in Y` supplies a `Y-B_j` edge, so
`j` cannot be monopolized by `X`.  Hence

\[
                         \Lambda(X)\subseteq\Delta_x
\]

is correct.

The original prose inferred `|Delta_x|>=2` without saying that an
A-arm exists.  That inference is false when there is no A-arm; a
singleton `x`-bag is the simplest counterexample.  The file now states
the existential qualification.  In the `C_5` row, any actual A-arm
therefore monopolizes both root-defect labels.

## 3. Theorem 3.1: GREEN

The root convention for the block--cutvertex tree is now unambiguous:
root at the cutvertex node if `u_x` is a cutvertex, and otherwise at
its unique block node.

The lobe family is laminar.  Demand-completeness is upward-closed under
lobe containment, because all witnessing edges of a smaller lobe
remain in a larger one.  Therefore distinct inclusion-minimal
demand-complete lobes are incomparable and disjoint.

For a monopoly label `j`, the nonempty set of all `B_x` endpoints of
old `B_x-B_j` edges is contained in the lobe.  Two disjoint lobes
cannot both contain that set.  Their monopoly sets are consequently
pairwise disjoint.  Since every one has size at least two and lies in
`Delta_x`, the bound

\[
            \#\{\text{minimal warehouse lobes}\}
            \le \left\lfloor |\Delta_x|/2\right\rfloor
\]

is valid.  Finite descent proves that every demand-complete lobe
contains a minimal one.

Scope qualification: this controls demand-complete rooted block lobes,
not arbitrary detachable subsets or 2-separations.  The constant-two
interpretation is valid for `m=5`; for general `m` only the displayed
`floor(|Delta_x|/2)` bound is proved.  Both qualifications are now
explicit.

## 4. Lemma 4.1: GREEN under its explicit spanning hypothesis

The needed hypotheses are exactly:

* the seven pairwise disjoint pieces `A,D,B_1,...,B_5` span `H=G-v`;
* `D` is anticomplete to `B_x`;
* `u_x` is the only neighbour of `v` in `B_x`; and
* `G` is seven-connected.

For a non-root lobe `K` attached at `q`, induced connectivity of
`H[B_x]` gives `N_G(K) intersect B_x subseteq {q}`.  The other two
hypotheses make `K` anticomplete to `D union {v}`.  Spanning then gives

\[
 N_G(K)\subseteq \{q\}\cup A\cup\bigcup_{j\ne x}B_j.
\]

The open neighbourhood separates nonempty `K` from `v`, so
seven-connectivity forces at least seven neighbours.  At most one is
`q`; hence the five external pieces contain at least six distinct
neighbours, and one is multiply hit.

The lemma does **not** prove that every initial rooted model can be
enlarged to such a spanning partition while retaining the defects.
The file now states that this is an assumption rather than a derived
fact.

## 5. Section 5 counterexample: GREEN, with a decisive caveat

The construction was checked both directly and with NetworkX.  It has
17 vertices before adding `v`, 102 edges, and

\[
                         \kappa(H)=7.
\]

A minimum cut returned by the independent computation is the six
vertices of `C_3 union C_4 union C_5` together with `u`, agreeing with
the hand proof.  After adjoining `v` to the seven specified roots,
`G` is also exactly seven-connected: fewer than seven deletions leave
`H` connected and, when `v` remains, leave it at least one neighbour.

For `x=1,y=2`, an arm satisfying the asymmetric Lemma 2.4 conditions
would have to contain `p` to meet `A` and `q` to meet `B_2`.  The only
`p-q` path in `B_1` contains the fixed root `u`, which must stay in the
other half.  No such arm exists.

However, `C` induces `K_8`.  The example is therefore not
`K_7`-minor-free and is not a counterexample to a splitter using the
full Hadwiger-counterexample hypotheses.  It proves only that
seven-connectivity, the sharp contact support, and portal multiplicity
alone do not force the split.  This caveat is now explicit in the
source note.

## 6. What remains

The audited result leaves exactly a block-level dichotomy:

* no demand-complete non-root lobe, placing the co-location problem in
  the root torso; or
* at most `floor(|Delta_x|/2)` minimal warehouse lobes, each charging
  at least two root defects and, under Lemma 4.1, at least six external
  portal vertices.

It supplies neither the proposed two-path/SPQR exchange in the root
torso nor the minor-transition exchange inside a warehouse.  Those are
the genuine theorem-strength gaps.
