# Sharp coherent-prism outcome for the simultaneous six-state packet

Let `D` be the triangular prism `C3 square K2`, with vertices in the
standard `networkx.circular_ladder_graph(3)` order.  Give its six portal
classes singleton representatives

\[
 (P_0,P_1,P_2,P_3,P_4,P_5)
   = (\{0\},\{4\},\{2\},\{3\},\{1\},\{5\}).
\]

Then the six portal classes have an SDR, none of the three antipodal
demands `e_i | e_(i+3)` has disjoint carriers, and all six frames are
present.  In particular the shore owns all three opposite frame pairs.

The dependency-free verifier
`c6_simultaneous_prism_sharpness_verify.py` enumerates every connected
vertex mask and tests the exact carrier definition.  It prints

```text
portal roots (0, 4, 2, 3, 1, 5)
host connectivity 3
antipodal linkages (False, False, False)
owned frames (True, True, True, True, True, True)
```

Thus the abstract simultaneous packet does **not** force an antipodal
crossing, even with singleton portal classes and a three-connected host.
A correct structural theorem must retain a coherent prism/disk outcome.
In the counterexample-derived `C6 dotunion K1` setting that outcome is
removed only by the ambient degree/contact argument: each prism vertex has
internal degree three and the face-intersection lock permits too few boundary
contacts to reach degree seven.  The example is therefore sharpness for the
local theorem, not an `HC7` counterexample.
