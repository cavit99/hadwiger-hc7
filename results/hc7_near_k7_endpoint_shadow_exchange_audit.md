# Independent audit: endpoint shadow exchange

## Verdict

**GREEN.**  The exchange is a literal repartition of branch sets and the
new quotient has exactly the required `K_7^vee` edges.  In the
deficient-first comparison class it proves that a repaired one-missing
transport cannot retain a nontrivial normalized path core.

## 1. A safe endpoint always exists

Let `P=p_0...p_m` with `m>=1`, and let `R_E=N_P(E)` be nonempty.  If
`R_E` has a member other than `p_0`, deletion of `p_0` retains an
`E`-edge.  Otherwise `R_E={p_0}`, and deletion of the distinct endpoint
`p_m` retains that edge.  Thus the proof does not assume two `E` portals
or an interior `E` portal.

## 2. Connectedness and disjointness

If `x=p_0`, the residual `P'=p_1...p_m` is nonempty and connected.  The
enlarged bag `U_1'=U_1 union {p_0}` is connected through an actual
`p_0U_1` edge.  Moving the whole singleton `p_0` preserves disjointness;
no vertex is duplicated.  The edge `p_0p_1` is now a literal edge
between `U_1'` and `P'`.  The argument at `p_m` is symmetric.

## 3. Exact quotient adjacencies

In the left-end operation, use foreign bags

\[
                    D,U_2,E,U_1',U_3,U_4.
\]

They remain a clique model because all six old foreign bags were
pairwise adjacent and no old foreign vertex was removed.  The residual
path has literal edges to

* `U_1'`, through `p_1p_0`;
* `U_3,U_4`, at the retained endpoint `p_m`; and
* `E`, by the safe-endpoint choice.

These are the four prescribed spokes of `K_7^vee`.  The old missing pair
`P'D` remains absent because `P' subseteq P`, while `P'U_2` is legitimately
left unprescribed.  It is harmless if an additional `P'U_2` edge exists:
a model may contain edges beyond the target graph.  No adjacency is
inferred from a palette colour or a contracted bag.

## 4. Minimality comparison

Deficient-first normalization minimizes the first coordinate over all
labelled, not necessarily spanning `K_7^vee` models.  The comparison may
therefore use a foreign bag enlarged earlier by a transported exterior
piece, and it may relabel the two unprescribed twins as `D,U_2` (or
`D,U_4` at the other endpoint).  The new deficient bag has order exactly
`|P|-1`, so later lexicographic coordinates are irrelevant.

After wholesale transfer and omission of path-private lobes, every old
endpoint edge remains literal and every transferred piece stays in one
foreign bag.  Hence the theorem applies to precisely the one-missing
path model cited in the corollary.

## 5. Scope

The result does not apply when both old twins remain anticomplete to the
path: deleting one endpoint can leave those two missing spokes plus the
unabsorbed endpoint row, which is not a `K_7^vee` model.  It also does not
make the six foreign bags singleton.  The exact new conclusion is:

\[
 \boxed{\text{nontrivial deficient-minimal path}\Longrightarrow
        \text{both original twins remain missing}.}
\]

Within that scope, no connectivity assumption and no computational
casework is used.

For the exterior corollary, the target-free hypothesis is essential to
the wording.  If the path or one connected `P`-lobe meets both old twins,
that connected set meets all six foreign bags and gives `K_7` directly.
If it meets exactly one twin, the other is genuinely anticomplete and
Theorem 1 applies after absorbing the lobe into the contacted twin.  Thus
the corrected conclusion is the dichotomy `K_7`, or genuine
two-missingness of the nontrivial path and every incident exterior lobe.

## 6. Uniform inequality

For an endpoint `x`, the rows lost on deleting it are exactly those with
literal portal set `{x}`.  If there are no such rows, deletion alone is
valid.  Otherwise absorbing `x` into one exclusively owned row restores
that row through the endpoint path edge, so precisely `|X_x|-1` new
spokes can be lost.  Adding the `q` already absent spokes proves the
threshold `q+|X_x|-1<=d` with no hidden overlap, because an absent row has
empty portal set and is not in `X_x`.

In a minimal model the strict negation is `|X_x|>=d-q+2`.  The exclusive
sets of distinct endpoints are disjoint, and all lie among the `s-q`
contacted rows, yielding `2(d-q+2)<=s-q`.  At `(s,d,q)=(6,2,1)` this is
false, while at `(6,2,2)` equality forces the exact disjoint `2+2`
endpoint bundles.  The uniform statement is therefore GREEN as well.
