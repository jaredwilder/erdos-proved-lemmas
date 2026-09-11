# Erdős #295 — exact value `k(3)=5`

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

For the canonical Erdős #295 function, let `k(N)` be the smallest `k` for which there exist distinct integers

`N <= n_1 < ... < n_k`

with

`1 = 1/n_1 + ... + 1/n_k`.

Then

> **`k(3)=5`.**

## Upper bound

The five denominators

`3,4,5,6,20`

satisfy

`1/3 + 1/4 + 1/5 + 1/6 + 1/20 = 1`.

Hence `k(3) <= 5`.

## Lower bound

Among distinct integers at least 3, the four largest possible reciprocal contributions come from `3,4,5,6`. Their sum is

`1/3 + 1/4 + 1/5 + 1/6 = 57/60 < 1`.

Therefore no four allowed denominators can sum reciprocally to 1, so `k(3) >= 5`.

Thus `k(3)=5`.

## Scope

This is an exact small-`N` slice of Erdős #295. It does not address the asymptotic question for `k(N)-(e-1)N`. Historical novelty is not claimed; the value is retained as a rigorous base case and regression theorem.

## Provenance

Recovered in the September 2026 Pass-3 estate audit as `P3-G009`.