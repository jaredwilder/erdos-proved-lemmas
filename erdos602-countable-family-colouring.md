# Erdős #602 — every countable family of infinite sets is bichromatically 2-colourable

Author: Jared Wilder  
Public release: 2026-09-11

## Theorem

Let `A_0,A_1,...` be any countable family of infinite sets. Then the union of the family admits a 2-colouring such that every `A_i` contains both colours.

In particular, the countable-index stratum of Erdős #602 is affirmative. The pairwise finite-intersection and `!=1` hypotheses of the parent problem are not needed on this countable stratum.

## Proof

Proceed recursively through the family. At stage `i`, only finitely many points have been assigned colours at earlier stages. Since `A_i` is infinite, choose two as-yet uncoloured points `x_i,y_i in A_i`. Colour `x_i` red and `y_i` blue.

After all stages, colour every still-uncoloured point arbitrarily.

For each `i`, the designated points `x_i,y_i` remain in `A_i` with opposite colours, so no `A_i` is monochromatic.

## Scope

The canonical Erdős problem allows an arbitrary family cardinality. This theorem resolves only the countable-index case and does not address the uncountable core.

## Provenance

Recovered from the Day-One route chronology. The original campaign used the pairwise-finite-intersection hypothesis in its construction; the direct fresh-point argument above shows that hypothesis is unnecessary for countable families.

## License

Apache-2.0.
