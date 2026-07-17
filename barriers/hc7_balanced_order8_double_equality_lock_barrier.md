# A balanced order-eight barrier to local double-equality repair

**Status:** computer-assisted finite barrier, with a written construction, a
deterministic
[`verifier`](hc7_balanced_order8_double_equality_lock_barrier_verify.py),
and an
[`independent internal audit`](hc7_balanced_order8_double_equality_lock_barrier_audit.md).
This graph is not a counterexample to
`HC_7`: it contains a `K_7` minor, is not minor-minimal, and does not have
the canonical rooted-web obstruction.

## 1. The inference that fails

The following local data do not force a boundary-preserving repair of a
simultaneous-equality colouring, a common boundary partition, or a direct
Kempe transition between the two one-edge responses:

1. an eight-connected, seven-chromatic graph with an actual order-eight
   separation whose two open shores are connected and adjacent to every
   boundary vertex;
2. the balanced star boundary

   \[
       S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
          \mathbin{\dot\cup}\{x\},
   \]

   where `R` is a triangle, `e,f` are disjoint anticomplete edges, the
   complement of `G[S]` has a perfect matching, and the endpoint
   nonneighbour sets in `R` satisfy the live rigidity condition;
3. two disjoint five-cliques with exactly the original-clique and
   opposite-shore placement used in the balanced order-eight programme;
4. disjoint edges `g,h` in opposite open shores such that `G-g`, `G-h`,
   and `G/g/h` are six-colourable, while `G` is not;
5. a six-colouring of `G-{g,h}` in which both pairs of endpoints are
   equal and in which every elementary boundary-preserving Kempe repair is
   blocked.

The graph below satisfies all five items.  Nevertheless, the selected
simultaneous-equality boundary partition extends to neither one-edge
restoration, the two restoration languages have no common boundary
partition, and no single Kempe interchange joins them.

Thus the local critical-edge locks cannot replace either of the two global
hypotheses still absent here: `K_7`-minor-freeness/minor-minimality and the
canonical rooted-web missing linkage.

## 2. Construction

Use the vertex set

\[
\begin{aligned}
V={}&\{a,b,a',b',p_a,q_a,p_b,q_b,c,d\}\\
   &\mathbin{\dot\cup}\{t_0,t_1,t_2\}
    \mathbin{\dot\cup}\{u,v,x\}
    \mathbin{\dot\cup}\{y_0,y_1,y_2\}.
\end{aligned}
\]

The verifier uses the ASCII names `ap,bp,pa,qa,pb,qb`.  Put

\[
\begin{aligned}
R&=\{t_0,t_1,t_2\},\\
A^\circ&=\{a,b,p_a,q_a,p_b,q_b\},\\
B^\circ&=\{c,d,y_0,y_1,y_2\},\\
S&=R\cup\{a',u,b',v,x\},\\
e&=a'u,\qquad f=b'v,\qquad g=ab,\qquad h=cd.
\end{aligned}
\]

Start with two copies of `K_4` minus an edge on

\[
       \{a,a',p_a,q_a\},\qquad \{b,b',p_b,q_b\},
\]

where respectively `aa'` and `bb'` are omitted.  Make each of `c,d`
adjacent to `a',b'`, add `g,h`, make `R` a triangle, and initially make
`R` complete to the ten displayed core vertices.  Add the boundary edges
`a'u,b'v`, the edges

\[
        ub,uc,\quad va,vd,\quad xa,xc,
\]

and make `\{c,d,y_0,y_1,y_2\}` a five-clique.

The remaining edges have a compact deterministic definition.  Consider
the following three colour assignments:

| assignment | `a` | `b` | `a'` | `b'` | `p_a` | `q_a` | `p_b` | `q_b` | `c` | `d` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `g` proper, `h` equal | 0 | 1 | 0 | 1 | 1 | 2 | 0 | 2 | 2 | 2 |
| both equal | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 2 | 2 |
| `g` equal, `h` proper | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 2 | 1 |

| assignment | `t_0` | `t_1` | `t_2` | `u` | `v` | `x` | `y_0` | `y_1` | `y_2` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `g` proper, `h` equal | 3 | 4 | 5 | 4 | 4 | 3 | 1 | 3 | 0 |
| both equal | 3 | 4 | 5 | 5 | 4 | 5 | 0 | 3 | 1 |
| `g` equal, `h` proper | 3 | 4 | 5 | 5 | 5 | 5 | 0 | 3 | 4 |

Forbid all `A^circ-B^circ` edges and also

\[
 a'b',\ a'v,\ ub',\ uv,\ aa',\ au,\ bb',\ bv.
\]

Except for the already inserted critical edges `g,h`, add every
nonforbidden edge whose endpoints have different colours in all three
assignments.  Finally delete

\[
 a't_0,\ b't_0,\quad
 t_2p_a,\ t_2q_a,\ t_2p_b,\ t_2q_b.
\]

This defines a graph on 19 vertices with 105 edges.

## 3. Exact checked properties

The verifier exhaustively establishes the following.

### Boundary and clique data

The displayed `(A^circ,S,B^circ)` is an order-eight separation.  Both
open shores are connected and adjacent to every literal vertex of `S`,
and the graph is eight-connected.

The two boundary edges are anticomplete.  Relative to

\[
                    L=R\cup\{a,b\},
\]

the edge `e` is anticomplete to `a` and collectively adjacent to
`L-{a}`, while `f` is anticomplete to `b` and collectively adjacent to
`L-{b}`.  For each of `e,f`, its two endpoint nonneighbour sets in `R`
are nonempty and disjoint.

The sets

\[
            L=R\cup\{a,b\},\qquad
            Y=\{c,d,y_0,y_1,y_2\}
\]

are disjoint five-cliques in the required opposite shores.  Moreover,
`A^circ-{a,b}` is connected and has boundary neighbourhood exactly
`S-{t_2}`.  Thus the usual connected leaf-side residue is present.

The complement of `G[S]` contains the perfect matching

\[
              t_0x,\quad t_1u,\quad t_2v,\quad a'b'.
\]

### Chromatic and response data

The graph has chromatic number seven.  Put `H=G-{g,h}`.  Then `H` is
exactly six-chromatic, has an explicit `K_6`-minor model, and the two
one-edge deletions are six-colourable.

After fixing the three colours of `R` to remove global colour
permutations, exhaustive enumeration gives

\[
\begin{array}{c|ccc}
 &G-g&G-h&H\\ \hline
\text{six-colourings}&24&342&792.
\end{array}
\]

The 792 colourings of `H` split as follows:

\[
\begin{array}{c|ccc}
 (g,h)&(\mathrm{equal},\mathrm{proper})
      &(\mathrm{proper},\mathrm{equal})
      &(\mathrm{equal},\mathrm{equal})\\ \hline
 \text{count}&24&342&426.
\end{array}
\]

No colouring makes both edges proper.  The `G-g` response realizes two
boundary partitions and the `G-h` response realizes twelve; the two sets
are disjoint.

### A fully blocked simultaneous-equality colouring

One colouring of `H` has boundary partition

\[
        \{a',b'\}\mid\{t_0,x\}\mid\{t_1\}\mid\{t_2\}
           \mid\{u,v\}.                              \tag{3.1}
\]

Partition (3.1) belongs to neither one-edge response language.  In this
colouring the endpoints of `g` have colour 3.  For alternate colours
`0,1,2,4`, they lie in the same bichromatic component of the closed
`A`-shore.  For alternate colour 5 they lie in distinct components, but
those two components meet the boundary in

\[
                       \{b',v\},\qquad\{a',u\}.
\]

Hence no elementary Kempe switch confined away from the boundary makes
`g` proper.  The endpoints of `h` have colour 4 and are in the same
bichromatic component for every alternate colour.  Thus `h` is locked
even more strongly.

Exhaustive construction of the Kempe-reconfiguration edges also confirms
that no single Kempe interchange takes any `G-h` response colouring to
any `G-g` response colouring.

### The planar list-critical core is not a Gallai tree

The open `A`-shore itself is planar.  In fact, with rim path

\[
                         p_a-a-b-p_b
\]

and nonadjacent hubs `q_a,q_b`, its graph is

\[
                         \overline{K_2}\vee P_4,
\]

the octahedral graph with one rim edge removed.

For the simultaneous-equality colouring in (3.1), fixing the boundary
colours gives the following lists on the induced subgraph

\[
                         K=G[\{a,b,p_a,p_b,q_a\}]:
\]

\[
\begin{aligned}
 L(a)=L(b)&=\{3,4\},\\
 L(p_a)=L(p_b)=L(q_a)&=\{2,4\}.
\end{aligned}
\]

The graph `K` is the fan obtained by making `q_a` adjacent to every
vertex of the path `p_a-a-b-p_b`.  It is not list-colourable.  If
`q_a` receives 2, then `p_a,p_b` receive 4 and force both `a,b` to
receive 3; if `q_a` receives 4, it directly forces both `a,b` to receive
3.  Either way the edge `ab` is monochromatic.  Deleting any vertex makes
the graph list-colourable, as does deleting `ab`, so `K` is precisely a
minimal fixed-boundary critical core of the type used in the active
double-equality argument.

But `K` is two-connected and is neither a clique nor an odd cycle.  It is
therefore not a Gallai tree.  Its degrees are

\[
                    3,3,2,2,4,
\]

while all five lists have order two.  This gives a concrete reason that
the degree-choosability theorem cannot be invoked: the critical-core
inequality is strict at three vertices.  Even planarity of the leaf shore,
the exact balanced boundary, and complete local nonrepairability do not
force a Gallai-tree core.  Any Gallai-tree endgame must first derive the
missing equality `d_K(w)=|L(w)|` throughout the core from a genuinely
global `HC_7` hypothesis.

## 4. Exact trust boundary

Three missing global hypotheses are visible rather than implicit.

First, `G` contains a `K_7` minor with branch sets

\[
 \{t_0\},\{t_1\},\{t_2\},
 \{a,p_a,a'\},\{b,p_b,b'\},\{c\},\{d\}.
\]

Second, `G` is not minor-minimal: deleting `u` leaves a seven-chromatic
graph.

Third, after contracting `e` and `f` to `z_e,z_f` and deleting `R`, the
same-index linkage which the canonical rooted web must forbid is already
present.  Its paths are

\[
                         a-x-z_e,\qquad b-q_a-z_f.
\]

Consequently this barrier does not refute a decoder that uses the full
canonical web together with `K_7`-minor-freeness and minor-minimality.  It
does prove that the boundary locks, balanced boundary, endpoint rigidity,
and the two named five-cliques are not by themselves a sufficient
decoding mechanism.

## Verification

Run:

```bash
python3 barriers/hc7_balanced_order8_double_equality_lock_barrier_verify.py
```

The verifier has no third-party dependencies.  It checks the construction,
all vertex cuts of order at most seven, all relevant six-colourings and
boundary partitions, all one-step Kempe interchanges, the lock certificate,
the two explicit minor models, and the three stated trust-boundary failures.
