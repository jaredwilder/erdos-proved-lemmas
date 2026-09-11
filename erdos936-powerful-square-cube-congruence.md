# Erdős #936 — congruence restrictions for powerful values of `2^n±1`

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem 1 — square-cube form and mod 8

Every odd powerful integer `m` can be written

`m=a^2 b^3`

with `b` squarefree.

Consequently, for `n>=3`:

- if `2^n-1` is powerful, then `b≡7 (mod 8)`;
- if `2^n+1` is powerful, then `b≡1 (mod 8)`.

The same mod-8 conclusion applies to `n!±1` for `n>=4`.

### Proof

Write the prime factorization of a powerful number as

`m=prod p^e`, with every `e>=2`.

Each exponent has a unique decomposition

`e=2q+3r`, with `r∈{0,1}`.

Putting the `p^q` factors into `a` and collecting the primes with `r=1` into `b` gives

`m=a^2 b^3`,

and `b` is squarefree.

If `m` is odd, then both `a` and `b` are odd. Hence

`a^2≡1 (mod 8)` and `b^3≡b (mod 8)`,

so `m≡b (mod 8)`.

For `n>=3`,

`2^n-1≡7 (mod 8)` and `2^n+1≡1 (mod 8)`,

which gives the stated restrictions on `b`.

For `n>=4`, `8|n!`, so `n!-1≡7` and `n!+1≡1 (mod 8)` as well.

## Theorem 2 — exact mod-9 periodicity

For every positive integer `n`,

`9 | 2^n+1`

if and only if

`n≡3 (mod 6)`.

### Proof

The powers of 2 modulo 9 have period 6:

`2,4,8,7,5,1`.

The unique residue `-1 mod 9` is `8`, occurring exactly for exponents

`n≡3 (mod 6)`.

Hence `2^n+1` is divisible by 9 exactly in that congruence class.

## Scope

These are exact necessary congruence restrictions and a complete mod-9 criterion. They do not classify all powerful values of `2^n±1`.

Historical novelty is not claimed.