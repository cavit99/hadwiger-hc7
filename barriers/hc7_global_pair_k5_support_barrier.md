# Exact support values in the two-apex icosahedron

## Status

This is a dependency-free exact census for the proposed global pair
potential

\[
 \mu(P)=\min\{|V(M)|:M\text{ is a `K_5` model in }G-P\},
\]

with value `infinity` when no model exists.  It both supports the potential
as a global normalization and shows that it does not orient neutral
near-`K_7` rotations.

The exhaustive checker is
[`hc7_global_pair_k5_support_barrier_verify.py`](hc7_global_pair_k5_support_barrier_verify.py).

## 1. Construction and complete census

Let `I` be the icosahedron and let

\[
                              G=K_2\vee I,
\]

with universal adjacent vertices `a,b`.  The graph is seven-connected and
`K_7`-minor-free, while `G-{a,b}=I` is planar.

For all 91 unordered vertex pairs, the checker proves exactly

\[
 \mu(P)=
 \begin{cases}
  5,&P\subseteq V(I),\\
  7,&|P\cap\{a,b\}|=1,\\
  \mathord\infty,&P=\{a,b\}.
 \end{cases}                                             \tag{1.1}
\]

There are respectively 66, 24 and one pairs of these types.  The order-five
line is immediate once a witness is found, because five nonempty branch
bags use at least five vertices.  For every apex--base pair, the checker
exhausts every connected candidate bag compatible with total support at
most six, finds none, and finds a model of support seven.  For the apex pair,
planarity of the remaining icosahedron excludes a `K_5` minor.

Thus `mu` sees the hidden terminal pair in this canonical guardrail and is
strictly stronger than the previously tested raw contact profile.

## 2. Exact neutral plateau

The reduced three-rotation component in
[`hc7_global_invariant_rotation_triangle.md`](hc7_global_invariant_rotation_triangle.md)
uses one fixed five-row frame.  Its unique missing bag pairs are

\[
 \begin{array}{c|c}
  M_T&\{T\}\ --\ \{w_0,w_2,B\},\\
  M_C&\{u_3,u_4,w_3,w_4\}\ --\ \{u_1,w_1\},\\
  M_0&\{u_0\}\ --\ \{u_2\}.
 \end{array}                                             \tag{2.1}
\]

Every vertex in (2.1) lies in the planar base.  The checker verifies the
three labelled near-`K_7` quotients and proves the stronger statement

\[
  \mu(\{x,y\})=5
  \quad\text{for every literal choice of }x,y
  \text{ across any missing pair in (2.1)}.              \tag{2.2}
\]

The rotations form a reduced directed triangle and preserve their coarse
carrier, while the terminal pair `{a,b}` remains in two fixed complete
rows.  Consequently `mu` cannot strictly increase on every legal neutral
rotation or on every rule that reselects a pair only across the current
missing adjacency.

## 3. Exact consequence for the proof programme

The example does **not** refute an existential monotone-exchange theorem.
Equation (1.1) contains increasing routes

\[
                 5\longrightarrow7\longrightarrow\mathord\infty
\]

if arbitrary pair changes can be justified.  It also does not refute a
theorem using seven-contraction-critical proper-minor responses: this graph
is six-colourable.

The correct conclusions are narrower.

1. A global maximization of `mu` is useful and recognizes the coherent pair
   in this family.
2. A local near-model rotation need not improve it; whole reversible
   components must still be quotiented.
3. The separate literal-`K_5` transversal theorem proves that every
   seven-connected `K_7`-minor-free graph has some pair of value at least
   six.  The live task starts at support six and requires a labelled
   exchange or a genuine `K_5`-**model** transversal.

Accordingly, the census is positive evidence for the global potential but
not the missing well-founded invariant.
