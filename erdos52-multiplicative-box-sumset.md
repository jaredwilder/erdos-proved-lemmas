# Erdős #52 — a multiplicative box with an almost-maximal sumset

Author: Jared Wilder  
Public release: 2026-09-11

Let

`A_N = {2^i 3^j : 0 <= i,j < N}`.

## Theorem

For every integer `N>=2`,

`|A_N + A_N| >= C(N,2)^2`,

while

`|A_N A_N| = (2N-1)^2`.

Since `|A_N|=N^2`, the additive lower bound is

`|A_N+A_N| >= N^2(N-1)^2/4 = (1/4+o(1))|A_N|^2`.

Thus this natural multiplicative-box family has quadratic-size multiplicative growth but asymptotically maximal-order additive growth. It cannot serve as a counterexample vehicle for the Erdős–Szemerédi sum-product phenomenon.

## Proof of the additive bound

Restrict to sums

`2^i 3^j + 2^k 3^ell`

with

`0 <= i < k < N`, `0 <= j < ell < N`.

There are exactly `C(N,2)^2` such quadruples. Factor a restricted sum as

`2^i 3^j (1 + 2^(k-i) 3^(ell-j))`.

Because `k-i>=1`, the parenthesized factor is odd. Because `ell-j>=1`, it is `1 mod 3`. Hence the sum determines

`v_2(sum)=i`, `v_3(sum)=j`.

After dividing by `2^i3^j` and subtracting one, the remaining integer is

`2^(k-i) 3^(ell-j)`.

Unique factorization therefore recovers `k-i` and `ell-j`, hence `k` and `ell`. The restricted-sum map is injective, proving

`|A_N+A_N| >= C(N,2)^2`.

## Product set

Multiplication adds exponent coordinates:

`A_N A_N = {2^a 3^b : 0 <= a,b <= 2N-2}`.

Every such pair occurs, and unique factorization makes the representation of the product value unique in exponent coordinates. Therefore

`|A_NA_N|=(2N-1)^2`.

## Scope

This is a theorem about one explicit structured family, not a solution of the general sum-product conjecture. Historical novelty of the exact bound is not claimed without a specialist prior-art search.

## Provenance

Recovered from the Day-One MSL/Erdős ore. The original route carried a weaker logarithmically-lost lower bound. Release-Day reconstruction exposed the exact valuation-decoding injection above and strengthened the result to `C(N,2)^2`.

## License

Apache-2.0.
