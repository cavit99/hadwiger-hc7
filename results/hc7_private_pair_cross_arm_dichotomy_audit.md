# Independent audit: private-pair cross-arm dichotomy

**Verdict:** **GREEN after a necessary graph-specific correction.**

The original abstract set-family statement was **RED** in the `5/5`
case.  The corrected theorem defines arms using the exact separated-support
bound and proves their nonemptiness from the `HC_7` host hypotheses.  All
size combinations, the collapse alternative, the forced replacements, and
the claimed exclusivity are valid in that corrected form.

## 1. The defect in the original statement

The old arm definition required only `|A cap B|<=4`.  This is the separated
bound when at least one of `A,B` has order six, but not when both have order
five: two five-sets are separated only when their intersection has order at
most three.  Therefore the old proof step

> a non-near-identical cross-pair, together with the two bounds in the arm
> definition, is a separated triple

was false.

There is a direct abstract counterexample.  Let

\[
 A=\{1,2,3,4,5\},\qquad P=\{p,q\},
\]

include all five sets

\[
 B_a=(A-\{a\})\cup\{p\}\quad(a\in A),
\]

and include one five-set `C` containing `q` and otherwise disjoint from
`A union {p}`.  Put

\[
                 \mathcal F=\{A,C\}\cup\{B_a:a\in A\}.
\]

Then `P` meets every member except `A`, and `tau(F)>2`:

* a set avoiding `A` misses `A`;
* a pair containing `a in A` and `p` misses `C`;
* a pair containing `a in A` and `q` misses `B_a`; and
* every other pair containing a vertex of `A` is missed by either `C` or
  the corresponding `B_a`.

Under the old definition both arm families were nonempty.  Every `B_a`
met `A` in four vertices, so no triple through `A` was separated, while
the `p`-arm family was not a singleton common-core family.  Thus neither
old outcome held.  The old conclusion `A cap X=emptyset` for `|A|=5`
depended on the same invalid step.

## 2. Exact corrected arm bounds

The corrected families require

\[
 |A\cap D|\le \max\{|A|,|D|\}-2.
\]

The four relevant size calculations are:

| `|A|` | `|D|` | separated upper bound |
|---:|---:|---:|
| 5 | 5 | 3 |
| 5 | 6 | 4 |
| 6 | 5 | 4 |
| 6 | 6 | 4 |

With these exact bounds, a non-near-identical cross-pair really does form
a separated triple with `A`.

## 3. Nonemptiness of both corrected arm families

For every `a in A`, nontransversality of `{q,a}` gives a support `D_a`
avoiding that pair.  It is not `A`, and the private-pair property therefore
forces exact trace `P cap D_a={p}`.

If `|A|=5` and none of these witnesses is separated from `A`, every
`D_a` must have order five and equal `(A-{a}) union {p}`.  Together with
`A`, these are all five-subsets of `A union {p}`.  Each is a literal
`K_5`, so every pair of vertices in the six-set is an edge and that six-set
is a literal `K_6`.  Seven-connectivity then supplies a seventh branch set,
contrary to `K_7`-minor-freeness.

If `|A|=6`, a witness of order five contains `p outside A` and hence meets
`A` in at most four vertices, so it is already separated.  If every
witness is nonseparated, all have order six and are exactly
`(A-{a}) union {p}`.  Thus every six-subset of `A union {p}` supports a
`K_5` model.  The audited full-seven-point-family lemma gives a `K_6`
model on that seven-set, and seven-connectivity again lifts it to `K_7`.

Consequently the corrected `p`-arm family is nonempty.  The symmetric
argument proves nonemptiness of the `q`-arm family.  This step is stronger
than the cited V-extraction theorem: V-extraction alone only guarantees
intersection at most four and therefore does not by itself settle the
`5/5` case.

## 4. Cross-arm collapse and exclusivity

Assume every corrected `p`-arm is near-identical to every corrected
`q`-arm.  A cross-pair cannot have orders five and six, because
near-identity would contain the five-set in the six-set, whereas the exact
traces force `p` into only the `p`-arm and `q` into only the `q`-arm.

For equal order `k`, the exclusive vertices `p,q` bound the intersection
by `k-1`; near-identity gives equality.  Hence the pair is
`X union {p}`, `X union {q}` for one `(k-1)`-set `X`.  Comparing any other
arm with the fixed opposite arm forces the same order and the same core,
so each corrected arm family is a singleton.

The two alternatives are genuinely exclusive.  In the collapse outcome
the sole cross-pair meets in `k-1` vertices and is near-identical, whereas
the separated-triple outcome requires a cross-pair meeting in at most
`k-2` vertices.

## 5. Forced replacements in every size case

Let `a in A cap X` and choose a support `D_a` avoiding `{q,a}`.  Again it
has exact trace `{p}`.  If it were separated from `A`, singleton collapse
would make it the arm `X union {p}`, which contains `a`, a contradiction.
It is therefore nonseparated.

The possibilities are then forced:

* if `|A|=5`, an order-six witness avoiding `a` would meet `A` in at most
  four vertices and be separated; hence `|D_a|=5`, its intersection with
  `A` has order four, and `D_a=(A-{a}) union {p}`;
* if `|A|=6`, an order-five witness containing `p outside A` meets `A` in
  at most four vertices and is separated; hence `|D_a|=6`, its intersection
  with `A` has order five, and the same displayed formula holds.

Interchanging `p,q` gives both forced replacements.  In particular, the
correct size-five conclusion is the replacement family, not the original
claim that `A cap X` must be empty.

## 6. HC7 application and trust boundary

For a private pair in a three-critical support kernel, the bounded-kernel
theorem supplies the private pair and `tau(F)>2`; disjointness from `A`
follows because otherwise the pair would meet the whole family.  The
corrected theorem itself, using the graph-specific top-family exclusions,
supplies both nonempty genuinely separated arm families.  It is therefore
valid to apply the corrected dichotomy to every such private pair.

The theorem remains only an extraction result.  It neither aligns the
split edge-bags of the three models nor composes the common-core outcome
into a `K_7`.  No stronger conclusion is certified by this audit.
