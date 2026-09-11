# Erdős #930 — Pell families and a threshold obstruction for perfect-power interval products

Author: Jared Wilder. Public release: 2026-09-11.

Consider two disjoint intervals of consecutive positive integers whose combined product is a perfect power.

## Theorem 1 — infinitely many length-2 square-product pairs

For every nontrivial positive solution of

`x^2 - 24 y^2 = 1`

with `x>5`, put `a=(x-1)/2`. Then

`a(a+1)=6y^2`.

Hence the two disjoint intervals

`{2,3}` and `{a,a+1}`

have square total product:

`6 a(a+1) = (6y)^2`.

Since the Pell equation has infinitely many positive solutions, there are infinitely many such length-2 examples.

## Theorem 2 — any r=2 threshold is at least 4

The disjoint length-3 intervals

`{1,2,3}` and `{48,49,50}`

have product

`1*2*3*48*49*50 = 705600 = 840^2`.

Therefore any threshold `k` that could rule out perfect powers for **all** pairs of disjoint intervals of length at least `k` must satisfy

`k >= 4`.

A separate exact search found no square-product example of the special form `{1,2,3,4}` together with `{t,t+1,t+2,t+3}` for `t<=10^6`. That is a finite computation on that particular family, not a theorem about all length-4 interval pairs.

These statements concern the lower-threshold side of Erdős #930. Historical novelty is a separate literature question.
