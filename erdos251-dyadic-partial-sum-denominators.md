# Erdős #251 — exact dyadic denominators of the finite prime-weighted partial sums

**Author:** Jared Wilder  
**Public release:** 2026-09-14

## Convention

Let `p_n` denote the `n`th prime with one-based indexing, so `p_1=2, p_2=3, ...`. Define

\[
S_N=\sum_{n=1}^N \frac{p_n}{2^n}.
\]

## Theorem

For every `N>=2`, the reduced denominator of `S_N` is exactly

\[
\boxed{2^N}.
\]

For the endpoint `N=1`, `S_1=1`, so the reduced denominator is `1`.

Equivalently, if

\[
2^N S_N=\sum_{n=1}^N p_n 2^{N-n},
\]

then this integer numerator is odd for every `N>=2`.

## Proof

Modulo `2`, every summand with `n<N` vanishes because it contains a factor `2^{N-n}`. The only surviving term is the last one:

\[
\sum_{n=1}^N p_n2^{N-n}\equiv p_N\pmod 2.
\]

For `N>=2`, `p_N` is an odd prime. Hence the numerator is odd, so no factor of `2` cancels from the displayed denominator `2^N`. Therefore the reduced denominator is exactly `2^N`.

The case `N=1` is exceptional because `p_1=2`, and `2/2=1`.

## Origin-zero variant

If primes are instead indexed `p_0=2,p_1=3,...` and one defines

\[
T_N=\sum_{n=0}^{N-1}\frac{p_n}{2^n},
\]

then for `N>=2` the same parity proof gives reduced denominator exactly `2^{N-1}`.

## Scope

This is a theorem about every **finite partial sum**. It does **not** by itself prove irrationality of the infinite series

\[
\sum_{n\ge1}\frac{p_n}{2^n}.
\]

The historical campaign explicitly identified that finite-to-infinite transfer as a separate unresolved step. No novelty claim is made for this elementary invariant.