# Erdős #489 — correction: the prime-set negative witness is inadmissible and its avoiding set was misidentified

**Author:** Jared Wilder  
**Status:** exact correction / route kill  
**Parent problem:** remains open in this record

Erdős #489 asks about sets `A⊆N` satisfying

\[
|A\cap[1,x]|=o(x^{1/2}),
\]

with avoiding set

\[
B=\{n\ge1: a\nmid n\text{ for every }a\in A\}.
\]

Writing `B={b_1<b_2<...}`, the question is whether

\[
\lim_{x\to\infty}\frac1x\sum_{b_i<x}(b_{i+1}-b_i)^2
\]

always exists and is finite.

A recovered campaign row claimed an unconditional negative close by choosing `A` to be the set of primes. It asserted that `B={1}∪primes` and then used prime-gap estimates to force divergence.

That route is invalid for two independent reasons.

## 1. The prime set does not satisfy the hypothesis

For `A` equal to all primes,

\[
|A\cap[1,x]|=\pi(x)\sim \frac{x}{\log x}.
\]

Therefore

\[
\frac{\pi(x)}{x^{1/2}}\sim\frac{x^{1/2}}{\log x}\to\infty,
\]

not zero. Thus the proposed `A` is outside the canonical domain.

## 2. Its avoiding set is not `{1}∪primes`

If `n>1`, then `n` has a prime divisor `p`. Since every prime belongs to `A`, we have `p|n`, so `n` is excluded from `B`.

Hence for `A` equal to the primes,

\[
\boxed{B=\{1\}.}
\]

In particular, primes themselves are excluded because each prime is divisible by itself.

So the claimed prime-gap sequence `b_i` never arises from this `A`.

## Consequence

The archived statement

> `A=primes` gives an admissible counterexample with `B={1}∪primes`

is false twice over: the set `A` violates the sparsity premise and the associated `B` was computed incorrectly.

This correction does not decide Erdős #489. It removes one invalid negative-close route. Finite-`A` periodicity statements in the same campaign are separate mathematical objects and are unaffected by this correction.

## Provenance

The recovered route graph itself later contains the correction `B={1}`, but earlier `PROVED` summaries still preserve the invalid branch-B close. This file makes the conflict explicit on the stable public theorem/correction surface.
