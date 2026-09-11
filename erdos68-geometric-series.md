# Erdős #68 — exact geometric-series and factorial-minus-one identities

Author: Jared Wilder. Public release: 2026-09-11.

## 1. Geometric-series reformulation

For every integer `n>=2`,

`1/(n!-1) = sum_{j=1}^infinity (n!)^(-j)`.

More generally, for every `J>=1`,

`1/(n!-1) = sum_{j=1}^J (n!)^(-j) + (n!)^(-J)/(n!-1)`.

Thus every finite truncation has an exact positive remainder.

### Proof

Put `x=n!>1`. The geometric-series formula gives

`sum_{j=1}^infinity x^(-j) = x^(-1)/(1-x^(-1)) = 1/(x-1)`.

The finite geometric formula leaves remainder `x^(-J)/(x-1)`.

## 2. Exact gcd reduction

For integers `2<=n<m`, put

`P_(n,m)=prod_{j=n+1}^m j`.

Then

`gcd(n!-1,m!-1) = gcd(n!-1, P_(n,m)-1)`.

### Proof

Since

`m! = n! P_(n,m)`

and `n!≡1 (mod n!-1)`, one has

`m!-1 ≡ P_(n,m)-1 (mod n!-1)`.

Taking gcds with `n!-1` gives the identity.

## Correction record

A Pass-6 extraction claimed the stronger statement

`gcd(n!-1,m!-1)=1` for all `2<=n<m`.

That statement is false. For example,

`4!-1=23`

and

`8!-1=40319=23*1753`,

so

`gcd(4!-1,8!-1)=23`.

The failed proof correctly observed that any prime divisor of `n!-1` exceeds `n`, but incorrectly inferred that such a prime can never divide a later factorial-minus-one value.

## Scope

The identities above do not settle the surrounding irrationality problem. Historical novelty is not claimed.