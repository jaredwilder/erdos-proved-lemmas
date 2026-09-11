# Erdős #681 — fourth-root witness window

Author: Jared Wilder  
Public release: 2026-09-11

Erdős #681 asks whether for all sufficiently large `n` there is a positive integer `k` such that `n+k` is composite and its least prime factor exceeds `k^2`.

## Theorem 1 — exact `k=1` slice

`k=1` is a witness if and only if `n+1` is composite.

### Proof

If `n+1` is composite, its least prime factor is at least `2`, hence is greater than `1^2`. Conversely the canonical witness condition itself requires `n+1` to be composite.

Thus every `n` with composite successor is immediately solved; any hard input must satisfy `n+1` prime.

## Theorem 2 — fourth-root search window

Every valid witness `k` satisfies

`k^4 < n+k`.

### Proof

Put `m=n+k`. Since a witness requires `m` composite, its least prime factor `p(m)` satisfies

`p(m) <= sqrt(m)`.

The witness inequality gives

`k^2 < p(m) <= sqrt(m)`.

Squaring the strict left inequality yields

`k^4 < m = n+k`.

## Consequence

For each fixed `n`, the witness search is finite: only positive integers `k` satisfying `k^4<n+k` can possibly work. Combined with Theorem 1, the genuinely nontrivial residual family is

`n+1 prime`,

with candidate `k` restricted to the fourth-root window.

This is a structural reduction, not a solution of the eventual-existence question.

## Scope and current status

The current Erdős Problems page lists #681 as open. The present theorem isolates its shifted-prime core and gives an exact necessary witness window; it does not establish that every sufficiently large shifted prime admits a witness.

Historical novelty is not claimed without a specialist literature search.

## Provenance

Recovered from the Day-One MSL/Erdős route chronology. Several historical rows confused the necessary fourth-root condition with a sufficient condition; this release retains only the direction proved above. The `k=1` equivalence also survived repeated independent checks in the chronology.

## License

Apache-2.0.
