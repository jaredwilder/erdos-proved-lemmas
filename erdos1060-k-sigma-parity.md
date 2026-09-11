# Erdős #1060 — parity structure of `k sigma(k)`

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

Let `sigma(k)` be the sum of positive divisors of `k`.

## Parity theorem

For every positive integer `k`,

> **`k sigma(k)` is odd if and only if `k` is an odd square.**

Indeed `k sigma(k)` is odd exactly when both `k` and `sigma(k)` are odd. The classical parity characterization says `sigma(k)` is odd exactly when `k` is a square or twice a square. Since `k` itself must already be odd, only the odd-square case survives. The converse is immediate.

## Explicit noninjectivity

The map

`k -> k sigma(k)`

is not injective:

`sigma(12)=28`, `sigma(14)=24`, and therefore

`12 sigma(12)=14 sigma(14)=336`.

## Scope

These are structural constraints on Erdős #1060. They do not bound the global representation multiplicity requested by the parent problem. Historical novelty is not claimed.

## Provenance

Compact routing of the public extraction in `jaredwilder/unpublished-math-papers/erdos1060-k-sigma-parity/`.