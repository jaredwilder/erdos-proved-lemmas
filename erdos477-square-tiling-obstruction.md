# Erdős #477 — finite unique tiling by squares is impossible

Author: Jared Wilder. Public release: 2026-09-11.

Let

`B={k^2 : k>=0}`.

## Theorem

There is no finite set `A⊂Z` such that every integer has a unique representation

`z=a+b`, with `a∈A`, `b∈B`.

## Proof

An integer is a difference of two squares if and only if it is not congruent to `2 mod 4`.

Indeed, odd integers are differences of consecutive squares; multiples of 4 are differences `(m+1)^2-(m-1)^2`; and a square is only `0` or `1 mod 4`, so a difference of squares is never `2 mod 4`.

Suppose `A+B` had unique representations. If `a!=a'` are in `A`, then `a-a'` cannot be a difference of two squares, since otherwise

`a+b = a'+b'`

for two squares `b,b'`, contradicting uniqueness. Therefore every nonzero difference between elements of `A` must be congruent to `2 mod 4`.

But `A` cannot contain three distinct elements. If `x,y,z` are distinct, then after ordering them the two successive differences are each `2 mod 4`, while their sum — the outer difference — is `0 mod 4`, contradiction.

Hence `|A|<=2`.

Finally, if `A` is finite then `A+B` is bounded below, because `B` is nonnegative. It therefore cannot equal all of `Z`.

## Scope

This proves the square-value slice exactly. Historical novelty is not claimed.
## All integer quadratics

The [all-quadratic written proof](erdos477-all-quadratics.md) removes the finite-complement assumption and treats every `a x²+b x+c` with integer coefficients and `a≠0`. Its proof status is stated separately from the square-case Lean source.
