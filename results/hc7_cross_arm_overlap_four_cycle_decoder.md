# Five-terminal cycle decoder in the overlap-four cell

## Status

Proved by the parameterized residue below and the dependency-free bitmask
checker
[`../active/hc7_cross_arm_overlap_four_cycle_decoder_verify.py`](../active/hc7_cross_arm_overlap_four_cycle_decoder_verify.py).
An independent cold audit is **GREEN**; see
[`hc7_cross_arm_overlap_four_cycle_decoder_audit.md`](hc7_cross_arm_overlap_four_cycle_decoder_audit.md).

This extends the rooted-`K_4` decoder.  A rooted five-cycle in the
exterior closes ten of the twelve cyclic orders.  The other two orders do
not branch into unrelated cases: they give one crossed two-gate
certificate with a three-state tail.

## 1. Setup

Use the same normalized labels and eleven irredundant supports as in
[`hc7_cross_arm_overlap_four_rooted_k4_decoder.md`](hc7_cross_arm_overlap_four_rooted_k4_decoder.md):

```text
A={0,1,2,3,4,5},        I={0,1,2,3},
X=I union {6},           p=7, q=8,
T={4,5,6,7,8}.
```

Let `H=G-I`.  Suppose `H` has five pairwise disjoint connected bags rooted
at the five vertices of `T`, with consecutive bags adjacent in a cyclic
order `pi`.  No chord is assumed.

As in the four-terminal decoder, keep two edge layers.  The eleven support
relations constrain the original literal edges.  The five cycle
adjacencies supplied by the rooted bags are added only in the final
composition layer.

## 2. Cycle-decoder theorem

### Theorem 2.1

Up to reversal, every cyclic order on `T` has one of the following
outcomes.

1. The original graph contains, for some `i in I`, a `K_4` model in
   `A-{i}` contacted by all three vertices `i,p,q`.
2. The original local edges together with the five rooted-cycle
   adjacencies contain a `K_7` model, which expands through the five rooted
   bags to a `K_7` model in `G`.
3. After interchanging `p,q` if necessary, the order is

   ```text
   4,5,p,6,q,
   ```

   and the augmented nine-label complement is the crossed-frame
   certificate in Section 3.

In particular, only the two oriented orders

```text
(4,5,p,6,q),   (4,5,q,6,p)
```

can reach outcome 3.  The other ten cyclic orders close by outcome 1 or 2.
If `G` is seven-connected, outcome 1 also gives `K_7` by the audited
three-rooted small-`K_4` composition theorem.

## 3. The uniform crossed-frame certificate

Write a bad order as

```text
l_1,l_2,r,6,s
```

where `{l_1,l_2}={4,5}`, `{r,s}={p,q}`, and in the normalized orientation
`l_1=4,l_2=5`.  Every survivor has complement

```text
{l_1 6, l_1 r, l_2 6, l_2 s} union M union F,       (3.1)
```

where

* `M` is one of the three perfect matchings of `I`; and
* for some `u in I`,

  ```text
  F in {{rs}, {u6}, {rs,u6}}.
  ```

All other augmented adjacencies are present.  Conversely, every choice in
(3.1) survives the finite local decoder.  Thus there are exactly

```text
3 matchings times (1+4+4) tails = 27
```

labelled survivors for either bad order.

This is the reusable alternative.  The two left gates are crossed:
`l_1` misses `6,r`, while `l_2` misses `6,s`.  The four vertices of `I`
carry only a matching defect, and the remaining obstruction is a
three-state rotation: the root edge `rs` is missing, one `I-6` spoke is
missing, or both are missing.  There are no further portal patterns hidden
behind the 27 labels.

The certificate is edge-maximal in the four gate defects.  Supplying even
one additional labelled adjacency from

```text
{l_1 6, l_1 r, l_2 6, l_2 s}
```

gives a `K_7` model in every one of the 27 states.  Supplying both the
root adjacency `rs` and all four `I-6` adjacencies also closes every state.
These repair assertions are checked by explicit branch-model enumeration,
not inferred from an edge count.

## 4. Complete order classification

Fix `4` first and identify a cyclic order with its reversal.  The checker
obtains:

| cyclic orders | number | result after common rooted-`K_4` outcomes are removed |
|---|---:|---|
| `(4,5,p,6,q)` and `(4,5,q,6,p)` | 2 | exactly the 27 crossed-frame states |
| every other order | 10 | every state has a `K_7` model |

The ten good orders are checked as complete equivalence classes, not by
choosing a favourable state.  The program first joins the original support
relations (387 partial states, 3096 full original completions), removes the
2016 completions with a common rooted `K_4`, and tests all 1080 remaining
completions under each virtual cycle.

## 5. Branch-set lift and trust boundary

For outcome 2, replace every terminal vertex used by the finite `K_7`
model with its rooted cycle bag.  If a finite branch bag contains two
consecutive terminals, take the union of their rooted bags and an edge
between them.  More generally, the finite checker verifies connectivity
using only original edges and the five cycle adjacencies, so replacing
each terminal by its rooted bag preserves connectedness, disjointness and
every inter-bag adjacency.  This yields actual branch sets in `G`.

The theorem does not eliminate the crossed frame (3.1).  Its contribution
is to replace an arbitrary five-terminal web order by one exact labelled
alternative.  The next structural step must use four-connectivity,
contraction-critical state transitions, or a second rooted route to break
one of the four fixed gate defects or the rotating tail.  Merely adding
another abstract five-cycle in the same bad order is not asserted to help.
