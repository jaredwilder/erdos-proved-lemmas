# Erdős #503 — exact one-dimensional isosceles-set answer

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

The largest finite subset `X⊂R` such that every three distinct points of `X` form an isosceles triangle has size exactly `3`.

Here a collinear triple is called isosceles when two of its three pairwise distances are equal.

## Lower bound

Any three equally spaced points work, for example

`{0,1,2}`.

Thus the maximum is at least `3`.

## Upper bound

Suppose four points exist:

`x_1<x_2<x_3<x_4`.

For the triple `x_1,x_2,x_3`, the only possible equality among its positive distances is

`x_2-x_1 = x_3-x_2`,

so

`x_1+x_3=2x_2`.

Likewise, for the triple `x_1,x_2,x_4`, isoscelesness forces

`x_1+x_4=2x_2`.

Therefore `x_3=x_4`, contradiction.

Hence no four-point set works, and the exact maximum is `3`.

## Scope

This is the exact one-dimensional slice only. Higher-dimensional versions are separate.

Historical novelty is not claimed.