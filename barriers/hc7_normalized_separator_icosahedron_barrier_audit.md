# Audit of the sharp normalized-separator example

**Verdict:** GREEN in its stated scope.

Audited source SHA-256:
`400b64a2a676a02f29fc466184618e3a00c901369a4b6593a258b1d0c0a92353`.

Verifier SHA-256:
`c6390c4fb1180b509295c7e827e03cc18bf642abf529f7bb51f9e67d252cae4e`.

An independent construction check and the retained deterministic verifier
confirm:

1. `K_2 join I` is seven-connected and `K_7`-minor-free;
2. the displayed seven branch sets form a spanning
   `K_7`-minus-one-edge model with singleton deficient roots;
3. `(T_1,T_2,T_3,{11},{10})` is a normalized dominating `K_5` model;
4. the displayed five vertices induce the required cycle;
5. the order-seven set `S` separates the portal vertex from `T_1` in `J`
   and is an actual separator of the whole graph; and
6. the explicit six-colouring makes both omitted roots miss the same colour,
   so the universal two-root colouring cover is absent.

The example refutes only the claim that connectivity and the static model
data force a separator of order five. It realizes a permitted terminal
order-seven separation and is not a counterexample to `HC_7` or to the
current completion-or-separation target.
