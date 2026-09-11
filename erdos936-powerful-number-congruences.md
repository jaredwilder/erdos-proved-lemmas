# Erdős #936 — square-cube form and mod-8 restrictions for odd powerful numbers

Author: Jared Wilder. Public release: 2026-09-11.

## Lemma 1 — square-cube representation

Every odd powerful integer `m` can be written

`m=a^2 b^3`

with `b` squarefree.

### Proof

Write `m=∏p^{e_p}` with every `e_p>=2`. Each exponent has a unique decomposition

`e_p=2q_p+3r_p`, with `r_p∈{0,1}`.

Put `p^{q_p}` into `a`, and put into `b` exactly the primes for which `r_p=1`. Then `b` is squarefree and `m=a^2b^3`.

## Lemma 2 — mod-8 reduction

If `m` is odd and powerful and `m=a^2b^3` as above, then

`m≡b (mod 8)`.

Indeed, odd `a` has `a^2≡1 (mod 8)` and odd `b` has `b^3≡b (mod 8)`.

## Consequences for `2^n±1`

For `n>=3`,

`2^n-1≡7 (mod 8)` and `2^n+1≡1 (mod 8)`.

Therefore, if either number is powerful and written in square-cube form with squarefree cube part `b`, then respectively

- `b≡7 (mod 8)` for `2^n-1`;
- `b≡1 (mod 8)` for `2^n+1`.

These are exact necessary structural conditions. Classification of powerful values of `2^n±1` is a separate problem.
