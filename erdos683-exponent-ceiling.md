# Erdős #683 — necessary ceiling on the universal exponent

Author: Jared Wilder. Public release: 2026-09-11.

Let `P(m)` denote the largest prime factor of `m`.

## Theorem

Any constant `c` satisfying the canonical inequality

`P(C(n,k)) >= min(n-k+1, k^(1+c))`

throughout its stated interior parameter range must satisfy

`c <= log_3(5/3)`.

## Proof

Use the single admissible instance

`(n,k)=(10,3)`.

Then

`C(10,3)=120`,

whose largest prime factor is `5`. Also

`n-k+1=8`.

Therefore the proposed universal inequality forces

`5 >= min(8, 3^(1+c))`.

Since `5<8`, the minimum can be at most 5 only if

`3^(1+c) <= 5`.

Taking logarithms base 3 gives

`1+c <= log_3 5`,

hence

`c <= log_3 5 - 1 = log_3(5/3)`.

## Scope and correction boundary

This is a necessary ceiling on any universal exponent `c`; it is not a proof that this ceiling is attainable. Earlier ore contained a false `(10,5)` derivation based on the incorrect value `C(10,5)=?`; that poisoned route is not used here.

Historical novelty is not claimed.