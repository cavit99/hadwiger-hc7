# Three explicit `K_7` models for the minimal degree-eight three-path quotient

**Status:** written finite structural theorem; separate internal audit GREEN.  The
proof is by three explicit minor models.  The adjacent checker verifies only
the displayed branch sets; it is not an unbounded search and it does not show
that every hypothetical counterexample reaches this quotient.

## 1. The labelled quotient

Let `G` contain the following eighteen pairwise distinct vertices:

\[
 \{u_0,u_1,u_2,u_3\}\mathbin{\dot\cup}
 \{x_0,x_1,x_2,x_3,x_4\}\mathbin{\dot\cup}
 \{b_0,b_1,b_2\}\mathbin{\dot\cup}
 \{a_I,a_J,z_0,z_1,z_2,v\}.
\tag{1.1}
\]

Indices on the `u`-vertices are taken modulo four and indices on the
`x`-vertices modulo five.  Assume that all of the following edges are
present.

1. `u_0u_1u_2u_3u_0` and `x_0x_1x_2x_3x_4x_0` are cycles, and
   `u_i x_i` is an edge for `0<=i<=3`.
2. `v` is adjacent to every `x_i` and to `b_0,b_1,b_2`.
3. Each of `b_1,b_2` is adjacent to every `x_i`, while `b_0` is adjacent
   to `x_3,x_4`.
4. `a_I` is adjacent to `u_0,u_2,z_0,z_1,z_2`, and `a_J` is adjacent to
   `u_1,u_3,z_0,z_1,z_2`.
5. `z_0z_1,z_0z_2` are edges, and all six edges

   \[
        b_1z_k,\quad z_ku_0\qquad(0\le k\le2)
   \tag{1.2}
   \]

   are present.
6. `b_0b_1,b_0b_2,b_1b_2,b_1u_0,b_2a_J` are edges.
7. `b_0` is adjacent to at least one of `z_0,z_1,z_2`.

Extra vertices and edges of `G` are unrestricted.

The sets

\[
 \{u_0,u_2,a_I\},\quad \{u_1,u_3,a_J\},\quad
 \{b_2\},\quad\{b_0\},\quad\{z_0,z_1,z_2\}
\tag{1.3}
\]

are the five connected subgraphs in the compressed three-path picture.
The theorem below uses only the listed edges, notably the location of the
mandatory contact from `b_0` to the last set.  Thus no enumeration of
unlisted contacts is involved.

## 2. Completion theorem

### Theorem 2.1

Every graph satisfying Section 1 contains a `K_7` minor.

#### Proof

If `b_0z_0` is an edge, take the following seven branch sets:

\[
\begin{split}
 &\{b_0\},\quad \{b_2\},\quad
 \{u_2,u_3,x_0,x_1,x_2,a_I,a_J,z_0\},\\
 &\{x_3\},\quad \{x_4\},\quad
 \{b_1,z_1,z_2\},\quad \{v\}.
\end{split}
\tag{2.1}
\]

If `b_0z_2` is an edge, take

\[
\begin{split}
 &\{u_1,u_2,x_0,x_1,x_2,a_I\},\quad \{b_2\},\quad
 \{x_4\},\quad \{b_1,z_0\},\\
 &\{u_3,x_3,a_J,z_1\},\quad \{b_0,z_2\},\quad \{v\}.
\end{split}
\tag{2.2}
\]

In the remaining case `b_0z_1` is an edge; take

\[
\begin{split}
 &\{u_0,x_0,x_4,a_J,z_0\},\quad \{b_0,z_1\},\quad
 \{b_2,x_2\},\quad \{x_3\},\\
 &\{u_2,u_3,a_I\},\quad \{b_1,z_2\},\quad
 \{u_1,x_1,v\}.
\end{split}
\tag{2.3}
\]

In each line the seven sets are nonempty and pairwise disjoint.  The edges
listed in Section 1 make every set connected and every two sets adjacent.
They are therefore branch sets of a `K_7` minor.  The three cases exhaust
the required `b_0`--`{z_0,z_1,z_2}` contact.  \(\square\)

## 3. Role and trust boundary

The theorem eliminates the fully compressed quotient in which the three
colour-indexed paths have the common form `b_1-z_k-u_0` and the fifth
connected subgraph contains the three vertices `z_0,z_1,z_2`.  It is
stronger than a contact-pattern census: once the displayed fixed edges are
present, the single mandatory contact from `b_0` selects one of three
explicit constructions.

The theorem does **not** prove that a general three-path branch can be
compressed to these eighteen vertices while preserving the five named
connected subgraphs.  In particular, it does not control first-hit
collisions inside a nonsingleton connected subgraph, and it uses neither
seven-connectivity nor contraction-criticality.  Its proper use is as the
terminal construction after a label-preserving compression theorem, not as
that missing compression theorem itself.
