# Erdős #653 — exact value `g(4)=3`

Author: Jared Wilder. Public release: 2026-09-11.

For a planar configuration `X={x_1,...,x_n}`, let

`R(x_i)=#{ |x_j-x_i| : j!=i }`,

and let `g(n)` be the maximum possible number of distinct values among the `R(x_i)`.

## Theorem

`g(4)=3`.

## Upper bound

With four points, each vertex sees only three other points, so

`1<=R(x_i)<=3`.

Therefore at most the three values `1,2,3` can occur, and

`g(4)<=3`.

## Matching construction

Take

`O=(0,0)`,

`A=(1,0)`,

`B=(1/2, sqrt(3)/2)`,

`C=(-sqrt(3)/2, 1/2)`.

Thus `A,B,C` lie on the unit circle about `O`, at angles `0`, `60` and `150` degrees.

The relevant distances are

`OA=OB=OC=AB=1`,

`BC=sqrt(2)`,

`AC=sqrt(2+sqrt(3))`.

Hence

- `R(O)=1`;
- `R(A)=2`;
- `R(B)=2`;
- `R(C)=3`.

The configuration therefore realizes the three distinct values

`{1,2,3}`.

So `g(4)>=3`, and together with the trivial ceiling,

`g(4)=3`.

## Scope / correction boundary

This exact four-point result does not imply an asymptotic upper bound on `g(n)`. A separate Pass-6 paragraph incorrectly transplanted the regular-polygon chord count from the geometry of Erdős #655 into #653; that semantic error is recorded in Semantic Court 13.

The asymptotic #653 problem remains open. Historical novelty is not claimed.