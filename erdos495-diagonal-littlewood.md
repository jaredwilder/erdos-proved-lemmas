# Erdős #495 — the diagonal Littlewood stratum

Author: Jared Wilder  
Public release: 2026-09-11

## Theorem

For every real number `alpha`,

`liminf_{n->infinity} n ||n alpha||^2 = 0`.

Equivalently, Littlewood's conclusion holds for every diagonal pair

`(alpha,beta)=(alpha,alpha)`.

It also holds whenever either coordinate is rational.

## Proof

If `alpha=p/q` is rational, then for every positive multiple `n` of `q`,

`||n alpha||=0`,

so the expression vanishes exactly.

Now suppose `alpha` is irrational. Dirichlet's approximation theorem, or equivalently the theory of continued-fraction convergents, gives infinitely many positive integers `n` for which

`||n alpha|| < 1/n`.

Along this subsequence,

`n ||n alpha||^2 < 1/n -> 0`.

Since the expression is nonnegative, its liminf is zero.

For a pair `(alpha,beta)` with `alpha` rational, the full Littlewood product

`n ||n alpha|| ||n beta||`

is zero on multiples of the denominator of `alpha`; similarly if `beta` is rational.

## Golden-ratio regression

For `phi=(1+sqrt(5))/2`, Fibonacci denominators give the explicit identity

`||F_k phi||=phi^(-k)`

for the nontrivial convergent range, so

`F_k ||F_k phi||^2 -> 0`.

This directly falsifies a historical raw-ore row that tried to use bad approximability of `phi` as a diagonal counterexample.

## Scope

This is a standard restricted stratum of Littlewood's conjecture, not a solution of the general two-irrational problem. It is released here because it is a useful semantic guardrail for the Day-One corpus: diagonal badly-approximable pairs cannot be counterexamples.

## License

Apache-2.0.
