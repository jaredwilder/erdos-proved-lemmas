# Erdős #885 — factor-difference / square duality

Author: Jared Wilder. Public release: 2026-09-11.

For `N>=1`, let

`D(N)={|a-b| : a,b positive integers, ab=N}`.

## Theorem

For every integer `d>=0`,

`d∈D(N)`

if and only if there is an integer `s>=0` with

`s^2=d^2+4N`.

Equivalently, factor-difference questions are integral-point questions on

`s^2-d^2=4N`.

## Proof

If `N=ab` and `d=|a-b|`, then

`d^2+4N=(a-b)^2+4ab=(a+b)^2`.

Conversely, if `s^2=d^2+4N`, then `(s-d)(s+d)=4N`. Since `s` and `d` have the same parity, put

`a=(s+d)/2`, `b=(s-d)/2`.

Then `ab=N` and `|a-b|=d`.

A formal companion to this exact equivalence appears in `jaredwilder/erdos-theorems`.
