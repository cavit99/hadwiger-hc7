# Independent audit: palette deletion and the antipodal gate

## Verdict

**GREEN after two local repairs to the source note.**  The palette-deletion
theorem, its six-colour specialization, the antipodal path split, all branch
adjacencies, and the Kempe switch are rigorous.  The original draft did not
justify the existence of the prescribed exact trace from the hypotheses as
written.  The source has now been repaired by assuming the standard
minor-minimal counterexample and deriving the trace by star contraction.  The
path split has also been written explicitly, and a stray control character in
the proof has been removed.

The only external theorem used is the proved four-colour case of Holroyd's
Strong Hadwiger Conjecture (Martinsson--Steiner): if a four-colourable graph
has a set which receives all four colours in every proper four-colouring, it
has a rooted (K_4)-model whose four bags each meet that set.

## 1. Audit of Theorem 1.1

Let the four retained classes of the fixed (k)-colouring be the vertex set of
(J).  If a four-colouring (\varphi) of (J) uses at most three colours on
(X=S\cap V(J)), assign a separate fresh colour to each of the other (k-4)
original classes.

This really is a proper colouring of all of (H):

* each deleted original class is independent;
* two distinct deleted classes receive distinct colours; and
* every deleted-to-retained edge has endpoints in the fresh and old palettes,
  respectively.

Its trace on (S) uses at most (3+(k-4)=k-1) colours, contradicting
(k)-saturation.  Thus every four-colouring of (J) uses all four colours on
(X).  In particular, (J) cannot be three-colourable (a three-colouring could
be regarded as a four-colouring with one unused label), so there is no
chromatic-number mismatch in the Strong-(HC_4) invocation.  The rooted model
conclusion is exactly the conclusion of that theorem.

Empty colour classes cause no exceptional case: saturation itself forces all
(k) labels to occur on (S), hence every one of the four selected classes meets
(S).

## 2. Audit of the six-colour specialization

If a six-colouring of (H=G-v) omits a colour on (S=N_G(v)), assigning that
colour to (v) gives a six-colouring of (G).  Therefore non-six-colourability
of (G) makes (S) six-saturating in every six-colouring of (H).

When (|S|=7) and the trace consists of one double class (I) and five singleton
classes, deleting the class of (I) and one singleton class leaves exactly four
boundary vertices (X), one in each retained colour.  Strong (HC_4) supplies
four disjoint rooted bags, each meeting (X).  Four nonempty, pairwise disjoint
subsets of a four-element set must each be singletons, so after relabelling the
bags one may indeed write (i\in R_i).

## 3. Exact-trace construction

This was the one substantive omission in the first draft.  An arbitrary
counterexample need not supply an exact trace with an arbitrarily prescribed
nonedge as its repeated pair.  In the corrected statement, (G) is
minor-minimal among non-six-colourable (K_7)-minor-free graphs.

For the Moser nonedge (05), contract the connected set (\{v,0,5\}) to (z).
The proper minor is six-colourable.  Pull the colouring back to (H), assigning
(0) and (5) the colour of (z).  This is proper because (05) is a nonedge and
every old neighbour of (0) or (5) is adjacent to (z) after contraction.  Each
member of (S-\{0,5\}) is adjacent to (z) through its old edge to (v), so none
has the repeated colour.  Finally, the saturation argument above forces all
six colours to occur on the seven vertices of (S).  Consequently those other
five vertices have the other five colours one each: the trace is exactly
(05\mid1\mid2\mid3\mid4\mid6).

## 4. Audit of the gate path and branch sets

The Moser edges relevant to the proof are

\[
 0i\in E(G)\quad(i=1,2,3,4),\qquad
 53,54,61,62,56\in E(G).
\]

Suppose the bichromatic components (K_0) and (K_{56}) coincide.  For a
shortest path (Q=x_0\ldots x_\ell) from (x_0=0) to (\{5,6\}), no internal
vertex is (5) or (6).  Therefore

\[
 P_0=\{x_0,\ldots,x_{\ell-1}\},\qquad P_{56}=\{5,6\}
\]

are disjoint and connected; the last edge of (Q) makes them adjacent, and
(56) makes (P_{56}) connected.

The root (0\in P_0) is adjacent to every (i\in X), so (P_0) is adjacent to
every (R_i).  The roots (5,6\in P_{56}) collectively dominate (X): (5) sees
(3,4), while (6) sees (1,2).  Thus (P_{56}) is adjacent to every (R_i).
The four (R_i) are mutually adjacent by the rooted (K_4)-model, and the two
gate sets are adjacent by the last path edge.  All six sets are disjoint
because the gate sets lie in (A\cup B) and the rooted bags lie in
(J=H-(A\cup B)).  Each contains a boundary vertex, so the singleton ({v}) is
adjacent to every one.  These are valid branch sets for a (K_7)-minor.

## 5. Audit of the Kempe switch

If (K_0\ne K_{56}), they are distinct components of the induced
bichromatic graph (H[A\cup B]) and hence anticomplete.  Since (5) and (6) are
joined by the boundary edge (56), both lie in (K_{56}); therefore (K_0)
contains (0) and neither (5) nor (6).

Swapping the two colours on an entire bichromatic component preserves
properness.  More explicitly, a newly equal-coloured edge from (K_0) to its
complement would formerly have been an (A,B)-edge of (H[A\cup B]), contrary
to component maximality.  The switch moves only boundary vertex (0) from one
gate colour to the other, changing

\[
                         05\mid6\quad\hbox{to}\quad5\mid06.
\]

The other four colour classes, their induced graph (J), and the already
chosen rooted (K_4)-model are unchanged.

Finally, in this outcome (K_0), (K_{56}), and the four rooted bags form a
(K_6^-)-model: the only missing bag adjacency is
(K_0K_{56}).  Adding ({v}) gives precisely the claimed canonical
(K_7^-)-model.  This is a structural gate, not yet a (K_7)-minor; the note
does not overclaim that the deficient adjacency has been repaired.

