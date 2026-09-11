# Erdős #17 — infinitude of cluster primes would imply Maillet's prime-difference conjecture

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Status:** exact hardness reduction; targeted audit found no tracker match; specialist priority check still required

A prime `p` is a **cluster prime** in the frozen Erdős #17 formulation when every even integer

`2 <= n <= p-3`

can be represented as

`n = q_1 - q_2`

for primes `q_1,q_2 <= p`.

Erdős #17 asks whether there are infinitely many cluster primes.

## Theorem

If there are infinitely many cluster primes, then **every positive even integer is the difference of two primes**.

Equivalently, an affirmative answer to Erdős #17 implies the classical prime-difference conjecture usually associated with Maillet.

## Proof

Fix any positive even integer `N`.

If there are infinitely many cluster primes, they are unbounded. Choose a cluster prime `p` with

`p >= N+3`.

Then

`2 <= N <= p-3`.

By the defining property of a cluster prime there exist primes `q_1,q_2 <= p` such that

`N = q_1-q_2`.

Since `N` was an arbitrary positive even integer, every positive even integer is a difference of two primes.

## What this does and does not say

This is a **hardness reduction**, not a proof of either conjecture.

An earlier campaign route incorrectly claimed that infinitely many cluster primes would force infinitely many twin-prime pairs by looking only at the `N=2` clause. That inference is false: the same fixed pair `5-3=2` can witness the `N=2` condition for arbitrarily large cluster primes. The universal Maillet consequence above survives because for each fixed even `N` we choose a cluster prime with `p>=N+3` and use the full defining interval.

## Novelty boundary

The estate's targeted novelty audit classified this implication as `APPARENTLY_UNRECORDED_REDUCTION`, with medium confidence and explicit specialist-check language. No global historical priority claim is made here.

## License

Apache-2.0.
