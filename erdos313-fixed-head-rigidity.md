# Erdős #313 — fixed-head rigidity at `(2,3,p)`

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

This is a separate child theorem from the fixed-`k` finiteness result already routed for Erdős #313.

## Theorem

Suppose the relevant Egyptian-prime branch begins with primes `(2,3,p)` and the residual equation gives

`1/p + 1/m = 1/6`.

Then

`m(p-6)=6p`,

so

`p-6 | 36`.

If `p` is prime and `p>6`, the only possibility is

> **`p=7`.**

Thus the `(2,3,p)` fixed-head branch is rigid.

## Formal evidence

`jaredwilder/erdos-theorems/theorems/erdos313-campaign-001/Erdos313Head.lean` contains two Lean theorems:

- `erdos313_head_prune` — prime `p>6` with `(p-6)|36` implies `p=7`;
- `erdos313_head_m` — prime `p>6` with `m*(p-6)=6*p` implies `p=7`.

The theorem is therefore not merely a workflow label; the branch-kill has a direct formal artifact.

## Scope

This is a sharp child theorem for one fixed head. It does not classify all solutions to Erdős #313 and does not replace the separate fixed-`k` finiteness theorem.

## Provenance

Recovered as Pass-3 gold `P3-G023`; surfaced separately during the 2026-09-11 burial audit because the existing #313 compact entry referred to a different theorem.