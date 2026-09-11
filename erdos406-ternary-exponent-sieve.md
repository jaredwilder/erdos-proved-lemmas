# Erdős #406 — 3-adic exponent sieve for ternary `{0,1}` digits

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Suppose every ternary digit of `2^n` is either `0` or `1`. Then

`n mod 18 ∈ {0,2,6,8}`.

More generally, modulo `3^r`, the admissible exponents form exactly `2^(r-1)` residue classes modulo

`phi(3^r)=2*3^(r-1)`.

## Proof

A residue modulo `3^r` whose first `r` ternary digits lie in `{0,1}` has the form

`epsilon_0 + epsilon_1*3 + ... + epsilon_{r-1}*3^(r-1)`.

Exactly half of the `2^r` such residues are units, namely those with `epsilon_0=1`. Since 2 is a primitive root modulo every power of 3, exponentiation by 2 bijects exponent classes modulo `phi(3^r)` with the units modulo `3^r`. Hence exactly `2^(r-1)` exponent classes survive.

For `r=3`, the surviving classes are `0,2,6,8 mod 18`.

This is an exact necessary congruence sieve. Stronger global statements require additional arguments.
