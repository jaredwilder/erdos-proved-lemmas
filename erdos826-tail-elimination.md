# Erdős #826 — square-root tail elimination

Author: Jared Wilder  
Public release: 2026-09-11

Erdős #826 asks whether there are infinitely many integers `n` for which

`τ(n+k) <= C k`

for every `k>=1`, with one absolute constant `C`.

## Theorem

For every positive integer `n` and every integer `k>sqrt(n)`,

`τ(n+k) < 3k`.

Consequently the entire difficulty of Erdős #826 lies in the finite window

`1 <= k <= sqrt(n)`.

More precisely, if an absolute constant `C` works for infinitely many `n` throughout that window, then `max(C,3)` works for those same `n` for every `k>=1`.

## Proof

For every positive integer `m`, divisor pairing gives

`τ(m) <= 2 sqrt(m)`.

Now suppose `k>sqrt(n)`. Then `n<k^2`, hence

`n+k < k^2+k`.

Therefore

`τ(n+k) <= 2 sqrt(n+k) < 2 sqrt(k^2+k)`.

For every integer `k>=1`,

`2 sqrt(k^2+k) < 3k`,

because after squaring this is equivalent to

`4(k^2+k) < 9k^2`,

or `4<5k`.

Thus `τ(n+k)<3k` whenever `k>sqrt(n)`.

## Scope

This does **not** solve the canonical infinitude problem. It removes the large-`k` tail uniformly, with an absolute constant independent of `n`, and reduces the open part to a square-root-sized initial window.

The current Erdős Problems page still lists #826 as open; it records Lau's 2026 result with a bound of the form `τ(n+k) << k^C` for infinitely many `n`. Historical novelty of this elementary tail reduction is not claimed here without a specialist literature search.

## Provenance

Recovered from the Day-One MSL/Erdős ore chronology. The raw campaign contained weaker and `n`-dependent divisor-bound rows before arriving at the absolute-constant square-root tail split. This writeup re-derives the surviving statement directly from divisor pairing.

## License

Apache-2.0.
