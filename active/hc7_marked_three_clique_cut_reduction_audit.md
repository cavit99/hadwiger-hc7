# Audit of the marked three-clique cut reduction

**Verdict:** **GREEN after three local writeup corrections.**  The four-fan
decoder, binary-cut corollary, `|W|=6` elimination, `|W|<=1` balanced-cell
elimination, and the residue classification in (4.1)--(4.3) are
mathematically valid.  They do not prove the marked three-clique theorem;
the `2<=|W|<=5` equality residue remains open exactly as stated.

The audit checked the argument against the definitions and inequalities in
Niu's six-connected, claw-free three-`K_5` proof.  The present argument uses
only six-connectivity, `K_7`-minor exclusion, and the marked-six-cut
hypothesis at the two advertised replacement steps.

## 1. Four-fan decoder

Lemma 1 is correct, including when `Q` meets `S`.

Let `I=Q cap (S-z)`.  Use the trivial one-vertex paths at the members of
`I`.  In

```text
(H-z)-I,
```

which is `(5-|I|)`-connected, set-Menger gives `4-|I|` disjoint paths from
`Q-I` to `(S-z)-I`; these paths can be chosen with distinct starts and
ends.  Thus the four paths asserted in the source really can be required to
use the trivial paths at `Q cap S`.  Since every nontrivial path starts in
the component of `H-S` containing `Q-S`, shortening it at its first vertex
of `S` keeps its interior in that component.

The seven proposed bags are disjoint.  In particular, the four ends
`t_q` and the leftover boundary vertex `r` are distinct, while the two full
components and the fan component are distinct components of `H-S`.
Every claimed adjacency is literal:

* the four fan bags meet the four distinct vertices of the clique `Q`;
* `z` is adjacent to those four vertices and has a neighbour in each full
  component;
* each full component has a neighbour at every `t_q`; and
* the second full component has a neighbour at `r`, which belongs to the
  first packet bag.

The statement should say explicitly that the component containing `Q-S`
is part of the hypothesis (hence `Q-S` is nonempty).  Corollary 2 supplies
this automatically because `L_i-S` cannot be empty.

Corollary 2 is therefore green.  A six-set containing the three marks
cannot contain an entire one of the disjoint five-cliques: doing so would
also require the two other marks, using seven distinct vertices.  Hence a
chosen `L_i-S` lies in one component, and two further components trigger
Lemma 1.

## 2. The `|W|=6` branch

The Mader budget gives `|X_j|<=1` for every cell.  At most one of the three
disjoint five-cliques can lie in the six-set `W`, so at least two `A_i` are
nonempty.

There is one incorrect sentence in the current proof, but its conclusion
has a short valid replacement.  The condition `|X_j|<=1` does **not** say
that `Y_j` is a singleton or that no internal edge of `Y_j` was deleted.
Instead use the certificate condition

```text
N(Y_j-X_j) subseteq W union Y_j.
```

Thus, in `H-W`, a cell has at most the one gateway in `X_j` through which
it can attach to other cells.  Restoring the deleted internal edges of such
a cell can attach pendant material to one auxiliary component, but cannot
merge two auxiliary components meeting different named cliques.  A cell
with `X_j=emptyset` has no attachment to another cell at all.  Consequently
distinct auxiliary components meeting distinct cliques remain distinct
components of `H-W`.

If some `A_i` is empty, its whole clique lies in `W`; the other two named
auxiliary components make `W` a six-separator.  The marked-cut hypothesis
would then put the other two marks into `W`, requiring seven vertices.  If
all three `A_i` are nonempty, `H-W` has at least three components, contrary
to the binary-cut corollary.  Lemma 3 is green after replacing the flawed
singleton-cell sentence by this gateway argument.

## 3. The balanced branch for `|W|<=1`

The counting is correct.  Equality in

```text
|B_1 union B_2 union B_3| <= 3(6-|W|)
```

forces `m=6-|W|`, every large `X_j` to have order three, and their union to
equal the union of the three `B_i`.

If `A_i-B_i` is nonempty, `W union B_i` is a six-separator.  Since at most
one of the two marks with labels different from `i` can lie in `W`, that
separator cannot contain all three marks.  Hence `A_i=B_i` for all `i`.

Before invoking the symmetric-difference separator, the proof should state
the following source dependency explicitly.  For `|W|<=1` and
`|X_j|=3`, six-connectivity gives

```text
Y_j=X_j,
```

because otherwise `W union X_j` would be a separator of order at most
four.  If `|B_i cap X_j|>=2`, then

```text
W union (B_i triangle X_j)
```

has order at most five and separates the nonempty set `B_i cap X_j`
from vertices of another `B`-row outside `X_j`.  Thus every intersection
has order at most one.  Since `|B_i|=m`, every intersection has order
exactly one, proving (3.3).

### The `W=emptyset` model

For `q in L_i` in cell `X_j`, all neighbours of `q` lie in the seven-set

```text
(B_i-q) union (X_j-B_i).
```

Six-connectivity gives `d(q)>=6`.  If `d(q)=6`, then `N(q)` is a
six-separator.  For an unmarked `q`, the two other marks must therefore be
the two cross-cell vertices.  For `q=z_i`, degree six is impossible because
the separator `N(q)` omits the required mark `z_i`; hence `d(q)=7` and `q`
sees the whole envelope.  In all cases every terminal sees both cross-cell
vertices.

The possible sixth vertex of `B_i` is adjacent to `z_i`, because the latter
has degree seven and its envelope contains every other member of `B_i`.
Thus every `B_i` is connected.  The five vertices of `L_1` occupy five
different large cells, so at least one (indeed five) supplies a literal
`B_1-B_2` edge.  Every singleton of the third clique contacts both external
bags through its two cross-cell vertices.  The stated seven bags are a
literal `K_7` model.

### The `|W|=1` model

If the unique vertex `w` lies in `L_i`, absorb it into `B_i`.  The four
vertices of `L_i-w` occupy distinct cells and each sees both cross-cell
vertices by the same degree-six/degree-seven argument, so a cross-cell edge
from `B_i` to either other row exists.  Choose one such row as the second
external bag and the remaining clique as the five-singleton core.  The
second external bag is exactly its named clique.  The bag `B_i union {w}`
is connected through `L_i-w`.

For a core vertex `q`, degree seven gives both cross contacts.  At degree
six, the two external marks must be the corresponding cross-cell vertices,
except when one is `w`, in which case the edge `qw` contacts the bag that
absorbed `w`.  A marked core vertex cannot have degree six.  Hence every
core singleton contacts both external bags.  If `w` belongs to no named
clique, every `B_i` is its literal clique and the same argument works with
any cross-cell edge.  The `|W|=1` construction is green.

## 4. Residue classification

For a nonempty tail in row `i`, `W union B_i` has order six and is a
separator.  Therefore every mark outside `W` lies in `B_i`.  Since the
`A`-rows are disjoint, this forces the two marks of the other rows into
`W`; two tails force all three marks into `W`.

The claimed normal forms follow, but the counting should be expanded as
follows.

* If `|W|=2`, no-tail in all three rows would require `W` to meet three
  disjoint cliques, which is impossible.  Two tails force all three marks
  into `W`, also impossible.  Thus exactly one row has a tail.  Relabel it
  row one.  Its cut forces `W={z_2,z_3}`, and the two tail-free rows have
  `A_i=B_i=L_i-z_i`, proving (4.3).
* Let `3<=w=|W|<=5`.  A tail-free row `i` requires at least `w-1` vertices
  of `L_i` in `W`.  If the other two rows have tails, their cuts put all
  three marks in `W`, so the tail-free row plus the two marks outside its
  clique require at least `(w-1)+2>w` vertices.  If at least two rows are
  tail-free, their two disjoint cliques alone require at least
  `2(w-1)>w` vertices.  Hence all three rows have tails, and any two tails
  put all three marks in `W`.

Thus (4.1)--(4.3) are exhaustive under the standing equality assumption.

## 5. Exact remaining gap

The audit promotes only the following conditional reduction:

> In a six-connected, `K_7`-minor-free graph with three disjoint marked
> `K_5` cliques such that every six-separator contains all three marks, the
> balanced Mader equality branch is impossible for `|W|<=1`; for
> `2<=|W|<=5` it has precisely the two forms in Section 4 of the source.

It does not eliminate those two forms, prove the marked three-clique
theorem, or prove the global support-six theorem.
