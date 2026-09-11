# Erdős #655 — the literal frozen statement is false by regular polygons

Author: Jared Wilder. Public release: 2026-09-11.

## Literal statement

Let `X={x_1,...,x_n}⊂R^2` satisfy: no circle centered at one of the `x_i` contains three other points of `X`.

The literal frozen question asks whether there is a constant `c>0` such that every sufficiently large such `X` determines at least

`(1+c)n/2`

distinct distances.

## Theorem

For every `n>=3`, the regular `n`-gon satisfies the stated circle condition and determines exactly

`floor(n/2)`

distinct distances.

Therefore the literal frozen conjecture is false for every proposed `c>0`.

## Proof

Take the vertices of a regular `n`-gon.

From any fixed vertex, chord length depends only on the cyclic separation `j`. The separations `j` and `n-j` give the same distance, and for

`1<=j<=floor(n/2)`

the chord lengths are distinct. Hence the entire configuration determines exactly

`floor(n/2)`

distinct distances.

For a fixed vertex, every non-antipodal distance occurs at exactly two other vertices, one in each cyclic direction; if `n` is even, the antipodal distance occurs once. Thus no circle centered at a vertex contains three other vertices. The configuration satisfies the literal hypothesis.

Finally,

`floor(n/2) <= n/2 < (1+c)n/2`

for every `c>0`, so the desired lower bound fails for every `n`.

## Literature / scope boundary

This counterexample is not claimed as historically new. The maintained Erdős Problems page attributes the regular-polygon observation to Zach Hunter, and current formal-conjectures material treats the literal statement as false while separating stronger general-position variants.

Accordingly this file records the exact mathematical status of the literal frozen statement; it does not claim to solve any repaired variant.