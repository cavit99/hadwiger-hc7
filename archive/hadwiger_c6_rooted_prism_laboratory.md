# The rooted-prism target extracted from the \(C_6\) laboratory

## 1. Six fixed roots

Write the missing cycle as

\[
 c_0c_1c_2c_3c_4c_5c_0,
\]

and put \(e_i=c_ic_{i+1}\). A frame \(i\) is the two-linkage demand
\(\{e_{i-2},e_{i+2}\}\). The exact \(K_7\) certificates now prove that
every surviving full-shore configuration has all of the following
properties:

1. one shore owns at least four frames, including two opposite frame
   pairs;
2. none of the three antipodal demands
   \(\{e_i,e_{i+3}\}\) is linkable in either shore;
3. no nonidentity perfect matching from
   \(\{c_0,c_2,c_4\}\) to \(\{c_1,c_3,c_5\}\) has a three-linkage.

The identity matching is

\[
 c_0c_3,\qquad c_2c_5,\qquad c_4c_1,
\]

and the two triples together with this matching form the triangular
prism.

## 2. Exact small-order experiment

The program c6_sixroot_7vertex_probe.py exhausts every three-connected
graph in the NetworkX graph atlas on seven vertices, every choice of one
unlabelled extra vertex, and every labelling of the other six vertices as
\(c_0,\ldots,c_5\). It tests the linkage conditions above by enumerating
simple paths and requiring vertex-disjoint path masks.

Its exact output is:

    underlying 3-connected atlas graphs: 2 [875, 1006]
    labelled survivor types: 8
    survivors without the prescribed rooted prism: 0

The analogous six-vertex check has a unique three-connected survivor:
the triangular prism itself. Every other six-root graph supporting four
frames while avoiding the forbidden two- and three-linkages has a
two-cut.

This is a finite certificate, not an unbounded proof. Its value is that
it identifies the correct structural object and falsifies the idea that
an arbitrary web or planar graph should be the final exception.

## 3. The unbounded theorem suggested by the experiment

The next target should be stated for fixed roots before portal
multiplicity is reintroduced.

> **Rooted-prism core target.** Let \(H\) be a three-connected graph
> with prescribed distinct roots \(r_0,\ldots,r_5\). If \(H\) supports
> two opposite pairs of frame linkages, but supports neither an
> antipodal two-linkage nor a nonidentity even-to-odd perfect-matching
> three-linkage, then \(H\) has a triangular-prism minor rooted at the
> \(r_i\) in the prescribed order.

The stronger rigidity target is that a minor-minimal such \(H\) is the
rooted prism itself. A plausible proof route is:

1. take a minor-minimal union of the four frame linkages;
2. pass to its three-connected torso;
3. use a label-preserving splitter or the specified-edge rooted-prism
   theorem to find the prism;
4. show that every proper bridge or splitter extension creates one of
   the forbidden linkages.

For an actual shore the frame linkages may use different representatives
of the same portal class. Therefore the rooted-prism core target alone is
not enough. The required preceding statement is a
**coherence-or-two-cut/web lemma**:

> either the owned frame linkages can be rerouted to use six coherent
> portal representatives in one three-connected torso, or their failure
> produces a two-separation/4-web whose exact boundary state is
> colour-gluable.

This formulation avoids the rejected symbolic-order argument: no portal
label is identified with a common vertex until coherence has actually
been proved.

## 4. How this can scale

For a general boundary \(J\), form a finite demand hypergraph whose
vertices are portal classes and whose hyperedges are the minimal repair
linkages having a positive boundary quotient. Complementary demands
cannot be assigned to anticomplete shores, giving a shore-ownership
constraint. A highly connected torso should realize a rooted minor of
this demand hypergraph; failure of coherent representatives should yield
a bounded-adhesion web.

The \(C_6\) case is the first nontrivial instance:

* its demand graph is three opposite frame pairs;
* its coherent torso is the triangular prism;
* its incoherent outcome is the rope/web decomposition now under attack.

Thus the intended reusable principle is not “enumerate more boundary
graphs,” but:

\[
\text{demand ownership}
\Longrightarrow
\text{coherent rooted torso or exact-state separator}.
\]

