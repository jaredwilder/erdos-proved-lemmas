# Erdős #486 — summable forbidden mass gives natural density

Author: Jared Wilder  
Public release: 2026-09-11

For each positive integer `n`, let `X_n` be a set of residue classes modulo `n`. A positive integer `m` survives when its residue avoids `X_n` for every activated modulus `n<m`. Let `B` be the set of survivors.

## Theorem

If

`sum_{n>=1} |X_n|/n < infinity`,

then `B` has an ordinary natural density. Consequently it has logarithmic density.

## Proof

Let `B_N` impose only restrictions with `n<=N`. Finitely many congruence restrictions with finite activation thresholds make `B_N` eventually periodic, so it has a natural density `delta_N`. The sets decrease with `N`, hence `delta_N` decreases to some `delta_*`.

Up to `x`, only moduli `N<n<x` can remove points of `B_N` that survive the first `N` restrictions. A modulus `n` removes at most

`|X_n|(x/n+1)`

integers up to `x`. Thus

`|(B_N\B) cap [1,x]|/x`

is at most

`sum_{N<n<x}|X_n|/n + (1/x) sum_{N<n<x}|X_n|`.

The first term is bounded by the convergent tail. For the second, convergence of `sum |X_n|/n` and Kronecker's lemma give

`(1/x) sum_{n<=x}|X_n| -> 0`.

Therefore

`delta_N - sum_{n>N}|X_n|/n <= lower_density(B) <= upper_density(B) <= delta_N`.

Letting `N->infinity` forces both densities to equal `delta_*`.

## Scope

The activation rule `n<m` is part of the theorem. This proves a strong summable-mass slice of Erdős #486, not the unrestricted parent problem.

Historical novelty is not claimed without a specialist sieve/Davenport–Erdős literature search.

## License

Apache-2.0.
