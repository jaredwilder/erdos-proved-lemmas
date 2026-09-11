# Erdős #887 — explicit family with two divisors just above the square root

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

For every integer `m>=2`, let

`N=m(m-1)(m+1)(m+2)`.

Then the two distinct divisors

`d_1=m(m+1)` and `d_2=m(m+2)`

both lie in

`(sqrt(N), sqrt(N)+2 N^(1/4))`.

## Proof

Both `d_1` and `d_2` divide `N`.

Put

`A=m(m+1)=d_1`.

Then

`N=A(A-2)`.

Since

`A^2-N=2A>0`,

we have `d_1=A>sqrt(N)`, and therefore also `d_2>d_1>sqrt(N)`.

Also

`N-(A-2)^2=2A-4>0`,

so

`sqrt(N)>A-2`.

Because `d_2=A+m`,

`d_2-sqrt(N) < (A+m)-(A-2)=m+2`.

It remains to show

`m+2 <= 2N^(1/4)`.

After raising to the fourth power, this is equivalent to

`(m+2)^4 <= 16m(m-1)(m+1)(m+2)`.

The difference between the right and left sides factors as

`(m+2)(15m^3-6m^2-28m-8)`.

The cubic is positive at `m=2` and strictly increasing for `m>=2`, so the inequality holds. Therefore

`d_2<sqrt(N)+2N^(1/4)`.

Since `d_1<d_2`, the same upper bound holds for `d_1`.

## Scope

This is an explicit structural family showing that two divisors can cluster within a fourth-root scale immediately above `sqrt(N)`. It is not by itself a refutation of any universal statement with a larger constant.

Historical novelty is not claimed.