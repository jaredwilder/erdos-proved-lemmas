# Erdős #155 — exact `k=1` Sidon monotonicity

Author: Jared Wilder  
Public release: 2026-09-11

Let `F(N)` be the maximum size of a Sidon subset of `{1,...,N}`.

## Theorem

For every `N>=1`,

`F(N+1) <= F(N)+1`.

## Proof

Take any Sidon set `A subset {1,...,N+1}`.

If `N+1 notin A`, then `A subset {1,...,N}` and `|A|<=F(N)`.

If `N+1 in A`, remove that element. The set `A\{N+1}` remains Sidon and lies in `{1,...,N}`, so

`|A|-1 <= F(N)`.

In either case `|A|<=F(N)+1`. Maximizing over `A` proves the theorem.

## Scope

This settles exactly the `k=1` case of Erdős #155. The canonical question asks whether, for every fixed `k`, the stronger inequality `F(N+k)<=F(N)+1` eventually holds. The raw campaign contained an invalid dilation argument purporting to refute that statement for larger `k`; it was correctly killed because the proposed union need not be Sidon.

## License

Apache-2.0.
