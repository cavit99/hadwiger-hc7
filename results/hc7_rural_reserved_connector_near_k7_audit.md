# Independent audit: rural reserved-connector near-`K_7` handoff

**Verdict:** GREEN after one exact-residue correction.

**Audited source:** `results/hc7_rural_reserved_connector_near_k7.md`

**Source SHA-256:**
`27b88d45edff784685c35b126bacf5ee257e172ec1249370f7a1ba59a5470cdb`

The first draft listed the case in which both alternating bad paths are
literal edges as part of the rural residue. That case is incompatible with
the rural disk. The source now contains the corrected, strictly smaller
residue.

## 1. Branch-set validity

Let `C=P-{a_i,b_i}`. Since the path has nonempty interior, the path edges
induced by its internal vertex sequence make `C` a nonempty connected
subgraph. The hypotheses put `C` outside all four rooted bags.

The seven displayed bags are pairwise disjoint:

- the four rooted bags are pairwise disjoint by hypothesis;
- `C` is disjoint from them by hypothesis;
- `P_1,P_2` are disjoint subsets of the open shore `R`;
- all of the first five bags lie in `A union S`, whereas the packet bags
  lie in `R`.

Every displayed bag is connected.

## 2. Complete adjacency ledger

All required bag adjacencies are literal:

1. The four rooted bags are pairwise adjacent by hypothesis.
2. `C` meets the `a_i`- and `b_i`-bags through the first and last edges of
   `P`.
3. Each packet is adjacent to every rooted bag because it is `S`-full and
   the bag contains its named literal root.
4. Each packet is adjacent to `C`: every vertex of the nonempty set `C`
   lies in `S`, and an `S`-full packet has a neighbour of that literal
   vertex.
5. The two packet bags are adjacent by hypothesis.

Thus the only unforced pairs are `C` with the two rooted bags whose roots
are not the ends of `P`. These two pairs share the bag `C`.

The repository uses `K_7^vee` for `K_7` with two incident edges deleted.
Ignoring any surplus edges, the displayed bags therefore form exactly a
labelled `K_7^vee` model. One optional contact leaves at most one missing
pair and gives a labelled `K_7^-`; both optional contacts give `K_7`.

## 3. Combination with the rural normalization

The audited closed-shore theorem starts with the two vertex-disjoint bad
paths `P_0,P_1` in `G[S]`, obtains a rooted diamond whose missing pair is
one of `a_0b_0,a_1b_1`, repairs that pair using its corresponding path,
and reserves the other path disjointly from the resulting rooted `K_4`.

If the reserved path has nonempty interior, the theorem audited here
applies and gives the labelled near-model. Therefore a direct-reserve
survivor must leave a literal edge as the reserved path.

Both bad paths cannot be literal edges in the rural branch: they would be
two vertex-disjoint paths joining alternating points of the disk boundary.
If exactly one is a literal edge, its rooted pair cannot be missing from
the diamond, because the literal edge already joins the two bags containing
its ends. Hence the corrected residue is exact:

- exactly one bad path is nontrivial;
- the other is a literal edge; and
- the diamond misses the nontrivial pair, so that nontrivial path is
  consumed in the repair.

## 4. Companion bounded probe

The final paragraph is a barrier statement, not part of the proof. The
companion script `active/hc7_rural_rooted_k4_augmentation_probe.py` was run
independently and reported:

```text
RURAL_K4_STATIC_AUGMENTATION instances 1183 path_pairs 3860
universally_closed 0 survivors 3860 both_nontrivial 134
FIRST_SURVIVOR ('tree_0', 0, (1, 2, 2, 2, 2, 2, 2),
                (0, 1, 3, 4), (2, 5, 6), (0, 0, 0), 'repair', 0)
```

This supports only the stated warning against a static fifth-bag inference;
it is not used to prove the uniform theorem.

## 5. Exact scope

The result closes every rural outcome in which the connector left after the
rooted-diamond repair is nontrivial by handing off a literal labelled
`K_7^vee`. It does not turn that near-model into `K_7`, and it leaves the
single exact direct-reserve configuration described above. No colouring or
minor-critical transition is proved here for that residue.
