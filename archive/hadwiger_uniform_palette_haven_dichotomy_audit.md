# Adversarial audit: palette haven and model-haven dichotomy

## Verdict

**GREEN.**  The palette-support lemma, private-colour haven, comparison
with the clique-model haven, Menger rank inequalities, and Rado
transversal conclusion are valid.  The theorem gives paths into model
bags, not a rooted clique model; the source note keeps this distinction
explicit.

## 1. Shore permutations

Let $X=A\cap B$, $D=A-B$, and let $C_X$ be the colours used on $X$.
A palette permutation on $D$ which fixes $C_X$ preserves every
$D$--$X$ edge: a bijection fixing a colour cannot map a different
colour to it.  It also preserves all edges inside $D$, and there are no
$D$--$(B-A)$ edges.  Thus this is a legitimate recolouring, not an
unjustified independent permutation at each vertex.

For subsets $P,Q$ of the free palette $F$, the minimum of
$|\pi(P)\cup Q|$ over palette permutations is
$\max\{|P|,|Q|\}$.  Extending an injection from the smaller set into
the larger proves the upper bound; the sizes prove the lower bound.
Hence, unless one shore uses all of $F$, the recoloured neighbourhood
of $v$ omits a colour.  Assigning that colour to $v$ is valid.

## 2. Components and haven nesting

If two private-colour roots outside $c(X)$ lay in different components
of $H-X$, use one component versus the union of all others as the two
open shores.  Each shore then misses the private colour whose unique
root is in the other shore, contradicting the palette-support lemma.
This proves that all free private roots lie in one component.

When $|X|<h$, at least one of the $h$ private colours is absent from
$c(X)$, so the component is nonempty and unique.  If $X\subseteq Y$
and $|Y|<h$, a private root whose colour is absent from $c(Y)$ lies in
both chosen components.  Since each component of $H-Y$ lies in a
component of $H-X$, the haven nesting axiom follows.  No implicit
connectivity hypothesis on $H$ is used.

The degree count is exact: if $h$ of the $r$ nonempty colour classes on
$N(v)$ are singletons, then

\[
 |N(v)|\ge h+2(r-h)=2r-h.
\]

Thus degrees seven, eight, and nine at $r=6$ give $h\ge5,4,3$.

## 3. Model haven

Deleting $p<r$ vertices meets at most $p$ of the pairwise disjoint
branch bags.  Every two untouched bags retain their original direct
cross-edge, so all untouched bags lie in one component.  If
$X\subseteq Y$, an untouched bag for $Y$ witnesses containment of the
chosen components.  This is the usual haven of order $r$ carried by a
$K_r$ model.

If the colour and model components differ at $X$, they are components
of the same graph $H-X$ and hence are genuinely separated.  Their
capacities are at least $h-|c(X)|$ private roots and $r-|X|$ untouched
bags.  This verifies the polarized branch.

For a minimum-order distinguishing set, every adhesion vertex meets both
chosen components.  If (x) missed one component, restoring only (x)
could not merge that component with the other one.  Haven nesting keeps
each old chosen component inside the corresponding new one, so the two
havens would already differ at (X-\{x\}).  Hence the minimum polarized
separator is an exact two-full-shore adhesion.

## 4. Menger and Rado

Assume the two havens agree below order $h$.  For a subfamily $J$ of
$j\le h$ bags, a failure of $j$ disjoint paths from the private roots
to their union gives, by set-Menger, a hitting set $X$ of order
$p<j$.  Endpoint vertices are allowed in $X$; this causes no problem:

* because $p<j$, at least one of the $j$ disjoint bags is completely
  disjoint from $X$ and lies in the model-haven component;
* because $p<h$, some private-root colour is absent from $c(X)$, and
  its unique root is outside $X$ in the colour-haven component.

Equality of the two components gives an $X$-avoiding path between the
two terminal sets, contradicting the hitting property.  Hence every
subfamily satisfies the gammoid rank inequality required by Rado's
matroidal transversal theorem.  Applying Rado to any prescribed $h$
bags gives distinct representatives linked from all $h$ private roots.

If $H$ is $h$-connected, two components of $H-X$ cannot differ for
$|X|<h$, so the path-transversal outcome is automatic.  Since deleting
one vertex lowers vertex connectivity by at most one, audited
seven-connectivity of an $HC_7$ counterexample gives
$\kappa(G-v)\ge6$, enough for all three low-degree rows.

## 5. Two-state gluing

The two-state gluing theorem is also sound.  Equality of the boundary
partitions is exactly what is required to align the two restrictions by
one palette permutation.  On the shore opposite a colouring's haven,
no private colour outside the boundary palette can occur: its unique
neighbourhood root lies in the haven component.  Hence the hybrid made
from the two nondominant shores uses at most

\[
 |c(X)|+\mu(c)+\mu(d)
\]

neighbourhood colours.  For exact one-block traces both nonprivate-colour
counts equal one, so an adhesion using at most $r-3$ colours cannot carry
the same boundary state with opposite orientations.

## 6. Exact limitation

The Rado linkage may enter one old branch bag on its way to another.
Absorbing such a path can disconnect or steal a uniquely necessary
portal from the transit bag.  Therefore the theorem does **not** prove
an $N(v)$-meeting model.  Truncation at first model hits gives only the
audited trichotomy: clean distinct target hits, an exchange hit, or a
multiply hit bag.  A label-preserving bag split is still required in
the last two cases.

This limitation is structural rather than a flaw in the palette or
gammoid proof.
