# Kempe-trace synchronization at an exact seven-adhesion

## 1. The deleted-edge fan is stronger than a five-colour neighbourhood

The following elementary fact is the operation-level input that is lost
when one records only equality partitions.

### Lemma 1.1 (critical-edge Kempe fan)

Let \(G\) be non-\(r\)-colourable and let \(e=ab\) be an edge such that
\(G-e\) is \(r\)-colourable. In every proper \(r\)-colouring \(c\) of
\(G-e\), put \(\alpha=c(a)=c(b)\). For every
\(\beta\ne\alpha\), the vertices \(a,b\) lie in the same component of

\[
                 (G-e)[c^{-1}(\{\alpha,\beta\})].          \tag{1.1}
\]

Consequently each endpoint has a neighbour of every one of the other
\(r-1\) colours. For \(r=6\), the deleted edge therefore carries five
actual bichromatic \(a\)-\(b\) paths.

#### Proof

The ends have the same colour, since otherwise \(e\) could be restored.
If their \(\alpha/\beta\)-components were different, interchange the two
colours on the component containing \(a\). The ends would then have
different colours and \(e\) could again be restored. The first and last
edges of an \(a\)-\(b\) path in (1.1) give the two neighbour assertions.
\(\square\)

This strengthens Lemma 2.1 of
*hadwiger_degree9_lobe_equality_transition.md*: the five colours are not
merely present around the operated endpoint. Every one belongs to an
actual Kempe connector to the other endpoint.

## 2. A boundary edge: exact synchronized-switch criterion

Let \(S\) be a separator containing \(a,b\), and write

\[
                         G-S=D_1\dot\cup\cdots\dot\cup D_m. \tag{2.1}
\]

Fix an \(r\)-colouring \(c\) of \(G-ab\), and fix
\(\beta\ne\alpha=c(a)=c(b)\). Put

\[
                 W_\beta=\{s\in S:c(s)\in\{\alpha,\beta\}\}. \tag{2.2}
\]

For each \(i\), let \(\mathcal P_i^\beta\) be the partition of
\(W_\beta\) induced by the \(\alpha/\beta\)-components of

\[
                       G[D_i\cup S]-ab.                    \tag{2.3}
\]

Empty component traces are discarded. Let
\(\mathcal P^\beta\) be the join of these partitions: two boundary
vertices are equivalent when they can be joined by a chain whose
consecutive members lie in one block of some \(\mathcal P_i^\beta\).

### Theorem 2.1 (synchronized switch or an alternating shore chain)

Exactly one of the following holds.

1. The vertices \(a,b\) lie in different blocks of
   \(\mathcal P^\beta\). Then the side colourings can be switched and
   glued to a proper \(r\)-colouring of \(G\).
2. The vertices \(a,b\) lie in one block of \(\mathcal P^\beta\). There
   is a boundary-simple sequence
   \[
                         a=s_0,s_1,\ldots,s_k=b             \tag{2.4}
   \]
   and, for each \(j\), one actual \(\alpha/\beta\)-component
   \(K_j\) of \(G[D_{i_j}\cup S]-ab\) whose boundary trace contains
   \(s_{j-1},s_j\). The sequence can be chosen so that
   \(i_j\ne i_{j+1}\). If every \(K_j\) has a path between its displayed
   ends avoiding \(S-\{s_{j-1},s_j\}\), these paths form a literal clean
   alternating shore chain. Otherwise the first additional boundary
   vertex on such a path is a concrete dirty hit.

In particular, outcome 2 is forced whenever \(G\) is not
\(r\)-colourable.

#### Proof

Suppose first that \(a,b\) lie in different join blocks, and let \(X\)
be the join block containing \(a\). A join block is a union of blocks
of every \(\mathcal P_i^\beta\). In each graph (2.3), switch
\(\alpha,\beta\) on every bichromatic component whose nonempty boundary
trace lies in \(X\). This changes precisely the colours on \(X\), on
every side. The switched side colourings therefore agree on \(S\) and
glue. Exactly one of \(a,b\) was switched, so \(ab\) is now proper.
This is an \(r\)-colouring of \(G\).

Conversely, if \(a,b\) lie in one join block, form the bipartite support
graph whose two node classes are \(W_\beta\) and all nonempty-trace
bichromatic components from the shores, with incidence given by boundary
membership. Take a shortest path from \(a\) to \(b\) in this graph and
list its boundary nodes and component nodes alternately. Its boundary
nodes are distinct. Two consecutive component nodes cannot come from the
same shore: both would contain their common intervening boundary vertex
and hence would be the same bichromatic component. This gives (2.4) and
the asserted alternating \(K_j\)'s. Inside each connected \(K_j\), choose
a shortest path between its displayed boundary vertices. It is either
clean or has the stated first dirty boundary hit. \(\square\)

Thus the failure of a common repaired state is not an abstract parity
phenomenon. It has a literal certificate: a shortest chain of actual
Kempe regions alternating among shores, with a clean path or a named
dirty boundary hit in each region.

## 3. A portal edge: the operated/far incidence graph

Now let \(e=ux\), where \(u\in D_0\) and \(x\in S\). Fix an
\(r\)-colouring of \(G-ux\), put \(\alpha=c(u)=c(x)\), and fix
\(\beta\ne\alpha\). In the operated side

\[
                         H_0=G[D_0\cup S]-ux                \tag{3.1}
\]

let \(C_u,C_x\) be the \(\alpha/\beta\)-components containing \(u,x\).
On \(W_\beta\subseteq S\), take the join \(\mathcal Q^\beta\) of the
component partitions supplied by all shores \(D_i\), \(i\ne0\).

Form a bipartite incidence graph \(\mathcal I_\beta\). Its left vertices
are the \(\alpha/\beta\)-components of \(H_0\) which meet \(W_\beta\),
together with \(C_u\); its right vertices are the blocks of
\(\mathcal Q^\beta\). Each \(s\in W_\beta\) is an edge, labelled \(s\),
between its component in \(H_0\) and its block in \(\mathcal Q^\beta\).

### Theorem 3.1 (portal incidence exchange)

If \(C_u\) and \(C_x\) lie in different components of
\(\mathcal I_\beta\), then \(G\) is \(r\)-colourable. Hence, in a
critical graph, one of the following geometric alternatives holds for
every \(\beta\ne\alpha\).

1. \(C_u=C_x\), so the operated shore itself contains an
   \(\alpha/\beta\) \(u\)-\(x\) path.
2. A shortest \(C_u\)-\(C_x\) path in \(\mathcal I_\beta\), after
   expanding each far-side join block, gives a boundary-simple chain of
   actual Kempe regions alternating between the operated shore and far
   shores. Every region supplies either a clean connector or a first
   dirty boundary hit.

#### Proof

Assume \(C_u,C_x\) are in distinct incidence components and let
\(\mathcal C\) be the component containing \(C_u\). Let \(X\subseteq
W_\beta\) be the labels of its incidence edges. On the operated side,
switch exactly the bichromatic components represented by the left nodes
of \(\mathcal C\). On every far side, switch the components whose
boundary traces lie in the right join blocks of \(\mathcal C\). The
definition of a join block makes \(X\) a union of component traces on
every far side, so all switches are legitimate and induce exactly the
same boundary change \(X\).

The component \(C_u\) is switched and \(C_x\) is not. Thus \(u,x\)
receive different colours, the side colourings glue, and \(ux\) can be
restored. This colours \(G\), proving the first assertion. If the two
nodes coincide there is a local path. Otherwise a shortest path in the
incidence graph alternates between its two node classes; expand a far
join adjacency by a shortest path in the far-side support graph from
Theorem 2.1. Shortestness removes repeated boundary labels and consecutive
regions in the same actual shore. The final clean/dirty assertion is the
last part of Theorem 2.1. \(\square\)

Theorem 3.1 is the exact operation-level replacement for a claim that
the two sides must merely accept a common equality partition. It says
that failure to repair produces an actual alternating carrier chain.

## 4. Ordered portals: a clean crossing is a rooted diamond

The ordered unique-owner boundary supplies one further geometric step.

### Lemma 4.1 (crossing chords on a reserved spine)

Let \(R\) be a path containing four prescribed vertices in the order

\[
                              a<b<c<d.                       \tag{4.1}
\]

Suppose \(P_{ac}\) and \(P_{bd}\) are paths whose interiors avoid \(R\),
meet \(R\) only in their displayed ends, and are internally disjoint.
Then

\[
 R[a,b]\cup R[b,c]\cup R[c,d]\cup P_{ac}\cup P_{bd}         \tag{4.2}
\]

is a subdivision of a rooted \(K_4^-\) on \(a,b,c,d\), with the
possibly missing edge \(ad\).

In particular, if the two connector paths have interiors in distinct
components behind an adhesion, their disjointness is automatic.

#### Proof

The five internally disjoint displayed paths represent the five edges

\[
                              ab,\ bc,\ cd,\ ac,\ bd
\]

of \(K_4-ad\). \(\square\)

For the unique-owner lobe, choose an actual root-to-residue path in the
ordinary bag through the ordered portals. Consider two support chords,
obtained from synchronized portal witnesses, whose four ends interlace
on that path. Theorems 2.1--3.1 and Lemma 4.1 give the following rigorous
trichotomy for that interlacing pair:

* a common Kempe repair exists;
* two clean, interlacing support chords give a rooted diamond; or
* every attempted interlacing chord has a first dirty hit on the reserved
  ordinary-bag spine.

The third outcome is exactly the label-preserving lobe--interval interface:
the dirty hit identifies the first interval which must be transferred or
whose transfer is blocked by ownership. A claim that the rooted diamond
always exists would be false without excluding this dirty-spine outcome.

Consequently, in every application where the displayed rooted diamond
has already been shown to lift to the target model, a surviving
\(K_7\)-free exact adhesion has a sharply ordered form: all clean support
chords from distinct shores are noncrossing. Without that model-specific
lift, Lemma 4.1 should be retained as a concrete rooted-diamond outcome,
not silently promoted to a \(K_7\)-minor. In either formulation the
remaining obstruction is laminar/nested rather than an arbitrary pair of
incompatible boundary-state families.

## 5. The actual central edge \(56\)

Use outcome 1 of Theorem 4.5 in
*hadwiger_four_connected_rooted_diamond.md*:

\[
                        S=\{h,1,2,5,6,y,z\}                  \tag{5.1}
\]

is an exact seven-cut and every component of \(G-S\) is full. Let \(c\)
be any six-colouring of \(G-56\), and put
\(\alpha=c(5)=c(6)\).

### Corollary 5.1 (five actual support chains at the central adhesion)

For every \(\beta\ne\alpha\), the two vertices \(5,6\) lie in one block
of the join of the shore \(\alpha/\beta\)-partitions. Hence there is a
shortest boundary-simple chain of actual bichromatic shore regions, with
consecutive regions in different shores. Every region either supplies a
clean connector between its displayed boundary vertices or has a named
first dirty boundary hit. In particular, if one shore component contains
both \(5,6\), it gives a one-region certificate (not automatically a
boundary-clean path).

For \(\beta=c(v)\), the component containing \(v\) supplies the literal
path \(5-v-6\). For \(\beta=c(1)\), the boundary edge \(16\) puts
\(\{1,6\}\) in one block of every shore partition, while vertex \(2\)
belongs to neither colour. Symmetrically, for \(\beta=c(2)\), the block
contains \(\{2,6\}\) and excludes \(1\).

#### Proof

Apply Lemma 1.1 and Theorem 2.1. The assertions involving \(v,1,2\)
use the edges \(v5,v6,16,26,12\). In the \(c(1)\) case, \(2\) cannot
have colour \(\alpha\) because \(26\in E(G)\), and cannot have colour
\(c(1)\) because \(12\in E(G)\); the other case is symmetric.
\(\square\)

### Corollary 5.2 (the central adhesion has only two structural rows)

In a hypothetical \(HC_7\) counterexample, \(G-S\) has at most three
components. If it has two, every one of the five certificates in
Corollary 5.1 is an alternating chain between exactly two shore
partitions. If it has three, \(G[S]\) is four-chromatic and isomorphic
to the pure Moser spindle.

#### Proof

The component bound and the four-chromatic three-shore conclusion are
the full-shore block-gluing and three-shore capacity theorems in
*hadwiger_full_shore_block_gluing.md* and
*hadwiger_three_shore_block_capacity.md*. Their audited seven-vertex
support classification identifies the unique surviving boundary as the
pure Moser spindle. With two shores, the support incidence graph in
Theorem 2.1 has only the two shore labels, so its component regions
alternate between them. \(\square\)

Thus the central-edge branch no longer ends at a generic exact cut. It
has one fixed two-edge Kempe spoke through \(v\), two literal-supported
chains at \(1,2\), and two further colour chains. To close this branch it
is enough to prove that these five chains either contain two clean crossing
chords/one shore split which lifts to the rooted \(K_4\) of Theorem 4.5,
or that their dirty hits all select the same carrier interval. In the
latter case the label-preserving interval exchange is the remaining
operation. This is strictly narrower than arbitrary seven-boundary
state compatibility.

## 6. A graph-level barrier to state-only synchronization

The operation facts above still do not imply a common state without the
\(K_7\)-minor-free and seven-connectivity hypotheses. There is a concrete
nineteen-vertex witness.

Take the ordered boundary

\[
 S_0=\{r,a_1,\ldots,a_6\},\qquad
 a_1a_2\cdots a_6,\qquad r\sim a_2,\ldots,a_6.               \tag{6.1}
\]

On each side put a \(K_6\), with vertices numbered \(0,\ldots,5\). A
bit in position \(j\) of a mask means that the boundary vertex is adjacent
to clique vertex \(j\). In the boundary order \(r,a_1,\ldots,a_6\), use

\[
\begin{aligned}
 P&=(32,52,60,40,35,52,40),\\
 Q&=(59,21,27,8,10,34,51).                                 \tag{6.2}
\end{aligned}
\]

Every mask is nonzero, so both open shores are connected and full. A
boundary equality partition extends across a \(K_6\) shore exactly when
its blocks admit distinct representatives from the corresponding
complements of the six portal masks. The exact state families have orders

\[
                              32\quad\hbox{and}\quad9          \tag{6.3}
\]

and are disjoint. Nevertheless:

* deleting or contracting any portal edge creates a common state;
* deleting or contracting any interior edge creates a common state;
* deleting any interior vertex creates a common state; and
* in every portal-edge deletion colouring, the two ends agree and the
  interior end sees all other five colours.

The independent, dependency-free verifier
*degree9_exact7_palette_core_counterarchitecture_verify.py* enumerates
the 66 proper boundary partitions, checks (6.3), and checks the actual
minor colourings rather than only an abstract state table. It also checks
that the graph has connectivity exactly five and verifies the
explicit \(K_7\)-model

\[
 \{r\},\ \{a_2\},\ \{a_3\},\ \{p_5\},
 \{a_6,p_3\},\ \{a_4,q_1\},\ \{a_1,q_0,q_3\}.               \tag{6.4}
\]

This is not an \(HC_7\) counterexample. Its purpose is sharper: even
connectedness, fullness, every one-step interior/portal transition,
endpoint equality, and all five Kempe colours do **not** force a common
boundary state. A valid positive theorem must use the missing global
input. Theorems 2.1--4.1 identify how that input can enter: seven-
connectivity must prevent a dirty laminar support architecture, while the
fixed model geometry must either lift the relevant crossing diamond to
\(K_7\) or reroute it into a label-preserving exchange.

## 7. Exact remaining gap

The new operation-level residue is no longer the parity family from
*hadwiger_degree9_lobe_equality_transition.md*. It is the following
geometric statement.

> In the seven-connected, \(K_7\)-minor-free unique-owner adhesion, the
> five alternating incidence chains supplied by one portal-edge witness
> cannot all be clean and noncrossing, and cannot all have nested dirty
> hits on the reserved ordered spine.

A clean interlacing pair gives the rooted diamond of Lemma 4.1. A first
dirty hit identifies an actual lobe--interval transfer. What remains to
be proved is that the nested dirty hits either satisfy the connectivity
conditions of the label-preserving swap or expose a separator of order at
most six. This is the precise point where seven-connectivity and the
fixed carrier labels, absent from the counterarchitecture, must be used.
