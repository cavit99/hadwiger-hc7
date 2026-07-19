# Independent internal audit: overlapping demand intervals in a path component

**Verdict:** GREEN for the stated induced-path-component normal form and
its explicit trust boundary.

## Audited revision and verdict

This audit checks the complete source file
[`hc7_order8_overlapping_interval_normal_form.md`](hc7_order8_overlapping_interval_normal_form.md)
at SHA-256

```text
c973d105dd9441840de98bf9ebf0c7a362a76f4980400ea3a9e403bd5b116560
```

The mathematical source, including the sharpness example, was independently
checked at SHA-256
`e53a9a9e2a536ced094f73df5ab4002b806978729cc45a3f1b2e79f2823e87ca`.
The first post-audit source revision had SHA-256
`9265cd03f5b6c1490b9073a779f311adb30273144ac3bc4fb8368d1cbae92142`;
it differed only by replacing the opening pending-audit sentence with the
link to this audit.  Promotion from `active/` to `results/` then removed
only the words `active draft;` from that status line.  Re-inserting those
words in the current source reproduces the prior hash exactly.  The theorem
statements, proofs, scope and sharpness argument are unchanged.

**Verdict: GREEN for Lemma 1.1, Theorems 2.1 and 3.1, Corollary 2.2, and
the scoped sharpness example.**  The result applies only when the entire
selected complementary component is the displayed induced path.  It does
not solve the general case in which the fan spine has off-spine vertices.

## 1. Exact interval criterion

For a connected set in a path containing `p_0`, connectedness forces the
set to be a prefix; the analogous set containing `p_m` is a suffix.  A
prefix through `p_{q-1}` meets both members of `D` exactly when `q>=a+1`,
and a suffix from `p_q` meets both members of `E` exactly when `q<=b`.
Thus a disjoint rooted pair exists exactly when `a<b`.

When `b<=a`, the minimum left hull is `P[0,a]` and the minimum right hull
is `P[b,m]`.  Their intersection is exactly `P[b,a]`, so the claimed
compulsory overlap core is literal and exact.

## 2. Strict reversal

Choose `d,e` with first and last indices `a,b`, respectively.  Under
`b<a`, the left tail through `p_b` misses `d`, the right tail from `p_a`
misses `e`, and the two contact edges `p_be,p_ad` have four distinct ends.

Because `C` is an induced path component of `G-S`, the full neighbourhood
of either tail is its literal boundary contact set plus its one path
successor or predecessor.  Seven-connectivity therefore makes the
boundary contact order six or seven.  These are exactly the order-seven
and one-defect alternatives in the source.

The middle subpath has precisely its boundary contacts plus whichever of
`p_{b-1},p_{a+1}` exist.  Its neighbourhood is a genuine separator because
another component of `G-S` remains outside.  The inequality and every
endpoint case in (2.7)--(2.10) follow.  Equality retains both selected
contact edges across the returned boundary.

The two independent edges admit the three contraction signatures, while
an all-proper six-colouring would colour `G`.  The cited audited
two-independent-edge theorem consequently gives exactly the stated
opposite-shore separation or endpoint-rooted `K_4` model.  No inherited
branch-set label is inferred from that rooted model.

## 3. Shared portal

When `a=b=q`, the two selected edges share `p_q`.  Their common deletion
is a proper minor and hence at most six-chromatic.  If it were at most
five-chromatic, recolouring `p_q` with a fresh sixth colour would permit
both edges to be restored, contradicting `chi(G)=7`.  Hence its chromatic
number is exactly six, and the established `t=6` case supplies a `K_6`
minor.

The connectedness used to make this model spanning is valid:
`kappa(G)<=lambda(G)` makes `G` seven-edge-connected, and deletion of two
edges leaves the common host connected.  Every component outside a
`K_6` model has an edge to the model union and can be absorbed into one
adjacent branch set.

The revised signature statement is also exact.  Contracting either edge
separately gives `(equal,proper)` or `(proper,equal)`.  Contracting both
gives a proper expanded `(equal,equal)` colouring only when `de` is absent;
if `de` is present, its ends are identified and the expanded assignment is
not proper on the common deletion.  The source makes precisely this
qualification.

## 4. Sharpness example

The icosahedral adjacencies in the audited `K_2 vee I` barrier verify all
claims in Section 5 of the source.  In particular:

- `u_4u_3w_3w_4` is a spanning path of the selected component;
- every member of the eight-vertex boundary has a neighbour on that path;
- the latest first contact of `{q,d}` is `w_3`, while the earliest last
  contact of `{w_0,u_2}` is `u_3`;
- inside the component, `d` contacts `w_3,w_4`, and `u_2` contacts `u_3`;
  and
- `u_3w_4` is absent, so every connected set containing both uses `u_4`
  or `w_3`.

The short disjointness argument in the source follows.  The cited barrier
already verifies that the host is seven-connected, `K_7`-minor-free and
six-colourable and has a compatible order-seven separation.  It therefore
refutes geometry-only rerouting but not the response-preserving
minor-or-compatible-separator target.

## 5. Trust boundary

The audit proves a complete path-component normal form.  It does not prove:

1. that a path spine contains every vertex of an arbitrary component;
2. that off-spine bridges can be assigned without changing the interval
   obstruction;
3. that either regenerated rooted minor respects the five inherited model
   labels; or
4. that any returned order-seven boundary carries one equality partition
   extending through both intact closed shores.

Those are not used in the GREEN verdict.
