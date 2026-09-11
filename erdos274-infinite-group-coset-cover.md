# Erdős #274 — finite exact coset covers of infinite groups

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let an infinite group `G` be partitioned into finitely many left cosets

`G=C_1 ⊔ ... ⊔ C_t`,

and suppose the cardinalities `|C_i|` are pairwise distinct. Then `t=1`.

Equivalently, any nontrivial finite exact coset cover whose parts have pairwise-distinct cardinalities must occur in a finite group.

## Proof

A finite union of subsets of cardinality strictly smaller than `|G|` still has cardinality smaller than `|G|`, so at least one part `C_i=gH` has `|H|=|G|`.

If `H` were proper, another `H`-coset disjoint from `gH` would also have cardinality `|G|`. The finitely many remaining partition parts cover that coset, so one of them must itself have cardinality `|G|`, contradicting pairwise distinctness.

Hence `H=G`, so `gH=G` and the partition has one part.

This reduces the nontrivial distinct-cardinality exact-cover question to finite groups.
