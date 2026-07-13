# Spanning normalization of a contact-maximal clique model

## 1. Setting

Let \(H\) be connected, let \(N\subseteq V(H)\), and let

\[
                    \mathcal M=(B_1,\ldots,B_r)
\]

be a \(K_r\)-model in \(H\).  A bag is contacted when it meets \(N\).
Assume \(\mathcal M\) maximizes the number of contacted bags among all
\(K_r\)-models in \(H\).

The usual Hall promotion is often formulated with unused components
outside the model.  At contact maximum those components can all be assigned
to old bags without losing contact information.

## 2. Root components cannot see an uncontacted bag

### Lemma 2.1 (root-component orientation)

Let \(C\) be a component of

\[
                    H-\bigcup_{i=1}^rB_i
\]

which contains a root \(n\in N\).  Then every model bag adjacent to
\(C\) is already contacted.

#### Proof

Suppose \(C\sim B_j\) and \(B_j\cap N=\varnothing\).  Inside the
connected graph \(C\), choose an \(n\)-to-\(B_j\) path and stop it at
its first vertex of the old model.  Because \(C\) is a component outside
the model and the chosen terminal bag is adjacent to \(C\), the path can
be chosen so that this first model vertex belongs to \(B_j\).  Adjoin the
model-free prefix to \(B_j\).  This preserves connectedness,
disjointness, and every old clique-bag adjacency, while it makes \(B_j\)
contacted.  This contradicts contact maximality. \(\square\)

The first-hit qualification is essential only when one starts with a path
allowed to meet several model bags.  Taking a shortest path from \(n\) to
the specific neighbour of \(B_j\) inside \(C\), followed by its last
edge into \(B_j\), gives the required path directly.

## 3. Spanning extension

### Theorem 3.1 (contact-preserving spanning normalization)

Every contact-maximal \(K_r\)-model extends to a spanning
contact-maximal \(K_r\)-model with exactly the same contacted bag set.
Moreover every root of \(N\) outside the old model can be assigned only
to a bag which was already contacted.

#### Proof

Let \(C_1,\ldots,C_m\) be the components outside the old model.  Since
\(H\) is connected, each \(C_s\) has a neighbour in at least one old
bag.  Assign the entire connected component \(C_s\) to one adjacent bag.

If \(C_s\cap N\ne\varnothing\), Lemma 2.1 says that every possible
adjacent recipient is already contacted.  Choose any one.  If
\(C_s\cap N=\varnothing\), choose any adjacent bag, contacted or not.
In either case the recipient remains connected, all bags remain disjoint,
and every old interbag edge remains.  The set of contacted bags is
unchanged.

Do this independently for all outside components.  The resulting bags
partition \(V(H)\), so the model is spanning.  Its contact count equals
the old maximum and is therefore still maximal. \(\square\)

### Corollary 3.2 (all root multiplicity is internal)

In the spanning normalization,

\[
                         N\subseteq\bigcup_{i=1}^rB_i,
\]

and every root lies in a contacted bag.  If exactly \(c<r\) bags are
contacted, some contacted bag contains at least

\[
                         \left\lceil\frac{|N|}{c}\right\rceil
\tag{3.1}
\]

roots.

For a hypothetical \(HC_7\) counterexample, \(|N(v)|\ge7\).  If a
contact-maximal \(K_6\)-model has five contacted bags, its root
multiplicities have surplus at least two: either two bags are multiply
rooted, or one bag contains at least three roots.

#### Proof

The first assertion follows from spanning and the definition of contact.
The bound is pigeonhole.  The final statement applies it with seven roots
in five bags and records the two possible distributions of two surplus
units. \(\square\)

## 4. Consequence for the genuine terminal lock

The contact-maximal obstruction may therefore be studied with no exterior
shadow components at all.  Its exact data are a spanning labelled clique
model and a distribution of all neighbourhood roots among its contacted
bags. For \(HC_7\) with five contacted bags, the degree bound rules out a
lone two-root bag with four single-root bags: that accounts for only six
of the at least seven roots. Dropping the sole uncontacted bag therefore
leaves either

1. two multiply rooted bags; or
2. one bag containing at least three roots.

The older rooted \(K_{2,4}+e\) split lock is a valid one-bag projection,
but the terminal spanning model always carries one additional unit of root
capacity which a complete argument must exploit.

This normalization does not itself prove the rooted split.  It removes a
genuine source of false cases: no argument in the terminal contact-maximal
cell may invoke an unassigned “shadow component,” since every such
component can already be allocated to an old bag as above.  Any remaining
dirty path lies inside a named branch bag, and any failed rerouting is a
label-owner or faithful-operation obstruction inside the spanning model.
