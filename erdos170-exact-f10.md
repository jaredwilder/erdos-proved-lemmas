# Erdős #170 — exact value `F(10)=6`

Author: Jared Wilder  
Public release: 2026-09-11

Let `F(N)` be the smallest size of a set

`A subset {0,1,...,N}`

such that every integer `0,...,N` occurs in the difference set `A-A`.

## Theorem

`F(10)=6`.

## Lower bound: five points are impossible

Suppose five points

`0 <= x_1 < x_2 < x_3 < x_4 < x_5 <= 10`

covered every positive difference `1,...,10`.

Five points determine exactly ten unordered positive pairwise differences. To cover all ten values `1,...,10`, these ten differences would therefore have to be distinct and equal exactly to `1,...,10`. Their sum would be

`1+2+...+10 = 55`,

which is odd.

Let the consecutive gaps be

`d_i=x_(i+1)-x_i`, `i=1,...,4`.

Summing all ten pairwise differences and collecting each gap by how many pairs span it gives

`4d_1 + 6d_2 + 6d_3 + 4d_4`,

which is even. Contradiction.

Hence `F(10)>=6`.

## Upper bound: a six-point witness

Take

`A={0,1,2,3,6,10}`.

Its positive differences contain every integer from 1 through 10:

- `1,2,3` from the initial block;
- `4=10-6`;
- `5=6-1`;
- `6=6-0`;
- `7=10-3`;
- `8=10-2`;
- `9=10-1`;
- `10=10-0`.

Therefore `F(10)<=6`.

Combining the two bounds gives `F(10)=6`.

## Scope

This is an exact finite value inside Erdős #170. It does not determine the asymptotic constant `lim F(N)/sqrt(N)` asked for by the parent problem.

Historical novelty is not claimed; the value is published here because the Day-One mine contained the lower obstruction but did not promote the matching exact value cleanly.

## License

Apache-2.0.
