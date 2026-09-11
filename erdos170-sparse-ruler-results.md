# Erdős #170 — sparse-ruler constants, exact small values, and parity obstruction

Author: Jared Wilder. Public release: 2026-09-11.

Let `F(N)` be the least number of marks in `{0,...,N}` whose positive pairwise differences cover every integer `1,...,N`.

## Correct evaluation of the analytic constant

The recovered research record uses the constant

`c0 = sqrt( sup_{t!=0} 2(1-sin(t)/t) )`.

The supremum is **not** obtained from the limit `sin(t)/t -> 0`. The function `sin(t)/t` becomes negative. Its first and global negative minimum occurs at the first positive nonzero solution `t*` of

`tan(t)=t`,

with

`t* ≈ 4.493409457909064`,

`sin(t*)/t* ≈ -0.217233628211222`.

Therefore

`c0 ≈ 1.560277942041880`,

not `sqrt(2)≈1.414214`.

This is a correction to the evaluation of the displayed constant in the historical corpus.

## Exact values through 20

Exhaustive enumeration gives

`F(1..20) = 2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,8,8,8`.

In particular,

`F(10)=6`.

There are 38 six-mark witnesses at `N=10`; a lexicographically first one is

`{0,1,2,3,6,10}`.

Two historical witness sets were incorrect even though the associated values were right:

- `{0,1,3,4,7}` misses distance 5; a valid five-mark witness is `{0,1,2,3,7}`;
- `{0,1,3,6,8}` misses distance 4; a valid five-mark witness is `{0,1,2,5,8}`.

## Counting bound and its first failure

The elementary difference count gives

`F(N) >= ceil((1+sqrt(1+8N))/2)`.

Within `N<=20`, this bound is tight at

`1,2,3,4,5,6,7,8,9,11,12,13,16,17`

and first fails at

`N=10`,

where the bound gives 5 but `F(10)=6`.

## Parity obstruction

For a `k`-mark ruler with ordered marks `a_1<...<a_k`,

`sum_{i<j}(a_j-a_i) = sum_i (2i-k-1)a_i`.

When `k` is odd, the right side is even. A perfect ruler whose positive differences are exactly

`1,...,C(k,2)`

would instead have total difference sum

`C(k,2)(C(k,2)+1)/2`.

Hence no perfect `k`-mark ruler exists whenever `k` is odd and that triangular sum is odd. The familiar `k=5`, `N=10` obstruction is the first case of this parity mechanism.

## Restricted and unrestricted variants

The restricted problem above requires all marks to lie in `[0,N]`. If marks are allowed outside that interval while still requiring differences `1,...,N`, the two variants first diverge at `N=18` in the recovered computation:

`{0,2,7,14,15,18,24}`

has seven marks and covers `1,...,18`, while the restricted exact value is `F(18)=8`.

The definition therefore becomes load-bearing beyond the smaller table.

## Verification

The provenance repository `jaredwilder/erdos-ore-findings` contains `ruler.py`, which exhaustively recomputes the values through 20 and checks the historical witnesses, and `c0.py`, which numerically locates the stationary point used above.
