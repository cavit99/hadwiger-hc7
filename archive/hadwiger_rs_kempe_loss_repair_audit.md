# Robertson--Seymour loss versus Kempe repair

## 1. The exact cited theorem

Proposition 3.3 of *Colorful Minors* (its Proposition
`prop_linkaclique`, quoted from Robertson--Seymour, Graph Minors XIII)
has the following parameters.  There is a root set (Z) of size (k)
and a family of (p\ge \lfloor 3k/2\rfloor) pairwise disjoint
near-clique pieces.  Under the stated no-separation condition it returns

\[
 p'=p-\left\lfloor {k-h\over2}\right\rfloor\ge k
\]

disjoint connected pieces, exactly (k) of which contain one root.
Every nonadjacent pair in the output consists of two rooted pieces.
The theorem statement does **not** say that these remaining nonedges
form a matching.

This has two immediate limitations for the present application.

* A (K_r)-model can be fed to the theorem with (k) roots only when
  (r\ge\lfloor 3k/2\rfloor).  In particular a (K_6)-model and the
  five private roots of the degree-seven (HC_7) trace do not meet the
  hypothesis.
* Even when it applies, the printed conclusion is a rooted near-clique,
  not a rooted clique.  The loss is not removed by the proposition
  itself.

## 2. What critical colouring really gives

Let (G) be non-(r)-colourable, let (H=G-v), and let (c) be a
proper (r)-colouring of (H).  Suppose (x,y\in N(v)) are the unique
vertices of (N(v)) of their respective colours (a,b).  Then (x)
and (y) lie in the same component of (H[c^{-1}(\{a,b\})]).

Indeed, otherwise interchange (a,b) in the bichromatic component
containing (x).  Colour (a) then disappears from (N(v)), so (v)
can receive (a), a contradiction.  Moreover, bichromatic paths for
vertex-disjoint pairs of private roots can be chosen mutually disjoint:
their colour pairs are disjoint, hence so are the vertex sets in which
the paths lie.

Thus Kempe theory supplies exactly the *pairwise-disjoint matching
paths* suggested by the (\lfloor(k-h)/2\rfloor) loss.

## 3. The valid no-loss repair lemma

The following elementary lemma isolates the extra property actually
needed.

**Clean matching repair lemma.**  Let
(A_1,\ldots,A_s) be pairwise disjoint connected branch sets, each
containing a prescribed root (z_i).  Suppose their missing-adjacency
graph is a matching (M).  For each (ij\in M), suppose there is a
(z_i)-(z_j) path (P_{ij}) such that

1. the interiors of the (P_{ij}) are mutually disjoint; and
2. (P_{ij}-\{z_i,z_j\}) avoids every (A_\ell).

Then the roots support a rooted (K_s)-model.

**Proof.**  On each (P_{ij}), choose one edge as a dividing edge.
Adjoin the initial segment before this edge to (A_i) and the terminal
segment after it to (A_j).  The enlarged branch sets remain connected
and pairwise disjoint.  The dividing edge supplies the formerly missing
adjacency.  Since (M) is a matching, these enlargements are compatible,
and all old adjacencies remain.  \(\square\)

The same proof permits several paths incident with one root if all
their interiors are disjoint and are assigned on the appropriate side
of a dividing edge.  The matching formulation is the one supplied
automatically by disjoint colour pairs.

## 4. Why the proposed automatic repair fails at the present point

Kempe paths are disjoint from one another for disjoint colour pairs,
but they are not automatically disjoint from the clique-model bags.
They may enter one bag, leave it, transit through further bags, and only
then reach the other root.  Splitting such a path does not preserve
branch-set disjointness.  First-hit truncation merely recreates the
collision that the Robertson--Seymour loss accounts for.

This is not a cosmetic concern.  Two independently verified examples
in this workspace show the exact obstruction.

* `hadwiger_linkage_model_cleaning_counterexample.md` gives an infinite
  end-locked comb in which even a full transversal linkage transits
  model bags and cannot be cleaned to a rooted clique.
* `hadwiger_same_haven_cleaning_counterexample.md` gives a 5-connected
  graph in which the palette and model havens agree for every cut below
  order five and a full transversal reaches a (K_5)-model, but there
  is no rooted (K_5).  The exhaustive certificate is
  `verify_icosahedron_haven_cleaning_counterexample.py`.

The second example does not satisfy all-colourings apex saturation, so
it does not refute a theorem using full contraction-criticality.  It
does refute any attempt to deduce model-clean Kempe paths merely from
one-colouring haven agreement plus Rado linkage.

## 5. Precise surviving target

The Robertson--Seymour idea becomes a genuine no-loss theorem if one
can prove the following additional statement in the minor-critical
apex setting:

> For the root pairs created by the pairing step, their bichromatic
> Kempe paths can be chosen so that their interiors avoid every
> surviving branch set other than the two rooted endpoint pieces.

Call this the **model-clean Kempe matching lemma**.  The clean matching
repair lemma would then remove every paired loss.  But neither private
colours, ordinary connectivity, haven equality, nor a full Rado
transversal proves this statement.  Any proof must use the family of
colourings of all proper contractions/deletions, or an equivalent
minor-critical exchange axiom.

Accordingly, Proposition 3.3 does not presently close the (HC_7)
cell.  It identifies a sharply formulated exchange target, while the
counterexamples delimit the hypotheses that cannot prove it.
