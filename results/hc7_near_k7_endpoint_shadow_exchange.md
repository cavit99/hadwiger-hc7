# Endpoint shadow exchange in the one-missing path branch

## Status

This is a label-preserving exchange on the normalized deficient path.  It
eliminates the whole nontrivial path-interface branch once coherent
transport has repaired one of the two initially missing spokes.

The point is that a `K_7^vee` model is allowed two missing spokes at its
deficient bag.  A one-missing model has one unit of deficiency in reserve.
Deleting an endpoint of the normalized `2+2` portal path can lose the
other endpoint row, but absorbing the endpoint into its twin row restores
one of the two contacts.  The fixed old missing row and the unabsorbed
endpoint row are then precisely the two permitted shadows.

This does not singletonize the six foreign bags and therefore does not by
itself prove `HC_7`.

## Setting

Let

\[
                 P,D,E,U_1,U_2,U_3,U_4
\]

be a labelled, not necessarily spanning, near-`K_7` model.  The six
foreign bags are connected, pairwise disjoint and pairwise adjacent.
The deficient bag is the induced path

\[
                         P=p_0p_1\cdots p_m .             \tag{1.1}
\]

Assume:

1. `P` is anticomplete to `D` and adjacent to `E`;
2. `p_0` has literal edges to `U_1,U_2`;
3. `p_m` has literal edges to `U_3,U_4`.

No uniqueness is required in items 2--3: the `U_i` may have additional
portals on `P`, and `E` may meet `P` arbitrarily.

## Theorem 1 (endpoint shadow exchange)

If `m>=1`, the graph has a labelled `K_7^vee` model whose deficient bag
has order `m`, strictly smaller than `P`.

### Proof

Because `P` meets `E` and has at least two vertices, one of its endpoints
can be deleted while retaining an `E`-portal.  More explicitly, if
`P-p_0` meets `E`, choose `x=p_0`; otherwise every `P-E` edge has its
`P`-end at `p_0`, and choosing `x=p_m` leaves `p_0` and hence retains an
`E`-portal.  Put

\[
                         P'=P-x .                         \tag{1.2}
\]

Thus `P'` is a nonempty connected path, remains anticomplete to `D`, and
is adjacent to `E`.

Suppose first that `x=p_0`.  Absorb `x` into `U_1`:

\[
                         U_1'=U_1\cup\{p_0\}.             \tag{1.3}
\]

The new bag is connected through the literal `p_0U_1` edge.  The cut
edge `p_0p_1` makes `P'` adjacent to `U_1'`.  The path `P'` retains its
literal contacts at `p_m` to `U_3,U_4`, and it retains an `E`-contact by
the choice of `x`.  It remains anticomplete to `D`.  Its contact with
`U_2` is immaterial: regard `D,U_2` as the two unprescribed twins of the
new deficient bag.

The six foreign bags

\[
                         D,U_2,E,U_1',U_3,U_4             \tag{1.4}
\]

are connected, pairwise disjoint and pairwise adjacent.  Indeed all old
foreign--foreign edges survive, and enlarging `U_1` cannot destroy any
of them.  The deficient bag `P'` is adjacent to the four prescribed
foreign bags `E,U_1',U_3,U_4`.  Hence (1.4), together with `P'`, is a
labelled `K_7^vee` model.  Its deficient bag has order `|P|-1=m`.

If `x=p_m`, the symmetric operation absorbs `p_m` into `U_3`, uses the
cut edge `p_{m-1}p_m`, retains the `p_0U_1,p_0U_2` contacts, and regards
`D,U_4` as the two unprescribed twins.  This gives the same conclusion.
\(\square\)

## Corollary 2 (one-missing normalized path is a singleton)

Start with a deficient-first lexicographically minimal `K_7^vee` model
from `hc7_near_k7_deficient_path_normalization.md`.  Perform coherent
transport and any whole-piece transfers, and then omit every path-private
lobe.  If the resulting nonspanning model has one repaired twin `E` and
one fixed missed twin `D`, then the normalized path core has one vertex.

### Proof

All operations leave the original endpoint vertices and their four
literal endpoint-row edges in their old bags.  Enlarging a foreign bag by
transported pieces is allowed in the comparison class of all
nonspanning labelled `K_7^vee` models.  If the path had at least two
vertices, Theorem 1 would give another such model with a strictly smaller
deficient bag, contradicting the first coordinate of the original
deficient-first minimization.  \(\square\)

## Uniform missing-star form

The exchange is not peculiar to seven bags.  The following form isolates
the exact deficiency budget.

### Theorem 3 (uniform endpoint-deficiency inequality)

Let `F_1,...,F_s` be pairwise disjoint connected pairwise adjacent
foreign bags and let `P=p_0...p_m`, `m>=1`, be a disjoint path bag.  Put

\[
 R_i=N_P(F_i),\qquad
 M=\{i:R_i=\varnothing\},\qquad q=|M|.                 \tag{3.1}
\]

Suppose models with at most `d` missing `P-F_i` spokes are admissible,
where `q<=d`.  For an endpoint `x` put

\[
                 X_x=\{i:R_i=\{x\}\}.                  \tag{3.2}
\]

If `X_x` is empty, the path bag can be shortened at `x`.  If `X_x` is
nonempty and

\[
                         q+|X_x|-1\le d,                \tag{3.3}
\]

the path bag can again be shortened at `x`, by absorbing `x` into any
`F_h` with `h in X_x`.

Consequently, in a deficient-bag-minimal path model, both endpoints obey

\[
                       |X_x|\ge d-q+2.                  \tag{3.4}
\]

The two endpoint sets are disjoint, and hence a necessary numerical
condition for a nontrivial minimal path is

\[
                       2(d-q+2)\le s-q.                 \tag{3.5}
\]

#### Proof

If `X_x` is empty, deleting `x` loses no foreign-row contact: every row
met at `x` has another portal on `P-x`.  The residual path is nonempty
and connected, so this is a smaller admissible model.

Suppose `X_x` is nonempty and choose `h in X_x`.  Move `x` from `P` into
`F_h`.  The enlarged row is connected through an actual `xF_h` edge,
and the endpoint path edge makes it adjacent to `P-x`.  Every row outside
`M union X_x` retains an old portal on `P-x`.  The only potentially
missing spokes are therefore the old `q` rows in `M` and the
`|X_x|-1` rows of `X_x-{h}`.  The foreign bags remain a clique model.
Under (3.3), this is an admissible model with a smaller path bag.

Minimality excludes both shortening cases.  Negating (3.3) gives (3.4).
For distinct endpoints, a nonempty portal set cannot equal both endpoint
singletons, so their `X_x` sets are disjoint.  They use contacted rows,
of which there are `s-q`; summing (3.4) proves (3.5). \(\square\)

For `K_7^vee`, `s=6,d=2`.  If exactly one spoke is missing, (3.5) would
read `6<=5`, which is impossible; this recovers Theorem 1 without even
choosing the repaired row explicitly.  If exactly two spokes are missing,
(3.5) is the equality `4<=4`: every contacted row is forced into one of
two disjoint two-row endpoint bundles.  Thus the audited `2+2` path is
the sharp equality cell of a parameter-uniform deficiency inequality,
not a Moser-specific configuration.

## Corollary 4 (nontrivial target-free paths have a genuinely two-missing exterior)

Let `P,B,C,U_1,...,U_4` be the deficient-first minimal nonspanning model
before coherent transport, suppose `|P|>=2`, and assume that the host has
no `K_7` minor.  Then:

1. `P` is anticomplete to both `B` and `C`; and
2. every component `K` outside the model union which meets `P` is
   anticomplete to both `B` and `C`.

Consequently coherent transport leaves **both** original twins missing;
the fixed-one-missing alternative occurs only when the deficient core is
a singleton.

### Proof

If `P` met both twins, the seven old bags would already be a `K_7` model.
If it met exactly one twin, call it `E`, while the other anticomplete twin
is `D`; Theorem 1 would immediately contradict deficient-first
minimality.  Thus it meets neither.

Now let an exterior component `K` meet `P`.  If it met both `B,C`, then
the connected bag `P union K`, together with the six old foreign bags,
would be a `K_7` model.  If it met, say, `B` but not `C`, replace `B` by
`B'=B union K`.  This is connected through the `KB` edge, remains
disjoint from the other model bags, and retains every old
foreign--foreign adjacency.  The old `PK` edge is now a literal `PB'`
edge, while `P` remains anticomplete to `C`.  Thus the same path model has
one repaired twin `B'` and one fixed missed twin `C`.  Theorem 1 again
produces a smaller deficient bag, a contradiction.  The argument with
`B,C` interchanged is symmetric.  Distinct exterior components are
irrelevant because the comparison model may omit all unused vertices.
\(\square\)

In a seven-connected host, every such exterior component therefore has
an order-at-least-seven adhesion contained in

\[
                      V(P)\cup U_1\cup U_2\cup U_3\cup U_4. \tag{3.1}
\]

This is a substantially narrower interface than the previous coherent
transport conclusion: no nontrivial path lobe can use either potential
apex bag.

## Exact residual

The ordered path-portal corridor is therefore not a terminal obstruction
in the one-missing branch.  Its only deficient-minimal realization has a
singleton deficient bag.  The remaining problem is now wholly in the six
foreign bags: one must either singletonize/split those bags, obtain a
literal `K_7`, splice compatible proper-minor boundary states, or prove
one coherent two-apex expansion.

The both-missing branch is untouched.  There is no spare missing spoke
there, so the same endpoint move can create a third absent adjacency and
need not preserve a `K_7^vee` model.
