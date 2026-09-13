# Erdős #274 — infinite-group reduction for exact coset covers

**Author:** Jared Wilder  
**Status:** exact structural theorem / reduction; parent finite-group problem remains outside this result  
**Historical novelty:** not asserted

## The theorem

Let an infinite group `G` be partitioned exactly into finitely many left cosets

\[
G=\bigsqcup_{i=1}^m g_iH_i.
\]

If the subgroup cardinalities `|H_i|` are pairwise distinct, then necessarily `m=1`.

Equivalently: a nontrivial finite exact coset cover of an infinite group cannot have pairwise-distinct part cardinalities.

## Proof

Suppose `m>1`.

Because `G` is infinite and is the union of finitely many cosets, at least one `H_i` is infinite. Let

\[
\kappa=\max_i |H_i|
\]

and choose a part `C=g_jH_j` with `|H_j|=kappa`.

The cardinalities are pairwise distinct, so every other part has cardinality strictly less than `kappa`. Since there are only finitely many other parts, their union has cardinality strictly less than `kappa`:

\[
|G\setminus C|<\kappa.
\]

Now `C` cannot equal `G`, because `m>1` and the partition has another nonempty part. Thus `H_j` is a proper subgroup of `G`. Pick `x∉C`; the left coset of `H_j` containing `x` is disjoint from `C` and has cardinality exactly `kappa`.

Hence

\[
|G\setminus C|\ge\kappa,
\]

contradicting `|G\setminus C|<kappa`.

Therefore `m=1`.

## Consequence for the recovered #274 program

Any counterexample requiring a nontrivial exact finite coset partition with pairwise-distinct subgroup/cardinality data must live in a **finite** group. Infinite groups are eliminated completely by the theorem above.

This is a reduction, not a resolution of the finite Herzog–Schönheim-type residual problem. The recovered campaign explicitly preserved that boundary.

No historical-priority claim is made.