# Audit: two-defect rooted face and portal capture

## Verdict

**GREEN.**  The five-root facial alternative uses the rooted-`K_4`
theorem at its valid strength, the face-uniqueness step is sound, the
captured portal hypothesis gives the exact displayed neighbourhood, and
the planar outcome deletes one literal global pair of original vertices.

## 1. Rooted-model lift

Deleting the three-vertex clique `O` from a seven-connected graph leaves
a 4-connected graph `H`.  Each of

\[
 v,b_s,b_t,x_s,x_t
\]

is adjacent to every vertex of `O`: the first is adjacent because its only
noncontact singleton labels are `s,t`, the next two by the singleton
clique, and the last two by their all-but-one witness rows.

Hence an `X`-rooted `K_4` model in `H`, for any four displayed roots,
lifts literally to `K_7`: each of its four rooted branch bags has an edge
to each of the three singleton bags in `O`, and those three singleton bags
form a triangle.  No contracted colour class is being used as a model
label.

## 2. One common face

In the target-free branch, the rooted theorem makes `H` planar and makes
each four-subset cofacial.  The faces for

\[
 \{v,b_s,b_t,x_s\},\qquad \{v,b_s,b_t,x_t\}
\]

share the three actual vertices `v,b_s,b_t`.  Since `H` is 4-connected,
it is 3-connected; its plane embedding is unique up to reflection and two
distinct faces share at most two vertices.  The faces are therefore the
same.  All five roots lie on one face.

## 3. Exact captured neighbourhood and two-apex lift

Let `O={q_1,q_2,q_3}` with `q_3=b_i` and suppose
`P_i={x_s,x_t}`.  The spanning-shell partition contains no vertices other
than `v`, `B`, and the five singleton labels.  Therefore in `H=G-O`,

\[
 N_H(q_3)=\{v,b_s,b_t,x_s,x_t\}.
\]

There are no hidden vertices from an unused component or a nonsingleton
foreign bag.  The first three incidences follow from `i notin {s,t}` and
the singleton clique; the last two are exactly the captured portal set.

Every one of these five vertices also sees `q_1,q_2`, so the nested
triangle theorem applies.  In fact Theorem 2.1 already gives a direct
proof: draw `H` with the five neighbours on one face, insert `q_3` in that
face, and join it to exactly those five vertices.  This draws
`G-{q_1,q_2}`.  Thus the rural outcome uses the single literal apex pair
`q_1,q_2` globally, not a pair chosen separately by local pieces.

Consequently the captured-portal alternative of the two-defect shell is
closed.  The only remaining `d=2` residue is the disconnected graph
`B-{x_s,x_t}`.
