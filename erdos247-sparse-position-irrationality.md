# Erdős #247 — sparse-position irrationality in every integer base

**Author:** Jared Wilder  
**Recovered:** September 2026 MSL audit/final synthesis  
**Subject-home promotion:** 2026-09-11

Let

`a_1<a_2<a_3<...`

be strictly increasing positive integers and let `b>=2` be an integer base. If

`limsup a_n/n = infinity`,

then

> **`sum_{n>=1} b^(-a_n)` is irrational.**

The base-2 statement is therefore one instance of an all-integer-base theorem.

## Proof

Because the exponents are distinct, the base-`b` expansion has digit `1` exactly in positions `a_n` and `0` elsewhere; no carries occur because the occupied digit is `1<b`.

The hypothesis forces the gaps `a_(n+1)-a_n` to be unbounded. If all sufficiently late gaps were at most `G`, then `a_n<=a_1+G(n-1)`, contradicting the unbounded limsup of `a_n/n`.

A rational real has an eventually periodic expansion in every integer base. An infinite eventually periodic digit string containing infinitely many `1`s has bounded gaps between successive `1` positions. The expansion here has infinitely many `1`s and unbounded gaps, so it is not eventually periodic and the sum is irrational.

## Companion density equivalence

If

`A(N)=#{n : a_n<=N}`,

then

> `limsup a_n/n = infinity` iff `liminf A(N)/N = 0`.

One direction evaluates at `N=a_n`, where `A(a_n)=n`. Conversely, along `N_j` with `A(N_j)/N_j -> 0`, set `n_j=A(N_j)+1`; then `a_(n_j)>N_j` and `a_(n_j)/n_j -> infinity`.

## Scope and literature

Erdős #247 asks for transcendence under the sparsity hypothesis; this theorem proves irrationality only. The September audit found no exact match in targeted searches, but specialist literature review was incomplete, so historical priority remains unresolved.

Original extraction: `jaredwilder/unpublished-math-papers/erdos247-sparse-binary-irrationality/`.
