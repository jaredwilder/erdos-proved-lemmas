# Erdős #341 — the seed `{1}` generates all odd integers

Author: Jared Wilder. Public release: 2026-09-11.

Start with the finite set `{1}`. Given

`a_1<...<a_n`,

define `a_(n+1)` to be the least integer greater than `a_n` which is not representable as

`a_i+a_j`, with `i,j<=n`.

## Theorem

Starting from `{1}`, the greedy sequence is exactly

`1,3,5,7,...`.

Consequently every successive gap equals `2`, so the gap sequence is periodic from the start.

## Proof

Suppose the current prefix is

`1,3,5,...,2m-1`.

Every pair sum is even. Conversely, every even integer from `2` through `4m-2` occurs as a pair sum: for any `1<=r<=2m-1`, choose `i,j∈{1,...,m}` with `i+j-1=r`; then

`(2i-1)+(2j-1)=2r`.

Thus every even integer greater than the current maximum `2m-1` and at most `4m-2` is represented, while the next odd integer

`2m+1`

is not represented at all.

Therefore the greedy rule chooses `2m+1` next.

Starting from `1`, induction gives the full odd sequence.

## Scope

This resolves one exact seed. The eventual-periodicity question for arbitrary finite starting sets remains separate.

Historical novelty is not claimed.