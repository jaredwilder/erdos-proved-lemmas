# Erdős #701 — rank-2 hereditary star theorem

Author: Jared Wilder  
Public release: 2026-09-11

Let `F` be a finite hereditary family of finite sets, every member having size at most two. Let `m(F)` be the maximum size of a pairwise-intersecting subfamily and let `Delta(F)` be the largest full star.

## Theorem

`m(F)=Delta(F)`.

## Proof

A largest star is pairwise intersecting, so `m(F)>=Delta(F)`.

Let `G` be any pairwise-intersecting subfamily. If `G` contains a singleton `{x}`, then every member of `G` contains `x`, so `|G|<=Delta(F)`.

Otherwise every member of `G` has size two. View `G` as an intersecting simple graph. If all edges share a common endpoint, `G` lies in a star. If not, choose edges `xy,xz` and an edge not containing `x`. Pairwise intersection forces that edge to be `yz`, and any edge intersecting all three of `xy,xz,yz` is one of those three. Thus `G={xy,xz,yz}`.

Because `F` is hereditary and contains `xy` and `xz`, it also contains `{x}`. Hence the star at `x` contains `{x},xy,xz`, so `Delta(F)>=3=|G|`.

Thus every intersecting subfamily has size at most `Delta(F)`, proving equality.

## Scope

This settles the complete rank-at-most-two hereditary class. It does not prove the unrestricted Chvátal star conjecture / parent Erdős problem. Historical novelty is not claimed.

## License

Apache-2.0.
