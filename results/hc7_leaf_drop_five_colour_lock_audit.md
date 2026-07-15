# Audit: five-colour lock at a leaf-rooted drop edge

**Verdict:** GREEN.

For a fixed five-colouring of `R=C-{u,v}`, a colour absent from the
neighbours of `u` is legally available at `u`, and similarly for `v`.
If two distinct colours are available at the two endpoints, the colouring
extends over the edge `uv`, contradicting `chi(C)=6`.  Hence either one
availability set is empty or both are one common singleton.  No
connectivity, minor, or colouring-extension assumption is hidden.

The statement is deliberately local.  It does not claim that the same
endpoint is saturated in every five-colouring, that the common missing
colour is invariant across colourings, or that a regenerated unrooted
`K_5` model contacts either endpoint.  The Hajós join verifies that the
common-singleton alternative can persist throughout the whole extension
language.
