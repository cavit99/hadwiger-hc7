# Internal audit: maximum-contact PB programme

**Verdict:** **YELLOW**.  The canonical lower bound, the two finite
experiments, and the two negative scope corrections are GREEN.  No unbounded
contact-ten or four-colourability theorem is proved.  This is an internal
audit, not external peer review.

## Exact revisions audited

```text
48d801dab58a84a7449da61373ba0d3bc38bda340c087dcbd4d8973967ae422a  active/hc7_pb_max_contact_nine_four_colour.md
c12d09934bc8c099753253c04953ea75b8a8a019a38fed5a62898ae07aea0bf3  active/hc7_pb_max_contact_nine_verify.py
3d4cbdeb3f5461c4165ee0a9949fbfb0afa0a6361f06c797ab6b13abbb349c0a  active/hc7_pb_paired_rooted_adversarial_probe.py
```

Any mathematical or encoding change requires renewed audit.

## GREEN claims

1. The five canonical parts are connected, pairwise disjoint, meet both
   roots, cover the host, and have exactly the nine claimed contacts.
2. The quotient contact graph does not bound the number of neighbours of a
   singleton rim vertex inside an adjacent column.  The original inference
   “singleton rim column implies degree at most four” is invalid.
3. If the left and right rim portals of `C_i-V(R)` lie in different
   components, their aggregate existence does not make the proposed double
   bag connected.  The component-aware theorem cited in the note correctly
   requires one component with both contacts and assigns every other
   component to the path/pole bag.
4. The maximum-contact verifier exhausts every five-part spanning partition
   on each tested 14-vertex host.  Its deterministic seeded run reports 43
   five-connected hosts, all with `c_*=10`, and one tested low-contact host,
   which is four-colourable and not five-connected.
5. The transfer probe exactly enumerates 17,644 and 28,281 packs on its two
   named hosts.  Both have complete maximum packs; the second has the printed
   incomplete contact-nine local maximum under the encoded connected-piece
   transfer rule.

## Reproduction

I ran:

```text
/usr/bin/python3 active/hc7_pb_max_contact_nine_verify.py
/usr/bin/python3 active/hc7_pb_paired_rooted_adversarial_probe.py --host audited
```

Both completed successfully with the counts recorded in the source note.
Python compilation and `git diff --check` also pass.

## Rejected claims from the original isolated Grok branch

The original draft labelled the following claims proved; they are not:

- five-connectivity does not imply every rim column has at least two vertices
  by the proposed degree argument;
- portal vertices somewhere on both sides of `C_i-V(R)` do not suffice for
  the displayed transfer when they lie in different components;
- the claimed general max-contact reduction depended on those two steps.

The revised note explicitly removes those claims.  It also omits the original
non-five-connected `K_5`-pole proposition because the final retained verifier
does not certify that separately described construction.

## Trust boundary

The experiments have fixed order, fixed column size, and fixed sampled or
named edge families.  They are positive finite evidence and a transfer-rule
barrier only.  They do not prove that every five-connected PB expansion has a
contact-ten pack, do not four-colour an arbitrary residual host, and do not
supply a strict same-form reduction.  The global allocation inference remains
open.
