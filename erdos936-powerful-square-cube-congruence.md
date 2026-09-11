# Erdős #936 — square-cube congruence restriction for powerful values

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Every odd powerful integer `m` can be written

`m=a^2 b^3`

with `b` squarefree.

Consequently, for `n>=3`:

- if `2^n-1` is powerful, then `b≡7 (mod 8)`;
- if `2^n+1` is powerful, then `b≡1 (mod 8)`.

The same mod-8 conclusion applies to `n!±1` for `n>=4`.

## Proof

Write the prime factorization of a powerful number as

`m=prod p^e`, with every `e>=2`.

Each exponent has a unique decomposition

`e=2q+3r`, with `r∈{0,1}`.

Putting the `p^q` factors into `a` and collecting the primes with `r=1` into `b` gives

`m=a^2 b^3`,

and `b` is squarefree.

If `m` is odd, then both `a` and `b` are odd. Hence

`a^2≡1 (mod 8)`

and

`b^3≡b (mod 8)`.

Therefore

`m≡b (mod 8)`.

For `n>=3`,

`2^n-1≡7 (mod 8)` and `2^n+1≡1 (mod 8)`,

which gives the stated restrictions on `b`.

For `n>=4`, `8|n!`, so `n!-1≡7` and `n!+1≡1 (mod 8)` as well.

## Scope

These are necessary congruence restrictions on the squarefree cube-part. They do not classify all powerful values of the forms above.

Historical novelty is not claimed.