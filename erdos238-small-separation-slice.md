# Erdős #238 — complete `c_2<2` separation slice

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

## Theorem

Fix constants `c_1>0` and `0<c_2<2`. In the frozen Erdős #238 formulation, the requested block of consecutive primes exists for all sufficiently large `x`.

## Proof

Apart from the prime 2, consecutive primes are odd. Hence any two distinct odd primes differ by an even positive integer and therefore by at least 2. Thus when `c_2<2`, the pair-separation requirement is automatic inside any block of odd primes.

The remaining requirement is only to have at least `c_1 log x` consecutive primes available below the relevant cutoff. Standard prime-counting growth gives

\[
\pi(x)\sim\frac{x}{\log x},
\]

so for fixed `c_1` this dominates `c_1\log x` for all sufficiently large `x`. Discard the initial prime 2 if necessary and take a consecutive block of the required length.

## Scope

This completely handles the elementary parameter slice `c_2<2`. It does not address the harder large-separation regime of Erdős #238.

The source novelty audit called this `APPARENTLY_UNRECORDED_ELEMENTARY`; no historical novelty is asserted here.