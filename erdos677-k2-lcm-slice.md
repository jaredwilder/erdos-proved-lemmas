# Erdős #677 — complete `k=2` LCM slice

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

For Erdős #677 define

`M(n,k) = lcm(n+1,...,n+k)`.

For `k=2`, consecutive integers are coprime, so

`M(n,2) = lcm(n+1,n+2) = (n+1)(n+2)`.

Therefore `M(n,2)` is strictly increasing in `n`.

Consequently, whenever `m >= n+2`,

> **`M(n,2) != M(m,2)`.**

Thus the canonical no-repeat statement is completely true in the `k=2` slice.

## Scope

The full Erdős #677 problem asks for the analogous non-repetition statement for general `k`; that problem remains separate. This result is only the exact `k=2` base case. Historical novelty is not claimed.

## Provenance

Recovered in the September 2026 Pass-3 estate audit as `P3-G025`.