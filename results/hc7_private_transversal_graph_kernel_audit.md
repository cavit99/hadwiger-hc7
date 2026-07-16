# Independent audit of the private-transversal kernel theorem

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `hc7_private_transversal_graph_kernel.md`
- SHA-256: `e92d8dd9d4b2fc37d5734307a9c18d29d84c9f1b4e7b9f2d8298ad5798c8c763`

After the mathematical audit, the source was moved from `active/` to
`results/` and only its status metadata was updated to link this audit.
The audited mathematical content is unchanged; the hash above binds the
final promoted revision.

This audit covers Theorem 2.1, Corollary 2.2, the cited use of the
seven-vertex full-support lemma, and the limitation statement in Section 3.

## Checks performed

### 1. Choice and distinctness of private transversals

Minimality of `C` supplies a transversal of order at most two for each
`H_i`.  The cited maximal-support-pair theorem validly enlarges it, when
necessary, to a two-set disjoint from `A_i`, and proves support height six.
For `i!=j`, `P_i` avoids `A_i` whereas `P_j` meets `A_i`, because
`A_i in H_j`; hence the chosen pairs are distinct.

### 2. Star and triangle classification

If no two chosen pairs are disjoint, their distinct edge family is
pairwise intersecting and therefore is contained in a star or is exactly a
triangle.  In the star case, `p notin A_i`, and for every `j!=i` the only
way `P_j={p,l_j}` can meet `A_i` is through `l_j`.  This proves (2.1).

Since every `A_i` has order six, (2.1) first gives `m<=7`.  If `m=7`, it
forces `A_i=L-{l_i}`.  Thus, for `J=G[L]`, every `J-l_i` has a spanning
`K_5` model.  Lemma 4.2 of the cited separated-support theorem then gives
a spanning `K_6` model on `L`, and Lemma 4.3 lifts it to a `K_7` minor in
the seven-connected host.  This validates the sharper step `m<=6`.

In the non-star case the edge family is exactly `ab,bc,ca`.  The support
private to `ab` avoids `a,b` but must meet both `bc` and `ca`, forcing it
to contain `c`; the cyclic assertions follow identically.

### 3. Literal-clique corollary

For distinct `i,j`, the pair `{l_i,l_j}` meets every member of `C`: it
meets `A_i` and `A_j` crosswise and every other support in both leaves.
Since the whole family has transversal number above two, this pair misses
some member of `F_5(G)`.  A five-vertex support of a `K_5` model is the
vertex set of a literal `K_5`.  Because `P_i={p,l_i}` meets every such
support and this one avoids `l_i`, it must contain `p`.  Corollary 2.2 is
therefore correct.

### 4. Exclusivity and scope

The matching, star, and triangle alternatives are mutually exclusive and
exhaustive.  The theorem bounds only the number of supports in the
no-matching branch; it does not bound their ambient branch sets or compose
their models.  Section 3 states this limitation accurately.

## Unresolved assumptions or gaps

None within the stated theorem and corollary.  The two cited promoted
results are treated as dependencies and were not re-audited from first
principles here.
