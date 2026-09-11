# Erdős #68 — exact geometric-series reformulation

Author: Jared Wilder. Public release: 2026-09-11.

## Identity

For every integer `n>=2`,

`1/(n!-1) = sum_{j=1}^infinity (n!)^(-j)`.

More generally, for every `J>=1`,

`1/(n!-1) = sum_{j=1}^J (n!)^(-j) + (n!)^(-J)/(n!-1)`.

In particular the finite truncation has an exact positive remainder.

## Proof

Put `x=n!>1`. The geometric-series formula gives

`sum_{j=1}^infinity x^(-j) = x^(-1)/(1-x^(-1)) = 1/(x-1)`.

For the finite form,

`sum_{j=1}^J x^(-j) = (1-x^(-J))/(x-1)`,

so subtracting from `1/(x-1)` leaves

`x^(-J)/(x-1)`.

Substituting `x=n!` proves both identities.

## Scope

This is an exact reformulation and remainder identity. It does not settle the surrounding irrationality problem.

Historical novelty is not claimed.