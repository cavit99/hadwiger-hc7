# Independent audit: terminal-edge contraction in a Mader delta-matroid

**Audited file:** `hc7_mader_terminal_contraction_projection.md`

**Audited SHA-256:**
`f032b3a5af71161aa421e82f7c22dfa88727e20cc03bf01cc7cbabbc0bc08e24`

**Audit verdict:** **GREEN** for Theorem 2.1, Theorem 3.1, and
Corollary 3.2.  The slice-preserving exchange statement in Section 4 is
only a conjectural target and is not included in this verdict.

Relative to the previously audited revision, only the status metadata was
updated to link this completed audit.  The mathematical content is
unchanged.

## 1. Scope of the audit

The audited note makes three proved claims:

1. contracting an edge between two terminals in the same terminal part
   replaces the two possible endpoint choices by one disjunctive endpoint;
2. a generic linear combination of the two corresponding columns and rows
   represents that disjunction; and
3. independent generic combinations give one master skew-symmetric matrix
   whose appropriate principal restrictions represent every quotient by a
   subset of pairwise vertex-disjoint terminal edges.

I checked the graph lifting in both directions, the Pfaffian calculation,
the use of algebraically independent coefficients, and the simultaneous
construction.  I also tested whether ordinary symmetric exchange can be
confined to the principal restrictions that correspond to actual graphs.
It cannot, even in a four-terminal example; Section 5 records the
counterexample.

## 2. Audit of Theorem 2.1

Let `xy` be contracted to `z`, with `x,y` terminals in the same part of
the terminal partition.

If a feasible endpoint set omits `z`, every path in the contracted graph
avoids `z`: a terminal not belonging to the endpoint set cannot be an
internal path vertex.  Consequently the packing uses no edge created by
identifying `x` and `y`, and it lifts unchanged to a packing avoiding both
old terminals.  The converse follows for the same reason: a packing whose
endpoint set omits `x,y` avoids both vertices and survives their
contraction.

If a feasible endpoint set contains `z`, exactly one path of the packing
ends at `z`.  The path edge incident with `z` is the image of an edge
incident with at least one of `x,y`; choosing such a preimage lifts that
path with endpoint `x` or endpoint `y`.  Every other path avoids `z` and
therefore lifts without using either old terminal.  Conversely, a packing
using exactly one of `x,y` as an endpoint cannot use the other as an
internal vertex.  Contracting `xy` therefore produces a packing ending at
`z` and creates no intersection with another path.

The hypothesis that `x,y` lie in one terminal part is important for the
stated terminal partition after contraction.  It also prevents the edge
`xy` itself from being a permitted path between different terminal parts.
Theorem 2.1 is correct.

## 3. Audit of Theorem 3.1

The clean matrix formulation is as follows.  Let

\[
 E'=(E-\{x,y\})\cup\{z\}
\]

and let `P` be the `E` by `E'` matrix which is the identity on
`E-\{x,y\}` and satisfies

\[
                  P e_z=\alpha e_x+\beta e_y.
\]

Then

\[
                         B=P^{\mathsf T}AP                 \tag{3.1}
\]

is skew-symmetric and has exactly the entries displayed in the audited
note.  This also checks that both the new row and the new column have the
required signs.

For `R` not containing `z`, `B[R]=A[R]`.  Now let
`R=U\cup\{z\}`.  Put `z` first and put `x,y` before the common ordering of
`U`.  Multilinearity of the Pfaffian in the row and matching column gives

\[
 \operatorname{Pf}B[U\cup\{z\}]
 =\alpha\operatorname{Pf}A[U\cup\{x\}]
  +\beta\operatorname{Pf}A[U\cup\{y\}].              \tag{3.2}
\]

With another fixed ordering the two summands may acquire fixed signs;
that does not affect the argument.  The variables `\alpha,\beta` are
algebraically independent, so the two distinct degree-one monomials
cannot cancel.  Hence the Pfaffian in (3.2) is nonzero if and only if at
least one coefficient Pfaffian is nonzero.  For an odd-order set all three
relevant skew-symmetric principal matrices are singular.  Thus (3.1)
represents precisely the feasibility rule of Theorem 2.1.

This proof works over the rational-function extension of the original
representation field.  If a finite numerical representation is wanted,
the generic variables may subsequently be specialized over a sufficiently
large extension field while avoiding the finitely many nonzero Pfaffian
polynomials.  No such specialization is needed for the theorem as stated.

Theorem 3.1 is correct.

## 4. Audit of Corollary 3.2

For pairwise disjoint pairs `\{x_i,y_i\}`, define a rectangular matrix
`P^\sharp` which retains every original basis vector and additionally has

\[
 P^\sharp e_{z_i}=\alpha_i e_{x_i}+\beta_i e_{y_i},
\]

where all `\alpha_i,\beta_i` are algebraically independent.  The master
matrix

\[
                   C=(P^\sharp)^{\mathsf T}A P^\sharp       \tag{4.1}
\]

is skew-symmetric.  In a principal restriction containing a set `Z` of
new elements and neither old endpoint belonging to the corresponding
pairs, Pfaffian multilinearity gives a sum indexed by choices
`\varepsilon_i\in\{x_i,y_i\}`:

\[
 \operatorname{Pf}C[U\cup Z]
   =\sum_{\varepsilon}
      \pm\!\left(\prod_{i:z_i\in Z}
                    \gamma_{i,\varepsilon_i}\right)
      \operatorname{Pf}A[U\cup\{\varepsilon_i:z_i\in Z\}], \tag{4.2}
\]

where `\gamma_{i,x_i}=\alpha_i` and
`\gamma_{i,y_i}=\beta_i`.  Distinct endpoint choices give distinct
monomials, so (4.2) is nonzero exactly when at least one lifted endpoint
set is feasible.

On the graph side, the contracted edges are vertex-disjoint.  A
vertex-disjoint path packing uses each contracted terminal as an endpoint
of at most one path, and that path can be lifted through one old endpoint.
The choices for different contracted terminals are therefore compatible.
The principal restriction prescribed in Corollary 3.2 consequently
represents exactly the corresponding contracted terminal network.

Corollary 3.2 is correct.

## 5. Ordinary symmetric exchange need not preserve graph slices

The qualification in Section 4 of the audited note is necessary.  It
cannot be replaced by an unconditional slice-preserving exchange claim.

Let the terminal set be

\[
                   \{x,y,b_1,b_2\}
\]

with terminal partition

\[
                   \{x,y\}\mid\{b_1,b_2\},
\]

and let the graph have edges

\[
                         xy,\quad xb_1,\quad yb_2.
\]

The split network has the feasible endpoint set

\[
                         F=\{x,y,b_1,b_2\},
\]

witnessed by the two one-edge paths `xb_1` and `yb_2`.  After contracting
`xy` to `z`, the endpoint set

\[
                         F'=\{z,b_1\}
\]

is feasible.  Both are feasible in the master delta-matroid of
Corollary 3.2.

Their symmetric difference is `\{x,y,z,b_2\}`.  Apply the symmetric
exchange axiom to `F`, `F'`, and the element `x`.  The possible second
elements give:

- toggling only `x` produces an odd set;
- toggling `x,y` produces `\{b_1,b_2\}`, whose two terminals lie in one
  part;
- toggling `x,b_2` produces `\{y,b_1\}`, for which no permitted path
  exists; and
- toggling `x,z` produces `\{y,z,b_1,b_2\}`.

The last set is feasible in the master matrix: the projected column `z`
must select its `x` term, and the resulting old endpoint set is `F`.
But it contains an old endpoint and its projected element simultaneously,
so it belongs to neither graph slice.  Thus the only successful exchange
in this instance leaves the family of principal restrictions corresponding
to actual contraction states.

This example does not contradict Corollary 3.2.  It proves that the next
exchange theorem must use additional graph-specific hypotheses; it is not
a formal consequence of the delta-matroid symmetric exchange axiom.

## 6. Exact remaining limitations

The audited results provide a common linear representation, but they do
not prove any of the following:

- that exchanges can be normalized to a principal restriction
  corresponding to an actual quotient;
- that a feasible endpoint set records prescribed endpoint pairings or
  path interiors;
- that the same representation encodes paths whose two ends lie in the
  same terminal part;
- that it retains colouring or Kempe-component data;
- that a principal-rank obstruction has a graph interpretation as an
  order-seven separation preserving the named minor models; or
- that the support-six transversal has order at most two.

In the current `HC_7` programme, the all-three-contracted Mader-path branch
has already been closed by a separate graph-theoretic argument.  The live
application would have to address the two-edge contraction/eight-boundary
residue or the label-preserving extraction problem.  The three audited
claims alone do neither.  Subject to this trust boundary, the verdict is
**GREEN**.
