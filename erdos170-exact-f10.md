# Erdős #170 — exact value `F(10)=6`

Author: Jared Wilder. Public release: 2026-09-11.

This note records the exact finite value `F(10)=6`. The broader current #170 writeup—including the corrected constant `c0≈1.560277942`, the exact table through `N=20`, parity obstruction, corrected witnesses, and the restricted/unrestricted split—is now:

[`erdos170-sparse-ruler-results.md`](erdos170-sparse-ruler-results.md)

## Exact value

Let `F(N)` be the least size of a set `A⊂{0,1,...,N}` whose positive difference set contains every integer `1,...,N`.

Then

`F(10)=6`.

### Five marks are impossible

Five marks determine exactly ten unordered positive pairwise differences. If they covered all ten values `1,...,10`, those differences would have to be exactly `1,...,10`, whose sum is 55.

If the consecutive mark gaps are `d_1,...,d_4`, the sum of all ten pairwise differences is

`4d_1+6d_2+6d_3+4d_4`,

which is even. Contradiction.

Hence `F(10)>=6`.

### Six marks suffice

The set

`{0,1,2,3,6,10}`

has positive differences containing every integer from 1 through 10, so `F(10)<=6`.

Therefore `F(10)=6`.
