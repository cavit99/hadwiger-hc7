# Independent audit: spanning `K_7^vee` `Q`-full normalization

## Verdict

**GREEN.**  No spanning, contraction, proper-view, clique-extension, or
model-lifting defect was found.  The only changes requested were
convention-sensitive wording in Lemma 6.1 and clarification of which
one-complex label remains possible; both are now patched in the source.

## 0. Spanning extension

Lemma 0.1 is valid.  Every component of the induced graph outside the
old model union has an edge to that union because the host is connected.
Assigning the entire component to one incident branch bag preserves
connectedness, disjointness and every old model adjacency.  Distinct
outside components are disjoint, so all assignments can be made
simultaneously.  No edge deletion or contraction claim is hidden here:
this is an enlargement of the branch sets witnessing the same minor.

## 1. Six contractions and the retained bag

The original seven branch bags form a spanning partition.  Contracting a
spanning tree inside each of the six bags other than the selected bag `X`
therefore leaves exactly six singleton images plus the uncontracted
connected vertex set `X`; there are no unaccounted outside vertices.
Every required model edge survives.  The three selected neutral images
form a triangle, and each of the other three singleton images is adjacent
to all of them because the only possibly missing model pairs are `AB` and
`AC`.  The retained bag is collectively adjacent to the neutral triangle.
Extra `AB` or `AC` edges only add quotient edges and do not invalidate the
argument.

## 2. Maximal `Q`-full refinement

The one-part partition of `X` is `Q`-full, so a finest finite partition
into connected `Q`-full parts exists.  A `K_4` minor in its quotient lifts
to four disjoint connected unions of parts, all adjacent to the neutral
triangle, and hence to a literal `K_7` model in the normalized minor and
in the original graph.  In the target-free branch every quotient is
therefore `K_4`-minor-free and has treewidth at most two.

The sixteen choices are counted correctly: four choices of the omitted
neutral label and four choices of the retained complementary bag.  Every
original branch bag is retained in at least one normalization.  The note
correctly warns that the sixteen normalized minors have different
contraction maps, so their quotient cuts and colouring states cannot be
spliced without an additional transport theorem.

## 3. Convention-sensitive wording

The current text uses the corrected formulation that no 3-connected
block of order at least four occurs; this avoids calling a triangle
3-connected under a convention which requires more than three vertices.

## 4. Proper-view count

Lemma 5.1 counts the sixteen views correctly.  If two original bags are
complex, every retained-bag choice contracts an edge in at least one of
the other six bags, so every normalized graph has strictly fewer
vertices.  If exactly one bag is complex, precisely the views retaining
it can be the identity: four views when its label is `A`, `B`, or `C`,
and one view when it is a fixed neutral `U_j`.  All other views are proper
minors.

If every original bag is a singleton, spanningness gives exactly seven
vertices.  Target-freeness excludes both deficient edges being present;
coloring the ends of an absent edge alike and the other five vertices
distinctly gives a six-coloring.  Thus the all-singleton architecture
cannot occur in a non-six-colorable target-free graph.

## 5. Clique-extension closure and labels

Under the standard convention that a `k`-connected graph has at least
`k+1` vertices, Lemma 6.1 is correct.  For a `(k-1)`-clique `S`, the set
`D=G-S` is nonempty and connected.  For every `s in S`, connectivity of
`G-(S-{s})` forces an edge from `s` to `D`.  Hence `D` plus the
`k-1` singleton clique vertices is a literal `K_k` model.  The source now
states `k>=2` and the order convention explicitly.

If `A` were the sole complex bag of the spanning `K_7^vee` model, the
six singleton bags `B,C,U_1,...,U_4` induce a `K_6`, since the only
non-required pairs are `AB` and `AC`.  Seven-connectivity and Lemma 6.1
then force `K_7`.  Thus the sole complex label can only be `B`, `C`, or
a neutral label.  For complex `B` (respectively `C`), the other six
singletons induce `K_6^-` with missing pair `AC` (respectively `AB`), so
calling the complex bag unaffected in the resulting `K_7^-` view is
label-correct.
